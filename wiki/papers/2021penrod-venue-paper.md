---
id: paper:2021penrod-venue-paper
type: paper
title: "Using C-DFT to develop an e-ReaxFF force field for acetophenone radical anion (publisher proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:ereaxff
  - method:dft-static
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:polymer
source_refs: []
doi: "10.1063/5.0064705"
year: 2021
authors:
  - "Katheryn A. Penrod"
  - "Maximiliano Aldo Burgess"
  - "Dooman Akbarian"
  - "Ismaila Dabo"
  - "W. H. Hunter Woodward"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. (proof); same DOI as VOR"
pdf_sha256: "32f1ab142465e89dd2b358c97d434d61519fd3c25ff1a4d66170005ee0efd9c3"
pdf_path: "papers/Penrod_Burgess_JCP_Acetophenon_eReaxFF_galley_2021.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021penrod-venue-paper -->

!!! note "Corpus PDF role"
    **AIP author proof / query** PDF. Full **typeset** article text and figures for **DOI `10.1063/5.0064705`** are on **[[2021penrod-j-chem-phys-using-c-dft]]** (`Penrod_Burgess_JCP_Acetophenon_eReaxFF_2021.pdf`). This slug’s **`extraction_quality`** reflects **proof** layout.

## Summary

**Cross-linked polyethylene (XLPE)** insulation for high-voltage cables can release **acetophenone** as a **by-product** of **peroxide** curing; the molecule has favorable **electron affinity**, motivating reactive simulations of its **radical anion** in **degradation** chemistry. **e-ReaxFF** extends **ReaxFF** with **explicit electronic** degrees of freedom for **charge-localized** states. Starting from the **2021** **Akbarian** **e-ReaxFF** parameterization oriented toward **XLPE** chemistry, this work uses **constrained DFT (C-DFT)** to place the **excess electron** on **each atomic center** of **acetophenone** in turn, collects **geometry-optimized** **energies** into the **e-ReaxFF** training set, and **iteratively refits** until the force field reproduces the **C-DFT** targets. The authors compare **equilibrium populations** from **energy-minimized** structures across **temperatures** and run **MD** to compare **e-ReaxFF** **electronic distributions** to **unconstrained** **DFT** **spin densities**. The intent is a **transferable** fragment description that can be embedded in larger **polymer** **oxidation** and **space-charge** modeling workflows without full **QM** on every timestep.

Methodological motivation is that **acetophenone** radical anions are **resonance-stabilized** and can **delocalize** under standard **DFT**, so **C-DFT** center constraints supply diabatic **site** energies that **e-ReaxFF** can fit without ambiguous delocalized references.


## Methods

The **`papers/Penrod_Burgess_JCP_Acetophenon_eReaxFF_galley_2021.pdf`** is an **AIP** **author** **proof**; **citable** **version-of-record** text, **pagination**, and **display** **equations** live on **[[2021penrod-j-chem-phys-using-c-dft]]** (`Penrod_Burgess_JCP_Acetophenon_eReaxFF_2021.pdf`).

**Methods (VOR is authoritative).** The **AIP** version-of-record and **[[2021penrod-j-chem-phys-using-c-dft]]** give the citable protocol: **C-DFT** training data, **eReaxFF** refit on the **2021 Akbarian** parent, and **NVT eReaxFF molecular dynamics** in **LAMMPS** on **periodic acetophenone-centered** supercells (**time step in fs**, **temperatures in K**, run lengths: **Section 2** + **SI**; **Nosé–Hoover**-class **thermostat** on the **VOR**). This **proof** path is **N/A** for line-by-line re-keying; use the **VOR** + **SI** for **fs**/**ps** settings, **NPT** (if present in **SI**), and **PBC** details. **Hydrostatic pressure (bar) — N/A** in the **NVT** **demos** highlighted in the **letter**. **E-field, umbrella, shock — N/A** in the **NVT eReaxFF** demos as described on the **VOR** page.

## Findings

**Practical (corpus).** **`pdf_sha256`** on this **slug** **differs** from the **VOR** file; use **[[2021penrod-j-chem-phys-using-c-dft]]** for **hash-locked** **ingest** **and** **bibliography** tied to the **AIP** **version**-**of**-**record** **PDF**.

**Outcomes and comparisons.** The **VOR** reports that **C-DFT**-aligned **eReaxFF** reproduces **constrained** **energetics** and that **NVT** **eReaxFF** **trajectories** match **unconstrained** DFT **spin-density** **features** at the level **discussed** in the **JCP** paper. **Lab** **cable** **field-cycling** is **not** a **benchmark** here. **Scope:** the **VOR** **Discussion** keeps **claims** to the **acetophenone** **radical** **anion** **fragment** under the stated **approximations**; **for** **numbers**, use the **VOR**+**SI**, not **this** **galley** for **pagination**.

## Limitations

Scope is **acetophenone** and its **radical anion** under the stated **DFT** approximations; broader **cable** **additives** and **electrolyte** environments are **not** parameterized here. **Proof-PDF** may lack final **pagination** and **figure** quality versus **[[2021penrod-j-chem-phys-using-c-dft]]**.

## Reader notes (navigation)

- Version-of-record PDF page: **[[2021penrod-j-chem-phys-using-c-dft]]**
- [[reaxff-family]]
