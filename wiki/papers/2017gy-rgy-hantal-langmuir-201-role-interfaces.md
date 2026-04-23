---
id: paper:2017gy-rgy-hantal-langmuir-201-role-interfaces
type: paper
title: "Role of Interfaces in Elasticity and Failure of Clay-Organic Nanocomposites: Toughening upon Interface Weakening?"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:nvt-simulation
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.7b01071"
year: 2017
authors:
  - "Gyorgy Hantal"
  - "Laurent Brochard"
  - "Roland J.-M. Pellenq"
  - "Franz-Joseph Ulm"
  - "Benoit Coasne"
venue: "Langmuir"
pdf_sha256: "1dedb1b9e0378742719e3ec1a8272b2eff1a20ac7f5b0ce58a4792c07b429054"
pdf_path: "papers/ReaxFF_others/Hantal_Ulm_Pellencq_Clay_Organic_Langmuir_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2017gy-rgy-hantal-langmuir-201-role-interfaces -->

## Summary

Exfoliated clay-organic nanocomposites achieve reinforcement through very large organic-inorganic interfacial area, but how interface chemistry controls strength versus toughness remains difficult to map experimentally. This study uses reactive molecular dynamics (ReaxFF) on a model system pairing illite clay with a dense amorphous carbonaceous organic phase (CS1000) to probe failure under uniaxial tensile loading normal to the layers. Two competing initiation sites are built into the models: fracture in the clay interlayer region versus debonding at the clay-organic interface. The authors systematically reduce the density of bonds at the clay-organic interface and follow how the dominant failure mechanism and energy release shift. They interpret the trends with a cohesive-zone style law (including a hyperbolic cosine fit to interface opening) and discuss when homogeneous-stress assumptions break down for weak interfaces.

## Methods

**A — Force-field training / fitting:** **Pitman–van Duin ReaxFF** for **clay** systems with a documented **K⁺** modification from the authors’ prior **illite** work—used as published (**no** new QM refit in this paper). **Pair** cutoff **9.3 Å** without long-range tail correction, per parametrization notes in the article.

**B — Molecular dynamics / sampling:** **LAMMPS** **ReaxFF** builds **illite** + **CS1000** **amorphous carbon** composites: **interface** formation via **simulated annealing** (starts **600 K**, **50 K** steps, **2 ps**/step, **0.1 fs** timestep) plus **20 ps** **NpT** at **300 K**, **1 atm**. **Mechanical tests:** **NVT**, **300 K**, **Nosé–Hoover** (**10 fs** damping), **0.1 fs** timestep (**0.2 fs** for weakest interfaces); **uniaxial tension** along **z**, lateral edges fixed; each strain step = **minimization** + **10 ps** dynamics; **virial** stress. **Interface weakening:** bond removal down to **23.2%** of original interface bonds.

**C — DFT / static QM:** **Not** the production fracture engine here—**ReaxFF** carries **reactive** interface construction and **mechanical** response.

**D — Review / non-simulation framing:** **Primary** **Langmuir** study—**not** a review.

**Engine:** **LAMMPS** **ReaxFF**. **System:** **illite** + **CS1000** **amorphous carbon** nanocomposite cells (see **article** for **atom counts** and **in-plane** dimensions). **Boundaries / periodicity:** **3D PBC** is the standard setup for these **clay–organic** **slab** models in the **illite** literature; confirm **fixed layers** vs fully mobile **substrate** choices in **`pdf_path`**. **Ensemble / thermostat / timestep / duration / staging:** **simulated annealing** from **600 K** in **50 K** steps (**2 ps** per step, **0.1 fs** timestep), then **20 ps** **NPT** at **300 K**, **1 atm**; tensile tests at **300 K** in **NVT** with **Nosé–Hoover** (**10 fs** damping), **0.1 fs** timestep (**0.2 fs** for the weakest interfaces), **uniaxial tension** along **z** with **lateral edges fixed**, each strain increment = energy **minimization** + **10 ps** **dynamics**. **Barostat:** **N/A —** during **NVT** tensile segments; **NPT** used only for the **300 K** **1 atm** equilibration window. **Pressure / stress:** **1 atm** target in the **NPT** equilibration; **virial stress** during **tension**. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

For the fully bonded reference composite, tensile failure initiates inside the illite region (not at the interface) despite the lower cohesive strength of illite versus CS1000; the composite is more compliant than either bulk phase, shows strain hardening, and fails at higher strain than bulk illite. Integrating the stress-strain response to estimate a critical energy release rate gives about 0.48 J/m^2 for bulk illite versus about 1.11 J/m^2 for the composite in the reported analysis, with the gap attributed partly to concurrent partial interface degradation (bond loss at the interface during loading) even when the crack path remains in illite.

Systematically lowering interface bond density reduces composite strength, increases strain at failure, and eventually moves failure to the clay-organic interface. Stress and strain become strongly heterogeneous when bonding is weak and uneven, producing wavy deformation patterns for the weakest cases. A hyperbolic cosine cohesive law with three fitted parameters (sigma0 = 3.01 GPa nm^2, delta_cr = 4.83 A, K0 = 0.60 A^-1 in the article's notation) captures multiple tensile curves with a single mechanical picture when stress homogeneity is adequate; a threshold based on interface bond density (about 52% of the original bonding, corresponding to rho0 about 0.73 nm^-2 versus illite strength near 2.2 GPa) separates illite-dominated failure from interface-dominated failure. A heterogeneous-interface extension (Supporting Information) is needed to match the weakest systems at large strain.

## Limitations

The organic phase is an idealized apolar carbonaceous matrix rather than a polar polymer; illite stacks are few-layer. ReaxFF accuracy limits chemistry and absolute mechanical numbers. Fracture stability arguments borrow from continuum fracture concepts that are not guaranteed at the nanoscale.

## Reader notes (navigation)

- [[reaxff-family]]
- Related illite and clay interface work by the same group appears elsewhere in the corpus (e.g. other Hantal illite entries).
