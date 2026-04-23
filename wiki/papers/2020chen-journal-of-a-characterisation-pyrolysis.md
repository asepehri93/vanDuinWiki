---
id: paper:2020chen-journal-of-a-characterisation-pyrolysis
type: paper
title: "Characterisation of pyrolysis kinetics and detailed gas species formations of engineering polymers via reactive molecular dynamics (ReaxFF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:validation
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.jaap.2020.104931"
year: 2020
authors:
  - "T.B.Y. Chen"
  - "A.C.Y. Yuen"
  - "B. Lin"
  - "L. Liu"
  - "A.L.P. Lo"
  - "Q.N. Chan"
  - "J. Zhang"
  - "S.C.P. Cheung"
  - "G.H. Yeoh"
venue: "J. Anal. Appl. Pyrolysis"
pdf_sha256: "d67de974db9f4e541c0acdbee761f2ff5ad3255dd197ee0b6039c5ecec1861e7"
pdf_path: "papers/ReaxFF_others/Chen_Yeoh_Engineering_polymers_ReaxFF_JAAP_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020chen-journal-of-a-characterisation-pyrolysis -->

**LAMMPS** ReaxFF pyrolysis of **HDPE, PMMA, and HIPS** with elevated-temperature accelerated kinetics is compared to **thermogravimetric** measurements and used to extract volatile and char compositions relevant to fire and combustion modeling.

## Summary

The article develops a **reactive MD workflow** to follow thermal decomposition of three engineering polymers from solid-like slabs to volatile products and char. **ReaxFF (reax/c in LAMMPS)** captures bond breaking and reformation during pyrolysis. Simulated mass-loss/char trends and species distributions are compared to **TGA** experiments across heating rates, and kinetics parameters are extracted from MD and compared to experimental DTG-based analysis.

## Methods

- **Software:** **LAMMPS** with the **reax/c** package for ReaxFF potentials; initial amorphous packings prepared with **PACKMOL**, pre-annealed using **PCFF** with **Nosé–Hoover** thermostat/barostat in stated preparation stages.
- **Initial structures:** Compressed to **3 nm × 3 nm × 4 nm** cells (final densities \(\approx\) 0.93, 1.18, and 1.08 g cm\(^{-3}\) for HDPE, PMMA, HIPS); **periodic boundary conditions in x and y** with **reflecting** (non-periodic) **z** for the free surface; **12 nm vacuum** along \(z\) (final box **3×3×16 nm**).
- **Pyrolysis protocol:** **NVT** simulations at fixed temperatures **1300–4000 K** for **300 ps** at each target \(T\); **1300 K** additionally run for **2 ns** to capture slow chemistry. **Nosé–Hoover** thermostat relaxation time **0.5 ps**. **Bottom 0.2 nm** of the slab fixed (excluded from thermostat); reactive region **3.8 nm** thick. **Timestep: N/A** — the article text in the indexed PDF does not quote a numerical **integration timestep**; confirm in the full PDF or SI if needed.
- **Experiment:** TGA/DTA under **N\(_2\)** from room temperature to **800 °C** at **5–30 K min\(^{-1}\)** on commercial sheet samples; kinetics extracted via Kissinger–Akahira–Sunose and iterative DTG fitting (per Methods).
- **Barostat / pressure control:** **N/A** — **NVT** **pyrolysis** with no **NPT** production stage in the protocol summary above. **Electric field** and **umbrella / metadynamics / replica exchange:** **N/A**.

## Findings

- MD reproduces major TGA/char trends for HDPE, PMMA, and HIPS and yields **C\(_1\)–C\(_3\)** alkane-rich volatile pools as principal fuel gases from all three polymers under the modeled conditions.
- **Char** composition and relative char yields from MD align with TGA-derived char mass fractions within the stated comparisons (see manuscript tables).
- Pyrolysis **activation energies and pre-exponential factors** extracted from MD decomposition curves are reported alongside experimental kinetics (Table 3 in the article).

The article positions reactive MD as a complement to macroscopic TGA: it resolves **bond-breaking sequences** and **volatile speciation** that are not uniquely determined from mass-loss curves alone, while still requiring elevated temperatures in simulation to match laboratory time scales.

## Limitations

Elevated temperatures accelerate chemistry relative to experiment; absolute timescales and quantitative toxic minor species should be cross-checked for regulatory use. ReaxFF parameter accuracy varies by bond class.

## Relevance to group

Exemplar **ReaxFF + LAMMPS** polymer **pyrolysis** study with experimental validation—useful benchmark for decomposition and gas-release workflows in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.jaap.2020.104931](https://doi.org/10.1016/j.jaap.2020.104931)

## Related topics

- [[reaxff-family]]
