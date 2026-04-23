---
id: paper:2024mahdi-khajeh-talkhon-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF Reactive Force Field for Pt/Cl Systems with Application to Platinum Metal Etching with Chlorine and Hydrogen Chloride Gases"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - material:metal-surface
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.4c01708"
year: 2024
authors:
  - "Mahdi Khajeh Talkhoncheh"
  - "Yun Kyung Shin"
  - "Junseok Kim"
  - "Omid Jahanmahin"
  - "Kristen Fichthorn"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A 2024, 128, 8232–8243"
pdf_sha256: "d6f107d678b63ffbd96eb42b835fa28f6d31d1391b6564f0de896990d7a6c580"
pdf_path: "papers/Talkhoncheh_JPCA_PtCl_etching_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024mahdi-khajeh-talkhon-j-phys-chem-development-reaxff -->

## Summary

A **Pt/Cl/H ReaxFF** parameter set is **trained** on **VASP** **GGA-PBE** data for **Pt** slabs, **Cl** and **HCl** adsorption on **Pt(100)** and **Pt(111)**, **PtCl\(_2\)** crystal equations of state, and **Cl** diffusion barriers (**CI-NEB**), then coupled to existing **Pt/O/H** and **Cl/O/H** ReaxFF libraries. **LAMMPS** **NVT** simulations at **1500 K** (**Berendsen** thermostat, **0.25 fs** timestep) study **Cl\(_2\)** and **HCl** attack on **Pt(100)** and **Pt(111)** slabs and on a **cuboctahedral** **Pt** nanoparticle, comparing **chlorination**, **etching**, and **relative etchant** behavior to experiment.

## Methods

- **DFT training data:** **VASP** **PAW** **GGA-PBE**; **450 eV** cutoff; **(14×14×14)** **k** mesh for bulk **Pt**; **Pt** slabs **6** layers with relaxation of top **3** layers + adsorbates; **dipole correction**; adsorption energies from the article’s formula; **CI-NEB** (**3 images**) with **5.0 eV/Å\(^2\)** spring and **0.05 eV/Å** force criterion; **k** meshes per coverage in **Table S1** (Supporting Information).
- **ReaxFF optimization:** Successive **one-parameter search** minimizing weighted **QM vs ReaxFF** errors for **Pt–Cl** bonded/off-diagonal/angle/dihedral terms combined with **Pt/O/H** and **Cl/O/H** sets as described in **§3.1**.
- **MD:** Slab box **110 × 110 × 256 Å**; **9600 Pt** per slab with **4500 Cl\(_2\)** or **6000 HCl** molecules initially; **cuboctahedron** **~586 Pt** NP in **65–78 Å** cubic boxes with **765–1020** etchant molecules; **NVT**, **1500 K**, **100 fs** **Berendsen** damping; **2 ns** slabs / **1 ns** NP; **0.25 fs** timestep.

**Analysis outputs tied to etching chemistry.** Trajectories monitor **surface** **chloride** coverage, **volatile** **Pt\(_x\)Cl\(_y\)** **evaporation** events, and **facet-resolved** **metal** **loss** curves used to compare **Cl\(_2\)** versus **HCl** **efficiency**. **RDF** and **coordination** metrics (as plotted in the article) connect **subsurface** **Cl** penetration depths to **passivation** differences between **(100)** and **(111)** **terraces**.

**1 — Application MD.** **LAMMPS** **ReaxFF**; **NVT** **1500 K**; **0.25 fs** timestep; **Berendsen** thermostat ( **100 fs** **damping** as stated in summary); **2 ns** (slabs) / **1 ns** (NP) production; **~9600 Pt** slabs, **cuboctahedral** NPs, **PBC** boxes. **NPT** /**barostat**: **N/A**. **E-field, umbrella, MTD**: **N/A** in the summarized work. **2 — ReaxFF / Pt–Cl training (DFT, §3.1)** in the first bullets. **3 — DFT** used for training data, not a standalone PES survey paper.
## Findings

- The fitted field reproduces key **QM** trends for **bulk Pt**, **PtCl\(_2\)** phases, **surface Cl/H** configurations, and **diffusion** barriers well enough for the subsequent MD survey (figures/tables in the article and SI).
- **Pt(100)** shows **higher** susceptibility to **chlorination** and **Pt** removal than **Pt(111)**, which remains more **passivated** against **Cl** penetration, slowing formation of volatile **Pt\(_x\)Cl\(_y\)** species.
- **HCl** vs **Cl\(_2\)** **etching ratios** from simulation align **satisfactorily** with **experimental** references cited in the paper, supporting use of the model for **atomistic** **Pt** **halogen etching** scenarios. **Facet and etchant** comparisons and **RDF**-based **subsurface Cl** **diffusion** narratives are the main **sensitivity** levers discussed; **T** is fixed at **1500 K** in the long runs summarized. **J. Phys. Chem. A** **PDF** is authoritative.
## Limitations

**1500 K** aggressive etching conditions accelerate chemistry; transferability to industrial **ALE**-like conditions and **alloy**/contaminated **Pt** surfaces is not established in the main text. If this note and the PDF disagree on numerical detail, treat the peer-reviewed article as authoritative.

## Relevance to group

**van Duin-group** **ReaxFF** parametrization for **transition-metal halogen** chemistry with **Shin** / **Fichthorn** collaboration.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.4c01708](https://doi.org/10.1021/acs.jpca.4c01708)

## Related topics

- [[reaxff-family]]
