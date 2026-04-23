---
id: paper:2018soria-j-phys-chem-si-reaxff
type: paper
title: Si/C/H ReaxFF Reactive Potential for Silicon Surfaces Grafted with Organic
  Molecules
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:reaxff-lineage
- domain:reactive-md
- material:widegap-semiconductor
- method:reaxff
- method:dft-static
- scale:atomistic
- task:parameterization
paper_keywords:
- keyword:qm-training-data
- keyword:reaxff-parameterization
- keyword:lammps
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b07075
year: 2018
authors:
- Federico A. Soria
- Weiwei Zhang
- Patricia A. Paredes-Olivera
- Adri C. T. van Duin
- Eduardo M. Patrito
venue: J. Phys. Chem. C
pdf_sha256: 01af12f1d84497b360274fe48645e3e178fe188744b0b43ac299a41434ce5745
pdf_path: papers/Soria_Si_organic_JPCC_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018soria-j-phys-chem-si-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JPCC article identified by `title` and `pdf_path`.

## Summary

A **Si/C/H ReaxFF** parameterization is developed for **alkyl-grafted silicon** surfaces, trained against **DFT** reaction energies and barriers for decomposition pathways on **small Si clusters** and extended surfaces. **ReaxFF MD** in **ADF** and **LAMMPS** follows **thermal decomposition** of alkyl monolayers at high temperature; **Arrhenius** analysis of MD rates is compared to **DFT** barriers and to **transition-state theory** expectations for pre-exponential trends with chain length. Coverage-dependent stability of monolayers on **Si(111)**, **Si(100) 2×1**, and **“half-flat” Si(100)** is compared between ReaxFF and experiment/DFT. Applications include **thermal** **stability** screening of **SAM** coatings used in **microfabrication** and **sensing** stacks.

## Methods

- **Parameterization:** Combine prior **Si/H** and **hydrocarbon** ReaxFFs; optimize on a **DFT training set** of reaction energies for **β-hydride elimination**, **alkene elimination**, radical-mediated steps, and related elementary reactions on cluster models; error-function minimization between ReaxFF and QM energies (equation and weighting in the paper). Training emphasizes **radical**-mediated **β-hydride** sequences that dominate **high-T** **decomposition** channels.
- **DFT validation:** Barrier and energy comparisons for elementary steps observed in MD; additional checks on coverage-dependent energetics vs prior DFT on ethyl-terminated Si(111).
- **Production reactive MD:** **ADF2017** and **LAMMPS** **ReaxFF** **NVT** runs on **alkyl-grafted** **Si(111)**, **Si(100) 2×1**, and half-flat **Si(100)** **slab** **supercells** with **PBC**; **0.1 fs** **velocity Verlet**; **100 fs** temperature damping after **1 ps** at **300 K**; **800 ps** at **1500–2200 K** for high-**T** **decomposition** statistics. **Thermostat name beyond damping:** **N/A — see JPCC Methods**. **Barostat / pressure:** **N/A — constant-volume NVT** (no **NPT**). **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not used (**Arrhenius** from direct **MD**).
- **Kinetics:** Arrhenius plots from MD rates; comparison of activation energies and prefactors to **DFT** and **TST** expectations.
## Findings

- **Mechanism:** Dominant decomposition path is **β-hydride abstraction** by **silyl radicals** followed by **alkene elimination** to the gas phase, consistent with DFT barrier ordering.
- **Barriers & kinetics:** MD **activation energies** match **DFT** well; **prefactor vs chain length** trends align with **TST**.
- **Coverage:** ReaxFF reproduces experimental trends for **alkyl coverage** on several Si orientations as a function of chain length; **DFT and ReaxFF** both indicate **decyl** monolayers can be stable at **high coverage (~0.8)** at moderate temperatures.
- **Cross-code** checks (**ADF** vs **LAMMPS**) are used to increase confidence that observed **kinetics** are not an artifact of a single integrator implementation.

## Limitations

High-temperature MD accelerates chemistry; direct comparison to low-T experiments is indirect. Cluster/surface models may omit full device-scale defects. **Ambient** **oxidation** or **aqueous** **hydrolysis** pathways are not the focus of the **thermal** **decomposition** benchmarks presented.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]] (adjacent **surface** **grafting** context for **Si** **electronics**)
