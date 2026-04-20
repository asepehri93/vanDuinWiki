---
id: paper:2022yawei-gao-j-phys-chem-al-reaxff
type: paper
title: "C/H/O/F/Al ReaxFF Force Field Development and Application to Study the Condensed-Phase Poly(vinylidene fluoride) and Reaction Mechanisms with Aluminum"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - material:polymer-organic
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c02043"
year: 2022
authors:
  - "Yawei Gao"
  - "Wenbo Zhu"
  - "Tao Wang"
  - "Dundar E. Yilmaz"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 126, 11058–11074 (2022)"
pdf_sha256: "699d3ae0c158c43c2f4c27d851ccbf42be36c0272168b2a05c96be2bc7751d7b"
pdf_path: "papers/Gao_Zhu_PVDF_Al_JPC_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022yawei-gao-j-phys-chem-al-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Develops a **C/H/O/F/Al ReaxFF** for **poly(vinylidene fluoride) (PVDF)** spanning **nonreactive** (polymorph / phase transformation) and **reactive** (pyrolysis and metal oxide surface chemistry) regimes. Low-temperature work explores **α → β** transitions under **electric poling** and **mechanical deformation**, reporting orientation-dependent **field thresholds** (e.g., ~**5** vs **7.5 GV/m** in excerpted directions) and showing how **stretch** can produce **all-trans** chains with **antiparallel packing** (zero net polarity) unless combined poling strategies are used. High-temperature chemistry treats **surface-oxidized Al nanoparticles**, emphasizing **HF** generation routes, **alumina fluorination/hydroxylation**, **water** evolution, and **AlC\(_x\)** side products—supporting analysis of **Al–PVDF energetic composites**.

## Methods

ReaxFF training against **QM** data and selected experimental constraints; MD sampling of PVDF crystal phases under **E-field** and **strain**; elevated-temperature reactive trajectories for PVDF with **oxidized Al** surfaces; Arrhenius-style analysis where reported for selected pathways.

## Findings

Demonstrates **transferability** across temperature windows; quantifies **poling/deformation** interplay for **ferroelectric β** promotion; maps multi-step **fluorination/oxidation** sequences at alumina interfaces consistent with expected pyrolysis product hierarchy.

## Limitations

ReaxFF cannot capture electronic polarization and band-structure effects; predicted field thresholds are classical-model dependent and should be interpreted as comparative trends.

## Relevance to group

Core **PVDF + aluminum combustion/ferroelectric** angle with explicit **parameterization** narrative—fits the group’s **reactive organofluorine + metal oxide** portfolio.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpcc.2c02043 — Abstract summarizes dual low-/high-T scope; Introduction anchors PVDF polymorphism context.

## Related topics

- [[reaxff-family]]
