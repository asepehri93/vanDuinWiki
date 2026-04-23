---
id: paper:2019lijun-combustion-a-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulation of the thermal decomposition mechanisms of 4,10-dinitro-2,6,8,12-tetraoxa-4,10-diazatetracyclo[5.5.0.05,9.03,11]dodecane (TEX)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:energetic-materials
  - keyword:reactive-md
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2019.01.014"
year: 2019
authors:
  - "Lijun Yang"
  - "Junying Wu"
  - "Deshen Geng"
  - "Fuping Wang"
  - "Yanxi Huang"
  - "Lang Chen"
venue: "Combustion and Flame"
pdf_sha256: "8b550656ac6bed92265a3bcbdba184060cbb5b77d327db41e16677d520bc6468"
pdf_path: "papers/ReaxFF_others/Yang_CombFlame_2019_TEX.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019lijun-combustion-a-reactive-molecular -->

TEX is a cage-structured energetic nitramine whose thermal decomposition chemistry is studied with ReaxFF/lg reactive MD at several thousand Kelvin to catalog bond-breaking sequences, gas-phase products, and carbon-rich clusters.

## Summary

The publication applies the ReaxFF/lg reactive force field in periodic boundary conditions to a TEX supercell and heats the system isothermally at 2000 K, 2500 K, 3000 K, and 3500 K to accelerate thermal decomposition. Trajectory analysis extracts dominant initiation steps, stable small-molecule products, evolving cage fragmentation, composition of condensed carbonaceous clusters, and effective kinetic staging as temperature increases. The abstract positions TEX as an isowurtzitane cage explosive with favorable casting properties and cites literature on N–NO₂ bond energy as a sensitivity correlate, motivating systematic reactive MD across temperatures where clusters and gas products compete.

## Methods

**1 — MD application (atomistic dynamics).** Simulations use **LAMMPS** with the **ReaxFF/lg** reactive force field. A **3 × 3 × 2** supercell of crystalline **TEX** contains **36 TEX molecules** (see Fig. 1 in the article). **Three-dimensional periodic boundary conditions** enclose the cell. The protocol first **relaxes** the geometry to a force tolerance of **10⁻⁷ kcal mol⁻¹ Å⁻¹**, assigns **Maxwell–Boltzmann** speeds at **300 K**, then equilibrates in **NVT** at **~300 K** for **10 ps** with a **Berendsen** thermostat, followed by **NPT** at **300 K** and **0 atm** for **10 ps** with a **Nosé–Hoover** barostat/thermostat (as stated in the paper’s Methods). **Isothermal–isochoric (NVT) MD** is then run at **2000 K, 2500 K, 3000 K, and 3500 K** with a **0.1 fs** timestep and a **Berendsen** thermostat (damping **100 fs**). **Molecular species** are recorded every **10 fs**; **bond orders and atomic trajectories** every **200 fs** (per the article). **Production** trajectories extend to the **hundreds of picoseconds** range in the reported potential-energy and species-count analyses (e.g. order **10² ps** at the higher temperatures in the text).

**2 — Force-field training:** **N/A** — the study **applies** the published **ReaxFF/lg** nitramine parameterization; it does not re-fit the force field.

**3 — Static QM / DFT-only:** **N/A** as a primary method; the **Introduction** cites prior **DFT** and **AIMD** on TEX for context only.

**Barostat in production:** **N/A** — thermal decomposition production stages are **NVT** (constant volume).

**Electric field / bias:** **N/A**.

**Replica / enhanced sampling:** **N/A** — direct **hot** NVT trajectories; no umbrella or metadynamics.
## Findings

Decomposition initiates with N–NO₂ bond cleavage, followed by C–O stretching and progressive cage rupture that releases NO₂ and related fragments in stages. The authors report major gas-phase products including NO₂, NO, H₂O, CO₂, N₂, H₂, HNO₂, and HNO, together with larger clusters such as C₁₂H₁₂N₆O₁₂ and C₁₈H₁₃N₇O₁₄ whose prevalence depends on temperature and reaction progress. Cluster evolution is temperature sensitive: lower temperatures leave the cage largely intact and limit cluster growth, whereas higher temperatures promote large clusters that may subsequently fragment. Hydrogen, nitrogen, and oxygen partition differently between clusters and gas-phase species, with oxygen retained more strongly in condensed fragments—a trend the authors connect to later autoxidation behavior. The introduction contrasts this temperature-swept ReaxFF survey with prior AIMD on small TEX supercells that did not simultaneously address clusters and high-temperature kinetics at scale.

## Limitations

High-temperature reactive MD uses empirical reactive potentials; quantitative rates should be cross-checked against experiment and quantum benchmarks where available.

## Relevance to group

Example of ReaxFF/lg applied to nitramine cage decomposition chemistry relevant to energetic materials modeling.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2019.01.014](https://doi.org/10.1016/j.combustflame.2019.01.014)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- [[reaxff-family]] · [[domain:organics-polymers-pyrolysis]]
