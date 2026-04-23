---
id: concept:theme-water-silica-geo
type: concept
title: "Theme: water at silica and geochemical interfaces (ReaxFF corpus)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "O2 + hydroxylated silica; water-related surface chemistry"
  - paper_id: "paper:2019hahn-j-phys-chem-surface-reactivity"
    note: "Silicate glass surface reactivity"
  - paper_id: "paper:2018ho-venue-paper"
    note: "Oxide / surface context in corpus"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Electrolyte interfaces (water-in-salt adjacency)"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Aqueous/catalytic C-O chemistry overlap"
supported_by:
  - "paper:2013muri-venue-jp3086649"
  - "paper:2019hahn-j-phys-chem-surface-reactivity"
---

<!-- id:concept:theme-water-silica-geo -->

!!! abstract "TL;DR"

    This theme synthesizes how the corpus treats water-exposed silica and related oxide interfaces, with emphasis on hydroxyl chemistry, oxygen reactivity, and interfacial structuring in ReaxFF-oriented studies. It bridges oxide surface chemistry pages with electrolyte-adjacent interface pages in the broader knowledge base.

## Scope (in / out)

This page covers corpus evidence on hydroxylated silica, silicate glass surfaces, and nearby oxide interfaces where explicit water, hydroxyl exchange, or proton-relevant interfacial chemistry appears in linked paper pages.

It is out of scope for bulk aqueous electrolyte thermodynamics that do not center a mineral or oxide interface; those questions route more directly to [[batteries-interfaces-reaxff]] and related electrolyte-focused hubs.

## How this theme is organized in the corpus

The corpus material groups into four subthemes: hydroxylated silica oxygen chemistry, silicate glass surface reactivity, electrolyte-adjacent interfacial structuring, and aqueous catalytic overlap. These subthemes are connected by interface chemistry, but they remain methodologically heterogeneous across parameter sets, simulation setups, and reported observables.

## Literature review (this knowledge base)

This is a corpus-scoped synthesis rather than a complete world literature review. The statements below summarize what is represented in linked wiki paper pages and their associated publication context.

### Hydroxylated silica and oxygen/water-related surface chemistry

[[2013muri-venue-jp3086649]] is a key entry point for oxygen interactions at hydroxylated silica interfaces in this corpus. It grounds questions about how local hydroxyl environments and oxygen-accessible sites influence the pathways explored in reactive interfacial simulations.

### Silicate glasses and surface reactivity

[[2019hahn-j-phys-chem-surface-reactivity]] extends the interface perspective to silicate glass surface reactivity and provides a second anchor for this theme. In corpus navigation terms, [[2018ho-venue-paper]] offers adjacent oxide and surface context that is useful for routing related questions, even when mechanistic emphasis differs across pages.

### Electrolyte interfaces (water structuring adjacency)

[[2018shin-physical-che-development-reaxff]] is curated primarily as an electrolyte-interface page, but it remains relevant here for queries on water or salt structuring near solid-like interfacial environments. Within this theme, it should be interpreted as adjacency evidence rather than as a direct substitute for silica-specific mechanistic studies.

### Catalytic aqueous chemistry overlap

[[2015broqvist-venue-jp5b01597]] connects this theme to aqueous or hydrogen-bonded catalytic C-O chemistry contexts. It is most useful when cross-reading with [[theme-catalysis-surfaces]] for interface questions that involve both surface reactivity and liquid-like chemical environments.

## Analysis and cross-cutting patterns

A recurring pattern across these pages is that interfacial water behavior depends strongly on local surface chemistry and on how reactive charge transfer and bond rearrangements are represented in the selected force-field setup. The same high-level question about water at oxide interfaces often maps to different evidence granularity depending on whether a page focuses on hydroxylated silica reactions, glass reactivity, or electrolyte-adjacent structuring. This enables thematic synthesis, but quantitative transfer across pages should remain cautious unless comparable protocols and validation targets are explicitly aligned.

## Debates, tensions, and limitations

One persistent tension is proton activity fidelity: reactive classical frameworks may not represent all relevant proton-transport behavior equally across hydration regimes, and interpretation depends on each paper's specific modeling assumptions. A second tension is scale: atomistic interface studies provide mechanistic detail at short length and time scales, but they do not by themselves establish complete geochemical dissolution or long-range transport behavior. A third limitation is cross-subtheme interoperability, because silica-focused, glass-focused, and electrolyte-adjacent pages often use different assumptions and validation objectives. Related framing and neighboring evidence are in [[theme-oxides-silica-ceramics]], [[theme-catalysis-surfaces]], and [[batteries-interfaces-reaxff]].

## Gaps and open directions (corpus view)

The current corpus is still thin on studies that bridge atomistic interfacial reactions to mesoscale or field-scale geochemical transport outcomes. It also has limited harmonized benchmark-style comparisons in which multiple interface chemistries are evaluated under matched sampling lengths, boundary choices, and validation metrics. As a result, this hub currently supports interface-level hypothesis generation and evidence routing, but not broad-condition model selection by itself.

## Methods and limitations

The underlying evidence relies on reactive force-field simulations whose conclusions can be sensitive to parameterization lineage, charge-equilibration treatment, and thermodynamic boundary conditions. Interfacial observables such as water structuring, wetting behavior, and reaction propensity can shift with system size, equilibration strategy, and trajectory length, so each claim should be interpreted inside the protocol context reported on the linked paper page. When users need cross-material or cross-scale transfer, this theme should be paired with protocol and debate pages before drawing strong comparative conclusions.

## Representative entry points

- Silica hydroxyl and oxygen interface chemistry: [[2013muri-venue-jp3086649]].
- Silicate glass surface reactivity and adjacent oxide context: [[2019hahn-j-phys-chem-surface-reactivity]], [[2018ho-venue-paper]].
- Electrolyte-adjacent interfacial structuring context: [[2018shin-physical-che-development-reaxff]].
- Domain index routing: [[paper-index-by-domain]] under `domain:water-silica-geo`.

??? info "MAS / retrieval"

    **id:** `concept:theme-water-silica-geo`. Tag new papers with `domain:water-silica-geo` when explicit water or hydroxyl equilibria on oxide or silicate interfaces are central. Refresh `source_refs` when new silica-water interface pages are added to keep this hub retrieval-grounded.
