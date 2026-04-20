# Taxonomy — canonical tags and relations

This directory holds the **controlled vocabulary** for wiki frontmatter `canonical_tags`, synonym redirects, and v1 **relation types** for the normalized layer (Phase 4).

## Files

| File | Role |
|------|------|
| [`canonical_tags.yml`](canonical_tags.yml) | All allowed `axis:slug` tags with labels and descriptions. **Source of truth** for `canonical_tags` in markdown. |
| [`synonyms.yml`](synonyms.yml) | Maps common aliases → canonical id; optional `deprecated` renames. |
| [`relations.yml`](relations.yml) | Allowed typed edges for `normalized/` records and MAS retrieval filters. |

## Seed vs evolving

- **Phase 2 seed:** Tags are derived from corpus theme buckets and group scope; counts are intentionally finite.
- **Phase 3:** After profiling (title/abstract histograms), expect a **taxonomy revision**: add tags, merge near-duplicates, extend `synonyms.yml`.
- Do **not** invent new `axis:slug` strings in wiki pages without adding them to `canonical_tags.yml` in the same change (or use `candidate_tags` until merge).

## Editing

1. Propose new canonical tags via PR or maintainer edit to `canonical_tags.yml` (follow `axis:slug` rules in [`AGENTS.md`](../AGENTS.md)).
2. Add synonyms for LLM/ingest variants to `synonyms.yml`.
3. Log merge decisions per [`docs/TAXONOMY_GOVERNANCE.md`](../docs/TAXONOMY_GOVERNANCE.md).

## Validation (optional automation)

v1 relies on human/LLM review. Optional later: a script that loads `canonical_tags.yml` and flags unknown tags in `wiki/**/*.md`.
