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

    This cluster covers **pyrolysis**, **oxidation**, and **organic bond-breaking** networks where **ReaxFF** is used to follow **reaction pathways** in **carbonaceous** materials and related **C/H/O** chemistry. It connects to [[theme-catalysis-surfaces]] when **surface elementary steps** dominate. **Combustion-first** and **flame-oriented** notes also map to [[theme-combustion-flames-fuels]].

## Scope (in / out)

**In corpus:** **coal and hydrocarbon pyrolysis**, **aviation-fuel** decomposition, **CO₂ hydrogenation** (organic product pathways), **carbon surface** reactions, and **oxidation** stories that share **C/H/O** parameterizations with combustion-adjacent work.

**Out of scope here:** pure **oxide ceramic** mechanics without organic bond chemistry (see [[theme-oxides-silica-ceramics]]). When the paper page’s **headline** is **combustion** or **flame** chemistry, start from [[theme-combustion-flames-fuels]] and cross-link back here as needed.

## Literature review (this knowledge base)

Corpus-limited: the following paragraphs route readers to **paper notes** that exist in vanDuinWiki.

### Pyrolysis and carbonaceous materials

[[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] is a primary KB anchor: **large-scale** **Illinois no. 6 coal** pyrolysis with ReaxFF. For **supercritical** **binary fuel** pyrolysis and **mixture** effects, see [[2018ashraf-fuel-235-201-pyrolysis-binary]]. **Aviation-fuel** bicyclic candidates and **Arrhenius**-style kinetics appear in [[2021lele-fuel-297-202-reaxff-molecular]] (also linked from [[theme-combustion-flames-fuels]]). **Petroleum coke** sulfur chemistry with explicit **combustion** framing is summarized on [[2018qifan-combustion-a-reaxff-simulations]] and listed under [[theme-combustion-flames-fuels]].

### CO₂ hydrogenation and oxygenate formation

[[2015broqvist-venue-jp5b01597]] documents **CO₂ hydrogenation** chemistry that shares **C/H/O** bond networks with many **combustion-adjacent** studies. It is catalogued under **catalysis** in the domain index but belongs in this theme when the question is **organic product** pathways rather than **heterogeneous catalyst** structure *per se*.

### Carbon surfaces and nanostructures

[[2013neyts-venue-c3nr00153a]] provides **surface reaction** context on **carbon** systems; pair with [[graphene-nanocarbon]] for **sp²** carbon parameter discussions.

### Oxidation coupling to mechanics and metals

[[2014sen-nat-oxidation-assisted-ductility]] links **oxidation** to **mechanical** response. [[2014zou-acta-materia-molecular-dynamics]] treats **O in Ni** and **oxidation initiation**—useful when comparing **gas-phase O** vs **internal oxidation** scenarios.

## Analysis and cross-cutting patterns

**Temperature** and **simulation time** choices differ between **coal** models and **fuel** molecules; extrapolate **only** along claims stated on each paper page. For **method** threads that span domains, see [[theme-reactive-md-corpus]].

## Gaps and open directions (corpus view)

The **`domain:organics-polymers-pyrolysis`** sort mixes **pyrolysis** and **combustion** stories—[[theme-combustion-flames-fuels]] reduces retrieval collision for **flame/fuel** questions. Not every slug in the domain table is yet summarized in these hubs.

## Debates, tensions, and cross-references

- **Temperature and timescale:** pyrolysis MD is often **shorter** than experiment; extrapolation claims should be read cautiously on each paper page.  
- **ReaxFF vs kinetics databases:** [[transferability-reactive-ff]], [[reaxff-family]].  
- **Adjacent:** [[theme-catalysis-surfaces]], [[theme-oxides-silica-ceramics]], [[theme-water-silica-geo]] when **hydroxyl** or **moist** environments matter.

## Representative entry points

- **Coal pyrolysis (large-scale model):** [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]].  
- **Supercritical mixture pyrolysis:** [[2018ashraf-fuel-235-201-pyrolysis-binary]].  
- **Aviation bicyclics:** [[2021lele-fuel-297-202-reaxff-molecular]].  
- **CO₂ hydrogenation:** [[2015broqvist-venue-jp5b01597]].  
- **Carbon surfaces:** [[2013neyts-venue-c3nr00153a]].  
- **Oxidation + mechanics:** [[2014sen-nat-oxidation-assisted-ductility]].  
- **Full domain sort:** [[paper-index-by-domain]] (`domain:organics-polymers-pyrolysis`).

## Methods and limitations

**Reactive MD** can reveal **plausible** pathways but rarely proves **rate-limiting steps** without **barrier refinement** or **experiment**. **Mass loss** and **tar composition** in pyrolysis involve **phase separation** and **transport** that may not be fully captured in **small** reactive cells.

??? info "MAS / retrieval"

    **id:** `concept:theme-pyrolysis-combustion-organics`. Tag pyrolysis papers with `domain:organics-polymers-pyrolysis` (first domain tag drives the index); use catalysis domain when **surface catalysis** is the headline.
