"""
Regenerate the navigation footer of every curriculum page.

Every topic, case study, and level index ends with a block delimited by
`<!-- nav:start -->` / `<!-- nav:end -->` that links to the previous page, the
next page, and the parent index. Concept topics additionally list the case
studies that apply them, derived from the links those case studies contain.

The reading order comes straight from the folder names, so after adding or
renumbering a topic you only need to re-run:

    python scripts/update_nav.py

Use `--check` (as CI does) to fail when any footer is out of date.
The script is idempotent: running it twice changes nothing the second time.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BONUS = "Bonus-Real-World-Architectures"
START, END = "<!-- nav:start -->", "<!-- nav:end -->"

NAV_BLOCK_RE = re.compile(
    r"\n*(?:^---[ \t]*\n+)?" + re.escape(START) + r".*?" + re.escape(END) + r"\s*\Z",
    re.S | re.M,
)
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+)\s*\)")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)

# Hand-written navigation lines from before this script existed. They are
# removed from the tail of a file so the generated block is the only one.
LEGACY_NAV = [
    re.compile(
        r"^- (?:Previous|Next|Next Level): \[[^\]]+\]\([^)]+\)"
        r"(?: · (?:Previous|Next|Next Level): \[[^\]]+\]\([^)]+\))?"
        r"(?: · Back to \[[^\]]+\]\([^)]+\))?"
        r"(?: [—-] .*)?\s*$"
    ),
    re.compile(r"^(?:\*\*)?⬅️.*\]\([^)]+\).*$"),
    re.compile(r"^\*← .*\]\([^)]+\).*→\*\s*$"),
    re.compile(r"^\*More designs: \[[^\]]+\]\([^)]+\)\*\s*$"),
]
BACK_RELATED_RE = re.compile(
    r"^\[← Back to all real-world architectures\]\([^)]+\)(?: · Related: (.+?))?\s*$"
)
ORPHAN_LABEL_RE = re.compile(r"^\*\*(?:See also|Related designs):?\*\*:?\s*$")
TAIL_WINDOW = 20      # legacy nav lines only ever lived at the end of a file
MAX_APPLIED = 8       # cap on the "See it applied in" list


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    """Write with LF endings, retrying briefly: on Windows an indexer or virus
    scanner can hold a just-modified file open for a moment."""
    for attempt in range(10):
        try:
            path.write_text(text, encoding="utf-8", newline="\n")
            return
        except OSError:
            if attempt == 9:
                raise
            time.sleep(0.2 * (attempt + 1))


def title(path: Path) -> str:
    """The page's H1 without any leading emoji."""
    match = H1_RE.search(read(path))
    raw = match.group(1) if match else path.parent.name
    return re.sub(r"^[^\w(\"']+", "", raw).strip()


def case_label(path: Path) -> str:
    """'07 · Instagram' from '# Design Instagram' in folder 07-Instagram."""
    name = re.sub(r"^Design\s+(?:an?\s+|the\s+)?", "", title(path))
    return f"{path.parent.name[:2]} · {name}"


def rel(target: Path, source: Path) -> str:
    return os.path.relpath(target, source.parent).replace(os.sep, "/")


def link(label: str, target: Path, source: Path) -> str:
    return f"[{label}]({rel(target, source)})"


def numbered_children(folder: Path) -> list[Path]:
    return sorted(
        child / "README.md"
        for child in folder.iterdir()
        if child.is_dir() and re.match(r"\d\d-", child.name) and (child / "README.md").is_file()
    )


def strip_generated(text: str) -> str:
    return NAV_BLOCK_RE.sub("", text).rstrip("\n")


def strip_legacy(text: str) -> str:
    """Remove hand-written nav lines from the end of a page (see LEGACY_NAV)."""
    lines = text.split("\n")
    cut = max(0, len(lines) - TAIL_WINDOW)
    head, tail = lines[:cut], lines[cut:]

    cleaned: list[str] = []
    for line in tail:
        back = BACK_RELATED_RE.match(line)
        if back:
            if back.group(1):
                cleaned.append(f"**Related:** {back.group(1)}")
            continue
        if any(pattern.match(line) for pattern in LEGACY_NAV):
            continue
        cleaned.append(line)

    lines = head + cleaned
    # Drop separators and labels that the removals left dangling at the end.
    while lines and (
        not lines[-1].strip() or lines[-1].strip() == "---" or ORPHAN_LABEL_RE.match(lines[-1])
    ):
        lines.pop()
    return "\n".join(lines)


def applied_index(concepts: list[Path], cases: list[Path]) -> dict[Path, list[Path]]:
    """Map each concept topic to the case studies that link to it."""
    concept_set = {path.resolve() for path in concepts}
    index: dict[Path, list[tuple[int, Path]]] = {}
    for case in cases:
        body = strip_generated(read(case))
        header = "\n".join(body.split("\n")[:16])
        primary = set()
        for scope, text in (("header", header), ("body", body)):
            for target in LINK_RE.findall(text):
                if target.startswith(("http", "#", "mailto")):
                    continue
                resolved = (case.parent / target.split("#")[0]).resolve()
                if resolved in concept_set:
                    if scope == "header":
                        primary.add(resolved)
                    index.setdefault(resolved, [])
                    if all(existing != case for _, existing in index[resolved]):
                        index[resolved].append((0 if resolved in primary else 1, case))
    # Designs that name the topic in their "Builds on" header come first.
    return {
        concept: [case for _, case in sorted(entries, key=lambda e: (e[0], e[1].parent.name))]
        for concept, entries in index.items()
    }


