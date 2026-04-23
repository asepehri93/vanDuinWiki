---
id: concept:theme-catalysis-surfaces
type: concept
title: "Theme: catalysis and surface reactions (ReaxFF corpus)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "CO₂ hydrogenation / catalytic surface chemistry"
  - paper_id: "paper:2013neyts-venue-c3nr00153a"
    note: "Catalytic surface reactions (CNT / surface)"
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "O₂ + hydroxylated silica; surface O chemistry"
  - paper_id: "paper:2015lloyd-surface-scie-development-reaxff"
    note: "Surface science oriented ReaxFF development"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Ni oxidation / surface-related metal oxidation"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Li-ion electrolyte interfaces (surface chemistry overlap)"
supported_by:
  - "paper:2015broqvist-venue-jp5b01597"
  - "paper:2013neyts-venue-c3nr00153a"
  - "paper:2013muri-venue-jp3086649"
  - "paper:2015lloyd-surface-scie-development-reaxff"
  - "paper:2014zou-acta-materia-molecular-dynamics"
  - "paper:2018shin-physical-che-development-reaxff"
---

<!-- id:concept:theme-catalysis-surfaces -->

!!! abstract "TL;DR"

    This theme page organizes the corpus slices where ReaxFF is used to model bond-making and bond-breaking at solid surfaces (catalytic CO2 conversion, carbon nanostructure surface chemistry, oxide/silica oxygen chemistry, and oxidation/electrolyte interfaces). It is a corpus-grounded map of linked paper pages, not a full field-wide review.

## Scope (in / out)

**In corpus:** catalytic CO2/H2 chemistry, carbon nanostructure surface reactions, metal-surface oxidation pathways, silica oxygen chemistry, and electrolyte interface chemistry when the page evidence is framed as surface reactivity.

**Out of scope here:** gas-phase combustion kinetics without an explicit surface mechanism (see [[theme-combustion-flames-fuels]] and [[theme-pyrolysis-combustion-organics]]).

## How this theme is organized in the corpus

The corpus evidence naturally splits into four recurring surface-reaction contexts: (1) catalytic CO2 conversion, (2) carbon-surface/CNT reaction chemistry, (3) oxide-surface oxygen chemistry and force-field setup, and (4) oxidation/electrolyte interfaces on metal or electrode-adjacent surfaces. The literature review below follows that structure so retrieval paths remain stable for both human readers and MAS routing.

## Literature review (this knowledge base)

This section summarizes only what the linked paper pages in this knowledge base report; it does not claim a complete review beyond the curated corpus.

### CO₂ hydrogenation and oxygenate pathways on surfaces

[[2015broqvist-venue-jp5b01597]] is the main corpus anchor here for CO2 hydrogenation-oriented catalytic surface chemistry under a ReaxFF framing. In this theme, that page serves as the primary route for mechanism-level discussion of C/H/O transformations that occur at catalytic interfaces rather than in purely gas-phase settings.

### Carbon surfaces, CNT contexts, and hydrocarbon coupling

[[2013neyts-venue-c3nr00153a]] provides the carbon-surface side of the cluster, with catalytic surface reactions in a CNT/carbon nanostructure context. This creates a bridge from catalysis-oriented routing to [[graphene-nanocarbon]] when the central mechanistic object is sp2-rich carbon surface chemistry.

### Oxide and silica surfaces under reactive environments

[[2013muri-venue-jp3086649]] covers O2 reactivity on hydroxylated silica surfaces and anchors the oxide/silica branch of this theme. [[2015lloyd-surface-scie-development-reaxff]] adds a surface-science-oriented force-field development perspective that is useful when interpreting whether observed surface pathways are likely parameterization-limited versus physically robust within this corpus.

### Metal surfaces, oxidation, and electrochemical overlap

[[2014zou-acta-materia-molecular-dynamics]] contributes the metal-oxidation branch (Ni oxidation/oxygen ingress behavior in a surface-reaction framing). [[2018shin-physical-che-development-reaxff]] contributes the electrolyte-interface overlap where interfacial chemistry and reactive surface processes meet battery-relevant questions, with direct cross-routing to [[batteries-interfaces-reaxff]].

## Analysis and cross-cutting patterns

