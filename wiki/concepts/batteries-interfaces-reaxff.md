---
id: concept:batteries-interfaces-reaxff
type: concept
title: "Battery interfaces and electrolytes modeled with ReaxFF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Abstract"
    note: "Ceramic NASICON/LATP electrolyte; composition-dependent Li transport"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Abstract"
    note: "Liquid carbonate electrolyte decomposition and Li0/Li+ discrimination"
  - paper_id: "paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism"
    section: "Abstract"
    note: "Si anode degradation; microscopy + ReaxFF on delithiation-driven processes"
supported_by:
  - "paper:2018shin-physical-che-development-reaxff"
  - "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
  - "paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism"
---

<!-- id:concept:batteries-interfaces-reaxff -->

## One-paragraph summary

Across the corpus, **ReaxFF** is used to connect atomistic detail to several **Li-ion battery** subproblems: **solid ceramic electrolytes** (NASICON-type LATP), **liquid carbonate electrolytes** at reducing anodes, and **Si anode** degradation phenomena alongside experiments. The unifying theme is that reactive MD can expose **composition-dependent transport**, **electrolyte decomposition sequences**, and **morphological evolution** that are difficult to infer from continuum models alone—provided the parameterization is validated for the chemistry at hand.

## Definitions and scope

- **Solid electrolytes:** ionic conductivity and site occupancies in oxide/phosphate frameworks.
- **Liquid electrolytes:** bond-making/breaking reactions involving solvent and salt species near Li0.
- **Electrodes:** Si and related materials where large volume change and SEI chemistry couple to (de)lithiation.

## Evidence across the literature

- **LATP:** Shin et al. demonstrate composition-sensitive Li transport and MC/MD sampling of disordered configurations (`paper:2018shin-physical-che-development-reaxff`).
- **Carbonate electrolytes:** Hossain et al. extend ReaxFF to common solvents/salt chemistry and distinguish Li0 vs Li+ reactivity (`paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation`).
- **Si degradation:** Foss et al. combine microscopy with ReaxFF to emphasize delithiation-driven Si redistribution (`paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism`).

## Implications for simulation and force fields

Reactive models are most valuable when **training sets explicitly include** the reactions and phases relevant to the interface problem; otherwise, predictions should be treated as hypotheses for further DFT or experiment.

## Related pages

- [[reaxff-family]]
- [[graphene-nanocarbon]]
