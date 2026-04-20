# Phase 3 runbook — corpus scan and profiling

**Scope:** This phase is **mechanical**: paths, hashes, and optional first-page text snippets for inventory. It does **not** perform scientific curation (what each paper is about, `canonical_tags`, or wiki prose). That work is **Phase 4 / LLM** — [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md).

This runbook describes how PDFs under `papers/` are registered, hashed, and profiled. Normative ingest fields remain in [`AGENTS.md`](../AGENTS.md).

## Prerequisites

- Python 3.10+ recommended.
- Vendored [`pypdf`](../.vendor/pypdf) on `PYTHONPATH` (the script adds `REPO_ROOT/.vendor` automatically).

## One-shot profiling

From the repository root:

```bash
python3 scripts/corpus_profile.py
```

- **Dry run** (count PDFs only, no writes):

  ```bash
  python3 scripts/corpus_profile.py --dry-run
  ```

## Outputs

| Artifact | Purpose |
|----------|---------|
| [`raw/MANIFEST.jsonl`](../raw/MANIFEST.jsonl) | One JSON object per PDF: `source_path`, `sha256`, `ingested_at`, `paper_id` |
| [`normalized/papers/{slug}.json`](../normalized/papers/) | Bibliography + extraction quality + `wiki_path` stub |
| [`normalized/extracts/{slug}_p1-2.txt`](../normalized/extracts/) | First two pages text (local cache; **gitignored**) |
| [`normalized/corpus_summary.json`](../normalized/corpus_summary.json) | Aggregate histograms and top title words |
| [`outputs/corpus_profile_YYYY-MM.md`](../outputs/) | Human-readable profile |
| [`outputs/ingest_exceptions.md`](../outputs/ingest_exceptions.md) | Read errors and duplicate-hash groups |

## `paper_id` slug rules (deterministic)

1. **Metadata first:** Read PDF info (`title`, `author`, `subject`) via pypdf.
2. **Year:** From metadata date string, first pages text, or filename (`19xx` / `20xx`).
3. **Author token:** First author’s family name (heuristic from `Author` string); if missing, first token of filename stem.
4. **Title tokens:** Up to two significant words from metadata title (stopwords removed).
5. **Venue hint:** Short token from subject line or common journal hints in text.
6. **Base slug:** `{year}{author}_{venue-token}-{title-words}` (lowercase, hyphenated), or `noyear-{author}-{filename}` if year missing.
7. **Uniqueness:** If the base collides with an already-assigned slug, append `-2`, `-3`, …

Slugs can look like `venue-paper` when metadata is thin (e.g. proofs); that is expected—Phase 4 can rename display titles without changing `paper_id` if needed (discouraged).

## Rerun policy

- Re-running **overwrites** `MANIFEST.jsonl`, all `normalized/papers/*.json`, extracts, and aggregate outputs.
- Commit `MANIFEST.jsonl` and normalized JSON; **do not commit** `normalized/extracts/` (see [`.gitignore`](../.gitignore)).

## Handoff to Phase 4

- Stable `paper_id` and bibliography JSON feed wiki page generation and linking.
