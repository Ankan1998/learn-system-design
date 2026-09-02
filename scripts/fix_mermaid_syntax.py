"""
Repair Mermaid syntax errors in the curriculum markdown.

Two classes of bug were introduced when the content was authored:

  1. `style X fill:...` / `classDef` / `class` statements inside a
     `sequenceDiagram`. Those are flowchart-only directives and make Mermaid
     reject the whole diagram (so it renders as nothing, on GitHub too).

  2. Flowchart node labels containing parentheses without quotes, e.g.
     `S3[Service C<br/>(internal RL optional)]`. The `(` terminates the label
     early. Quoting the label fixes it: `S3["Service C<br/>(internal RL optional)"]`.

Edits the source README.md files in place. Run:  python scripts/fix_mermaid_syntax.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
STYLE_LINE_RE = re.compile(r"^[ \t]*(?:style|classDef|class)\b.*$", re.MULTILINE)

# NODE[label] where the label has a paren, does not already start with a quote
# or a paren (so cylinders `[(` and stadiums stay untouched), and has no nested
# brackets. Group 1 is the label text.
UNQUOTED_LABEL_RE = re.compile(r"\[(?![\"'(])([^\[\]\"]*\([^\[\]\"]*)\]")

SKIP_DIRS = {".git", ".venv", "venv", "site", "docs", "node_modules", "__pycache__"}


def is_sequence_diagram(body: str) -> bool:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.startswith("sequenceDiagram")
    return False


def is_flowchart(body: str) -> bool:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.startswith(("flowchart", "graph"))
    return False


def fix_body(body: str, stats: dict[str, int]) -> str:
    if is_sequence_diagram(body):
        cleaned, removed = STYLE_LINE_RE.subn("", body)
        if removed:
            stats["style_lines_removed"] += removed
            # Collapse the blank lines the removal leaves behind.
            cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
            cleaned = re.sub(r"\n\s*\n```", "\n```", cleaned)
            return cleaned.rstrip() + "\n"
        return body

    if is_flowchart(body):
        def quote(match: re.Match) -> str:
            stats["labels_quoted"] += 1
            return f'["{match.group(1).strip()}"]'

        return UNQUOTED_LABEL_RE.sub(quote, body)

    return body


def main() -> int:
    stats = {"style_lines_removed": 0, "labels_quoted": 0}
    changed: list[str] = []

    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        original = path.read_text(encoding="utf-8")
        updated = FENCE_RE.sub(
            lambda m: "```mermaid\n" + fix_body(m.group(1), stats) + "```",
            original,
        )

        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)).replace("\\", "/"))

    print(f"Files changed:        {len(changed)}")
    print(f"style/classDef lines removed from sequenceDiagrams: {stats['style_lines_removed']}")
    print(f"flowchart labels quoted:                            {stats['labels_quoted']}")
    for name in changed:
        print(f"   {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
