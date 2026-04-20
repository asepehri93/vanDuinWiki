---
id: concept:theme-water-silica-geo
type: concept
title: "Theme: water films, silica, and geochemical interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2015achtyl-nat-aqueous-proton"
    note: "Aqueous proton / water at interfaces"
  - paper_id: "paper:2016rahnamoun-venue-study-ice"
    note: "Ice / water hydrogen bonding studies"
  - paper_id: "paper:2018bree-organic-geoc-origin-formation"
    note: "Geochemical organic formation context"
  - paper_id: "paper:2015surwade-nat-water-desalination"
    note: "Nanoporous graphene water transport (experimental; context)"
supported_by:
  - "paper:2015achtyl-nat-aqueous-proton"
  - "paper:2016rahnamoun-venue-study-ice"
---

<!-- id:concept:theme-water-silica-geo -->

!!! abstract "TL;DR"

    This theme groups **aqueous interfaces**, **ice**, **clays**, and **mineral–water** systems that recur in environmental and **geochemical** framing. It complements [[theme-oxides-silica-ceramics]] (dry oxidation) with **H-bonded** and **confined water** behavior.

## Scope

**In:** **proton transport**, **ice** nucleation or structure, **clay** and **oxide** surfaces in contact with **liquid water**, and **geochemical** organic processes when tied to atomistic models in the wiki.

## Representative papers

- **Aqueous protons / interfaces:** [[2015achtyl-nat-aqueous-proton]].  
- **Ice:** [[2016rahnamoun-venue-study-ice]].  
- **Geochemistry / organics:** [[2018bree-organic-geoc-origin-formation]].  
- **Water desalination / 2D pores (context):** [[2015surwade-nat-water-desalination]].  
- **Silica + water overlap:** cross-link [[2013muri-venue-jp3086649]], [[2021verma-physical-che-reaxff-reactive]].

## Methods and limitations

**Water models** coupled to **ReaxFF** oxides require consistent **protonation** states; **pH** and **electrochemical potential** are not always explicit in classical reactive MD.

## Related

- [[theme-oxides-silica-ceramics]]  
- [[graphene-nanocarbon]]  

??? info "Maintainers"

    Tag: `domain:water-silica-geo`. Merge overlaps with [[batteries-interfaces-reaxff]] only when papers explicitly bridge both.
