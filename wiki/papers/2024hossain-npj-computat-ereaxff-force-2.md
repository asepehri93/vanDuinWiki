---
id: paper:2024hossain-npj-computat-ereaxff-force-2
type: paper
title: "eReaxFF force field development for BaZr0.8Y0.2O3-delta solid oxide electrolysis cells applications"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - material:perovskite-oxide
  - domain:oxides-ceramics
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-024-01268-9"
year: 2024
authors:
  - "Md Jamil Hossain"
  - "Prashik Gaikwad"
  - "Yun Kyung Shin"
  - "Jessica A. Schulze"
  - "Katheryn A. Penrod"
  - "Meng Li"
  - "Yuxiao Lin"
  - "Gorakh Pawar"
  - "Adri C. T. van Duin"
venue: "npj Computational Materials (2024)"
pdf_sha256: "760fe7bec2addef75d890e030f5e69c3bfce6de65dff40fe78ffc3458d9f9057"
pdf_path: "papers/Hossain_eReaxFF_YSZ_npjCompMat_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024hossain-npj-computat-ereaxff-force-2 -->

## Summary

This corpus PDF is an **uncorrected proof** galley of the npj Computational Materials article on eReaxFF for BZY20 solid-oxide electrochemistry (same DOI as the version-of-record file paired as `2024hossain-npj-computat-ereaxff-force`). Scientific content matches that publication: eReaxFF training to DFT/C-DFT for vacancies, water reactions, and explicit-electron effects, plus large-scale AMS/LAMMPS-style simulations of steam on BZY20 surfaces.

Galley PDFs sometimes differ in pagination, line breaks, and figure placement; operators should cite locator-independent quantities (reaction labels, barrier heights, supercell stoichiometries) from whichever file is designated canonical after manifest review.

## Methods

**QM fitting targets** mirror the VOR article: **bulk BZY20** Y-doping preference (**Type 3**), **oxygen-vacancy** energies in bulk and on **(100)/(110)** slabs (**Ba-O** vs **Zr-Y-O** terminations; surface vacancies up to **25%** in supercells), **EOS**, **H2O** adsorption/splitting, **H2** release energetics, and **C-DFT** excess-electron localization and migration barriers on cluster models. **eReaxFF** balances reproduction of **relative** energies and **structural** metrics; absolute vacancy formation energies are described as qualitatively tracked.

**Atomistic simulations** use the fitted eReaxFF with **ACKS2** charges and optional **explicit electrons**; **bond-biased** scans estimate adsorption, water-splitting, and **H2** formation barriers. **Production MD** (e.g. **~3000-atom**, **1000 K**, **NVT**, repeated **H2O** dosing) probes **vacancy filling**, **proton hopping** into the bulk, and **bias-assisted H2** pathways; galley pagination differs, but equations and numerical examples align with the journal PDF.

Training prioritizes reproducing the ordering of surface elementary steps and proton-electron coupling trends needed for electrolysis modeling rather than perfect absolute formation energies for every oxygen vacancy configuration.

**1 — MD / 2 — Force-field** details align with the **VOR** article’s **Methods**; this **proof PDF** is not the preferred citation for **page** numbers. **RMD** examples use **AMS**/**eReaxFF** **molecular dynamics** as in the VOR: **3D PBC** **metallic-oxide** **slabs**, **NVT** **kinetics** of **H2O** at **~1000 K**, **~1.4 ns**-scale cumulative **steam** exposure, **0 GPa** external **hydrostatic** target (**N/A** to **NPT** **Parrinello** barostats in the same excerpt). For **timestep**, **Langevin**/**Nose** thermostat, and per-segment **ps**/**ns** **duration**, use **`2024hossain-npj-computat-ereaxff-force`**. **3 — Static-only QM** as standalone primary claim: **N/A**—**DFT** is in service of **eReaxFF** training, as in the sibling page.
## Findings

The proof reports the same core validation outcomes as the article: **Type 3** doping stability, **EOS** agreement, semiquantitative **Ov** trends, **surface** reaction-energy ordering (**Zr-Y-O** vs **Ba-O** terminations), **high thermal barriers** for **H2** evolution without bias, **lowering** of barriers when **excess electrons** or **H-H bond biasing** stand in for applied voltage, and **long MD** showing **subsurface proton transfer** without **H2** in zero-bias steam simulations. Use **`2024hossain-npj-computat-ereaxff-force`** for page-cited reading when possible.

Readers should interpret explicit-electron and biased-bond workflows as mechanistic analogues of electrochemical driving force, not literal constant-voltage continuum boundary conditions. For **kcal/mol** and **reaction** labels, prefer the **version-of-record** wiki page and **PDF** (`2024hossain-npj-computat-ereaxff-force`).
## Limitations

Proof PDFs can diverge slightly from the final layout; any figure numbering referenced externally should be checked against the journal version-of-record PDF linked by DOI.

## Relevance to group

Co-authored **eReaxFF** development for proton-conducting perovskite electrolytes with **Adri C. T. van Duin**, supporting solid-oxide electrochemistry and interface simulation threads in the KB.

## Citations and evidence anchors

- DOI: [10.1038/s41524-024-01268-9](https://doi.org/10.1038/s41524-024-01268-9)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
