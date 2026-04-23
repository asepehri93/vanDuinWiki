---
id: "concept:paper-corpus-browser"
type: concept
title: "Paper corpus browser (sort & filter)"
updated: "2026-04-22"
confidence: high
canonical_tags: [domain:methods-software]
candidate_tags: []
source_refs: []
---

<!-- id:concept:paper-corpus-browser -->

!!! abstract "Interactive table"

    This page is a navigation entry point for exploring the local paper corpus with sortable and filterable metadata. It helps readers and agents decide where to start, without introducing new scientific claims beyond curated paper metadata and existing wiki links.

## Scope and user intent

This page answers practical "where do I begin?" questions for corpus navigation, such as "Which domain clusters are represented?", "Which papers are group-affiliated?", and "Which theme hubs already connect a paper?".
It does not attempt to provide a literature review, methodological recommendations, or scientific conclusions; those belong on paper, theme, protocol, and debate pages.

## Start-here pathways

If your goal is chronological orientation, start with a year filter and sort by newest first, then branch into [All papers by year](paper-index-by-year.md) for static snapshots.
If your goal is thematic orientation, filter by domain and theme link first, then open the relevant `[[theme-...]]` hubs for cross-paper synthesis.
If your goal is curation triage, filter by confidence and group affiliation to prioritize pages that are most actionable for internal updates.
If your goal is broad discovery, use free-text search on titles, slugs, venues, and tags, then pivot to linked paper pages for source-grounded details.

## Decision levers and trade-offs

Year filtering emphasizes recency but can hide foundational older references that remain central in a domain.
Domain filtering increases topical precision but depends on the first `domain:*` canonical tag, so classification quality influences recall.
Theme filtering quickly surfaces cross-links but under-represents papers that have not yet been linked to a `[[theme-...]]` page.
Confidence and group-only filters support operational prioritization, but they are curation metadata rather than direct quality scores of the underlying science.

## Canonical starting papers

This browser is intentionally metadata-driven and does not nominate fixed "starter papers" on its own.
Use the filtered table to identify candidate papers, then open each `wiki/papers/*.md` page for methods/findings context and evidence-grounded interpretation.
For static, corpus-wide entry points, use [All papers by year](paper-index-by-year.md) and [All papers by domain](paper-index-by-domain.md).

## Related protocols and debates

After identifying a paper subset here, continue through `wiki/protocols/` when you need executable workflow guidance, and through `wiki/debates/` when you need evidence-structured disagreement analysis.
This page is intentionally a routing layer, so it links readers outward instead of duplicating protocol or debate content.

## Failure modes and interpretation pitfalls

A missing theme link does not mean a paper is irrelevant to that theme; it can also indicate that cross-linking is incomplete.
A paper with limited metadata can still be scientifically important, so final judgment should be made on the paper page and source-backed sections.
Filter combinations can become overly restrictive, so clear one or more controls when result counts drop unexpectedly.

<div markdown="0" id="paper-corpus-root">

<p class="pc-count">Loading paper list…</p>

<div class="pc-controls" style="display:flex;flex-wrap:wrap;gap:0.75rem 1.25rem;align-items:flex-end;margin:1rem 0;">

<label>Search<br/>
<input type="search" class="pc-search" placeholder="Title, slug, venue, tags…" style="min-width:16rem;"/></label>

<label>Year<br/>
<select class="pc-year"></select></label>

<label>Domain<br/>
<select class="pc-domain"></select></label>

<label>Theme (wikilink)<br/>
<select class="pc-theme"></select></label>

<label>Sort by<br/>
<select class="pc-sort">
<option value="year-desc">Year (newest first)</option>
<option value="year-asc">Year (oldest first)</option>
<option value="title-az">Title (A–Z)</option>
<option value="title-za">Title (Z–A)</option>
<option value="domain-az">Domain (A–Z)</option>
<option value="slug-az">Slug (A–Z)</option>
</select></label>

<label>Confidence<br/>
<select class="pc-confidence"></select></label>

<label style="display:flex;align-items:center;gap:0.35rem;margin-top:1.1rem;"><input type="checkbox" class="pc-group"/> Group papers only</label>

</div>

<div style="overflow-x:auto;">

<table class="pc-table">
<thead>
<tr>
<th>Year</th>
<th>Title</th>
<th>Domain</th>
<th>Method</th>
<th>Themes</th>
<th>Conf.</th>
<th>Group</th>
<th>Slug</th>
</tr>
</thead>
<tbody class="pc-tbody"></tbody>
</table>

</div>

</div>

<script src="../javascripts/paper-corpus-browser.js"></script>

## Data fields

| Field | Source |
|-------|--------|
| Year, title, venue, tags, confidence, group | YAML front matter in each `wiki/papers/*.md` |
| **Domain** | First `domain:*` in `canonical_tags` (same rule as the static domain index) |
| **Method** | First `method:*` in `canonical_tags`, if any |
| **Themes** | `[[theme-…]]` wikilinks anywhere in the paper body (hub cross-links) |

Papers with **no** `[[theme-…]]` link still appear; use **Theme → Any theme link** and rely on domain/year search.

??? info "MAS / retrieval"
    Stable id: `concept:paper-corpus-browser`.
    Primary retrieval hooks are slug, title, year, venue, `canonical_tags`, confidence, group affiliation, and detected `[[theme-...]]` links exported into `wiki/javascripts/papers_corpus.json`.
    Refresh this page's backing data after bulk edits to paper frontmatter or tags by running `python3 scripts/generate_papers_indexes.py`.
