---
id: paper:2013gouissem-computationa-reactive-force-field-2
type: paper
title: "A reactive force-field for zirconium and hafnium di-boride"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:metallic-systems
source_refs: []
doi: "10.1016/j.commatsci.2012.12.038"
year: 2013
authors:
  - "Gouissem, Afif"
  - "Fan, Wu"
  - "van Duin, Adri C. T."
  - "Sharma, Pradeep"
venue: "Computational Materials Science"
pdf_sha256: "cef3ce23dc9ca7cf896b3dc89024f9c2df7e01234573cd7cef4562355ec79e06"
pdf_path: "papers/Gouissem_ZrHfB2_CompMatSci_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013gouissem-computationa-reactive-force-field-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Develops **ReaxFF** parameters for **ZrB₂** and **HfB₂**—**ultra-high-temperature ceramics** of interest for hypersonic and thermal-protection applications—by fitting to **quantum mechanical** data on **clusters** and **crystal** fragments. The goal is to enable **atomistic** simulations where **bond-making/breaking** (oxidation, defect evolution, grain-boundary processes) matters, which is intractable with fixed-bond potentials. The motivation is explicitly materials-driven: borides are used where **extreme thermal loads** and **oxidizing environments** coexist, so a reactive description must capture **metal–boron** chemistry beyond harmonic elasticity.

## Methods

**2 — Force-field training.** **Parent FF / elements:** **ReaxFF** for **Zr–B** and **Hf–B**, using the reduced **Eq. (3)** total-energy expression specialized in the manuscript (see `normalized/extracts/2013gouissem-computationa-reactive-force-field-2_p1-2.txt` for the **Eq. (3)** discussion head). **QM reference:** **QuantumWise** (**DFT**) for periodic **ZrB₂**/**HfB₂** crystal-phase data; **Gaussian 09** for **Zr(BH₂)₂** and **Hf(BH₂)₂** cluster **geometry**/**PES** targets (**Sections 3–4** for **basis** sets and **functionals**—read **`pdf_path`** for tables). **Training set:** periodic **DFT** points plus cluster **QM** scans feeding the fit. **Optimization:** **weighted least squares** **ReaxFF** parameter optimization against the **QM** training data. **Reference data / validation:** **Section 5** reports **molecular dynamics** checks with the fitted potential against **QM** or **literature** references for **crystal**- and **defect**-like motifs.

**1 — MD application (atomistic dynamics).** **Section 5** uses **ReaxFF** **molecular dynamics** on **ZrB₂**/**HfB₂**-related **crystal** and **defect** motifs as validation (**pdf_path**). **Engine / code:** **N/A —** explicit package string not duplicated in this wiki summary (common practice: **LAMMPS**; confirm in **`pdf_path`**). **System size & composition:** **atom** counts / **supercell** **stoichiometry** for each validation case—see **`pdf_path`** tables. **Boundaries / periodicity:** **three-dimensional periodic boundary conditions** where bulk-like cells are used; any non-periodic cluster tests—confirm in **`pdf_path`**. **Ensemble:** **NVT** and/or **NPT** **MD** settings for **Section 5** trajectories are tabulated in **`pdf_path`** (this summary does not transcribe every numerical control). **Timestep / duration / thermostat / barostat:** **N/A —** not transcribed line-by-line here; copy from **`pdf_path`** **Section 5**. **Temperature:** finite-**temperature** **MD** in **Section 5** (exact **K** values in **`pdf_path`**). **Pressure:** **N/A —** not summarized here. **Electric field:** **N/A —**. **Replica / enhanced sampling:** **N/A —**.

**3 — Static QM / DFT.** Embedded in the **QM reference** generation for training (not a separate QM-only application study split from the **ReaxFF** fit).

## Findings

**1 — Outcomes & mechanisms.** The fitted **ReaxFF** reproduces targeted **QM** **energetics** and **structural** metrics for **ZrB₂**/**HfB₂** training sets, enabling **reactive** simulations with explicit **bond rearrangement** at **interfaces** where boron **redistributes** rather than behaving as a frozen sublattice.

**2 — Comparisons.** **Section 5** **MD** is compared against **QM** and/or **literature** references for selected **crystal**/**defect** motifs (see **`pdf_path`**).

**3 — Sensitivity & design levers.** Which **clusters** and **bulk** phases enter the **QM** **training** set controls what chemistry the subsequent **MD** can faithfully represent; any explicit **temperature**/**pressure** sweeps in validation **MD** should be read from **`pdf_path`**.

**4 — Limitations & outlook.** **Transferability** to complex multicomponent ceramics and long-time high-**temperature** kinetics still depends on expanded **training** data, as discussed in the article.

**5 — Corpus honesty.** This page summarizes **`papers/Gouissem_ZrHfB2_CompMatSci_2013.pdf`**; the Elsevier proof bundle is registered separately as **`[[2013gouissem-computationa-reactive-force-field]]`** for provenance.

## Limitations

- Transferability to complex multicomponent ceramics and high-temperature long-time kinetics still depends on expanded training data.

## Relevance to group

Direct **van Duin** collaboration on extending **ReaxFF** into **boride** chemistry for extreme environments.

## Citations and evidence anchors

- Abstract and Sec. 1: motivation and fitting strategy (Comput. Mater. Sci. 70 (2013) 171–177; DOI above).

## Reader notes (navigation)

- Proof-query PDF path: [[2013gouissem-computationa-reactive-force-field]]. Proof/galley duplicate policy: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
