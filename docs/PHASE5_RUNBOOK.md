# Phase 5 — Retrieval indexes and benchmark grading

This runbook defines how to **build**, **refresh**, and **evaluate** the machine retrieval layer under [`indexes/`](../indexes/). It complements [`PHASE0.md`](PHASE0.md) (KPIs) and [`AGENTS.md`](../AGENTS.md) (schema). **Indexing is mechanical**: chunking copies text from `wiki/` (and optionally local `normalized/extracts/`); it does not author new scientific claims.

## Goals

1. **Regenerable artifacts** — delete `indexes/` outputs and rebuild from the same sources + scripts.
2. **Hybrid retrieval** — combine **lexical** (BM25 over chunks) and **dense** (embedding cosine similarity) with **fusion** (default: RRF; optional weighted sum).
3. **Provenance** — every hit returns `chunk_id`, `wiki_path`, optional `paper_id` / wiki `id`, and scores.
4. **Benchmarking** — grade against [`benchmarks/v1_frozen.yaml`](benchmarks/v1_frozen.yaml) per rubric below.

## Privacy and data boundaries

- **Repo-safe:** `indexes/` derived from `wiki/` is generally safe; **embedding APIs** may send chunk text off-machine — document provider choice; use **local** `sentence-transformers` for air-gapped workflows.
- **Extracts:** [`normalized/extracts/`](../normalized/extracts/) may be **gitignored**; chunking can skip them if absent. Do not commit raw PDFs to fix retrieval.

## Chunking rules (v1)

| Source | Include? | Notes |
|--------|----------|--------|
| `wiki/**/*.md` | Yes | Skip [`wiki/_templates/`](../wiki/_templates/). |
| `wiki/index.md` | Yes | Navigation text; lower weight in eval if needed. |
| `normalized/extracts/*_p1-2.txt` | Optional (`--include-extracts`) | Only if present on disk; chunks tagged `source_type: extract`. |

Split each file on markdown `##` headings (level-2). First chunk may have empty heading (preamble). Strip YAML frontmatter from body text before splitting.

**Stable ids:** `chunk_id = sha256( wiki_path + "\n" + section_heading + "\n" + str(index) )[:16]` (see [`scripts/build_chunks.py`](../scripts/build_chunks.py)).

## Index artifacts

| File | Purpose |
|------|---------|
| `indexes/chunks.jsonl` | One JSON object per line: chunk metadata + `text`. |
| `indexes/bm25.pkl` | Pickled BM25 + chunk id order ([`scripts/bm25_okapi.py`](../scripts/bm25_okapi.py)). |
| `indexes/vectors.json.gz` | Gzip JSON: `vectors`, `chunk_ids`, `model` label. |
| `indexes/embedding_manifest.json` | Backend (`hash` vs `sentence_transformers`), model id, dimension. |
| `indexes/manifest.json` | Build timestamp, chunk count, script versions. |

Large binaries may be **gitignored**; always regenerate in CI or locally.

## Commands

From repo root (**Python 3.10+**; default path uses **stdlib only** — no `pip install` required):

```bash
# 1) Build chunk manifest (wiki + optional extracts)
python3 scripts/build_chunks.py
python3 scripts/build_chunks.py --include-extracts   # if extracts exist locally

# 2) Lexical index (BM25, pure Python)
python3 scripts/build_bm25.py

# 3) Dense vectors — default: deterministic hash embedding (fast, no extra deps)
python3 scripts/build_vectors.py
# Optional semantic embeddings (install sentence-transformers first):
#   pip install -r requirements-phase5.txt
#   python3 scripts/build_vectors.py --backend sentence_transformers

# 4) Query
python3 scripts/search_hybrid.py "ReaxFF LATP solid electrolyte" --top-k 10

# 5) Benchmark
python3 scripts/eval_retrieval.py --output outputs/phase5_retrieval_report.md
```

## Hybrid scoring

- **RRF (default):** `RRF_score(d) = sum 1/(k + rank_i)` across lexical and dense ranked lists (`k=60` default).
- **Weights:** tune `lex_weight` / `dense_weight` only after baseline numbers in [`outputs/phase5_retrieval_report.md`](../outputs/phase5_retrieval_report.md).

## KPI alignment

See [`PHASE0.md`](PHASE0.md): retrieval benchmark pass rate targets apply to the **frozen** set in [`benchmarks/v1_frozen.json`](benchmarks/v1_frozen.json). This is a **starting** gold set; extend with maintainer labels.

## Troubleshooting

| Symptom | Action |
|---------|--------|
| Empty extracts | Omit `--include-extracts`; wiki-only chunks still work. |
| OOM on `build_vectors.py` | Reduce batch size in script or use smaller model in `embedding_manifest`. |
| Low recall | Increase `top_k`, add synonyms to queries, or enrich wiki text (Phase 4), not index “fixes” that invent content. |

## Handoff

- **Phase 4:** [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md)
- **Benchmark pool:** [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md)
- **Frozen v1 eval:** [`benchmarks/v1_frozen.json`](benchmarks/v1_frozen.json) + [`benchmarks/V1_FROZEN.md`](benchmarks/V1_FROZEN.md)
