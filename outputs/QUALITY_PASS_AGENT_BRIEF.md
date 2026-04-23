# Final paper wiki quality pass — sub-agent brief

> Status: execution completed (all 5 waves processed); this brief is retained as the audit/playbook for reruns.

**Goal:** Reader-facing, **PDF-grounded** prose on every assigned `wiki/papers/{slug}.md`. Replace **thin** or **mechanical** filler (validator blocks, “indexed excerpt” hand-waving, duplicate blueprint bullets) with **integrated** `## Summary`, `## Methods`, and `## Findings` that a domain reader can use without opening tricks.

**Authority:** [`AGENTS.md`](../AGENTS.md) — especially *Scientific claims must trace to publications*, *Paper `## Methods` blueprint*, *Paper `## Findings` blueprint*, and *Corpus / KB honesty*.

## Sources (in order)

1. **`pdf_path`** in the page YAML (under repo root). Read the PDF when the file exists.
2. **`normalized/extracts/{slug}_*.txt`** if present (local cache; may be gitignored).
3. **`normalized/papers/{slug}.json`** for bibliography pointers and `extraction_quality`.
4. If the PDF is **missing** locally, state that under **`## Limitations`** and only summarize what the extract/JSON allows — **no invented chemistry**.

## Edits to perform (every slug in your batch file)

1. **Remove** HTML comment wrappers `<!-- blueprint-slot-coverage:auto -->` … `<!-- /blueprint-slot-coverage:auto -->` (and similar). **Merge** any still-useful facts into normal markdown under `## Methods` / `## Findings`.
2. **Rewrite** `## Methods` into the **applicable AGENTS blocks** (MD application, FF training, static QM, and/or review/non-sim) as **continuous prose or tight sub-bullets** — not a checklist of “language appears in indexed text”. Every required line item must be **either** answered from the paper **or** explicit **`N/A — …`** with a one-line reason tied to the source (e.g. *not in SI we have*, *experimental-only paper*).
3. **Rewrite** `## Findings` per AGENTS: outcomes/mechanisms, comparisons, sensitivity/levers, limitations/outlook as **authored**, corpus-honesty line if SI/galley/thin.
4. **Tighten** `## Summary` so it matches the expanded Methods/Findings (no contradictions).
5. **Frontmatter:** bump `updated` to the pass date; adjust `confidence` if you materially improved grounding; **do not** remove `id`, `type`, `doi`, `pdf_path`, `canonical_tags` without cause.
6. **Do not** add new scientific claims beyond what the PDF/extract supports. **Paraphrase**; prefer **units and numbers** when the source gives them.
7. **Sibling / non-primary PDFs:** If [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](../docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) applies, keep navigation honesty and point to the **version-of-record** sibling where relevant.

## After your batch (your slice only)

```bash
python3 scripts/validate_paper_methods_blueprint.py --check-slug SLUG   # per file if needed
```

When **all** slugs in your list are done, run once from repo root:

```bash
python3 scripts/validate_paper_methods_blueprint.py -o outputs/paper_methods_blueprint_backlog.md
python3 scripts/report_paper_richness.py --min-words 400 -o outputs/paper_richness_backlog.md
```

**Do not** run `build_chunks.py` or `mkdocs` unless you are the **coordinator** after a full wave; reduces lock contention.

## Return to coordinator

Reply with: wave/part id, **slugs completed**, **slugs skipped/blocked** (and why), and any **systemic issues** (missing PDFs, bad paths).
