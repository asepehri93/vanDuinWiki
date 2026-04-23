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

    The table below loads **`papers_corpus.json`** (generated from each paper’s YAML + optional `[[theme-…]]` wikilinks). **Sort** by year, title, domain, or slug; **filter** by year, primary **domain** tag, **theme hub** link, **group affiliation**, **confidence**, and free-text **search** (title, slug, venue, tags).

## How this differs from static indexes

- **[All papers by year](paper-index-by-year.md)** and **[by domain](paper-index-by-domain.md)** are plain Markdown tables (good for printing and diffs).
- **This page** is for **exploring** the same corpus with **client-side** filters. Regenerate data after bulk metadata edits: `python3 scripts/generate_papers_indexes.py`.

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
