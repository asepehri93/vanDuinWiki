---
id: paper:2016kim-venue-rsc-cp
type: paper
title: "Self-generated concentration and modulus gradient coating design to protect Si nanowire electrodes during lithiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c5cp07219k"
year: 2016
authors:
  - "Sung-Yup Kim"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
  - "Xingcheng Xiao"
  - "Huajian Gao"
  - "Yue Qi"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "c39156578526a5e0bc40526faca587b766bd0c965a0a4f3f57fbb22b6cfe160e"
pdf_path: "papers/Kim_PCCP_2016_LiSiOAl_proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
---

<!-- id:paper:2016kim-venue-rsc-cp -->

## Summary

**ReaxFF reactive MD** in **LAMMPS** simulates **radial lithiation** of **amorphous Si nanowire cores** coated by **amorphous SiO₂** or **Al₂O₃** shells, extending a **Li–Si–Al–O** parameterization from prior work with added **DFT training** data. The study correlates **lithiation rate**, **shell chemistry**, **modulus evolution**, and **fracture** to argue that **Al₂O₃** can develop a **self-generated Li concentration → elastic modulus gradient** that **suppresses stress concentration** versus **SiO₂**.

## Methods

**Force-field training.** **ReaxFF** simulations use an extended **Li–Si–Al–O** description obtained by augmenting the **Narayanan**-family **Li/Si/Al/O** parameter set with additional **DFT** training data for **Li** diffusion barriers, **formation energies**, and **lithiation energies** (**Section 2**).

**MD application (radial lithiation of coated Si nanowires).** Atomistic models place an **amorphous Si** core (**478 Si**, initial mass density **2.38 g cm⁻³**) inside either **amorphous SiO₂** or **amorphous Al₂O₃** shells of initial thickness **2.5, 4.5, or 7.5 Å** around a **~15 Å** core diameter, embedded in **3D periodic** cells of roughly **78 × 53 × 72 Å³** with external **Li** supplied for lithiation. Structures are prepared with **melt–quench** recipes and **NPT** equilibration at **298 K**, followed by energy minimization (tolerance **10⁻⁵ eV** or **2000** steps). Production dynamics run in **NVT** at **900 K** using **LAMMPS** with **velocity Verlet** and **Δt = 0.25 fs** (**ReaxFF** forces). **Barostat** control is **not** applied during the quoted **900 K** production segment (**N/A**). **Thermostat** class for that **900 K** window, **electrostatic cutoffs**, and **QEq** update cadence are **not** restated in the excerpted protocol summary on this page (**N/A** — consult the **PCCP** article). **Shear, shock, or applied electric fields** are **not** part of the lithiation workflow described here (**N/A**).

**Analysis metrics.** The authors track shell boundaries via **innermost/outermost oxide** markers, define **Li_xSi** stoichiometry in the **Si** core, stop insertion at the **x = 3.75** “fully lithiated” condition stated in the paper, and extract **effective Li diffusivity** from **R₀ ∝ √(D_eff t)** scaling (**Table 1**).

## Findings

**SiO₂**-coated nanowires lithiate faster than **Al₂O₃**-coated counterparts in the effective diffusivity metrics in **Table 1** (the article reports roughly a **~4×** trend in that comparison). **SiO₂** shells can fracture and unlock rapid Si expansion, whereas **Al₂O₃** allows more gradual Li ingress while developing a radial Li concentration gradient and a soft-outside / stiff-inside elastic modulus gradient that lowers von Mises stress peaks relative to **SiO₂**; among the thickness and chemistry matrix explored, the **4.5 Å Al₂O₃** case is highlighted as a practical optimum. Shell chemistry (**SiO₂** vs **Al₂O₃**) and initial oxide thicknesses (**2.5 / 4.5 / 7.5 Å**) shift lithiation rate, stress, and failure mode (through-thickness cracking versus delamination-like behavior for thin **Al₂O₃** when gradients weaken). **900 K** production MD accelerates kinetics versus room-temperature cells, so kinetics should be read qualitatively when mapping to devices.

**Corpus note.** Local `pdf_path` is an **RSC proof** PDF—confirm numbers against the *Phys. Chem. Chem. Phys.* version-of-record when auditing tables.

## Limitations

Corpus PDF is an **RSC author proof** (`Kim_PCCP_2016_LiSiOAl_proof.pdf`); use **Phys. Chem. Chem. Phys.** issue pages for final figure/table numbering.
- **High temperature (900 K)** MD accelerates kinetics vs room-temperature operation.

## Relevance to group

**van Duin co-authorship**; demonstrates **ReaxFF** for **artificial SEI / oxide coatings** on **Si anodes** with explicit **mechano-chemical** coupling.

## Citations and evidence anchors

- DOI: [10.1039/c5cp07219k](https://doi.org/10.1039/c5cp07219k) — *Phys. Chem. Chem. Phys.* **18**, 3706–3715 (2016).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
