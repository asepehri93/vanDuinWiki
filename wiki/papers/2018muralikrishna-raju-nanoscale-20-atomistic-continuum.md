---
id: paper:2018muralikrishna-raju-nanoscale-20-atomistic-continuum
type: paper
title: "Atomistic and continuum scale modeling of functionalized graphyne membranes for water desalination"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - material:graphene-carbon-nano
  - method:classical-md
  - method:continuum-or-mesoscale
  - task:application
  - scale:multiscale
candidate_tags: []
source_refs: []
doi: "10.1039/c7nr07963j"
year: 2018
authors:
  - "Muralikrishna Raju"
  - "Pavan B. Govindaraju"
  - "Adri C. T. van Duin"
  - "Matthias Ihme"
venue: "Nanoscale"
pdf_sha256: "9dd462ce05d18bbde5d613ca28d9d6b74376f7bf9367f70f1d73905c52dc3c4d"
pdf_path: "papers/Raju_Nanoscale_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018muralikrishna-raju-nanoscale-20-atomistic-continuum -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Nanoscale** article evaluates **α-** and **γ-graphyne** membranes—bare and **hydrogenated**, with varied **pore chemistry** and **geometry**—as **desalination** candidates using **classical MD** for **atomistic transport** metrics and **continuum-scale** analysis for **cross-flow reverse-osmosis** device context. **MD** predicts extremely high **intrinsic water permeability** and strong **ion rejection** for certain **pore sizes**, while the **continuum upscaling** argues that **module-level transport limitations** partially blunt the **MD-only** advantage—yet still project **meaningful energy / recovery** improvements versus **thin-film composite** benchmarks under stated assumptions. **Adri C. T. van Duin** is a coauthor on the **atomistic** modeling thread.

## Methods

- **Classical MD** for **pressure-driven** water flow, **ion rejection**, and **pore energetics** (see force field and setup details in the paper).
- **Continuum transport** model coupling to interpret **process-scale** implications.

## Findings

- **Pores ~20–50 Å²** (as categorized in the abstract) can reject **>90%** of ions up to **1 GPa** applied pressure in the **MD** protocol described.
- **Permeability** trends are explained with **in-pore water velocity**, **density**, and **energy barrier** analyses.
- **Upscale RO analysis** tempers, but does not eliminate, the **permeability benefit** vs **commercial** membranes.

## Limitations

- **Classical force fields** for **graphyne–water–ion** systems have **uncertainty** near **sub-nm** pores; **quantitative** barriers benefit from **QM spot checks**.
- **Manufacturability** of **graphyne** remains a **materials synthesis** challenge outside the simulation scope.

## Relevance to group

Shows **van Duin-group participation** in **2D nanoporous carbon** **water** modeling coupled to **engineering-scale** interpretation.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/c7nr07963j` (`papers/Raju_Nanoscale_2018.pdf`).

## Related topics

- [[reaxff-family]]
