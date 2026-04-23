---
id: paper:2014bhoi-fuel-136-201-molecular-dynamic
type: paper
title: "Molecular dynamic simulation of spontaneous combustion and pyrolysis of brown coal using ReaxFF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:lammps
  - keyword:nvt-simulation
source_refs: []
doi: "10.1016/j.fuel.2014.07.058"
year: 2014
authors:
  - "Sanjukta Bhoi"
  - "Tamal Banerjee"
  - "Kaustubha Mohanty"
venue: "Fuel"
pdf_sha256: "9d4d6429e2214653819149a68b0cb9f3783436e31f8c4ddaad37bf04dc44a41d"
pdf_path: "papers/ReaxFF_others/Sanjukta_BrownCoal_Fuel_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014bhoi-fuel-136-201-molecular-dynamic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Stoichiometric labels in the abstract use φ notation—verify definitions in the paper.

## Summary

**ReaxFF MD** simulates **pyrolysis** and **combustion** of a **brown coal** model at **large** (**>1000 atoms**) scale. Runs explore **fuel-lean**, **fuel-rich**, and **stoichiometric** **oxidizer** conditions at **high temperature** to access chemistry within affordable CPU time. The abstract notes **combustion** initiates by **thermal fragmentation**, followed by **H abstraction** and **H₂O** formation; **potential energy** trends **differ** between **combustion** vs **pyrolysis**; **temperature** effects dominate over **density** in the pyrolysis cases highlighted; **formaldehyde** appears as an **intermediate** consistent with **literature**.

## Methods

- **Force field:** **ReaxFF** parameterization for **C/H/O/N/S/B** **coal** chemistry (**Castro-Marcano**-type **Illinois No. 6** training lineage as referenced).
- **Pyrolysis:** **16** literature **brown-coal** molecules in **periodic** cells (**~60×56×44 Å**) at **ρ = 0.08, 0.10, and 0.20 g/cm³**; minimize at **10 K (NVE)**, **NVT equilibration 10 ps** with **Δt = 0.1 fs**, then **heat 2000–4000 K** in **500 K steps** (**150 ps** per stage, **Berendsen** thermostat **τ = 100 fs**, **Δt = 0.25 fs**, **150 ps** production) to follow **thermal decomposition**.
- **Combustion:** **12** coal molecules plus **250 / 500 / 1000 O₂** (**equivalence ratios φ ≈ 0.5, 1.008, and 2.0**, labeled **fuel-lean, stoichiometric, fuel-rich** in the paper) in **~93×79×69 Å** periodic cells; **10 K minimization (NVE)** then **NVT** heating **2000–4000 K** in **500 K** intervals (**250 ps** per interval, **τ = 100 fs**) to access **combustion** chemistry at accelerated temperatures.

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with **ReaxFF** (`papers/ReaxFF_others/Sanjukta_BrownCoal_Fuel_2014.pdf`). **Systems:** **pyrolysis** cells with **16** literature brown-coal molecules in **~60×56×44 Å** boxes at **ρ = 0.08, 0.10, 0.20 g/cm³**; **combustion** cells as above. **Boundaries:** **3D PBC**. **Ensemble:** **NVE** minimization at **10 K**, then **NVT** heating/production with **Berendsen** thermostat (**τ = 100 fs**). **Timestep:** **0.1 fs** (early equilibration) and **0.25 fs** (heated stages) as stated in Methods bullets above. **Duration:** **10 ps** equilibration (pyrolysis path), then staged heating (**150 ps** per **500 K** step pyrolysis; **250 ps** per **500 K** step combustion). **Barostat / pressure:** **N/A —** **NVT** gas-phase cells; no hydrostatic **NPT** target summarized here. **Temperature:** **2000–4000 K** staged ramps. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** applies a **C/H/O/N/S/B** **ReaxFF** parameterization from the **Castro-Marcano** / **Illinois No. 6** lineage as referenced, without reporting a new fit.

## Findings

- **Combustion** initiates with **thermal fragmentation** of the coal skeleton, followed by **H abstraction** and **O₂** chemistry that produces **large H₂O** counts in the monitored species populations; **gas-phase yields** (CO, CO₂, H₂, H₂O, residual O₂) **depend strongly** on the **three O₂ loadings** (**φ ≈ 0.5, 1.0, 2.0** with **250 / 500 / 1000 O₂** molecules in §2.2).
- **Pyrolysis** vs **combustion** differ in **potential-energy drift** with **temperature** (**exothermic oxidation** vs **endothermic pyrolysis** trends described in the Discussion), and **temperature** effects outweigh **density** effects for the **pyrolysis** cases highlighted.
- **Formaldehyde** appears among **intermediates**, which the authors compare qualitatively to **literature** observations on **oxygenated** pyrolysis/combustion products.

## Limitations

- **Simplified** **coal** **chemistry** and **high-T** **acceleration**; **quantitative** agreement with **experiment** is **partial** and **qualitative**.

## Relevance to group

**Coal** **combustion** **ReaxFF** benchmark in the **Fuel** literature alongside other **fossil** **pyrolysis** entries.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.fuel.2014.07.058` (`papers/ReaxFF_others/Sanjukta_BrownCoal_Fuel_2014.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
