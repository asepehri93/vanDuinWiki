# Taxonomy governance — hybrid canonical + candidate tags

This document defines how tags enter the KB, how they are **normalized to canonical** `axis:slug` values, and how maintainers **merge** emergent vocabulary without drift.

**Normative files:** [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml), [`taxonomy/synonyms.yml`](../taxonomy/synonyms.yml), [`taxonomy/relations.yml`](../taxonomy/relations.yml).  
**Operator rules:** [`AGENTS.md`](../AGENTS.md).

## Canonical vs candidate

| Field | Purpose |
|-------|---------|
| `canonical_tags` | Only tags listed in `taxonomy/canonical_tags.yml` (`id` = `axis:slug`). Used for stable search, filters, and exports. |
| `candidate_tags` | Free-form strings from ingest or LLM (abbreviations, one-off phrases, near-misses). Resolved at **merge** into canonical + synonyms. |

**Rule:** Every string in `canonical_tags` must appear as an `id` under `tags:` in `canonical_tags.yml`. If you need a new tag, **add it to the YAML first** (same commit/PR), or park the phrase in `candidate_tags` until merge.

**Guideline:** Prefer **3–8** canonical tags per page to avoid noise; use the most specific applicable tags.

**Production tag assignment:** `canonical_tags` on wiki pages must be chosen by **LLM or human** against [`canonical_tags.yml`](../taxonomy/canonical_tags.yml). Do not rely on unattended scripts to assign tags for production pages (scripts may assist with validation or suggested lists for review only).

## Candidate tag workflow

1. **During ingest or wiki generation:** LLM may emit labels (e.g. “Li–S cathode”, “graphite anode”).  
   - If an exact canonical id fits, put it in `canonical_tags`.  
   - Otherwise add leftovers to `candidate_tags` **or** append lines to [`outputs/taxonomy_candidates.md`](../outputs/taxonomy_candidates.md) (create if missing) for batch review.

2. **Maintainer review (monthly or end of batch):**  
   - For each frequent `candidate_tags` string: map to existing canonical via [`synonyms.yml`](../taxonomy/synonyms.yml), **or** add a new `tags:` entry to `canonical_tags.yml` with a clear `axis`.  
   - Remove resolved candidates from pages when you next touch them (or via scripted pass).

3. **Synonyms:** Add alternate spellings / legacy labels to `synonyms.yml` so future ingests map cleanly.

## Monthly merge checklist

Use this after each significant ingest or on a fixed calendar date.

1. Open `outputs/taxonomy_candidates.md` (if used) and scan `candidate_tags` across new wiki pages.  
2. **Collapse synonyms:** merge near-duplicate canonical tags if two `id`s describe the same bucket; add `deprecated` entries in `synonyms.yml` pointing old → new.  
3. **Promote:** add high-signal recurring candidates to `canonical_tags.yml`.  
4. **Deprecate:** for retired `id`s, list under `deprecated` in `synonyms.yml` with replacement.  
5. **Log:** write [`outputs/taxonomy_merge_YYYY-MM.md`](../outputs/) with date, decisions, and tag counts (optional table).  
6. **Reconcile benchmarks:** if theme names in [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md) no longer match domain tags, update section headers **only** for clarity (questions themselves stay until you revise content).

## Phase 3 handoff (corpus profiling)

After title/abstract profiling (Phase 3):

- Compare **empirical cluster frequencies** to the Phase 2 seed list.  
- Open a **taxonomy revision**: add missing `domain:` / `method:` tags; merge sparse tags into broader ones + synonyms.  
- Update `taxonomy/README.md` seed note if the vocabulary stabilizes.

## Relations (Phase 4)

Edge types for `normalized/` JSON and future graphs are defined in [`taxonomy/relations.yml`](../taxonomy/relations.yml). Do not invent new relation ids in code or prompts without adding them there with `subject_types` / `object_types`.

## Optional automation

A small validator (future) can load `canonical_tags.yml` and fail CI on unknown `canonical_tags` in `wiki/`. Not required for v1.
