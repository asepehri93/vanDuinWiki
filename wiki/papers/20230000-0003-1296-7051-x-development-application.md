---
id: paper:20230000-0003-1296-7051-x-development-application
type: paper
title: "Development and Application of a ReaxFF Reactive Force Field for Ni-Doped MoS2"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - material:tmd
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c00668"
year: 2023
authors:
  - "Karen Mohammadtabar"
  - "Enrique Guerrero"
  - "Sergio Romero Garcia"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "David A. Strubbe"
  - "Ashlie Martini"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "f812908102d725a4d9b9a059b8a83b6f37f7af4fd8e727734cbbfcbd02e2fed3"
pdf_path: "papers/Mohammadtabar_JPCC_NiMoS2_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20230000-0003-1296-7051-x-development-application -->

## Summary

Doping molybdenum disulfide with nickel modulates catalytic and tribological response, but transferable classical models that capture both structural polymorphism and chemistry are scarce. Mohammadtabar et al. parameterize a ReaxFF description for Ni-doped MoS₂ using a broad density functional theory training set covering substitutional and intercalated Ni sites under multiple strain modes. The field is validated against DFT structural and energetic metrics for 2H monolayers, relative stabilities of competing sites, and vacancy-bearing configurations, then applied to reactive simulations of sputtering deposition and annealing that probe amorphous-to-crystalline evolution in doped films. The motivation ties to tribological films where nickel is introduced during synthesis or wear. The combination of strain-rich training data and processing simulations distinguishes this work from static lattice-only parameterizations.

## Methods

### DFT training corpus (C)

- **Structures:** **2H-MoS\(_2\)** with **Ni** at **Mo** and **S** **substitutional** sites and at **octahedral** / **tetrahedral** **intercalation** sites.
- **Deformation sampling:** **Uniaxial**, **biaxial**, **triaxial**, and **shear** **strain** paths on selected configurations.
- **QM details:** **Functional**, **basis**, **k-mesh**, and **convergence** settings appear in *J. Phys. Chem. C* **DOI** `10.1021/acs.jpcc.3c00668`.

### ReaxFF optimization targets (A)

- **Fits** reproduce **relaxed structures**, **site-energy ordering** (e.g. **tetrahedral** vs **octahedral** Ni), **1H vs 1T** **relative energies**, and selected **defected** configurations within tolerances quoted in the paper.

### Reactive MD applications (B)

- **Deposition / annealing:** **Sputtering**-like impact simulations followed by **thermal annealing** to study **amorphous→crystalline** conversion in **Ni-doped** films.
- **Numerics in the VOR/SI:** **Timestep**, **thermostat**, **impact** **energy** / **flux** for **sputter**-like **events**, and **annealing** **schedules** for the **a-C → crystal** post-processing; **hash**-linked **galley** here may differ in **pagination** from **VOR**.

### MD application (sputter + anneal on Ni-doped film)

**Engine / code:** **LAMMPS** with the **new Ni–MoS\(_2\)** **ReaxFF**. **Deposition/impact** and **NVT**-type **(or as stated) anneal** in **3D** **PBC** **TMD** **supercells**; **T**, **kinetic** **energy** of **arrivals**, and **duration** in **JPCC**. **N/A** — not an **open**-circuit **electrolyte** or **SCCM** **reactive** **flow** **RMD** as summarized; **N/A** — no **NPT** **barostat** unless the **VOR** specifies **NPT** for **deposition** **stress**; **N/A** — no **replica**/**metadynamics**; **Coulomb** and **QEq** **in** the **VOR**/**SI**. **N/A** — no **shock** **Hugoniot** **NEMD**; **N/A** — no **static external electric** **field** in the **RMD** protocol summarized on this page.

## Findings

### Validation

The fitted **ReaxFF** matches the **DFT** validation suite for **Ni-doped MoS\(_2\)** within the authors’ stated **error** bounds. The abstract lists explicit checks: **ReaxFF vs DFT** relaxed **structural parameters**, the **tetrahedral/octahedral** site **energy gap** in doped **2H**, **1H** vs **1T** monolayer **energies**, and **vacancy-bearing** doped **2H** structures.

### Processing simulations

**Sputter + anneal** trajectories capture **amorphous-to-crystalline** pathways accessible with the new field, supporting **deposition** / **tribology**-oriented modeling of **doped** **TMD** films.

### Scope and extensions

**Gas-phase / solid** training shown in the paper does not automatically validate **electrochemical** or **solvated** environments without additional benchmarks. Porting to **other dopants** should repeat **site preference** and **polymorph** **DFT** checks before trusting **extrapolated** chemistry.

## Limitations

Training chemistry focuses on Ni doping sites and strain windows listed in the paper; electrochemical or strongly oxidizing environments require separate validation.

## Relevance to group

Group-authored ReaxFF for TMD doping with applications in tribology and catalysis modeling contexts.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.3c00668](https://doi.org/10.1021/acs.jpcc.3c00668)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
