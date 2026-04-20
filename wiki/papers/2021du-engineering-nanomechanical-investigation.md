---
id: paper:2021du-engineering-nanomechanical-investigation
type: paper
title: "Nanomechanical investigation of the interplay between pore morphology and crack orientation of amorphous silica"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.engfracmech.2021.107749"
year: 2021
authors:
  - "Tao Du"
  - "Michael Blum"
  - "Chen Chen"
  - "Murali Gopal Muraleedharan"
  - "Adri C. T. van Duin"
  - "Pania Newell"
venue: "Eng. Fract. Mech. 250:107749 (2021)"
pdf_sha256: "06669df4d0af41ecbfa04d7456128f4ba7568d2306e2e611e002a6dede4ba2bf"
pdf_path: "papers/Du_EngFracMech_2021_crack.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2021du-engineering-nanomechanical-investigation -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Reactive MD with ReaxFF explores how **pore shape** and **pre-crack orientation** jointly govern Young’s modulus, critical energy release rate (G_IC), and failure evolution in nanoporous amorphous silica. Ligament thickness (wall thickness between pores) correlates with higher G_IC. Von Mises stress fields show pore geometry imprint on stress hotspots; density evolution during crack growth confirms the expected interplay of voids and brittle failure.

## Methods

ReaxFF molecular dynamics; porous a-SiO2 samples with shaped pores and oriented cracks; mechanical loading protocols extracting modulus and fracture metrics.

## Findings

Pore morphology is a primary knob on E and G_IC besides crack orientation; qualitative failure maps emphasize stress localization patterns.


## Limitations

Nanoscale specimens and rapid loading; extrapolation to macroscopic fracture statistics requires multiscale care.

## Relevance to group

Utah/Penn State collaboration highlighting ReaxFF for brittle fracture and porous silica—touching catalysis supports, MEMS, and glass technology.

## Citations and evidence anchors

`papers/Du_EngFracMech_2021_crack.pdf` — abstract (modulus/G_IC, ligament thickness, stress fields). https://doi.org/10.1016/j.engfracmech.2021.107749

## Related topics

- [[reaxff-family]]