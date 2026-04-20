---
id: paper:2023uene-venue-paper
type: paper
title: "Supporting Information: Reactive Force Field MD Studies of BN Growth from BCl3 and NH3 by Atomic Layer Deposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
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
venue: "J. Phys. Chem. C (2024), Supporting Information"
pdf_sha256: "28a9050601e3978b83a8d2f58df5f5bd7a1b9a7229993e72f8b84d1e26d85afd"
pdf_path: "papers/Uene_2024_BN_BCl3_JPC_SI.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2023uene-venue-paper -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Publisher **Supporting Information** for the **BN ALD** study using **BCl\(_3\)** and **NH\(_3\)**: the extract includes the **tabulated ReaxFF parameter file** (global + element/block entries) accompanying **[[2024naoya-uene-j-phys-chem-reactive-force]]**. This file enables reproducing the reactive MD setup and parameter provenance described in the main article.

## Methods

SI tables of ReaxFF coefficients; auxiliary material standard for JPCC article packages.

The article further notes that reactive MD-force field,BN-ALD using BCl3 and NH3, N.Uene et.al 39 !

## Findings

Provides **full numeric parameter set** for the trained **B/Cl/N/H** chemistry used in ALD-cycle simulations (see main paper for training targets and validation).


From the abstract: nr of atoms; cov.r; valency;a.m;Rvdw;Evdw;gammaEEM;cov.r2;# alfa;gammavdW;valency;Eunder;Eover;chiEEM;etaEEM;n.u. cov r3;Elp;Heat inc.;bo131;bo132;bo133;softcut;n.u. ov/un;val1;n.u.;val3,vval4 C 1.3727 4.0000 12.0000 2.0270 0.1113 0.5516 1.1706 4.0000 9.2293 4.5389 4.0000 30.0000 79.5548 4.4087 7.0601 0.0000 1.1168 0.0000 181.0000 14.5210 24.9431 6.7313 0.8563 0.0000 -6.7437 5.6329 1.0564 4.0000 2.9663 0.0000 0.0000 0.0000 H 0.7112 1.0000 1.0080 1.6724 0.0529 0.7512 -0.1000 1.0000 8.3100 4.3031 1.0000 0.0000 121.1250 3.5442 9.4838 1.0000 -0.1000 0.0000 61.3948 2.8015 2.1485 0.0003 1.0698 0.0000.

## Limitations

SI PDF does not substitute for reading the main text’s cycle protocol, timestep choices, and surface models.

## Relevance to group

Archived **force-field disclosure** for **industrial ALD + academic collaboration** work on **2D BN** processing.

## Citations and evidence anchors

Primary article DOI (same work): https://doi.org/10.1021/acs.jpcc.3c06704

## Related topics

- [[2024naoya-uene-j-phys-chem-reactive-force]]