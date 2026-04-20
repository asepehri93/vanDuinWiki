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
  - paper_id: "paper:2018aral-physical-che-oxyhydroxide-metallic"
    note: "Oxyhydroxide / metallic interfaces"
  - paper_id: "paper:2019hahn-j-phys-chem-surface-reactivity"
    note: "Silicate glass surface reactivity"
  - paper_id: "paper:2014sen-nat-oxidation-assisted-ductility"
    note: "Oxidation-assisted ductility"
  - paper_id: "paper:2013newsome-venue-jp307680t"
    note: "Oxide-related ReaxFF application"
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

## Literature review (this knowledge base)

This subsection is a **corpus-limited review**: it organizes **what the linked paper notes say** about oxides and ceramic interfaces in vanDuinWiki, not an exhaustive survey of all world literature. Open each `[[slug]]` for methods, findings, and citations to the **peer-reviewed source**.

### Silica, oxygen, and gas–surface Si/O chemistry

The KB documents **QM-motivated extensions** of ReaxFF for **oxygen interacting with silica** surfaces, including cluster-model training paths and the **ReaxFF_SiO_GSI** extension discussed in [[2013muri-venue-jp3086649]]. Related **surface science** and **oxide** development lines appear in [[2015lloyd-surface-scie-development-reaxff]] and in **alumina** nanoslab work such as [[2013verners-venue-paper]] and [[2015verners-computationa-al2o3-nanoslab]]. **Silicate glass** and **surface reactivity** angles are developed in notes including [[2019hahn-j-phys-chem-surface-reactivity]] and [[2018ho-venue-paper]].

### Metals, Ni–O, oxidation initiation, and internal oxidation

**Nickel self-diffusion, oxygen diffusion, and oxidation initiation** with ReaxFF are treated in [[2014zou-acta-materia-molecular-dynamics]], which the KB presents as a **validation-heavy** Ni–O line. **Oxidation-assisted ductility** appears in [[2014sen-nat-oxidation-assisted-ductility]]. **Oxyhydroxide / metallic** interface chemistry is summarized on [[2018aral-physical-che-oxyhydroxide-metallic]]. Broader **oxide-supported** and **thin-film** angles show up across additional `domain:oxides-ceramics` notes (see [[paper-index-by-domain]] for the full sortable list).

### Overlap with batteries, water, and catalysis

**Solid electrolyte** oxide chemistry connects outward to [[batteries-interfaces-reaxff]] and [[2018shin-physical-che-development-reaxff]]. **Aqueous films and silica** connect to [[theme-water-silica-geo]] and [[2013muri-venue-jp3086649]]. **Catalyst supports** and **surface reactions** intersect [[theme-catalysis-surfaces]] (e.g. [[2015broqvist-venue-jp5b01597]], [[2013neyts-venue-c3nr00153a]]).

## Debates, tensions, and cross-references

- **Transferability** of a single Si/O/H reactive set across phases and chemistries is discussed at the KB level in [[transferability-reactive-ff]] and in parameterization narratives on individual pages.  
- **ReaxFF vs higher-level QM / MLIPs** for accuracy trade-offs: [[reaxff-vs-mlip-accuracy]], [[reaxff-family]].  
- **Adjacent themes:** [[theme-catalysis-surfaces]], [[theme-water-silica-geo]], [[theme-ferroelectrics-polar-oxides]] (polar perovskites vs generic oxides).

## Representative entry points (short list)

- **Silica + O₂:** [[2013muri-venue-jp3086649]].  
- **Ni oxidation / O in metal:** [[2014zou-acta-materia-molecular-dynamics]].  
- **Alumina surfaces:** [[2013verners-venue-paper]], [[2015verners-computationa-al2o3-nanoslab]].  
- **Broader oxide / hydroxide interfaces:** [[2018aral-physical-che-oxyhydroxide-metallic]], [[2019hahn-j-phys-chem-surface-reactivity]].  
- **Structural / high-T oxides:** [[2025krstic-venue-paper]], [[2024baksa-adv-elect-ma-strain-fluctuations]], [[2023roshan-venue-paper]] (read each note for the exact system).

## Methods and limitations

**ReaxFF** parameter sets are **element-range specific**; barrier heights and defect energetics should be checked against **DFT** when papers provide both. **Surface reconstructions** and **hydroxyl coverage** strongly affect oxidation onset—simulation cells must be large enough that artificial periodicity does not dominate.

??? info "MAS / retrieval"

    **id:** `concept:theme-oxides-silica-ceramics`. Prefer `domain:oxides-ceramics` tags when ingesting new papers. Refresh `source_refs` when major new slugs are added to this narrative.
