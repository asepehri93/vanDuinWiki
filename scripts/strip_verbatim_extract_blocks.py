#!/usr/bin/env python3
"""Remove ### Extract-based cues (verbatim excerpt) blockquote sections from wiki/papers.

Keeps prose after the blockquote (checklist bullets, protocol summaries). See AGENTS.md."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "wiki" / "papers"
MARKER = "### Extract-based cues (verbatim excerpt)"


def strip_block(lines: list[str], start_idx: int) -> int:
    """Skip from MARKER line through blockquote lines; return new index."""
    i = start_idx + 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines) and not lines[i].strip().startswith(">"):
        i += 1
    while i < len(lines) and lines[i].strip().startswith(">"):
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    return i


def process_text(text: str) -> tuple[str, bool]:
    if MARKER not in text:
        return text, False
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    changed = False
    while i < len(lines):
        if lines[i].strip() == MARKER:
            changed = True
            i = strip_block(lines, i)
            continue
        out.append(lines[i])
        i += 1
    # preserve trailing newline style
    nl = "\n"
    if text.endswith("\n"):
        body = nl.join(out) + nl
    else:
        body = nl.join(out)
    return body, changed


def main() -> None:
    n_files = 0
    for path in sorted(PAPERS.glob("*.md")):
        if path.name.startswith("._") or path.name == "index.md":
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        new, changed = process_text(raw)
        if changed:
            path.write_text(new, encoding="utf-8")
            n_files += 1
            print(path.name)
    print(f"updated {n_files} files", file=sys.stderr)


if __name__ == "__main__":
    main()
