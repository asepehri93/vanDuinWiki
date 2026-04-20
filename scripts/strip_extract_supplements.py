#!/usr/bin/env python3
"""Remove auto-generated extract supplement blocks from paper pages (rollback helper)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "wiki" / "papers"


def strip_supplements(raw: str) -> str:
    for marker in ("<!-- enrich-from-extract:v1 -->", "<!-- enrich-from-extract:v2 -->"):
        if marker not in raw:
            continue
        raw = re.sub(
            rf"\n\n{re.escape(marker)}[\s\S]*?(?=\n## Findings\n)",
            "\n",
            raw,
            count=1,
        )
    raw = re.sub(
        r"\n### (?:Supplemental results|Additional results) \(article abstract\)[\s\S]*?(?=\n## Limitations\n)",
        "\n",
        raw,
        count=1,
    )
    return raw


def main() -> None:
    dry = "--dry-run" in sys.argv
    n = 0
    for path in sorted(PAPERS.glob("*.md")):
        if path.name == "index.md":
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        new = strip_supplements(raw)
        if new != raw:
            n += 1
            if not dry:
                path.write_text(new, encoding="utf-8")
    print(f"stripped supplements in {n} files" + (" [dry-run]" if dry else ""))


if __name__ == "__main__":
    main()
