---
id: paper:2022jacobson-jcis-open-8-effect-nanoconfinement
type: paper
title: "Effect of nanoconfinement and pore geometry on point of zero charge in synthesized mesoporous siliceous materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - task:experiment-integrated
  - material:silicate-glass
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.jciso.2022.100069"
year: 2022
authors:
  - "Andrew T. Jacobson"
  - "Chen Chen"
  - "Janet C. Dewey"
  - "Grant C. Copeland"
  - "Wayne T. Allen"
  - "Bryony Richards"
  - "John P. Kaszuba"
  - "Adri C.T. van Duin"
  - "Hyeyoung Cho"
  - "Milind Deo"
  - "Yuqi She"
  - "Thomas P. Martin"
venue: "JCIS Open"
pdf_sha256: "8c435d56c6f4a7bff6d4ce92b6583fe8af54dac238fca704d30f98e9d644d39a"
pdf_path: "papers/Jacobsen_Chen_silica_PoZ_JCIS_open_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022jacobson-jcis-open-8-effect-nanoconfinement -->

## Summary

**Point of zero charge (PZC)** and **surface acidity** control adsorption, film stability, and electrostatic corrections in porous **silica**–**water** systems, yet published **PZC** values for nominally similar materials scatter widely in the literature. This **JCIS Open** article combines **potentiometric titrations** on **synthetic mesoporous silicas** (**SBA-15**, **SBA-16**, **MCM-41**) with **ReaxFF molecular dynamics** models of **amorphous silica** to ask whether **nanoconfinement** or **pore geometry** (cylindrical versus cage-like motifs) systematically shifts **PZC** once experimental protocols are controlled. Pore sizes around **4–13 nm** bracket common **mesopore** regimes relevant to catalysis and subsurface **shale**-like confinement narratives. Electrolytes were **pre-saturated with silica** to reduce bulk **dissolution** artifacts during measurement. The study also contextualizes results against a broad literature compilation (**>150** studies) to interpret scatter versus true physical effects.

## Methods

Experimentally, the authors perform **potentiometric titrations** and extract **PZC** and **pK** descriptors for each archetype under silica-saturated fluid conditions, comparing across **pore geometry** and **diameter** as described in the article. Computationally, **ReaxFF** simulations estimate **surface equilibrium constants** / charging response for **amorphous silica** models, linking molecular-scale **deprotonation/protonation** behavior to macroscopic **PZC** trends. A **meta-analysis** aggregates published **PZC** measurements for porous and nonporous silicas to separate protocol-induced variability from material trends. Together, the workflow aims to couple **reactive interface MD** with **careful wet chemistry** on well-characterized powders.

**ReaxFF MD (simulation block in the article):** **Engine: LAMMPS** **ReaxFF**; **amorphous** **silica** **slabs** with **explicit** **water**/**hydronium**/**hydroxide** in **3D** **PBC**; **NVT**-class **integration** with **thermostat** and **~fs** **timestep**; **ps**–**ns** **trajectories** to sample **proton** **transfer** and **surface** **pK**-related **populations**; **room-temperature** **(300 K)** or the **T** in *JCIS Open*; **barostat** **N/A** if **constant** **volume**; **hydrostatic** **pressure** **N/A**; **external** **electric** **field** **N/A**; **umbrella**/**replica** **exchange** **N/A**; **cutoffs** and **QEq**-style **electrostatics** per **Methods**.

## Findings

**ReaxFF** is used to rationalize the **wide spread** of **PZC** values reported for **macroporous/nonporous** silicas when laboratories differ in **ionic strength**, **pretreatment**, and **equilibration** history. For the **mesoporous** materials studied (**SBA-15**, **SBA-16**, **MCM-41**), the combined dataset does **not** resolve a **PZC shift** attributable to **nano-confinement** or **pore geometry** within the experimental and modeling resolution reported. The practical implication stated in the framing is that **surface charging** models in **mesopores** may not require an ad hoc **confinement correction** to **PZC** for these synthetic silicas—while still cautioning that **natural** geomaterials can differ due to **impurities**, **clays**, and **roughness** not captured in idealized powders. The study’s design—**controlled synthesis** plus **silica-saturated** electrolytes—aims to reduce artifacts that historically inflate **PZC** scatter in the literature, making the “no shift” conclusion a statement about **well-controlled mesopores** rather than all nanoporous media. Together, the experimental sweep across **SBA-15**, **SBA-16**, and **MCM-41** and the ReaxFF interpretation of **amorphous silica** acidity aim to separate **pore shape** effects from **surface chemistry** effects that can masquerade as confinement in poorly controlled datasets. For **geoscience** readers, the manuscript’s caution is explicit: **mesoporous** **synthetic** silicas are not **shale** microstructures, but if **PZC** is stable across these well-defined pores, then **confinement-first** explanations for **PZC** shifts elsewhere merit extra scrutiny.


## Limitations

Synthesis heterogeneity (defects, hydration layers, residual surfactant chemistry) can mask small shifts; natural shales and reservoir rocks require case-specific validation.

## Relevance to group

Joint **ReaxFF** + **experiment** study with **van Duin** authorship on **silica–water** geochemical interfaces.

## Citations and evidence anchors

- DOI: [10.1016/j.jciso.2022.100069](https://doi.org/10.1016/j.jciso.2022.100069)

## Related topics

- [[reaxff-family]]
