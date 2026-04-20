# Phase 4 gap log (2026-04-20, updated)

## Coverage

- **`wiki/papers/*.md`:** 190 files; each has **curated prose** (Phase 4 agent pass) and **non-empty `canonical_tags`** drawn from `taxonomy/canonical_tags.yml`.
- **Stubs:** `phase4-stub-pending-curation` has been **cleared** corpus-wide (no remaining matches under `wiki/papers/`).
- **`pdf_sha256`:** Mechanical check: **190/190** wiki pages match `manifest.sha256` in `normalized/papers/{slug}.json`.

## Known corpus quirks (operator follow-up)

Some PDFs are **proofs, SI-only, duplicate manifest rows, or mismatched filenames** vs article identity. Subagents documented caveats inline (Limitations / Citations) on affected pages—e.g. workflow artifacts, alternate PDFs for the same DOI, slug/year vs publisher year mismatches. **Normalize `normalized/papers/*.json` bibliography** where you want strict alignment with publisher metadata (partial enrichment was done on some slugs during the final waves).

## KPI notes (vs `docs/PHASE0.md`)

- **Coverage / prose:** Substantively improved toward the Phase 0 “real prose” expectation; edge cases remain **low confidence** where extracts are proof-only or missing abstract text.
- **Connectivity:** Paper pages retain **`[[reaxff-family]]`** and topical links to **`[[batteries-interfaces-reaxff]]`** / **`[[graphene-nanocarbon]]`** where appropriate.
- **Phase 5:** Safe to plan retrieval build once maintainers accept residual low-confidence pages or patch metadata.

## Hygiene

- Ignore or delete macOS **`._*`** sidecar files under `normalized/` and `wiki/` if they reappear on external volumes.
