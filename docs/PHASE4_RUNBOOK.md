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

For each paper, work in **batches** so context stays manageable (older guidance: 5–20 per *conversation*; corpus-wide passes use **larger batch *lists*** split across parallel agents):

1. Open [`wiki/_templates/paper.md`](../wiki/_templates/paper.md).
2. From **PDF + SI** (when available in `papers/` / `raw/papers/`) and/or extract text + [`normalized/papers/{slug}.json`](../normalized/papers/) bibliography fields, fill:
   - Summary, Methods, Findings, Limitations, Relevance to group, Citations / evidence anchors.
   - **MAS / reproducibility:** follow [`AGENTS.md`](../AGENTS.md) *MAS / reproducibility depth* — **Methods** must carry enough **FF-training** and **MD protocol** detail (software, ensembles, timesteps, training sets when stated) for downstream automation; **Findings** in full sentences with units, not stub bullets. If only p1–2 extracts exist locally, say so.
3. Set frontmatter: `id`, `title`, `updated`, `confidence`, **`canonical_tags`** (only ids from [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml)), `pdf_sha256` / `pdf_path` per [`AGENTS.md`](../AGENTS.md). **YAML:** If the title contains LaTeX-style backslashes (e.g. `Zn\(_{1-x}\)`), use a **single-quoted** `title:` string so `yaml.safe_load` does not fail (double-quoted YAML strings treat `\(` as an invalid escape).
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

### Rich paper pages + theme hub waves (corpus-deepening)

After the first-pass wiki exists, operators may run **Stage A** of [`MASTER_PLAN.md`](MASTER_PLAN.md) *Phase: rich papers + analysis-driven theme hubs*: use [`scripts/report_paper_richness.py`](../scripts/report_paper_richness.py) to list thin standalone `wiki/papers/*.md` entries ([`outputs/paper_richness_backlog.md`](../outputs/paper_richness_backlog.md)), curate in **waves** (see [`outputs/STAGE_A_PAPER_ENRICHMENT.md`](../outputs/STAGE_A_PAPER_ENRICHMENT.md)), then refresh [`scripts/generate_papers_indexes.py`](../scripts/generate_papers_indexes.py) and [`scripts/build_chunks.py`](../scripts/build_chunks.py) after substantive batches.

Theme hub upgrades should follow **pre-writing artifacts** in [`outputs/theme_plans/`](../outputs/theme_plans/) and the expanded template in [`AGENTS.md`](../AGENTS.md) (*Theme hub pages*) before large prose edits.

### Post-first-pass: connectivity and theme hubs (Wave 2)

After every `wiki/papers/{slug}.md` has real prose (Phase 4 first pass **done**), the graph still needs **incoming links** from synthesis pages to meet the Phase 0 **connectivity** KPI.

1. **Measure** — Run the mechanical report (no invented science):

   ```bash
   python3 scripts/report_paper_connectivity.py --output outputs/connectivity_report.md
   ```

2. **Survey themes** — For each major bucket in [`wiki/concepts/themes-index.md`](../wiki/concepts/themes-index.md), expand the matching [`wiki/concepts/theme-*.md`](../wiki/concepts/) pages: **Literature review (this knowledge base)** lists only papers already in the repo, with `[[paper-slug]]` wikilinks and `source_refs` where the template requires them ([`AGENTS.md`](../AGENTS.md)).

3. **Close orphans** — Papers with no incoming link from `concepts/`, `materials/`, `forcefields/`, or `protocols/` should gain at least one such link (often via a theme hub “Representative entry points” or a short Reader-notes cross-link on the paper page pointing back to a hub).

4. **Debates and corpus-scoped surveys** — New or expanded [`wiki/debates/`](../wiki/debates/) pages and long-form theme narrative **belong in Phase 4** when evidence supports them. They are **not** “Phase 8” work; Phase 8 is **export policy** only ([`PHASE8_EXPORT.md`](PHASE8_EXPORT.md)).

5. **Re-run retrieval** — After large link additions, rebuild chunks and indexes per [`PHASE5_RUNBOOK.md`](PHASE5_RUNBOOK.md) and [`MASTER_PLAN.md`](MASTER_PLAN.md).

## Batching strategy (full corpus, ~1278 papers)

**Yes — 200 PDFs per “pass” is a good default** for *throughput*: it defines how many paper pages you aim to finish before rotating to the next slice. You do **not** put 200 full articles in one LLM context window; you **split the workload across parallel agents or sessions**, each taking a batch list.

1. **Generate batch lists** (one slug per line; default **200** slugs per file):

   ```bash
   python3 scripts/paper_curation_batches.py --batch-size 200 --mode pending
   ```

   Output: `outputs/curation_batches/batch-001.txt` … `manifest.json`, `_README.md`.  
   `--mode pending` includes pages that still have `phase4-stub-pending-curation` **or** the mechanical stub phrase in the body. After you curate a page, drop the stub tag and replace stub prose — the next run will **exclude** it from `pending`.

   When a batch is **operator-approved**, add an entry under `approvals` in `outputs/curation_batches/manifest.json` and a row in `outputs/curation_batches/_README.md` so later passes do not silently overwrite the baseline.

2. **Parallelism:** Assign **`batch-001.txt`** to agent A, **`batch-002.txt`** to agent B, etc. Seven batches cover ~1.4k slugs at 200 each.

3. **Full pass including already curated pages** (e.g. second editorial sweep):

   ```bash
   python3 scripts/paper_curation_batches.py --batch-size 200 --mode all
   ```

4. **Wave 0 (recommended once):** Pilot **10–15** papers in a single thread to lock template and tagging habits before scaling.

5. **Later:** Concept/entity pages (`wiki/concepts/`, …) and orphan papers with no incoming links — still LLM-led; optional subdomain ordering (ReaxFF / oxides / batteries) within a batch if that helps cross-linking.

## Out of scope for Phase 4

- **Phase 5:** Hybrid retrieval, vector indexes under [`indexes/`](../indexes/) — not required to finish wiki pages.
- **Fully automated** wiki generation without LLM review of scientific content — not the default process here.

## Acceptance pointers

- Connectivity and grounding targets: [`PHASE0.md`](PHASE0.md).
- Full roadmap: [`MASTER_PLAN.md`](MASTER_PLAN.md).
- Benchmark questions for eventual retrieval tests: [`benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](benchmarks/WARMUP_CANDIDATE_QUESTIONS.md).
