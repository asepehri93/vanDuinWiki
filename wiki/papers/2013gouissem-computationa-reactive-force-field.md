---
id: paper:2013gouissem-computationa-reactive-force-field
type: paper
title: "A reactive force-field for zirconium and hafnium di-boride (Elsevier proof query PDF)"
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
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
source_refs: []
doi: "10.1016/j.commatsci.2012.12.038"
year: 2013
authors:
  - "Gouissem, Afif"
  - "Fan, Wu"
  - "van Duin, Adri C. T."
  - "Sharma, Pradeep"
venue: "Computational Materials Science"
pdf_sha256: "f3f1ae9b8083e77b0848857bd21dd850f514661150fe28953ce0e41066cbfbdf"
pdf_path: "papers/Afif_CompMatSci_2013_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013gouissem-computationa-reactive-force-field -->

## Evidence and attribution

!!! note "Authority of statements"

    This corpus PDF is an **Elsevier author-query / proof** bundle. Full scientific prose is curated against the **final article** PDF on [[2013gouissem-computationa-reactive-force-field-2]].

## Summary

This wiki page registers an **Elsevier author-query / proof** PDF (`papers/Afif_CompMatSci_2013_galley.pdf`) for the *Computational Materials Science* article that develops a **ReaxFF** description of **zirconium diboride** and **hafnium diboride** (**DOI** `10.1016/j.commatsci.2012.12.038`). The scientific program, co-authored by **Adri C. T. van Duin**, targets **ultra-high-temperature ceramic** borides where **bond-making and bond-breaking** events—including oxidation, defect evolution, and grain-boundary chemistry—are central but difficult to capture with fixed-bond empirical potentials. The manuscript fits **bond-order-dependent ReaxFF** energy expressions to a combined **quantum mechanical** training set spanning **periodic** boride fragments (computed with **QuantumWise** tools as described in the paper) and **cluster** targets from **Gaussian 09**, so that large-scale **reactive molecular dynamics** of **Zr–B** and **Hf–B** chemistry becomes feasible without abandoning the ReaxFF formalism used across the broader corpus. Because the ingested file is a **proof bundle**, readers should treat **pagination**, line breaks, and some figure placement as **non-final**; the **version-of-record article** PDF curated on [[2013gouissem-computationa-reactive-force-field-2]] is the preferred locator for section numbers, equations, and edited wording.

## Methods

The underlying article follows the standard **ReaxFF** decomposition of the total energy into bonded (bond-order-dependent), **van der Waals**, and **Coulomb** contributions, specialized here to **Zr**, **Hf**, and **B** (see **Eq. (3)** and surrounding definitions on [[2013gouissem-computationa-reactive-force-field-2]]). **Parameter optimization** proceeds by **weighted least squares** minimization against **DFT** reference data: **periodic** **ZrB₂** and **HfB₂** calculations support bulk-like bonding environments, while **cluster** potential-energy scans and geometries for species such as **Zr(BH₂)₂** and **Hf(BH₂)₂** (with basis sets and functionals specified in **Sections 3–4** of the published paper) anchor molecular fragmentation and coordination trends. **Section 5** documents post-fit validation using **ReaxFF molecular dynamics** on crystal- and defect-like motifs to check consistency with **QM** or literature references. For this **proof** path, the wiki does **not** assert differences in scientific content relative to [[2013gouissem-computationa-reactive-force-field-2]]; the distinction is **provenance and citation hygiene** (which PDF bytes the manifest tracks) rather than an alternate parameterization.

**1 — MD application (atomistic dynamics).** **Section 5** reports illustrative **molecular dynamics** with the fitted **ReaxFF** on **crystal**- and **defect**-like **ZrB₂**/**HfB₂** motifs. **Engine / code:** **N/A —** explicit **MD** engine string not transcribed on this proof-ingest page (confirm **LAMMPS** vs alternatives in **`pdf_path`** / [[2013gouissem-computationa-reactive-force-field-2]]). **System size & composition:** **atom** counts / **supercell** definitions for each validation demo—copy from **`pdf_path`**. **Boundaries / periodicity:** **PBC** details—copy from **`pdf_path`**. **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** not duplicated here; see canonical page. **Temperature:** finite-**temperature** **MD** is part of the **Section 5** narrative in the article (exact **K** targets in **`pdf_path`**). **Pressure:** **N/A —** not summarized here. **Electric field:** **N/A —**. **Replica / enhanced sampling:** **N/A —**.

**2 — Force-field training.** **Parent FF / elements:** **ReaxFF** for **Zr–B** and **Hf–B**, using the reduced **Eq. (3)** energy expression specialized in the manuscript. **QM reference:** **QuantumWise** (**DFT**) for periodic **ZrB₂**/**HfB₂** crystal-phase data; **Gaussian 09** for **Zr(BH₂)₂** and **Hf(BH₂)₂** cluster **PES**/**geometry** targets (**Section 3**/**4**). **Training set:** periodic **DFT** points plus cluster **QM** scans. **Optimization:** **weighted least squares** **ReaxFF** parameter fit to the **QM** training data. **Reference data / validation:** **Section 5** **MD** vs **QM**/literature checks as reported.

**3 — Static QM / DFT.** Treated as the **QM reference** engine for training (not a separate QM-only application paper).

## Findings

**1 — Outcomes & mechanisms.** The optimized **ReaxFF** reproduces targeted **QM energetics** and **structural** metrics for the **ZrB₂**/**HfB₂** training sets, enabling **reactive** simulations of boride chemistry where simpler fixed-bond models would be inappropriate.

**2 — Comparisons.** **Section 5** compares **MD** results to **QM** or literature references for selected motifs (tables on [[2013gouissem-computationa-reactive-force-field-2]]).

**3 — Sensitivity & design levers.** Which **clusters** and **bulk** phases enter the **QM** training database controls subsequent **MD** reliability; explicit **temperature**/**pressure** sweeps (if any) should be read from **`pdf_path`**.

**4 — Limitations & outlook.** **Transferability** to complex multicomponent ceramics and long-time high-temperature kinetics remains contingent on expanded training data, as discussed in the article.

**5 — Corpus honesty.** Cite **equations**, **Section** numbers, and validation tables from **`[[2013gouissem-computationa-reactive-force-field-2]]`**; this slug documents the **Elsevier proof** PDF bytes (`papers/Afif_CompMatSci_2013_galley.pdf`) only.

## Limitations

**Proof** PDF is not authoritative for **pagination** or **final** edited wording; **transferability** to complex ceramics still depends on expanded training (as on the canonical page).

## Relevance to group

**van Duin** collaboration extending **ReaxFF** to **ZrB₂**/**HfB₂** for **extreme-environment** materials.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2012.12.038](https://doi.org/10.1016/j.commatsci.2012.12.038) — proof: `papers/Afif_CompMatSci_2013_galley.pdf`.

## Reader notes (navigation)

- **Version-of-record article page:** [[2013gouissem-computationa-reactive-force-field-2]].

## Related topics

- [[2013gouissem-computationa-reactive-force-field-2]]
- [[reaxff-family]]
