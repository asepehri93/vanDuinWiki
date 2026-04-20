---
id: paper:2020atmani-energy-fuels-simulating-geological
type: paper
title: "Simulating the Geological Fate of Terrestrial Organic Matter: Lignin vs Cellulose"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.energyfuels.9b03681"
year: 2020
authors:
  - "Lea Atmani"
  - "Pierre-Louis Valdenaire"
  - "Roland J.-M. Pellenq"
  - "Christophe Bichara"
  - "Henri Van Damme"
  - "Adri C. T. van Duin"
  - "Franz J. Ulm"
  - "Jean-Marc Leyssale"
venue: "Energy Fuels 34:1537-1547 (2020)"
pdf_sha256: "674ecf2e14ba2eaa0b2fb16b062171ea44fe9b25dac962344857b603b93cf9b2"
pdf_path: "papers/Atmani_Energy_Fuels_2020.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2020atmani-energy-fuels-simulating-geological -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Replica-exchange molecular dynamics compares the simulated geological conversion of **lignin** vs **cellulose** precursors into kerogen-like material and methane. Pyrolysis-relevant behavior is aligned with experiment in broad strokes: lignin yields roughly twice as much kerogen and about five times more methane than cellulose under their protocol. Ex-lignin kerogen is much more compliant and microporous than ex-cellulose kerogen despite similar composition/bonding statistics, informing nanoscale bricks for shale gas models.

## Methods

Replica-exchange MD (not ReaxFF-specific in the abstract) to sample conversion of biopolymer models; analysis of kerogen yield, methane release, and mechanical/porous structure of the products.

## Findings

Clear lignin vs cellulose split on yields and methane; large mechanical and porosity contrast between derived kerogens.

## Limitations

Simplified precursor models and simulation protocol may not capture full basin-specific organic matter diversity or in-situ pressure history.

## Relevance to group

van Duin as co-author on organic matter diagenesis and kerogen properties, relevant to geochemistry and energy applications of MD.

## Citations and evidence anchors

`papers/Atmani_Energy_Fuels_2020.pdf` — abstract (yield ratios, modulus/porosity contrast). https://doi.org/10.1021/acs.energyfuels.9b03681

## Related topics

- [[reaxff-family]]
