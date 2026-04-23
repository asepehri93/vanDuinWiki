---
id: paper:2017carbrero-venue-paper
type: paper
title: "Molecular dynamics approach for crystal structures of methane A and B"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:classical-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:npt-simulation
  - keyword:reaxff-application
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1142/S0129183117500486"
year: 2017
authors:
  - "César G. Galván"
  - "José M. Cabrera-Trujillo"
  - "Ivonne J. Hernández-Hernández"
  - "Luis A. Pérez"
venue: "Int. J. Mod. Phys. C"
pdf_sha256: "8145bf30e471d5a8e406f1c269c9d97d0ae74ba7455dc87a85ad5ff54b45d6b8"
pdf_path: "papers/ReaxFF_others/Carbrero_methane.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017carbrero-venue-paper -->

## Summary

The work compares **classical all-atom (OPLS-type) and ReaxFF** molecular dynamics for methane high-pressure phases **A and B**. Final states are reached by **ramping temperature and pressure in the NPT ensemble** through regions of the methane phase diagram. Reported carbon structures are compared with recent experimental structures for these phases.

High-pressure molecular crystals exhibit plastic molecular orientations; both reactive and non-reactive classical models are tested for their ability to land on the experimentally reported carbon sublattices.

## Methods

**MD application (classical OPLS-AA and ReaxFF).** **Molecular dynamics** explores **high-pressure** solid **methane** phases **A** and **B** using both **optimized potentials for liquid simulations (OPLS) all-atom** (non-reactive) and **ReaxFF** (reactive) models. **Sampling protocol:** **NPT** integration with **controlled ramps** of **temperature** and **pressure** along segments of the **published methane phase diagram** until the simulations settle in the **A** and **B** basins (rather than quenching from a low-density fluid in one step). **Structural validation** compares relaxed **carbon sublattices** to **recent diffraction**: phase **A** as **rhombohedral R3** (lattice parameters and **21-molecule** cell construction discussed in the paper’s introduction); phase **B** as **body-centered I-43m** **carbon** ordering consistent with **cI58**-manganese-type motifs from **synchrotron** single-crystal / powder work cited there.

**Force-field training** is **N/A** (**literature** **OPLS** and **ReaxFF** forms). **Static QM**, **applied electric fields**, and **enhanced sampling** are **N/A** within the indexed scope.

**Numerical run cards** (**code**, **system sizes**, **atom counts**, **timestep**, **thermostat/barostat** brands and **coupling constants**, **ramp schedules**, **production lengths**, **full PBC** specification) are in *Int. J. Mod. Phys. C* **§2**—this wiki entry does not duplicate those tables.

**MD blueprint honesty.** **NPT** integration with **PBC** is the stated exploration mode. **Molecular dynamics** is performed with **OPLS-AA** and **ReaxFF** as described in the journal text. **Equilibration**/**production** segment durations (**ps**/**ns**), **timestep**, **thermostat**/**barostat** parameters, and the **MD engine** (**LAMMPS**-class tools are typical—confirm) are **N/A** line-by-line on this page—use **§2** of the **PDF**.

## Findings

**Outcomes:** **Phase A** and **Phase B** end states are obtained after **controlled NPT ramping** rather than abrupt quenches from low-density fluid states. **Comparisons:** authors report **good agreement** between simulated **carbon positions** and **new experimental** diffraction constraints for both phases versus crystallographic references cited in the paper. **Sensitivity:** the narrative stresses that **pathway through (T,P) space** matters for landing in the ordered molecular packings of **A/B**; **temperature**/**pressure** ramps are the primary levers. **Limitations / outlook:** high-pressure methane models remain sensitive to **force-field** choice (**OPLS** vs **ReaxFF**); readers should treat this work as a **benchmark** for **carbon** sublattices rather than full spectroscopic property prediction without further validation. ## Limitations

The indexed extract is **overview-level**; **ramp schedules, thermostat/barostat settings, and OPLS vs ReaxFF numerical tables** require the **full PDF**.

## Relevance to group

Illustrates **ReaxFF alongside classical all-atom MD** for **dense hydrocarbon phases** and **NPT exploration of phase space**, complementary to combustion- and shock-oriented methane work elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1142/S0129183117500486](https://doi.org/10.1142/S0129183117500486)

## Related topics

- [[reaxff-family]]
