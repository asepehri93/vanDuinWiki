#!/usr/bin/env python3
"""Remove common PDF-extract paste tails from wiki/papers/*.md (website-only cleanup).

Strips blocks that start with 'From the abstract:' or 'The article further notes that'
and run until the next '## ' heading or end of file. Does not invent new science.
Run from repo root: python3 scripts/strip_paste_artifacts.py [--dry-run]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "wiki" / "papers"

# Through next markdown H2 or EOF (standalone site should not carry raw abstract dumps).
BLOCK_UNTIL_H2 = re.compile(
    r"(\n\n|\n)(From the abstract:|The article further notes that)[\s\S]*?(?=\n## |\Z)"
)


def strip_artifacts(raw: str) -> str:
    original = raw
    prev = None
    while prev != raw:
        prev = raw
        raw = BLOCK_UNTIL_H2.sub("\n\n", raw, count=1)
    if raw == original:
        return raw
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.rstrip() + "\n"


def main() -> None:
    dry = "--dry-run" in sys.argv
    changed = 0
    for path in sorted(PAPERS.glob("*.md")):
        if path.name == "index.md":
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        new = strip_artifacts(raw)
        if new != raw:
            changed += 1
            if not dry:
                path.write_text(new, encoding="utf-8")
    print(f"strip_paste_artifacts: updated {changed} files" + (" [dry-run]" if dry else ""))


if __name__ == "__main__":
    main()
