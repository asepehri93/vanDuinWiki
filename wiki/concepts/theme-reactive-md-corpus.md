---
id: concept:theme-reactive-md-corpus
type: concept
title: "Theme: reactive molecular dynamics in this corpus (method hub)"
updated: "2026-04-21"
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
---

<!-- id:concept:theme-reactive-md-corpus -->

!!! abstract "TL;DR"

    This hub routes **method** questions about **reactive molecular dynamics**—with **ReaxFF** or other reactive models used in the corpus—**separately** from [[reaxff-family]] and [[protocols/reaxff-parameterization-workflow]], which document **parameterization lineage** and training workflows. Use domain hubs ([[theme-oxides-silica-ceramics]], [[theme-2d-epitaxy-growth]], …) for **material-first** synthesis.

## Scope (in / out)

**In corpus:** papers whose wiki notes describe **bond-making/breaking MD**, **QM-informed reactive MD**, **ReaxFF application studies**, **reactive electrolyte** chemistry, **shock/reactive** protocols, or **QM/MM** when the note supports it.

**Out of scope here:** pure **force-field fitting** narratives without an application trajectory—those belong with **ReaxFF lineage** pages. **Non-reactive** classical MD surveys belong under **mechanics** or **material** themes unless reactivity is central.

## How this theme is organized in the corpus

Subsections below mirror **how work is tagged in KB paper pages**, not a universal taxonomy. Prefer **`method:`** tags on each `[[slug]]` and the domain index when this hub is too broad.

## Literature review (this knowledge base)

### Reactive MD with ReaxFF (applications)

Coal and hydrocarbon **pyrolysis** at scale is documented in [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]]. **Metal oxidation** and **oxygen transport** appear in [[2014zou-acta-materia-molecular-dynamics]]. **Silica and O₂** surface chemistry is developed in [[2013muri-venue-jp3086649]]. **Graphene intercalation** and **defect** pathways appear in [[2022nayir-carbon-190-2-atomic-scale-probing]].

### Reactive MD with first-principles-based or hybrid flavors

[[2017liu-venue-research]] reports **first-principles-based reactive MD** for **h-BN** nucleation on **Ni**—read that page for the exact **reactive Hamiltonian** stack and validation.

### Electrolytes and interfaces (reactive bond networks)

[[2018shin-physical-che-development-reaxff]] and [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] illustrate **reactive** treatments of **ceramic** and **carbonate** electrolyte chemistry in this KB. Route battery-context questions to [[batteries-interfaces-reaxff]] when the **cell chemistry** is the headline.

### Combustion- and high-T organic networks

[[2018jain-j-phys-chem-understanding-combustion]] supports **combustion-oriented** reactive MD threads; pair with [[theme-combustion-flames-fuels]] for **fuel/flame** framing and [[theme-pyrolysis-combustion-organics]] for **slow thermal** organics.

### Catalytic surfaces

[[2015broqvist-venue-jp5b01597]] anchors **heterogeneous** reactive surface chemistry; see [[theme-catalysis-surfaces]] for catalyst-first organization.

### 2D materials, water droplets, and defects

[[2021verma-physical-che-reaxff-reactive]] couples **defective h-BN**, **water**, and **ReaxFF** reactive MD—use alongside [[theme-2d-epitaxy-growth]] and [[theme-water-silica-geo]].

## Analysis and cross-cutting patterns

Across linked pages, **timestep**, **thermostat**, and **system size** reporting varies by subfield; **comparability** claims should be checked on each paper note. Where papers give both **barrier** or **energetic** benchmarks and ReaxFF results, those comparisons belong in the **paper** summary—not generalized here without citations.

## Debates, tensions, and limitations

- **Transferability** of reactive models: [[transferability-reactive-ff]], [[reaxff-vs-mlip-accuracy]].  
- **Sampling**: rare events may require specialized workflows not documented on every page—do not assume **single long MD** trajectories suffice.  
- **Disambiguation:** training **new** ReaxFF parameters vs **running** published parameters—use lineage docs vs this hub accordingly.

## Gaps and open directions (corpus view)

The KB does not guarantee **uniform** coverage of **accelerated sampling**, **adaptive kinetic Monte Carlo**, or **every** QM/MM coupling variant; where those appear, they will be **paper-specific**. This hub should gain more `source_refs` as new **method-forward** notes are curated.

## Representative entry points

- **Large-scale organics:** [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]].  
- **Electrolytes:** [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]].  
- **2D / graphene:** [[2022nayir-carbon-190-2-atomic-scale-probing]].  
- **Combustion:** [[2018jain-j-phys-chem-understanding-combustion]].  
- **Index by method:** [[paper-index-by-domain]] (combine `method:*` tags in individual notes).

## Methods and limitations

Reactive MD inherits **force-field** limitations of whichever model is used; **quantitative** kinetics generally need **validation** against experiment or higher-level theory on a per-system basis.

??? info "MAS / retrieval"

    **id:** `concept:theme-reactive-md-corpus`. Use `domain:reactive-md` when ingesting **method-primary** pages; keep **material** `domain:*` tags as well so domain hubs remain discoverable. Refresh `source_refs` when adding **method-forward** paper notes.
