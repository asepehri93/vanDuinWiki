---
id: paper:2021molaei-scientific-r-hypersonic-impact
type: paper
title: "Hypersonic impact properties of pristine and hybrid single and multilayer C3N and BC3 nanosheets"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:widegap-semiconductor
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:shock-compression
  - keyword:classical-ff
  - keyword:npt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1038/s41598-021-86537-z"
year: 2021
authors:
  - "Fatemeh Molaei"
  - "Kasra Einalipour Eshkalak"
  - "Sadegh Sadeghzadeh"
  - "Hossein Siavoshi"
venue: "Sci. Rep. 2021, 11, 7972"
pdf_sha256: "e8a3846bdaaa0185667b039c432b293cdbbf12fd2eea4fcf3960f5226ed867e1"
pdf_path: "papers/Others/Molaei_C3N_BC3_impact_SciRep_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021molaei-scientific-r-hypersonic-impact -->

## Summary

**Classical molecular dynamics** in **LAMMPS** models **C\(_{60}\)** projectile impacts on **C\(_3\)N** and **BC\(_3\)** monolayers and multilayers using **Tersoff** interactions for intralayer bonding (parameters from Kinaci *et al.* as cited) and **Lennard–Jones** for interlayer **vdW** gaps. After **NPT equilibration** at **300 K** (**Nosé–Hoover**, **0.25 fs** timestep, **50 ps**), **C\(_{60}\)** is launched along **\(z\)** toward fixed edge atoms. The study maps **ballistic curves**, residual velocities, and energy absorption versus impact speed, layer count, spacing, and **C\(_3\)N/BC\(_3\)** stacking, reporting that **C\(_3\)N** can absorb more energy than **BC\(_3\)** at high speed due to stronger **N–C** vs **B–C** bonding, with hybrid stacks improving **BC\(_3\)** performance.

## Methods

**MD application (classical, ballistic impact).** **LAMMPS** runs **NPT** equilibration at **300 K** (Nosé–Hoover as stated in the article) for **C\(_3\)N** and **BC\(_3\)** monolayers and multilayers, then **NVE**-style **impact** segments (post-equilibration) where a **C\(_{60}\)** projectile is given initial velocity along **z** toward the sheet. **Velocity Verlet** integration with **Δt = 0.25 fs**; equilibration **50 ps** (per the article’s “Computational methods” table). **Tersoff** parameters from Kinaci *et al.* (cited) describe intralayer **C–B / C–N / C–C** bonding; **Lennard–Jones** 12-6 terms with **Lorentz–Berthelot** mixing (Table 1) treat **interlayer** van der Waals interactions. A representative monolayer patch is about **6×6 nm\(^2\)** with **PBC** in plane; one **edge** row of atoms is **fixed** in **x,y** to anchor the target; initial projectile–sheet gap **5 nm**; total atom count **1404** in the documented monolayer example (**1068** C including **60** in C\(_{60}\), **336** B/N in the monolayer sheet). **Barostat** — used in **NPT** equilibration only. **Production impact** — **NVE** (no thermostat on the colliding system as described for the strike protocol). **Electric field / enhanced sampling — N/A**. **Electrostatics** — Tersoff+LJ; **N/A** long-range Ewald beyond the LJ model as described. **Shock** — hypersonic impact speeds span the paper’s parametric table (see Table 2 / Figs. 2–3 for residual speed vs impact speed).

**Force-field training.** **N/A —** uses published Tersoff + LJ parameters; no refit in this work.

**Static QM.** **N/A** — not used.

## Findings

**Outcomes and mechanisms.** The study maps **ballistic curves** and **residual velocities** for **C\(_{60}\)** impacts on **C\(_3\)N** and **BC\(_3\)**; **C\(_3\)N** can **absorb more energy** at high impact speeds, linked in the paper to stronger **N–C** vs **B–C** bonding. At lower speeds before penetration, **single-layer** responses are more similar. **Decomposition** of kinetic energy into **bond** **stretching** vs **interlayer** **slip** is discussed qualitatively through the **Tersoff**+**LJ** **partition**—**N/A** **reactive** **bond**-**making** **chemistry** in this **classical** **stack**.

**Comparisons and sensitivity.** **Hybrid** stacks with alternating **C\(_3\)N/BC\(_3\)** **multilayers** can outperform homogeneous **BC\(_3\)** stacks in the reported energy-absorption metrics. **Sensitivity** to **layer** **count**, **interlayer** **spacing**, and **initial** **projectile** **velocity** is **tabulated** in the **article**; **N/A** — direct **experiment** **or** **shock**-**tube** **validation** in this **computational** **paper** (the **authors** **do** **not** **claim** **quantitative** **agreement** **with** **macro**-**scale** **experiments** **here**). **Strain** **rate** and **shock** **invariant** **comparisons** are **N/A** **beyond** the **stated** **C\(_{60}\)** **ballistic** **setup**.

**Limitations (as implied by the model class).** **Tersoff**+**LJ** **omits** **bond**-**breaking** **chemistry** and **charge** **transfer**; **transferability** of **parameters** to **other** **projectiles** or **alloys** is **uncertain** without **further** **benchmarks** (see **##** **Limitations** **below** for **this** **wiki** **note**).

## Limitations

Tersoff+LJ models omit bond-breaking chemistry (contrast with ReaxFF reactive studies); parameter transferability at extreme impact speeds should be benchmarked against experiment or higher-level theory.

## Relevance to group

**Non-ReaxFF** ballistic MD benchmark of 2D nitride/boride sheets—useful contrast to reactive workflows in the corpus.

## Citations and evidence anchors

- Sci. Rep. **11**, 7972 (2021); “Computational methods” and Table 1–2.

## Related topics

- [[reaxff-family]]