def nav_line(prev: str | None, home: str | None, nxt: str | None) -> str:
    return " · ".join(part for part in (prev, home, nxt) if part)


def build_blocks() -> dict[Path, str]:
    """Compute the nav block for every page that should have one."""
    home = ROOT / "README.md"
    levels = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"Level-\d\d-", p.name))
    bonus_dir = ROOT / BONUS
    bonus_index = bonus_dir / "README.md"
    cases = numbered_children(bonus_dir)
    topics_by_level = {level: numbered_children(level) for level in levels}
    concepts = [topic for level in levels for topic in topics_by_level[level]]
    applied = applied_index(concepts, cases)

    blocks: dict[Path, str] = {}

    for i, level in enumerate(levels):
        index = level / "README.md"
        topics = topics_by_level[level]
        next_index = levels[i + 1] / "README.md" if i + 1 < len(levels) else bonus_index
        next_label = title(next_index) if next_index != bonus_index else "Bonus — Real-World System Designs"

        # Level index page.
        if i == 0:
            prev = f"⬅️ **Previous:** {link('Curriculum home', home, index)}"
            mid = None
        else:
            prev_index = levels[i - 1] / "README.md"
            prev = f"⬅️ **Previous level:** {link(title(prev_index), prev_index, index)}"
            mid = f"🏠 {link('Curriculum home', home, index)}"
        start = f"➡️ **Start this level:** {link(title(topics[0]), topics[0], index)}" if topics else None
        blocks[index] = nav_line(prev, mid, start)

        # Topics inside the level.
        for j, topic in enumerate(topics):
            if j == 0:
                prev = f"⬅️ **Previous:** {link(title(index) + ' (overview)', index, topic)}"
                mid = None
            else:
                prev = f"⬅️ **Previous:** {link(title(topics[j - 1]), topics[j - 1], topic)}"
                mid = f"🏠 {link(title(index), index, topic)}"
            if j + 1 < len(topics):
                nxt = f"➡️ **Next:** {link(title(topics[j + 1]), topics[j + 1], topic)}"
            else:
                nxt = f"➡️ **Next:** {link(next_label, next_index, topic)}"
            block = nav_line(prev, mid, nxt)

            # Skip designs the topic's own text already links to.
            own_links = {
                (topic.parent / target.split("#")[0]).resolve()
                for target in LINK_RE.findall(strip_generated(read(topic)))
                if not target.startswith(("http", "#", "mailto"))
            }
            designs = [case for case in applied.get(topic.resolve(), []) if case.resolve() not in own_links]
            if designs:
                shown = " · ".join(link(case_label(case), case, topic) for case in designs[:MAX_APPLIED])
                extra = len(designs) - MAX_APPLIED
                if extra > 0:
                    shown += f" · …and {extra} more in the {link('designs index', bonus_index, topic)}"
                block += f"\n\n🧩 **See it applied in:** {shown}"
            blocks[topic] = block

    # Bonus index and case studies.
    last_level_index = levels[-1] / "README.md"
    blocks[bonus_index] = nav_line(
        f"⬅️ **Previous:** {link(title(last_level_index), last_level_index, bonus_index)}",
        f"🏠 {link('Curriculum home', home, bonus_index)}",
        f"➡️ **Start:** {link(case_label(cases[0]), cases[0], bonus_index)}" if cases else None,
    )
    for k, case in enumerate(cases):
        if k == 0:
            prev = f"⬅️ **Previous:** {link('All designs (overview)', bonus_index, case)}"
            mid = None
        else:
            prev = f"⬅️ **Previous:** {link(case_label(cases[k - 1]), cases[k - 1], case)}"
            mid = f"🏠 {link('All designs', bonus_index, case)}"
        if k + 1 < len(cases):
            nxt = f"➡️ **Next:** {link(case_label(cases[k + 1]), cases[k + 1], case)}"
        else:
            nxt = f"🏁 **You finished the last design** — back to the {link('curriculum home', home, case)}"
        blocks[case] = nav_line(prev, mid, nxt)

    return blocks


def render(path: Path, block: str) -> str:
    body = strip_legacy(strip_generated(read(path)))
    return f"{body}\n\n---\n\n{START}\n\n{block}\n\n{END}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="report stale footers and exit 1 without writing")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    stale: list[Path] = []
    blocks = build_blocks()
    for path, block in sorted(blocks.items()):
        new_text = render(path, block)
        if new_text != read(path):
            stale.append(path)
            if not args.check:
                write(path, new_text)

    verb = "out of date" if args.check else "updated"
    print(f"nav footers: {len(blocks)} pages, {len(stale)} {verb}")
    for path in stale[:200]:
        print(f"   {path.relative_to(ROOT).as_posix()}")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
