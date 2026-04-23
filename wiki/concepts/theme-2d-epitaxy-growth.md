---
id: concept:theme-2d-epitaxy-growth
type: concept
title: "Theme: 2D materials, epitaxy, and growth simulations (corpus)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2023nadire-nayir-2d-materials-modeling-simulations-2"
    note: "ReaxFF perspective on 2D materials modeling"
  - paper_id: "paper:2022nayir-carbon-190-2-atomic-scale-probing"
    note: "Graphene intercalation and defects (ReaxFF MD)"
  - paper_id: "paper:2022momeni-npj-computat-computational-framework"
    note: "MOCVD growth framework for 2D materials (multiscale)"
  - paper_id: "paper:2021momeni-journal-of-m-computational-synthesis"
    note: "Computational synthesis of CVD-grown 2D materials"
  - paper_id: "paper:2020momeni-npj-computat-multiscale-computational"
    note: "Multiscale review of 2D growth (corpus touchpoint)"
  - paper_id: "paper:2019xuan-journal-of-c-multi-scale-modeling"
    note: "Gas-phase reactions in MOCVD growth of WSe₂"
  - paper_id: "paper:2017liu-venue-research"
    note: "h-BN nucleation on Ni (reactive MD)"
  - paper_id: "paper:2022i-ponomarev-j-phys-chem-new-reactive"
    note: "ReaxFF for MoS₂ crystallization"
supported_by:
  - "paper:2023nadire-nayir-2d-materials-modeling-simulations-2"
  - "paper:2022nayir-carbon-190-2-atomic-scale-probing"
  - "paper:2022momeni-npj-computat-computational-framework"
---

<!-- id:concept:theme-2d-epitaxy-growth -->

!!! abstract "TL;DR"

    This hub summarizes how the corpus treats two-dimensional material growth and epitaxy, with emphasis on CVD and MOCVD process modeling, substrate-coupled nucleation behavior, defect-enabled pathways, and reactive-force-field development for graphene, h-BN, and transition-metal dichalcogenide systems. It complements [[graphene-nanocarbon]] for carbon-focused parameterization context and [[theme-reactive-md-corpus]] for method-level reactive-MD framing.

## Scope (in / out)

This page is scoped to corpus papers that are tagged `domain:2d-layered` and contain explicit discussion of growth-relevant phenomena, including precursor chemistry, substrate interactions, nucleation and crystallization pathways, defect-mediated events, or force-field choices that materially affect simulated growth behavior.

It does not attempt to cover bulk-material simulation literature that lacks a 2D growth framing, and it does not function as a complete world-literature review outside the curated corpus represented by the linked paper pages.

## How this theme is organized in the corpus

The full inventory of slugs under `domain:2d-layered` is maintained in [[paper-index-by-domain]]. This hub is intentionally selective and organizes representative papers into synthesis threads so readers can move from broad perspective articles to mechanism-focused growth and nucleation studies without losing corpus provenance.

## Literature review (this knowledge base)

### Reviews and modeling perspectives

[[2023nadire-nayir-2d-materials-modeling-simulations-2]] and [[2020momeni-npj-computat-multiscale-computational]] function as corpus-level orientation papers. In this knowledge base, they anchor shared terminology for simulation workflows and establish the recurring separation between atomistic reactive events and process-scale growth interpretation.

### Frameworks for CVD / MOCVD and gas-phase chemistry

[[2022momeni-npj-computat-computational-framework]] and [[2021momeni-journal-of-m-computational-synthesis]] are used in the corpus as method-bridge references between reactor-scale CVD or MOCVD conditions and atomistic growth representations. [[2019xuan-journal-of-c-multi-scale-modeling]] adds a gas-phase reaction-network perspective tied to WSe2 growth, which is important in this corpus because it explicitly connects precursor-state assumptions to downstream deposition interpretations.

### Graphene, intercalation, and defects

