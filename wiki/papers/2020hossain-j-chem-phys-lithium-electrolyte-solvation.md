---
id: paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation
type: paper
title: "Lithium-electrolyte solvation and reaction in the electrolyte of a lithium ion battery: A ReaxFF reactive force field study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0003333"
year: 2020
authors:
  - "Md Jamil Hossain"
  - "Gorakh Pawar"
  - "Boryann Liaw"
  - "Kevin L. Gering"
  - "Eric J. Dufek"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 152, 184301 (2020)"
pdf_sha256: "231221cee087887ad21069d25969689ef4e9868cd8d1eaa27af75711e788734b"
pdf_path: "papers/Hossain_JCP_2020_EC_Li.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation -->

## Summary

This JCP paper extends ReaxFF to **organic carbonate electrolyte** species (e.g., EC, EMC, VC) and LiPF6-related chemistry so that Li solvation, solvent exchange, and decomposition pathways near reducing anode conditions can be studied reactively. DFT data on Li-associated initiation reactions and solvation structures augment the training set; the parametrization introduces distinct treatments so that **Li⁺** and **neutral Li** can reproduce similar solvation energetics while differing in chemical reactivity—neutral Li drives electrolyte decomposition, modeled with a Monte Carlo-style charge/state update compatible with ReaxFF dynamics. Decomposition barriers depend on EC coordination number around neutral Li.

Broader framing in the article highlights that **SEI** formation from organic carbonate reduction at graphitic anodes requires models that distinguish **Li⁺** solvation from **Li⁰** chemistry, because nonreactive force fields cannot follow bond-breaking sequences that set onset potentials and product distributions in electrolyte decomposition.


## Methods

**Training data (DFT).** **DFT** reference data cover **Li-associated initiation** reactions for **organic carbonate** electrolytes and **binding energies** of **Li–electrolyte** solvation structures, merged into the broader **ReaxFF** training set for optimization.

**Species scope.** Parameter extension targets **ethylene carbonate (EC)**, **ethyl methyl carbonate (EMC)**, **vinylene carbonate (VC)**, and **LiPF₆**-related chemistry (as stated in the abstract).

**Li⁺ vs Li⁰ representation.** A **second Li parameter set** describes **Li⁺**; **ReaxFF** is trained so **neutral Li** and **Li⁺** reproduce **similar solvation energies**, but only **neutral Li** initiates **reactive** decomposition of solvent—mirroring the physical picture that **Li⁺** is chemically inert toward bond-breaking in the same way as **Li⁰** in the parametrization.

**Reduction / reactivity trigger.** **Solvent decomposition** is accessed after **Li⁺ → Li⁰** reduction using a **Monte Carlo–type atom modification** within the **ReaxFF** dynamics framework (per abstract).

**Reactive MD.** **Molecular dynamics** in **LAMMPS**-class integration with **ReaxFF** on **finite** electrolyte **cells** (thousands of **atoms** per **supercell** as in the paper); **NVT** **thermostat**-controlled **temperature** (**K**-scale targets in the paper); **femtosecond** **timestep**; **nanoseconds** of **sampling** / **equilibration** and **production**; **PBC** for **bulk**-like liquid; **N/A — NPT** **barostat** if runs are **constant volume**; **N/A** for **GPa** **pressure** in typical **NVT** electrolyte boxes. **N/A** for static **MV/cm** **electric** **field** applied across the cell in the same sense as continuum battery models—the work uses a **Monte Carlo**-style **Li⁺/Li⁰** state change for reduction chemistry. **N/A — metadynamics**.

## Findings

**Dual-state fidelity.** The fitted potential **distinguishes Li atom vs Li⁺** so **anode-side** reduction chemistry can be represented without collapsing both into a single nonphysical state.

**Barrier–solvation coupling.** **Decomposition reaction barriers** depend on how many **EC** molecules **solvate** the **neutral Li atom**—highlighting **local solvation number** as a control on **reduction** kinetics in the model.

**SEI context.** The work supports **SEI**-relevant narratives where **electron leakage** to electrolyte reduces **Li⁺** to **reactive Li⁰**, triggering **organic carbonate** **decomposition** pathways that fixed-bond models cannot follow.

**Compared** to **nonreactive** **FFs**, the model **agrees** in spirit with **literature** that **reduction** chemistry requires **reactive** sampling. **Sensitivity** to **EC** **coordination** around **Li⁰** controls **reaction** **barriers** and thus **kinetics**. **Limitations** include **transfer** to full **electrolyte** **mixtures**; **caveat**: **ReaxFF** is **empirical**—**future** **benchmarks** against more **DFT** **pathways** may be needed. **No** **galley**-only **PDF** is required to read the published **article**; use **VOR** for **pagination** if your tree has a **proof** **duplicate** slug for the same DOI.

## Limitations

- Complex commercial electrolyte mixtures and long-time SEI evolution require careful interpretation; parameter transfer should be checked when moving to new salts or additives. For **exact** **barriers**, **Monte Carlo** **acceptance** **rules**, and **table** **values**, use the **JCP** **pdf** and **SI**; this page is a **curated** **summary**, not a substitute for those sources.

## Relevance to group

Central reference for **Li-ion electrolyte reactivity** with ReaxFF at PSU/INL collaboration—connects to SEI formation narratives in the battery literature.

## Citations and evidence anchors

- DOI: [10.1063/5.0003333](https://doi.org/10.1063/5.0003333)
- Abstract: `normalized/extracts/2020hossain-j-chem-phys-lithium-electrolyte-solvation_p1-2.txt`

## Reader notes (navigation)

- Pairs with **solid electrolyte** parameterization ([[2018shin-physical-che-development-reaxff]]) to show **two regimes**: ceramic lattice transport vs **organic** bond chemistry at the anode.  
- **Theme:** [[batteries-interfaces-reaxff]]; **workflow:** [[reaxff-parameterization-workflow]].  
- **Frozen eval:** FF2, BAT1 in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
- Carbonate electrolytes, Li⁰ vs Li⁺ chemistry, and anode-side decomposition
- ReaxFF parameterization for organics containing Li, P, F
