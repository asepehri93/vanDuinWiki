---
id: paper:2015joshi-venue-paper
type: paper
title: "Reactive simulations-based model for the chemistry behind condensed phase ignition in RDX crystals from hot spots"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:energetic-materials
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nve-simulation
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1039/C5CP00950B"
year: 2015
authors:
  - "Kaushik L. Joshi"
  - "Santanu Chaudhuri"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "457b81433f591af5dd05a2cdfdcb23ad057feceeee5c482dae10ce9ca7b1bc2e"
pdf_path: "papers/ReaxFF_others/Joshi_RDX_PCCP_2015_JustAccepted.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015joshi-venue-paper -->


!!! abstract "Note on the PDF"
The corpus PDF is a **Royal Society of Chemistry Accepted Manuscript** (pre-technical editing). Scientific claims below follow this file and the abstract text.

## Summary

Reactive molecular dynamics with **ReaxFF** is used to study **condensed-phase ignition** of **high-pressure γ-RDX** after localized **thermal hot spots** are created by heating a small fraction of the crystal. After the pulse, dynamics continue under **adiabatic (NVE)** integration so incubation and runaway reflect exothermic chemistry rather than fixed-temperature constraints. The paper’s central claim is that **condensed-phase** pathways differ qualitatively from common **gas-phase** unimolecular pictures for nitramines: hydrogen-transfer chemistry and **polyradical** intermediates matter before **NO₂**-first mechanisms dominate.

## Methods

- **Crystal phase and cell:** **γ-RDX** at experimental density **~2.26 g cm⁻³**; unit cell from **CASTEP** **PBE** **DFT-D** relaxations, then **ReaxFF** relaxation; supercell **4×4×4** (**512** RDX molecules, ~**50.24×37.92×43.68 Å**).
- **Hot-spot protocol:** Central region (**~5%** by volume, **24** molecules) receives a **thermal pulse** at **1000 K** or **2000 K** for **5–40 ps**; during the pulse the hot zone uses **NVT** (**1000 K** or **2000 K**) while the remainder is **NVE**; after the pulse the **entire system** is **NVE**. Initial equilibration **300 K**, **100 000** steps, **Δt = 0.01 fs**; production **Δt = 0.01 fs** throughout.
- **Force field / code:** **ReaxFF** in **LAMMPS**, combining the **Wood et al.** nitramine **CHNO** set with **C/H/O combustion** training (**Chenoweth et al.**); **original ReaxFF** form (not **ReaxFF-lg**) as stated for dense γ-RDX combustion chemistry.
- **PBC / ensembles:** **3D periodic** **γ-RDX** supercell. During the pulse, the **hot zone** is held at **1000 K** or **2000 K** with **NVT** while the remainder is **NVE**; after the pulse the **entire** system runs **NVE** at fixed volume. The **NVT** subregion implements **thermostat**-like **temperature** control as described in the **PCCP** **Methods** for their **LAMMPS** setup. **Barostat / applied pressure:** **N/A —** not used in this fixed-cell hot-spot protocol.

## Findings

Longer **thermal pulses** on the **central hot zone** favor an **incubation** period followed by **thermal runaway**; shorter pulses let the cell re-equilibrate without ignition within the simulated window. During incubation, **inter- and intramolecular hydrogen transfer** dominates, while **N–N** scission to **NO\(_2\)**—typical of gas-phase **unimolecular** nitramine pictures—is **suppressed** in this **dense γ-RDX** setup. **Polyradicals** retaining **triazine** rings accumulate before **ring-opening** chemistry accelerates exothermic release of **N\(_2\)**, **H\(_2\)O**, and **CO\(_2\)**. The authors stress **finite system size**, **picosecond–nanosecond** horizons, and the idealized **hot-spot** protocol versus **shock** or **laser** energy deposition. This note tracks the **Just Accepted** PDF in `pdf_path`; use the **issue-of-record PCCP** PDF for stable **figure** numbering.

## Limitations

Accepted-manuscript formatting; finite system size and short timescales; hot-spot protocol is a stylized stand-in for laser/shock initiation. Validation against higher-level electronic structure is described only at selected points in the paper. The **γ-RDX** crystal setup and **adiabatic** continuation are idealizations relative to real defects, voids, and multi-crystal textures in pressed formulations.

## Relevance to group

Illustrates **ReaxFF** applied to **nitramine** condensed-phase ignition chemistry and **hot-spot**–to–**runaway** sequencing. Complements other **energetic materials** reactive MD notes in the KB that emphasize **gas-phase** kinetics instead of **condensed** hydrogen-transfer sequences.

## Citations and evidence anchors

DOI `10.1039/C5CP00950B`.

## Related topics

- [[reaxff-family]]
