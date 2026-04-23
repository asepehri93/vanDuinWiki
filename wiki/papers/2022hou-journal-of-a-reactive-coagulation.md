---
id: paper:2022hou-journal-of-a-reactive-coagulation
type: paper
title: "On the reactive coagulation of incipient soot nanoparticles"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:reactive-md
  - keyword:lammps
source_refs: []
doi: "10.1016/j.jaerosci.2021.105866"
year: 2022
authors:
  - "Dingyu Hou"
  - "Laura Pascazio"
  - "Jacob Martin"
  - "Yuxin Zhou"
  - "Markus Kraft"
  - "Xiaoqing You"
venue: "J. Aerosol Sci."
pdf_sha256: "b4622fcbd8633289b9b8f2186b2c8b1158d8f0cc283dee27fa031adf3289cfd5"
pdf_path: "papers/ReaxFF_others/Hou_Kraft_J_AerosolSci_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022hou-journal-of-a-reactive-coagulation -->

## Summary

Hou *et al.* use **ReaxFF-based reactive molecular dynamics** to study **head-on coagulation** of two **~2 nm** **PAH-rich** soot precursor clusters at **1500–2000 K**, a temperature window relevant to **soot inception** in flames. The authors compute **coagulation efficiency** \(\eta\) by tracking **center-of-mass separation**, **interaction potential energy**, and **kinetic energy** across many trajectories, asking whether **reactive** **C–C** bridging materially increases sticking compared with purely **physical** coagulation. They further introduce **surface σ-radical** fractions between **0.01** and **0.1** to mimic partially radicalized **soot** surfaces and quantify the incremental effect on \(\eta\). The framing connects **atomistic** outcomes to **population-balance** models that require **collision efficiencies** as inputs, warning against assuming \(\eta \approx 1\) in hot zones without microscopic justification.

## Methods

### A — Reactive force field

- **ReaxFF** parametrization for **hydrocarbon** / **soot-precursor** chemistry (PAH-rich clusters) as specified in *J. Aerosol Sci.*.

### B — Reactive MD (head-on coagulation)

- **Engine / code:** **LAMMPS** with **ReaxFF** (`pair reax/c` family per standard practice; input details in article).
- **System:** Two **~2 nm** **PAH-rich** **incipient soot** clusters in **head-on** collision geometry.
- **Thermodynamic conditions:** **1500–2000 K**; many independent trajectories (**hundreds**) for statistics.
- **Radical treatment:** Surface **σ-radical** fraction varied between **0.01** and **0.1** to mimic partially radicalized surfaces.
- **Metrics:** Center-of-mass separation, interaction **potential** energy, and **kinetic** energy vs time; **coagulation efficiency** \(\eta\) defined as in the paper (aerosol coagulation conventions).
- **Not stated in wiki summary:** Timestep, thermostat, initial relative velocity—confirm in PDF.

### C — Quantum chemistry

- None for production runs; ReaxFF is the reactive model.

### D — Experiments

- None; outcomes inform **population-balance** **collision efficiency** inputs for soot models.

**Atomistic protocol (see *J. Aerosol Sci.* **PDF** for values):** **LAMMPS** **ReaxFF**; **two** **~2 nm** **PAH** **clusters** in **head-on** **collision** **geometry** with **3D** **PBC**; **NVT** at **1500–2000 K**; **fs** **timestep** and **thermostat** per **Methods**; **many** **short** **trajectories** (**hundreds**) totaling **ps**–**ns** **sampling**; **barostat** **N/A**; **hydrostatic** **pressure** **N/A**; **external** **electric** **field** **N/A**; **replica** **exchange** / **metadynamics** **N/A**.

## Findings

\(\eta\) **decreases** as **temperature** increases, primarily because higher \(T\) raises **atomic kinetic energy** inside clusters and promotes **rebound** rather than **capture**. Introducing **σ-radicals** enables some **covalent bridging** between clusters, yielding only a **moderate** relative increase in \(\eta\) (about **~10%** in the scanned range) compared with the **non-radical** baseline. The authors conclude that **reactive coagulation** does not restore **high** sticking efficiencies for **incipient soot** under these **hot** conditions, implying that **population-balance** simulations should not casually set \(\eta\) to unity in **high-T** regions.


## Limitations

Idealized **cluster** sizes and **radical** fractions; linking to **full** **soot** **PSD** evolution still requires **mesoscale** models. **Population-balance** models should import \(\eta\) as a **conditional** parameter that may vary with **local** **temperature** and **radical** pool assumptions.

## Reader notes (navigation)

This article intersects **combustion** theme hubs and **soot**-focused retrieval; keep **`paper_keywords`** aligned with **`fuel-combustion`** and **`reactive-md`** to reduce accidental routing to unrelated **carbon** allotrope pages.

## Relevance to group

Bridges **ReaxFF** atomistics to **aerosol coagulation efficiency** parameters for **soot inception** modeling.

## Citations and evidence anchors

- DOI: [10.1016/j.jaerosci.2021.105866](https://doi.org/10.1016/j.jaerosci.2021.105866)

## Related topics

- [[reaxff-family]]
