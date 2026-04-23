---
id: concept:theme-catalysis-surfaces
type: concept
title: "Theme: catalysis and surface reactions (ReaxFF corpus)"
updated: "2026-04-21"
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
---

<!-- id:concept:theme-catalysis-surfaces -->

!!! abstract "TL;DR"

    This cluster covers **heterogeneous catalysis** and **surface reactions** where **bond formation/breaking** is modeled with **ReaxFF** (CO₂ hydrogenation, carbon surfaces, metal oxidation, silica oxygen chemistry). It overlaps [[theme-oxides-silica-ceramics]] and [[theme-pyrolysis-combustion-organics]].

## Scope (in / out)

**In corpus:** catalytic **CO₂/H₂** chemistry, **carbon nanostructure** surface reactions, **metal oxidation** surfaces, **silica** oxygen chemistry, and **electrolyte interface** chemistry when framed as surface reactivity.

**Out of scope here:** gas-phase **combustion** kinetics without a catalytic surface (see [[theme-combustion-flames-fuels]] and [[theme-pyrolysis-combustion-organics]]).

## Literature review (this knowledge base)

Corpus-limited synthesis: the bullets below summarize **what the linked paper pages document** about catalysis and surfaces in this KB.

### CO₂ hydrogenation and oxygenate pathways on surfaces

[[2015broqvist-venue-jp5b01597]] is a primary KB anchor for **CO₂ hydrogenation** and related **surface chemistry** framed with ReaxFF. Use that page for **mechanistic detail** and **parameter context**; cross-link to [[theme-pyrolysis-combustion-organics]] when discussing **C/H/O** bond networks shared with combustion modeling.

### Carbon surfaces, CNT contexts, and hydrocarbon coupling

[[2013neyts-venue-c3nr00153a]] documents **catalytic surface reactions** in a **carbon nanostructure** setting. This theme intersects [[graphene-nanocarbon]] when **sp² carbon** chemistry is central.

### Oxide and silica surfaces under reactive environments

[[2013muri-venue-jp3086649]] treats **O₂ + hydroxylated silica** and is a natural bridge to [[theme-oxides-silica-ceramics]]. **Surface science** parameterization narratives appear in [[2015lloyd-surface-scie-development-reaxff]].

### Metal surfaces, oxidation, and electrochemical overlap

**Ni oxidation** and **oxygen ingress** in metals are covered in [[2014zou-acta-materia-molecular-dynamics]]. **Electrolyte interface** chemistry that is explicitly **surface-reaction** oriented appears in [[2018shin-physical-che-development-reaxff]] and ties to [[batteries-interfaces-reaxff]].

## Analysis and cross-cutting patterns

**CO₂ hydrogenation** and **C/H/O** networks in [[2015broqvist-venue-jp5b01597]] overlap thematically with [[theme-pyrolysis-combustion-organics]]; keep **heterogeneous surface** elementary steps in this hub unless the paper page frames **gas-phase thermal** decomposition as primary.

## Gaps and open directions (corpus view)

Catalyst papers whose **first** `domain:` tag sorts them elsewhere may be **under-linked** from this hub—use full-text search and [[paper-index-by-domain]] to find **surface** chemistry that is not yet routed here.

## Debates, tensions, and cross-references

- **Barrier accuracy** for catalytic elementary steps: compare claims on individual papers with [[transferability-reactive-ff]] and [[reaxff-vs-mlip-accuracy]].  
- **Coverage effects** (adsorbate layers) vs **idealized surfaces**: many ReaxFF studies use **small cells**—check each paper’s **finite-size** discussion.  
- **Related themes:** [[theme-oxides-silica-ceramics]], [[theme-pyrolysis-combustion-organics]], [[theme-water-silica-geo]] (solvation at oxide surfaces).

## Representative entry points

- **CO₂ / catalytic surfaces:** [[2015broqvist-venue-jp5b01597]].  
- **CNT / carbon surface catalysis:** [[2013neyts-venue-c3nr00153a]].  
- **Silica + O₂:** [[2013muri-venue-jp3086649]].  
- **Ni oxidation surfaces:** [[2014zou-acta-materia-molecular-dynamics]].  
- **Electrolyte surfaces:** [[2018shin-physical-che-development-reaxff]].  
- **Index:** [[paper-index-by-domain]] (filter `domain:catalysis-surfaces`).

## Methods and limitations

**ReaxFF** excels at **qualitative** reaction-network exploration; **quantitative** turnover frequencies usually require **validation** against experiment or higher-level theory on a **case-by-case** basis. **Electrostatics** at polar surfaces may need **explicit checks** when comparing to continuum models.

??? info "MAS / retrieval"

    **id:** `concept:theme-catalysis-surfaces`. Tag new papers with `domain:catalysis-surfaces` when the dominant story is **surface elementary steps** or **heterogeneous catalysis**.
