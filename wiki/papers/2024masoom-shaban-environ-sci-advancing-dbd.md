---
id: paper:2024masoom-shaban-environ-sci-advancing-dbd
type: paper
title: "Advancing DBD Plasma Chemistry: Insights into Reactive Nitrogen Species such as NO2, N2O5, and N2O Optimization and Species Reactivity through Experiments and MD Simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - method:classical-md
  - task:experiment-integrated
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.est.4c04894"
year: 2024
authors:
  - "Masoom Shaban"
  - "Nina Merkert"
  - "Adri C. T. van Duin"
  - "Diana van Duin"
  - "Alfred P. Weber"
venue: "Environ. Sci. Technol. 2024, 58, 16087–16099"
pdf_sha256: "9f895472e70ce0428f8b4c7502cba742c6cc913104ba03069aca33bd907507b8"
pdf_path: "papers/Shaban_Plasma_DBD_Clausthal_EnvSciTech_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024masoom-shaban-environ-sci-advancing-dbd -->

## Summary

A **cylindrical dielectric barrier discharge (CDBD)** reactor is tuned—via **voltage**, **frequency**, and **N\(_2\)/O\(_2\)** composition—to manipulate **reactive nitrogen species (RNS)** (**NO\(_2\)**, **N\(_2\)O\(_5\)**, **N\(_2\)O**) quantified by **FTIR**, with **aerosol polymerization** of **acrylamide** used as a probe of **RNS** reactivity. Complementary **LAMMPS** **ReaxFF MD** (extended **Monti**/**Verlackt**-type **CHO/N/O/H** reactive chemistry for **OH** and **H\(_2\)O\(_2\)** in water) studies **plasma–water** interfacial reactivity, emphasizing **OH** recycling in **liquid water**.

Linking FTIR-speciated RNS to a condensed-phase reactivity probe (polymer yield) gives an integrated metric when short-lived radicals are difficult to measure directly at the liquid interface.

## Methods

- **Plasma experiments:** **CDBD** operation across electrical settings and **Ar/N\(_2\)/O\(_2\)** mixtures; **FTIR** quantification of **RNS**; **aerosol** **AM → PAM** polymerization yields versus conditions (Table 1 in the article).
- **MD:** **LAMMPS** with **ReaxFF** parametrization extended from **Monti**/**Verlackt**-line **amino-acid** / biomolecular training sets as cited; **water column** built to **~1 g cm\(^{-3}\)** bulk density up to **~100 Å** height; **1000 ps** **NVT** equilibration at **300 K** with **Nosé–Hoover** thermostat (**25 fs** coupling); **periodic** **x,y**, fixed **z** boundaries; **OH** or **H\(_2\)O\(_2\)** placed **~1 nm** above the surface with **300 K** Maxwell–Boltzmann velocities; **2 ns** production tracking **OH** density and reaction intermediates (Figure 9).

The MD portion isolates aqueous OH chemistry from full plasma kinetics, providing a mechanistic complement to gas-phase RNS measurements rather than a self-contained plasma model.

**1 — MD (plasma–water complement).** **Engine:** **LAMMPS** + **ReaxFF** (extended **Monti**/**Verlackt**-type). **~1 g cm\(^{-3}\)** water column, **Nosé–Hoover** at **300 K** (**25 fs** coupling) after **1000 ps** equilibration, **2 ns** production, **2D PBC** in x,y, fixed **z**; **OH** or **H\(_2\)O\(_2\)** seeds **~1 nm** above the surface. **NPT** and **0 GPa** isotropic **hydrostatic** **pressure** with **Parrinello**/**Berendsen** **barostat**: **N/A** — the excerpt tracks **NVT** **300 K** **water** in **fixed**-**z** **cells** (see **ES&T** for any **Hydrostatic** target). **Barostat, E-field, umbrella, MTD:** **N/A** in this excerpt. **Timestep / atom counts:** use **ES&T** **Methods** for exact values if not restated. **2 — ReaxFF** extension is application-side; not a de novo full **parameter** paper in the sense of AGENTS **block 2** beyond citing parent training lines. **3 — Static QM** as primary result: **N/A**.
## Findings

- **NO\(_2\)**-rich conditions correlate with **high** **PAM** yields in the **aerosol** experiments; **OH**-dominated humid **Ar** plasmas give **low** yields, consistent with short **OH** lifetime (**~0.2 ms** scale cited).
- **MD** shows **OH** can engage **water** in a cycle that **regenerates** **OH** (mechanism **R17** in the paper), supporting **non-negligible** effective **OH** activity even when gas-phase lifetimes are short.
- Together, the **experimental** **RNS** tuning and **simulation** **ROS**–**water** results frame **DBD** chemistry optimization for **environmental** uses (air/water treatment) as stated in the conclusions.

The combined evidence cautions against inferring environmental efficacy from gas-phase RNS alone when liquid-phase radical recycling can amplify effective oxidative stress. Operators and readers should use the full **ES&T** **PDF** (reactor, **FTIR** protocol, and **PAM** yields, **Table 1**) for authoritative numbers. **RNS/ROS** tuning vs **PAM** yield and **MD**-derived **OH** **recycling** (mechanism **R17**) are the main **cross-method** comparisons; **kinetic** lifetimes and **T** are cited from the **paper** where noted above.
## Limitations

**MD** focuses on **OH/H\(_2\)O\(_2\)** in **liquid water**, not full **plasma** kinetics; **FTIR** cannot resolve all short-lived radicals.

## Relevance to group

**Adri C. T. van Duin** co-authorship on **environmental plasma** chemistry with **ReaxFF** **aqueous** interfaces.

## Citations and evidence anchors

- DOI: [10.1021/acs.est.4c04894](https://doi.org/10.1021/acs.est.4c04894)

## Related topics

- [[reaxff-family]]
