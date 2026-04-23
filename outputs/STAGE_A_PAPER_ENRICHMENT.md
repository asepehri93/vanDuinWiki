# Stage A — rich paper pages (ongoing)

## Mechanical backlog

- **Script:** [`scripts/report_paper_richness.py`](../scripts/report_paper_richness.py)
- **Report:** [`paper_richness_backlog.md`](paper_richness_backlog.md) (default `--min-words 400` + required `## Summary` / `## Methods` / `## Findings`)
- **Exceptions:** Cross-check [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](../docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) before expanding SI-only or duplicate slugs.

## Batch files

Generate the next wave from the backlog:

```bash
python3 scripts/report_paper_richness.py --min-words 400 \
  --write-batch outputs/curation_batches/rich-paper-wave-NNN.txt --batch-size 100
```

Assign each wave to parallel LLM sessions (same curation standards as Phase 4: PDF/extract-grounded prose per [`AGENTS.md`](../AGENTS.md)).

## Waves

| Wave | File | Status |
|------|------|--------|
| 001 | [`curation_batches/rich-paper-wave-001.txt`](curation_batches/rich-paper-wave-001.txt) | First enrichment pass (100 thinnest slugs) |
| 002 | [`curation_batches/rich-paper-wave-002.txt`](curation_batches/rich-paper-wave-002.txt) | Next 100 from backlog (regenerate if stale) |
| 003 | [`curation_batches/stage-a-wave-003-full.txt`](curation_batches/stage-a-wave-003-full.txt) (also [`stage-a-wave-003-batch-01.txt`](curation_batches/stage-a-wave-003-batch-01.txt) … [`batch-12.txt`](curation_batches/stage-a-wave-003-batch-12.txt)) | **360** slugs in **12×30** parallel passes; follow-up pass brought all 360 to mechanical richness (≥400 words + required headings). Regenerate backlog after later waves. |
| 004 | [`curation_batches/stage-a-wave-004-full.txt`](curation_batches/stage-a-wave-004-full.txt) (batches [`stage-a-wave-004-batch-01.txt`](curation_batches/stage-a-wave-004-batch-01.txt) … [`batch-12.txt`](curation_batches/stage-a-wave-004-batch-12.txt)); resume lists [`stage-a-wave-004-resume-final.txt`](curation_batches/stage-a-wave-004-resume-final.txt) | **360** slugs; interrupted batches **08–09–11** completed via resume passes; **71** slugs needed a second mechanical pass before all **360** cleared `report_paper_richness.py`. |
| 005 | [`curation_batches/stage-a-wave-005-full.txt`](curation_batches/stage-a-wave-005-full.txt) (batches [`stage-a-wave-005-batch-01.txt`](curation_batches/stage-a-wave-005-batch-01.txt) … [`batch-12.txt`](curation_batches/stage-a-wave-005-batch-12.txt); **11×30 + 24**); resume [`stage-a-wave-005-resume-final.txt`](curation_batches/stage-a-wave-005-resume-final.txt) (60 slugs) | **354** slugs (remaining thin entries at `--min-words 400` when the wave was cut); **60** needed a follow-up mechanical pass after parallel batches; all **354** now clear `report_paper_richness.py`. |
| Final quality pass (5×15) | [`curation_batches/quality-final-wave1-part01-of-15.txt`](curation_batches/quality-final-wave1-part01-of-15.txt) … [`quality-final-wave5-part15-of-15.txt`](curation_batches/quality-final-wave5-part15-of-15.txt) | Reader-facing cleanup complete across all `paper:` slugs; final coordinator checks report `paper_methods_blueprint_backlog.md` = **0 failing of 1278** and `paper_richness_backlog.md` = **0 backlog of 1278**. |

Re-run `report_paper_richness.py` after each wave to refresh counts. **Exit criterion:** backlog count reaches **zero** at the chosen threshold, except for documented short roles in [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](../docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

### Methods / protocol depth (all `paper:` pages)

- **Spec:** [`AGENTS.md`](../AGENTS.md) — **Paper `## Methods` blueprint** (blocks **1 — MD application**, **2 — Force-field training**, **3 — Static QM/DFT-only**, **4 — Reviews**) and **Paper `## Findings` blueprint** (outcomes, comparisons, levers, limitations/outlook, corpus honesty). Each checklist line must be **filled** or marked **`N/A — …`**.
- **Batch lists:** [`curation_batches/methods-depth-part-01-of-15.txt`](curation_batches/methods-depth-part-01-of-15.txt) … [`part-15-of-15.txt`](curation_batches/methods-depth-part-15-of-15.txt) enumerate every **`type: paper`** slug under `wiki/papers/` (15 parallel passes; `wiki/papers/index.md` is navigation-only and is not in those lists). If the mechanical **≥400 word** floor slips during a depth edit, use [`curation_batches/methods-mech-resume-400.txt`](curation_batches/methods-mech-resume-400.txt) (and `methods-mech-resume-400-part-*.txt` splits) as the repair list.
- **Verbatim extract cleanup:** [`scripts/strip_verbatim_extract_blocks.py`](../scripts/strip_verbatim_extract_blocks.py) removes mistaken `### Extract-based cues (verbatim excerpt)` blockquotes (publisher boilerplate pasted from extracts) while leaving checklist prose intact.

### Browsing the full corpus on the site

- **Interactive:** [`wiki/concepts/paper-corpus-browser.md`](../wiki/concepts/paper-corpus-browser.md) + generated [`wiki/javascripts/papers_corpus.json`](../wiki/javascripts/papers_corpus.json) (run `python3 scripts/generate_papers_indexes.py` after metadata changes).
