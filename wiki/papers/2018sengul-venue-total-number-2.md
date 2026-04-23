---
id: paper:2018sengul-venue-total-number-2
type: paper
title: "Total Number of pages:7 (author proof, corrected)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
paper_keywords:
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: ""
year: 2018
authors:
  - "Mert Y. Sengul"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. (author proof PDF, corrected)"
pdf_sha256: "d13ae14f8928080652136ca6b535f294b17054f27b8c1bbe63f1de9e38126e41"
pdf_path: "papers/Sengul_aceticacid_water_JCP_2018_proof_corrected.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2018sengul-venue-total-number-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    This page describes a **non-version-of-record** author proof PDF in the corpus. Scientific content is summarized on the version-of-record article page [[2018sengul-venue-reaxff-molecular]] (see also the uncorrected proof [[2018sengul-venue-total-number]]).

## Summary

This corpus file is an **AIP eProof** PDF for *The Journal of Chemical Physics* (article checklist and publisher queries on the first pages, then the manuscript body). It is the **corrected** proof variant (`Sengul_aceticacid_water_JCP_2018_proof_corrected.pdf`); the substantive research is the same reactive molecular dynamics study of **acetic acid–water** mixtures across ambient and **supercritical** conditions reported in the version-of-record article. The proof exists so authors could answer copy queries and confirm figures before typesetting; it should not be treated as the canonical paginated article for citation, but it preserves the same scientific narrative as the online journal PDF.

## Methods

This note does not replace the full **Methods** on [[2018sengul-venue-reaxff-molecular]], which is grounded in `papers/Sengul_aceticacid_water_JCP_2018_online.pdf` and the article text. In brief, the work merges **ReaxFF** water and biomolecular acetic-acid parameters, adjusts **O–C–O valence conjugation** so that **metadynamics** on acetic acid dissociation reproduces a realistic **acid dissociation constant** (\(K_a\)), and then runs **canonical molecular dynamics** in **ADF** with **0.25 fs** timesteps, **Berendsen** thermostats, and **1000-molecule** cells. Simulations scan composition and density, heat to high temperature in controlled steps, and analyze **radial distribution functions**, hydrogen-bond statistics, and clustering in **acid-rich** versus **water-rich** regimes, including supercritical states where hydrogen-bond criteria are broadened. Readers reproducing the study should follow timestep, ensemble, equilibration lengths, and analysis windows exactly as listed on the primary article page and in the published paper.

## Findings

The proof carries the same conclusions as [[2018sengul-venue-reaxff-molecular]]: at ambient conditions, **cyclic dimers** and **chain-like** acetic acid assemblies appear when the mixture is acid-rich, while added water disrupts those motifs and shifts pair correlations toward dipole-like **~4 Å** features. **Water–water** structure matches experimental-like shells at high water content and becomes increasingly distorted as acetic acid dominates. In the **supercritical** regime, longer-range order weakens relative to ambient liquid structure, yet some **first-neighbor** acid–water correlations persist at lower supercritical temperatures before fading at higher temperatures within the range examined. These statements mirror the primary article’s **Results** and are not independent experimental findings of this wiki.

## Limitations

Proof PDFs may differ slightly from the final typeset article in pagination, figure coloring, or copy edits; use the publisher’s final version for citation-critical text.

## Reader notes (navigation)

- Version-of-record article: [[2018sengul-venue-reaxff-molecular]]
- Related ACS interface study (ZnO / cold sintering): [[2018sengul-acs-reaxff-molecular]]

## Related topics

- [[reaxff-family]]
