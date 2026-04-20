---
id: concept:theme-catalysis-surfaces
type: concept
title: "Theme: catalysis and reactive metal/oxide surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2013somers-catalysis-to-temperature-influence"
    note: "Ni surface CHx and H2 pathways; temperature effects"
  - paper_id: "paper:2015psofogiannakis-venue-jp5b00699"
    note: "Cu-zeolite SCR chemistry; reactive MD framing"
  - paper_id: "paper:2014somers-applied-cata-interactions-plasma"
    note: "Plasma–catalyst interactions"
supported_by:
  - "paper:2013somers-catalysis-to-temperature-influence"
  - "paper:2015psofogiannakis-venue-jp5b00699"
---

<!-- id:concept:theme-catalysis-surfaces -->

!!! abstract "TL;DR"

    **Heterogeneous catalysis** entries in this wiki emphasize **atomistic pathways** on **Ni**, **Cu-zeolite** systems, and related **surface reactions** where **ReaxFF** captures bond rearrangements at **elevated temperature** or under **non-equilibrium** conditions (e.g. plasma). Use this hub before opening individual **venue-specific** paper pages.

## Scope

**Included:** metal and oxide **surfaces**, **zeolite**-hosted chemistry where parameterized, **SCR**-adjacent nitrogen chemistry, and **plasma–catalyst** coupling when documented with reactive MD.

**Boundary:** gas-phase **combustion** without a catalyst surface is cross-listed under [[theme-pyrolysis-combustion-organics]].

## Representative papers

- **Ni / CHx / H₂:** [[2013somers-catalysis-to-temperature-influence]] — benchmark-style question in frozen eval **CAT1**.  
- **Cu zeolite / SCR:** [[2015psofogiannakis-venue-jp5b00699]].  
- **Plasma + catalyst:** [[2014somers-applied-cata-interactions-plasma]].  
- **Broader ReaxFF catalysis / surface training:** [[2017jejoon-yeon-j-phys-chem-development-reaxff]], [[2018tao-liang-j-phys-chem-applied-potentials]], [[2019shabnam-physical-che-evaluation-effect]].  
- **Corrosion / electrocatalyst angles:** [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]].

## Methods and limitations

**Temperature** and **coverage** dictate which pathways dominate; papers often compare several **reaction coordinates**. **ReaxFF** barriers are only as good as the **training reactions** included—**experimental turnover** data are rarely matched quantitatively in the same paper.

## Related

- [[theme-oxides-silica-ceramics]]  
- [[reaxff-family]]  

??? info "Maintainers"

    Tag alignment: `domain:catalysis-surfaces`. Expand wikilinks as new `wiki/papers/` slugs are tagged for catalysis.
