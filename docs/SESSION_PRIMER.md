# Session Primer — vanDuinWiki

This primer is the canonical startup context for any new blank chat session working on this repository. Use it to restore project intent, constraints, workflows, and current quality gates before making changes.

## 1) Project identity and mission

`vanDuinWiki` is a computational chemistry knowledge base built from local PDF sources under `papers/`. The repository serves two audiences simultaneously:

- Website readers who need grounded, understandable scientific synthesis.
- MAS and retrieval pipelines that need stable IDs, evidence anchors, and machine-tractable structure.

The operating principle is evidence-first synthesis: claims in wiki pages must remain traceable to corpus publications and linked paper pages.

## 2) Fast orientation map

- Primary operator contract: [`AGENTS.md`](../AGENTS.md)
- Workflow by phase:
  - Phase 0 KPIs: [`PHASE0.md`](PHASE0.md)
  - Phase 3 profiling: [`PHASE3_RUNBOOK.md`](PHASE3_RUNBOOK.md)
  - Phase 4 curation: [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md)
  - Phase 5 retrieval: [`PHASE5_RUNBOOK.md`](PHASE5_RUNBOOK.md)
- Ongoing roadmap: [`MASTER_PLAN.md`](MASTER_PLAN.md)

Repository role map:

- `papers/`: source PDFs (read-only as primary sources).
- `raw/`: ingest manifests.
- `normalized/`: machine-oriented records and extraction pointers.
- `wiki/`: human-facing pages (papers, concepts/themes, debates, protocols).
- `indexes/`: retrieval artifacts.
- `outputs/`: reports and operator artifacts.

## 3) Non-negotiable rules

1. Do not invent scientific claims, numbers, mechanisms, or citations.
2. Keep substantive synthesis claims anchored through `source_refs` or linked `paper:` pages.
3. Keep YAML schemas and stable IDs valid (`id`, `type`, canonical tags, paths).
4. Use canonical taxonomy IDs only from [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml); unresolved terms stay in `candidate_tags`.
5. Keep website-facing synthesis prose in full, grounded sentences; avoid shorthand fragments and template filler.
6. Keep navigation-only pages free of uncited scientific assertions.

## 4) Page-type contracts (authoring summary)

Detailed contracts are in `AGENTS.md`; this section is a startup shorthand.

### Paper pages (`wiki/papers/*.md`)

- Required scientific body sections: `## Summary`, `## Methods`, `## Findings`.
- Methods and findings follow the mandatory blueprint (MD, FF training, DFT-only, review applicability).
- Use explicit `N/A — ...` when details are not stated in source material.

### Theme hubs (`wiki/concepts/theme-*.md`)

- Corpus-scale synthesis hubs with:
  - scope,
  - literature review by subtheme,
  - cross-cutting analysis,
  - debates/limitations,
  - corpus gaps,
  - methods caveats,
  - retrieval note.

### Cross-cutting entry-point hubs (`wiki/concepts/entrypoint-*.md` and selected concept hubs)

- Query-first navigation pages with:
  - scope/user intent,
  - start-here pathways,
  - decision levers,
  - canonical starter papers,
  - links to protocols/debates,
  - failure/pitfall guidance,
  - MAS retrieval note.

### Debate pages (`wiki/debates/*.md`)

- Evidence-structured disagreements with explicit position mapping, scope conditions, shared ground, and practical decision implications.

### Protocol pages (`wiki/protocols/*.md`)

- Reusable playbooks with inputs, procedure, validation checks, failure modes, variants, outputs/downstream links, and evidence anchors.

## 5) Current synthesis-layer baseline

The synthesis-layer wave has already been executed and documented:

- Blueprint summary: [`outputs/SYNTHESIS_LAYER_BLUEPRINTS.md`](../outputs/SYNTHESIS_LAYER_BLUEPRINTS.md)
- Completion report: [`outputs/SYNTHESIS_LAYER_COMPLETION.md`](../outputs/SYNTHESIS_LAYER_COMPLETION.md)

As of the last completed pass:

- paper methods/findings backlog: `0` failing.
- paper richness backlog (`>= 400` words): `0`.
- paper-to-theme assignment: `0` unassigned.

## 6) Deterministic quality gates (must run before major handoff)

From repo root:

```bash
python3 scripts/validate_paper_methods_blueprint.py -o outputs/paper_methods_blueprint_backlog.md
python3 scripts/report_paper_richness.py --min-words 400 -o outputs/paper_richness_backlog.md
python3 scripts/check_paper_theme_coverage.py
python3 scripts/generate_papers_indexes.py
python3 scripts/build_chunks.py
mkdocs build --strict
```

Expected baseline for synthesis-complete state:

- `paper_methods_blueprint_backlog.md`: `0 failing`
- `paper_richness_backlog.md`: `0 backlog`
- `paper_theme_coverage.md`: `0 unassigned`
- `mkdocs build --strict`: pass

## 7) Session startup checklist

At the start of a new chat:

1. Read `AGENTS.md` and this primer.
2. Read latest output baselines:
   - `outputs/paper_methods_blueprint_backlog.md`
   - `outputs/paper_richness_backlog.md`
   - `outputs/paper_theme_coverage.md`
3. Inspect `git status` for existing in-progress work.
4. Confirm whether task is:
   - paper-level curation,
   - synthesis-layer authoring,
   - maintenance/indexing,
   - documentation/governance update.
5. Execute only the smallest required scope, then re-run relevant gates.

## 8) Session closeout checklist

Before committing:

1. Re-run the relevant deterministic checks.
2. Regenerate index/chunk artifacts if wiki metadata/body changed.
3. Build site with `mkdocs build --strict`.
4. Update operational docs if contracts or workflow changed.
5. Summarize changed files, risks, and follow-up items in `outputs/` when needed.

## 9) Common failure modes and how to avoid them

- **Template pass but weak science**: avoid validator keyword stuffing; write grounded protocol/finding detail.
- **Uncited synthesis drift**: ensure `source_refs` and linked `paper:` anchors are present.
- **Schema drift**: keep `id`, `type`, and canonical tags valid.
- **Navigation invisibility**: update `mkdocs.yml` nav when adding major concept/debate/protocol pages.
- **Theme coverage regression**: run `check_paper_theme_coverage.py` after taxonomy/theme updates.
- **Confusing non-primary PDFs**: respect [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) and keep corpus honesty explicit.

## 10) Priority queue when no explicit task is given

1. Resolve any nonzero deterministic backlog.
2. Improve evidence depth in high-traffic theme and entry-point hubs.
3. Expand debates where decision-critical disagreement remains unresolved.
4. Strengthen protocol pages with clearer acceptance criteria and failure mitigations.
5. Run retrieval evaluation loops after substantial content/link updates.
