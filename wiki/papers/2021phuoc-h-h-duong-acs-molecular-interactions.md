---
id: paper:2021phuoc-h-h-duong-acs-molecular-interactions
type: paper
title: "Molecular Interactions and Layer Stacking Dictate Covalent Organic Framework Effective Pore Size"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:zeolite-porous
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c10866"
year: 2021
authors:
  - "Phuoc H. H. Duong"
  - "Yun Kyung Shin"
  - "Valerie A. Kuehl"
  - "Mohammad M. Afroz"
  - "John O. Hoberg"
  - "Bruce Parkinson"
  - "Adri C. T. van Duin"
  - "Katie D. Li-Oakey"
venue: "ACS Appl. Mater. Interfaces 2021, 13, 42164–42175"
pdf_sha256: "4f94e549399495e4ea82f0f7b81fdefce15539f90dfd78c91067902c5b2b0f26"
pdf_path: "papers/Duong_Shin_ACS_AMI_COF_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021phuoc-h-h-duong-acs-molecular-interactions -->

!!! abstract "Scope"
    Reactive (ReaxFF) molecular dynamics of an imine-linked **carboxylated COF (C-COF)** membrane, compared with experiments, to relate **effective** pore size and solvation to organic-solvent nanofiltration performance.

## Summary

Covalent organic frameworks (COFs) offer designer pores for molecular separations, yet **crystallographic** pore dimensions can mislead when **solvation**, **framework flexibility**, and **layer stacking** renormalize what solutes experience in the liquid phase. This **ACS Applied Materials & Interfaces** study couples **ReaxFF reactive molecular dynamics** with experiments on an **imine-linked carboxylated two-dimensional COF (C-COF)** membrane platform used for **organic solvent nanofiltration (OSN)**. The authors relate **effective pore size**, **layer registry**, and **interfacial interactions** to measured **permeance** and **selectivity**, arguing that transport metrics must be interpreted with explicit **solid–liquid** structure rather than nominal pore metrics alone. **Adri C. T. van Duin** co-authors, placing the work in the group’s reactive FF portfolio for soft porous materials.

## Methods

**Experiments (C-COF membrane, OSN).** The **imine**-**linked** **carboxylated** **2D** **C-COF** is **synthesized** and **processed** into a **membrane** **platform**; **organic** **solvent** **nanofiltration** (**OSN**) **tests** report **permeance** and **selectivity** vs **solute** **probes** and **feeds** as in *ACS Appl. Mater. Interfaces* **13**, **42164**–**42175** (DOI `10.1021/acsami.1c10866`). **Characterization** (**PXRD**, **microscopy**, **porometry**-class **data** as **figured**) **frames** the **real** **membrane** **morphology** (mosaicity, **defects**, **layer** **stacking**).

**MD application (ReaxFF; LAMMPS in practice).** The *ACS Appl. Mater. Interfaces* Methods describe **ReaxFF** in **periodic 3D** **C–COF**+**solvent** **supercells** (in-plane **xy** and **z**-periodic **pore** channels from the **article**; exact **stoichiometry** in **Table**/**SI**). **Equilibration: NPT** at **300 K** and **0** **atm** to relax **lattice**+**pore** **void** (**0.25 fs** time step, **200 ps**); **Berendsen** thermostat (relaxation **~100** **fs**) and **Berendsen** barostat (relaxation **~1000** **fs**). **Production for diffusion: NVT** **200 ps** at the **same T** (Berendsen thermostat, **~1000** **fs** **coupling** in the “weak” **NVT** block as written). **E-field, shear, impact, metadynamics — N/A** in the **methods** as summarized.

**FF reparameterization. N/A** (literature ReaxFF for the **C–COF** chemistry, per article).

**Standalone DFT benchmark. N/A** for the **main** **MD** line (**DFT** is cited only in the general **ReaxFF**-validation literature sense).

## Findings

**Outcomes and mechanisms.** **Mosaic** **C-COF** **membranes** with **contiguous** **1D** **pore** **percolation** can deliver **strong** **OSN**; **poor** **in-plane** **registry** or **defects** that **chop** **channels** **hurt** **transport** even when **crystal** **chemistry** is the **same**. **Simulations** **(ReaxFF)** and **permeation** **data** **converge** on the idea that **solvated** **solute** **hindrance** and **carboxylate** **ionization** (set by **pH**/**base**) **tune** **exclusion** **and** **affinity**, not the **naked** **X-ray** **pore** **metric** alone. **N/A** here to **re-tabulate** every **D_solv** or **J** **value**—**see** **PDF**.

**Comparisons.** The **work** is **positioned** **as** a **case** **for** **experimental** **+** **atomistic** **agreement** on **effective** **pore** **throat**; **N/A** **third**-**party** **industrial** **dataset** in the **cited** **text**.

**Sensitivity. Solvent** **polarity**/**H-bonding** and **solute** **diameter** **(with** **shell)** **trend** with **rejection**/**J**; **N/A** in this **note** to **sweep** **E-field**.

## Limitations

Results are tied to the specific C-COF chemistry and solvents studied; generalization to other link chemistries or feed mixtures requires additional modeling and experiment.

## Relevance to group

Demonstrates ReaxFF for porous organic frameworks and membrane separations with experimental co-validation.

## Citations and evidence anchors

- DOI: [10.1021/acsami.1c10866](https://doi.org/10.1021/acsami.1c10866)

## Related topics

- [[reaxff-family]]
