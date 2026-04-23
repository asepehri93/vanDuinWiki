---
id: paper:2013qaps-venue-paper
type: paper
title: "Computational modeling of structure and OH-anion diffusion in quaternary ammonium polysulfone hydroxide – Polymer electrolyte for application in electrochemical devices"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:classical-md
  - material:polymer-organic
  - task:application
  - scale:atomistic
  - domain:methods-software
candidate_tags: []
source_refs: []
doi: "10.1016/j.memsci.2012.12.010"
year: 2013
authors:
  - "Merinov, Boris V."
  - "Goddard, William A., III"
venue: "Journal of Membrane Science"
pdf_sha256: "ab24968fe6d08ad62c2b817f9ea91103abfd671167c21cded18f08c9ea22833a"
pdf_path: "papers/Others/QAPS_OH_JMS-2013.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2013qaps-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Quaternary ammonium polysulfone hydroxide (QAPS-OH)** membranes conduct **hydroxide** in **alkaline fuel cells** and related electrochemical devices; morphology and **water uptake** strongly affect **OH⁻** mobility. This **Journal of Membrane Science** article (**Merinov**, **Goddard III**) uses **classical molecular dynamics** to predict **amorphous packing**, **nanophase separation**, and **diffusion** in **dry** films and films hydrated to roughly **14 wt% water**, matching the abstract’s stated hydration window. The physical picture is a **hydrophobic polysulfone backbone** threaded with **hydrophilic quaternary ammonium** groups that **percolate** into **three-dimensional hydrophilic channels** where **OH⁻** resides and hops. Computed **diffusion coefficients** and **activation energies** are compared with **experimental** values, with mechanistic commentary on **vehicle** versus **Grotthuss-like** character as framed in the paper.

## Methods

Grounding: `papers/Others/QAPS_OH_JMS-2013.pdf`; `normalized/extracts/2013qaps-venue-paper_p1-2.txt` (publisher wrapper + abstract + start of Sec. 2).

### 1 — MD application (polymer membrane atomistic MD)

- **Engine / code:** **Molecular dynamics simulations** are used to compute **OH⁻ diffusion** and **activation energies** for **QAPS-OH** membranes (abstract); the **MD code/package name** is **not stated** on the indexed excerpt pages.
- **System size & composition:** The study targets **quaternary ammonium polysulfone hydroxide (QAPS-OH)** membranes modeled **dry** and with **~14 wt% water uptake** (abstract; “/C24 14 wt%” artifact in extract OCR).
- **Initial packing / boundary workflow:** The initial structure is constructed with the **Amorphous Builder** in **Cerius2**, using **Monte Carlo** techniques (Sec. 2 “Simulation details” opening in extract).
- **Boundaries / periodicity:** N/A — **PBC details** are **not stated** on the indexed excerpt pages (expected for bulk amorphous polymer cells, but not spelled out here).
- **Ensemble:** N/A — **NVE/NVT/NPT** specification is **not stated** on the indexed excerpt pages.
- **Timestep:** N/A — **timestep** is **not stated** in the indexed excerpt.
- **Duration / stages:** N/A — **equilibration/production lengths** are **not stated** in the indexed excerpt.
- **Thermostat / barostat:** N/A — **not stated** in the indexed excerpt.
- **Temperature:** Simulations are performed at **different temperatures** to access **OH⁻ diffusion** and **Arrhenius-type activation energy** analysis (abstract); **explicit K values** are **not listed** on p1–2.
- **Pressure:** N/A — **not stated** in the indexed excerpt.
- **Electric field:** N/A — **not used** in the abstract framing.
- **Replica / enhanced sampling:** N/A — **not stated** in the indexed excerpt.

### 2 — Force-field training

N/A — **classical MD** parameterization paper (not ReaxFF training); **force field, charges, and water model** are expected in later **Simulation details** paragraphs in `pdf_path` (not captured on p1–2).

### 3 — Static QM / DFT-only

N/A — central methods are **MD + amorphous structure generation**, not a standalone DFT benchmark study in the indexed excerpt.

## Findings

- **Outcomes & mechanisms:** The predicted microstructure is described as a **hydrophobic polysulfone backbone** penetrated by a **3D network of interlinked hydrophilic channels** of varying diameter, with **mobile OH⁻** distributed inside channels (abstract).
- **Comparisons:** Predicted **OH⁻ diffusion coefficients** and **activation energy** are reported as **consistent with available experimental data** (abstract).
- **Sensitivity / design levers:** The abstract explicitly contrasts **dry** vs **~14 wt% hydrated** membranes as two states used in the modeling.
- **Limitations & outlook:** The indexed excerpt does not restate author limitations; broader **AFC durability / mechanical stability** context appears in the introduction (extract) as motivation rather than MD outcomes.
- **Corpus honesty:** `extraction_quality` is **partial** because the tracked extract begins with **Elsevier author-copy boilerplate** and only reaches the opening of **Simulation details**; **ensemble, timestep, production length, and FF tables** must be read from the **full PDF**.

## Limitations

Normalized `extraction_quality` is partial (publisher cover page occupies part of the extract). Force field and water model details beyond the first pages are not visible in the p1–2 extract.

## Relevance to group

Alkaline polymer electrolytes adjacent to battery/fuel-cell interface topics in the broader corpus; not a ReaxFF paper but relevant electrochemical device modeling context.

## Citations and evidence anchors

- Abstract and keywords: modeling scope, water content, diffusion/activation energy claims (extract).
- Journal of Membrane Science 431 (2013) 79–85 and DOI line in extract.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
