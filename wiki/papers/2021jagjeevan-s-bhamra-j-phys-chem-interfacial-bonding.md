---
id: paper:2021jagjeevan-s-bhamra-j-phys-chem-interfacial-bonding
type: paper
title: "Interfacial bonding controls friction in diamond–rock contacts"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.1c02857"
year: 2021
authors:
  - "Jagjeevan S. Bhamra"
  - "James P. Ewen"
  - "Carlos Ayestarán Latorre"
  - "John A. R. Bomidi"
  - "Marc W. Bird"
  - "Nabankur Dasgupta"
  - "Adri C. T. van Duin"
  - "Daniele Dini"
venue: "J. Phys. Chem. C 2021, 125, 18395–18408"
pdf_sha256: "2959480c757c1c3eb74b8c06218a27813a0ef78d6200caa1a3751c22964b3fdf"
pdf_path: "papers/Bhamra_Ewen_Diamond_Rock_JPC_C_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021jagjeevan-s-bhamra-j-phys-chem-interfacial-bonding -->

## Summary

Macroscale tribometry and nonequilibrium molecular dynamics (NEMD) with a ReaxFF description for diamond on calcite versus quartz show that, in humid or wet conditions, friction on soft limestone (calcite) can exceed that on hard granite (quartz), reversing the dry trend. With water, diamond–calcite contacts retain more interfacial covalent bonding (often with chemisorbed water) than diamond–quartz. Bond-formation rates grow approximately exponentially with contact pressure, and steady-state friction scales about linearly with the number of interfacial bonds (bond order > 0.3) in the authors’ LAMMPS analysis, linking nanoscale chemistry to macroscale friction.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** LAMMPS, velocity–Verlet integration, ReaxFF reactive NEMD (“Simulation Details” in *J. Phys. Chem. C*).
- **System size & composition:** Rigid or constrained diamond tip on mineral slabs; H\(_2\)O loading 0, 50, or 150 molecules; normal load 2.5–40 nN; slip velocity 10 m/s; production 0.75 ns with steady state assessed over the last 200 ps. Atom counts: see article figures and `pdf_path`.
- **Boundaries / periodicity:** Periodic in *x* and *y*; non-periodic (reflective) in *z* as stated.
- **Ensemble / thermostating:** Langevin thermostat (25 fs damping) on selected interior layers; bottom substrate layer fixed; N/A — isotropic NPT (contact load is applied mechanically, not via a barostat in the NEMD protocol described on this page).
- **Timestep:** 0.25 fs.
- **Duration / stages:** Energy minimization; 0.1 ns equilibration at \(F_n = 0.1\) nN; ramp to target normal load; 0.75 ns shear. Electric field: N/A. Enhanced sampling: N/A.
- **Barostat / pressure:** N/A — NVT-style thermal control in sliding; normal load in nN, not a bulk hydrostatic NPT setpoint.
- **Temperature:** 300 K in the NEMD protocol quoted on the prior curation; confirm any additional \(T\) in the PDF.
- **Electrostatics:** ReaxFF (bond order + QEq) as implemented in LAMMPS per the article.

**Experiments:** Point-contact tribometer, diamond on limestone versus granite, humid air and immersed; small indentation to emphasize interfacial chemistry; friction versus load up to the ~2 GPa Hertz-onset regime discussed in the paper (see `pdf_path` for exact phrasing and figures).

### 2 — Force-field training (ReaxFF and related)

- **Parent / elements:** ReaxFF refit or extension for C/O/H and Ca—C—O (diamond, quartz, calcite) in the Ewen *et al.* line, trained against DFT reference data (equation of state, vibrational and reaction data as in the article and SI; mean energy deviations in figures). **QM reference (training):** DFT level as stated in the parameterization section of *J. Phys. Chem. C* and SI (functional, basis, *k*-mesh: follow the PDF, not this wiki). **Training set & optimization:** ReaxFF least-squares-style optimization with targets listed in the article/SI. **Reference data used:** DFT for fitting; independent comparison to tribometry for qualitative validation of dry/wet and calcite vs quartz trends.

### 3 — Static QM

DFT data enter only as the ReaxFF training and validation set; the paper’s new contribution is NEMD + experiment, not standalone static pathways.

## Findings

- **Experiments:** Friction increases superlinearly with load when interfacial bonding governs dissipation; wet limestone can exceed wet granite though granite is harder.
- **NEMD:** With water, calcite shows more C–O interfacial bonds and higher friction than quartz, reversing the dry ordering in the simulation, qualitatively matching experiment. Bond-formation kinetics: exponential in pressure; activation volumes sub-2 Å\(^3\) in the article’s analysis. Friction at steady shear scales linearly with interfacial bond count. **Comparisons:** sim vs experiment; dry vs wet; calcite vs quartz. **Limitations (authored):** single asperity, 10 m/s slip. **Corpus / KB:** numbers and figure IDs from `pdf_path`.

## Limitations

Single-asperity NEMD at high shear does not map to full rough-surface or field-scale drilling; parameter transfer to other rocks or chemistries needs separate validation.

## Relevance to group

ReaxFF parameterization and LAMMPS NEMD for rock–diamond tribology; Adri C. T. van Duin co-authorship.

## Citations and evidence anchors

*J. Phys. Chem. C* **2021,** **125,** 18395–18408, “Simulation Details” and Figs. 4–9; [10.1021/acs.jpcc.1c02857](https://doi.org/10.1021/acs.jpcc.1c02857).

## Related topics

- [[reaxff-family]]
- [[tribochemistry-reaxff]]
