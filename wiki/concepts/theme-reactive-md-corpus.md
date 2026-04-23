---
id: concept:theme-reactive-md-corpus
type: concept
title: "Theme: reactive molecular dynamics in this corpus (method hub)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
    note: "Large-scale reactive MD (ReaxFF) for coal pyrolysis"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Surface CO₂ hydrogenation with ReaxFF"
  - paper_id: "paper:2017liu-venue-research"
    note: "First-principles-based reactive MD (h-BN nucleation on Ni)"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Reactive MD for ceramic electrolyte compositions"
  - paper_id: "paper:2018jain-j-phys-chem-understanding-combustion"
    note: "Reactive MD / combustion chemistry (ReaxFF-class workflows)"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    note: "Liquid electrolyte decomposition pathways (reactive)"
  - paper_id: "paper:2022nayir-carbon-190-2-atomic-scale-probing"
    note: "Defect-assisted intercalation through graphene (ReaxFF MD)"
  - paper_id: "paper:2021verma-physical-che-reaxff-reactive"
    note: "Reactive MD for defective h-BN with water nanodroplets"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Reactive MD for Ni oxidation and O transport"
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "Reactive O₂ + hydroxylated silica surfaces"
supported_by:
  - "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
  - "paper:2015broqvist-venue-jp5b01597"
  - "paper:2017liu-venue-research"
  - "paper:2018shin-physical-che-development-reaxff"
  - "paper:2018jain-j-phys-chem-understanding-combustion"
  - "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
  - "paper:2022nayir-carbon-190-2-atomic-scale-probing"
  - "paper:2021verma-physical-che-reaxff-reactive"
  - "paper:2014zou-acta-materia-molecular-dynamics"
  - "paper:2013muri-venue-jp3086649"
---

<!-- id:concept:theme-reactive-md-corpus -->

!!! abstract "TL;DR"

    This is the method hub for reactive molecular dynamics in this corpus: where and how bond-breaking or bond-forming trajectories are used in practice. It is intentionally separate from [[reaxff-family]] and [[protocols/reaxff-parameterization-workflow]], which track parameter-set lineage and fitting workflows rather than application-side interpretation.

## Scope (in / out)

**In scope:** corpus pages that report reactive trajectories (ReaxFF or other reactive Hamiltonians), including electrolyte decomposition, oxidation, pyrolysis, combustion, intercalation, and surface reaction use cases documented in linked paper notes.

**Out of scope:** force-field training history without an application trajectory (route to [[reaxff-family]] and [[protocols/reaxff-parameterization-workflow]]), and non-reactive classical MD surveys where reactivity is not central.

**Routing rule (method vs lineage):**
- If the user asks, "What chemistry emerges in trajectories under conditions X?", start here.
- If the user asks, "Which parameter set was fit to what data, and how transferable is that fit?", start at [[reaxff-family]] and then [[protocols/reaxff-parameterization-workflow]].

## How this theme is organized in the corpus

Subsections below reflect corpus organization rather than a universal taxonomy. They are intended to speed retrieval across method-first questions while preserving links back to material and domain hubs.

## Literature review (this knowledge base)

### Reactive MD with ReaxFF (applications)

The corpus includes large-scale pyrolysis trajectories in [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]], oxidation and oxygen-transport behavior in [[2014zou-acta-materia-molecular-dynamics]], reactive silica surface chemistry in [[2013muri-venue-jp3086649]], and defect-mediated graphene intercalation behavior in [[2022nayir-carbon-190-2-atomic-scale-probing]].

### Reactive MD with first-principles-based or hybrid flavors

[[2017liu-venue-research]] documents a first-principles-based reactive MD treatment for h-BN nucleation on Ni, and should be used as the detailed reference point for that Hamiltonian and validation setup.

### Electrolytes and interfaces (reactive bond networks)

[[2018shin-physical-che-development-reaxff]] and [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] anchor reactive electrolyte and interface chemistry threads in this KB. When the question is battery-context first (rather than method-first), route through [[batteries-interfaces-reaxff]].

### Combustion- and high-T organic networks

[[2018jain-j-phys-chem-understanding-combustion]] provides a combustion-oriented reactive MD entry point. For fuel-centric framing, pair with [[theme-combustion-flames-fuels]] and [[theme-pyrolysis-combustion-organics]].

### Catalytic surfaces

[[2015broqvist-venue-jp5b01597]] anchors heterogeneous reactive surface chemistry in this corpus. For catalyst-family synthesis, use [[theme-catalysis-surfaces]].

### 2D materials, water droplets, and defects

[[2021verma-physical-che-reaxff-reactive]] connects defective h-BN, water nanodroplets, and reactive ReaxFF trajectories; combine with [[theme-2d-epitaxy-growth]] and [[theme-water-silica-geo]] for material-first navigation.

## Analysis and cross-cutting patterns

Across linked pages, reporting depth for timestep, ensemble control, and system size is uneven, so cross-paper comparability must be checked at the paper page level. This hub therefore summarizes where reactive MD is used, while numerical benchmarking and parameter-quality claims remain anchored to individual paper notes.

## Debates, tensions, and limitations

- **Transferability** of reactive models: [[transferability-reactive-ff]], [[reaxff-vs-mlip-accuracy]].  
- **Sampling**: rare events may require specialized workflows not documented on every page—do not assume **single long MD** trajectories suffice.  
- **Method-lineage split:** training or re-fitting parameters is a lineage/protocol concern, while trajectory interpretation under a chosen reactive model is a method/application concern.

## Gaps and open directions (corpus view)

The corpus does not yet provide uniform coverage of accelerated sampling variants, adaptive KMC couplings, or every QM/MM reactive workflow. As method-forward paper notes are expanded, this hub should be refreshed with additional `source_refs` and tighter cross-links to protocol and debate pages.

## Representative entry points

- **Large-scale organics:** [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]].  
- **Electrolytes:** [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]].  
- **2D / graphene:** [[2022nayir-carbon-190-2-atomic-scale-probing]].  
- **Combustion:** [[2018jain-j-phys-chem-understanding-combustion]].  
- **Index by method:** [[paper-index-by-domain]] (combine `method:*` tags in individual notes).

## Methods and limitations

Reactive MD interpretation depends on the chosen reactive Hamiltonian and parameter set, so quantitative kinetics and transferability should be treated as paper-scoped unless independently validated against experiment or higher-level calculations in the linked notes.

??? info "MAS / retrieval"

    **id:** `concept:theme-reactive-md-corpus`.
    **primary intent:** method-first routing for reactive trajectory questions.
    **disambiguation cues:** `method:reaxff` + `domain:reactive-md` indicate application usage; lineage and fitting provenance route to [[reaxff-family]] and [[protocols/reaxff-parameterization-workflow]].
    **query hints:** "reactive MD transferability", "bond breaking trajectory", "electrolyte decomposition reactive", "surface reaction ReaxFF", "combustion reactive trajectory".
    **maintenance note:** refresh `source_refs` and `supported_by` together when adding method-forward papers so retrieval and evidence graphs remain aligned.
