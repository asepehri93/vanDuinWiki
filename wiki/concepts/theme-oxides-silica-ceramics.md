---
id: concept:theme-oxides-silica-ceramics
type: concept
title: "Theme: oxides, silica, and ceramic surfaces (ReaxFF corpus)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "O₂ + hydroxylated silica; ReaxFF SiO extension"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Ni oxidation and O diffusion in metal"
  - paper_id: "paper:2015lloyd-surface-scie-development-reaxff"
    note: "Surface science oriented ReaxFF development"
  - paper_id: "paper:2013verners-venue-paper"
    note: "Al₂O₃ nanoslab / oxide surfaces"
supported_by:
  - "paper:2013muri-venue-jp3086649"
  - "paper:2014zou-acta-materia-molecular-dynamics"
---

<!-- id:concept:theme-oxides-silica-ceramics -->

!!! abstract "TL;DR"

    This cluster covers **oxide and ceramic surfaces** where **bond-breaking chemistry** matters: **silica** under oxygen exposure, **nickel oxidation**, **alumina** nanostructures, and related **surface science** parameterizations. It complements [[batteries-interfaces-reaxff]] (electrolytes) and [[theme-water-silica-geo]] (aqueous geo interfaces).

## Scope (in / out)

**In corpus:** reactive MD with **ReaxFF** (and occasional comparisons) for **Si/O/H**, **Ni/O**, **Al/O**, corrosion, and **thin oxide** films on metals.

**Out of scope here:** purely **non-reactive** classical fits unless the paper is a standard reference for oxide parameters used elsewhere in the wiki.

## Representative papers

- **Silica + O₂:** [[2013muri-venue-jp3086649]] — oxygen reactions with hydroxylated silica; SiO parameter discussion.  
- **Ni oxidation / O in metal:** [[2014zou-acta-materia-molecular-dynamics]] — Ni–O chemistry and oxygen diffusion pathways.  
- **Alumina surfaces:** [[2013verners-venue-paper]], [[2015verners-computationa-al2o3-nanoslab]] — nanoslab and surface models.  
- **Broader oxide / hydroxide interfaces:** [[2018aral-physical-che-oxyhydroxide-metallic]], [[2019hahn-j-phys-chem-surface-reactivity]].  
- **Structural ceramics / high-T oxides:** [[2025krstic-venue-paper]], [[2024baksa-adv-elect-ma-strain-fluctuations]] (check each note for exact system).

## Methods and limitations

**ReaxFF** parameter sets are **element-range specific**; barrier heights and defect energetics should be checked against **DFT** when papers provide both. **Surface reconstructions** and **hydroxyl coverage** strongly affect oxidation onset—simulation cells must be large enough that artificial periodicity does not dominate.

## Open gaps

Debate-style uncertainty on **transferability** of a single Si/O/H set across **amorphous vs crystalline** silica appears across sources; see [[transferability-reactive-ff]].

## Related

- [[reaxff-family]]  
- [[theme-catalysis-surfaces]] (overlapping oxide-supported catalysis)  

??? info "Maintainers"

    **id:** `concept:theme-oxides-silica-ceramics` — align tags with `domain:oxides-ceramics` in [`taxonomy/canonical_tags.yml`](https://github.com/asepehri93/vanDuinWiki/blob/main/taxonomy/canonical_tags.yml). Refresh paper lists when new `wiki/papers/` entries land.
