# Phase 4 gap log (updated)

## Coverage

- **`wiki/papers/*.md`:** **1278** paper notes (excluding `papers/index.md`); each is intended to have curated prose, `canonical_tags`, and Methods/Findings aligned with sources per [`AGENTS.md`](../AGENTS.md).
- **Stubs:** `phase4-stub-pending-curation` and the mechanical stub phrase are **cleared** corpus-wide (`python3 scripts/paper_curation_batches.py --mode pending --dry-run` → `total_slugs=0`).
- **First-pass curation batches:** Approved through `batch-006` — see [`outputs/curation_batches/manifest.json`](curation_batches/manifest.json) and [`outputs/curation_batches/_README.md`](curation_batches/_README.md).

## Wave 2 connectivity + Phase 5

- **Mechanical connectivity:** **100%** of paper slugs are linked from synthesis trees (see [`wave2_connectivity_status.md`](wave2_connectivity_status.md), [`connectivity_report.md`](connectivity_report.md)).
- **Optional narrative Wave 2:** Expand theme hub “literature review” prose per [`docs/MASTER_PLAN.md`](../docs/MASTER_PLAN.md).
- **Retrieval:** Baseline report [`phase5_retrieval_report.md`](phase5_retrieval_report.md); iteration notes [`phase5_iteration_notes.md`](phase5_iteration_notes.md).

## Known corpus quirks (operator follow-up)

Some PDFs are **proofs, SI-only, duplicate manifest rows, or mismatched filenames** vs article identity. Maintainer catalog: [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](../docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md). Normalize `normalized/papers/*.json` bibliography where strict publisher alignment matters.

## Hygiene

- Ignore or delete macOS **`._*`** sidecar files under `normalized/` and `wiki/` if they reappear on external volumes.
