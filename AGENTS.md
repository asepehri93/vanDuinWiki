# AGENTS.md — Knowledge base schema and operator rules

This file is the **single operator manual** for humans and LLM agents working on vanDuinWiki. It defines information architecture, ingest policy, wiki page contracts, linking rules, and the normalized record shape for downstream pipelines (Phase 4+).

## What this is

A **computational chemistry** knowledge base for a research group: educational synthesis, cross-linked concepts, and a **MAS-ready** structured layer (`normalized/`, future `indexes/`). It is built from PDFs under `papers/` and must remain **evidence-grounded** (claims cite sources).

## LLM vs mechanical tooling

| Layer | Owner | Examples |
|-------|--------|----------|
| **Semantic** | **LLM or human** | Paper summaries, methods/findings, `canonical_tags`, concept and entity pages, `claims`, wikilinks, resolving `candidate_tags`, bibliography judgment |
| **Mechanical / bulk** | **Python or shell (optional)** | SHA-256, listing paths, appending `MANIFEST.jsonl`, frontmatter shape validation, file counts, tables of filenames **without** thematic interpretation |

**Not allowed:** using Python (or any script) to **invent** scientific claims, summaries, or production tag assignments without an LLM or human authoring that content. [`scripts/corpus_profile.py`](scripts/corpus_profile.py) is **mechanical registration** only (Phase 3); it does not replace LLM-led wiki compilation (Phase 4).

Full Phase 4 workflow: [`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md).

## Phase 0: KPIs and benchmarks

Numerical acceptance targets, data boundaries, operator roles, and the **LLM-led warm-up** workflow for benchmark questions (including the 50-question candidate pool) are defined in [`docs/PHASE0.md`](docs/PHASE0.md). Candidate questions live in [`docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md`](docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md).

## Phase 3: Corpus profiling (mechanical bootstrap)

Operator steps, deterministic `paper_id` slug rules, and rerun policy are in [`docs/PHASE3_RUNBOOK.md`](docs/PHASE3_RUNBOOK.md). The optional profiling script [`scripts/corpus_profile.py`](scripts/corpus_profile.py) registers paths, hashes, and text **snippets** — not semantic curation. Scientific ingestion (what each paper *means*, tags, wiki prose) is **Phase 4 / LLM** per [`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md).

## Tags and taxonomy (Phase 2)

- **Canonical tags** (`canonical_tags` in frontmatter) must be chosen **only** from [`taxonomy/canonical_tags.yml`](taxonomy/canonical_tags.yml): each entry is an `id` of the form `axis:slug` (`axis` is one of `domain`, `method`, `material`, `task`, `scale`; `slug` is lowercase `[a-z0-9-]+`). Add new allowed ids by editing that file (same PR/commit as first use), or use `candidate_tags` until merge.
- **Candidate tags** (`candidate_tags`): free-form strings for terms not yet in the canonical list; resolved per [`docs/TAXONOMY_GOVERNANCE.md`](docs/TAXONOMY_GOVERNANCE.md).
- **Synonyms:** common aliases map to canonical ids in [`taxonomy/synonyms.yml`](taxonomy/synonyms.yml).
- **Relations** (for Phase 4 normalized records): use relation ids from [`taxonomy/relations.yml`](taxonomy/relations.yml) only.
- **Guideline:** about **3–8** canonical tags per page.

## Folder roles and immutability

| Path | Mutable by wiki workflow? | Purpose |
|------|----------------------------|---------|
| `papers/` | **No** (read-only sources) | PDF corpus. |
| `raw/` | **Append-only** for `MANIFEST.jsonl` | Register sources; do not alter PDF bytes “through” this folder unless doing a controlled corpus update. |
| `normalized/` | **Yes** (machine records) | Canonical metadata, extraction pointers, structured entities/claims (Phase 4). |
| `wiki/` | **Yes** (markdown) | Human-readable graph; prefer generation over hand-editing, but edits are allowed when reviewed. |
| `indexes/` | **Yes** (generated) | Retrieval indices; safe to delete and rebuild. |
| `outputs/` | **Yes** | Scratch and reports; not canonical. |

**Rule:** Never “fix” a primary source PDF in place for KB convenience. Fix representation in `normalized/` and `wiki/`, and record provenance.

## Page types and responsibilities

