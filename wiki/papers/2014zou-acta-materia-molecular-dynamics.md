---
id: paper:2014zou-acta-materia-molecular-dynamics
type: paper
title: "Molecular dynamics simulations of the effects of vacancies on nickel self-diffusion, oxygen diffusion and oxidation initiation in nickel, using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2014.09.047"
year: 2014
authors:
  - "Chenyu Zou"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Huazhi Fang"
  - "Zi-Kui Liu"
venue: "Acta Materialia 83 (2015) 102–112"
pdf_sha256: "1f4c14bcf7a3c837c08435870afd2f2de142c1d147cc2a7700641a3a73466596"
pdf_path: "papers/Zou_ActaMater_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014zou-acta-materia-molecular-dynamics -->

## One-paragraph summary

A Ni–O ReaxFF description is developed from QM training data spanning Ni and NiO equations of state, Ni vacancy formation and self-diffusion, and O insertion and diffusion barriers in Ni. MD validation shows agreement with published Ni self-diffusivity and O interstitial diffusivity/activation energy. The work then examines how vacancies alter O transport and internal oxidation: a **vacancy-pair** oxygen migration mechanism is proposed, and simulations suggest voids at grain boundaries can promote local O segregation via strong O–vacancy binding, nucleating NiO in voids—linking atomistic transport to early oxidation microstructures.

## Methods

- **Parameterization:** ReaxFF fit to DFT-derived bulk, defect, and surface-related training data for Ni–O.
- **MD:** Large-temperature MD for diffusivities; structural analysis of GB/vacancy environments.

## Findings

- Quantitative agreement for tracer-like diffusivities and activation energies compared to literature.
- New mechanistic insight: oxygen can diffuse in concert with vacancies (oxygen–vacancy pair picture).
- GB voids as traps that enhance local O concentration and initiate oxide precipitation.

## Limitations

- Complex real alloys (alloying elements, long-range stress) are not fully captured in a binary Ni–O model.

## Relevance to group

Foundational **metal oxidation + ReaxFF** paper from the group with clear validation metrics—often cited for Ni/NiO reactive simulations.

## Citations and evidence anchors

- DOI: [10.1016/j.actamat.2014.09.047](https://doi.org/10.1016/j.actamat.2014.09.047)
- Abstract: `normalized/extracts/2014zou-acta-materia-molecular-dynamics_p1-2.txt`

## Reader notes (navigation)

- **Cluster:** [[theme-oxides-silica-ceramics]] (metal oxidation); compare catalytic Ni surfaces under [[theme-catalysis-surfaces]].  
- **Frozen eval:** MET1 gold hit in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
- Nickel oxidation and short-circuit diffusion at grain boundaries
- ReaxFF for metals and oxides (Ni–O)
