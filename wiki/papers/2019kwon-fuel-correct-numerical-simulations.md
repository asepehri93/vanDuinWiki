---
id: paper:2019kwon-fuel-correct-numerical-simulations
type: paper
title: "Numerical simulations of yield-based sooting tendencies of aromatic fuels using ReaxFF molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116545"
year: 2019
authors:
  - "Hyunguk Kwon"
  - "Sharmin Shabnam"
  - "Adri C. T. van Duin"
  - "Yuan Xuan"
venue: "Fuel (2019), corrected proof, article 116545"
pdf_sha256: "8c7353e44798d865ca22090ecbec03d6cfa40a400f308afc2fede75c1ecb5662"
pdf_path: "papers/Kwon_Fuel_2019_online.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019kwon-fuel-correct-numerical-simulations -->

## One-paragraph summary

The authors present a ReaxFF molecular dynamics workflow to compute the experimental Yield Sooting Index (YSI) for fuels, using a multi-stage procedure designed to mirror how YSI is obtained experimentally and in continuum models. Toluene and phenol are used as proof-of-concept aromatics with relatively well-characterized chemistry. Simulations capture key growth pathways expected from kinetics (toluene retaining and growing aromatic rings; phenol involving carbon-loss pathways with CO release). A quantitative YSI construction from ReaxFF output is compared to measurements with reasonable agreement, arguing that the approach can rank sooting tendency when detailed kinetic mechanisms are unknown.

## Methods

Reactive MD with ReaxFF; multi-stage simulation protocol aligned with the YSI concept. Proof-of-concept fuels: toluene and phenol. Comparison of ReaxFF-derived YSI values to published experimental YSI data.

## Findings

ReaxFF captures qualitative soot-relevant chemistry consistent with known pathways for the chosen fuels. The derived YSI formulation gives values in reasonably good agreement with experiment for the cases studied, supporting use of the framework for relative sooting tendency among structurally related fuels.

## Limitations

Demonstration is limited to two aromatic compounds; extension to broader fuel spaces, blend effects, and quantitative error bars requires further validation. YSI mapping from atomistic trajectories introduces modeling choices that may not transfer unchanged to all fuel classes.

## Relevance to group

Co-authored from Penn State mechanical engineering; extends group capabilities in ReaxFF-based combustion and soot precursor chemistry relevant to fuels and emissions modeling.

## Citations and evidence anchors

Primary locator: `papers/Kwon_Fuel_2019_online.pdf` — abstract and methods for YSI protocol and toluene/phenol results. DOI: https://doi.org/10.1016/j.fuel.2019.116545

## Related topics

- [[2019kwon-venue-paper]] (uncorrected proof PDF of the same article)
- [[reaxff-family]]
