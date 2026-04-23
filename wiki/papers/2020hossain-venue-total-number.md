---
id: paper:2020hossain-venue-total-number
type: paper
title: "Lithium-electrolyte solvation and reaction in the electrolyte of a lithium ion battery: A ReaxFF reactive force field study (AIP galley proof PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:batteries-interfaces
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
venue: "J. Chem. Phys. (galley proof in corpus)"
pdf_sha256: "e2f3dcf0d7357b70cfddc4d4308497bb9347faeb2b9ca9b8d5a121cd62078d56"
pdf_path: "papers/Hossain_JCP_2020_EC_Li_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020hossain-venue-total-number -->

## Summary

This wiki slug registers an **AIP galley / eProof** PDF (`papers/Hossain_JCP_2020_EC_Li_galley.pdf`) for the same *Journal of Chemical Physics* article summarized on **`[[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]`** (**DOI `10.1063/5.0003333`**). Scientifically, the publication extends **ReaxFF** to **organic carbonate electrolyte** chemistry—species such as **ethylene carbonate (EC)**, **ethyl methyl carbonate (EMC)**, and **vinylene carbonate (VC)** together with **LiPF₆**-related fragments—so that **Li⁺ solvation**, solvent exchange, and **reductive decomposition** near **lithium-metal-like reducing conditions** can be studied with **reactive MD**. A central modeling innovation is to treat **Li⁺** and **neutral Li** within one reactive framework such that both can reproduce similar **solvation energetics** while differing sharply in **chemical reactivity**, enabling the simulation to capture **electron leakage**-like scenarios that form **Li⁰** and trigger **solvent breakdown**.

## Methods

**Force-field training / extension.** **DFT** **reference** **energies** and **reaction** data for **carbonate** and **LiPF\(_6\)**-related fragments enter a **ReaxFF** **parameter** **optimization** / **training** **set**; **validation** against **QM** and (where used) **experiment** follows the **JCP** text. **MD application.** **Molecular dynamics** in **LAMMPS**-class code with **ReaxFF** on **periodic** **PBC** **electrolyte** **supercells** (atom **counts** per the **JCP**); **NVT** **thermostat**; **K**-scale **temperature**; **femtosecond** **timestep**; **nanoseconds** of **sampling** / **equilibration**; **N/A — NPT** **barostat** for typical **constant**-**volume** **boxes**; **N/A** for **GPa** **hydrostatic** **pressure** in those **NVT** runs. **Monte Carlo** **Li⁺/Li⁰** state updates ride on top of standard integration. For exact numbers, use the **VOR** on **[[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]**—this slug is a **galley** **proof** **duplicate** **PDF** for **manifest** provenance.

## Findings

The article argues that **Li⁰** and **Li⁺** can be parametrized to match comparable **solvation energetics** while preserving distinct **reactivity**, and that **decomposition barriers** for carbonate **decomposition** **reaction** **pathways** depend on the **local** **EC** **coordination** of **Li⁰**. **Compared** to fixed-charge **FFs**, the setup targets **anode**-side **reduction** **kinetics** consistent with how **lithium** **electrolyte** work is **benchmarked** in the **battery** **literature**. **Sensitivity** to **EC** **concentration** in the first **solvation** **shell** shifts **barriers** in the model. **Limitations**: **force-field** error vs **DFT**; this **AIP** **galley** is **not** a substitute for the **JCP** **PDF**; use **VOR** sibling. **Open questions** remain for **industrial** **multicomponent** **electrolytes**.

## Limitations

**Galley** PDFs may contain **query blocks**, non-final pagination, or figure placement differences relative to the **volume/issue** PDF; prefer **`[[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]`** for stable reader navigation.

## Reproducibility notes

Battery-electrolyte ReaxFF work should always record **salt concentration**, **Li⁺/Li⁰** switching schedule, **cutoffs**, and **charge update** frequency, because anode-side decomposition is sensitive to local **EC** coordination and electric-field approximations implicit in classical cells. When reproducing decomposition barriers, compare against the **final** JCP tables rather than galley placeholders, and cross-check any **Monte Carlo** state-change acceptance statistics reported in the SI. **Galley** query sheets may omit final **supporting-information** pointers; verify SI filenames against the published article landing page.

## Relevance to group

Duplicate ingest for provenance; use **`2020hossain-j-chem-phys-lithium-electrolyte-solvation`** for primary navigation.

## Citations and evidence anchors

- DOI: [10.1063/5.0003333](https://doi.org/10.1063/5.0003333)

## Related topics

- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

