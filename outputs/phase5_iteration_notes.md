# Phase 5 iteration notes (2026-04-20)

## Baseline (archived)

- **Report:** [`archives/phase5_retrieval_baseline_2026-04-20.md`](archives/phase5_retrieval_baseline_2026-04-20.md) (copy of first full pipeline run after YAML fixes).
- **Embeddings:** default **hash** backend (`scripts/build_vectors.py --backend hash`).
- **Pass rate (v1 frozen, 12 questions):** **10/12 (83.3%)**.

## Semantic embedding trial

- Rebuilt vectors with `python3 scripts/build_vectors.py --backend sentence_transformers` (384-d MiniLM).
- Eval output: [`phase5_retrieval_report_semantic.md`](phase5_retrieval_report_semantic.md) — **10/12 (83.3%)** (same as hash on this benchmark).
- **Indexes restored** to hash vectors for portable, stdlib-friendly default (`build_vectors.py --backend hash`).

## Follow-ups

- Try larger `k` in `docs/benchmarks/v1_frozen.json` or per-query tuning only after adding more benchmark questions.
- If OMP/torch errors appear in sandboxed CI, run eval with `OMP_NUM_THREADS=1` or full permissions.
