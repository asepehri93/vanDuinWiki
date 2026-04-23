---
id: paper:2021penrod-j-chem-phys-using-c-dft
type: paper
title: "Using C-DFT to develop an e-ReaxFF force field for acetophenone radical anion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:ereaxff
  - method:dft-static
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
candidate_tags: []
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
venue: "J. Chem. Phys. 155, 214104 (2021)"
pdf_sha256: "b1e89d2f13d00d2e2e53f934d0cac5c885bf77eaf441909572dee7a0275976ae"
pdf_path: "papers/Penrod_Burgess_JCP_Acetophenon_eReaxFF_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021penrod-j-chem-phys-using-c-dft -->

!!! abstract "Scope"
    e-ReaxFF extension for the acetophenone radical anion using **constrained DFT (C-DFT)** targets on each atomic center, building on the 2021 Akbarian e-ReaxFF parameterization for cross-linked polyethylene (XLPE) chemistry.

## Summary

Cross-linking polyethylene with dicumyl peroxide yields XLPE for high-voltage cable insulation but also by-products such as acetophenone, which has favorable electron affinity. The paper develops an e-ReaxFF description of the acetophenone radical anion for use in reactive molecular dynamics of degradation chemistry. Starting from the existing XLPE-oriented e-ReaxFF parameter set, the authors run C-DFT geometry optimizations with the excess electron constrained separately to each atom of acetophenone, add the resulting energies to the e-ReaxFF training set, and iteratively refit until e-ReaxFF reproduces the C-DFT data. They compare equilibrium populations from energy-minimized structures between C-DFT and e-ReaxFF across temperatures, and they test MD by comparing e-ReaxFF electronic distributions to unconstrained-DFT spin densities.

## Methods

**Static QM (C-DFT for eReaxFF training).** *Constrained DFT* (C-DFT) **geometry optimizations** place the **excess electron** of the **acetophenone radical anion** on **each heavy-atom center in turn**, yielding **site-resolved** energies that standard **unconstrained** DFT would **over-delocalize**. The full **functional**, **dispersion**, and **basis** specifications are in *J. Chem. Phys.* **155**, 214104.

**Force-field training (eReaxFF extension).** The **eReaxFF** description extends the **2021 Akbarian eReaxFF** parameterization used for **XLPE**-related **chemistry**. Constrained-DFT **total energies and geometries** enter the **eReaxFF** training set; the parameters are **reoptimized** until **RMS** agreement is acceptable (least-squares / **Monte Carlo** updates as described for **eReaxFF** in the paper). **Unconstrained** DFT **VASP** **spin densities** provide an independent check on **charge/spin** distributions; covalent chemistry *outside* the **acetophenone** **fragment** is not refit here.

**MD application (eReaxFF in LAMMPS).** **eReaxFF** **molecular dynamics** in **LAMMPS** compares **trajectory-averaged** on-site **electronic populations** to **unconstrained** DFT **spin** **density** **maps** for the **radical anion**. The letter reports **NVT** sampling with a **Nosé–Hoover**-type **thermostat**; **time step, temperature list, and equilibration vs production** durations are in Section 2 of the *JCP* issue and the **SI**. **Barostat — N/A** in the **highlighted** **NVT** validation blocks. **Hydrostatic pressure (bar) — N/A** as an **independent** **MD** **control** in these **NVT** **demonstrations** (fixed **cell** **volume** for the **stated** **tests**). **Static external electric field in MD — N/A**. **PBC** and **box** details for the **acetophenone** test cells: **see** the article and **SI**. **Shock, shear, metadynamics — N/A** for the stated eReaxFF tests.

## Findings

**Fitting and thermodynamics.** The refitted **eReaxFF** set reproduces the **C-DFT** site energies well enough to close the training loop, and the paper reports **multi-temperature** mixture behavior consistent with the same **C-DFT** references (see tables and discussion in the **VOR**).

**MD validation.** **Trajectory-averaged eReaxFF** on-site **electronic** weights **qualitatively** track **unconstrained** DFT **spin-density** **features** for the **radical anion**, supporting the intended use in larger **ReaxFF+eReaxFF** **insulation**-chemistry **models**.

**Sensitivity and scope.** The study varies **temperature** in the eReaxFF tests it reports; it does not benchmark **cable** **aging** in a **laboratory** under **high field**. The **JCP** text limits **claims** to the **acetophenone** **radical** **anion** in the **XLPE**-aligned **chemistry** space—**not** a full **cable**-additive or **electrolyte** **eReaxFF** fit (see **## Limitations** and the article Discussion).

## Limitations

The study focuses on acetophenone and its radical anion in the stated electronic-structure approximations; broader electrolyte or cable additives are outside the demonstrated training set. **Corpus** **note:** long **XLPE** **insulation** **field** **biases** and **real** **electrolyte** **solutions** are **not** **parameterized** **by** this **C-DFT**+**eReaxFF** **fragment** **alone**; **see** `pdf_path` **Discussion** **for** **outlook**.

## Relevance to group

Extends e-ReaxFF for high-voltage polymer insulation chemistry with explicit charge-localization training via C-DFT.

## Citations and evidence anchors

- DOI: [10.1063/5.0064705](https://doi.org/10.1063/5.0064705)

## Related topics

- [[reaxff-family]]
