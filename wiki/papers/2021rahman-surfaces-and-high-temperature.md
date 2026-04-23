---
id: paper:2021rahman-surfaces-and-high-temperature
type: paper
title: "High temperature oxidation of monolayer MoS2 and its effect on mechanical properties: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:reaxff
  - material:tmd
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.surfin.2021.101371"
year: 2021
authors:
  - "Md. Habibur Rahman"
  - "Emdadul Haque Chowdhury"
  - "Sungwook Hong"
venue: "Surfaces and Interfaces 26 (2021) 101371"
pdf_sha256: "2569524f084093569cf120be2b5f88e842fddb211a1e5e74535b871fe4e67b69"
pdf_path: "papers/ReaxFF_others/Rahman_Hong_Surf_Int_2021_MoS2_oxidation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021rahman-surfaces-and-high-temperature -->

!!! abstract "Scope"
    **ReaxFF reactive MD** of **basal-plane oxidation** of monolayer MoS\(_2\) at **1400–1800 K**, followed by **tensile** tests comparing pristine versus oxidized structures; reports **2H→1T** transitions under load.

## Summary

Reactive molecular dynamics with ReaxFF is used to follow high-temperature oxidation of monolayer MoS\(_2\) on the basal plane and to quantify consequences for mechanical response. Simulations explore oxidation kinetics at 1400 K, 1500 K, and 1800 K with O\(_2\) present, finding facile reaction above about 1500 K beginning with O\(_2\) adsorption atop sulfur and progressing toward an oxy-sulfide MoS\(_{2-x}\)O\(_x\) solid solution. Uniaxial tensile simulations show degradation of fracture strength, fracture strain, Young’s modulus, and fracture toughness upon oxidation relative to pristine sheets. Both pristine and oxidized systems exhibit a transition from trigonal prismatic 2H-MoS\(_2\) to a distorted octahedral 1T-like metallic phase during the mechanical tests reported. Fracture pathways are analyzed from atomic trajectories. Oxidation converts sulfide to oxy-sulfide phases that weaken the basal plane—relevant to flexible electronics and tribological coatings exposed to air; stress-induced 2H→1T-like transitions couple chemistry to mechanical phase behavior in the simulated monolayers. For authoritative numbers, use the version-of-record PDF and Supporting Information.
## Methods

**1 — MD application (ReaxFF RMD).** **Reactive molecular dynamics** is performed in **LAMMPS** with the Mo–S–O **ReaxFF** parameter set referenced in *Surfaces and Interfaces* for monolayer MoS\(_2\) **oxidation** and follow-on **mechanics**. The in-plane **supercell** contains **O\(_2\)** above the **basal** surface; **PBC** apply in the periodic cell. **NVT** trajectories with a **thermostat** (details and **timestep** in **fs** in the article) run **equilibration** and **production** stages whose lengths are given in **ps**/**ns**; **temperature** is held at **1400 K**, **1500 K**, and **1800 K** to study **oxidation** kinetics. **Barostat / pressure control:** **N/A —** not the focus of the excerpted NVT oxidation protocol; **N/A — external electric field**; **N/A — umbrella** / **metadynamics** / **replica** **enhanced sampling** in the reported work. Uniaxial **tensile** tests on **pristine** versus **oxidized** structures use the same code base; authors report **fracture** strength, **strain** at failure, **Young’s modulus**, and **fracture** toughness, and track **2H** vs **1T**-like **distortions** along **atomic** trajectories.

**2 — Force-field training.** **N/A —** the study applies a published ReaxFF description to MoS\(_2\) + O\(_2\); it is not a new ReaxFF parameterization paper.

**3 — Static QM.** **N/A —** not used as the main engine; **oxidation** and **mechanics** are ReaxFF-based.

**4 — Experiments.** **N/A —** computation-only in the work summarized here.
## Findings

- Oxidation initiates via O\(_2\) adsorption on sulfur and advances to oxy-sulfide formation; reactivity increases strongly above ~1500 K in the simulations described.
- Oxidation reduces multiple tensile and fracture metrics relative to pristine monolayer MoS\(_2\).
- Stress-driven 2H→1T transitions appear for both pristine and oxidized samples in the reported tests.
- Atomic-scale fracture sequences are documented for comparison between oxidized and unoxidized cases.

**Comparisons & sensitivity.** Oxidized films are **compared** to **pristine** monolayers on multiple mechanical metrics. **Oxidation** reactivity and mechanical degradation depend strongly on **temperature** in the 1400–**1800 K** window studied.

**Limitations (corpus).** The abstract-level summary here does not restate every numerical control; confirm **timestep**, **O\(_2\)** **coverage**, and run lengths in the **PDF**/**SI** when citing protocols.

## Limitations

High-temperature, idealized monolayer setups omit full environmental complexity (e.g., humidity, defects other than those formed during oxidation in the model).

## Relevance to group

Application-focused ReaxFF study for TMD oxidation and mechanics under extreme thermal conditions.

## Citations and evidence anchors

- DOI: [10.1016/j.surfin.2021.101371](https://doi.org/10.1016/j.surfin.2021.101371)

## Related topics

- [[reaxff-family]]