| `type` | Responsibility | Directory |
|--------|----------------|-----------|
| `paper` | One PDF / one publication: summary, methods, findings, limitations, evidence anchors, links to concepts and entities. | `wiki/papers/` |
| `concept` | Cross-paper synthesis of an idea or theme; every substantive claim cites `paper_id` (via `source_refs` and/or inline). | `wiki/concepts/` |
| `material` | Material or system class (e.g., perovskite family, 2D X): facts relevant to simulation and force-field coverage. | `wiki/materials/` |
| `forcefield` | Force-field family or parameterization line: scope, applicability, known failures, validation hooks. | `wiki/forcefields/` |
| `methodprotocol` | Reusable workflow (fitting, AIMD setup, benchmarking). | `wiki/protocols/` |
| `debate` | **Optional:** substantive disagreement across sources, with balanced evidence. | `wiki/debates/` |

**Navigation-only pages** (e.g. root `wiki/index.md`) may use `type: concept` and an `id` prefix `index:` until a dedicated nav type exists; keep them free of uncited scientific claims.

### Theme hub pages (corpus clusters)

Large **domain** groupings live as ordinary **`concept` pages** in `wiki/concepts/` using a **`theme-`** filename prefix (example: `theme-oxides-silica-ceramics.md` → `id: concept:theme-oxides-silica-ceramics`). They exist to improve **Phase 0 connectivity** (papers linked from synthesis pages) and **MkDocs** navigation; each hub should list **representative `paper:`** slugs with `source_refs` grounding. The entry point **`wiki/concepts/themes-index.md`** (`concept:themes-index`) lists all theme hubs.

**Recommended section template for theme hubs:**

1. **`!!! abstract` or lead** — Plain-language scope for **human readers** (no new uncited science).
2. **`## Scope (in / out)`** — What the corpus does and does **not** promise.
3. **`## Literature review (this knowledge base)`** — **Corpus-scoped** synthesis only: organize **existing** `[[paper-slug]]` links by subtopic, state explicitly that it is **not** a world literature review, and avoid claims not traceable to linked paper pages.
4. **`## Debates, tensions, and cross-references`** — Wikilinks to `wiki/debates/`, other theme hubs, [[reaxff-family]], [[batteries-interfaces-reaxff]], etc.
5. **`## Representative entry points`** (optional if redundant) — Short bullet list of slugs.
6. **`## Methods and limitations`** — Honest limits of ReaxFF / MD for that domain.
7. **`??? info "MAS / retrieval"`** — Stable `id`, tagging hints, when to refresh `source_refs` (machine-oriented).

Theme pages serve **two audiences**: a **MAS / retrieval** spine (structured `id`, `canonical_tags`, `source_refs`) and a **public** site—keep technical caveats in admonitions or “limitations” sections so the narrative stays readable.

### Reader-facing layer (static site / GitHub Pages)

The same markdown is published via **MkDocs** (see `mkdocs.yml`). Conventions:

- Put a **plain-language lead** immediately after the `<!-- id:... -->` HTML comment (or use `!!! abstract "..."` for a visible blurb).
- Keep **YAML front matter** machine-complete; use **`??? info "Maintainers"`** or **`!!! note`** for operator-only reminders so casual readers skim the science first.
- **Paper** pages may include **`## Reader notes (navigation)`** with wikilinks to theme hubs and docs benchmarks—avoid new scientific claims there unless cited elsewhere on the page.

### Scientific claims must trace to publications (`paper` pages)

- Prose in **`## One-paragraph summary`**, **`## Methods`**, **`## Findings`**, and related sections must be **faithful summaries of the cited work** identified by `doi`, `title`, and `pdf_path` in front matter (and optional text in `normalized/extracts/` / `normalized/papers/` when those sources were used to draft the note).
- **Do not** invent numerical results, barriers, or mechanisms that are not stated or clearly implied in those sources. When expanding prose for readability, **paraphrase** the publication (or extraction) rather than adding new chemistry.
- **Navigation pages** (theme hubs, `paper-index-by-year`, search indexes) may list **metadata and links** without making new scientific assertions beyond what tags and titles encode.
- After bulk edits to `year` or `canonical_tags` across `wiki/papers/`, run `python3 scripts/generate_papers_indexes.py` to refresh [`wiki/concepts/paper-index-by-year.md`](wiki/concepts/paper-index-by-year.md) and [`wiki/concepts/paper-index-by-domain.md`](wiki/concepts/paper-index-by-domain.md).

