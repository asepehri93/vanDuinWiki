---
id: paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived-2
type: paper
title: "An Atomistic Carbide-Derived Carbon Model Generated Using ReaxFF-Based Quenched Molecular Dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.3390/c3040032"
year: 2017
authors:
  - "Matthew W. Thompson"
  - "Boris Dyatkin"
  - "Hsiu-Wen Wang"
  - "C. Heath Turner"
  - "Xiahan Sang"
  - "Raymond R. Unocic"
  - "Christopher R. Iacovella"
  - "Yury Gogotsi"
  - "Peter T. Cummings"
  - "Adri C. T. van Duin"
venue: "C (MDPI)"
pdf_sha256: "2e9349aae703d17e91308ce477b3f7acea9a1dbc8a3521451ea7d536cb87c384"
pdf_path: "papers/Thompson_J_Carbon_Research_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived-2 -->

!!! abstract
ReaxFF quenched MD in LAMMPS generates nanoporous carbide-derived carbon models whose structure (g(r), pores, rings) and adsorption properties are compared to experiment, including optional post-quench compression.

## Summary

The authors generate atomistic models of carbide-derived carbon (CDC) using ReaxFF reactive molecular dynamics in **LAMMPS** (version 27-Jul-2013). Initial configurations place **20,000 carbon atoms** at random positions in a periodic cell of **7.488 nm** side length (~**0.95 g/cm³** initial density). **Quenched MD** runs from **3500 K** to **3000 K** with quench durations **5–500 ps** (rates **1–100 K/ps**). The ReaxFF parameterization targets carbon materials from the literature. Thermostat: **Nosé–Hoover** with **10 fs** damping; ensemble **NVT**; timestep **0.5 fs** (larger than typical 0.25 fs because only carbon is present). Optional **NPT compression** after quenching uses an **NPT** integrator at **3000 K** and **20,000 atm** with **10 fs** temperature and **100 fs** pressure damping (timestep **0.5 fs**) to shift pore statistics toward experimental targets. Structural diagnostics include pair distribution functions, pore-size distributions, adsorptive properties vs experiment, ring statistics (including non-hexagonal rings), and comparison of compressed vs uncompressed models.

## Methods

**Force-field training / fitting.** The study uses a published **ReaxFF** parameterization for **carbon** aimed at **nanoporous / carbide-derived carbon** chemistry; the article does **not** report a new QM refit in this work.

**MD application (atomistic dynamics).** Simulations use **LAMMPS** (27-Jul-2013) with **ReaxFF**. Initial states place **20,000 carbon atoms** at random positions in a **cubic** cell of side **7.488 nm** (~**0.95 g/cm³** initial density), i.e. **three-dimensional periodic** boundary conditions in the disordered bulk model. **Quenched MD** cools **3500 K → 3000 K** with quench durations **5–500 ps** (**1–100 K/ps**). Production quenches use **NVT** integration with a **Nosé–Hoover** thermostat (**10 fs** damping) and timestep **Δt = 0.5 fs** (the authors note this is larger than typical **0.25 fs** settings because only carbon is present). An **optional post-quench compression** stage uses **NPT** at **3000 K** and **20,000 atm** with **10 fs** temperature damping and **100 fs** pressure damping (same **0.5 fs** timestep). **N/A —** static **electric fields** are not applied. **N/A —** no umbrella sampling, metadynamics, or other **enhanced sampling**; the protocol is direct quench (plus optional compression). Structural and adsorption analysis uses **g(r)**, **pore-size distributions**, **ring statistics**, and comparison to **experimental** adsorption data as reported in the article.

**Static QM / DFT.** **N/A —** DFT is not the engine used to generate the CDC models summarized here.

**Review / non-simulation framing.** This is the primary **C (MDPI)** research article (**DOI 10.3390/c3040032**). A separate corpus slug may hold a **proof** PDF sibling: **`[[2017matthew-w-thompson-we-report-a-atomistic-carbide-derived]]`**.

## Findings

**Outcomes and mechanisms.** **Quenched ReaxFF MD** yields **disordered, nanoporous** carbon models whose **pair correlations**, **pore statistics**, and **adsorption-related** metrics can align with **experimental** CDC data, especially when the **optional high-pressure NPT compression** step after quenching is included. **Ring statistics** retain substantial **non-hexagonal** character relative to simple graphitic motifs, as the authors emphasize for CDC-like disorder.

**Comparisons.** The manuscript compares simulated **structure** and **adsorption** behavior to **experimental** references for CDC-type carbons (tables and figures in the PDF are authoritative for numerics).

**Sensitivity and design levers.** **Quench rate** (**1–100 K/ps** over the stated temperature window) and the **presence or absence** of the **post-quench compression** stage shift **pore-size distributions** and related observables; follow the article for quantitative trends.

**Limitations and outlook (as authored).** High-temperature quenches and extreme compression are **computational expedients** to access rearrangement kinetics and target porosity; they are not literal replicas of experimental synthesis paths—see **`## Limitations`** below for KB context.

**Corpus honesty.** Claims here follow the **indexed PDF** at `pdf_path` and the article text; refresh after any corpus PDF swap.

## Limitations

High-temperature quench and compression steps are motivated by accessible kinetics in MD and are not direct replicas of experimental synthesis paths; timestep and temperature ranges should be interpreted in that context.

## Relevance to group

Adri C. T. van Duin is a co-author; the work demonstrates ReaxFF-based CDC model building and validation against experiment.

## Citations and evidence anchors

- DOI: `10.3390/c3040032`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
