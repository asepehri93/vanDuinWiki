---
id: paper:2014huygh-computationa-development-reaxff
type: paper
title: "Development of a ReaxFF reactive force field for intrinsic point defects in titanium dioxide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2014.07.056"
year: 2014
authors:
  - "Huygh, Stijn"
  - "Bogaerts, Annemie"
  - "van Duin, Adri C. T."
  - "Neyts, Erik C."
venue: "Computational Materials Science"
pdf_sha256: "37ccdd401c2b8a269bd685767dad3e2f21b4efb24a2b0f793e7c50bbbfea31c2"
pdf_path: "papers/Huygh_CompMatSci_TiO2_defect_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014huygh-computationa-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

A **ReaxFF** parametrization targets **intrinsic defects** in **TiO\(_2\)** condensed phases, motivated by **photocatalysis** and **redox** applications where **oxygen vacancies** mediate **surface** chemistry and **transport**. Training spans **equations of state**, **Ti** versus **TiO\(_2\)** relative stabilities, **(TiO\(_2\))\(_n\)** cluster energies, and **anatase** **defect** data including **interstitial Ti**, **oxygen vacancies**, **vacancy diffusion barriers**, and **O\(_2\)** adsorption on **reduced anatase (101)**. Subsequent **MD** explores how **vacancy concentration** and **surface strain** affect **oxygen-vacancy diffusion** pathways on **anatase** surfaces. **Subsurface** diffusion barriers from the fitted model (**~27.7 kcal/mol** in the abstract) are compared to **DFT** barriers for **surface**, **subsurface**, and **cross-layer** processes quoted alongside (**17.07**, **21.91**, and **61.12 kcal/mol** for selected pathways in the abstract text).

## Methods

### ReaxFF training data (bulk + clusters + defects)

- **Ti–O** parameters are fit to **ab initio** benchmarks including **equations of state**, **Ti** vs **TiO\(_2\)** relative stabilities, **(TiO\(_2\))\(_n\)** cluster energies (**n = 1–16**), and **intrinsic defects in anatase**: **interstitial Ti**, **oxygen vacancies** (**formation energies**), **vacancy diffusion barriers**, and **O\(_2\)** adsorption on **reduced anatase (101)** (**abstract**).

### Reactive MD studies (surfaces under strain)

- Subsequent **MD** explores how **oxygen-vacancy concentration** and **biaxial surface strain** (**expansion/compression**) influence **vacancy diffusion** on **anatase** surfaces (**abstract**).
- Barrier extraction uses **temperature-accelerated** and/or **biased** sampling protocols detailed in **Comput. Mater. Sci.** (not reproduced numerically here).

### Reporting convention

- Abstract quotes mix **ReaxFF** barriers (e.g., **~27.7 kcal/mol** subsurface diffusion) with **DFT** barriers for specific **surface/subsurface/cross-layer** pathways—consult tables for **exact** **reaction coordinates**.

### 1 — MD application (vacancy diffusion on anatase surfaces)

- **Engine / code:** **Reactive MD** with **ReaxFF** is discussed in the article in the **LAMMPS** implementation context (see *Comput. Mater. Sci.* §2.1 and `normalized/extracts/2014huygh-computationa-development-reaxff_p1-2.txt`); treat **executable revision/build** details as **N/A — not restated on extract pages 1–2**.
- **System size & composition:** **Anatase** **surface** models with tunable **oxygen-vacancy concentration** and **biaxial surface strain** (expansion/compression) as described in the **abstract**; **exact supercell sizes** are **N/A — not on indexed extract** (see PDF §2+).
- **Boundaries / periodicity:** **PBC** for **slab/supercell** surface workflows is implied by standard **DFT/ReaxFF** practice in this article class; **N/A — explicit boundary wording not on extract p1–2** (confirm in PDF).
- **Ensemble / thermostat / timestep / duration:** **N/A — numerical MD integration settings not stated on extract pages 1–2** (full **Comput. Mater. Sci.** Methods).
- **Barostat / pressure:** **N/A — not stated as NPT-driven** in the abstract-level summary here; confirm whether strain is imposed mechanically vs barostat in the article.
- **Temperature:** **N/A — explicit thermostat temperatures not on extract p1–2** (article body/SI).
- **Electric field:** **N/A — not indicated** in the indexed abstract/extract opener.
- **Replica / enhanced sampling:** **N/A — umbrella/metadynamics not indicated** in the indexed abstract/extract opener (the abstract refers generically to evaluating a **subsurface diffusion barrier** with the fitted model).

