#!/usr/bin/env python3
"""
Mechanical Phase 4 helper: create wiki/papers/{slug}.md for any normalized/papers/*.json
that does not yet have a matching wiki page.

Per AGENTS.md, this script MUST NOT assign canonical_tags or write scientific summaries.
It only copies metadata from JSON and optionally pastes an extract text prefix from disk.
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_JSON = ROOT / "normalized" / "papers"
WIKI_PAPERS = ROOT / "wiki" / "papers"
PREVIEW_CHARS = 3500


def load_json(path: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    return json.loads(text)


def authors_to_yaml(authors) -> str:
    if isinstance(authors, list):
        lines = [f'  - {json.dumps(a)}' for a in authors]
        return "\n".join(lines) if lines else "  []"
    if isinstance(authors, str):
        return f"  - {json.dumps(authors)}"
    return "  []"


def extract_preview(slug: str, data: dict) -> str | None:
    ext = data.get("extraction") or {}
    rel = ext.get("text_path")
    if not rel:
        return None
    p = ROOT / rel
    if not p.is_file():
        return None
    raw = p.read_text(encoding="utf-8", errors="replace")
    raw = raw.strip()
    if len(raw) > PREVIEW_CHARS:
        raw = raw[:PREVIEW_CHARS].rstrip() + "\n\n…"
    return raw


def render_md(slug: str, data: dict) -> str:
    bib = data.get("bibliography") or {}
    man = data.get("manifest") or {}
    ext = data.get("extraction") or {}
    title = bib.get("title") or "Untitled"
    year = bib.get("year") or 0
    doi = bib.get("doi") or ""
    venue = bib.get("venue") or ""
    pdf_path = data.get("pdf_path") or ""
    sha = man.get("sha256") or ""
    eq = ext.get("quality") or "unknown"
    preview = extract_preview(slug, data)

    body_summary = (
        "This file was created as a **Phase 4 mechanical stub**: metadata is copied from "
        "`normalized/papers/{slug}.json`. Replace this section with an LLM- or human-authored "
        "summary grounded in the PDF and extraction text; assign `canonical_tags` from "
        "`taxonomy/canonical_tags.yml` only."
    ).format(slug=slug)

    preview_block = ""
    if preview:
        preview_block = (
            "\n### Excerpt from normalized extract (mechanical paste)\n\n"
            "> " + "\n> ".join(preview.splitlines()) + "\n"
        )

    return f"""---
id: paper:{slug}
type: paper
title: {json.dumps(title)}
updated: "2026-04-20"
confidence: low
canonical_tags: []
candidate_tags:
  - "phase4-stub-pending-curation"
source_refs: []
doi: {json.dumps(doi)}
year: {int(year) if year else 0}
authors:
{authors_to_yaml(bib.get("authors"))}
venue: {json.dumps(venue)}
pdf_sha256: {json.dumps(sha)}
pdf_path: {json.dumps(pdf_path)}
extraction_quality: {json.dumps(eq)}
group_affiliation: false
---

<!-- id:paper:{slug} -->

## One-paragraph summary

{body_summary}
{preview_block}
## Methods

<!-- Pending Phase 4 curation. -->

## Findings

<!-- Pending Phase 4 curation. -->

## Limitations

<!-- Pending Phase 4 curation. -->

## Relevance to group

<!-- Pending Phase 4 curation. -->

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
"""


def main() -> None:
    WIKI_PAPERS.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped = 0
    for jpath in sorted(PAPERS_JSON.glob("*.json")):
        if jpath.name.startswith("._"):
            continue
        slug = jpath.stem
        out = WIKI_PAPERS / f"{slug}.md"
        if out.is_file():
            skipped += 1
            continue
        data = load_json(jpath)
        out.write_text(render_md(slug, data), encoding="utf-8")
        written += 1
    print(f"written={written} skipped_existing={skipped}")


if __name__ == "__main__":
    main()