## ID conventions (stable)

All wiki pages carry `id` in frontmatter. Format:

```text
<typeSlug>:<stableSlug>
```

- `typeSlug`: `paper` | `concept` | `material` | `forcefield` | `methodprotocol` | `debate` | `index`
- `stableSlug`: lowercase `[a-z0-9_-]+`, no spaces, globally unique.

**Paper ids:** Prefer derivation from DOI or first author + year + short venue or keyword, e.g. `paper:2024smith_jctc_reaxff-hf`. Once assigned, **never rename**; link stability depends on this.

**Other ids:** Use descriptive slugs, e.g. `concept:ferroelectric-domain-wall-md`, `forcefield:reaxff-sio2-parameter-set-x`.

## File path mapping (`id` → markdown path)

For all standard pages (not root index):

```text
wiki/papers/{slug}.md          ← id paper:{slug}
wiki/concepts/{slug}.md        ← id concept:{slug}
wiki/materials/{slug}.md       ← id material:{slug}
wiki/forcefields/{slug}.md     ← id forcefield:{slug}
wiki/protocols/{slug}.md       ← id methodprotocol:{slug}
wiki/debates/{slug}.md         ← id debate:{slug}
```

Where `{slug}` is everything after the first `:`. **Enforcement:** filename stem must equal `{slug}`.

**Exception:** `wiki/index.md` may use `id: index:root` (or similar) as the hub; static-site export maps it to `/`.

**Case sensitivity:** On **case-insensitive** volumes (common default macOS), `wiki/index.md` and `wiki/INDEX.md` are the **same path**—never maintain both names; use lowercase **`index.md`** only.

This mapping lets a static site generator compute URLs from `id` without parsing wikilinks.

## Frontmatter schema v1

Use YAML between `---` delimiters. All lists may be empty `[]` where allowed.

### Common fields (all types)

| Field | Required | Type | Notes |
|-------|----------|------|------|
| `id` | yes | string | See ID conventions. |
| `type` | yes | enum | `paper` \| `concept` \| `material` \| `forcefield` \| `methodprotocol` \| `debate`. |
| `title` | yes | string | Human title; may appear in wikilinks. |
| `updated` | yes | string | ISO 8601 date `YYYY-MM-DD` or datetime. |
| `confidence` | yes | enum | `low` \| `med` \| `high` (machine or human assessment of page reliability). |
| `canonical_tags` | yes | list[string] | Each string must be an `id` from [`taxonomy/canonical_tags.yml`](taxonomy/canonical_tags.yml); use `[]` if none apply yet. |
| `candidate_tags` | no | list[string] | Emergent labels pending merge; see [`docs/TAXONOMY_GOVERNANCE.md`](docs/TAXONOMY_GOVERNANCE.md). |
| `source_refs` | yes | list | List of objects (see below). Use `[]` for pages with no external claims. |

### `source_refs` object shape

Used on non-paper pages to ground claims; on `paper` pages may be `[]` if evidence is inline in the body.

```yaml
source_refs:
  - paper_id: "paper:2024smith_jctc_reaxff-hf"
    section: "Results"
    pages: "4-6"
    note: "optional short locator"
```

Fields:

- `paper_id` (required): matches a `paper` page `id`.
- `section` (optional): heading or section label in the PDF or normalized extraction.
- `pages` (optional): page range string as printed on the PDF.
- `note` (optional): free text for agents.

### `paper` — additional fields

| Field | Required | Type | Notes |
|-------|----------|------|------|
| `doi` | no | string | Raw DOI string without URL prefix preferred. |
| `year` | yes | int | Publication year. |
| `authors` | yes | list[string] or string | Prefer list. |
| `venue` | no | string | Journal or repository. |
| `pdf_sha256` | yes | string | SHA-256 of the file bytes under `papers/`. |
| `pdf_path` | yes | string | Repo-relative path, e.g. `papers/foo.pdf`. |
| `extraction_quality` | yes | enum | `good` \| `partial` \| `poor` \| `unknown`. |
| `group_affiliation` | no | bool or string | Whether / how this work relates to the host group. |

### `concept` — additional fields