### 2 — Force-field training (TiO₂ intrinsic defects)

- **Parent FF / elements:** **ReaxFF** for **Ti–O** chemistry building on the **van Duin** reactive formalism (introduction/extract).
- **QM reference:** **Ab initio / DFT** data used as **training** references; **functional, basis, k-mesh** specifics appear in the article’s **QM** subsection—**N/A — not duplicated on extract p1–2**.
- **Training set:** **Equations of state**; **Ti** vs **TiO₂** relative stabilities; **(TiO₂)\(_n\)** clusters (**n = 1–16**); **anatase** **intrinsic defects** including **interstitial Ti**, **oxygen vacancies** (formation energies), **vacancy diffusion barriers**, and **O₂** adsorption on **reduced anatase (101)** (abstract; extract).
- **Optimization:** **Parameter optimization** to the **ab initio** database is stated abstractly; **software/weighting** details—**N/A — not on extract p1–2** (Methods/SI).
- **Reference data:** **DFT** barriers cited alongside **ReaxFF** for **surface**, **subsurface**, and **cross-layer** vacancy processes (**17.07**, **21.91**, **61.12 kcal/mol** pathways in abstract text) plus the **ReaxFF** subsurface value **~27.7 kcal/mol**.

## Findings

### Outcomes and mechanisms

Using the fitted potential, **subsurface oxygen-vacancy diffusion** is characterized by a **ReaxFF barrier of 27.7 kcal/mol** (abstract). The authors argue **lateral redistribution** of vacancies between **surface and subsurface** is **dominated by subsurface diffusion** because this barrier—and **DFT** barriers for **surface ↔ subsurface** exchange (**17.07** and **21.91 kcal/mol**, respectively)—are **far lower** than the **DFT** barrier for **on-surface** vacancy diffusion (**61.12 kcal/mol**), implying **in-plane subsurface** transport should outpace **purely surface** hopping for the models studied (abstract).

### Comparisons (ReaxFF versus DFT)

The abstract explicitly **juxtaposes** the **ReaxFF** subsurface diffusion barrier with **DFT** barriers for **distinct vacancy transport classes** (surface hopping vs surface–subsurface exchange vs subsurface diffusion). **Exact reaction-coordinate definitions** and any additional benchmarks should be taken from the **Computational Materials Science** tables in `papers/Huygh_CompMatSci_TiO2_defect_2014.pdf`, not inferred from the short extract alone.

### Sensitivity and design levers

The abstract states subsequent **MD** explores how **oxygen-vacancy concentration** and **biaxial surface strain** (expansion/compression) influence **vacancy diffusion** on **anatase** surfaces; **quantitative trend curves** are **not** restated on `normalized/extracts/2014huygh-computationa-development-reaxff_p1-2.txt` (read the article figures).

### Limitations and outlook (authored / scope)

**Parametrization** scope follows the **training** reactions listed in the abstract (bulk EOS, clusters, **anatase** intrinsic defects); **rutile** defect chemistry is outside the **anatase**-focused training envelope unless separately validated (**## Limitations** below). **Future** extensions and caveats beyond the indexed abstract should be quoted from the discussion in the **PDF**.

### Corpus honesty

This page is grounded in **`papers/Huygh_CompMatSci_TiO2_defect_2014.pdf`** plus the short **`normalized/extracts/2014huygh-computationa-development-reaxff_p1-2.txt`** window; **numerical MD settings** and **full barrier tables** require the **full article** text.

## Limitations

Parametrization scope follows the **training** reactions listed; **rutile** versus **anatase** coverage follows the paper’s **anatase**-focused dataset, so **rutile** **defect** chemistry is outside the stated training envelope unless separately validated.

## Citations and evidence anchors

- DOI `10.1016/j.commatsci.2014.07.056` (extract footer).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]

## Reader notes (navigation)

**Vacancy** **barriers** quoted in the abstract mix **ReaxFF** and **DFT** values; use the **Computational Materials Science** tables for **exact** **path** definitions before comparing numbers to other **TiO\(_2\)** **defect** studies in the corpus. **Surface** **strain** magnitudes applied during **diffusion** sweeps should be read from the article to avoid mixing **bulk** and **surface** **stress** states.
