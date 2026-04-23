---
id: paper:2024alireza-sepehrinezha-j-phys-chem-reaxff-reactive
type: paper
title: "ReaxFF reactive force field for exploring electronically switchable polarization in Zn1−xMgxO ferroelectric semiconductors"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:ferroelectrics-polar
  - method:reaxff
  - method:dft-static
  - material:widegap-semiconductor
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c02233"
year: 2024
authors:
  - "Alireza Sepehrinezhad"
  - "Steven M. Baksa"
  - "Ismaila Dabo"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 2024, 128, 12534–12543"
pdf_sha256: "0a35d43bc1ace6b09b1f8196130e38e5e97bd4f648b07f3d3afd3c25ec71dea1"
pdf_path: "papers/Sepehrinezhad_ZnMgO_JPCC_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024alireza-sepehrinezha-j-phys-chem-reaxff-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

Wurtzite-derived ZnO can host ferroelectric-like polar order when alloyed and strained, offering a non-perovskite route to switchable polarization in wide-gap oxides, but quantitative modeling must connect dopant chemistry to domain stability and coercivity. The paper parametrizes a **ReaxFF** model for **Zn₁₋ₓMgₓO**, a **non-perovskite** **ferroelectric semiconductor**, using **density-functional theory (DFT)** training data spanning bonding environments relevant to wurtzite-derived polar distortions, then uses **large-scale MD** to study **polarization hysteresis**, **coercive fields**, and **Mg** distribution effects in nanoscale films. The abstract motivates the force-field effort by noting that first-principles studies of doped ZnO ferroelectricity are computationally costly at device-relevant scales, whereas ReaxFF enables field-driven switching trajectories in larger cells. Readers should treat reported remnant polarization magnitudes, critical thickness estimates, and coercive-field trends as model predictions to be cross-checked against DFT and experiment in the full article and supporting information.

## Methods

### ReaxFF parameterization (A)

**DFT** database for **Zn–Mg–O** environments supporting **wurtzite-derived** **polar** distortions.

### Field-driven reactive MD (B)

**Thin-film**-like supercells; **E-field** **switching** sweeps; **Mg** **x**, **clustered vs random** dopant layouts, **T**; outputs include **P(E)** **hysteresis** and **remanent P**.

**Protocol sensitivity:** **coercive field**, **critical thickness**—verify **thermostat**, **damping**, **ramp** against **Computational Details**/**SI** in **`papers/Sepehrinezhad_ZnMgO_JPCC_2024.pdf`**.

**Electrostatics in field-driven runs.** Field-coupled **ReaxFF** simulations require consistent **charge** equilibration frequency and **damping** choices when **E-field** magnitudes change; the article’s **Computational Details** specify how **thin-film** **supercells** treat **vacuum** padding, **fixed** **bottom** layers (if any), and **ramp** **schedules** for **polarization** reversal.

**MD application (E-field, ferroelectric switching).** **LAMMPS**+**ReaxFF** in **NVT** (or as stated) with **PBC** in-plane for **wurtzite** **Zn\(_{1-x}\)Mg\(_x\)O**-like **thin-film** **supercells**; **system** size and **Mg** **doping** layouts in **J. Phys. Chem. C** **2024**. **Time step** (fs), **equilibration**/**production** (ps/**ns**), **Nosé–Hoover** **thermostat** and damping, and **E-field** sweeps in **V/nm** or **MV/cm** (see article) are **N/A** to restate line-by-line here. **N/A**—**NPT** **barostat** if runs are **constant**-volume and **isotropic** stress is not targeted; **N/A**—**metadynamics**. **Temperature** is varied to study coercive trends. **Hydrostatic** **pressure** **N/A** for standard **NVT** **E-field** protocols in the summary.

## Findings

**Ferroelectric switching** appears at a **critical thickness** near **~10 nm** with **residual polarization ~100 μC/cm²** (order of magnitude as reported). **Higher Mg substitution** correlates with **lower coercive field** in the model study. **Coercive field** decreases with **increasing temperature**. **Clustered Mg** increases **coercive field** relative to more **uniform** arrangements, whereas **random** Mg lowers it versus **uniform** distributions—highlighting **microstructural** control of **switching** in **doped ZnO**-class ferroelectrics.

## Limitations

**Electronic polarization** in **ReaxFF** is **classical**; quantitative agreement with **DFT** or **experiment** for **absolute** **P(E)** curves should be checked against the **full article** and **SI**.

## Relevance to group

Extends **ReaxFF** into **ferroelectric oxide** semiconductors beyond **perovskites**, co-authored by **van Duin** and **Dabo**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c02233](https://doi.org/10.1021/acs.jpcc.4c02233)
- **J. Phys. Chem. C** **128**, **12534–12543** (2024)
- `normalized/extracts/2024alireza-sepehrinezha-j-phys-chem-reaxff-reactive_p1-2.txt`

## Reader notes (navigation)

- Ferroelectric / polar oxides: [[theme-ferroelectrics-polar-oxides]]; ReaxFF hub: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
