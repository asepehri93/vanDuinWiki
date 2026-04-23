---
id: paper:2017aussems-chemical-sci-atomistic-simulations
type: paper
title: "Atomistic simulations of graphite etching at realistic time scales"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:enhanced-sampling
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1039/C7SC02763J"
year: 2017
authors:
  - "D. U. B. Aussems"
  - "K. M. Bal"
  - "T. W. Morgan"
  - "M. C. M. van de Sanden"
  - "E. C. Neyts"
venue: "Chem. Sci."
pdf_sha256: "f2b6e782331d445fbed49b2c87d2a8e5bfee2674358b33bf17316ab0ec634660"
pdf_path: "papers/ReaxFF_others/Aussems_ReaxFF_graphene_H.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017aussems-chemical-sci-atomistic-simulations -->

## Summary

Hydrogen plasmas erode graphite plasma-facing components through a combination of prompt collisional damage and slower thermochemical pathways that unfold between ion impacts. Aussems et al. combine ReaxFF chemistry with collective-variable hyperdynamics (CVHD) in LAMMPS to extend the effective time between energetic hydrogen impacts toward roughly one millisecond at a reference flux of order \(10^{20}\) m\(^{-2}\) s\(^{-1}\), matching the abstract’s framing. The central thesis is that dwell time between impacts determines whether erosion is dominated by knock-on sputtering or by thermally activated C–C chemistry—a distinction that collapses when MD schedules impacts too frequently for computational convenience.

The motivation spans fusion devices and related environments where hydrogen–graphite interactions control impurity sources and wall erosion, but where laboratory ion fluxes are orders of magnitude lower than those implicit in picosecond-spaced MD impacts. Bridging that gap requires accelerated dynamics so relaxation, diffusion, and thermochemical bond breaking between impacts enter the same simulation as prompt collisional events.

## Methods

**MD application (LAMMPS + CVHD).** All simulations use **LAMMPS** with a **modified Colvars** module implementing **collective-variable hyperdynamics (CVHD)**, which builds a **self-learning bias potential** to accelerate basin-to-basin transitions (`papers/ReaxFF_others/Aussems_ReaxFF_graphene_H.pdf`, **Simulation model** section). **ReaxFF** is used instead of **second-generation REBO** because **long-range van der Waals**, **Coulomb**, and **torsion** terms matter for **H–graphite** chemistry under reactive conditions. The work compares **unbiased H bombardment** with **CVHD** runs that stretch the **effective dwell time** between **keV-scale H** impacts across **nine orders of magnitude**, reaching **~1 ms** between impacts for a reference **flux ~10²⁰ m⁻² s⁻¹** as stated in the abstract. **Graphite slab** dimensions, **PBC**, **thermostat** parameters (**Berendsen** / **Nosé–Hoover** as applicable), **timestep**, **NVT/NPT** staging, **production duration**, **temperature**, **pressure** coupling, and any **electric field** are **not** duplicated in the abstract-level note used here—extract them from **Methods** in **`pdf_path`**. **CVHD** is the **enhanced-sampling** mechanism; unbiased bombardment supplies **controls**.

**Force-field training:** **N/A —** applies an established **ReaxFF** description for **C/H** chemistry cited in the article; the novelty here is **CVHD**-accelerated **dynamics**, not a new **FF** fit.

## Findings

**Erosion yield**, **H coverage**, and **emitted species** distributions hinge on **time between impacts**: longer gaps favor **thermally activated C–C chemistry**, whereas **picosecond-spaced** impacts emphasize **prompt knock-on** removal—a regime prior bombardment studies could not reach. Readers must therefore treat **simulated flux** as a tunable knob, not a literal match to experiment, when **chemical erosion** matters. **CVHD** is framed as a **bridge** rather than a drop-in replacement for unbiased **long-time** kinetics. **Limitations:** bias potentials alter dynamics; **ReaxFF** omits **electronic excitations** from the plasma environment.

## Limitations

Hyperdynamics biases dynamics; quantitative erosion yields require unbiased segments and experimental cross-checks. ReaxFF cannot capture electronic excitations from the plasma sheath.

## Relevance to group

Methodological reference combining **ReaxFF** with **accelerated dynamics** for **carbon** plasma/etching chemistry.

## Citations and evidence anchors

- DOI: `10.1039/C7SC02763J`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