Across the cited pages, the recurring pattern is that catalysis and "surface oxidation" are treated through shared reactive bond-network machinery, but the scientific interpretation depends strongly on where reactions are localized (surface active sites, near-surface oxide regions, or interfacial electrolyte zones).

[[2015broqvist-venue-jp5b01597]] and [[2013neyts-venue-c3nr00153a]] both sit in C/H/O-rich chemistry spaces that can otherwise be misfiled as combustion/pyrolysis; this theme keeps them together when the linked page narrative is explicitly heterogeneous and surface-centered.

[[2013muri-venue-jp3086649]] and [[2014zou-acta-materia-molecular-dynamics]] show a second cross-cutting thread: oxygen chemistry at surfaces can encode both catalytic and degradation/oxidation behavior, so transfer of mechanistic language across oxide and metal contexts should stay conditional and paper-specific.

[[2015lloyd-surface-scie-development-reaxff]] and [[2018shin-physical-che-development-reaxff]] reinforce a method-level caution seen across this corpus: interpretation of elementary-step pathways must be read together with the parameterization lineage and interface assumptions documented on each page.

## Debates, tensions, and limitations

Within this corpus, at least three unresolved tensions recur:

- Elementary-step barrier reliability for catalytic surfaces versus broader qualitative trend capture (compare with [[transferability-reactive-ff]] and [[reaxff-vs-mlip-accuracy]]).
- Surface-coverage and finite-size effects versus idealized slabs or limited-cell setups in reactive MD studies.
- Cross-domain transfer risk when moving insights between catalytic, oxidation, and electrolyte-interface pages without checking each source page's stated scope.

These tensions are included as routing cautions rather than settled conclusions, because the relevant evidence is distributed across the linked paper pages and method debates rather than concentrated in one benchmark-style corpus study.

## Gaps and open directions (corpus view)

Coverage appears thin for catalyst families beyond the current CO2/carbon/oxide/metal subset, and papers whose primary domain tag is not `domain:catalysis-surfaces` may still contain surface-reaction evidence that is currently under-linked here.

A practical corpus gap is benchmark-style reconciliation across the linked branches (catalytic conversion, oxidation, and interface chemistry) using shared validation targets. Until such synthesis pages are expanded, this hub should be treated as a routing map with cautious cross-transfer.

## Representative entry points

- CO2 / catalytic surfaces: [[2015broqvist-venue-jp5b01597]]
- CNT / carbon-surface catalysis: [[2013neyts-venue-c3nr00153a]]
- Silica + O2 surface chemistry: [[2013muri-venue-jp3086649]]
- Surface-science ReaxFF development context: [[2015lloyd-surface-scie-development-reaxff]]
- Ni oxidation surfaces: [[2014zou-acta-materia-molecular-dynamics]]
- Electrolyte-interface overlap: [[2018shin-physical-che-development-reaxff]]
- Domain index pivot: [[paper-index-by-domain]] (filter `domain:catalysis-surfaces`)

## Methods and limitations

This theme-level synthesis is constrained by heterogeneous study designs across the linked papers (different surface models, state-point choices, and calibration goals), so direct quantitative comparison is often not possible from the current corpus pages alone.

The hub therefore emphasizes evidence-grounded routing and mechanism-level patterning. Quantitative catalytic ranking, absolute barrier fidelity, and transfer claims across materials classes should be treated as conditional unless the linked paper pages provide direct validation context.

??? info "MAS / retrieval"

    **id:** `concept:theme-catalysis-surfaces`
    **type:** `concept`
    **routing intent:** Use for queries about heterogeneous catalysis, reactive surface elementary steps, carbon/oxide/metal surface chemistry, and electrolyte-surface overlap where the mechanistic center is at an interface.
    **primary corpus anchors:** `paper:2015broqvist-venue-jp5b01597`, `paper:2013neyts-venue-c3nr00153a`, `paper:2013muri-venue-jp3086649`, `paper:2015lloyd-surface-scie-development-reaxff`, `paper:2014zou-acta-materia-molecular-dynamics`, `paper:2018shin-physical-che-development-reaxff`.
    **tagging hint:** Apply `domain:catalysis-surfaces` when the dominant narrative is heterogeneous surface reactivity; route gas-phase-first chemistry to combustion/pyrolysis themes.
    **maintenance note:** Refresh `source_refs` and `supported_by` together when adding or removing representative papers so MAS grounding and reader narrative stay aligned.
