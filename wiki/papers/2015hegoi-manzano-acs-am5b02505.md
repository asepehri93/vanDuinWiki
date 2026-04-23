---
id: paper:2015hegoi-manzano-acs-am5b02505
type: paper
title: "Insight on Tricalcium Silicate Hydration and Dissolution Mechanism from Molecular Simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - material:cement-mineral
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:water-interfaces
  - keyword:reaxff-application
  - keyword:oxide-surface
source_refs: []
doi: "10.1021/acsami.5b02505"
year: 2015
authors:
  - "Hegoi Manzano"
  - "Engin Durgun"
  - "Iñigo López-Arbeloa"
  - "Jeffrey C. Grossman"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "711499c8437a084c6ec4cad0bb433535430b5949b1042867462955d07dd0d1aa"
pdf_path: "papers/ReaxFF_others/Manzano_CaO_H2O_ACS_AMI_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015hegoi-manzano-acs-am5b02505 -->

## Summary

Hydration of mineral surfaces couples multiple reactions and topological rearrangements that challenge both experiment and simulation. This study applies ReaxFF reactive molecular dynamics in LAMMPS to tricalcium silicate (C₃S), the dominant phase in ordinary Portland cement, comparing static descriptors such as surface energies and water adsorption energies to fully dynamic hydration over nanosecond trajectories. The central conclusion is that static metrics alone fail to predict hydration propensity once hydrogen from dissociated water penetrates the crystal, producing a disordered calcium silicate hydrate-like layer whose morphology converges across surfaces despite widely varying static adsorption characteristics. Dynamic hydration also exposes how surface topology templates unexpected water tessellation patterns that can stabilize surfaces against dissolution.

## Methods

The ReaxFF parameter set merges independently developed Si–O–H and Ca–O–H parameterizations (Fogarty et al. and Manzano et al., as cited) and has prior use for calcium silicate hydrates and clays. Slabs cut from bulk C₃S are at least about 4 nm thick with in-plane dimensions exceeding roughly 2.5 nm; a 3 nm vacuum separates the slab from periodic images. Energy minimization uses Polak–Ribiere conjugate gradients. Molecular dynamics runs in the NPT ensemble at 298 K and 1 atm with a Nosé–Hoover thermostat (20 fs damping constant), velocity-Verlet integration, and a 0.2 fs timestep. Water is packed to roughly 1 g cm⁻³ in the fluid region with packmol, relaxed separately, then contacted with the crystal with initial Maxwell–Boltzmann velocities at 298 K; center-of-mass velocities are removed periodically to avoid drift. Trajectories extend on the order of 2 ns for the dynamic hydration comparisons discussed in the article.

## Findings

Surface energies and adsorption energies computed before reaction do not rank subsequent hydration behavior once major interfacial reconstruction occurs. Hydrogen ingress yields a disordered C–S–H-like layer that appears similar for several distinct starting surfaces. Topology-dependent water arrangements stabilize certain surfaces against dissolution in ways invisible to static adsorption pictures alone, demonstrating that long reactive MD is necessary to capture dissolution precursors for this cementitious model system.

The “static picture” section of the article contrasts bare-slab energetics with the later dynamic interface, showing wide variation in pre-reaction adsorption metrics that collapses once a disordered hydrate layer forms. That collapse is the quantitative backbone for the claim that designers cannot rely on pre-reaction surface-energy rankings alone when selecting facets or additives for C₃S hydration.

## Limitations

Nanosecond sampling still undershoots laboratory hydration timescales; ReaxFF kinetics are approximate; pore solution chemistry beyond pure water is not represented.

## Relevance to group

Foundational **cement** + **ReaxFF** demonstration that **dynamic** interfaces invalidate **static** reactivity metrics for C₃S.

## Citations and evidence anchors

- DOI: [10.1021/acsami.5b02505](https://doi.org/10.1021/acsami.5b02505)

## Related topics

- [[reaxff-family]]
