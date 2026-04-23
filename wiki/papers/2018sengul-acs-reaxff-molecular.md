---
id: paper:2018sengul-acs-reaxff-molecular
type: paper
title: ReaxFF Molecular Dynamics Study on the Influence of Temperature on Adsorption,
  Desorption, and Decomposition at the Acetic Acid/Water/ZnO(1010) Interface Enabling
  Cold Sintering
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:catalysis-surfaces
- domain:oxides-ceramics
- domain:reactive-md
- material:oxide
- method:reaxff
- scale:atomistic
- task:application
paper_keywords:
- keyword:oxide-surface
- keyword:reaxff-application
- keyword:water-interfaces
- keyword:nvt-simulation
- keyword:berendsen-thermostat
candidate_tags: []
source_refs: []
doi: 10.1021/acsami.8b13630
year: 2018
authors:
- Mert Y. Sengul
- Clive A. Randall
- Adri C. T. van Duin
venue: ACS Appl. Mater. Interfaces
pdf_sha256: e545b8040902a5da8a944d6d2bcb4df0b211bfdda3aa5fc967f0413689c20746
pdf_path: papers/Sengul_ZnO_AceticAcid_ACS_AMI_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018sengul-acs-reaxff-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the ACS article identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Reactive molecular dynamics with a **combined ReaxFF** potential (O/H/Zn for ZnO–water from prior work plus O/H/C for organics, with merged optimization for acetic acid deprotonation in water) is applied to a **ZnO(101̅0)** slab contacting a concentrated **acetic acid/water** mixture (800 H\(_2\)O + 200 CH\(_3\)COOH, intended to mimic low-pH cold-sintering environments). Simulations span effective **300–1200 K** with staged heating and long equilibration; species populations and coverages are analyzed in the surface layer versus gas-like region. The work connects adsorption/desorption trends to **Langmuir-type** behavior, tracks **acetate decomposition** toward CO\(_2\) and formaldehyde, and discusses decomposition pathways and barrier estimates from constrained ReaxFF runs.

## Methods

- **Force field:** H/O/Zn potential for ZnO–water (literature parameterization for water on ZnO surfaces) combined with C/H/O parameters for biomolecular solutions; cross-terms optimized so that **dissociative adsorption energies** of acetic acid on ZnO(101̅0) match DFT trends; Zn–C bonding terms disabled as nonphysical for this system.
- **Energy minimizations** on 12-layer ZnO slabs (360 Zn + 360 O per layer stack) with controlled acetic acid coverage \(\theta\) (e.g. 30 molecules for \(\theta=1\)) to obtain adsorption energies via an adsorption-energy formula in the paper.
- **Dynamics:** **ADF** ReaxFF MD; **0.25 fs** integration (velocity Verlet); **Berendsen thermostat** with **0.1 ps** damping; simulation cell about **60 × 65 × 300 Å\(^3\)** including vacuum; liquid slab placed on the oxide after density-based equilibration (~1 g/cm\(^3\) water, ~1.05 g/cm\(^3\) acetic acid).
- **Protocol:** Temperature raised in **100 K** steps with **50 ps** equilibration per step, then **1 ns** at the target temperature; production statistics from the last **0.5 ns** (25 fs sampling) with surface species defined by **≤ 3.0 Å** from surface Zn.
- **Decomposition path analysis:** Restrained ReaxFF runs at very low temperature (**0.25 K**) with distance-based restraints (exponential restraint form in the paper) to step formaldehyde oxidation toward CO\(_2\) on the surface; barrier heights reported in **kcal/mol** for sequential steps.

**Production MD (interface, consolidated).** Same protocol as the bullets above: **NVT**-style **Berendsen**-thermostatted **ReaxFF molecular dynamics** in **AMS/ADF** on the **60 × 65 × 300 Å\(^3\)** periodic **supercell** with **PBC**; **0.25 fs** **velocity Verlet**; staged **100 K** ramps with **50 ps** **equilibration** per step and **1 ns** at target **T**; statistics from the last **0.5 ns** (**25 fs** output interval). **Barostat / pressure:** **N/A — constant-volume** (**no NPT**). **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not used for production trajectories (low-**T** restrained scans only).
## Findings

At **300 K**, roughly **one-third** of water molecules adsorb on the surface (mix of molecular and dissociated forms, including half-dissociated (2×1)-like patterns consistent with prior DFT/ReaxFF); about **58%** of acetic acid molecules adsorb, with **chelating, bridging, and monodentate** acetate modes and two deprotonation routes (to lattice oxygen vs bridging hydroxyl/water formation). **Overall surface coverage** by water- and acid-derived species is high (~**80%** of sites), with acetates competitively stabilized relative to molecular water.

With heating, adsorption/desorption and decomposition evolve: acetate surface fraction can rise to a maximum near **~800 K** in the simulated protocol, then **CO\(_2\)** appears as decomposition sets in; trends align qualitatively with experiments that coupled gas-phase acid and CO\(_2\) evolution, with the paper noting **temperature offsets** versus experiment due to faster simulated heating. **Surface coverage** decreases with temperature in a manner consistent with a **Frumkin–Fowler–Guggenheim** (modified Langmuir) picture with **positive** lateral interaction energies from fits. **Acetate decomposition** to **H\(_2\)CO** and **CO\(_2\)** proceeds via nucleophilic attack on the methyl group and radical intermediates as illustrated in the paper; formaldehyde is reported to desorb rather than further oxidize on the simulated timescales. Restrained MD along the CH\(_2\)O → CO\(_2\) pathway yields **small** step barriers (order **~0.5–6 kcal/mol** for the documented stages), interpreted as consistent with observed decomposition at elevated temperature.

## Limitations

- Effective temperatures and rapid heating in MD shift quantitative temperatures relative to experiment; the authors caution that trends are more reliable than absolute T values.
- CH\(_2\)O further oxidation on ZnO is not observed within the simulated timescales.

## Reader notes (navigation)

- Companion JCP study on bulk acetic acid–water mixtures: [[2018sengul-venue-reaxff-molecular]]
- Supporting figures: [[2018sengul-venue-microsoft-word]]

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
