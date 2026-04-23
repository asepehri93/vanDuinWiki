# indexes — retrieval layer (Phase 5)

Machine-oriented indices for hybrid search (**BM25** + **dense** vectors). Retrieval is part of the **iterative loop** in [`docs/MASTER_PLAN.md`](../docs/MASTER_PLAN.md): baseline eval → Phase 4 Wave 2 (theme links) → rebuild indexes → re-eval. After large edits to `wiki/`, rerun the build steps below.

**Regenerate** with:

```bash
python3 scripts/build_chunks.py
python3 scripts/build_bm25.py
python3 scripts/build_vectors.py   # default: deterministic hash embedding (no pip deps)
python3 scripts/eval_retrieval.py
```

Optional **semantic** embeddings (install [`requirements-phase5.txt`](../requirements-phase5.txt) first):

```bash
pip install -r requirements-phase5.txt
python3 scripts/build_vectors.py --backend sentence_transformers
```

Artifacts (see [`docs/PHASE5_RUNBOOK.md`](../docs/PHASE5_RUNBOOK.md)):

| File | Description |
|------|-------------|
| `chunks.jsonl` | One JSON chunk per line (wiki and optional extract text). |
| `bm25.pkl` | Pickled [`BM25Okapi`](../scripts/bm25_okapi.py) + chunk id order. |
| `vectors.json.gz` | Gzip JSON: embedding matrix, `chunk_ids`, model label. |
| `embedding_manifest.json` | Backend (`hash` or `sentence_transformers`), model id, dimension. |
| `manifest.json` | Chunk build metadata from `build_chunks.py`. |

**Query:** `python3 scripts/search_hybrid.py "your query here"`  
**Evaluate:** `python3 scripts/eval_retrieval.py` → [`outputs/phase5_retrieval_report.md`](../outputs/phase5_retrieval_report.md)

Default chunks are derived from [`wiki/`](../wiki/) only. Add `--include-extracts` to `build_chunks.py` if [`normalized/extracts/`](../normalized/extracts/) exists locally (often gitignored).
