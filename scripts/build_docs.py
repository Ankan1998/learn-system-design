"""
Stage the curriculum markdown into a MkDocs-friendly `docs/` tree.

The repo stores each topic as  Level-XX-Name/NN-Topic/README.md
MkDocs reads much better as     Level-XX-Name/NN-Topic.md
so every topic folder is flattened to a single page. Because that moves files,
every internal link is re-resolved and rewritten to the new layout.

Run:  python scripts/build_docs.py
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Standalone pages that live at the repo root.
ROOT_PAGES = {
    "README.md": "index.md",
    "INTERVIEW_PLAYBOOK.md": "INTERVIEW_PLAYBOOK.md",
    "GLOSSARY.md": "GLOSSARY.md",
}

# Order of the top-level sections in the sidebar.
SECTION_ORDER = [
    "Level-00-Foundations",
    "Level-01-Building-Blocks",
    "Level-02-Data-Layer",
    "Level-03-Communication",
    "Level-04-Distributed-Systems",
    "Level-05-Architecture-Patterns",
    "Level-06-Scale-and-Reliability",
    "Level-07-Big-Data-and-Specialized",
    "Bonus-Real-World-Architectures",
]

LINK_RE = re.compile(r"(!?\[[^\]]*\])\(\s*([^)\s]+)\s*\)")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "data:")


def first_h1(path: Path) -> str | None:
    """Pull the page title out of the first markdown H1."""
    try:
        match = H1_RE.search(path.read_text(encoding="utf-8"))
    except OSError:
        return None
    return match.group(1).strip() if match else None


def build_mapping() -> dict[str, str]:
    """Map every source markdown path -> its staged path (both repo-relative, posix)."""
    mapping: dict[str, str] = {}

    for src_name, dest_name in ROOT_PAGES.items():
        if (ROOT / src_name).is_file():
            mapping[src_name] = dest_name

    for section in SECTION_ORDER:
        section_dir = ROOT / section
        if not section_dir.is_dir():
            print(f"  ! section missing, skipping: {section}")
            continue

        # The section's own landing page.
        if (section_dir / "README.md").is_file():
            mapping[f"{section}/README.md"] = f"{section}/index.md"

        # Each topic folder collapses into one page.
        for topic_dir in sorted(p for p in section_dir.iterdir() if p.is_dir()):
            readme = topic_dir / "README.md"
            if readme.is_file():
                mapping[f"{section}/{topic_dir.name}/README.md"] = f"{section}/{topic_dir.name}.md"

    return mapping


def rewrite_links(text: str, src_rel: str, dest_rel: str, mapping: dict[str, str]) -> tuple[str, list[str]]:
    """Re-point every internal link so it still resolves after the flattening."""
    src_dir = os.path.dirname(src_rel)
    dest_dir = os.path.dirname(dest_rel)
    unresolved: list[str] = []

    def replace(match: re.Match) -> str:
        label, target = match.group(1), match.group(2)

        if target.startswith(EXTERNAL_PREFIXES) or target.startswith("<"):
            return match.group(0)

        raw, sep, anchor = target.partition("#")
        if not raw:
            return match.group(0)

        # Directory-style links (".../01-Topic/") point at that folder's README.
        candidate = raw[:-1] if raw.endswith("/") else raw
        resolved = os.path.normpath(os.path.join(src_dir, candidate)).replace(os.sep, "/")

        keys = [resolved]
        if not resolved.endswith(".md"):
            keys.append(f"{resolved}/README.md")

        for key in keys:
            if key in mapping:
                new_path = os.path.relpath(mapping[key], dest_dir or ".").replace(os.sep, "/")
                return f"{label}({new_path}{sep}{anchor})"

        # Non-markdown assets (images etc.) are copied verbatim, so leave them alone.
        if not raw.endswith(".md") and not raw.endswith("/"):
            return match.group(0)

        unresolved.append(target)
        return match.group(0)

    return LINK_RE.sub(replace, text), unresolved


def write_pages_file(path: Path, title: str | None, nav: list[str]) -> None:
    lines: list[str] = []
    if title:
        lines.append(f'title: "{title}"')
    if nav:
        lines.append("nav:")
        lines.extend(f"  - {entry}" for entry in nav)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    mapping = build_mapping()
    print(f"Staging {len(mapping)} markdown pages -> docs/")

    all_unresolved: list[tuple[str, str]] = []

    for src_rel, dest_rel in mapping.items():
        text = (ROOT / src_rel).read_text(encoding="utf-8")
        text, unresolved = rewrite_links(text, src_rel, dest_rel, mapping)
        all_unresolved.extend((src_rel, link) for link in unresolved)

        dest_path = DOCS / dest_rel
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(text, encoding="utf-8")

    # Sidebar ordering + human-readable section titles.
    write_pages_file(
        DOCS / ".pages",
        title=None,
        nav=["index.md", "INTERVIEW_PLAYBOOK.md", *SECTION_ORDER, "GLOSSARY.md"],
    )

    for section in SECTION_ORDER:
        section_dir = DOCS / section
        if not section_dir.is_dir():
            continue
        pages = sorted(p.name for p in section_dir.glob("*.md") if p.name != "index.md")
        nav = (["index.md"] if (section_dir / "index.md").is_file() else []) + pages
        title = first_h1(section_dir / "index.md") or section.replace("-", " ")
        write_pages_file(section_dir / ".pages", title=title, nav=nav)

    # Static extras (custom CSS, images) ride along untouched.
    assets = ROOT / "site-assets"
    if assets.is_dir():
        for item in assets.iterdir():
            target = DOCS / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)
        print(f"Copied static assets from {assets.name}/")

    if all_unresolved:
        print(f"\n!! {len(all_unresolved)} link(s) could not be remapped:")
        for src, link in all_unresolved[:40]:
            print(f"   {src} -> {link}")
        return 1

    print(f"OK: {len(mapping)} pages staged, all internal links remapped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
