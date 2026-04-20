# raw — ingest scope and manifests

- **`MANIFEST.jsonl`**: one JSON object per line. Each line registers a source file (typically a PDF under `papers/`) as in-scope for the KB. This is the canonical list of ingested sources.
- **`MANIFEST.example.jsonl`**: example lines for format reference (not loaded by default).
- **`papers/`** (optional): reserved if you later symlink or copy PDFs here for a single `raw/` tree; v1 may keep PDFs only under repo-root `papers/`.

Do **not** modify PDF bytes as part of “wiki edits”; treat sources as immutable. Corrections belong in `normalized/` and `wiki/`.

See [`AGENTS.md`](../AGENTS.md) for the full `MANIFEST.jsonl` schema.
