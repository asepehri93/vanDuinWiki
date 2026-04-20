# Phase 4 runbook — LLM-led wiki compilation

This runbook defines how the knowledge base **grows from registered PDFs into a linked wiki**. It aligns with the master plan’s Phase 4 goal (“compile raw documents into a strongly linked research wiki”) with an explicit split: **semantic work is LLM-led**; **Python (or shell) is only for bulk mechanical tasks** — see [`AGENTS.md`](../AGENTS.md) section *LLM vs mechanical tooling*.

## Policy reminder

| Owner | Work |
|--------|------|
| **LLM or human** | Summaries, methods/findings, limitations, `canonical_tags`, concept/material/forcefield/protocol pages, `claims`, wikilinks, bibliography fixes that require judgment |
| **Script (optional)** | Hashing, path lists, JSONL append, frontmatter shape checks, counting files, building tables of filenames — **no** automated invention of scientific claims or tag assignments for production pages |

## Preconditions

- [`raw/MANIFEST.jsonl`](../raw/MANIFEST.jsonl) and [`normalized/papers/{slug}.json`](../normalized/papers/) stubs (Phase 3 mechanical pass).
- Stable `paper_id` = `paper:{slug}`; slug matches JSON filename stem and future `wiki/papers/{slug}.md`.
- [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml) and [`AGENTS.md`](../AGENTS.md) frontmatter rules.
- Optional: [`normalized/extracts/{slug}_p1-2.txt`](../normalized/extracts/) (local text snippets; gitignored) or read PDFs directly in the IDE/agent.

## Stages

```mermaid
flowchart LR
  sources[papers_and_normalized_stubs]
  llmRead[LLM_reads_PDF_or_extracts]
  wikiPages[wiki_papers_and_entities]
  enrich[LLM_cross_links_and_concepts]
  mech[optional_mechanical_validate_index]
  sources --> llmRead --> wikiPages --> enrich --> mech
```

### Stage A — Per-paper wiki pages (LLM)

For each paper (batch 5–20 at a time to fit context):

1. Open [`wiki/_templates/paper.md`](../wiki/_templates/paper.md).
2. From PDF and/or extract text + [`normalized/papers/{slug}.json`](../normalized/papers/) bibliography fields, fill:
   - One-paragraph summary, Methods, Findings, Limitations, Relevance to group, Citations / evidence anchors.
3. Set frontmatter: `id`, `title`, `updated`, `confidence`, **`canonical_tags`** (only ids from [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml)), `pdf_sha256` / `pdf_path` per [`AGENTS.md`](../AGENTS.md).
4. Save as [`wiki/papers/{slug}.md`](../wiki/papers/) (filename stem **must** equal slug).

### Stage B — Semantic updates to normalized JSON (LLM)

Update the matching [`normalized/papers/{slug}.json`](../normalized/papers/) **only** for semantic enrichment, for example:

- Fix or complete `bibliography` when the stub was wrong (cite source in commit message or a short `notes` field if you add one).
- Populate `entities_mentioned` with coarse strings or ids (materials, methods, FF names).
- Optional `claims` entries with `source_refs` for MAS — still **authored by LLM/human**, not by a summarizer script.

Do **not** bulk-fill claims with an untrusted automated extractor without review.

### Stage C — Entity and synthesis pages (LLM)

When evidence supports it (default: **≥3 papers** for a concept):

- Add [`wiki/concepts/`](../wiki/concepts/), [`wiki/materials/`](../wiki/materials/), [`wiki/forcefields/`](../wiki/forcefields/), [`wiki/protocols/`](../wiki/protocols/) pages using the matching templates.
- Every substantive statement on synthesis pages needs `source_refs` or citations per [`AGENTS.md`](../AGENTS.md).
- Optional [`wiki/debates/`](../wiki/debates/) only when disagreement is real and cited.

### Stage D — Cross-linking and index (LLM, optional mechanical assist)

- Add `[[wikilinks]]` between papers and entity pages; keep titles unique where possible.
- Refresh [`wiki/index.md`](../wiki/index.md) with curated sections (themes, “start here” lists).
- **Mechanical assist (allowed):** a script that lists `wiki/papers/*.md` and prints counts or a markdown table of **filenames only** — it must **not** generate thematic blurbs.

### Stage E — Quality gate

- LLM or human review before setting `confidence: high` on synthesis pages.
- Track progress against KPIs in [`PHASE0.md`](PHASE0.md) (coverage, connectivity, grounding).

## Batching strategy (~190 papers)

- **Wave 1:** Pilot 10–15 papers (diverse methods/materials); fix template and tag habits.
- **Wave 2–N:** Batches of 15–25 papers by subdomain (e.g. ReaxFF / oxides / batteries) to simplify cross-linking.
- **Wave final:** Concept and entity pages that span batches; second pass for orphan papers (no incoming links).

## Out of scope for Phase 4

- **Phase 5:** Hybrid retrieval, vector indexes under [`indexes/`](../indexes/) — not required to finish wiki pages.
- **Fully automated** wiki generation without LLM review of scientific content — not the default process here.

## Acceptance pointers

- Connectivity and grounding targets: [`PHASE0.md`](PHASE0.md).
- Benchmark questions for eventual retrieval tests: [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md).
