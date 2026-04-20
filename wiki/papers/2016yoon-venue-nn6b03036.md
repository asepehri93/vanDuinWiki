---
id: paper:2016yoon-venue-nn6b03036
type: paper
title: "Atomistic-scale simulations of defect formation in graphene under noble gas ion irradiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.6b03036"
year: 2016
authors:
  - "Kichul Yoon"
  - "Ali Rahnamoun"
  - "Jacob L. Swett"
  - "Vighter Iberi"
  - "David A. Cullen"
  - "Ivan V. Vlassiouk"
  - "Alex Belianinov"
  - "Stephen Jesse"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: "ACS Nano"
pdf_sha256: "0841b72e219d95fb553133d0a01f8ef46119e33ed435f6fe1b825443d8e8e005"
pdf_path: "papers/Yoon_ACSNano_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-nn6b03036 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** simulates **noble gas ion** bombardment of **graphene** followed by **annealing**, linking **dose**, **ion species**, and **energy** to **defect** populations and **nanopore** formation. Post-irradiation **relaxation** allows **vacancy-like** defects to **coalesce**; heavier ions and higher doses produce larger pores, consistent with **aberration-corrected STEM** and **helium ion microscopy** trends from **ORNL** collaborators. Defect statistics distinguish **Stone–Thrower–Wales** dominance under **He\(^+\)** vs **monovacancies** for heavier ions.

## Methods

- **Reactive MD** with **ReaxFF** including dynamical **collision** cascades and subsequent **thermal** treatment.
- Correlative **electron microscopy** datasets for qualitative validation.

## Findings

- **Simulation** and **experiment** broadly agree on **dose-dependent** damage evolution and **amorphization** at high dose.
- Mechanistic vignettes include **Frenkel** pair evolution into **STW** defects and competing **healing** pathways.

## Limitations

- **Electronic** stopping is neglected; **beam** parameters between **simulation** and **experiment** are not always identical (**Ne\(^+\)** conditions called out as mismatched).

## Relevance to group

**van Duin** coauthored **ACS Nano** flagship on **ReaxFF** for **ion-induced** **graphene** defects.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acsnano.6b03036` (`papers/Yoon_ACSNano_2016.pdf`).

## Related topics

- [[reaxff-family]]
