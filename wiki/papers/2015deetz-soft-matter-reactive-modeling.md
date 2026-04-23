---
id: paper:2015deetz-soft-matter-reactive-modeling
type: paper
title: "Reactive modeling of the initial stages of alkoxysilane polycondensation: effects of precursor molecule structure and solution composition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:silica-silicate
source_refs: []
doi: "10.1039/C5SM00964B"
year: 2015
authors:
  - "Joshua D. Deetz"
  - "Roland Faller"
venue: "Soft Matter"
pdf_sha256: "1dc51eb4e2baf843a43421decca683a1ea8cadbe8d38cd37257d785cdcc4b555"
pdf_path: "papers/ReaxFF_others/Deetz_SoftMatter_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015deetz-soft-matter-reactive-modeling -->

## Summary

Sol–gel chemistry links molecular alkoxysilane precursors to oxide networks through hydrolysis and condensation steps that are difficult to observe directly at experimental time scales. This Soft Matter article uses **ReaxFF reactive molecular dynamics** in **LAMMPS** within the **NVT** ensemble to study early-stage **polycondensation** in **methanol/water** mixtures for several precursors—**tetramethoxysilane**, **trimethoxysilane**, **methyltrimethoxysilane**, and **tetraethoxysilane**. The work isolates how **precursor sterics** and **solution composition** steer hydrolysis versus condensation rates and how clusters grow by **monomer addition** versus **cluster–cluster** aggregation. Faller’s group connects the simulations to parameterization practice for silica-forming systems relevant to coatings, gels, and interfacial oxide films. Industrial sol–gels often use acid or base catalysts not fully explicit in every simulation snapshot; the paper’s neutral-pH-like compositions represent one controlled limit.

## Methods

### MD application (atomistic dynamics)

**LAMMPS** (**velocity-Verlet**) runs **NVT** sol–gel cells at **2000 K** with a **Nosé–Hoover** thermostat (**50 fs** damping), **0.5 fs** timestep, and **H** masses scaled to **3 amu** (reported not to change the observed kinetics for the targeted chemistry). **ReaxFF** uses the authors’ **alkoxysilane-parameterized** field (Deetz & Faller, cited). **Packmol** packs **TMOS**, **TEOS**, **methyltrimethoxysilane**, **trimethoxysilane**, with **water/methanol** mixtures in volumes **59.9–140.9 nm³** (Table 1, Soft Matter **2015**, **11**, 6780–6789) under **3D PBC**; each production segment is **5 ns** (Methods IIa). **Si–H, Si–C, C–C, O–C, C–H** bonds are **harmonically restrained** to block **PDMS-like decomposition** so the study isolates **hydrolysis/condensation**; bond-order-based reaction detection follows Methods IIb. **Barostat, shear, shock, electric field:** **N/A —** not used. **Hydrostatic pressure control:** **N/A —** constant-volume **NVT** only (no reported **GPa**/**bar** stress protocol).

### Force-field training

**N/A —** treated as an **application** paper of a recently published **alkoxysilane ReaxFF** parameterization (training details are in the cited parameterization work, not re-derived here).

### Static QM / DFT

**N/A —** not run on-the-fly in the reported MD trajectories.

## Findings

**Siloxane** rings and oligomers **nucleate spontaneously**; clusters grow by **monomer addition** and **cluster–cluster** aggregation, with rates slowed by **bulky** substituents near Si. **Water/methanol/silane** composition shifts the balance between **hydrolysis** and **condensation**, changing early **clusterization** versus more dispersed oligomers (figures/tables in *Soft Matter*). The discussion compares sequences to prior **reactive MD** siloxane literature. All **rates** are conditional on the **2000 K** acceleration; **room-temperature** extrapolation and quantitative **barriers** should be read from the **PDF**, not this summary.

## Limitations

Simulations are at **2000 K** to access **ns** chemistry timescales; extrapolation to **room-temperature** kinetics requires caution. **Harmonic restraints** suppress side reactions (e.g., **PDMS decomposition**) that could matter in some experimental formulations.

## Relevance to group

Core ReaxFF application to silica sol–gel chemistry adjacent to oxide surface science in the van Duin ecosystem.

## Related topics

- [[reaxff-family]]
