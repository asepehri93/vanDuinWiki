---
id: paper:2015black-venue-la5049858
type: paper
title: "Molecular Dynamics Study of Alkylsilane Monolayers on Realistic Amorphous Silica Surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:reaxff
  - method:classical-md
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:tribology
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:reactive-md
source_refs: []
doi: "10.1021/la5049858"
year: 2015
authors:
  - "Jana E. Black"
  - "Christopher R. Iacovella"
  - "Peter T. Cummings"
  - "Clare McCabe"
venue: "Langmuir"
pdf_sha256: "7ece766648d756f2bbda45f01537a3a8aab9c2eeab49e16ab05b6d313f9d8c98"
pdf_path: "papers/ReaxFF_others/Black_Langmuir_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015black-venue-la5049858 -->

## Summary

Molecular dynamics simulations compare **reactive** (ReaxFF) and **classical (nonreactive)** models for **n-alkylsilane** monolayers on silica. The authors introduce a **synthesis mimetic simulation (SMS)** sequence in which amorphous silica is generated and exposed to **H₂O₂** to build a hydroxide-rich surface analogous to **piranha** treatment of silicon wafers, then alkylsilanes are assembled. Results are compared to more idealized setups (crystalline silica, non-H₂O₂ amorphous surfaces, controlled roughness).

The central claim is tribological: laboratory-relevant oxidation roughens and hydroxylates silica at nanometer scales that classical monolayer studies often omit.

## Methods

### MD application (atomistic dynamics)

All trajectories use **LAMMPS**. **ReaxFF** (Fogarty *et al.* Si/O; Rahaman *et al.* C/O/H) builds **amorphous silica** substrates **with and without** **synthesis mimetic simulation (SMS)** exposure to **H₂O₂**, intended to mimic **piranha**-type oxidation and hydroxylation before **n-alkylsilane** assembly; **OPLS-AA** (Lorenz *et al.* silica; Jorgensen *et al.* alkanes) carries **nonequilibrium shear** because it is ~**50×** cheaper than ReaxFF at similar sizes, with the authors reporting close **equilibrium** monolayer agreement between ReaxFF and OPLS-AA so friction uses OPLS-AA on SMS-prepared surfaces. **SMS** is melt/quench silica followed by **H₂O₂** processing, then monolayer deposition, compared to crystalline, defected-crystalline, and non-H₂O₂ amorphous surfaces.

Shear cells use **C₁₀** alkylsilanes at **3.9 chains nm⁻²** (~experimental **4.0**), **PBC in xy**, and **PPPM slab** electrostatics with **no** long-range Coulomb across the nonperiodic **z** normal. Runs are **NVT** at **300 K** with a **Nose–Hoover thermostat** (**50 fs** damping); **0.5 fs** timestep for ReaxFF and **rRESPA** for OPLS-AA (**0.3 / 0.6 / 1.2 fs** for bonds/angles/LJ+Coulomb). **2 ns** production samples **equilibrium** monolayer structure (ReaxFF); **5–10 ns** production applies **±5 m s⁻¹** sliding velocities to mirrored stacks (faster than typical AFM but consistent with prior monolayer friction MD). The **outer 50%** of each silica slab is **rigid**; normal load is scanned by fixing inner surface separations at **4–5** spacings between **1.8** and **3.0 nm** (**N/A —** stochastic **NPT** barostat). **OPLS-AA LJ cutoff 10 Å**. **Applied electric fields and replica sampling:** **N/A —** not used.

### Force-field training

**N/A —** this work applies published ReaxFF/OPLS-AA parameterizations; it does not report a new QM training loop.

### Static QM / DFT

**N/A —** central claims are from reactive/classical MD and nonequilibrium shear.

## Findings

**SMS** produces hydroxyl-rich, **rough** amorphous silica that changes monolayer **packing and tilt** versus idealized crystalline or unprocessed amorphous substrates; **nematic order** and **tilt distributions** track **RMS roughness** in the article’s analysis. **Friction** correlates **negatively** with **global orientational order** under monolayer–monolayer shear: **defects** modestly raise friction, while **substrate roughness** (especially after SMS) lowers order and raises friction more strongly, with **defects plus SMS roughness** acting **together**. Omitting postsynthesis oxidation therefore **underestimates friction** and **overestimates order** versus laboratory-relevant surfaces, so ideal crystalline silica can **misrank** lubricant chemistries.

## Limitations

Wear via **C–C/C–Si bond scission** is explicitly **out of scope** (OPLS-AA shear avoids reactive scission); extending to wear chemistry would require reactive shear models and longer timescales than reported here.

## Relevance to group

Illustrates **ReaxFF** use for **oxidative surface preparation** and **tribology** on **silica**, with explicit comparison to classical modeling of the same interfaces.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
