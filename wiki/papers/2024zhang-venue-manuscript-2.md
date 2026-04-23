---
id: paper:2024zhang-venue-manuscript-2
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
pdf_sha256: "2459b9fbb6b57f5b82e4451a85b0b8860e8bb43b5528fd1be564a9ac1e842297"
pdf_path: "papers/Zhang_Yuwei_Al2O3_H2O_H2_JPCC_2024_galley_v2.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024zhang-venue-manuscript-2 -->

Second **galley** PDF byte variant for the Zhang et al. **J. Phys. Chem. C** sapphire surface chemistry article; same DOI and science as [[2024zhang-venue-manuscript]].

## Evidence and attribution

!!! note "Authority of statements"

    Prose follows the publication identified by `doi` and the primary curated page. This file exists for **hash-level** provenance of an alternate galley export.

## Summary

An Al/O/H ReaxFF is trained to α-Al₂O₃ surface energies (A, C, R, M facets; Al- and O-terminated models), hydrolysis and hydrogen-diffusion targets on (0001), and step–terrace dehydration data, then applied in large-scale MD of H₂O and H₂ on α-Al₂O₃(0001) and related terminations with Berendsen thermostats and barostats mimicking vacuum and MOCVD-like conditions. Section 4 of the article documents NPT then NVT segments, mixed thermostats for gas versus substrate, 0.15 fs timestep, and isothermal holds over hundreds of picoseconds to nanoseconds depending on case, including H₂ protocols with optional modified H–H σ bond energy to accelerate dissociation in controlled tests.

## Methods

**Force-field training:** The Al/O/H **ReaxFF** is built with successive single-parameter refinement against **DFT** reference data (formation energies, **(0001)** and stepped surface slabs, **50%** Al-termination **hydrolysis** paths, **step–terrace dehydration** targets, bulk cell parameters). The parent scope and **QM** level follow [[2024zhang-venue-manuscript]]; this duplicate page does not re-tabulate the training tables.

**MD application:** **Reactive MD** in **LAMMPS** (see primary page) studies **H₂O** and **H₂** on **α-Al₂O₃(0001)** (ordered and random Al terminations, variable loadings). The article’s **Methods** report **NPT** then **NVT** stages, **Berendsen** thermostats and barostats, **0.15 fs** timestep, and isothermal holds including **~300 K** and **~350 K** **temperature** settings in the spray scenarios. **ps–ns** **production** **duration** and **equilibration** are tabulated in the VOR. **3D PBC** **periodic** cells for slabs. **N/A — electric field**; **N/A — umbrella / metadynamics** (not used). Full **atom** counts and thermostat damping: **[[2024zhang-venue-manuscript]]** and **PDF**.
## Findings

The model reproduces DFT surface energetics and hydrolysis and dehydration training targets within the reported figures. Water networks accelerate hydroxylation; 100% Al-terminated (0001) hydroxylates more readily at 350 K than 50% termination in the explored sprays, while full dehydroxylation is not achieved under those conditions. Random Al distributions on (0001) can be more reactive than ordered surfaces at comparable coverage. H₂ on O-rich surfaces shows enhanced dissociation when oxygen coverage is high; parameter-modified H–H tests accelerate O removal while leaving some hydroxyls after the simulated segments.

This duplicate **galley** hash exists for provenance only; keep the narrative in lockstep with **[[2024zhang-venue-manuscript]]** so numbers and conditions do not drift between sibling **PDF** exports.

## Limitations

Duplicate galley artifact; prefer the **version-of-record** PDF for citation, pagination, and final figures. Kinetic rates are classical ReaxFF estimates; σ(H–H) modification is a diagnostic, not a general gas-phase H₂ model.

## Relevance to group

Group-authored ReaxFF for sapphire and 2D-growth substrate chemistry; this slug tracks a second galley hash.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c04669](https://doi.org/10.1021/acs.jpcc.4c04669)

## Reader notes (navigation)

- Canonical narrative and sibling galley: [[2024zhang-venue-manuscript]].
- Theme hub: [[theme-oxides-silica-ceramics]].

## Related topics

- [[reaxff-family]]
- [[2024zhang-venue-manuscript]]
