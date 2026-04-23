---
id: paper:2018harpale-carbon-130-2-ablative-thermal
type: paper
title: "Ablative thermal protection systems: Pyrolysis modeling by scale-bridging molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:continuum-or-mesoscale
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.12.099"
year: 2018
authors:
  - "Abhilash Harpale"
  - "Saurabh Sawant"
  - "Rakesh Kumar"
  - "Deborah Levin"
  - "Huck Beng Chew"
venue: "Carbon"
pdf_sha256: "1406db0f480b436016cef297b9600591f1bd10f546741704523fa269b6d7a397"
pdf_path: "papers/ReaxFF_others/Harpale_Levin_Ablative_pyrolysis_Carbon_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018harpale-carbon-130-2-ablative-thermal -->

## Summary

**Scale-bridging MD** connects atomistic **pyrolysis** of a **highly crosslinked phenolic formaldehyde** network to a **continuum thermal response model** for a **charring syntactic foam** ablator. **Curing** of the thermoset uses **PCFF** in **LAMMPS**; **pyrolysis** stages switch to **ReaxFF** for bond breaking/formation. **Arrhenius**-like temperature dependence of bulk pyrolysis is reported from **500–2300 K** MD; recession inputs feed **macroscopic** predictions compared to experiments. The motivating context is **thermal protection systems** where **charring**, **gas blowing**, and **surface recession** must be predicted for mission-relevant heat loads.

## Methods

- **Curing (PCFF / LAMMPS):** Initial **20×20×26 nm³** box of **phenolic rings + CH\(_2\)** (**thousands of atoms** once populated); **0.2 fs** **timestep**; periodic **x,y**, reflecting **z** boundaries; **NVT**-style **Berendsen** **thermostat** stages over curing **runs** whose lengths are tabulated in **ps**/**ns** in the **Carbon** **PDF**; biaxial compression to ~**1.20 g/cc**; **explicit C–C bond formation** when ortho/para C–C distances **< 0.3 nm**; degree of crosslinking **D** tracked up to **D ≈ 0.93**; conjugate-gradient minimization after removing disconnected fragments.
- **Pyrolysis (ReaxFF):** **ReaxFF** replaces **PCFF** (hydrocarbon oxidation–calibrated **parameter set**, with **DFT/QM** benchmarks from the prior parametrization cited in the article); **N/A — new QM training set** or **genetic-algorithm** **ReaxFF optimization** performed in this **Carbon** paper beyond adopting that file. **12–15 nm** vacuum slab added; **300 K** equilibration with **~10 atm** **biaxial stress** (anisotropic **pressure** control); density ~**1.25 g/cc**; fixed **bottom 0.5 nm**; **5 nm** heated slab with **NVT**-targeted **Berendsen** **thermostat** sweeps at **500–2300 K**; **uni-directional walls** trap fragments; **0.25 fs** **timestep** during pyrolysis segments lasting **hundreds of ps** as reported in the **PDF**.
- **Kinetics / continuum:** **C–C** bond-breaking statistics → **Arrhenius** rates → **effective surface recession**; fed into **thermal material response** for **AVCOAT-like** foam; compared to experimental **char thickness / temperature** data.
- **Coupling intent:** Atomistic rates are **not** used as standalone chemistry benchmarks alone; they are reduced to **effective** pyrolysis inputs that a **continuum** thermal-response solver can consume, closing the loop to **engineering** observables.

## Findings

- Bulk **pyrolysis onset** ~**500–800 K**, consistent with **TGA**; **H\(_2\)O** loss then **ring fragmentation**; **Arrhenius** behavior for bulk kinetics.
- **Mechanism vs temperature:** low-T **bulk** fragmentation vs **~2300 K** onset of **surface spallation**-like removal of larger clusters.
- **Continuum model** predictions (char thickness, temperature fields, blowing) agree with **prior experiments** for the foam scenario studied.
- The authors stress that **high-temperature** surface removal can involve **cluster** ejection pathways that differ from bulk **bond-by-bond** statistics, motivating separate characterization of **spallation-like** regimes in addition to volumetric pyrolysis.

## Limitations

**ReaxFF** parametrization targets **gas-phase hydrocarbon oxidation**; **time scales** remain short vs flight; **continuum** coupling uses extracted **effective** kinetics.

## Relevance to group

Demonstrates **ReaxFF pyrolysis** linked to **engineering** TPS response—adjacent to **combustion** and **polymer** reactive MD in the corpus.

## Citations and evidence anchors

- DOI: `10.1016/j.carbon.2017.12.099`.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
