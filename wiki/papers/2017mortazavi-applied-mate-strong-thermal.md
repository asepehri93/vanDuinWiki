---
id: paper:2017mortazavi-applied-mate-strong-thermal
type: paper
title: "Strong thermal transport along polycrystalline transition metal dichalcogenides revealed by multiscale modeling for MoS₂"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:2d-materials
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.apmt.2017.02.005"
year: 2017
authors:
  - "Bohayra Mortazavi"
  - "Romain Quey"
  - "Alireza Ostadhossein"
  - "Aurelien Villani"
  - "Nicolas Moulin"
  - "Adri C. T. van Duin"
  - "Timon Rabczuk"
venue: "Appl. Mater. Today"
pdf_sha256: "06e09fe62b57e7cd4e1459d5b110d2c4ad7b5fbc4e9251d4ce2a8f61733a0e35"
pdf_path: "papers/Mortavazi_AMT_MoS2_thermal_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mortazavi-applied-mate-strong-thermal -->

!!! abstract
Same study as the proof ingest: ReaxFF NEMD thermal conductances for MoS₂ grain boundaries feed FE models of polycrystalline films; validates multiscale route against graphene/h-BN.

## Summary

Thermal management in two-dimensional transition metal dichalcogenides depends strongly on microstructure: grain boundaries and defects scatter phonons and reduce in-plane thermal conductivity relative to pristine single crystals. This *Applied Materials Today* article develops a multiscale workflow in which atomically resolved thermal conductances from nonequilibrium molecular dynamics (NEMD) with a ReaxFF parametrization for MoS₂ feed into finite-element continuum models of polycrystalline films reminiscent of chemical-vapor-deposited microstructures. The authors construct on the order of twenty representative grain-boundary configurations informed by microscopy and density-functional-theory literature, extract thermal boundary resistances or conductances as needed for continuum meshes, and then solve heat transport on statistically structured polycrystals. Cross-material benchmarking against graphene and hexagonal boron nitride polycrystals, including discussion of equilibrium versus nonequilibrium estimators for thermal conductivity, positions the MoS₂ results within a broader two-dimensional thermal-transport context. This wiki slug attaches to the version-of-record PDF filename `Mortavazi_AMT_MoS2_thermal_2017.pdf`; a parallel ingest slug **`[[2017mortavazi-venue-paper]]`** may exist for alternate corpus bytes of the same study.

## Methods

**Force-field training / fitting.** **ReaxFF** for **MoS₂** is used as published (prior mechanical validation cited in the article); this *Appl. Mater. Today* paper **does not** report a new QM refit of the reactive potential.

**MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** carries **nonequilibrium molecular dynamics (NEMD)** with the **ReaxFF** bond-order energy expression (bond/valence/torsion/over- and under-coordination/lone-pair terms plus **vdW** and **Coulomb** contributions, Eq. (1) in the paper). **System size & composition:** **Twenty** distinct **MoS₂** **grain-boundary** supercells (armchair/zigzag families with **4–4**, **4–8**, **5–7**, **4–6**, **6–8** cores, including symmetric and asymmetric variants where applicable) plus **pristine** **single-layer MoS₂** reference cells for bulk **κ** extraction—see Fig. 1 and accompanying text for the structural inventory. **Boundaries / periodicity:** **In-plane periodic** supercells along the **grain-boundary line** (as stated for the constructed GB models). **Timestep:** **Δt = 0.25 fs**. **Protocol / ensembles:** structures are first **equilibrated at room temperature (~300 K)**; **end atoms are fixed**, followed by additional **NVT** equilibration with a **Nose–Hoover thermostat**. For the **NEMD** production stage, the cell is partitioned into **22 slabs** along the transport direction: the **first** and **last** slabs are held at **310 K** and **290 K**, respectively (**ΔT = 20 K** between hot/cold slabs), using **NVT** control on those slabs, while the **interior 20 slabs** evolve in the **microcanonical (NVE)** ensemble to establish a **steady-state heat flux** \(J_x\) and a **linear temperature profile** in the pristine case (Fourier-law extraction, Eq. (2)). **Barostat / global hydrostatic pressure:** **N/A —** no Parrinello–Rahman **pressure** servo; **NVT** hot/cold reservoirs impose the **thermal** bias while interior slabs remain **NVE**. **Thermostat summary:** **Nose–Hoover** in **NVT** equilibration; **NVT** thermostats on hot/cold slabs during **NEMD** production. **Electric field:** **N/A —** not applied. **Replica / enhanced sampling:** **N/A —** direct **NEMD** rather than umbrella or replica-exchange methods. **Duration:** **N/A —** total trajectory lengths beyond the **steady-state** criterion are tied to prior protocols **[66]** and are not re-tabulated numerically on this wiki page—use the article/SI for exact run lengths.

**Static QM / DFT.** **Literature DFT/TEM** motivates **GB** geometries and defect topologies; **DFT** is **not** rerun here as the **κ** engine.

**Review / non-simulation framing.** **Finite-element (FE)** **continuum** models (2D tessellated polycrystals with **Neper**, **~10⁴** grains, **~60** triangular elements per grain on average) consume the **NEMD** **grain-boundary conductances** to predict **effective in-plane κ** vs **grain statistics**; additional **graphene** and **h-BN** multiscale benchmarks compare **NEMD+FE** against fully atomistic **EMD** references as described in the article. **Corpus note:** this slug uses the **version-of-record** PDF `Mortavazi_AMT_MoS2_thermal_2017.pdf`; **`[[2017mortavazi-venue-paper]]`** tracks an **uncorrected proof** duplicate of the same study.

## Findings

**Outcomes & mechanisms.** **Reactive NEMD** supplies **thermal conductance** values for **~20** representative **MoS₂** **grain boundaries** plus **pristine** **SL MoS₂**; inserting those conductances into **FE** meshes yields **effective in-plane thermal conductivity** maps for **polycrystalline** films. **Effective κ** drops sharply when **grain sizes** approach **~100 nm** and smaller because **boundary scattering** density increases.

**Comparisons.** The workflow is cross-checked on **polycrystalline graphene** and **h-BN**, comparing the **multiscale (NEMD+FE)** route to **fully atomistic EMD** effective conductivities as reported in the manuscript.

**Sensitivity & design levers.** **Broadened grain-size distributions** alter **intrafilm heat-flux** patterns relative to **uniform** microstructure approximations at comparable average grain sizes; **non-uniform** texture therefore matters for **thermal routing**.

**Limitations & outlook (as authored).** The model emphasizes **phonon-dominated** transport in the insulating regime and does not treat **electronic thermal conduction** or **hot carriers**; absolute **κ** values can depend on **NEMD vs EMD** estimators—follow the article’s method discussion.

**Corpus / KB honesty.** Numeric **κ** and **conductance** tables should be read from the **DOI-linked** article/PDF; this page summarizes the protocol narrative for navigation.


## Limitations

The model focuses on phonon-dominated thermal transport in the insulating regime and does not couple to electronic thermal conduction or hot-carrier effects. Absolute thermal conductivity numbers can differ between EMD and NEMD protocols; readers should follow the article’s discussion of method dependence rather than treating any single κ value as universal.

## Relevance to group

Adri C. T. van Duin appears among the coauthors; the work is a concrete example of ReaxFF-derived thermal properties feeding engineering-scale continuum predictions for two-dimensional materials.

## Citations and evidence anchors

- DOI: `10.1016/j.apmt.2017.02.005`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Proof duplicate: [[2017mortavazi-venue-paper]].
