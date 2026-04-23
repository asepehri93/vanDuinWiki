---
id: paper:2018hou-physical-che-reactive-force-field
type: paper
title: "Reactive force-field molecular dynamics study on graphene oxide reinforced cement composite: functional group de-protonation, interfacial bonding and strengthening mechanism"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:cement-mineral
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1039/c8cp00006a"
year: 2018
authors:
  - "Dongshuai Hou"
  - "Tiejun Yang"
  - "Jinhui Tang"
  - "Shaochun Li"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "f5cdefae0c0b1142e4476a1a0f6dac3462b6b3cdb67935ed45ef874c2b17b4d2"
pdf_path: "papers/ReaxFF_others/Hou_CaOH_graphene_PCCP_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018hou-physical-che-reactive-force-field -->

## Summary

**Graphene oxide (GO)** is widely explored as a **nanoscale reinforcement** in **cement** matrices, but atomistic mechanisms coupling **GO functional groups** to **calcium–silicate–hydrate (C–S–H)** gels remain under-characterized. This **PCCP** article uses **ReaxFF MD** via **LAMMPS** (`reax/c`) to model **C–S–H** gel with an interlayer insert of **graphene** or **GO** decorated with **–OH**, **epoxy**, **–SO\(_3\)H**, and **–COOH** groups at **~10%** coverage (per the manuscript). The work tracks **water dissociation**, **proton transfer**, **Ca–O\(_c\)–Ca** bridge formation, and **uniaxial tension** responses, ranking **GO–COOH** and **GO–OH** composites highest in **interfacial strength** and **ductility** relative to pristine graphene or epoxide/sulfonate-dominated cases.

## Methods

The substrate is a **tobermorite 11 Å**-like **C–S–H** cell cleaved to introduce an **~10 Å** channel into which **graphene/GO** sheets are placed. **Reactive MD** uses **LAMMPS** with **ReaxFF** and **3D periodic boundary conditions (PBC)** on **supercells** reaching **~63k–72k** **atoms** for mechanical replicas. **Verlet** integration uses **0.25 fs** **timestep**; **NPT** **equilibration** **250 ps** at **300 K** and **1 atm** with **Nosé–Hoover** **thermostat**/**barostat**, followed by **NVT** **100 ps** and extended **1000 ps** **production** relaxation to allow chemistry. **Uniaxial** strain is applied at **0.08 ps⁻¹** along interlayer **c** under **NPT** with **a,b** stresses coupled toward approximate **zero** lateral stress. **N/A — external electric field** or **umbrella sampling** in the protocol summarized here.

## Findings

**Outcomes & mechanisms:** **Deprotonation** propensity near **C–S–H** follows **COOH (≈SO\(_3\)H) > OH > epoxy** in the scenarios reported; **COO⁻–Ca** bridges and **H-bonds** to **Si–OH** strengthen **GO–COOH** interfaces, while **epoxide** opens only **~8%** under **Ca**, leaving **GO–epoxide** interfaces comparatively weak.

**Comparisons:** the authors relate **interfacial** **cohesive** response to **prior** **GO–cement** **experiments** in the **Introduction** (e.g. **Lv**, **Pan**, **Lu** citations in the article) as motivation; atomistic **tensile** metrics should be read as **nanoscale** benchmarks, not direct **macroscopic** strength predictions.

**Sensitivity:** **functional group** identity and **coverage** (**~10%** in the models) dominate **interface** chemistry; **strain rate** (**0.08 ps⁻¹**) is high relative to **laboratory** tests, so **ductility** rankings are most meaningful comparatively within this **ReaxFF** study.

**Limitations / outlook:** **idealized** **C–S–H** morphology and **ReaxFF** **transferability** caveats are stated in the article; **mesoscale** **porosity** and **aggregate** microstructure are outside the **slit-pore** **supercells**.

**Corpus honesty:** quantitative **stress** values and **figure** references belong in the **PCCP** **PDF** (`pdf_path`); verify before quoting in **benchmarks**.

## Limitations

**ReaxFF** transferability; **idealized C–S–H** morphology; **high strain rate** in mechanical tests compared to experiments.

## Reader notes (MAS / retrieval)

Route **GO–cement** interface questions here when the user names **deprotonation order**, **Ca bridges**, or **uniaxial tension** of **nanocarbon** in a **C–S–H** slit pore.

Cross-link [[theme-oxides-silica-ceramics]] for **C–S–H** background.

## Relevance to group

**Cement–nanocarbon** **ReaxFF** interface chemistry adjacent to **oxide** surface reactivity studies in the knowledge base.

## Citations and evidence anchors

- DOI: `10.1039/c8cp00006a`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