| Field | Required | Type | Notes |
|-------|----------|------|------|
| `supported_by` | yes | list[string] | `paper_id` list backing the synthesis. |

### `material`, `forcefield`, `methodprotocol` — additional fields

| Field | Required | Type | Notes |
|-------|----------|------|------|
| `aliases` | no | list[string] | Synonyms for search and linking. |
| `related_ids` | no | list[string] | Other page `id`s. |
| `applies_to` | no | list[string] | ids of materials/systems/protocols this entry applies to (shallow v1). |
| `evaluates` | no | list[string] | Properties or benchmarks evaluated (string labels; align with `evaluates_property` in [`taxonomy/relations.yml`](taxonomy/relations.yml) when structured). |

### `debate` — additional fields

| Field | Required | Type | Notes |
|-------|----------|------|------|
| `positions` | yes | list | Short labels, e.g. `[{ "name": "View A", "summary": "..." }]` — keep YAML simple. |
| `evidence` | yes | list | Same shape as `source_refs`; each position should be supported by entries here. |

### Minimal examples

**Paper**

```yaml
---
id: paper:2024smith_jctc_reaxff-hf
type: paper
title: "Example title from metadata"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, method:reaxff, task:parameterization]
candidate_tags: []
source_refs: []
doi: "10.1063/5.0123456"
year: 2024
authors: ["Smith, J.", "Doe, A."]
venue: "J. Chem. Phys."
pdf_sha256: "<64-char hex>"
pdf_path: "papers/2024smith_jcp_reaxff.pdf"
extraction_quality: good
group_affiliation: false
---
```

**Concept**

```yaml
---
id: concept:ferroelectric-md-protocols
type: concept
title: "Ferroelectric materials in classical MD"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:ferroelectrics-polar, method:classical-md, task:application]
candidate_tags: []
source_refs:
  - paper_id: "paper:2024smith_jctc_reaxff-hf"
    section: "Introduction"
    pages: "1-2"
supported_by:
  - "paper:2024smith_jctc_reaxff-hf"
---
```

## Citations and claims policy

- **Substantive claims** in `concept`, `material`, `forcefield`, `methodprotocol`, and `debate` pages must have backing in `source_refs` or explicit inline citations that include `paper_id` and locator.
- **Paper** pages should anchor methods/results to sections/pages where possible (in body text).
- Do not invent DOIs or page numbers; if unknown, mark `extraction_quality` / `confidence` accordingly and omit locators.

## Ingest: `papers/` → `raw/MANIFEST.jsonl`

### Policy (v1)

- PDFs remain under repo-root **`papers/`** (recommended for Phase 1).
- Each ingested file gets one line in **`raw/MANIFEST.jsonl`** (JSON Lines: one JSON object per line, UTF-8, no comments).
- **`raw/papers/`** is optional: reserved for a future migration (symlink or copy) if you want all blobs under `raw/`. Update manifest `source_path` if you migrate.

### `MANIFEST.jsonl` record fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `source_path` | string | yes | Repo-relative path, e.g. `papers/myfile.pdf` or `papers/Others/myfile.pdf` (use full path from repo root for nested folders). |
| `sha256` | string | yes | SHA-256 hex digest of file contents. |
| `ingested_at` | string | yes | ISO 8601 UTC timestamp when the row was appended. |
| `paper_id` | string or null | no | Assigned when a stable `paper:{slug}` exists; may be null on first registration. |
| `notes` | string | no | Operator or pipeline notes. |

Example lines live in [`raw/MANIFEST.example.jsonl`](raw/MANIFEST.example.jsonl). The operational manifest starts empty until ingest runs.

## Wikilinks (Obsidian) and static export

- Use Obsidian **`[[wikilink]]`** targets that match the **note title** (`title` field) **or** the note **filename without `.md`** (the `{slug}` part), depending on what your tooling resolves best; **canonical resolution** for automation is: **filename stem** = `{slug}` from `id`.
- Prefer **unique titles** to reduce ambiguity in graph UIs.
- Immediately after frontmatter, you may include an HTML comment for tooling:

  `<!-- id:paper:2024smith_jctc_reaxff-hf -->`

  This is optional for humans but helps agents and exporters that scan raw markdown.

**Static site mapping:** `id` → URL path = `/<typeFolder>/<slug>/` using the directory table above (`methodprotocol` → `protocols` folder name in paths). Exporters should read frontmatter `id` and `type` rather than parsing link syntax alone.

