---
id: paper:2018qian-mao-j-phys-chem-dimerization-polycyclic
type: paper
title: Dimerization of Polycyclic Aromatic Hydrocarbon Molecules and Radicals under
  Flame Conditions
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:fuel-combustion
- domain:carbon-hydrocarbon
- domain:reactive-md
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:combustion
- keyword:reaxff-application
- keyword:lammps
- keyword:reactive-md
- keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpca.8b07102
year: 2018
authors:
- Qian Mao
- Ding Yu Hou
- Kai Hong Luo
- Xiaoqing You
venue: J. Phys. Chem. A
pdf_sha256: b4a613e3bb6def6fa27a8899bf738b6ded83b32f21c839a742deb5b4dce15e4c
pdf_path: papers/ReaxFF_others/QianMao_JPCA_2018_PAH_dimer.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018qian-mao-j-phys-chem-dimerization-polycyclic -->

## Summary

ReaxFF molecular dynamics and supporting quantum chemistry quantify collision efficiencies and dimerization pathways for polycyclic aromatic hydrocarbon (PAH) molecules and radicals relevant to soot nucleation, including oxygenated radicals. The study is positioned as a way to supply **microscopic** sticking and recombination inputs where full **flame** chemistry is too expensive to resolve exhaustively at the **QM** level.

The paper cross-checks ReaxFF barriers for hydrogen abstraction from coronene against B3LYP and M06-2X data, couples ReaxFF MD with 0-D Chemkin kinetics for H/OH pools, and performs large batches of binary-collision ReaxFF MD in LAMMPS (`reax/c`) for pyrene and coronene species. Gas-phase QC uses Gaussian 09 at B3LYP/6-311G(d,p) geometries with higher single-point energies (M06-2X/B3LYP). MD equilibrates PAHs in NVT (1500–2500 K, Nosé–Hoover, 100 fs damping) before adiabatic NVE collisions at 0.1 fs with 120,000 sampled binary events.

## Methods
**1 — MD application (binary collisions + staged heating).** **ReaxFF** (**C/H/O combustion** parameterization) is integrated in **LAMMPS** (`fix reax/c`) for large batches of **binary-collision** trajectories: **NVT** preequilibration of **PAH** targets at **1500–2500 K** with **Nosé–Hoover** thermostat (**100 fs** damping quoted in this wiki’s prior curation traceable to the article), followed by **adiabatic NVE** collisions at **0.1 fs** with **120 000** sampled events and **50–80 Å** initial separations. **System composition:** each event pairs **pyrene**/**coronene**-family **molecules/radicals** with **~10²–10³ atoms** in the combined periodic cell depending on the selected radical site count and buffer gas content (see *J. Phys. Chem. A* tables). **PBC:** large **gas-phase** cells with **three-dimensional PBC** as in standard collision studies. **Barostat:** **N/A —** **NVE/NVT** stages without **NPT** hydrostatic control. **Pressure:** **N/A —** not a high-pressure study. **Electric fields / enhanced sampling:** **N/A —** statistics come from **brute-force** collision sampling rather than **umbrella**/**metadynamics**.

**2 — Static QM.** **Gaussian 09**: **B3LYP/6-311G(d,p)** optimizations/TSs with **M06-2X/6-311G(d,p)** single points for barrier benchmarking.

**3 — Kinetics coupling.** **Chemkin-Pro** **0-D** reactor for **H/OH** pools (**19** species, **27** reactions) parameterized from **QM**.

**4 — Force-field training.** **N/A —** applies an established **ReaxFF** combustion parameterization with **QM** spot checks rather than refitting here.

## Findings
**Outcomes / mechanisms:** **ReaxFF** reproduces **H-abstraction** energetics for **coronene** between **B3LYP** and **M06-2X** trends and tracks **0-D** kinetics qualitatively, while some **radical–radical** recombination efficiencies differ, affecting **dimer** concentrations. Many **radical–radical** encounters form **weakly bound complexes** rather than immediate **covalent dimers**; **oxygenated PAH radicals** show reduced propensity toward **soot nucleation** channels in the modeled scenarios.

**Comparisons:** explicit **QM** (**B3LYP/M06-2X**) and **0-D** kinetics comparisons anchor the **ReaxFF** collision database.

**Sensitivity:** **collision temperature**, **PAH size**, and **radical site count** modulate **sticking** vs **transient** outcomes.

**Limitations:** high-**T** gas-phase collisions are not ambient condensed phases; **ReaxFF** remains approximate for conjugated radicals.

**Corpus honesty:** protocol numbers follow the curated summary traceable to **`papers/ReaxFF_others/QianMao_JPCA_2018_PAH_dimer.pdf`**; confirm any updated values in the **VOR**.

## Limitations

High-temperature collision settings target flame chemistry, not ambient condensed phases; ReaxFF remains approximate versus high-level QM for conjugated radicals. Extending the collision database to heavier PAHs or heteroatom-rich radicals would increase statistical cost and parameterization scrutiny without changing the paper’s core conclusion that **binary-collision** statistics can discriminate **sticky** versus **transient** encounters.

## Relevance to group

Demonstrates ReaxFF + LAMMPS workflows for PAH growth relevant to combustion soot modeling.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.8b07102](https://doi.org/10.1021/acs.jpca.8b07102)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
