---
id: paper:2024naoya-uene-j-phys-chem-reactive-force
type: paper
title: "Reactive Force Field Molecular Dynamics Studies of the Initial Growth of Boron Nitride Using BCl3 and NH3 by Atomic Layer Deposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - domain:reactive-md
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c06704"
year: 2024
authors:
  - "Naoya Uene"
  - "Takuya Mabuchi"
  - "Masaru Zaitsu"
  - "Shigeo Yasuhara"
  - "Adri C. T. van Duin"
  - "Takashi Tokumasu"
venue: "J. Phys. Chem. C 128, 1075–1086 (2024)"
pdf_sha256: "b14124f29f7821562d223f0153fa2cf17a621b9e2abb2f772d19ac84d08f13e3"
pdf_path: "papers/Uene_2024_BN_BCl3_JPC.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024naoya-uene-j-phys-chem-reactive-force -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Develops a **ReaxFF** description for **BN ALD** from **BCl\(_3\)** + **NH\(_3\)**, trains bonded/geometry-sensitive terms against **DFT**, and runs **cycle-resolved ReaxFF MD** mimicking **pulse–purge ALD** steps. The growth story is decomposed into **surface diffusion**, **BN cluster nucleation/growth**, **HCl formation/diffusion/desorption**, and temperature-sensitive **competition** between **3D cluster growth** vs **2D film growth** across five simulated cycles. **Substrate temperature** modulates **initial growth mode** and **film thickness**—too-high **T** accelerates **desorption** of gases/clusters, suppressing film thickening in the regimes explored.

## Methods

DFT training data for gas-phase and surface reactions; ReaxFF optimization; **four-step** ALD loop (BCl\(_3\) pulse → purge → NH\(_3\) pulse → purge) with repeated cycling; analysis of intermediate surface species and defect/cluster metrics.

## Findings

Mixed **3D cluster + 2D terrace** growth emerges; **moderate T** favors cluster persistence/growth while **excessive T** encourages desorption-dominated kinetics and thinner films; HCl chemistry is a first-class kinetic participant.

## Limitations

Simulation duration/cycles are still far below industrial wafer-scale times; surface models omit full reactor fluid dynamics—ALD **macroscale coupling** is named as future work in the abstract.

## Relevance to group

Industrial **ALD** collaboration (**Japan Advanced Chemicals / Tohoku**) with **van Duin** co-authorship; complements gas-phase **BN** synthesis papers (**[[20220000-0002-1558-1560-x-reaxff-force]]**) with a **surface-process** viewpoint.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpcc.3c06704 — Abstract (~pp. 1–2) lists ALD loop stages and growth steps (i–v).

## Related topics

- [[2023uene-venue-paper]]
- [[20220000-0002-1558-1560-x-reaxff-force]]
- [[reaxff-family]]
