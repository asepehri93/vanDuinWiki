---
id: paper:2017mohammad-alaghemandi-j-phys-chem-jp7b00249
type: paper
title: "Ignition in an Atomistic Model of Hydrogen Oxidation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:puremd
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.7b00249"
year: 2017
authors:
  - "Mohammad Alaghemandi"
  - "Lucas B. Newcomb"
  - "Jason R. Green"
venue: "J. Phys. Chem. A"
pdf_sha256: "2d7fe2b19fda3ca388a37eb874ec91e260e2b46dd8f0357181332efb88efdd42"
pdf_path: "papers/ReaxFF_others/Alaghemandi_JPCA_H2_O2_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017mohammad-alaghemandi-j-phys-chem-jp7b00249 -->

!!! abstract
PuReMD-GPU ReaxFF NVE trajectories seed H₂/O₂ ignition statistics across equivalence ratios; shortest ignition delay at ϕ = 0.5 with H₂O₂ precursor and anticorrelation of ignition time with energy dissipation rate above 200 MPa.

## Summary

Reactive **NVE** molecular dynamics with **ReaxFF** in **PuReMD-GPU** studies **H₂/O₂** ignition statistics. Mixtures use **equivalence ratio ϕ** from **0.08 to 3.31**; stoichiometric boxes use **66 H₂** and **33 O₂** in an **8 nm** cubic cell with **99 molecules total** at other ϕ. Simulations use **Δt = 0.1 fs** and **3 ns** duration (sufficient to convert >80% reactants at reported conditions). Initial state **Tᵢ = 1500 K**, **ρᵢ = 250 kg/m³** with **100** independent runs per ϕ; an additional **1000** runs at **1000 K** for stoichiometric gas. Chemistry is **seeded with one OH radical** to reduce ignition delay cost. Pressure and temperature evolve during exothermic reaction (**NVE**). Ignition times are extracted from kinetic energy traces; **H₂O₂** mole fraction peaks precede ignition (~**100 ps** warning window); at high pressure (**>200 MPa**) ignition time **anticorrelates** with energy dissipation rate, implicating thermal feedback.

## Methods

**Force-field training / fitting.** The study employs a published **ReaxFF** parametrization for **H/O** chemistry (literature references **30–33**, **39** in the article); **no** new QM-based refit is reported in this *J. Phys. Chem. A* contribution.

**MD application (atomistic dynamics).** **Engine / code:** **PuReMD-GPU** drives **ReaxFF** reactive trajectories. **System size & composition:** **H₂/O₂** boxes at multiple **equivalence ratios ϕ** spanning **0.08–3.31**; the manuscript quotes a **stoichiometric** reference cell with **66 H₂** and **33 O₂** molecules in an **~8 nm** cubic periodic supercell, with analogous stoichiometry adjustments at off-stoichiometric **ϕ**. **Boundaries / periodicity:** **Three-dimensional periodic** gas-phase supercells (as standard for these homogeneous ignition ensembles). **Ensemble:** **NVE** microcanonical reactive dynamics (temperature and pressure evolve with chemistry and energy release). **Timestep:** **Δt = 0.1 fs**. **Duration:** **3 ns** trajectories (reported sufficient to consume **>80%** of reactants under the stated conditions). **Replica / statistics:** **100** independent replicas per **ϕ** at **initial Tᵢ = 1500 K** and **ρᵢ = 250 kg/m³**, plus **1000** replicas for the **stoichiometric** mixture at **1000 K**; each trajectory **seeds** chemistry with **one OH radical** to shorten ignition delay while preserving subsequent growth chemistry. **Thermostat / barostat:** **N/A —** **NVE** protocol without stochastic thermostat or hydrostatic **barostat** control. **Target temperature:** initial conditions **1500 K** (additional **1000 K** stoichiometric batch as above); **not** a constant-T production thermostat. **Pressure:** evolves under **NVE** reactive heating (authors analyze high-**P** states exceeding **~200 MPa** in the statistics). **Electric field:** **N/A —** not applied. **Enhanced sampling:** **N/A —** brute-force **MD** ensembles rather than umbrella sampling or metadynamics. **Diagnostics:** ignition times from energy traces; **H₂O₂** mole-fraction transients; correlation of ignition delay with **energy dissipation rate** at elevated pressures.

**Static QM / DFT.** **N/A —** **DFT** is **not** the time-integration engine for the ignition statistics summarized here.

**Review / non-simulation framing.** **N/A —** primary **reactive MD** research article (not a narrative review).

## Findings

**Outcomes & mechanisms.** **Ignition delay** is shortest near **ϕ = 0.5** (equal **H₂** and **O₂** counts), consistent with the authors’ comparison to a cited reduced **chemical kinetic** model. **H₂O₂** accumulates ahead of ignition, providing a **~100 ps** “early warning” window in the reported traces. At **P > 200 MPa**, ignition time **anticorrelates** with the **energy dissipation rate**, supporting a **thermal feedback** interpretation in the high-pressure portion of the **NVE** ensembles.

**Comparisons.** Atomistic ignition statistics are positioned against **continuum** kinetic expectations and the referenced reduced model (see article figures/tables for quantitative agreement).

**Sensitivity & design levers.** Trends are mapped versus **equivalence ratio**, **initial temperature** (**1500 K** vs **1000 K** stoichiometric batch), and the evolving **pressure** state reached under **NVE** exothermic compression.

**Limitations & outlook (as authored).** **OH seeding** omits some natural initiation channels; the ultrahigh-pressure regime explored is more representative of **detonation-related** physics than ambient flames—interpret accordingly.

**Corpus / KB honesty.** Claims follow the **indexed PDF** at `pdf_path`; refresh numerics after any corpus PDF swap.


## Limitations

Seeded OH radical omits some initiation channels; high-pressure regime explored is extreme vs ambient combustion but informative for detonation-related physics. Repository automation maps this stable `paper_id` to `normalized/papers/2017mohammad-alaghemandi-j-phys-chem-jp7b00249.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

Demonstrates GPU ReaxFF ignition statistics workflow relevant to reactive MD benchmarking.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpca.7b00249`

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
