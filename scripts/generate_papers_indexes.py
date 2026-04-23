#!/usr/bin/env python3
"""Emit concepts/paper-index-by-year.md, concepts/paper-index-by-domain.md,
and wiki/javascripts/papers_corpus.json for the interactive paper browser.

Rows are built only from existing wiki/papers/*.md front matter (title, year, tags).
"""
from __future__ import annotations

import json
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
JS_DIR = WIKI / "javascripts"
SKIP_NAMES = {"index.md"}
THEME_WIKILINK_RE = re.compile(r"\[\[(theme-[a-z0-9-]+)\]\]")


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


def first_axis_tag(tags: list | None, axis: str) -> str | None:
    if not tags:
        return None
    prefix = f"{axis}:"
    for t in tags:
        if isinstance(t, str) and t.startswith(prefix):
            return t
    return None


def theme_slugs_from_body(body: str) -> list[str]:
    return sorted(set(THEME_WIKILINK_RE.findall(body)))


def main() -> None:
    rows: list[tuple[str, dict, str]] = []
    for path in sorted(PAPERS.glob("*.md")):
        if path.name in SKIP_NAMES:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        meta, body = parse_frontmatter(raw)
        if not meta.get("id"):
            inner = raw.split("---", 2)
            meta.update(fallback_meta(inner[1] if len(inner) >= 2 else ""))
        if meta.get("type") != "paper":
            continue
        rows.append((path.stem, meta, body))

    by_year: dict[int, list[tuple[str, str]]] = defaultdict(list)
    by_domain: dict[str, list[tuple[str, str, int]]] = defaultdict(list)

    for slug, meta, _ in rows:
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
        'updated: "2026-04-22"',
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
        'updated: "2026-04-22"',
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

    corpus: list[dict] = []
    for slug, meta, body in rows:
        tags = meta.get("canonical_tags") if isinstance(meta.get("canonical_tags"), list) else []
        tags_s = [t for t in tags if isinstance(t, str)]
        title = meta.get("title")
        if not isinstance(title, str):
            title = slug
        year = meta.get("year")
        if not isinstance(year, int):
            year = 0
        venue = meta.get("venue")
        if not isinstance(venue, str):
            venue = ""
        dom = first_domain_tag(tags_s) or "domain:unsorted"
        meth = first_axis_tag(tags_s, "method")
        task = first_axis_tag(tags_s, "task")
        conf = meta.get("confidence")
        if not isinstance(conf, str):
            conf = "med"
        group = meta.get("group_affiliation")
        if isinstance(group, bool):
            group_b = group
        elif isinstance(group, str) and group.lower() in ("true", "yes", "1"):
            group_b = True
        else:
            group_b = False
        themes = theme_slugs_from_body(body)
        corpus.append(
            {
                "slug": slug,
                "title": title,
                "year": year,
                "venue": venue,
                "domain": dom,
                "method": meth,
                "task": task,
                "tags": tags_s,
                "themes": themes,
                "group": group_b,
                "confidence": conf,
            }
        )

    JS_DIR.mkdir(parents=True, exist_ok=True)
    out_json = JS_DIR / "papers_corpus.json"
    payload = {
        "generated": "2026-04-22",
        "count": len(corpus),
        "papers": corpus,
    }
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {out_y} ({len(rows)} papers)")
    print(f"wrote {out_d}")
    print(f"wrote {out_json}")


if __name__ == "__main__":
    main()
