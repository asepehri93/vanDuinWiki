---
id: paper:2015o-connor-venue-airebo-m-reactive
type: paper
title: "AIREBO-M: A reactive model for hydrocarbons at extreme pressures"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:classical-ff-specialized
  - method:classical-md
  - material:polymer-organic
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1063/1.4905549"
year: 2015
authors:
  - "Thomas C. O'Connor"
  - "Jan Andzelm"
  - "Mark O. Robbins"
venue: "Journal of Chemical Physics"
pdf_sha256: "8e7f75142d1ac0d5f8c9e5c88839931b91742004e52adcc32a045b8524540327"
pdf_path: "papers/Others/OConnor_Andzelm_AIREBO_m.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015o-connor-venue-airebo-m-reactive -->

## Summary

The AIREBO potential extends the reactive hydrocarbon framework with Lennard-Jones nonbonded terms, but those LJ interactions become unrealistically stiff at small intermolecular separations, producing excess repulsion under high pressure compared with density functional theory benchmarks for polyethylene and graphite. O’Connor, Andzelm, and Robbins introduce AIREBO-M, which replaces the carbon–carbon Lennard-Jones tail with a Morse form fit to graphite interlayer compression up to about 14 GPa and to post-Hartree–Fock steric reference data for small alkanes, while preserving ambient-density behavior where the original parametrization is adequate. The motivation section ties the failure mode to high-pressure polymer and graphite simulations where interchain repulsion dominates stress.

## Methods

### Force-field training (classical reactive hydrocarbon model)

**Parent model:** **AIREBO** retains its reactive bond-order **intramolecular** description; **AIREBO-M** replaces the **intermolecular carbon–carbon Lennard-Jones** tail with a **Morse** form so repulsion does not diverge as steeply at small separations. **QM / experiment references:** the **C–C Morse** branch is fit to **x-ray** measurements of **graphite** interlayer compression up to **~14 GPa** and to **post-Hartree–Fock** reference data for **steric** interactions between **small alkanes** (for **C–H** and **H–H** channels where separate x-ray constraints are lacking). **Optimization goal:** soften the **repulsive wall** with an extra parameter while preserving **ambient** thermodynamics of the original AIREBO as far as possible (see JCP discussion).

### MD application (validation simulations)

**Classical molecular dynamics** validates **AIREBO-M** on **graphite bilayer** compression and on **quasistatic** plus **shock** compression of **orthorhombic polyethylene** supercells (Sec. II–III, *J. Chem. Phys.*). **Systems** use **3D periodic** cells with **atom** counts, **lattice** settings, and **uniaxial shock** or **quasistatic** loading paths spelled out in those sections; **timestep**, **thermostat** use away from the **shock** piston, and segment **durations** are given numerically there rather than duplicated on this wiki page. **Barostat / NPT:** **N/A** for the **shock** Hugoniot-style validation, where volume follows the **shock** driver instead of a hydrostatic **barostat**. **Replica / umbrella sampling / applied electric fields:** **N/A** for the benchmarks summarized in the abstract. **Thermal / temperature control:** **quasistatic** and **shock** protocols span **ambient** reference states and **shock**-heated **high-pressure** regimes along the Hugoniot-style paths tabulated in the article, so there is **no single fixed “production temperature”** to quote outside those **multi-state** tables.

## Findings

**Versus parent AIREBO:** replacing the **intermolecular C–C LJ** tail removes the **spurious stiffening** that breaks high-pressure graphite and polyethylene benchmarks. **Graphite bilayer** compression from **AIREBO-M** matches **quantum** reference calculations in the tests reported in the abstract. **Polyethylene:** **AIREBO-M** reproduces **quasistatic and shock** compression of **orthorhombic polyethylene** to **at least ~40 GPa** in the validation highlighted in the abstract—substantially extending the pressure window where the **LJ-limited** form fails. **Outlook (as framed in the paper):** the modification is positioned as a way to keep **ambient** AIREBO behavior while enabling **high-pressure** hydrocarbon simulations relevant to **shock** and dense molecular solid regimes.

## Limitations

Electronic polarization and explicit quantum accuracy are not recovered; chemistry remains within the AIREBO bond-order class.

## Relevance to group

Comparative context for bond-order hydrocarbon models discussed alongside ReaxFF in high-pressure organics literature.

## Citations and evidence anchors

DOI `10.1063/1.4905549`.

## Related topics

- [[reaxff-family]]
