---
id: paper:2015dri-computationa-evaluation-reactive
type: paper
title: "Evaluation of reactive force fields for prediction of the thermo-mechanical properties of cellulose Iβ"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - method:classical-md
  - material:polymer-organic
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:classical-ff
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2015.06.040"
year: 2015
authors:
  - "Fernando L. Dri"
  - "Xiawa Wu"
  - "Robert J. Moon"
  - "Ashlie Martini"
  - "Pablo D. Zavattieri"
venue: "Computational Materials Science"
pdf_sha256: "3aa544b6c0b657b42a76b2f5967cea992b648a770be6cfe27d9320864e7cb3b5"
pdf_path: "papers/ReaxFF_others/Dri_cellulose_CompMatSci_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015dri-computationa-evaluation-reactive -->

## Summary

**Crystalline cellulose Iβ** is a foundational biopolymer structure for materials science, yet predicting its **thermo-mechanical** response depends critically on the **force field** chosen. This **Computational Materials Science** article benchmarks **three ReaxFF parameter sets** (**Mattsson**, **Chenoweth**, and **Rahaman** branches as labeled in the paper) against **COMPASS** (Class II) and **GLYCAM** (Class I) models for **lattice parameters**, **elastic constants**, **thermal expansion**, and **elastic anisotropy**, referencing **DFT** and **experimental** data compiled in the manuscript. The central result is negative in a useful sense: **no** tested model is uniformly accurate across all targets, but the paper provides **which** model is least inaccurate for each property—guidance for practitioners deciding whether reactive fidelity is worth the cost.

## Methods

### MD application (atomistic dynamics)

- **Model construction:** **cellulose Iβ** supercells are built starting from the **Nishiyama** “network A” coordinates using **Materials Studio** (and the **NanoHUB** crystalline-cellulose toolkit cited in the paper).
- **Boundary conditions:** **3D periodic boundary conditions (PBC)** are used for the crystalline **cellulose** **supercells** in all **MD** stages described.
- **Engine / code:** **LAMMPS** is used for MD sampling of **mechanical** and **thermal** properties for **three ReaxFF parameterizations** (Mattsson / Chenoweth / Rahaman branches as labeled) and for comparison against **COMPASS** and **GLYCAM** classical models.
- **Equilibration protocol:** a two-step relaxation is used: **canonical (NVT)** equilibration followed by **isothermal–isobaric (NPT)** equilibration (**300 ps** total in the second stage excerpted in Methods) with **0.25 fs** timestep, targeting **1 atm** pressure for relaxed lattice constants.
- **Elastic constants:** after NPT equilibration, **uniaxial strain increments (~0.2%)** are applied along directions **1–3** and **shear directions 12/13/23** with other cell parameters constrained as described; each strained state is **energy-minimized (conjugate gradient)** to extract stresses for the stiffness matrix (**mechanical stiffness prediction is minimization-based**, not finite-temperature dynamical sampling).
- **Thermal expansion:** lattice constants are sampled from **200 K to 500 K** in **20 K** steps at **1 atm**, repeating the **NVT → NPT** equilibration windows (**50 ps + 300 ps** as stated for the expansion workflow excerpt).
- **Thermostat naming detail:** **N/A —** the main text excerpted here emphasizes **NVT/NPT** stages and **timestep** settings more than a specific **Berendsen**/**Nose–Hoover** thermostat brand string—confirm thermostat implementation details in **papers/ReaxFF_others/Dri_cellulose_CompMatSci_2015.pdf** if required for reproduction.
- **Replica / shock / electric field:** **N/A —** not used.

### Force-field training

**N/A —** this is a **benchmarking** study of existing parameterizations, not a new ReaxFF fit.

### Static QM / DFT

**N/A —** DFT values appear as **literature / tabulated references** for comparison rather than as newly computed QM in this paper (see article tables and citations).

## Findings

**No** tested field is uniformly accurate for **lattice parameters**, **elastic constants**, **thermal expansion**, and **anisotropy** at once; the manuscript argues **property-by-property** choice instead of a single “best” score. A model can match some **elastic** components yet fail **expansion** along an axis, so **task-specific** selection matters even before deciding if **reactive** chemistry is needed. Tables compare **ReaxFF** variants and classical fields to compiled **DFT** and **experimental** references; errors shift with **temperature**, **strain** direction, and observable. Use the **PDF** tables for quantitative winners—this page is not a substitute.

## Limitations

The reactive ReaxFF sets were **not** originally trained for **crystalline cellulose**; errors reflect **transferability limits** of each training lineage more than a blanket statement about reactive MD overall.

## Reader notes (MAS / retrieval)

Point users here for **force-field benchmarking** language (“no universal winner”) before they adopt a **ReaxFF** cellulose model for pyrolysis studies that assume accurate crystal mechanics.

Cross-check the manuscript’s **tables** for property-by-property winners.

## Relevance to group

Clear **validation** framing for **ReaxFF** on **biopolymer** crystals—useful when weighing **reactive** chemistry versus **fixed-bond** carbohydrate force fields in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2015.06.040](https://doi.org/10.1016/j.commatsci.2015.06.040)

## Related topics

- [[reaxff-family]]
