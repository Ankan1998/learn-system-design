"""
Validate the curriculum's markdown: links, Mermaid diagrams, metadata, counts.

    python scripts/verify.py

Exits non-zero when anything fails, so it can gate CI. Every check exists
because the mistake it catches has actually happened in this repository:

  * broken relative links after folders were added or renamed
  * Mermaid diagrams that silently render as nothing (`style` inside a
    sequenceDiagram, `;` in a sequence message, a literal backslash-n in a
    label, an unquoted parenthesis in a flowchart label)
  * pastel `fill:` colours without a text `color:` (unreadable in dark mode)
  * link labels that name the wrong level ("Level 03 - Caching" -> Level 1)
  * topic headers whose Level/Topic numbers disagree with their folder
  * "N topics / N designs" counts that went stale after new content landed
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BONUS = "Bonus-Real-World-Architectures"
SKIP = {".git", ".venv", "venv", "docs", "site", "node_modules", "__pycache__", ".claude"}

LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(\s*([^)\s]+)\s*\)")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)
TOPIC_RE = re.compile(r"^Level-(\d\d)-[^/]+/(\d\d)-[^/]+/README\.md$")
CASE_RE = re.compile(rf"^{BONUS}/(\d\d)-[^/]+/README\.md$")
UNQUOTED_PAREN_LABEL_RE = re.compile(r"\[(?![\"'(/\\])([^\[\]\"]*\([^\[\]\"]*)\]")
EXTERNAL = ("http://", "https://", "mailto:", "tel:", "#")


def collect() -> dict[str, str]:
    pages: dict[str, str] = {}
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for name in files:
            if name.endswith(".md"):
                path = Path(folder) / name
                pages[path.relative_to(ROOT).as_posix()] = path.read_text(encoding="utf-8")
    return dict(sorted(pages.items()))


def diagram_kind(body: str) -> str:
    for line in body.splitlines():
        if line.strip():
            return line.split()[0]
    return "?"


def check_links(pages: dict[str, str], problems: list[str]) -> int:
    checked = 0
    for page, text in pages.items():
        for image, label, target in LINK_RE.findall(text):
            if target.startswith(EXTERNAL):
                continue
            checked += 1
            resolved = os.path.normpath(os.path.join(os.path.dirname(page), target.split("#")[0]))
            if not (ROOT / resolved).exists():
                problems.append(f"broken link      {page}: [{label}]({target})")
                continue
            if image:
                continue
            resolved = resolved.replace(os.sep, "/")
            said = re.search(r"Level[ -]?0?(\d)\b", label)
            actual = re.search(r"Level-0(\d)-", resolved)
            if said and actual and said.group(1) != actual.group(1):
                problems.append(f"wrong level name {page}: [{label}] points at Level {actual.group(1)}")
    return checked


def check_mermaid(pages: dict[str, str], problems: list[str]) -> Counter:
    kinds: Counter = Counter()
    for page, text in pages.items():
        blocks = MERMAID_RE.findall(text)
        if len(blocks) != text.count("```mermaid"):
            problems.append(f"unclosed mermaid {page}")
        if len(re.findall(r"^\s*```", text, re.M)) % 2:
            problems.append(f"odd code fences  {page}")
        for body in blocks:
            kind = diagram_kind(body)
            kinds[kind] += 1
            if "\\n" in body:
                problems.append(f"literal \\n       {page}: use <br/> for line breaks in {kind} labels")
            for raw in body.splitlines():
                line = raw.strip()
                if not line or line.startswith("%%"):
                    continue
                if kind == "sequenceDiagram":
                    if re.match(r"(style|classDef|class)\b", line):
                        problems.append(f"style in seq     {page}: `{line[:60]}` is not valid in a sequenceDiagram")
                    if ";" in line and re.search(r"-[->x)]|^Note\b", line):
                        problems.append(f"; in seq message {page}: `{line[:60]}` (a semicolon ends the statement)")
                elif kind in ("flowchart", "graph"):
                    if re.match(r"(style|classDef)\b", line) and "fill:" in line and "color:" not in line:
                        problems.append(f"fill w/o color   {page}: `{line[:60]}` is unreadable in dark mode")
                    if not re.match(r"(style|classDef|class|linkStyle|click)\b", line):
                        hit = UNQUOTED_PAREN_LABEL_RE.search(line)
                        if hit:
                            problems.append(f"unquoted ( in [] {page}: `[{hit.group(1)[:50]}]` needs double quotes")
    return kinds


def check_metadata(pages: dict[str, str], problems: list[str]) -> tuple[int, int]:
    topics = [p for p in pages if TOPIC_RE.match(p)]
    cases = [p for p in pages if CASE_RE.match(p)]

    for page in topics:
        level, topic = (int(n) for n in TOPIC_RE.match(page).groups())
        head = "\n".join(pages[page].split("\n")[:12])
        stated = re.search(r"\*\*Level:\*\*\s*(\d+)\s*·\s*\*\*Topic:\*\*\s*(\d+)", head)
        if not stated:
            problems.append(f"no Level/Topic   {page}")
        elif (int(stated.group(1)), int(stated.group(2))) != (level, topic):
            problems.append(f"wrong Level/Topic {page}: header says {stated.group(1)}.{stated.group(2)}")

    for page in cases:
        numbers = [int(n) for n in re.findall(r"^## +(\d+)\.", pages[page], re.M)]
        missing = [n for n in range(1, 12) if n not in numbers]
        if missing:
            problems.append(f"missing sections {page}: {missing}")
        head = "\n".join(pages[page].split("\n")[:14])
        if "**Difficulty:**" not in head or "**Builds on:**" not in head:
            problems.append(f"no Difficulty/Builds-on header {page}")

    # Counts quoted in the index pages must match what is actually on disk.
    expectations = [
        ("README.md", r"Topics-(\d+)-", len(topics), "topic badge"),
        ("README.md", r"Designs-(\d+)-", len(cases), "design badge"),
        ("README.md", r"Bonus — (\d+) Real-World", len(cases), "bonus heading/diagram"),
        (f"{BONUS}/README.md", r"Bonus — (\d+) Real-World", len(cases), "bonus title"),
        (f"{BONUS}/README.md", r"The (\d+) designs", len(cases), "bonus section heading"),
        (f"{BONUS}/README.md", r"Finished all (\d+)", len(cases), "bonus closing line"),
    ]
    for page, pattern, actual, what in expectations:
        for found in re.findall(pattern, pages.get(page, "")):
            if int(found) != actual:
                problems.append(f"stale count      {page}: {what} says {found}, there are {actual}")

    # Every topic and design must be reachable from the main index.
    index = pages.get("README.md", "")
    for page in topics + cases:
        folder = page.rsplit("/", 1)[0]
        if folder not in index:
            problems.append(f"not in main index {page}")

    return len(topics), len(cases)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    pages = collect()
    problems: list[str] = []
    links = check_links(pages, problems)
    kinds = check_mermaid(pages, problems)
    topics, cases = check_metadata(pages, problems)

    print(f"Markdown files:    {len(pages)}  ({topics} topics, {cases} case studies)")
    print(f"Internal links:    {links}")
    print(f"Mermaid diagrams:  {sum(kinds.values())}  {dict(kinds.most_common())}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        print("\nRESULT: ISSUES FOUND")
        return 1
    print("\nRESULT: ALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
