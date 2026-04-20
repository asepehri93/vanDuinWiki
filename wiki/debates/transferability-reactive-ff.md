---
id: debate:transferability-reactive-ff
type: debate
title: "Transferability of reactive force fields across phases and chemistries"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, task:review, scale:atomistic]
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Shows composition-specific validation for ceramic electrolyte systems"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    note: "Different chemistry (liquid carbonate) — different training needs"
positions:
  - name: "Strong locality"
    summary: "A ReaxFF fit is reliable only for element combinations and coordination environments represented in its training set."
  - name: "Pragmatic reuse"
    summary: "Teams often reuse published sets as starting points and re-fit subsets when moving to adjacent chemistries."
evidence:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Discussion"
    note: "supports Strong locality — ionic conductivity trends vs composition"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Abstract"
    note: "supports need for chemistry-specific extension (liquid electrolytes)"
---

<!-- id:debate:transferability-reactive-ff -->

!!! abstract "TL;DR"

    **Reactive FF transferability** is not a single yes/no: it splits into **element coverage**, **phase** (crystal vs amorphous vs liquid), and **reaction classes** included in QM training. The KB documents many **fit-for-purpose** successes and **explicit caveats**.

## Positions

**Strong locality:** extrapolating a parameter set to **new stoichiometries** or **unsampled reaction channels** is scientifically fragile without new training data.

**Pragmatic reuse:** published sets are often **starting points**; incremental reparameterization is normal practice in the cited battery and oxide work.

## Evidence summary

- Ceramic electrolyte / **LATP**-class behavior and MC/MD sampling of disorder: [[2018shin-physical-che-development-reaxff]].  
- **Organic carbonate** electrolyte chemistry requiring **different** bond types: [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]].  
- Cross-cutting overview: [[reaxff-family]], [[theme-oxides-silica-ceramics]].

## Open questions

Where should the KB **flag** “same element set, different phase” as a **high-risk** transfer? Maintainer policy: tag `confidence` on paper pages when extraction is partial.

## Key references

See YAML `evidence` and `source_refs`; browse the [papers index](../papers/index.md) for parameterization bibliography.
