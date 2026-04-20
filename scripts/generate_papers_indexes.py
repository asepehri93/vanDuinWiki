#!/usr/bin/env python3
"""Emit concepts/paper-index-by-year.md and concepts/paper-index-by-domain.md.

Rows are built only from existing wiki/papers/*.md front matter (title, year, tags).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from phase5_retrieval_lib import ROOT, WIKI, parse_frontmatter

PAPERS = WIKI / "papers"
CONCEPTS = WIKI / "concepts"
SKIP_NAMES = {"index.md"}


def fallback_meta(raw: str) -> dict:
    meta: dict = {}
    m = re.search(r"^id:\s*\"([^\"]+)\"", raw, re.MULTILINE)
    if m:
        meta["id"] = m.group(1)
    m = re.search(r"^year:\s*(\d{4})", raw, re.MULTILINE)
    if m:
        meta["year"] = int(m.group(1))
    m = re.search(r'^title:\s*"(.*?)"\s*$', raw, re.MULTILINE | re.DOTALL)
    if m:
        meta["title"] = m.group(1).replace('\\"', '"')
    return meta


def first_domain_tag(tags: list | None) -> str | None:
    if not tags:
        return None
    for t in tags:
        if isinstance(t, str) and t.startswith("domain:"):
            return t
    return None


def main() -> None:
    rows: list[tuple[str, dict]] = []
    for path in sorted(PAPERS.glob("*.md")):
        if path.name in SKIP_NAMES:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        meta, _ = parse_frontmatter(raw)
        if not meta.get("id"):
            inner = raw.split("---", 2)
            meta.update(fallback_meta(inner[1] if len(inner) >= 2 else ""))
        if meta.get("type") != "paper":
            continue
        rows.append((path.stem, meta))

    by_year: dict[int, list[tuple[str, str]]] = defaultdict(list)
    by_domain: dict[str, list[tuple[str, str, int]]] = defaultdict(list)

    for slug, meta in rows:
        title = meta.get("title")
        if not isinstance(title, str):
            title = slug
        year = meta.get("year")
        if not isinstance(year, int):
            year = 0
        by_year[year].append((slug, title))
        dom = first_domain_tag(meta.get("canonical_tags") if isinstance(meta.get("canonical_tags"), list) else None)
        if not dom:
            dom = "domain:unsorted"
        by_domain[dom].append((slug, title, year))

    rel_paper = "../papers"

    lines_y = [
        "---",
        'id: "concept:paper-index-by-year"',
        "type: concept",
        'title: "Paper index by publication year"',
        'updated: "2026-04-20"',
        "confidence: high",
        "canonical_tags: [domain:methods-software]",
        "candidate_tags: []",
        "source_refs: []",
        "---",
        "",
        "<!-- id:concept:paper-index-by-year -->",
        "",
        "!!! abstract \"Browse the corpus\"",
        "",
        "    Every row links to an existing **`wiki/papers/`** note. **Years and titles** are taken only from each file’s YAML (`year`, `title`)—the same bibliographic fields used elsewhere in this KB—not generated prose.",
        "",
        "## How to use",
        "",
        f"- Open any linked title for the curated summary (grounded in the publication).",
        "- Use **search** (`/`) for author or keyword strings.",
        "",
    ]

    for year in sorted(by_year.keys(), reverse=True):
        if year == 0:
            continue
        lines_y.append(f"## {year}")
        lines_y.append("")
        lines_y.append("| Title | Slug |")
        lines_y.append("|-------|------|")
        for slug, title in sorted(by_year[year], key=lambda x: x[1].lower()):
            safe = title.replace("|", "\\|")
            lines_y.append(f"| [{safe}]({rel_paper}/{slug}.md) | `{slug}` |")
        lines_y.append("")

    if by_year.get(0):
        lines_y.append("## Year not set in front matter")
        lines_y.append("")
        lines_y.append("| Title | Slug |")
        lines_y.append("|-------|------|")
        for slug, title in sorted(by_year[0], key=lambda x: x[1].lower()):
            safe = title.replace("|", "\\|")
            lines_y.append(f"| [{safe}]({rel_paper}/{slug}.md) | `{slug}` |")
        lines_y.append("")

    CONCEPTS.mkdir(parents=True, exist_ok=True)
    out_y = CONCEPTS / "paper-index-by-year.md"
    out_y.write_text("\n".join(lines_y) + "\n", encoding="utf-8")

    lines_d = [
        "---",
        'id: "concept:paper-index-by-domain"',
        "type: concept",
        'title: "Paper index by primary domain tag"',
        'updated: "2026-04-20"',
        "confidence: high",
        "canonical_tags: [domain:methods-software]",
        "candidate_tags: []",
        "source_refs: []",
        "---",
        "",
        "<!-- id:concept:paper-index-by-domain -->",
        "",
        "!!! abstract \"Browse by taxonomy\"",
        "",
        "    Grouping uses the **first `domain:`** string in each paper’s `canonical_tags`. This is a **navigational sort** from existing wiki metadata, not a new scientific classification step.",
        "",
    ]

    for dom in sorted(by_domain.keys(), key=lambda s: s.lower()):
        lines_d.append(f"## {dom}")
        lines_d.append("")
        lines_d.append("| Year | Title | Slug |")
        lines_d.append("|------|-------|------|")
        for slug, title, year in sorted(by_domain[dom], key=lambda x: (-(x[2] or 0), x[1].lower())):
            safe = title.replace("|", "\\|")
            yr = year if year else "—"
            lines_d.append(f"| {yr} | [{safe}]({rel_paper}/{slug}.md) | `{slug}` |")
        lines_d.append("")

    out_d = CONCEPTS / "paper-index-by-domain.md"
    out_d.write_text("\n".join(lines_d) + "\n", encoding="utf-8")

    print(f"wrote {out_y} ({len(rows)} papers)")
    print(f"wrote {out_d}")


if __name__ == "__main__":
    main()
