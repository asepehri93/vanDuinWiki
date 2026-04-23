---
id: paper:2020kwon-fuel-279-202-reaxff-based-molecular-2
type: paper
title: "ReaxFF-based molecular dynamics study of bio-derived polycyclic alkanes as potential alternative jet fuels"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:lammps
source_refs: []
doi: "10.1016/j.fuel.2020.118548"
year: 2020
authors:
  - "Hyunguk Kwon"
  - "Aditya Lele"
  - "Junqing Zhu"
  - "Charles S. McEnally"
  - "Lisa D. Pfefferle"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel 279, 118548 (2020)"
pdf_sha256: "b141d1bebb6aab24c9ca372e642975086c052ce273f28e206951bbb3f4a023f1"
pdf_path: "papers/Kwon_Lele_Fuel_2020_Jetfuel.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020kwon-fuel-279-202-reaxff-based-molecular-2 -->

## Summary

This wiki page registers a **second PDF bytes** for the *Fuel* article **DOI [10.1016/j.fuel.2020.118548](https://doi.org/10.1016/j.fuel.2020.118548)** (filename `Kwon_Lele_Fuel_2020_Jetfuel.pdf`); the scientific content is the same peer-reviewed work summarized on **`[[2020kwon-fuel-279-202-reaxff-based-molecular]]`**, which uses the alternate path `Kwon_Fuel_2020_polycyclic_alkanes_jet_fuel.pdf`. The publication investigates **early-stage pyrolysis** of bio-derived **head-to-head polycyclic alkanes** **HtH-1 (C₁₈H₃₂)** and **HtH-2 (C₁₈H₃₄)** as **high energy-density aviation fuel** candidates, using **ReaxFF-based molecular dynamics**. The abstract reports **global Arrhenius** parameters (activation energies and pre-exponential factors) for overall decomposition, a **temperature-dependent** decomposition mechanism from systematic reaction analysis, comparison to fuels such as **JP-10**, product distributions connected to **sooting** tendency, and **binary mixtures** where the two components react largely through **unimolecular** channels with **weak cross-talk**. Retaining two PDFs documents manifest and hashing history; for citation workflows operators should pick **one** canonical file unless both scans are intentionally kept.

## Methods

**Corpus / PDF role.** This slug registers a **second** **PDF** **bytes** for **DOI** **10.1016/j.fuel.2020.118548** (`Kwon_Lele_Fuel_2020_Jetfuel.pdf`); **protocol** **text** and **kinetics** are **the** **same** **peer-reviewed** **work** as **`[[2020kwon-fuel-279-202-reaxff-based-molecular]]`**.

**1 — MD application (ReaxFF pyrolysis, same article as the canonical PDF).** **ReaxFF** reactive **molecular dynamics** in **LAMMPS** for **gas-phase** **pyrolysis** of **HtH-1** / **HtH-2** in **3D** **periodic** **(PBC)** **cells**; **system** **composition** is **O(10²)** **atoms** from **~40** **molecules** per **setup** in the **protocol** **documented** for this **DOI** on **`[[2020kwon-venue-paper]]`** / **`[[2020kwon-fuel-279-202-reaxff-based-molecular]]`**. **Target** **temperature** in **K** and **ρ** (e.g. **1500–3000** **K** and **0.1–0.3** **kg** **dm⁻³** **ranges** in the **galley**-level **notes** **for** **this** **DOI**): use **VOR** **PDF** **(not** **re**-**typed** **here**). **Timestep (fs)**, **equilibration (ps)**, and **production (ns)**: in **the** **same** **source**; **thermostat** (e.g. **Berendsen** **with** **100** **fs** **damping** in **the** **galley** **sibling**); **NVT** **(constant**-**volume** **vapor** **at** **set** **ρ**)**. **Barostat** / **NPT** **/ hydrostatic** **pressure:** **N/A** for **stages** **where** **ρ** is **held** **fixed** **(NVT**-**like**); **N/A** **in** the **thermobaric** **sense** **unless** the **VOR** **adds** **NPT** **(verify** in **VOR**)**. **Duration** in **ps** / **ns**: **see** **Fuel** **article**. **E-field, umbrella, metadynamics, replica** **sampling:** **N/A**.

**2 — Force-field training.** **N/A** (uses an existing **C/H** **ReaxFF**).

**3 — Static QM / DFT as headline.** **N/A**.

## Findings

The abstract and body conclusions are unchanged between PDF copies: **HtH-1** decomposes **faster** than **HtH-2** at the same temperature and density, and both can exceed **JP-10** in the compared decomposition metrics. At **lower** temperature, **central C–C** scission between **cyclohexane** rings dominates for both fuels; at **higher** temperature, **C–CH₃** bond breaking becomes dominant, attributed to **entropy**-favored fragmentation. Major products are **C₅H₈** and **C₄H₈** for **HtH-1**, and **C₄H₈** and **C₂H₄** for **HtH-2**, implying **higher sooting tendency** for **HtH-1**, consistent with experimental measurements quoted by the authors. In **mixtures**, **HtH-1** and **HtH-2** decompose by **unimolecular** reactions with **little intermolecular coupling**. The work is presented as showing how **ReaxFF** can support **pyrolysis** and **combustion** chemistry studies and **kinetic model** development without **a priori** reaction lists.

## Limitations

**ReaxFF** kinetics are empirical; mapping to **flame** chemistry and **soot** formation needs further validation. Maintaining **two PDFs** for one DOI can confuse checksum-based automation—prefer a single canonical blob unless both are required.

## Relevance to group

**Penn State / van Duin-group** contribution to **sustainable aviation** chemistry via **ReaxFF pyrolysis** workflows.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2020.118548](https://doi.org/10.1016/j.fuel.2020.118548)

## Reader notes (navigation)

- Primary curated path: [[2020kwon-fuel-279-202-reaxff-based-molecular]]

## Related topics

- [[2020kwon-fuel-279-202-reaxff-based-molecular]]
- [[reaxff-family]]