[[2022nayir-carbon-190-2-atomic-scale-probing]] is the key corpus example for defect-assisted intercalation in graphene using reactive MD. In this hub, it supports the broader synthesis point that local defect structure can alter accessible pathways during layered-material processing, and it should be read with [[graphene-nanocarbon]] when parameter-coverage questions become central.

### h-BN and TMD nucleation

[[2017liu-venue-research]] contributes a substrate-specific h-BN nucleation case on Ni within a reactive simulation framework, while [[2022i-ponomarev-j-phys-chem-new-reactive]] contributes a MoS2-focused ReaxFF development and crystallization narrative. Together, these papers ground the corpus view that mechanistic claims are tightly coupled to both chemistry coverage and the target material system.

## Analysis and cross-cutting patterns

Across these linked papers, substrate identity, precursor-state assumptions, and defect availability repeatedly appear as practical control levers for simulated growth outcomes. The corpus also repeatedly indicates that transferability is conditional: conclusions are usually reliable inside the parameterization and process window discussed in each individual paper page, but they should not be generalized to all 2D growth regimes without additional validation anchors. This pattern is especially visible when moving between framework papers and material-specific reactive-MD studies.

## Debates, tensions, and limitations

The strongest recurring tension in this corpus is scope versus transferability of parameterizations. Several papers are useful for specific chemistry subsets or process windows, but they do not claim universal performance across all layered-material growth conditions. A second tension is representation across scales: reactor-level interpretations and atomistic reactive trajectories can be meaningfully linked, yet assumptions introduced at either scale can dominate inferred mechanisms. A third limitation is curation heterogeneity in source artifacts; some records in this domain correspond to non-primary or duplicate corpus files, so readers should use the page-level limitations language and the non-primary catalog when interpreting evidentiary strength.

## Gaps and open directions (corpus view)

The corpus contains more `domain:2d-layered` entries than are currently synthesized in this page narrative, so one clear gap is broader integration of additional mature paper notes into the thematic threads above. Another gap is more explicit cross-paper comparison language for when gas-phase, substrate-specific, and defect-mediated stories converge versus diverge. These are corpus-coverage gaps rather than claims about unknowns in the external literature.

## Methods and limitations

This page is a synthesis layer over existing corpus notes rather than a de novo extraction from every primary PDF in the domain. Its claims are therefore constrained to what the linked paper pages currently support and what their `source_refs` document. Where a linked paper is known to be SI-only, duplicate, or otherwise non-primary in corpus role, interpretation should follow the corresponding page limitations and, when needed, the maintainer catalog in `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

## Representative entry points

- For high-level modeling orientation, start with [[2023nadire-nayir-2d-materials-modeling-simulations-2]] and [[2020momeni-npj-computat-multiscale-computational]].
- For CVD or MOCVD process-to-atomistic framing, start with [[2022momeni-npj-computat-computational-framework]] and [[2021momeni-journal-of-m-computational-synthesis]].
- For gas-phase coupling in growth interpretation, use [[2019xuan-journal-of-c-multi-scale-modeling]].
- For defect-mediated pathway examples in graphene, use [[2022nayir-carbon-190-2-atomic-scale-probing]].
- For nucleation and crystallization cases in h-BN and TMD contexts, use [[2017liu-venue-research]] and [[2022i-ponomarev-j-phys-chem-new-reactive]].
- For the complete domain inventory, use [[paper-index-by-domain]] and filter on `domain:2d-layered`.

??? info "MAS / retrieval"

    **id:** `concept:theme-2d-epitaxy-growth`.
    **query hooks:** 2D growth, epitaxy, CVD, MOCVD, nucleation, defect-mediated growth, reactive MD, ReaxFF, WSe2, MoS2, h-BN, graphene intercalation.
    **tagging hint:** prioritize `domain:2d-layered` with method tags that distinguish reactive-MD mechanism work from multiscale process frameworks.
    **refresh rule:** when new `domain:2d-layered` paper pages gain stable methods/findings prose, update this hub narrative and expand `source_refs` to keep corpus-grounded synthesis current.
