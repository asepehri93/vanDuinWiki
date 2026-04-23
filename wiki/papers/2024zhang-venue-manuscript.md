---
id: paper:2024zhang-venue-manuscript
type: paper
title: "ReaxFF study of surface chemical reactions between α-Al₂O₃ substrates and H₂O/H₂ gas-phase molecules"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - task:parameterization
  - task:application
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:oxide-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c04669"
year: 2024
authors:
  - "Yuwei Zhang"
  - "Nadire Nayir"
  - "Yun Kyung Shin"
  - "Qian Mao"
  - "Ga-Un Jeong"
  - "Chen Chen"
  - "Joan M. Redwing"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "08de552743849aeac0467246532e4b3316905c9c7f6d6acb0836b4db1b876719"
pdf_path: "papers/Zhang_Yuwei_Al2O3_H2O_H2_JPCC_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024zhang-venue-manuscript -->

An Al/O/H ReaxFF is trained to α-Al₂O₃ surface energies (A, C, R, M facets; Al- and O-terminated models), hydrolysis and hydrogen-diffusion targets on (0001), and step–terrace dehydration data, then used in large-scale MD of H₂O and H₂ on α-Al₂O₃(0001) and related terminations with mixed Berendsen thermostats mimicking vacuum MOCVD-like conditions.

## Summary

The authors develop an Al/O/H reactive potential starting from prior Al₂O₃ bulk data and DFT surface energies for stoichiometric and non-stoichiometric α-Al₂O₃ slabs (Sun/Kurita/Hüttner-style references in the paper), then refine Al–O, Al–H, and Al–O–H parameters against hydroxylation, diffusion, and step–terrace dehydration energies from literature DFT. Section 4 documents MD protocols: relaxation and heating with Berendsen thermostat/barostat in NPT then NVT segments; mixed thermostats (100 fs substrate vs 10³ fs gas) for H₂O + α-Al₂O₃(0001) with ordered Al terminations (50% vs 100% Al, C_Al_I / C_Al_II) and random Al distributions; timestep 0.15 fs; isothermal holds (e.g., 0.5 ns) at 350–1500 K depending on case; H₂ exposure protocols including heating to 1275 K, optional modified H–H σ bond energy to accelerate H₂ dissociation on O-terminated surfaces (~19.4 kcal/mol barrier reduction stated in abstract), and ~1.5 ns segments to remove O while tracking hydroxyl remnants.

## Methods

- **Force field:** ReaxFF energy decomposition as in standard formulation; training via successive single-parameter search against QC datasets (formation energy, surface slabs, hydrolysis 1–2 and 1–4 pathways on 50% Al (0001), step–terrace dehydrations, bulk lattice/aH).
- **DFT sources:** Surface energies and reaction energies from cited PBE/surface studies; comparisons to bond-scan artificial forces in Fig. 3 for pathway training.
- **MD:** H₂O/α-Al₂O₃(0001) grids in Tables 3–4 (varying H₂O/Al ratios); random surfaces with fixed H₂O load; H₂ runs on multiple terminations (A, C, M, R families) per Table 5; Berendsen thermostats/barostats as quoted in §4.1–4.2; σ(H–H) parameter perturbation case for O removal kinetics.

**1 — MD application (ReaxFF, vacuum/MOCVD-mimic).** **Engine:** **LAMMPS**-class **ReaxFF** **molecular** **dynamics**; **NVT** **H₂O** and **H₂** **exposure** **stages** at **isothermal** **K** in **~350**–**1500** **K** **(temperature)** **windows** per **Table**; **0.15** **fs** **time** **step**; **~0.5** **ns** **holds** / **~1.5** **ns** **H₂** **segments** as **cited**; **mixed** **Berendsen** **thermostat** on **gas** **vs** **substrate** (**e.g.** **100** **fs** **substrate** **vs** **10³** **fs** **vapor**); **earlier** **segments** also use **NPT** **relax** with **Berendsen** **thermostat** and **barostat** (near-ambient **pressure** in **bar**/**GPa** **units** as listed in §4) in **article** text. **PBC** **slab**; **E-field** and **rare**-**event** **methods** — **N/A** in the **stated** **H₂O/H₂** **protocols** on *this* **summary** (use **VOR**/**SI**).

**2 — Force-field training (Al/O/H).** **Iterative** **ReaxFF** **fit** to **DFT** **α-Al₂O₃** **(0001)** **A/C/R/M** **surface** **energies**, **hydrolysis**/**diffusion**/**dehydration** **paths**, **H₂O** **/H₂** **chemistry** with **PBE**-**style** **literature** **targets** (see **force**-**field** bullet in **Summary** and **SI** for **parrex**-style **search**). **3 — Static QM** — **PBE** **slab** **and** **reaction** **energies** **in** the **fit**; **separate** **QM** **“application-only”** **manuscript** **N/A** beyond **training** and **select** **plots**.
## Findings

1. The ReaxFF reproduces DFT surface energetics trends and hydrolysis/dehydration training targets for flat and step–terrace models within the figures reported.
2. Water autocatalysis accelerates hydroxylation: at moderate vapor loads, proton transfer via hydrogen-bond networks and oxohydroxide clustering (O\(_x\)H\(_y\)) competes with full dissociation; 100% Al-terminated (0001) hydroxylates more readily at 350 K than 50% termination and desorbs more water above ~500 K, yet full dehydroxylation is not achieved and a gibbsite-like overlayer is deemed unlikely under the explored sprays.
3. Random vacancy-like Al distributions on (0001) deviate from ideal 1–2 and 1–4 pathways and appear more reactive than ordered surfaces at comparable Al coverage.
4. H₂ on O-rich surfaces shows enhanced dissociation kinetics when oxygen coverage is high and surface stability is low; lowering the H–H σ energy (or equivalent barrier scaling) in a controlled parameter test accelerates O removal toward Al-terminated-like states while leaving some hydroxyls after ~1.5 ns.

**Corpus honesty** — **galley** **PDF**; duplicate **ingest** **[[2024zhang-venue-manuscript-2]]** may **differ** by **file** **hash** only.
## Limitations

Publisher **galley** PDF; kinetic rates are classical-ReaxFF estimates; parameter modification for H–H is a diagnostic tool rather than a general gas-phase H₂ model.

## Relevance to group

Group-authored ReaxFF for sapphire/2D-growth substrate chemistry with explicit MD protocols for H₂O and H₂ environments.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c04669](https://doi.org/10.1021/acs.jpcc.4c04669)

## Reader notes (navigation)

- Duplicate ingest for the same DOI: [[2024zhang-venue-manuscript-2]] (alternate galley PDF hash).
- Related: [[reaxff-family]], [[theme-oxides-silica-ceramics]].

## Related topics

- [[reaxff-family]]
