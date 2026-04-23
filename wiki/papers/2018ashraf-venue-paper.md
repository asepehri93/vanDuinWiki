---
id: paper:2018ashraf-venue-paper
type: paper
title: "Application of ReaxFF-Reactive Molecular Dynamics and Continuum Methods in High-Temperature/Pressure Pyrolysis of Fuel Mixtures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: ""
year: 2018
authors:
  - "Chowdhury Ashraf"
  - "Sharmin Shabnam"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Book chapter in Computational Approaches for Chemistry Under Extreme Conditions (Springer)"
pdf_sha256: "1b790c554191ed96c06d8c93a94fac5831030ec6f1bdb7b52f8c5915adcd8362"
pdf_path: "papers/Ashraf_Shabnam_En_7_Chapter_Author_annotated_2018.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2018ashraf-venue-paper -->

## Summary

Book chapter on using **ReaxFF reactive molecular dynamics** together with **continuum** modeling to study **high-temperature and high-pressure pyrolysis** of **fuel mixtures** (including **toluene** and **n-dodecane**), motivated by combustion devices that operate above the critical pressure of fuel or oxidizer. The discussion connects **Arrhenius-type** rate parameters from atomistic simulations to continuum treatments and examines when simple kinetic pictures break down.

## Methods

Sourced from the chapter PDF (`pdf_path`).

- **Reactive MD (ReaxFF):** Simulations use the **CHO-2016** combustion ReaxFF parameterization (Ashraf et al., as cited in the chapter) for **toluene** and **n-dodecane** pyrolysis. All atomistic runs are **NVT** (fixed **N**, **V**, **T**) in periodic cubic cells; **temperature** is controlled with a **Berendsen** thermostat (**damping 100.0 ps**). The **integration timestep is 0.1 fs** throughout. **Bond-order cutoff 0.3** is used only for species identification (not to alter dynamics).
- **Single-component benchmarks:** **40** molecules per species in cubic boxes chosen to give overall densities **0.2** and **0.4 kg per dm^3** (e.g. toluene boxes **31.20 A** and **25.00 A**; n-dodecane **38.39 A** and **30.47 A**). After minimization, **NVT equilibration 10 ps at 1500 K**, then **10** distinct initial samples; **NVT** production at **2000-2600 K** in **100 K** steps with average initial pressures in the **~26-75 MPa** range over the first **5 ps** of each run. **n-Dodecane** trajectories **50 ps**; **toluene** **200 ps** (less reactive). **Mixtures:** compositions and cubic box sizes per **Table 7.1** (e.g. **1:40** through **40:40** n-dodecane:toluene at **0.2** and **0.4 kg per dm^3**); **10 ps** equilibration at **1500 K**, then **200 ps** **NVT-MD** at **2000-2600 K** (**100 K** intervals) at **0.1 fs** timestep.
- **Continuum (0D):** Matching **zero-dimensional** pyrolysis simulations use the **same** initial **temperature**, **density**, and **mole fractions** as the MD cases; **constant-volume, constant-temperature** integration parallels the **NVT** atomistic setup. A **cubic equation of state** handles real-gas effects; a **179**-species, **1895**-reaction Arrhenius mechanism (as referenced in the chapter) supplies continuum kinetics.

## Findings

- ReaxFF-MD is used to examine how a **highly reactive fuel** alters the behavior of a **less reactive fuel** as **concentration**, **temperature**, and **density/pressure** change.
- **Activation energies** from Arrhenius-type analyses are **compared** between ReaxFF-based MD and continuum simulations, and limitations of the continuum side are discussed.
- The work identifies **pressure/temperature** and **mixing** conditions where **simple first-order Arrhenius relations** are **not applicable**, linked to **different initial reaction mechanisms** and **product distributions** for the two fuels.
- The chapter argues that ReaxFF MD can yield **atomistic insight** into fuel-mixture combustion properties under **supercritical** conditions where experiments are difficult.

## Limitations

- **Continuum** mechanism (**179** species) is validated in the chapter mainly at **lower P/T** than the **ReaxFF** windows; extrapolation caveats apply. Atomistic runs use **elevated T/P** to accelerate chemistry (**as discussed** in **Sec. 7.3**).

## Reader notes (navigation)

- Companion ingest: [[2018ashraf-venue-paper-2]] (alternate PDF).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
