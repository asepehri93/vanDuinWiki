---
id: concept:theme-porous-mof-zeolite
type: concept
title: "Theme: porous media, MOFs, and zeolites (corpus touchpoints)"
updated: "2026-04-20"
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

    This cluster is a **routing hub** for **porous** and **confined** reactive environments. The KB’s **explicit** MOF/zeolite paper count is **smaller** than for **oxides** or **catalysis**; many links are **adjacent** (catalytic surfaces, silica, carbon nanostructures). Prefer [[paper-index-by-domain]] for authoritative coverage.

## Scope (in / out)

**In corpus:** papers tagged `domain:porous-mof-zeolite` **plus** **neighboring** catalysis and surface notes where **confinement** or **porous support** is part of the story.

**Out of scope:** claims about specific **MOF** structures **not** present on a wiki page.

## Literature review (this knowledge base)

**Honest corpus scope:** vanDuinWiki is **ReaxFF-centric**; **MOF** and **zeolite** entries may be **sparse** relative to bulk oxides. This section tells you **where to look** and **what is adjacent**.

### Catalytic surfaces and confined reactants

[[2015broqvist-venue-jp5b01597]] (CO₂ hydrogenation) and [[2013neyts-venue-c3nr00153a]] (carbon surface reactions) are the KB’s strongest **catalysis** anchors that often **pair** with **porous catalyst** discussions in the broader literature. Here, treat them as **entry points** when the user question is **surface chemistry inside a porous medium** rather than **bulk micropore diffusion** (which may not be modeled explicitly on the page).

### Silica, glasses, and nanopore-like surface chemistry

[[2013muri-venue-jp3086649]] and [[2019hahn-j-phys-chem-surface-reactivity]] document **silica / silicate** surface chemistry relevant to **mesoporous silica** and **glass** surfaces. [[2018ho-venue-paper]] may add **oxide** surface context—follow the paper note.

### What the KB does not promise

If a **specific MOF name** or **zeolite framework** is not on a paper page, **do not infer** parameters or mechanisms from this hub alone.

## Debates, tensions, and cross-references

- **Force field transferability** to **open-metal-site** MOFs is **contentious** in the wider field; the KB addresses it only where paper pages do—see [[transferability-reactive-ff]].  
- **Adjacent themes:** [[theme-catalysis-surfaces]], [[theme-water-silica-geo]] (hydrated pores), [[theme-oxides-silica-ceramics]].

## Representative entry points

- **Catalysis (porous adjacency):** [[2015broqvist-venue-jp5b01597]], [[2013neyts-venue-c3nr00153a]].  
- **Silica / glass surfaces:** [[2013muri-venue-jp3086649]], [[2019hahn-j-phys-chem-surface-reactivity]].  
- **Domain listing:** [[paper-index-by-domain]] (`domain:porous-mof-zeolite`).

## Methods and limitations

**Reactive MD** in **micropores** requires **large** cells and **long** timescales for **adsorption/desorption** equilibria; many studies focus on **local** active sites instead.

??? info "MAS / retrieval"

    **id:** `concept:theme-porous-mof-zeolite`. As MOF/zeolite-tagged papers are added, expand this hub’s **Literature review** with **verbatim** pointers to new `[[slug]]` pages.
