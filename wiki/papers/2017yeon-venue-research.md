---
id: paper:2017yeon-venue-research
type: paper
title: "Development of a ReaxFF Force Field for Cu/S/C/H and Reactive MD Simulations of Methyl Thiolate Decomposition on Cu(100)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:metal-surface
  - task:parameterization
  - domain:mechanics-tribology
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:tribology
  - keyword:dft-static
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.7b06976"
year: 2017
authors:
  - "Jejoon Yeon"
  - "Heather L. Adams"
  - "Chad E. Junkermeier"
  - "Adri C. T. van Duin"
  - "Wilfred T. Tysoe"
  - "Ashlie Martini"
venue: "J. Phys. Chem. B"
pdf_sha256: "ce19c411d015f05386c6c0ea4638698a4055599279f5d1be1561069e5a8c043a"
pdf_path: "papers/Yeon_CuSCH_JPCB_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017yeon-venue-research -->

!!! note "Corpus note"
    The ingested PDF is a **proof**; the published article is identified by the ACS DOI in the extract footer.

## Summary

A ReaxFF reactive force field for Cu/S/C/H was developed and trained against density functional theory (DFT) data so that reactive molecular dynamics can probe methyl thiolate chemistry on copper, including the mechanochemical acceleration of decomposition observed under mild sliding in ultrahigh vacuum. The work reports DFT-driven parametrization (bulk sulfides, adsorption and decomposition paths on Cu(100)) and thermal ReaxFF molecular dynamics of adsorbed methyl thiolates to compare with experiment. **Methyl thiolate** coverage on **Cu(100)** is a well-studied **surface-science** anchor for **organosulfur** **tribochemistry**, motivating a **single** **reactive** model that spans **bulk** **Cu–S** chemistry and **adsorbate** **reaction** sequences on the **close-packed** terrace.

## Methods

**Force-field training (ReaxFF + DFT).** A **Cu/S/C/H ReaxFF** description is **optimized** using **density functional theory (DFT)** reference data for **CuS**, **CuS₂**, and **Cu₂S** **unit-cell** **equation-of-state** curves, **Cu–S** bond **dissociation**, **Cu–S–C** angle bending, **SCH₃**/**CH₃**/**S** **adsorption** **energies** on **Cu**, and **energy** profiles along **methyl thiolate** **decomposition** pathways on **Cu(100)**—mirroring the abstract’s training inventory. **DFT** barriers for thiolate **decomposition** are noted to agree with **experiment** in prior work cited by the authors. **Parameter optimization** follows the manuscript’s **ReaxFF** fitting workflow (see **`[[2017jejoon-yeon-j-phys-chem-development-reaxff]]`** for the **version-of-record** narrative when pagination differs from this **proof** **PDF**).

**Molecular dynamics (reactive).** **Molecular dynamics** simulations of **CH₃S**/**methyl thiolate** **decomposition** on **Cu(100)** at **multiple temperatures** complement **mechanochemical** sliding protocols discussed in the article, separating **thermal** **C–S scission** from **shear**-biased pathways under controlled **stress**/**pressure** conditions reported in the **JPCB** **Methods**. **Periodic** **slab** models with explicit **atom** counts, **timestep** (fs), **thermostat** coupling, **NVT** staging, **equilibration**/**production** **duration** (ps/ns), and any **barostat** usage should be read from **`papers/Yeon_CuSCH_JPCB_2017_proof.pdf`** or the final **JPCB** layout—this wiki does not duplicate every numerical control from the **proof** ingest. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the excerpted introduction beyond noting **parallel replica** dynamics as a general rare-event strategy in the literature.

**Static QM / DFT.** **DFT** supplies **training** **energies** and **reaction** profiles; it is not the long-time **MD** engine.

**Review scope.** **N/A —** primary research communicated through this **proof** duplicate slug.

## Findings

**Outcomes and mechanisms.** **Thermal** **ReaxFF MD** shows **methyl thiolate** **decomposition** initiating with **C–S bond scission**, after which **methyl** fragments **diffuse** on **Cu(100)** and recombine to **desorb ethane**, matching the **experimental** picture summarized in the abstract.

**Comparisons.** **Mechanochemical** **UHV** **sliding** accelerates **decomposition** relative to purely **thermal** trajectories at similarly mild **interface** **temperatures**, consistent with **tribochemical** observations that **stress** can lower effective **barriers** without large frictional heating.

**Sensitivity / design levers.** **Temperature** sweeps in **MD** bracket **reaction** propensity for **covered** surfaces; **shear** amplitude enters the mechanochemical discussion as the mechanical analogue of **pressure**/**stress** in Bell-type models.

**Limitations / outlook.** **Proof** **PDF** pagination may differ from the final **JPCB** article; rare events may still demand **accelerated** sampling beyond standard **MD** lengths.

**Corpus honesty.** This page tracks **`papers/Yeon_CuSCH_JPCB_2017_proof.pdf`**; cite **`[[2017jejoon-yeon-j-phys-chem-development-reaxff]]`** when you need **version-of-record** locators, and pull any missing protocol numerics from the **PDF** rather than this summary.
## Limitations

Local proof PDF and abbreviated extract: simulation protocol details (timestep, thermostat, system sizes, run lengths) should be confirmed from the full article or SI when present.

## Relevance to group

Develops ReaxFF for sulfur–copper tribochemistry and surface decomposition pathways with Adri C. T. van Duin as a coauthor; connects to reactive interface modeling in the broader van Duin ReaxFF line.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcb.7b06976` (version-of-record citation; confirm page locators from PDF).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
