---
id: concept:theme-pyrolysis-combustion-organics
type: concept
title: "Theme: pyrolysis, combustion, and organic reactivity (ReaxFF corpus)"
updated: "2026-04-21"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:review
candidate_tags:
  - domain:pyrolysis-combustion
source_refs:
  - paper_id: "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
    note: "Large-scale Illinois coal pyrolysis (ReaxFF)"
  - paper_id: "paper:2018ashraf-fuel-235-201-pyrolysis-binary"
    note: "Supercritical binary fuel pyrolysis mixtures"
  - paper_id: "paper:2021lele-fuel-297-202-reaxff-molecular"
    note: "Aviation-fuel bicyclic pyrolysis kinetics"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "CO₂ hydrogenation (C/H/O network overlap)"
  - paper_id: "paper:2013neyts-venue-c3nr00153a"
    note: "Carbon surface reactions"
  - paper_id: "paper:2014sen-nat-oxidation-assisted-ductility"
    note: "Oxidation / mechanical coupling (related O ingress)"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Metal oxidation (O in Ni)"
supported_by:
  - "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
  - "paper:2015broqvist-venue-jp5b01597"
---

<!-- id:concept:theme-pyrolysis-combustion-organics -->

!!! abstract "TL;DR"

    This theme clusters corpus pages where reactive molecular simulations are used to describe thermal decomposition, oxidation, and C/H/O bond-network evolution in carbon-rich systems and related organics. It is a corpus-scoped synthesis page: use [[theme-combustion-flames-fuels]] for flame-first framing and [[theme-catalysis-surfaces]] when catalyst structure is the primary organizing axis.

## Scope (in / out)

**In corpus:** coal and hydrocarbon pyrolysis, aviation-fuel decomposition, CO2 hydrogenation pathways that traverse C/H/O networks, carbon-surface reactivity, and oxidation-linked studies that overlap with combustion-adjacent reactive chemistry.

**Out of scope here:** oxide-focused mechanics pages without central organic bond chemistry (see [[theme-oxides-silica-ceramics]]). When a paper page is primarily organized around combustion or flame behavior, start in [[theme-combustion-flames-fuels]] and return here for pyrolysis and thermal-decomposition cross-links.

## How this theme is organized in the corpus

The sections follow corpus organization rather than a full field taxonomy: pyrolysis anchors first, then closely related C/H/O pathway contexts (hydrogenation, carbon surfaces, and oxidation-coupled studies) that appear in the current wiki pages.

## Literature review (this knowledge base)

This is a literature review of this knowledge base only, not a full external review.

### Pyrolysis and carbonaceous materials

[[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] is the central corpus anchor for large-scale Illinois no. 6 coal pyrolysis with ReaxFF. [[2018ashraf-fuel-235-201-pyrolysis-binary]] extends that pyrolysis thread to supercritical binary fuel mixtures. [[2021lele-fuel-297-202-reaxff-molecular]] adds aviation-fuel bicyclic decomposition and kinetics-oriented interpretation. For petroleum-coke sulfur chemistry framed directly as combustion, see [[2018qifan-combustion-a-reaxff-simulations]] and the combustion hub [[theme-combustion-flames-fuels]].

### CO₂ hydrogenation and oxygenate formation

[[2015broqvist-venue-jp5b01597]] documents CO2 hydrogenation chemistry with C/H/O network overlap relevant to pyrolysis-and-combustion-adjacent pathway questions. It is also a catalyst-surface page; this hub includes it when the user intent is product-network evolution rather than catalyst-first comparison.

### Carbon surfaces and nanostructures

[[2013neyts-venue-c3nr00153a]] provides carbon-surface reaction context that helps bridge condensed-phase pyrolysis narratives and surface-mediated bond rearrangement. Pair with [[graphene-nanocarbon]] for broader nanocarbon context.

### Oxidation coupling to mechanics and metals

[[2014sen-nat-oxidation-assisted-ductility]] links oxidation with mechanical response, while [[2014zou-acta-materia-molecular-dynamics]] addresses oxygen transport and oxidation initiation in Ni. These pages are included as adjacent evidence when oxidation ingress and reactive pathway framing overlap with this theme's C/H/O reactivity lens.

## Analysis and cross-cutting patterns

Across the linked corpus pages, temperature windows, model sizes, and simulation durations vary substantially between coal-scale models and smaller fuel-molecule studies. Cross-paper generalization should stay limited to claims explicit on each paper page. For method-first comparison across domains, use [[theme-reactive-md-corpus]].

## Debates, tensions, and limitations

- **Timescale interpretation:** reactive MD pyrolysis trajectories are often shorter than experimental thermal histories, so rate and yield extrapolation should remain page-specific.
- **Model transferability:** parameterization scope versus downstream application breadth remains a recurring concern; see [[transferability-reactive-ff]] and [[reaxff-family]].
- **Boundary between hubs:** catalyst-first interpretation can shift conclusions relative to pyrolysis-first framing; cross-check [[theme-catalysis-surfaces]] for the same paper when applicable.

## Gaps and open directions (corpus view)

The `domain:organics-polymers-pyrolysis` bucket currently blends pyrolysis-first and combustion-first papers; this hub and [[theme-combustion-flames-fuels]] are complementary disambiguation layers. Coverage is still uneven across the domain list, so additional paper pages and refreshed `source_refs` are needed as curation advances.

## Representative entry points

- **Coal pyrolysis (large-scale model):** [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]].
- **Supercritical mixture pyrolysis:** [[2018ashraf-fuel-235-201-pyrolysis-binary]].
- **Aviation bicyclic decomposition:** [[2021lele-fuel-297-202-reaxff-molecular]].
- **CO2 hydrogenation crossover:** [[2015broqvist-venue-jp5b01597]].
- **Carbon surfaces:** [[2013neyts-venue-c3nr00153a]].
- **Oxidation-mechanics adjacency:** [[2014sen-nat-oxidation-assisted-ductility]] and [[2014zou-acta-materia-molecular-dynamics]].
- **Full domain sort:** [[paper-index-by-domain]] (`domain:organics-polymers-pyrolysis`).

## Methods and limitations

Reactive MD can expose plausible bond-network pathways but does not, by itself, establish definitive rate control without higher-level energetics or experimental triangulation. In pyrolysis contexts, mass-loss partitioning and product distributions can depend on mesoscale transport and phase behavior beyond what small reactive cells typically capture.

??? info "MAS / retrieval"

    **id:** `concept:theme-pyrolysis-combustion-organics`. Primary tagging is `domain:organics-polymers-pyrolysis` for pyrolysis-first pages; keep catalyst-first pages discoverable via [[theme-catalysis-surfaces]] and combustion-first pages via [[theme-combustion-flames-fuels]]. Refresh `source_refs` as additional corpus paper pages are upgraded.
