---
id: paper:2015ermakov-srep-2015-do-burning-graphene
type: paper
title: "Burning Graphene Layer-by-Layer"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:carbon-hydrocarbon
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:graphene-carbon
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:reactive-md
source_refs: []
doi: "10.1038/srep11546"
year: 2015
authors:
  - "Victor A. Ermakov"
  - "Andrei V. Alaferdov"
  - "Alfredo R. Vaz"
  - "Eric Perim"
  - "Pedro A. S. Autreto"
  - "Ricardo Paupitz"
  - "Douglas S. Galvão"
  - "Stanislav A. Moshkalev"
venue: "Scientific Reports"
pdf_sha256: "c99e2fec442f3cc67282db529f284799ff70cfe46e5142e7fcbbc161dc9e69fc"
pdf_path: "papers/ReaxFF_others/Ermakov_Paupitz_etal_SciRep_GraphOx_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015ermakov-srep-2015-do-burning-graphene -->

## Summary

Oxidation resistance of graphene and few-layer graphite is central to high-temperature electronics and processing, yet controlled thinning without basal-plane damage remains difficult: many methods yield **nonuniform** etching or introduce defects. This paper reports **low-power laser** heating of **multi-layer graphene (MLG)** in air in a **cold-wall** configuration—only the sample is hot while the surrounding gas stays near room temperature—reaching **temperatures exceeding 2000 K** on **suspended** flakes without immediate burnout. Under these conditions, **layer-by-layer oxidative thinning** proceeds with comparatively **uniform in-plane** etching. **Supported** samples on substrates, by contrast, burn **nonuniformly** at much higher rates. **Fully atomistic reactive molecular dynamics** with **ReaxFF**-class chemistry interprets **oxidation and gasification** microsteps that produce the observed **uniform** removal versus rapid **localized** attack.

## Methods

### Experiment

**MLG** from **sonicated natural graphite** on **TEM** grids compares **suspended** flakes to **supported** samples. **Low-power** laser heating in **air** uses a **cold-wall** arrangement (sample hot, gas not furnace-hot). **SEM** tracks **in-plane** versus **normal** etching; **Raman** and related optics estimate local peaks **~>2000 K** on suspended material.

### MD application (atomistic dynamics)

**LAMMPS** with **combustion-oriented ReaxFF** (*Sci. Rep.*) models **multi-layer graphene** in an **atomic oxygen** atmosphere under **PBC**, intended to mimic the **low gas-temperature** limit of the **cold-wall** experiments. **NVT** sampling with a **Nose–Hoover thermostat** spans **800–3000 K** with **0.1 fs** steps over **~150 ps** typical runs; supercell sizes are in **papers/ReaxFF_others/Ermakov_Paupitz_etal_SciRep_GraphOx_2015.pdf**. **Shear, shock, applied electric field, NPT barostat:** **N/A —** not used in the described gas-phase oxidation setup.

### Force-field training

**N/A —** applies an existing **ReaxFF** combustion parameterization (cited in the PDF) rather than reporting a new fit.

### Static QM / DFT

**N/A —** not the primary modality for the oxidation trajectories summarized here.

## Findings

**Suspended** MLG thins **layer-by-layer** in **air** under **cold-wall** laser heating at very high local **T**, while **supported** flakes oxidize **faster** and **nonuniformly** (**SEM** shows localized holes)—a direct **experiment** contrast in **morphology** and **etching** rate. **ReaxFF** trajectories support **basal-plane oxidation/gasification** chemistry consistent with an **atomic-oxygen**, **cold-wall**-like environment, linking **decomposition** microsteps to uniform removal versus localized attack. **Sensitivity** to **temperature** (**800–3000 K** in simulation) and to **substrate** support is central to the narrative. **Limitations** include simplified laser–plasma chemistry and ReaxFF’s approximate **O₂** excitation physics; see the **PDF** for quantitative **Raman**/**SEM** claims.

## Limitations

**Laser–plasma chemistry** and **defect distributions** in real flakes are simplified; **ReaxFF** captures **combustion-like** bond rearrangements but not **explicit electronic excitations** of **O₂** under laser irradiation.

## Relevance to group

Couples **graphene high-temperature oxidation** experiments with **reactive MD** interpretation for combustion-adjacent carbon chemistry.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/srep11546](https://doi.org/10.1038/srep11546) (`papers/ReaxFF_others/Ermakov_Paupitz_etal_SciRep_GraphOx_2015.pdf`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
