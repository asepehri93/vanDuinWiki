---
id: concept:theme-porous-mof-zeolite
type: concept
title: "Theme: porous media, MOFs, and zeolites (corpus touchpoints)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:porous-mof-zeolite
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Catalytic surfaces (porous catalyst adjacency)"
  - paper_id: "paper:2013neyts-venue-c3nr00153a"
    note: "Surface reactions on nanostructured carbon"
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "Silica surfaces / pores (gas transport adjacency)"
  - paper_id: "paper:2019hahn-j-phys-chem-surface-reactivity"
    note: "Silicate glass surfaces"
supported_by:
  - "paper:2015broqvist-venue-jp5b01597"
  - "paper:2013neyts-venue-c3nr00153a"
---

<!-- id:concept:theme-porous-mof-zeolite -->

!!! abstract "TL;DR"

    This theme hub is a corpus-scoped routing page for porous and confined reactive environments. In this knowledge base, explicit MOF and zeolite coverage is still thinner than oxide and catalysis coverage, so most reliable entry points are adjacent papers on catalytic surfaces, carbon nanostructures, and silica or silicate interfaces.

## Scope (in / out)

**In corpus:** pages tagged `domain:porous-mof-zeolite` plus neighboring catalysis and surface papers where confinement or porous support is part of the modeled chemistry.

**Out of scope:** specific MOF topology behavior, zeolite framework comparisons, or transferability claims that are not explicitly documented on linked paper pages.

## How this theme is organized in the corpus

This page is organized as a navigation spine with two evidence-backed routes: (1) catalytic or reactive-surface questions with porous-context adjacency, and (2) silica or silicate surface chemistry that often maps to pore-wall environments in mesostructured systems. Use [[paper-index-by-domain]] to confirm current domain coverage before drawing broader conclusions.

## Literature review (this knowledge base)

This is a corpus review, not a full field review. The current evidence base here is ReaxFF-heavy and skewed toward adjacent catalytic and silica-interface chemistry rather than dense, named MOF or zeolite framework benchmarking.

### Catalytic surfaces and confined reactants

[[2015broqvist-venue-jp5b01597]] and [[2013neyts-venue-c3nr00153a]] are the most direct in-corpus anchors when the practical question is "which reactive-surface results can inform porous catalyst reasoning?" They are strongest for mechanism-level surface reactivity and weaker for explicit micropore transport claims.

### Silica, glasses, and nanopore-like surface chemistry

[[2013muri-venue-jp3086649]] and [[2019hahn-j-phys-chem-surface-reactivity]] provide silica or silicate surface chemistry that is often the best available proxy in this corpus for pore-wall reactivity questions in oxide-rich porous systems.

### Coverage boundary reminders

If a specific MOF or zeolite framework is not represented by a paper page, this hub should be used for routing only, not for parameter or mechanism claims.

## Analysis and cross-cutting patterns

Across the current pages, the repeated pattern is methodological adjacency: porous questions are most often answered via catalytic surface papers and silica-interface papers rather than framework-specific force-field studies. As a result, confinement conclusions should be treated as paper-local unless multiple porous-domain pages converge on the same claim.

## Debates, tensions, and limitations

- Transferability of reactive force fields to open-metal-site or framework-specific chemistry remains a known tension; this corpus currently supports that discussion only where linked paper pages and [[transferability-reactive-ff]] make it explicit.
- Scope is limited by sparse framework-resolved MOF and zeolite notes, so absence of a result here should be treated as a corpus gap rather than negative evidence.

## Gaps and open directions (corpus view)

Priority gap-filling for this hub is straightforward: add curated, named MOF and zeolite paper pages with explicit methods and findings, then replace adjacency-first routing with framework-specific pathways.

## Methods and limitations

Reactive MD in confined porous systems often requires larger cells and longer sampling for adsorption or desorption equilibration than local-surface studies. Because many current corpus anchors emphasize surface-reactivity mechanisms, users should verify whether each linked page actually reports pore-scale transport behavior before generalizing.

## Representative entry points

- **If your question is reactive chemistry on porous supports:** start with [[2015broqvist-venue-jp5b01597]] and [[2013neyts-venue-c3nr00153a]].
- **If your question is pore-wall behavior in silica-like systems:** start with [[2013muri-venue-jp3086649]] and [[2019hahn-j-phys-chem-surface-reactivity]].
- **If your question needs corpus-wide coverage checks first:** open [[paper-index-by-domain]] and filter around `domain:porous-mof-zeolite`.
- **Adjacent synthesis hubs:** [[theme-catalysis-surfaces]], [[theme-water-silica-geo]], [[theme-oxides-silica-ceramics]], [[transferability-reactive-ff]].
- **Domain listing:** [[paper-index-by-domain]] (`domain:porous-mof-zeolite`).

??? info "MAS / retrieval"

    **id:** `concept:theme-porous-mof-zeolite`. As MOF/zeolite-tagged papers are added, expand this hub’s **Literature review** with **verbatim** pointers to new `[[slug]]` pages.
