---
id: concept:theme-water-silica-geo
type: concept
title: "Theme: water at silica and geochemical interfaces (ReaxFF corpus)"
updated: "2026-04-21"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "O₂ + hydroxylated silica; water-related surface chemistry"
  - paper_id: "paper:2019hahn-j-phys-chem-surface-reactivity"
    note: "Silicate glass surface reactivity"
  - paper_id: "paper:2018ho-venue-paper"
    note: "Oxide / surface context in corpus"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Electrolyte interfaces (water-in-salt adjacency)"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Aqueous/catalytic C–O chemistry overlap"
supported_by:
  - "paper:2013muri-venue-jp3086649"
  - "paper:2019hahn-j-phys-chem-surface-reactivity"
---

<!-- id:concept:theme-water-silica-geo -->

!!! abstract "TL;DR"

    This cluster focuses on **water**, **hydroxylated silica**, and **geo-/material** interfaces where **ReaxFF** captures **proton** and **oxygen** rearrangements. It is the natural bridge between [[theme-oxides-silica-ceramics]] and [[batteries-interfaces-reaxff]].

## Scope (in / out)

**In corpus:** **hydroxylated silica**, **silicate glass** surfaces, and **oxide** interfaces where **explicit water** or **proton transport** is discussed on wiki pages.

**Out of scope:** bulk **electrolyte** thermodynamics without a **mineral** or **oxide** interface (see battery hub).

## Literature review (this knowledge base)

Corpus-limited review: each **bold claim** about mechanisms should be checked on the linked **paper page**.

### Hydroxylated silica and oxygen/water-related surface chemistry

[[2013muri-venue-jp3086649]] documents **O₂** interactions with **hydroxylated silica** and is a **keystone** page for this theme. Use it when questions involve **surface hydroxyl** coverage and **oxygen** attack pathways.

### Silicate glasses and surface reactivity

[[2019hahn-j-phys-chem-surface-reactivity]] focuses on **silicate glass** **surface reactivity**; pair with [[2018ho-venue-paper]] when the KB’s index routes you to related **oxide** surface notes.

### Electrolyte interfaces (water structuring adjacency)

[[2018shin-physical-che-development-reaxff]] is primarily a **battery electrolyte** paper in the KB, but it belongs in this theme when the question is **interfacial** **water** / **salt** structuring next to **oxide**-like regions—see the paper note for what is actually simulated.

### Catalytic aqueous chemistry overlap

[[2015broqvist-venue-jp5b01597]] connects when **liquid-like** or **hydrogen-bonding** environments participate in **C–O** chemistry; cross-read [[theme-catalysis-surfaces]].

## Analysis and cross-cutting patterns

**Interfacial water** structure recurs across **oxide**, **glass**, and **electrolyte** notes; **electrostatic** and **coverage** details remain **publication-specific**.

## Gaps and open directions (corpus view)

**Field-scale** geochemistry and **long** transport paths are **not** typically captured in atomistic notes here—use this hub for **interface**-resolved stories in the KB.

## Debates, tensions, and cross-references

- **pH and proton activity:** classical MD without **explicit** proton hopping may omit **Grotthuss** mechanisms—check each paper’s **proton** treatment.  
- **Mineral dissolution** completeness: the KB may not cover every **dissolution** pathway; avoid over-claiming **geochemical** completeness.  
- **Related:** [[theme-oxides-silica-ceramics]], [[theme-catalysis-surfaces]], [[batteries-interfaces-reaxff]] (electrolyte–oxide interfaces and interphase chemistry).

## Representative entry points

- **Silica + hydroxyl / O₂:** [[2013muri-venue-jp3086649]].  
- **Silicate glass surfaces:** [[2019hahn-j-phys-chem-surface-reactivity]], [[2018ho-venue-paper]].  
- **Electrolyte–oxide interface:** [[2018shin-physical-che-development-reaxff]].  
- **Index:** [[paper-index-by-domain]] (`domain:water-silica-geo`).

## Methods and limitations

**Water models** and **ReaxFF** parameterizations must be **jointly** validated; **interfacial tension** and **contact angles** are sensitive to **system size** and **sampling time**.

??? info "MAS / retrieval"

    **id:** `concept:theme-water-silica-geo`. Tag new papers with `domain:water-silica-geo` when **explicit water** or **hydroxyl** equilibria on **oxide**/**silicate** are central.
