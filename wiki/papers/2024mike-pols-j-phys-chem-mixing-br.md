---
id: paper:2024mike-pols-j-phys-chem-mixing-br
type: paper
title: "Mixing I and Br in Inorganic Perovskites: Atomistic Insights from Reactive Molecular Dynamics Simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:perovskite-oxide
  - material:widegap-semiconductor
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:npt-simulation
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c00563"
year: 2024
authors:
  - "Mike Pols"
  - "Adri C. T. van Duin"
  - "Sofía Calero"
  - "Shuxia Tao"
venue: "J. Phys. Chem. C 2024 (see DOI for volume/pages)"
pdf_sha256: "2165f96a9a676bc5bc8737b88f8f4ff7d30c3c02006594ea95108629066f4ea6"
pdf_path: "papers/Pols_JPCC_2024_IBr_Perovskites_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024mike-pols-j-phys-chem-mixing-br -->

## Summary

The study extends a **CsPbI\(_3\)**-focused **ReaxFF** parametrization to **CsPbBr\(_3\)** and **mixed CsPb(Br\(_x\)I\(_{1-x}\))\(_3\)**, training to **VASP**/**ADF** **PBE + D3(BJ)** data (equations of state, precursor phases, **defect** formation/migration, phase transitions). **CMA-ES** optimization in **ParAMS**/**AMS 2022** minimizes a weighted **SSE** loss starting from prior **Cs/Pb/I** parameters and **scaled** **Br** interactions. Large **NPT**-style **ReaxFF MD** sweeps map **temperature–composition** behavior of **pseudocubic** lattice vectors and **octahedral tilting**, showing that **Br** substitution **lowers** the **cubic**-like transition temperature and couples to **~2 nm** cooperative **octahedral** dynamics—consistent with strong effects at **x ≤ 1/4**.

## Methods

- **Reference QM:** **VASP** and **ADF** with **PBE + D3(BJ)**; training properties include **atomic charges**, **EOS** of **perovskite** and **non-perovskite** phases, **precursor** **EOS** (**CsX**, **PbX\(_2\)**), **defect** energies/barriers, and **phase** transitions (Supporting Information Notes).
- **ReaxFF fit:** **SSE** objective with weights **σ\(_i\)**; **CMA-ES** in **ParAMS**; initial **Br** parameters from **scaled** **I**-interaction starting points (SI Note 2).
- **MD validation / phase diagrams:** **Gradual heating** **100–700 K** for compositions **x = 0, 1/8, …, 1**; monitor **lattice vectors** and **octahedral** orientation angles (**θ\(_x\), θ\(_y\), θ\(_z\)**); compare **unit-cell volumes** at **575 K** to experiment within **~1%** (Figure 2).

**1 — NPT** **ReaxFF** **MD** (phase mapping). **Engine:** **LAMMPS** + fitted **ReaxFF**; **3D PBC** **pseudocubic** **perovskite** **supercell**s at each **halide** **composition** **x**; **NPT** isotropic with **Nose–Hoover**/**Berendsen**-style **thermostat** + **Parrinello**/**Berendsen**-class **barostat** as in the article (**GPa**-scale isotropic **pressure** near **0**). **Integration timestep** in **fs** (typically sub-**1 fs** for **ReaxFF** **halide** perovskites): **JPCC** *Methods* if not copied here. **E-field, umbrella, MTD:** **N/A**. **Ramped** **100–700 K** **anneal** over **multi-ns**-scale (exact **ps**/**ns** **equilibration** and **production** / **ramp** **duration**: **JPCC** if not tabulated in this one-page blurb). **Compositions** x = 0, 1/8, …, 1. **2 — CMA-ES / ParAMS** training: **PBE + D3(BJ)** **VASP/ADF** targets (first bullets). **3 — Static-only** primary claim: **N/A** beyond training references.
## Findings

- The fitted potential recovers **DFT**-ranked **bulk** stability ordering for **CsPbI\(_3\)** phases and **positive** **mixing enthalpies** for **Br/I** substitution (**< ~1 kcal/mol per formula unit** in their Table/figures), with noted discrepancies near **x = 1/6** and **1/4** linked to overstabilized **mixed** supercells (SI).
- **Defect** barriers—for example **I** **vacancy** migration **~4.8 kcal/mol** (**ReaxFF**) vs **~7.0 kcal/mol** (**DFT**)—track the training set reasonably, enabling **kinetic** discussions.
- **Pure** **CsPbBr\(_3\)** attains **cubic**-like averages at **lower** temperature than **CsPbI\(_3\)** in the simulations (**~310 K** vs **~430 K**), with **Br**’s smaller ionic radius (**~1.96 Å** vs **I** **~2.20 Å**) reducing **lattice** volumes and **Goldschmidt tolerance**-related behavior as discussed.
- For **mixtures**, most of the **drop** in **cubic** onset temperature occurs by **x ≤ 1/4**, matching experimental narratives that **small Br** fractions strongly stabilize **cubic**-like **halide** perovskites; **octahedral** **tilt** correlations show **coherence lengths** up to **~2 nm**, explaining long-range sensitivity to dilute **Br**.

The **Pols–Tao–Calero–van Duin** line thus treats **halide mixing** as both a **thermodynamic** and a **dynamic** problem: **tilt coherence** and **defect migration** are co-trained against **DFT** so that **composition–temperature** maps are not inferred from **static** energies alone. **DFT** vs **ReaxFF** **defect** barriers, **T**-dependent **cubic**-like onsets, and **Br**-dilution trends are the key **sensitivity** levers. **JPCC** line-edited **VOR** **PDF** is authoritative.
## Limitations

**PBE + D3(BJ)** training biases **transition temperatures** low by **~50–100 K** vs experiment; **ReaxFF** cannot capture **electronic** **band** properties.

## Relevance to group

Continues the **Eindhoven–van Duin** **halide perovskite** **ReaxFF** line (**Pols**, **Tao**, **Calero**) for **CsPb(Br\(_x\)I\(_{1-x}\))\(_3\)** **phase** behavior.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c00563](https://doi.org/10.1021/acs.jpcc.4c00563)

## Related topics

- [[reaxff-family]]
- [[2021mike-pols-j-phys-chem-atomistic-insights]]
