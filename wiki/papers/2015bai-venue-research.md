---
id: paper:2015bai-venue-research
type: paper
title: "Bombarding Graphene with Oxygen Ions: Combining Effects of Incident Angle and Ion Energy To Control Defect Generation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:nvt-simulation
  - keyword:nve-simulation
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b09620"
year: 2015
authors:
  - "Zhitong Bai"
  - "Lin Zhang"
  - "Ling Liu"
venue: "J. Phys. Chem. C"
pdf_sha256: "7b81baea18e27e03663e83415101dadfe07cf54ad3a5f2d71aa9ff783b1ff5a3"
pdf_path: "papers/ReaxFF_others/Bai_JPCC_O_Graphene_collision.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015bai-venue-research -->

## Summary

Ion bombardment is a standard lever for **defect engineering** and **heteroatom doping** of **graphene**, with outcomes that depend on **projectile energy**, **impact site**, and **incidence angle**. This **J. Phys. Chem. C** study applies **LAMMPS** with **ReaxFF** to **oxygen-ion** impacts, sweeping kinetic energy and incidence angle while classifying **substitution**, **vacancy**, and **disorder** products—motivated by **implantation** for electronic tuning and by **irradiation damage** where unintended defects degrade mechanics. The authors report that **oblique** incidence can bias outcomes toward **substitution-rich** versus **damage-rich** regimes, giving qualitative guidance for ion processing.

## Methods

**Force-field training.** **N/A —** the study applies a published **C/O ReaxFF** description suitable for oxygen impact on graphene (cited in the article) without reporting a new parameterization.

**MD application (LAMMPS + ReaxFF bombardment).** **Engine:** **LAMMPS** (large-scale atomic/molecular massively parallel simulator) as stated in `papers/ReaxFF_others/Bai_JPCC_O_Graphene_collision.pdf`. **System:** monolayer graphene models with supercell sizes tabulated in the article. **Boundaries:** **3D periodic** graphene cells (in-plane periodicity with finite vacuum normal as defined in the manuscript). **Stages:** **NVT** equilibration at **300 K** for **10 ps** with **0.1 fs** timesteps; **NVE** impact segments use **0.01 fs** timesteps to resolve collisional energy transfer; post-impact **NVT** relaxation runs **10 ps** at **300 K**. **Thermostat:** **N/A —** the recovered Methods paragraph specifies **NVT** temperature control but does not name the **thermostat** algorithm or damping constants; read the full PDF/SI for those details. **Projectile conditions:** oxygen ions span **1.33–1008 eV** kinetic energy with incidence angles including **70°–90°** and **30°–50°** relative to the surface normal. **Pressure control:** **N/A —** bombardment stages use **NVE**/**NVT** cells without documented hydrostatic **pressure** targeting beyond constant-volume control. **Replica / electric bias:** **N/A —** not part of the reported bombardment protocol.

## Findings

Larger incidence angles (**70°–90°**) favor **substitution** and **single vacancies**, whereas smaller angles (**30°–50°**) favor **double and multiple vacancies** and **in-plane disorder** in the simulations summarized by the authors. **70°** incidence yields the **highest probability of oxygen substitution** in their parameter sweep. For “doping quality” defined by substitution relative to collateral damage, **ions near 40–60 eV** at **70°** maximize substitution-focused outcomes with comparatively minimal competing defects in the classification used. These trends are presented as **computational** guidance for ion implantation and irradiation interpretations, subject to ReaxFF limitations at very high energies where electronic stopping and channeling effects may depart from the classical reactive model.

## Limitations

Reactive MD cannot capture full **electronic stopping** physics at all energies; very high-energy regimes may require complementary **binary collision** or **DFT** benchmarks.

## Relevance to group

**ReaxFF application** to **graphene** defect engineering under **oxygen** ion impact, adjacent to broader **nanocarbon** simulation threads.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.5b09620](https://doi.org/10.1021/acs.jpcc.5b09620)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
