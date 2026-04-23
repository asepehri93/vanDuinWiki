---
id: paper:2014lordi-venue-paper
type: paper
title: "Molecular structure and ion transport near electrode–electrolyte interfaces in lithium-ion batteries"
updated: "2026-04-20"
confidence: low
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:methods-software
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: ""
year: 2014
authors:
  - "V. Lordi"
  - "M. T. Ong"
  - "O. Verners"
  - "A. C. T. van Duin"
  - "E. W. Draeger"
  - "J. E. Pask"
venue: "LLNL-CONF-663739; ACS National Meeting presentation (Denver, 2015)"
pdf_sha256: "f898cc70d1661f8b9f4105cd2d95546d626ddbea6d0b6be80f7cd253d913d3fe"
pdf_path: "papers/Lordi_LLNL_Conf_Li_electrolyte.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014lordi-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This entry is grounded in the **LLNL conference document metadata** and cover text available in the corpus extract. It does **not** reproduce slide results absent from **`normalized/extracts/2014lordi-venue-paper_p1-2.txt`**.

## Summary

The corpus registers **LLNL-CONF-663739**, a **Lawrence Livermore National Laboratory** presentation package for the **ACS National Meeting** in **Denver** (**March 22–26, 2015**), with document metadata dated **November 4, 2014**. The authorship team spans **LLNL** (**Lordi**, **Draeger**, **Pask**) and **Penn State** (**van Duin**), with collaborators **Ong** and **Verners** who appear in related **electrolyte** modeling papers in this wiki. The stated topic is **molecular-scale structure** and **ion transport** near **electrode–electrolyte interfaces** in **lithium-ion batteries**, positioning **simulation** as a complement to continuum models that cannot resolve **interfacial solvation**, **desolvation**, or **flux** hot spots. The PDF in `papers/` functions as **conference material** rather than a **journal article**; **no DOI** is assigned in frontmatter.

## Methods

### Document type and recoverable protocol text

The registered PDF `papers/Lordi_LLNL_Conf_Li_electrolyte.pdf` and `normalized/extracts/2014lordi-venue-paper_p1-2.txt` contain **cover metadata and LLNL disclaimer text** for **LLNL-CONF-663739** (249th ACS National Meeting, Denver, March 22–26, 2015; document date November 4, 2014). **Slide-body methods are not present** in that indexed layer.

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **N/A — not stated** in the cover-only extract; any **molecular dynamics** engine would appear in the presentation body or a journal article, not in `2014lordi-venue-paper_p1-2.txt`.
- **System size & composition:** **N/A — not stated** in the indexed text (no atom counts, electrolyte stoichiometry, or electrode models recoverable here).
- **Boundaries / periodicity:** **N/A — not stated** (no supercell or boundary-condition description on file).
- **Ensemble:** **N/A — not stated.**
- **Timestep:** **N/A — not stated.**
- **Duration / stages:** **N/A — not stated** (no equilibration or production **ps**/**ns** in the extract).
- **Thermostat:** **N/A — not stated.**
- **Barostat:** **N/A — not stated** (no **NPT** / pressure-control description in the extract).
- **Temperature:** **N/A — not stated** for simulations (meeting dates only).
- **Pressure:** **N/A — not stated.**
- **Electric field:** **N/A — not stated** (no bias or potentiostat protocol in the extract).
- **Replica / enhanced sampling:** **N/A — not stated.**

### 2 — Force-field training

**N/A —** the indexed text does not describe **ReaxFF** (or other) parameter files, training sets, or optimization workflows.

### 3 — Static QM / DFT-only

**N/A —** no **DFT** functional, basis, or **k**-mesh details appear in the cover-only extract.

### 4 — Presentation scope (non-journal primary)

The cover text positions the work as **molecular-scale structure** and **ion transport** near **electrode–electrolyte interfaces** in **lithium-ion batteries**, complementing continuum models that omit interfacial solvation and flux detail. For **peer-reviewed** simulation protocols from overlapping authors on **carbonate electrolytes**, use **`[[2014ong-venue-research]]`** (J. Phys. Chem. B; DOI on that page).

## Findings

### Outcomes and mechanisms

The indexed material does not report **simulation outcomes** (no **interface** **density profiles**, **ionic conductivity**, or **reaction** statistics on file). Any mechanistic discussion of **electrode–electrolyte** **transport** on this page would therefore be **speculation** rather than evidence from `papers/Lordi_LLNL_Conf_Li_electrolyte.pdf` at the current extraction depth.

### Comparisons and sensitivity

**N/A —** the cover/disclaimer extract contains **no experimental comparison**, **no literature benchmarks**, and **no sensitivity study** (e.g., **temperature**, salt concentration, or field) tied to reported numerical results.

### Limitations and outlook (as available on this slug)

**Limitation:** only **cover metadata** and **disclaimer** text are indexed (`normalized/extracts/2014lordi-venue-paper_p1-2.txt`), so **limitations** of any simulation workflow **cannot** be excerpted here. **Outlook:** when full slide or article text is ingested, expand **Findings** with **quantitative** results and authored **caveats** from those sources.

### Corpus / KB honesty

This entry is **extract-thin** relative to scientific detail; prefer **`[[2014ong-venue-research]]`** or other **paper:** pages with **version-of-record** **PDF** grounding when citing **Li-ion electrolyte** **diffusion** or **solvation** **mechanisms**. Update **`extraction_quality`** if deeper **PDF** text is added later.

## Limitations

**Conference PDF** vs **peer-reviewed** article; **partial** extraction; **DOI** absent—**confidence** is **low** for scientific detail. **LLNL** distribution statements on the cover may constrain redistribution—respect institutional **export** rules when copying PDFs outside the workspace.

## Reader notes (navigation)

Until slides are text-extracted, treat this slug as **bibliographic glue** between **LLNL** battery modeling and **Penn State** **ReaxFF** efforts; expand only when new sources arrive.

## Relevance to group

Documents a **Lordi–Ong–Verners–van Duin** collaboration thread on **battery electrolytes**; pairs with [[2014ong-venue-research]] for **peer-reviewed** **electrolyte** content.

## Citations and evidence anchors

- Document identifier **LLNL-CONF-663739** (PDF header).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Curator note

Revise when slide bodies or a journal version enter the corpus; keep **`extraction_quality`** aligned with indexed depth.

