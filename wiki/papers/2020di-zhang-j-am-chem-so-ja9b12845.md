---
id: paper:2020di-zhang-j-am-chem-so-ja9b12845
type: paper
title: "Controlling the Nucleation and Growth Orientation of Nanocrystalline Carbon Films during Plasma-Assisted Deposition: A Reactive Molecular Dynamics/Monte Carlo Study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:monte-carlo
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:monte-carlo-sampling
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.9b12845"
year: 2020
authors:
  - "Di Zhang"
  - "Linfa Peng"
  - "Xiaobo Li"
  - "Peiyun Yi"
  - "Xinmin Lai"
venue: "J. Am. Chem. Soc."
pdf_sha256: "55c504d06e9cbcbfae7e8de07f39bd9e5a9e4b6ce9a0a9159f7536ddc444328a"
pdf_path: "papers/ReaxFF_others/DiZhang_JACS_2020_carbonfilm_growth.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020di-zhang-j-am-chem-so-ja9b12845 -->

**Hybrid MD + time-stamped Monte Carlo (tfMC)** with **charge-implicit ReaxFF (Ci-ReaxFF)** in **LAMMPS** models **plasma-assisted** growth of **nanocrystalline carbon**, including **Ar\(^+\)** bombardment studies to map **nucleation density** and **graphitic orientation** trends versus ion energy and angle.

## Summary

The article couples experimentally informed **plasma conditions** with **atomistic deposition simulations** of **hydrogenated amorphous carbon** matrices embedding **graphene-like** nanocrystals. **Ci-ReaxFF** balances cost and condensed-phase carbon chemistry versus older ReaxFF/Tersoff benchmarks in their tests. The authors map **crystallization phase diagrams** in **(energy, density)** space for nucleation and perform **graphene irradiation** sweeps with **Ar** projectiles across **energies and incidence angles**, relating **Stone–Wales** defect thresholds to preferred **orientation** of graphitic domains. The overarching claim is that **processing windows** can be rationalized from **atomistic** nucleation and **ion-impact** selection rules rather than from continuum film-growth models alone.

## Methods

- **Software / engine:** LAMMPS with Ci-ReaxFF for C/H chemistry; Ar via Lennard-Jones mixing as stated; comparisons to Tersoff, AIREBO, BOP, and legacy ReaxFF variants. Molecular dynamics is hybridized with time-stamped Monte Carlo (tfMC) as in *J. Am. Chem. Soc.* Methods.
- **System & boundaries:** **Hydrogenated** **amorphous** **carbon** **matrices** with **embedded** **graphene-like** **nanocrystals**; **3D** **PBC** **supercells** for **condensed** **a-C:H** **deposition**; **graphene** **+** **Ar** **bombardment** **cells** for **ion** **impact** **(PBC** **lateral** **sheets** **per** **article**).
- **Deposition protocol:** Initial **classical MD relaxation** (**1.5 ps**, **timestep 0.25 fs**) after species insertion; subsequent **tfMC** moves with tunable **temperature \(T\)** and maximum displacement **Δ** (see parameter study in Methods).
- **Irradiation studies:** **NVT** and **NPT** segments for **graphene + Ar** impacts; **Nosé–Hoover** thermostat; **anisotropic barostat** with **pressure damping 250 fs** (~**1000** timesteps) to maintain near-zero lateral stress as described.
- **Benchmarking:** Side-by-side comparisons to **Tersoff**, **AIREBO**, **BOP**, and legacy ReaxFF variants contextualize when **Ci-ReaxFF** is preferred for **condensed** carbon chemistry under impact and annealing.
- **N/A** — no **external** **electric** **field** in the **MD** **protocol** as summarized; **umbrella**/**metadynamics**/**replica** **sampling: N/A** (uses **tfMC**/**MD** **hybrid** and **bombardment** **dynamics** instead).

## Findings

- Intermediate **plasma energy/density** windows maximize **nucleation density** of nanocrystals within the simulated deposition framework.
- **Crystallization phase diagrams** summarize optimal plasma parameters consistent with experimental **sp\(^2\)** clustering trends.
- **Ar irradiation** simulations connect **ion energy and incidence angle** to **defect populations** (including **Stone–Wales**-based thresholds) and thereby to **preferred growth orientation** of graphitic grains via a “survival of the fittest” selection argument presented in the paper.
- The defect-threshold narrative is used to explain why certain **grains** persist while others are **amorphized** or **re-oriented** under continued bombardment, feeding an orientation texture in the simulated films.

## Limitations

Ci-ReaxFF omits explicit charge dynamics; plasma chemistry is represented through simplified bombardment models rather than full ionic plasma kinetics.

## Relevance to group

Demonstrates **ReaxFF-class** potentials in **industrial DLC / nanocrystalline carbon** modeling—adjacent to group’s carbon materials work.

## Citations and evidence anchors

- DOI: [10.1021/jacs.9b12845](https://doi.org/10.1021/jacs.9b12845)

## Related topics

- [[reaxff-family]]
