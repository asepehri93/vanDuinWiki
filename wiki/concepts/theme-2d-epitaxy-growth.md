---
id: concept:theme-2d-epitaxy-growth
type: concept
title: "Theme: 2D materials, epitaxy, and growth simulations (corpus)"
updated: "2026-04-21"
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

    This hub organizes **two-dimensional** and **layered** materials work in the KB—**epitaxy**, **CVD/MOCVD**, **defect-assisted** processes, and **ReaxFF** development for **TMDs**, **h-BN**, and **graphene** stacks. It complements [[graphene-nanocarbon]] (carbon-centric parameters) and [[theme-reactive-md-corpus]] (method spine).

## Scope (in / out)

**In corpus:** papers tagged `domain:2d-layered` whose notes discuss **growth**, **substrate** interactions, **precursor** chemistry, **defects**, or **ReaxFF** extensions for **2D** systems.

**Out of scope:** generic **bulk oxide** ceramics without a **2D** framing (see [[theme-oxides-silica-ceramics]]).

## How this theme is organized in the corpus

The authoritative **full table** of `domain:2d-layered` slugs is [[paper-index-by-domain]]; this page highlights **representative** notes and **cross-links**—not every row is named.

## Literature review (this knowledge base)

### Reviews and modeling perspectives

[[2023nadire-nayir-2d-materials-modeling-simulations-2]] and [[2020momeni-npj-computat-multiscale-computational]] provide **corpus-level** entry points for **modeling** and **multiscale** growth narratives. Use them to locate **terminology** and **further** `[[wikilinks]]` inside the KB.

### Frameworks for CVD / MOCVD and gas-phase chemistry

[[2022momeni-npj-computat-computational-framework]] and [[2021momeni-journal-of-m-computational-synthesis]] document **computational** workflows for **wafer-scale** and **CVD** contexts. [[2019xuan-journal-of-c-multi-scale-modeling]] treats **gas-phase** reaction networks coupled to **WSe₂** growth questions.

### Graphene, intercalation, and defects

[[2022nayir-carbon-190-2-atomic-scale-probing]] studies **defect-assisted** **Ga** intercalation through **graphene** with ReaxFF MD—pair with [[graphene-nanocarbon]] for **parameter** discussions.

### h-BN and TMD nucleation

[[2017liu-venue-research]] focuses on **h-BN** **nucleation** on **Ni** using **first-principles-based reactive MD**. [[2022i-ponomarev-j-phys-chem-new-reactive]] develops **ReaxFF** for **MoS₂** **crystallization** pathways.

## Analysis and cross-cutting patterns

Across these notes, **substrate** choice and **precursor** partial pressures recur as **control knobs**; **quantitative** agreement with **experiment** is **paper-specific**. **Duplicate** or **proof** PDFs appear in this domain—see the maintainer catalog in the repo (`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`) when a page explains **non-primary** corpus roles.

## Debates, tensions, and limitations

- **ReaxFF** parameter sets are often **element-subset** specific—check each paper for **coverage**.  
- **ML / neural** potentials enter some **mechanics** and **defect** studies—see [[theme-ml-atomistic-potentials]].  
- **Reactive vs non-reactive** stages in multiscale pipelines: read methods sections carefully.

## Gaps and open directions (corpus view)

The **2D** domain table is large; this hub will remain **selective** until more slugs are woven into narrative bullets—prefer adding **`[[wikilinks]]` here** when a paper note is **mature**.

## Representative entry points

- **Modeling perspective:** [[2023nadire-nayir-2d-materials-modeling-simulations-2]].  
- **Growth frameworks:** [[2022momeni-npj-computat-computational-framework]].  
- **Graphene intercalation:** [[2022nayir-carbon-190-2-atomic-scale-probing]].  
- **h-BN nucleation:** [[2017liu-venue-research]].  
- **Full list:** [[paper-index-by-domain]] (`domain:2d-layered`).

## Methods and limitations

**Epitaxy** MD often uses **small** patches or **idealized** interfaces; **long-wavelength** **strain** from **misorientation** may require **continuum** or **multiscale** coupling beyond a single reactive MD run.

??? info "MAS / retrieval"

    **id:** `concept:theme-2d-epitaxy-growth`. Tag `domain:2d-layered` on new papers; add bullets here when a note is a **strong** growth/epitaxy anchor.
