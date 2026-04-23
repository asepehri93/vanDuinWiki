---
id: paper:2018joseph-p-abrahamson-the-earliest-trajectories-graphitizable
type: paper
title: 'Trajectories of graphitizable anthracene coke and non-graphitizable sucrose char during the earliest stages of annealing by rapid CO\(_2\) laser heating'
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.3390/c4020036"
year: 2018
authors:
  - "Joseph P. Abrahamson"
  - "Abhishek Jain"
  - "Adri C. T. van Duin"
  - "Randy L. Vander Wal"
venue: "J. Carbon Res."
pdf_sha256: "fd700278b5d85b3989f4c46715e1e24123a6875cf2b8d374dc77090da7c36136"
pdf_path: "papers/Abrahamson_J_Carb_Res_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018joseph-p-abrahamson-the-earliest-trajectories-graphitizable -->

## Summary

**CO\(_2\)** **laser** heating (**1200–2600 °C**, **0.25–300 s**) vs **1 h** **furnace** routes compares **graphitizing** **anthracene coke** vs **non-graphitizing** **sucrose char** during early **carbonization**. **TEM** tracks **nanostructure**; **anthracene** **graphitizes faster**. **Sucrose char** passes through **closed-shell** **fullerenic** **nanoparticles** that **open** on further heating, producing **pores**; **odd-membered rings** are argued **present initially** rather than generated only by **annealing**. **ReaxFF MD** simulates **shell unraveling** for the **sucrose**-derived structure. The study connects **graphitizability** distinctions in **carbon** **materials science** to **nanoscale** **curvature** and **defect** topologies that precede **long-range** **graphitic** **ordering** (introduction themes).

## Methods

- **Materials:** **Anthracene** vs **sucrose** precursors **carbonized** in **tube bomb** (**500 °C**, **5 h**, **~6.9 MPa** autogenous pressure).
- **Furnace:** **Ar**; **25 °C/min** to **1200** or **2600 °C**, **1 h** holds.
- **Laser:** **250 W** **CW CO\(_2\)** laser, **pulse-width** **modulated** power; **multi-wavelength pyrometry** + **LII**/**TTH** spectroscopy for **temperature** histories; **TEM** (**FEI Talos 200 kV**); **XRD** **d\(_{002}\)**, **Scherrer** **L\(_a\)/L\(_c\)** where applicable.
- **ReaxFF MD (atomistic fragment):** **LAMMPS** **ReaxFF** on a **2250-atom** **sucrose-char-inspired** **fullerenic** **shell** using the **CHO** **combustion** **ReaxFF** extension cited in the article; **energy minimization** then **NVT** heating with a **Berendsen** thermostat to **~3327 °C**; **0.1 fs** timestep (see **PDF** for staging in **ps**/**ns**).

- **Cross-validation:** authors compare **laser**-heated **trajectories** to **furnace** **holds** by mapping comparable **integrated** **temperature–time** exposure to argue **kinetic** vs **thermodynamic** control of **ordering** (methods narrative).

**Additional controls.** **PBC:** **three-dimensional PBC** for the **cluster** supercell as in standard **LAMMPS** setups unless the article specifies isolation. **Barostat / bulk pressure:** **N/A — NPT** not used for the **ReaxFF** heating segment summarized. **Electric field:** **N/A — laser** heating is **thermal**; no **EFIELD** bias in the quoted protocol. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not reported for this illustrative **MD**.

## Findings

**Outcomes.** **Laser** anneals reach comparable **end-state** **nanostructures** to **furnace** holds when **temperature–time** integrals match, but **laser** exposes **faster** early **kinetics**. **Graphitizable** **anthracene** **coke** **orders** more rapidly than **non-graphitizable** **sucrose** **char** under similar programs.

**Mechanisms.** **Sucrose** **char** passes through **closed** **fullerenic** **shells** that **open** to **porous** **morphologies**; **odd-membered** rings are argued to be present early, not only as **annealing** products. **ReaxFF** trajectories show **shell unraveling** consistent with the proposed bottleneck before extended **graphene** **stacking**.

**Comparisons.** **TEM** **micrographs** and **XRD** metrics (**d\(_{002}\)**, **Scherrer** widths) **benchmark** the **simulation** narrative.

**Sensitivity / limitations.** **Heating rate**, peak **temperature**, and **hold** **time** shift **graphitization** extent; **ReaxFF** **carbon** chemistry and the single **fragment** model are **approximate**—confirm all **numbers** in **`pdf_path`**.
## Limitations

**ReaxFF** **carbon** chemistry transferability; **single** **atomistic** **model** for **complex** **char**; **laser** **heating** heterogeneity.

**Experimental** **comparison** should account for **spatial** **gradients** in **laser**-heated **foils** that are **averaged** differently than **furnace** **isothermal** holds—see **temperature** **diagnostics** in the **PDF**.

**Carbonization** **literature** context: distinguishing **graphitizing** vs **non-graphitizing** **precursors** remains central to **carbon** **fiber** **processing**; this work adds **time-resolved** **laser** **access** to **early** **annealing** stages (introduction framing).

## Relevance to group

**van Duin-group** **ReaxFF** on **carbonization** paired with **Penn State** **experimental** **laser** **kinetics**.

## Citations and evidence anchors

- DOI: `10.3390/c4020036`.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
