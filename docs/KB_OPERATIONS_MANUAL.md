# Knowledge Base Operations Manual

This manual is the authoritative operating guide for maintaining and extending `vanDuinWiki`. It covers technical workflows, writing standards, quality gates, and release discipline.

## 1) Operating model

The project separates semantic and mechanical work:

- Semantic (LLM/human): synthesis writing, scientific judgment, taxonomy assignment decisions, debate/protocol interpretation.
- Mechanical (scripts/shell): file registration, deterministic reports, index/chunk generation, structural checks.

Never use scripts to generate scientific conclusions, production tag meaning, or unreviewed claims.

## 2) Core assets and responsibilities

- Governance contract: [`AGENTS.md`](../AGENTS.md)
- Roadmap: [`MASTER_PLAN.md`](MASTER_PLAN.md)
- Runbooks:
  - Phase 3: [`PHASE3_RUNBOOK.md`](PHASE3_RUNBOOK.md)
  - Phase 4: [`PHASE4_RUNBOOK.md`](PHASE4_RUNBOOK.md)
  - Phase 5: [`PHASE5_RUNBOOK.md`](PHASE5_RUNBOOK.md)
- Synthesis playbooks:
  - [`outputs/SYNTHESIS_LAYER_BLUEPRINTS.md`](../outputs/SYNTHESIS_LAYER_BLUEPRINTS.md)
  - [`outputs/SYNTHESIS_LAYER_COMPLETION.md`](../outputs/SYNTHESIS_LAYER_COMPLETION.md)

## 3) Ingest and metadata maintenance (new PDFs)

When new papers are added:

1. Register source files and manifest records per Phase 3 runbook.
2. Refresh normalized paper stubs and extraction pointers.
3. Sync wiki frontmatter from normalized records where applicable.
4. Create or update the corresponding `wiki/papers/{slug}.md`.
5. Add canonical tags and optional paper keywords using controlled taxonomy.
6. If PDF is non-primary (SI, proof, duplicate), update:
   - [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md)
   - paper-page corpus honesty text and sibling link guidance.

## 4) Paper-page curation maintenance

Use paper methods/findings contracts from `AGENTS.md`:

- Write source-grounded `Summary`, `Methods`, and `Findings`.
- Fill every applicable methods/findings slot with either reported detail or explicit `N/A — ...` rationale.
- Keep limitations and corpus honesty explicit for thin or non-primary sources.

Deterministic paper-quality checks:

```bash
python3 scripts/validate_paper_methods_blueprint.py -o outputs/paper_methods_blueprint_backlog.md
python3 scripts/report_paper_richness.py --min-words 400 -o outputs/paper_richness_backlog.md
```

Target operational state:

- `paper_methods_blueprint_backlog.md`: `0 failing`
- `paper_richness_backlog.md`: `0 backlog`

## 5) Synthesis-layer maintenance (themes, entry points, debates, protocols)

### Theme hubs

- Keep section contract intact (scope, literature review, analysis, debates/limitations, gaps, methods caveats, retrieval note).
- Maintain `source_refs` and `supported_by` coherence.
- Keep synthesis corpus-scoped; avoid uncited extrapolation.

### Entry-point hubs

- Keep query-first pathways current with active themes, debates, and protocols.
- Ensure practical “where to start” routes remain explicit.

### Debate pages

- Keep position/evidence mapping explicit and balanced.
- Prefer decision-relevant implications over rhetorical contrast.

### Protocol pages

- Keep procedures executable and validation criteria concrete.
- Update failure modes as recurring issues are observed.

## 6) Paper-to-theme assignment gate

Every paper must map to at least one theme assignment.

Run:

```bash
python3 scripts/check_paper_theme_coverage.py
```

Artifacts:

- `outputs/paper_theme_coverage.md`
- `outputs/paper_theme_assignments.json`

Operational target: `0 unassigned`.

## 7) Taxonomy governance maintenance

- Canonical tags come only from [`taxonomy/canonical_tags.yml`](../taxonomy/canonical_tags.yml).
- Use candidate tags for unresolved concepts and promote through governance process.
- Keep synonyms and relation IDs updated when taxonomy changes.

Do not silently repurpose existing canonical tags with changed meaning.

## 8) Retrieval/index maintenance

After substantial wiki updates:

```bash
python3 scripts/generate_papers_indexes.py
python3 scripts/build_chunks.py
```

Then run retrieval workflows from Phase 5 runbook (`build_bm25.py`, `build_vectors.py`, `eval_retrieval.py`) as needed.

## 9) Website maintenance

When adding major concept/debate/protocol pages:

1. Add them to `mkdocs.yml` navigation where appropriate.
2. Validate site build:

```bash
mkdocs build --strict
```

Keep navigation-only pages free from uncited scientific statements.

## 10) Writing style and tone standards

Use website-ready, grounded prose:

- Full sentences with explicit assumptions and boundaries.
- Objective, third-person voice.
- No shorthand fragments that obscure conditions.
- No unsupported generic claims.
- Explicit uncertainty language where source support is partial.

For synthesis pages, prioritize clarity and educational flow while preserving evidentiary discipline.

## 11) Quality gates and definition of done

### Done for a paper-page maintenance wave

- Paper methods blueprint: clean.
- Richness threshold: clean.
- Frontmatter schema intact.

### Done for a synthesis-page wave

- Blueprint section contract satisfied.
- `source_refs` and narrative evidence coherence checked.
- No broken nav discoverability for newly added major pages.

### Done for a release

- Deterministic reports regenerated and passing.
- Index/chunk artifacts refreshed.
- Strict site build passing.
- Operational docs updated.

## 12) Documentation governance

Update docs whenever process or quality gates change:

- `AGENTS.md` for rule/contract changes.
- Phase runbooks for workflow changes.
- `MASTER_PLAN.md` for roadmap status changes.
- `outputs/` completion reports for major execution waves.

## 13) Incident playbooks

### Validator spike

1. Regenerate backlog artifacts.
2. Identify whether failure is template drift, source-thin pages, or frontmatter corruption.
3. Fix by smallest coherent batch and re-run checks.

### Coverage regression

1. Run `check_paper_theme_coverage.py`.
2. Resolve unassigned papers via deterministic mapping and/or manual curation.
3. Re-run and archive clean report.

### Website invisibility

1. Verify page exists under `wiki/`.
2. Verify nav inclusion in `mkdocs.yml`.
3. Run strict build and inspect warnings/errors.

## 14) Release checklist (push-ready)

1. `git status` cleanly reflects intended scope.
2. Run deterministic quality gates:
   - methods blueprint
   - richness
   - theme coverage
3. Regenerate index/chunk artifacts where applicable.
4. `mkdocs build --strict`.
5. Update docs and completion artifacts.
6. Commit with a why-focused message and push.

## 15) Minimal command crib sheet

```bash
# Paper quality gates
python3 scripts/validate_paper_methods_blueprint.py -o outputs/paper_methods_blueprint_backlog.md
python3 scripts/report_paper_richness.py --min-words 400 -o outputs/paper_richness_backlog.md

# Theme coverage gate
python3 scripts/check_paper_theme_coverage.py

# Retrieval/site refresh
python3 scripts/generate_papers_indexes.py
python3 scripts/build_chunks.py
mkdocs build --strict
```
