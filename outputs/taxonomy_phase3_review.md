# Taxonomy review — Phase 3 (corpus profiling)

**Date:** 2026-04-20  
**Evidence:** [`corpus_profile_2026-04.md`](corpus_profile_2026-04.md), [`normalized/corpus_summary.json`](../normalized/corpus_summary.json)

## Corpus snapshot

- **Papers registered:** 190 PDFs (see [`raw/MANIFEST.jsonl`](../raw/MANIFEST.jsonl)).
- **Extraction quality:** majority `good`; a minority `partial` (thin metadata); one file failed open (`papers/Senftle_ACS Catalysis_2015.pdf` — see [`ingest_exceptions.md`](ingest_exceptions.md)).
- **Duplicate content hashes:** 0 groups (proofs/finals in this tree differ byte-for-byte or only one copy per hash).

## Title-word signal (metadata)

Strong recurring terms in PDF titles include: **reaxff**, **molecular**, **dynamics**, **reactive**, **force**, **simulations**, plus **graphene**, **pyrolysis**, **nickel**, **water**, **carbon**, **oxidation**, **fuel**, **surface**, **mechanical**, **plasma**, **single-layer**, etc.

This aligns with the Phase 2 seed axes: reactive MD / ReaxFF lineage, oxides and surfaces, carbon and fuels, catalysis (Ni), 2D (graphene, single-layer), mechanics, water/aqueous chemistry.

## Decision

- **No mandatory changes** to [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml) for v1—the seed list already covers these themes.
- **Synonym additions:** optional strings were added in [`taxonomy/synonyms.yml`](../taxonomy/synonyms.yml) for common variants (`pyrolysis`, `MD`, `DFT`) mapping to existing canonical tags.
- **Follow-up after Phase 4:** if entity extraction surfaces systematic gaps (e.g. a new recurring material class), add a `domain:` or `material:` tag and document in the next monthly merge log.

## Benchmarks

[`docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](../docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md) was annotated with a short corpus-evidence subsection pointing to this profile run.
