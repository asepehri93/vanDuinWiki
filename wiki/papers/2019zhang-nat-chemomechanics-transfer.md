---
id: paper:2019zhang-nat-chemomechanics-transfer
type: paper
title: "Chemomechanics of transfer printing of thin films in a liquid environment"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:continuum-or-mesoscale
  - method:reaxff
  - task:method-development
  - scale:multiscale
paper_keywords:
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.ijsolstr.2019.07.011"
year: 2019
authors:
  - "Zhang, Yue"
  - "Kim, Bongjoong"
  - "Gao, Yuan"
  - "Wie, Dae Seung"
  - "Lee, Chi Hwan"
  - "Xu, Baoxing"
venue: "Int. J. Solids Struct."
pdf_sha256: "514086098cb216d53fec2d99fedc706395357ba06e05b292ae7a371802f9198c"
pdf_path: "papers/ReaxFF_others/ReaxFF_NiSiO_Chemomechanics of transfer printing of thin films in a liquid environment.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019zhang-nat-chemomechanics-transfer -->


!!! abstract "Scope"

Chemomechanical theory and finite-element modeling of thin-film peeling from SiO₂/Si in liquid water, with reactive atomistic–continuum simulation and complementary peeling experiments in air versus water.

## Summary

Liquid-assisted transfer printing detaches thin films by coupling mechanical loading with interfacial chemistry in aqueous environments. The paper develops an interface-energy-release framework that incorporates rate-dependent chemical reaction kinetics at the solid–liquid interface, then links those interface laws to mechanical peeling through peeling rate, angle, and film-thickness dependent steady-state forces. A finite-element implementation informed by atomistic detail and a reactive atomistic–continuum multiscale approach simulate film detachment at continuum resolution, while bench peeling experiments compare separation layers on wafers in dry air and water. The manuscript therefore emphasizes peel-rate and environment coupling rather than a catalog of static interface energies alone.

## Methods

### Continuum chemomechanical peeling framework (D + mechanics)

**Energy release rate** for thin-film detachment is augmented by **kinetic** terms for **liquid** reactions at **interfacial bonds** → **rate-dependent** debonding, coupled to **elastic** film deformation under varied **peel** kinematics (**angle**, **rate**, **thickness** dependence as in **Int. J. Solids Struct.**).

### Finite-element implementation (B, continuum)

**FE** solves **mechanical** peeling with **interface** laws informed by **atomistic** inputs (parameters not invented here—see paper).

### Reactive atomistic–continuum coupling

A **reactive atomistic–continuum multiscale** route supplies **interface** parameters / **reaction** kinetics feeding the **continuum** peel model.

### Experiments

**Peeling** tests on **three** separation-layer **stacks** comparing **air** vs **water**; quantitative comparison to **theory**/**simulation**.

**Reactive atomistic block (informed by ReaxFF, not a standalone LAMMPS production case study).** **Molecular** **dynamics** with **ReaxFF**-informed **kinetics** **feeds** a **reactive** **atomistic–continuum** **stack**; **N/A** on this page for **exact** **timestep** (**fs**), **NVT** **production** **duration** (**ps**), **Nose–Hoover** **thermostat** **damping**, and **room-temperature** **K** **targets**—see *Int. J. Solids Struct.* **Interface** **MD** uses **PBC** **in-plane** on **wafer**-like **adhesion** **stacks** as **described** there. **Barostat:** **N/A** on this summary page for the **MD** **substrate** unless the article reports **NPT** **slab** **relaxation**. **Electric field:** **N/A** — not part of the stated **peel** **protocol** in the abstract-level summary. **Metadynamics / umbrella / replica:** **N/A** unless the article states otherwise.

## Findings

### Mechanisms and regime maps

**Theory**, **multiscale** models, and **experiment** agree on **steady-state** peel forces—supporting **kinetic** **chemical** coupling beyond static **adhesion**. **Interfacial delamination** vs **bulk** **deformation** competition is explicit; a **phase-style** diagram guides **nanomembrane** **transfer**. **Capillary** vs **reaction** driving forces partition by **wettability** and stack.

### Limitations / future calibration

Parameters are **system-specific**; new **adhesives**, **chemistries**, or **solvents** need **recalibration**.

## Limitations

Model parameters are system-specific; extending quantitative predictions to new adhesives, surface chemistries, or non-aqueous liquids requires recalibration and additional validation. The paper’s **multiscale** coupling also means retrieval should preserve the split between **continuum peeling mechanics**, **interface kinetic** laws, and **atomistic** inputs used to inform those laws—none of the three alone is “the full method.”

## Relevance to group

Demonstrates multiscale coupling between ReaxFF-informed chemistry and continuum fracture/peeling mechanics relevant to microfabrication and interface engineering problems. The **Int. J. Solids Struct.** framing is useful for retrieval queries that mix **interface kinetics**, **peeling**, and **wafer transfer** keywords.

## Citations and evidence anchors

- https://doi.org/10.1016/j.ijsolstr.2019.07.011

## Related topics

- [[reaxff-family]]