## Normalized record shape: `normalized/papers/<paper_id>.json`

One JSON file per paper, named **`{slug}.json`** where `paper_id` is `paper:{slug}`.

Top-level keys (v1 contract for Phase 4 consumers):

| Key | Type | Description |
|-----|------|-------------|
| `paper_id` | string | Same as wiki `id`, e.g. `paper:2024smith_jctc_reaxff-hf`. |
| `manifest` | object | `{ "source_path", "sha256", "ingested_at" }` copied from manifest row. |
| `bibliography` | object | `doi`, `title`, `year`, `authors`, `venue`, optional identifiers. |
| `pdf_path` | string | Repo-relative path to PDF. |
| `extraction` | object | Paths or ids to raw text dumps, section map, `quality` enum, `extracted_at`. |
| `entities_mentioned` | list | Optional v1: coarse strings or ids for materials, methods, force fields (Phase 4 enrichment). |
| `claims` | list | Optional: objects with `text`, `confidence`, `source_refs` for MAS grounding. |
| `wiki_path` | string | Expected markdown path, e.g. `wiki/papers/2024smith_jctc_reaxff-hf.md`. |
| `updated` | string | ISO 8601 last update to this record. |

Example (minimal placeholder):

```json
{
  "paper_id": "paper:2024smith_jctc_reaxff-hf",
  "manifest": {
    "source_path": "papers/2024smith_jcp_reaxff.pdf",
    "sha256": "<64-char hex>",
    "ingested_at": "2026-04-20T12:00:00Z"
  },
  "bibliography": {
    "doi": "10.1063/5.0123456",
    "title": "Example title",
    "year": 2024,
    "authors": ["Smith, J."],
    "venue": "J. Chem. Phys."
  },
  "pdf_path": "papers/2024smith_jcp_reaxff.pdf",
  "extraction": {
    "text_path": "normalized/papers/2024smith_jctc_reaxff-hf.fulltext.txt",
    "quality": "good",
    "extracted_at": "2026-04-20T12:00:00Z"
  },
  "entities_mentioned": [],
  "claims": [],
  "wiki_path": "wiki/papers/2024smith_jctc_reaxff-hf.md",
  "updated": "2026-04-20T12:00:00Z"
}
```

## Git, privacy, and public export

- **Default recommendation:** Track **schemas, wiki, and normalized JSON** in git; treat **`papers/*.pdf`** as **optional** for git (large binaries, licensing). Use a tracked `papers/README.md` explaining how to obtain or attach the corpus locally.
- If PDFs are excluded, clones remain valid: pipelines read **`raw/MANIFEST.jsonl`** and expect files at `source_path` on disk.
- **Public export (Phase 8):** Publish only redacted or rights-cleared markdown and metadata; full PDFs may stay private. `AGENTS.md` and `README.md` should be updated when an export profile is chosen.

See [`.gitignore`](.gitignore) for optional ignore patterns (commented).

## Phase boundaries

- **Phase 2:** [`taxonomy/`](taxonomy/) canonical tags, [`synonyms.yml`](taxonomy/synonyms.yml), [`relations.yml`](taxonomy/relations.yml), [`docs/TAXONOMY_GOVERNANCE.md`](docs/TAXONOMY_GOVERNANCE.md) — vocabulary v1; revised after Phase 3 review ([`outputs/taxonomy_phase3_review.md`](outputs/taxonomy_phase3_review.md)).
- **Phase 3:** manifest + [`normalized/papers/*.json`](normalized/papers/) stubs (mechanical) — see [`docs/PHASE3_RUNBOOK.md`](docs/PHASE3_RUNBOOK.md).
- **Phase 4:** **LLM-led** wiki compilation — narrative pages, tags, concepts, links; scripts at most validate or list files — see [`docs/PHASE4_RUNBOOK.md`](docs/PHASE4_RUNBOOK.md). Must conform to this document and taxonomy files.
- **Phase 5:** `indexes/` population for hybrid retrieval — see [`docs/PHASE5_RUNBOOK.md`](docs/PHASE5_RUNBOOK.md) and [`indexes/README.md`](indexes/README.md).

When in doubt, prefer **provenance and stable ids** over prettier prose.
