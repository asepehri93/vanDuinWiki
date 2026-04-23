---
id: paper:2015han-venue-atomistic-observation
type: paper
title: "Atomistic Observation of the Lithiation and Delithiation Behaviors of Silicon Nanowires Using Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - material:li-metal-anode
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:reactive-md
source_refs: []
doi: "10.1021/jp5094756"
year: 2015
authors:
  - "Hyun Jung"
  - "Minho Lee"
  - "Byung Chul Yeo"
  - "Kwang-Ryeol Lee"
  - "Sang Soo Han"
venue: "J. Phys. Chem. C"
pdf_sha256: "8b3356f302bcea85a4a6af7e5a08d0baa9e1f9815a33f6ab8eb0d6fa8f107108"
pdf_path: "papers/ReaxFF_others/Han_LiSi_JPC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015han-venue-atomistic-observation -->

## Summary

Han *et al.* present **large-scale ReaxFF molecular dynamics** of **lithiation** and **delithiation** in **silicon nanowires**, using a **Li–Si parameter set** fit to **first-principles** data within the same publication. The study focuses on how **crystalline Si** transforms to **amorphous lithiated silicon** under **Li** insertion, how **volume expansion** depends on **surface facet**, and how **delithiation** can partially regenerate **crystalline Si** domains at intermediate **Li** stoichiometries. The work connects **mechanical** anisotropy, **bond-breaking** under stress, and **microstructural** motifs such as **silicene-like** intermediates to the broader **Li-ion anode** literature where **Si** offers high capacity but large **strain** and **degradation**. By explicitly varying **surface termination** and **delithiation rate**, the authors aim to separate **kinetic** pathways from **thermodynamic** two-phase coexistence that may appear in **a-Li\(_x\)Si** matrices.

## Methods

### Force-field training (Li–Si ReaxFF)

- **QM reference / targets:** a **Li–Si ReaxFF** parameter set is **fit to first-principles data** in this work (details, training sets, and weighting are in the article **Supporting Information** as referenced in the main text).
- **Optimization:** standard **ReaxFF optimization** workflow (successive parabolic / ReaxFF-culture procedures cited therein), benchmarked against the QM training database used for **Li–Si** reactions and equations of state.

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with **velocity-Verlet** integration.
- **Timestep / thermostat / ensemble:** **0.5 fs** timestep; **canonical NVT** at **300 K** with a **Nose–Hoover thermostat** (**0.01 fs⁻¹** damping parameter as stated in *J. Phys. Chem. C* **2015**, DOI **10.1021/jp5094756**).
- **Systems:** **~10⁵-atom**-class **Si nanowires** (~**5 nm** diameter, ~**10 nm** length) with two contrasting **surface terminations** discussed in the article: **four {110} + four {100} facets** vs **six {110} facets**.
- **Boundary conditions:** **3D periodic boundary conditions (PBC)** are used for the **nanowire** **supercell** setup in **LAMMPS** (as standard for isolated wires embedded in a simulation box).
- **Protocol:** **Li insertion/removal** sequences are applied to study **lithiation** and **delithiation** pathways and kinetics (exact insertion rates/schedules are specified in the article/SI).
- **Duration / staging:** representative lithiation/delithiation segments are propagated to **~1000 ps** (and shorter **75–500 ps** windows for specific stages) as tabulated in the **J. Phys. Chem. C** article—see **papers/ReaxFF_others/Han_LiSi_JPC_2015.pdf** for the full stage list.
- **Barostat / pressure / fields:** **N/A —** constant-volume **NVT** lithiation protocol (no applied stress barostat reported in the excerpted computational details).

### Static QM / DFT

Used as the **training reference** for ReaxFF development (see **Supporting Information**), not as on-the-fly **ab initio MD** in the large-scale wire simulations.

## Findings

**Lithiation** swells wires **anisotropically** according to **facet** population, yet **fully lithiated** volumes converge across the facetings studied. **Li** penetrates **c-Si** preferentially along **⟨110⟩**/**⟨112⟩**-related channels, forming **a-Li\(_x\)Si** with **Si–Si** scission under local tension; **silicene-like** structures appear **transiently** before deeper lithiation yields **low-coordinated** Si. **Delithiation** can nucleate **small c-Si** regions inside **a-Li\(_x\)Si** near **Li\(_{1.4–1.5}\)Si**, with **rate-dependent** crystalline fraction and discussion of **two-phase c-Si + a-Li\(_x\)Si** versus single-phase amorphous arrangements. The authors relate trajectories to **experimental** Si nanowire morphologies. **Delithiation rate** and **surface** termination shift crystalline recovery and expansion pathways; insertion/removal schedules are in the **PDF/SI**.

## Limitations

**ReaxFF** omits **explicit voltage / electrochemical double-layer** physics; **SEI** chemistry and long **cycle-life** degradation modes are outside the modeled setup.

## Reader notes (navigation)

Operators updating **`paper_keywords`** should preserve overlap with **`batteries-interfaces`** and **`reaxff-parameterization`** facets—this paper is a common bridge between **interface chemistry** and **mechanics** pages.

## Relevance to group

Canonical **ReaxFF** **battery anode** example with explicit **Li–Si parameterization** narrative.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
