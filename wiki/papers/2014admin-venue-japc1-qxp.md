---
id: paper:2014admin-venue-japc1-qxp
type: paper
title: "Journal of Applied Physics cover / layout artifact (NiO diffusion special issue)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - material:oxide
  - task:review
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
source_refs: []
doi: ""
year: 2014
authors: []
venue: "Journal of Applied Physics (cover fragment)"
pdf_sha256: "1065961148e46276effb4be8b3b89604872a7fa6a432a140327a7dd2585c9f10"
pdf_path: "papers/Fang_J_App_Phys_NiO_diffusion_2014_journal_cover.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014admin-venue-japc1-qxp -->

??? info "Why confidence is med"
    No DOI is assigned in front matter; the PDF is a **cover/layout fragment** with no article body (`normalized/extracts/2014admin-venue-japc1-qxp_p1-2.txt` shows only masthead text). Scientific claims belong on [[2014fang-venue-untitled]].

## Summary

The file `papers/Fang_J_App_Phys_NiO_diffusion_2014_journal_cover.pdf` is not a research article. It records a *Journal of Applied Physics* cover or layout fragment. The automated extract (`normalized/extracts/2014admin-venue-japc1-qxp_p1-2.txt`) contains only masthead lines: **“28 January 2014 Volume 115 Number 4”**, **“jap.aip.org”**, and the journal name banner **“Journal of Applied Physics”**—no author list, abstract, or methods section appears in that text layer. This wiki entry exists so manifest rows pointing at the file remain interpretable for operators: it is a navigation stub, not a source for methods or numerical data about nickel oxide diffusion or ReaxFF simulations.

Historical corpus imports occasionally bundled promotional PDFs, table-of-contents extracts, or cover sheets alongside primary research PDFs. Those artifacts remain in `papers/` to preserve byte-identical provenance for hashes recorded in `raw/MANIFEST.jsonl`, even when they carry no standalone scientific text. This pattern is why the front matter for this slug omits authors and DOI: the cover fragment does not encode bibliographic metadata in a reliable way, and assigning a guessed DOI would violate evidence-grounded curation rules. The filename string “NiO_diffusion” is a **human catalog hint** about the themed issue content; it is not itself an extract-derived claim about diffusion coefficients or mechanisms.

## Methods

### Document type

- The ingested PDF is a **journal cover/layout fragment** only; it contains **no Methods section** usable for science extraction.

### What this implies (checklist D / navigation stub)

- **Not applicable:** there are **no experimental or computational protocols** recoverable from `normalized/extracts/2014admin-venue-japc1-qxp_p1-2.txt` beyond masthead metadata.

### Where methods actually live

- For **Ni–O diffusion** / **oxidation** modeling content, use full article ingests such as **`[[2014fang-venue-untitled]]`** (or other curated primary PDFs), not this cover artifact.

### Operator guardrail

- Do **not** infer **ReaxFF** settings, **DFT** parameters, or diffusion coefficients from filenames or cover art.

### Literature scope (review-style checklist for this artifact)

- **Corpus role:** this slug documents **manifest** **provenance** for a **non-article** PDF; it is **not** a **computational** or **experimental** **methods** source.
- **Experimental methodology:** **N/A —** no laboratory or instrument protocol is recoverable from the **cover** extract.
- **Atomistic simulation methodology:** **N/A —** no **LAMMPS**/**VASP** inputs, **timestep**, **ensemble**, or **interatomic potential** tables are present in the indexed text.
- **Where to read science instead:** use **`[[2014fang-venue-untitled]]`** (or other **full-article** slugs) for **NiO** **diffusion**/**oxidation** simulation content.

## Findings

No quantitative findings can be recovered from the cover extract beyond the **publication date**, **volume 115**, **number 4**, and **AIP journal branding** shown in `normalized/extracts/2014admin-venue-japc1-qxp_p1-2.txt`. Retrieval systems should rank this page as **provenance-only** and route scientific questions about NiO transport to wiki entries backed by full article PDFs and structured `normalized/papers` records.

**Compared to a research article:** there are **no** **results** figures, **tables**, or **statistics** on this path—any **diffusion** **coefficient** or **barrier** claim must come from a **different** **PDF** in the corpus.

**Sensitivity / design levers:** **N/A —** not applicable because the **artifact** contains **no** **study** **parameters** beyond **issue** metadata.

**Limitations / outlook:** the **cover** will remain **useful** only as a **navigation** and **hash** anchor unless operators attach a **version-of-record** article PDF to a sibling slug.

**Corpus honesty:** the **extract** is **masthead-only**; treat this page as **explicitly** **thin** evidence for **science** questions and prefer **PDF-backed** **paper:** pages for **mechanisms** or **kinetics**.

## Limitations

The absence of a DOI and article text in this path prevents using the slug as a citable scientific reference. Prefer the primary article PDF for all substantive claims.

## Relevance to group

Provenance-only record steering readers toward the actual NiO diffusion paper in the corpus.

Downstream pipelines should tag this slug as **navigation-only** so retrieval ranking does not treat cover fragments as authoritative answers for diffusion coefficients, vacancy formation energies, or ReaxFF validation metrics. When a user query matches NiO diffusion themes, prefer routing to [[2014fang-venue-untitled]] or other full-article ingests that actually contain methods and results sections.

MkDocs and Obsidian exporters can still link this page for completeness, but sitemap generation may choose to `noindex` navigation stubs if that becomes a policy in Phase 8 export profiles.

Keeping the SHA-256 in front matter stable matters: even though the PDF is non-scientific, manifests use it to detect accidental overwrites when curators reorganize `papers/`.

## Reader notes (navigation)

- [[2014fang-venue-untitled]]
