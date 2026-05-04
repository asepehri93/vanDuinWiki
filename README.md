# vanDuinWiki — Computational chemistry knowledge base.

Private-first research memory and future MAS retrieval substrate, built from a PDF corpus under `papers/` and compiled into structured records and markdown wiki pages.

**Browse online (GitHub Pages):** after pushing to `main` and enabling Actions → Pages, the MkDocs site is served at [https://asepehri93.github.io/vanDuinWiki/](https://asepehri93.github.io/vanDuinWiki/) (see [`mkdocs.yml`](mkdocs.yml) and [`.github/workflows/mkdocs-gh-pages.yml`](.github/workflows/mkdocs-gh-pages.yml)).

**Navigation:** the sidebar lists **every paper** via auto-generated tables ([`wiki/concepts/paper-index-by-year.md`](wiki/concepts/paper-index-by-year.md), [`wiki/concepts/paper-index-by-domain.md`](wiki/concepts/paper-index-by-domain.md)) plus **theme** cluster pages. Regenerate those tables after bulk `year` / tag edits: `python3 scripts/generate_papers_indexes.py`.

## Layout

| Path | Role |
|------|------|
| [`papers/`](papers/) | PDF corpus (~500). Treat as **read-only**; do not edit sources in place. |
| [`raw/`](raw/) | Ingest manifests and immutable ingest metadata. See [`raw/README.md`](raw/README.md). |
| [`normalized/`](normalized/) | Machine-oriented JSON records per paper (and later entities). Source of truth for pipelines. |
| [`wiki/`](wiki/) | Human-readable markdown (Obsidian-compatible). Generated and maintained by the KB workflow. |
| [`indexes/`](indexes/) | Retrieval artifacts (chunk maps, future BM25/vector indices). |
| [`outputs/`](outputs/) | Ad-hoc reports, briefings, slides — not canonical KB state. |

## Operator manual

All schemas, ID rules, frontmatter contracts, and ingest policy are defined in [`AGENTS.md`](AGENTS.md).

**Semantic vs mechanical:** Scientific content (summaries, tags, synthesis) is **LLM- or human-authored**; **Python/shell** is only for bulk mechanical work (hashing, lists, validation) — see [`AGENTS.md`](AGENTS.md) and [`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md).

**Phase 0 (success metrics and benchmarks):** [`docs/PHASE0.md`](docs/PHASE0.md) — v1 KPI thresholds, privacy boundaries, roles, and how retrieval benchmark questions are accumulated (LLM warm-up, not template scripts).

**Phase 2 (taxonomy):** [`docs/TAXONOMY_GOVERNANCE.md`](docs/TAXONOMY_GOVERNANCE.md) — canonical `axis:slug` tags, synonyms, candidate-tag merge, relation types in [`taxonomy/`](taxonomy/).

**Phase 3 (corpus profiling):** [`docs/PHASE3_RUNBOOK.md`](docs/PHASE3_RUNBOOK.md) — optional mechanical run `python3 scripts/corpus_profile.py`; outputs include [`raw/MANIFEST.jsonl`](raw/MANIFEST.jsonl), [`normalized/papers/`](normalized/papers/), and [`outputs/corpus_profile_2026-04.md`](outputs/corpus_profile_2026-04.md).

**Phase 4 (wiki compilation):** [`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md) — LLM-led paper and entity pages, linking, and normalized JSON enrichment.

**Operator roadmap (connectivity Wave 2 + Phase 5 loop + Phase 8 scope):** [`docs/MASTER_PLAN.md`](docs/MASTER_PLAN.md)

**Session priming anchor:** [`docs/SESSION_PRIMER.md`](docs/SESSION_PRIMER.md) — fastest complete context for new blank chat sessions.

**Operations anchor:** [`docs/KB_OPERATIONS_MANUAL.md`](docs/KB_OPERATIONS_MANUAL.md) — full maintenance and update handbook (technical + writing contracts).

## Phases

This repo follows a phased master plan: Phase 0–3 are documented in-repo (KPIs, IA/schema, taxonomy, corpus profiling); **Phase 4** is LLM-led wiki compilation ([`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md)); **Phase 5** is hybrid retrieval and benchmark grading ([`docs/PHASE5_RUNBOOK.md`](docs/PHASE5_RUNBOOK.md), [`indexes/README.md`](indexes/README.md)); **Phase 8** is public/export policy ([`docs/PHASE8_EXPORT.md`](docs/PHASE8_EXPORT.md)). The **single roadmap** tying these together after the first-pass compile is [`docs/MASTER_PLAN.md`](docs/MASTER_PLAN.md).
