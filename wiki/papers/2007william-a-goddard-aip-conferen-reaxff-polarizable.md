---
id: paper:2007william-a-goddard-aip-conferen-reaxff-polarizable
type: paper
title: "The ReaxFF polarizable reactive force fields for molecular dynamics simulation of ferroelectrics"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:polarizable-ff
  - keyword:charge-equilibration
  - keyword:dft-static
  - keyword:validation-experiment
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:reaxff-lineage
  - material:perovskite-oxide
  - method:ereaxff
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.1499551"
year: 2002
authors:
  - "William A. Goddard III"
  - "Qingsong Zhang"
  - "Mustafa Uludogan"
  - "Alejandro Strachan"
  - "Tahir Cagin"
venue: "AIP Conference Proceedings 626, 45–55 (2002)"
pdf_sha256: "79eace53375b0fa74e837cdec6ac3531078850043eab1be6924edf3aa87f8ade"
pdf_path: "papers/Others/The ReaxFF Polarizable Reactive Force Fields for.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2007william-a-goddard-aip-conferen-reaxff-polarizable -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **AIP Conference Proceedings** chapter identified by `doi`. Numerical claims follow the **abstract** in the extract.

## Summary

This proceedings contribution presents a **polarizable ReaxFF** formulation for **BaTiO\(_3\)** aimed at MD simulations of thousands of atoms. The abstract describes **self-consistent charge transfer and polarization**: each atom carries a **fixed-core** Gaussian charge (e.g., **+4** for Ti) and a **mobile valence** Gaussian charge equilibrated via **QEq**-style charge equilibration; core–valence restoring forces come from electrostatics between distributions. **Nonelectrostatic** terms use **Morse** interactions with additional pair parameters. Parameters are fit to reproduce **0 K equations of state** (energy–volume and pressure–volume) for **cubic and tetragonal** BaTiO\(_3\) over a pressure range from **QM** data. Subsequent MD explores **thermal properties**, including the **cubic–tetragonal** transition; the abstract states the ReaxFF transition temperature is in **good agreement** with experiment.

## Methods


The authors derive a polarizable ReaxFF for BaTiO\(_3\) from ab initio quantum data. Each atom carries a fixed Gaussian core charge (for example +4 on Ti) and a mobile valence Gaussian whose magnitude responds via charge equilibration (QEq-style); restoring forces between core and valence distributions come from their mutual electrostatic interaction, with four electrostatic parameters per element class fitted once to QM charge distributions on representative clusters. Pauli repulsion and dispersion are represented with pairwise Morse interactions (three additional parameters per atom pair). Morse parameters are optimized to reproduce zero-temperature equations of state—energy–volume and pressure–volume curves—for cubic and tetragonal BaTiO\(_3\) from QM over a broad pressure range. Molecular dynamics with the fitted model is then used to study thermal properties, including the cubic–to–tetragonal ferroelectric transition.

### MD application (post-fit)

**molecular dynamics** studies of **thermal** properties—including the **cubic→tetragonal** transition—are reported at the **thousands-of-atoms** scale claimed in the abstract. **N/A — MD package name** in the short extract; **N/A — full supercell sizes** line-by-line; **N/A — PBC** details beyond the general **bulk** **perovskite** context; **N/A — explicit NVE/NVT/NPT** labels in the excerpt; **N/A — timestep**; **N/A — trajectory segment lengths** in **ps**/**ns**; **N/A — thermostat** algorithm; **Barostat:** **N/A — NPT** usage not recovered from the excerpt (EOS fitting uses **pressure–volume** **QM** data at **0 K**); **Temperature:** transition **temperature** is an **MD** outcome compared to **experiment**; **Pressure / stress:** **0 K** **EOS** training includes **pressure–volume** **QM** targets; **Electric field:** **N/A — MD bias field** not discussed in the short extract; **Replica / enhanced sampling:** **N/A**.

### Force-field training (QM-driven)

**Parent FF / elements:** **polarizable ReaxFF** for **BaTiO\(_3\)** with **Gaussian** core/valence charges and **Morse** **pair** terms. **QM reference:** **ab initio** data for **charges** on clusters and for **0 K** **EOS** (**energy–volume**, **pressure–volume**) of **cubic** and **tetragonal** phases (**N/A — DFT program/functional/basis/k-mesh** line in this wiki summary—see **AIP Conf. Proc.** **626**, 45–55 (2002), DOI **10.1063/1.1499551**). **Training set:** **QM** **EOS** curves plus **cluster** charge **training** as described above. **Optimization:** **Morse** parameters **optimized** to reproduce the **QM** **EOS**; electrostatic parameters fitted to **QM** charge distributions. **Reference data used:** **QM** **EOS** and **charge** targets; **MD** results compared to **experiment** for the transition **temperature**. Grounding: `papers/Others/The ReaxFF Polarizable Reactive Force Fields for.pdf`, `normalized/extracts/2007william-a-goddard-aip-conferen-reaxff-polarizable_p1-2.txt`.

## Findings

The **polarizable** electrostatic core/valence **Gaussian** charges plus **QEq**-style equilibration and **Morse** nonelectrostatic terms reproduce the fitted **0 K** **EOS** targets for **cubic** and **tetragonal** BaTiO\(_3\) from QM over the pressure range used in the fit. **MD** of the **cubic→tetragonal** transition gives a transition **temperature** in **good agreement** with **experiment** in the authors’ tests, supporting use of the model for larger-scale ferroelectric simulations than feasible with full QM. **Corpus honesty:** the repo filename suggests a later PDF copy; use the **AIP CP** bibliographic string for citations.

## Limitations

- Conference article (2002) with limited page scope; transferability to defects, surfaces, and chemistry outside the training set must be checked case-by-case.
- Filename suggests a later-added PDF copy; authoritative bibliographic data are the **AIP CP 626** citation in the extract.

## Relevance to group

Foundational **eReaxFF / polarizable ReaxFF** narrative for **ferroelectric perovskites**, relevant to reactive/polarizable extensions used across the broader ReaxFF ecosystem.

## Citations and evidence anchors

- DOI: `10.1063/1.1499551`.
- PDF: `papers/Others/The ReaxFF Polarizable Reactive Force Fields for.pdf`.
- Extract: `normalized/extracts/2007william-a-goddard-aip-conferen-reaxff-polarizable_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-ferroelectrics-polar-oxides]]
