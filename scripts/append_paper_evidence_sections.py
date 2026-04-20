#!/usr/bin/env python3
"""Insert a standard Evidence section after the paper id HTML comment if missing.

Idempotent: skips files that already contain '## Evidence and attribution'.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from phase5_retrieval_lib import WIKI, parse_frontmatter

PAPERS = WIKI / "papers"
SKIP = {"index.md"}

BLOCK = """

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

"""


def main() -> None:
    n = 0
    for path in sorted(PAPERS.glob("*.md")):
        if path.name in SKIP:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        meta, _ = parse_frontmatter(raw)
        if meta.get("type") != "paper":
            continue
        if "## Evidence and attribution" in raw:
            continue
        start = raw.find("<!-- id:paper:")
        if start == -1:
            continue
        m_end = raw.find("-->", start)
        if m_end == -1:
            continue
        insert_pos = m_end + 3
        while insert_pos < len(raw) and raw[insert_pos] in "\r\n":
            insert_pos += 1
        new_raw = raw[:insert_pos] + BLOCK + raw[insert_pos:]
        path.write_text(new_raw, encoding="utf-8")
        n += 1

    print(f"updated {n} paper files (idempotent: skips if section exists)")


if __name__ == "__main__":
    main()
