---
id: paper:2020shi-physical-che-anomalous-proton
type: paper
title: "Anomalous proton conduction behavior across a nanoporous two-dimensional conjugated aromatic polymer membrane"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1039/c9cp06372b"
year: 2020
authors:
  - "Le Shi"
venue: "Phys. Chem. Chem. Phys., 2020, 22, 2978–2985"
pdf_sha256: "85d5f08feac1b8328f916890705a2c032115f1b6525bf97cdb585e78937034f9"
pdf_path: "papers/ReaxFF_others/LeShi_proton_graphene_oxide_PCCP_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020shi-physical-che-anomalous-proton -->

Aqueous proton transport across a **nanoporous two-dimensional conjugated aromatic polymer (2D-CAP)** membrane is studied with **large-scale ReaxFF reactive molecular dynamics**. The computed barrier for proton penetration across 2D-CAP is **higher** than for a **graphtetrayne** reference despite **larger pores** in 2D-CAP, traced to **edge hydrogen** that stabilizes a local hydrogen-bond network with pore water and **slows water mobility**, impeding proton conduction.

## Summary

The work compares proton penetration energetics and mechanism for 2D-CAP versus graphtetrayne using ReaxFF-based reactive MD. The central result is an **anomalously high barrier** for 2D-CAP tied to **nanopore-edge chemistry** (hydrogen at the periphery) rather than pore size alone: those atoms participate in a **stable local H-bond network** with water in and near the pore, reducing water mobility and hindering proton transport. The study argues that **pore-edge decoration** must be considered alongside pore size when designing nanoporous 2D proton-selective membranes.

## Methods

- **Software / FF:** **LAMMPS** with the **CHON-2017_weak** **ReaxFF** parametrization; **time step 0.25 fs**; **Nose-Hoover chain** thermostat with **100 fs** (NVT) and **1000 fs** (NPT) temperature damping as stated in **Section 2.2**.
- **Ensembles:** **Metadynamics** runs for barrier sampling; additional **500 ps** **NVT** **300 K** checks of proton-position statistics; **2 ns NPT** (**P = 1 atm**, **T = 300 K**) with **x** and **y** fixed, then **2 ns NVT** **300 K** equilibration before **production NVT** analysis of 2D-CAP vs reference **G4** (graphtetrayne).
- **Analysis:** Unbiased **2 ns** **NVT** trajectories of proton-membrane distance (Figure 2); **metadynamics** for penetration barriers; water mobility and **H-bond** structure at **pore edges**.

**MD application (complementing the bullets).** **LAMMPS** + **CHON-2017_weak** **ReaxFF**; **0.25 fs** timesteps; **Nose–Hoover** chains (**100** **fs** coupling in **NVT**, **1000** **fs** in some **NPT** **stages** per **§2.2**); **2** **ns** **NPT** at **1** **atm** / **300** **K** with **lateral** **cell** **area** **fixed** then **2** **ns** **NVT** at **300** **K** before **production** **NVT** **2D-CAP** vs **G4** **(graphtetrayne)** **comparisons**. **Replica / umbrella: N/A —** **not** used; **metadynamics: yes** for **barrier** **sampling** of **proton** **permeation**. **Electric** **(static) field: N/A —** not used. **PBC** **3D** **condensed** **water**+**membrane** **supercells** (see **`pdf_path`** for **box** **dimensions** and **2D**-**CAP** **and** **pore** **H** **decoration**).


## Findings

- The **proton penetration barrier** for **2D-CAP** is about **twice** that for **graphtetrayne**, even though 2D-CAP has a **larger pore** in the comparison presented.
- The **high barrier** is attributed to **2D-CAP’s atomic nanopore structure**, specifically **hydrogen at the pore periphery** forming a **stable local hydrogen-bond network** with water inside or near the nanopores.
- **Water molecules** participating in that network show **reduced mobility**, which **impedes** the **proton transport** pathway through the pore.
- The authors conclude that **proton penetration across nanoporous 2D materials** depends on **pore size and pore-edge composition** (decorating atoms or functional groups); certain edge hydrogens can **further hamper** proton conductivity via localized H-bonding to water.

**Comparisons:** **2D-CAP** is contrasted with **G4 (graphtetrayne)**: higher barrier in **2D-CAP** **despite** a **larger** **pore** in the same comparison, tracing to **pore**-**edge** **H** **(see** **PCCP** **text**)**. **Sensitivity / parameters:** all **NVT** **/ NPT** **stages** reported **at** **300** **K** and **1** **atm** **(NPT)** in **the** **equilibration** **blocks** in **Section** **2.2**. **Limitations:** **ReaxFF**-only **barriers** and **H-bond** **patterns**; **uncertainty** vs **experiment** **/ DFT** **remains** **(see** **## Limitations**). **Corpus honesty:** this **ReaxFF_others** `pdf_path` is the **author** **VOR** **citable** **PDF** for **reproduction**; **definitive** **numbers** **from** **Table** **/** **figure** **captions** **in** that **file**, **not** **inferred** here.

## Limitations

Barrier heights and structural interpretations are **force-field–dependent**; quantitative agreement with experiment or DFT would require cross-checks beyond the ReaxFF study as reported.

## Relevance to group

Illustrates **ReaxFF** application to **2D nanoporous membranes** and **aqueous proton transport**, relevant to fuel-cell and flow-battery membrane design contexts cited in the introduction.

## Citations and evidence anchors

- DOI: `10.1039/c9cp06372b`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
