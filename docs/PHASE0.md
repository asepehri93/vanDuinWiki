# Phase 0 — Success criteria, boundaries, and retrieval benchmarks

This document **closes Phase 0** of the master plan: what “good” means before scaling pipelines, what stays private vs publishable, who does what, and how **benchmark questions** are produced and frozen.

## v1 acceptance metrics (numeric thresholds)

These are **starting targets**; tighten after the first full compile and retrieval build.

| Metric | Definition | v1 target |
|--------|------------|-----------|
| **Coverage** | Fraction of rows in `raw/MANIFEST.jsonl` that have a valid `normalized/papers/{slug}.json` **and** a `wiki/papers/{slug}.md` with matching `paper_id` and `pdf_sha256`. | **≥ 95%** |
| **Bibliography completeness** | Among covered papers, fraction with `year` and (`title` or resolvable `doi`) in the normalized record. | **≥ 98%** |
| **Connectivity** | Fraction of `paper` pages linked (wikilink or `related_ids` / backlinks) from **≥ 1** of: `concept`, `material`, `forcefield`, `methodprotocol`. | **≥ 80%** at end of Phase 4; **≥ 50%** acceptable after first linking pass |

**Milestone note:** Per-paper curation (Phase 4 first pass) can be **complete** while this connectivity fraction is still below target. Close the gap in **Phase 4 Wave 2** (theme hubs, incoming links)—see [`MASTER_PLAN.md`](MASTER_PLAN.md) and [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md).
| **Grounding (synthesis pages)** | On `concept` / `material` / `forcefield` / `methodprotocol` / `debate` pages: fraction of `##`-level sections that include at least one `source_refs` entry or explicit `paper_id` citation. | **≥ 90%** |
| **High-confidence orphans** | Count of synthesis pages with `confidence: high` and empty `source_refs` (and no inline citations). | **0** |
| **Retrieval benchmark pass rate** | Fraction of **frozen v1** benchmark questions for which a retrieval+answer workflow returns relevant supporting `paper_id`s or entity pages in the top set (see grading rubric in Phase 5). | **≥ 70%** overall once indexes exist; **≥ 50%** on the “force field / protocol existence” subset |

Track failures in a small **exceptions log** (e.g. `outputs/ingest_exceptions.md`): corrupt PDFs, duplicates, missing metadata—so headline percentages stay honest.

## Data boundaries

| Class | Examples | Default |
|-------|----------|--------|
| **Private** | PDFs under `papers/`, raw full-text extractions, internal lab notes, unreleased snapshots | Not in public git remotes without an explicit policy |
| **Repo-safe machine layer** | `normalized/`, `indexes/` (regenerable), `raw/MANIFEST.jsonl` | Yes |
| **Publishable later (Phase 8)** | Curated `wiki/` pages, redacted summaries, derived metadata without full text | Export subset only; run publication checklist |

## Roles (lightweight v1)

| Role | Responsibility |
|------|----------------|
| **Maintainer** | Append manifest rows, run batch ingest, regenerate indexes, archive monthly snapshot notes under `outputs/` or tagged git |
| **Contributor** | Add PDFs, propose taxonomy candidates, file gaps in `outputs/` |
| **Reviewer (optional)** | Spot-check high-`confidence` synthesis pages and promotion to “publish-ready” export; not required for private-only operation |

## Benchmark questions: principles

- Questions must be **answerable from the KB** (papers + entity pages + citations), not from memory alone.
- Avoid **too-general** stems (“which papers use ReaxFF?”) that only test keyword search.
- Avoid **too-specific** stems that single out one obscure system unless you explicitly want a stress test.
- Prefer **mid-level** stems: theme + method + material class + task (e.g. validation, coverage, protocol), so both humans and MAS workflows are exercised.

## Warm-up pass (LLM-led, not template scripts)

**Do not** generate benchmark questions by automated token frequency or fill-in templates (that produces repetitive, low-information questions).

**Do** run a **warm-up pass** over the corpus using an LLM with **real paper context**:

1. **Batch inputs:** For each PDF (or batch of 10–20), supply **title, abstract, and optional first-page keywords** (from extraction or manual paste). Filenames alone are insufficient for final categories but help disambiguate.
2. **LLM task A — taxonomy:** Propose or refine **high-level categories** that actually appear (e.g. reactive MD and parameterization, battery interfaces, oxide surfaces, 2D semiconductors, carbon/soot chemistry, catalysis, ferroelectrics, polymer / organic oxidation, water and silica, mechanical / fracture, machine-learned potentials). Merge synonyms; cap roughly **8–15** top-level buckets for the group corpus.
3. **LLM task B — question seeds:** For each bucket, propose **5–10 candidate questions** at mid granularity, varied (existence, comparison, protocol, gap-finding, disagreement-if-evidence).
4. **Human / maintainer:** Append seeds to a working list (e.g. [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md) or a scratch file), deduplicate, and **select 50** for the official candidate pool; then **narrow to 20–40** for the frozen v1 evaluation set after one review round.

Re-run steps 2–4 **after large ingests** or quarterly; version the frozen set (e.g. `docs/benchmarks/V1_FROZEN.md` in Phase 5).

## Current artifact: 50 candidate questions (initial pool)

The file [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md) contains **50 numbered candidate questions** produced by an **LLM survey** of this repo’s PDF set: categories were inferred from **filenames, paths, and recurring themes** across ~190 PDFs (excluding AppleDouble `._*` files), not from automated term counting. **They are candidates, not frozen benchmarks.** Replace or refine them after your abstract-level warm-up pass if needed.

## Handoff

- **Operator roadmap (post first-pass):** [`MASTER_PLAN.md`](MASTER_PLAN.md) — connectivity audit, Phase 5 retrieval loop, Wave 2 themes, Phase 8 export outline.
- **Phase 1:** Schema and folders — [`AGENTS.md`](../AGENTS.md).
- **Phase 2:** Canonical tags and governance — [`TAXONOMY_GOVERNANCE.md`](TAXONOMY_GOVERNANCE.md), [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml).
- **Phase 3:** Corpus profiling — [`PHASE3_RUNBOOK.md`](PHASE3_RUNBOOK.md), [`../outputs/corpus_profile_2026-04.md`](../outputs/corpus_profile_2026-04.md); reconcile benchmarks and taxonomy per [`../outputs/taxonomy_phase3_review.md`](../outputs/taxonomy_phase3_review.md).
- **Phase 4:** Wiki compilation is **LLM-led** (not script-generated science) — [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md); KPIs above apply after a full compile pass.
- **Phase 5:** Grade retrieval against the **frozen** subset; tune hybrid search until thresholds are met — [`PHASE5_RUNBOOK.md`](PHASE5_RUNBOOK.md), [`benchmarks/v1_frozen.json`](benchmarks/v1_frozen.json), [`benchmarks/V1_FROZEN.md`](benchmarks/V1_FROZEN.md).
