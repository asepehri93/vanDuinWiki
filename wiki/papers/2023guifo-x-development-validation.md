---
id: paper:2023guifo-x-development-validation
type: paper
title: "Development and Validation of a ReaxFF Reactive Force Field for Modeling Silicon–Carbon Composite Anode Materials in Lithium-Ion Batteries"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:lammps
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c07773"
year: 2023
authors:
  - "Stéphane B. Olou'ou Guifo"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "d8d2e6f9492080ef9c0965e0bd00cbbcdfc870a226560a8c4cf9ce2441f648c1"
pdf_path: "papers/Guifo_LiSiC_JPCC_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023guifo-x-development-validation -->

## Summary

**Silicon–carbon** composites are pursued as **high-capacity** **anodes** because **sp²-carbon** buffers can mitigate **pulverization**, yet **atomistic** models must capture **Li–Si**, **Li–C**, and **interfacial** chemistry simultaneously. Olou’ou Guifo and van Duin develop a **Li–Si–C ReaxFF** parametrization fit to an extensive **PBE**-level **DFT** database covering **equations of state**, **cohesive energies**, **surfaces**, **interfaces**, and **lithiation**-connected reaction energetics across binary and **ternary** motifs. The fitted field is deployed in **LAMMPS** **MD** and **Monte Carlo** workflows targeting **Si–sp²-C** microstructures, **SiC-rich** domains, **amorphous lithium carbide** formation, and **grain-boundary** **interphases** during **(de)lithiation**.

## Methods

### QM training database (C) and ReaxFF optimization (A)

- **DFT reference:** **PBE**-level data for **Li–Si**, **Li–C**, **Si–C**, and **Li–Si–C** configurations: **equations of state**, **cohesive energies**, **surfaces**, **interfaces**, and **lithiation**-connected energetics (full list in article/SI).
- **Fitting:** Iterative **weighted** minimization of **ReaxFF** vs **DFT** observables across **binary/ternary** and **amorphous/defective** snapshots.

### Production atomistic workflows (B)

- **Codes:** **LAMMPS** **MD** with optional **Monte Carlo** moves as described in *J. Phys. Chem. C*.
- **Structures:** **Si–sp²-C** composites, **SiC-rich** domains, **grain-boundary** cells juxtaposing **Si-rich** and **C-rich** regions to monitor **Li segregation** and **adhesion**.
- **Corpus PDF:** Galley at `papers/Guifo_LiSiC_JPCC_2023_galley.pdf`—confirm numbers against **VOR**.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with the new **Li–Si–C** **ReaxFF**, plus **Monte Carlo** moves when used for sampling as described in the article. **System & composition:** **Si–sp\(^2\)-C** and **SiC**-containing **composite**-like cells and **grain-boundary** constructions for **(de)lithiation** (details in the paper). **Boundaries / periodicity:** **3D PBC** as appropriate for those cells. **Ensemble, timestep, thermostating, barostat, production length:** the **JPCC** text uses **NVT** and **NPT**-style **MD** over **ps**–**ns** **durations** to follow **(de)lithiation** and **stress**-related **observables**; **hydrostatic** **pressure** in **GPa** (or **stress** **tensors**) is reported in the **article** when needed for **volume**-constrained **Si–C** **microstructures**—**N/A** to paste every **NVT**/**NPT** **switch** and **ns** **clock** on this page (use **VOR**/**SI**). **Temperature, stress, lithiation stage:** as in the reported **illustrations**. **Electric field / bias in MD:** **N/A** in the short summary (bulk anode **chemistry**, not a biased **cell** in the abstract). **Enhanced-sampling (umbrella, metadynamics, RE):** **N/A** here.

### 2 — Force-field training (summarized with §QM training database above)

**Parent / scope:** new **ReaxFF** for **Li–Si–C** (extends prior **C/Si**/**Li**-containing ReaxFF lines; see **Introduction** and **Methods** in `pdf_path`). **QM reference:** **PBE** **ab initio** data across **equations of state**, **cohesive** energies, **surfaces**, **interfaces**, and **(de)lithiation**-linked energetics for **binary/ternary** and **a-SiC/a-C**-like **motifs** (database summarized in the article and SI). **Training set** diversity and **weighting** as reported. **Optimization** software and iteration: per **J. Phys. Chem. C** (e.g. **CMA-ES**-class workflow where stated). **Reference to experiments:** validation framed against **ab initio**; **N/A** — the abstract’s examples are **in silico** illustrations.

## Findings

### Training-set performance

The field reproduces the **optimization** targets used for **Li/Si/C** chemistry in the published training suite.

### Lithiation mechanics (illustrative)

Abstract-level example reports **~668% volumetric expansion** in an **a-Li\(_{4.4}\)(SiC)\(_{0.5}\)**-like scenario, tied to **soft amorphous lithium carbide** formation that accommodates strain.

### Interdomain behavior

**Li-rich interphase** regions at **Si/C** boundaries can **improve adhesion** and shift local **(de)lithiation voltage** by up to **~1 V** vs bulk-like regions in the authors’ analysis.

### Modeling scope

Targets **composite** microstructures where **sp² carbon** buffering and **SiC**-rich regions matter—distinct from **pure Si** anode models.

At the level of the **JPCC** **abstract** and main **figures**, the new **ReaxFF** recovers the **lithiation**-driven **reaction** **pathways** (alloying + carbide **formation**) and **interfacial** **morphology** **compared** with **PBE** **reference** data used in the **fit**, and highlights a **sensitivity** of local **(de)insertion** overpotential to **domain** **geometry**; **ReaxFF**-specific **kinetic** and **thermodynamic** **uncertainties** remain—an **inherent** **limitation** when **extrapolating** to long **cycle** life—alongside **SEI** and **continuum** **resistance** effects **outside** the **parameterization**. **Future** **work** in the field would add explicit **electrolyte** **chemistry**; for **citations** use the **peer-reviewed** **PDF** at `pdf_path` (or **VOR** if the **galley** is reconciled to the issue).

## Limitations

Galley PDF in corpus may differ cosmetically from the final issue; thermodynamic voltages and capacity metrics remain **model-dependent**. When reconciling with experiments, prioritize **half-cell** references and **SEI** chemistry not captured in these **bulk** **Li–Si–C** cells. **Particle** **morphology** in real **composite** electrodes may introduce **percolation** constraints not represented in the illustrative **MD** cells summarized in the abstract. **Grain-boundary** cells in the paper are included precisely to watch **adhesion** and **voltage** **shifts** where **Si-rich** and **C-rich** domains meet—those **interphase** **trends** are **qualitative** **ReaxFF** outcomes tied to the **training** database, not universal **engineering** **metrics**.

## Relevance to group

Foundational **Li/Si/C ReaxFF** for **composite anode** design space, directly aligned with **van Duin** parameterization workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.2c07773](https://doi.org/10.1021/acs.jpcc.2c07773)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
