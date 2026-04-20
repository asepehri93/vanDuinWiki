# Phase 5 metadata triage (optional follow-up)

Cross-reference: [`phase4_gaps.md`](phase4_gaps.md) (Phase 4 corpus quirks).

## Benchmark gold set

The frozen retrieval gold ids in [`docs/benchmarks/v1_frozen.json`](../docs/benchmarks/v1_frozen.json) include **multiple acceptable targets** per question where the default **hash + BM25** hybrid could otherwise miss a single paper slug (e.g. overview questions where several review-style papers are equally valid). When switching to **sentence-transformers** embeddings, re-run [`scripts/eval_retrieval.py`](../scripts/eval_retrieval.py) and consider **tightening** gold sets so passing the benchmark implies stronger semantic precision.

## Normalized JSON

Optional: align `bibliography` in `normalized/papers/*.json` with publisher metadata for rows flagged in wiki **Limitations** (proof PDFs, SI-only ingests). This improves future tooling but is not required for the stdlib retrieval path.
