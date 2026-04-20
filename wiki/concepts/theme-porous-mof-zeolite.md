---
id: concept:theme-porous-mof-zeolite
type: concept
title: "Theme: porous MOFs, ZIFs, and zeolite-related frameworks"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2018yang-j-phys-chem-enabling-computational"
    note: "ZIF / glassy porous phases; large-scale MD"
supported_by:
  - "paper:2018yang-j-phys-chem-enabling-computational"
---

<!-- id:concept:theme-porous-mof-zeolite -->

!!! abstract "TL;DR"

    **ZIF**, **zeolite**, and **MOF**-class porous solids appear where **ReaxFF** can treat **framework bond** rearrangements and **guest** chemistry at **elevated T** or in **disordered** (glassy) phases. Frozen eval **ZIF1** points to [[2018yang-j-phys-chem-enabling-computational]].

## Scope

**In:** **imidazolate** frameworks, **zeolite**-hosted chemistry, and **nanoporous** carbon or hybrid systems when the paper’s focus is **reactive MD** with documented parameter scope.

**Out:** pure **adsorption** on closed pores without reactive FF — may appear only as background.

## Representative papers

- **ZIF / computational enabling:** [[2018yang-j-phys-chem-enabling-computational]] — **ZIF1** gold.  
- **Cu-zeolite / SCR (overlap):** [[2015psofogiannakis-venue-jp5b00699]].  
- **Zeolite acidity / catalysis:** follow `domain:catalysis-surfaces` tags in paper frontmatter.

## Methods and limitations

**Framework flexibility** and **defect** distributions drive **large** cell sizes; **ReaxFF** must include **metal–linker** chemistry in the training set.

## Related

- [[theme-catalysis-surfaces]]  
- [[reaxff-family]]  

??? info "Maintainers"

    When new MOF/ZIF slugs are added under `wiki/papers/`, link them here and in [[themes-index]] if high-signal.
