---
id: paper:2023krstic-j-appl-phys-detailed-studies
type: paper
title: "Detailed studies of the processes in low energy H irradiation of Li and Li-compound surfaces"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1063/5.0149502"
year: 2023
authors:
  - "P. S. Krstic"
  - "E. T. Ostrowski"
  - "S. Dwivedi"
  - "S. Abe"
  - "A. Maan"
  - "A. C. T. van Duin"
  - "B. E. Koel"
venue: "J. Appl. Phys."
pdf_sha256: "24f67e261541992bc3d5b891979f712f9fa0ffd0c2f69fd2154953e39c7f713c"
pdf_path: "papers/Krstic_Dwivedi_H_LiO_JAP_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023krstic-j-appl-phys-detailed-studies -->

Perspective article on plasma–material interaction at lithium-containing surfaces relevant to magnetic fusion: low-energy (1–100 eV) hydrogen irradiation of amorphous lithium oxide and lithium hydroxide surfaces is simulated and compared with prior work on amorphous Li and LiH, with emphasis on charge evolution and surface response.

## Summary

The work addresses how hydrogen-fuel irradiation drives reflection, retention, chemical sputtering, and related processes on amorphous surfaces containing Li, O, and H—materials relevant to lithium-conditioned plasma-facing components. The study highlights electronegativity-driven polarization of Li and O and the need for reactive modeling that captures charge redistribution during collision cascades.

The *J. Appl. Phys.* abstract stresses **side-by-side** treatment of **reflection**, **retention**, and **sputtering** on the **same footing** for **amorphous Li\(_2\)O** and **LiOH** versus earlier **amorphous Li** and **LiH** benchmarks, and argues that **time-dependent charging** of **Li/O/H** during **H** irradiation can steer **surface chemistry** in ways that couple back to **recycling**, **erosion**, and **plasma confinement** modeling.

## Methods

### Interaction model (ReaxFF + EEM) (A/B)

**Classical MD** with **ReaxFF** bond order + **electronegativity equalization** in **LAMMPS** so **charges** evolve with **geometry** during cascades (**Coulomb** long-range included).

### Amorphous surface preparation

**Li\(_2\)O** / **LiOH** slabs from **fluorite** **Li\(_2\)O** supercells: **minimize**, **thermalize**, **relax** to **2D periodic** surfaces, then **amorphize** via **heat/anneal** cycles and final relaxation. Example **LiOH** cell ~**5.6 × 5.6 × 12.2 nm**, **29 735** atoms (~equimolar **Li/O/H**).

### Impact protocol (B)

Incident **H** (also **D/T** context) **1–100 eV**, varied **incidence angles**; **Δt = 0.25 fs**; **4 000–10 000** steps per run. Accumulate **~10³** impacts on **~3.5 × 3.5 nm\(^2\)** patch for **statistics**.

### 1 — MD application (atomistic dynamics) — impact cascades

**Engine / code:** **LAMMPS** with **ReaxFF** + **electronegativity equalization** (EEM) for **dynamical charges**; **Coulomb** as in the article. **System & composition:** amorphous **Li\(_2\)O** and **LiOH** **slab** **cells**; example **~29 735** **atoms** in a **5.6 × 5.6 × 12.2 nm** **LiOH** case (~equimolar **Li/O/H**). **Boundaries / periodicity:** **2D in-plane PBC** for the **bombarded** **surface** **patches** (z non-periodic or as defined in the paper for the slab). **Ensemble & thermostat for impacts:** **N/A** in this short page—the article specifies whether **NVE**-like short trajectories and/or **thermostat**-attached **baths** are used in different stages. **Barostat / hydrostatic pressure target:** **N/A** for **cascade** **bombardment** in this note. **Timestep:** **0.25** fs; **4 000–10 000** **steps/impact** as in the **Impact protocol** above. **Total wall-clock per impact:** **N/A** — see paper. **Temperature:** **~300** K for **prepared** **surfaces**; **beam** **energy** **1–100** eV is the main **driving** variable, not a thermostat setpoint. **External electric or magnetic field in MD:** **N/A** (here the focus is **H**-beam **PMI**, not a macroscopic **E**-field in the **MD**). **Coulomb / cutoffs** as in the **J. Appl. Phys.** model. **Enhanced sampling:** **N/A** — direct **cascade** **sampling**.

### 2 — Force-field training

**N/A** — the work **applies** **ReaxFF**/**EEM** to **Li–H–O** **surfaces**; parameter provenance and validation context are in the article and prior work.

### 3 — Static QM

**N/A** — the paper compares to **select** **quantum**/**classical** references; full **DFT** production is not the core **Methods** line here.

## Findings

### Process competition

**Reflection**, **retention**, and **chemical sputtering** analyzed jointly and compared to prior **amorphous Li** / **LiH** studies.

### Charging and PMI coupling

**Time-dependent** **Li/O/H** **charges** under irradiation alter **erosion** and **recycling** kinetics—relevant to **lithium-conditioned** **plasma-facing** components.

The abstract narrative also connects these atomistic mechanisms to **tokamak** **PMI** contexts where **lithium** coatings are used to modify **impurity** gettering and **hydrogen** **recycling**, motivating **reactive** models that retain **charge evolution** rather than **fixed-partial-charge** cascades alone.

**Compared** to prior **amorphous** **Li** and **LiH** **sputtering** data, the **H**-beam **energy** **(1–100 eV)**, **grazing** **incidence**, and **surface** **chemistry** **(Li\(_2\)O/LiOH)** set a **sensitivity** map for **chemical sputtering** that **EEM**+**ReaxFF** is meant to reproduce; **ReaxFF**-level **kinetic** **reaction** barriers remain an **inherent** **uncertainty** relative to **QCMD**, and the **open** **future** direction in such **PMI** **work** is to extend the **H**-energy window and **surface** **morphology** with longer **NVT**-equilibrated **patches**—**confirm** all **trends** in the **peer-reviewed** `pdf_path` because this page does not capture every **table**.

## Limitations

EEM-based charge updates approximate quantum mechanical polarization; the authors contrast this with full QCMD cost and note validation against selected quantum–classical results in related work. Low-energy chemical sputtering requires large cells at grazing incidence and higher impact energies to capture penetration depth, increasing cost.

## Relevance to group

Co-authored by **A. C. T. van Duin**; extends ReaxFF/EEM lithium–oxygen–hydrogen surface chemistry for fusion PMI in collaboration with Princeton and Stony Brook groups.

## Citations and evidence anchors

- DOI: [10.1063/5.0149502](https://doi.org/10.1063/5.0149502)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Theme hubs: fusion / energy materials as covered elsewhere in the corpus when linked from indexes.
