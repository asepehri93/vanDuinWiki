---
id: concept:theme-pyrolysis-combustion-organics
type: concept
title: "Theme: pyrolysis, combustion, and large-scale organics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
    note: "Large-scale coal model; pyrolysis"
  - paper_id: "paper:2018ashraf-fuel-235-201-pyrolysis-binary"
    note: "Binary fuel pyrolysis"
  - paper_id: "paper:2018qifan-combustion-a-reaxff-simulations"
    note: "Combustion-oriented ReaxFF"
supported_by:
  - "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
  - "paper:2018qifan-combustion-a-reaxff-simulations"
---

<!-- id:concept:theme-pyrolysis-combustion-organics -->

!!! abstract "TL;DR"

    This cluster groups **high-temperature organic chemistry** in the corpus: **coal** and **hydrocarbon** pyrolysis at scale, **fuel**-related decomposition, and **combustion** simulations with **ReaxFF**. It connects to **carbon materials** ([[graphene-nanocarbon]]) but focuses on **reactive bulk/liquid** systems rather than 2D mechanics alone.

## Scope

**Pyrolysis / devolatilization:** large molecular models, **char** formation precursors, **PAH**-like chemistry where parameterized.

**Combustion:** gas-phase and **flame-relevant** subsets when tied to ReaxFF parameter sets in the wiki.

## Representative papers

- **Large-scale coal / hydrocarbon solid:** [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] — **PYR1** gold hit in frozen benchmark.  
- **Binary pyrolysis:** [[2018ashraf-fuel-235-201-pyrolysis-binary]].  
- **Combustion ReaxFF:** [[2018qifan-combustion-a-reaxff-simulations]].  
- **Polymer / organic decomposition:** [[2018vashisth-polymer-158-effect-chemical]], [[2019akbarian-polymer-183-atomistic-scale-insights]].  
- **Energetic / propulsion angle (tutorial):** [[2013ijemcp1202-1-5739-venue-paper]], [[2013vanduin-venue-paper]].

## Methods and limitations

**System size** vs **wall time** trades off against **chemical diversity** captured. Papers often report **qualitative** product distributions; **quantitative** agreement with experiment may require **kinetic Monte Carlo** or **continuum** coupling not present in every entry.

## Related

- [[theme-catalysis-surfaces]]  
- [[reaxff-family]]  

??? info "Maintainers"

    Domains: `domain:organics-polymers-pyrolysis`, `domain:fuel-combustion`. Keep cross-links to [[graphene-nanocarbon]] where carbon products overlap.
