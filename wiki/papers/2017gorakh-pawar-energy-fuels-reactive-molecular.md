---
id: paper:2017gorakh-pawar-energy-fuels-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulation of kerogen thermal maturation and cross-linking pathways"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.energyfuels.7b01555"
year: 2017
authors:
  - "Gorakh Pawar"
  - "Paul Meakin"
  - "Hai Huang"
venue: "Energy Fuels"
pdf_sha256: "d4c51eb3a1f5a0c9174a3eb49065afbf62d8f3c5f408f0337ddb0c49909c2ca8"
pdf_path: "papers/ReaxFF_others/Pawar_Kerogen_Energy_Fuels_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017gorakh-pawar-energy-fuels-reactive-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **Energy Fuels** article identified by `doi`. **Kerogen** model **chemistry** and **simulation** **timestep** belong in the **PDF**.

**ReaxFF MD** tracks **thermal maturation** of **three kerogen** **molecular ensembles** (types **I immature**, **II oil-window**, **III low-maturity**) and analyzes **cross-linking** toward **3D macromolecular** networks.

## Summary

**Reactive MD** with **ReaxFF** heats **small high-molecular-mass** **kerogen** models representing **Green River (I)**, **type II**, and **type III** maturities. Simulations produce **light species** (**H2O**, **C2H4**, **C3H6**, etc.) as **maturity** advances, alongside **highly reactive fragments** not always seen in **pyrolysis experiments**. **Cross-linking** involves **C–S**, **C–O**, and **C–C** **bridges** between **monomer** units. Overall **trends** align with **literature** **theory/experiment**, but the **density of intermolecular cross-links** achieved in the **simulated** **3D** network remains **low**. **Shale** **oil/gas** resource quality ties to **kerogen** **type** and **thermal** **history**; **atomistic** models aim to connect **lab** **pyrolysis** products to **network** **rearrangements** in **geologic** **maturation** (introduction themes).

## Methods

**A — Force-field training / fitting:** **ReaxFF** parametrization covering **hydrocarbon** plus **heteroatom** (**S**, **O**) chemistry appropriate to **kerogen-like** models—used as published; **no** new fitting exercise summarized on this page.

**B — Molecular dynamics / reactive sampling:** **High-temperature** **ReaxFF MD** on **three** molecular **kerogen** ensembles (**Green River type I immature**, **type II oil-window**, **type III low-maturity**). Monitors **bond breaking/forming**, **light gas** and **fragment** release, and **intermolecular** **cross-linking** toward **3D** networks (**timestep**, **thermostat**, **heating** in article **Methods**).

**C — DFT / static QM:** **Not reported** as the driver of maturation trajectories in the summarized work.

**D — Review / non-simulation framing:** **Application** paper connecting **atomistic** trends to **geologic** **maturation** themes in the **introduction**—**not** a methods review.

**Engine:** **ReaxFF MD** on **kerogen**-like molecular ensembles (**Energy Fuels** **Methods**). **System:** **three** maturity classes (**Green River type I immature**, **type II oil-window**, **type III low-maturity**) as described in the article; **atom counts** are **not** transcribed here. **Ensemble:** **NVT** for the **high-temperature** **ReaxFF** **maturation** trajectories (confirm any **NVE** segments in **SI**). **Timestep / thermostat / duration / PBC / barostat:** **N/A —** copy from **`pdf_path`** rather than this summary. **Temperature:** **high-temperature** **annealing** / **ramp** schedules drive **maturation** chemistry in-source. **Pressure:** **N/A —** **geologic pressure** is not modeled in the atomistic cells summarized on this page. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

- **Maturation:** **Light gas** and **fragment** evolution tracks **increasing** **simulated maturity** with **H2O**, **C2H4**, **C3H6** among products.
- **Reactive intermediates:** Some **fragments** are **over-produced** vs **pyrolysis experiments** (authors note **detection** gaps).
- **Cross-linking:** **Primary** **linkages** are **C–S**, **C–O**, **C–C** between **kerogen** **oligomer** units; pathways are **complex**.
- **3D network:** **Conversion** to a **dense 3D cross-linked** network is **limited**—**intermolecular cross-link density** stays **low** in the **accessible** **simulation** window.

- **Upshot:** the authors argue **ReaxFF** captures **qualitative** **maturation** **trends** but **finite** **system size** and **short** **times** limit **quantitative** **agreement** with **reservoir** **maturity** indicators (discussion framing).

## Limitations

**Small ensembles** and **short** **geologic time** **scaling**; **ReaxFF** **accuracy** for **S** chemistry may vary; **quantitative** **vitrinite**-equivalent **maturity** not claimed.

**Mineral** **matrix** interactions and **pressure** in **source rocks** are omitted from these **gas-phase**-like **kerogen** **cells**—expect **compositional** **shifts** when moving toward **reservoir** **realism**.

**Pyrolysis** **comparison:** match **simulation** **temperature** **ramps** and **closed-cell** constraints to **laboratory** **reactor** **conditions** before claiming **quantitative** **overlap** in **product** **yields**.

## Relevance to group

**Shale/kerogen** **pyrolysis** with **ReaxFF** complements **coal** and **petroleum** **reactive MD** entries in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.energyfuels.7b01555](https://doi.org/10.1021/acs.energyfuels.7b01555)

## Related topics

- [[reaxff-family]]
