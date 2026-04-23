---
id: paper:2024hossain-npj-computat-ereaxff-force
type: paper
title: "eReaxFF force field development for BaZr0.8Y0.2O3-delta solid oxide electrolysis cells applications"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - material:perovskite-oxide
  - domain:oxides-ceramics
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-024-01268-9"
year: 2024
authors:
  - "Md Jamil Hossain"
  - "Prashik Gaikwad"
  - "Yun Kyung Shin"
  - "Jessica A. Schulze"
  - "Katheryn A. Penrod"
  - "Meng Li"
  - "Yuxiao Lin"
  - "Gorakh Pawar"
  - "Adri C. T. van Duin"
venue: "npj Computational Materials (2024)"
pdf_sha256: "75283701e930659a58ef6fd8619c70f8e15fcbcfd52fb8ff0c4edf15c0727d82"
pdf_path: "papers/Hossain_eReaxFF_YSZ_npjCompMat_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024hossain-npj-computat-ereaxff-force -->

## Summary

An eReaxFF parametrization for BaZr0.8Y0.2O3-delta (BZY20) is fitted to DFT and constrained-DFT data for oxygen vacancies, water chemistry, and excess electrons, then applied in zero- and finite-bias-style MD to probe water splitting, proton motion, and hydrogen evolution on BZY20 surfaces.

## Methods

**QM reference:** DFT targets include Y-doping site preference in bulk BZY20, **oxygen-vacancy formation energies** in bulk and on **(100)** and **(110)** slabs with **Ba-O** versus **Zr-Y-O** terminations and variable surface vacancy concentrations (e.g. **12.5%** and **25%** for supercell convenience), **equations of state**, **H2O adsorption and splitting** energies, **H2** formation energies, and **C-DFT** energies for an **excess electron** localized on lattice oxygens in isolated clusters (parameterized **electron hopping** barriers, e.g. **~16.87 kcal/mol** O1 to O10 and **~9.85 kcal/mol** in a hydrogenated cluster scenario per SI). **eReaxFF** optimization targets qualitative trends for vacancy formation energies while emphasizing **Y-site energies**, **bond lengths**, and **EOS** agreement.

**Reactive MD:** **Bond-scan** biasing potentials assess barriers for adsorption, splitting, and H2 evolution. Large-scale examples: **Zr-Y-O (100)** slab with **12.5%** surface vacancies, periodic box **~42.95 x 42.90 x 50.00 Angstrom**, **steam** represented by repeated **H2O** additions (**10 H2O** every **200 ps**), **1000 K**, **NVT**, **~3000 atoms**, **200 ps** segments run in **~48 h CPU** on **four CPUs** cited for one case; zero-bias runs used **Amsterdam Modeling Suite (AMS)**. **ACKS2** charge updates accompany explicit electrons in eReaxFF. Authors apply an **H-H bond bias** (SI table) to lower H2-formation barriers for observable MD time scales.

**1 — MD application.** **Code:** **eReaxFF**-based dynamics in **AMS** for cases cited. **Size:** order **~3000-atom** slab **supercell**; **(100) Zr-Y-O** with **12.5%** surface O vacancies. **PBC** **slab** geometry. **NVT** at **1000 K**; **timestep** and **Nose**/**Berendsen** details for all runs: **N/A** if not in this note—**PDF** tables. **Duration:** **H2O** dosed every **200 ps**; cumulative **1.4 ns** steam MD cited in the narrative. **No NPT** hydrostatic **pressure** or **barostat** in the long zero-bias example summarized. **No external electric field**; **voltage** enters via **biasing** and **explicit electron** treatments, not a continuum field table here. **Enhanced sampling** beyond **bond-biased** / constrained pathways: **N/A** in the short summary. **2 — Force-field training.** Covered above (**QM** targets, **C-DFT**, **eReaxFF** reoptimization). **3 — Static QM-only:** not applicable as the main contribution—**DFT** and **C-DFT** serve the **eReaxFF** fit; standalone static-only claims follow the **QM** and **eReaxFF** validation sections in the paper.
## Findings

DFT and eReaxFF agree that **BZY20 "Type 3"** Y-doping is most stable and that **EOS** near equilibrium volume matches well. **Surface chemistry:** On **Zr-Y-O (100)** with vacancies, water adsorbs strongly to vacancies; **Path A** (H on lattice O between **Y and Zr**) is **kinetically favored** over **Path B** (between two **Zr**) with lower barrier (**~7 vs ~9 kcal/mol**) and more exothermic splitting. **H2** evolution barriers from surface OH are **very high** without voltage (**~70-90 kcal/mol** class), so **no H2** forms in **zero-bias** long MD. **Ba-O (100)** termination shows **stronger** vacancy adsorption but less favorable single-water splitting unless **water-assisted** proton transfer lowers the barrier (**~13.4 kcal/mol** vs **~37.5 kcal/mol** for single-water path in the reported scan). **Explicit excess electron** on OH lowers one H2 barrier pathway to **~45 kcal/mol** from **~67 kcal/mol**; with **H-H bias**, barriers fall to about **28.4 kcal/mol** (no excess electron) and **~20 kcal/mol** (with excess electron). **1.4 ns** cumulative **steam** MD on the **Zr-Y-O** surface shows **vacancy filling**, **water dissociation**, **proton transfer** into **subsurface layers** (down to **sixth** layer cited), and **no H2** without applied bias, consistent with high barriers. **Comparisons / parameter sensitivity** (e.g. surface termination, **bias** vs **H-H** workarounds) are as stated in the **PDF**; **kcal/mol** locators in this note are **VOR**-backed, not the galley duplicate elsewhere in the corpus.
## Limitations

**eReaxFF** and **bond-biased** / **explicit-electron** workflows are **approximate** stand-ins for **electrode polarization** and **electrolyte** microenvironments; **zero-bias** long MD omits **steady-state** **applied voltage** boundary conditions. **Absolute** **oxygen-vacancy** formation energies are described as **qualitatively** tracked in places; transferability beyond **BZY20**-like stoichiometries and surface terminations is not established in one article.

## Relevance to group

Co-authored **eReaxFF** development for **proton-conducting perovskite** electrochemistry with **Adri C. T. van Duin**, supporting **solid-oxide** interface simulation in the corpus.

## Citations and evidence anchors

- DOI: [10.1038/s41524-024-01268-9](https://doi.org/10.1038/s41524-024-01268-9)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
