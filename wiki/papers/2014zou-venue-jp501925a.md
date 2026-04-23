---
id: paper:2014zou-venue-jp501925a
type: paper
title: "Large-Scale Reactive Molecular Dynamics Simulation and Kinetic Modeling of High-Temperature Pyrolysis of the Gloeocapsomorphaprisca Microfossils"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - domain:carbon-hydrocarbon
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:thermal-decomposition
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/jp501925a"
year: 2014
authors:
  - "Chenyu Zou"
  - "Sumathy Raman"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. B"
pdf_sha256: "cb52cc8774303a0791db598cb07a3f51224caf2cd8c0a92f9c71359c8f17fc95"
pdf_path: "papers/Zou_Raman_JPCB_2014_Pyrolysis.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014zou-venue-jp501925a -->

## Summary

ReaxFF reactive MD on multi-thousand-atom models of Guttenberg and Kukersite microfossil fragments quantifies pyrolysis products, radical initiation sites, and lumped kinetics, comparing isolated fragments with multi-component mixtures. The **J. Phys. Chem. B** study targets **kerogen-like** **macromolecular** motifs relevant to **oil** **shale** **retorting** and **thermal** **maturation** proxies drawn from **microfossil** **chemistry** literature.

## Methods

**Force-field training.** **N/A —** this application paper employs the established **C/H/O ReaxFF** parameterization cited as reference **12** in the article rather than refitting the potential within this study.

**MD application (LAMMPS ReaxFF RMD).** Fragment geometries are pre-optimized with **B3LYP/6-31G** in **Gaussian 09**, then solvated into periodic supercells with **PACKMOL** at the compositions and mass densities listed in **Table 1** (including duplicated microfossil fragments up to order **10⁴–10⁵** atoms per abstract). Equilibration follows an **NVT** minimization at **2 K** for **1.5 ps**, a **2 K → 300 K** heat ramp over **25 ps**, a short **300 K** hold, compression toward **~1.38 g cm⁻³**, and **NPT** relaxation at **1 bar** and **300 K** before launching high-temperature **NVT** pyrolysis trajectories (**1800–2500 K** for Guttenberg fragments **A/B**, **1500–2200 K** for fragment **D** and mixture cases, with additional **0.6–1.38 g cm⁻³** sets tabulated in Table 1). Reported reactive production segments span **250 ps** per the manuscript. Thermostat/barostat brands, output cadence for species tracking, and the numeric integration step are specified in `papers/Zou_Raman_JPCB_2014_Pyrolysis.pdf`; **N/A —** the integration timestep is not recovered reliably from the PDF text layer in this workspace and should be read directly from the Methods/SI tables.

**Static QM / DFT-only.** **B3LYP/6-31G** relaxations in **Gaussian 09** supply gas-phase fragment geometries prior to packing; the reactive production trajectories themselves are ReaxFF-based rather than *ab initio* MD.

**Replica sampling, electric fields, and pressure during pyrolysis.** No replica-exchange or electric-bias protocols are reported. After the **300 K**, **1 bar** **NPT** relaxation used to set density, high-temperature chemistry is advanced in constant-volume **NVT** windows at the pyrolysis temperatures listed above.

## Findings

Radical inventories and carbon-number distributions highlight preferred bond-scission initiation motifs (benzylic cleavage in fragment **A**; phenoxy-ether cleavage in fragments **B/D**) consistent with the bond-strength arguments developed in the paper. Guttenberg mixture simulations show **radical cross-talk**: radicals generated on one fragment accelerate chemistry on another—especially component **A**—relative to isolated fragment runs. A lumped kinetic model fit to the RMD trajectories yields an Arrhenius barrier the authors describe as reasonable for overall cracking, while noting that running at **T > 1500 K** within **~1 ns** windows biases product distributions toward entropically favored routes such as **ethylene**, so low-temperature selectivity predictions require caution or accelerated-sampling follow-on (as stated in the abstract).

## Limitations

High **temperature** **MD** windows and **short** **trajectories** limit direct **extrapolation** to **industrial** **retort** **timescales**; **lumped** **kinetics** are **illustrative** rather than **drop-in** **process** **models** without **calibration**.

## Relevance to group

**Adri C. T. van Duin** coauthors; **ReaxFF** **pyrolysis** of **complex** **hydrocarbon** **feedstocks** complements other **organics**/**combustion** entries in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/jp501925a](https://doi.org/10.1021/jp501925a) — `papers/Zou_Raman_JPCB_2014_Pyrolysis.pdf`.

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
