---
id: paper:2020hyunguk-kwon-j-phys-chem-jp0c03355
type: paper
title: "Reactive Molecular Dynamics Simulations and Quantum Chemistry Calculations To Investigate Soot-Relevant Reaction Pathways for Hexylamine Isomers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:dft-static
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.0c03355"
year: 2020
authors:
  - "Hyunguk Kwon"
  - "Brian D. Etz"
  - "Matthew J. Montgomery"
  - "Richard Messerly"
  - "Sharmin Shabnam"
  - "Shubham Vyas"
  - "Adri C. T. van Duin"
  - "Charles S. McEnally"
  - "Lisa D. Pfefferle"
  - "Seonah Kim"
  - "Yuan Xuan"
venue: "J. Phys. Chem. A 124:4290-4304 (2020)"
pdf_sha256: "c63e9df678f8aec7347345bbd4ca7942cc3f0a2f1d70033b96fe7c83bdfbd7e9"
pdf_path: "papers/Kwon_JPC_2020_Soot_growth.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2020hyunguk-kwon-j-phys-chem-jp0c03355 -->

## One-paragraph summary

Building on experimental YSI measurements for nitrogen-containing hydrocarbons, this work studies three C6H15N isomeric amines—dipropylamine (DPA), diisopropylamine (DIPA), and 3,3-dimethylbutylamine (DMBA)—with ReaxFF MD at 1400–1800 K (sooting-relevant window) plus QM refinement of reaction networks. ReaxFF ranks reactivity DIPA > DPA > DMBA across temperatures. Major nonaromatic soot precursors differ by isomer (C2H4, C3H6, C4H8 families); combined ReaxFF and QM sooting tendency order matches experimental YSI trends.

## Methods

ReaxFF NVT simulations with a methane-rich radical pool framework; QM energy surface surveys keyed off MD intermediates.

## Findings

Consistent story between ReaxFF and QM on key intermediates and relative sooting propensity for the three amines.

## Limitations

Isomer subset only; nitrogen chemistry under real flame conditions is richer than the modeled gas-phase subset.

## Relevance to group

Penn State combustion collaboration tying ReaxFF to biomimetic/bio-derived fuel nitrogen chemistry and YSI metrics.

## Citations and evidence anchors

`papers/Kwon_JPC_2020_Soot_growth.pdf` — abstract (fuels, temperatures, reactivity order, precursor species). https://doi.org/10.1021/acs.jpca.0c03355

## Related topics

- [[2019kwon-fuel-correct-numerical-simulations]]
- [[reaxff-family]]
