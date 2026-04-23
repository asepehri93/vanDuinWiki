---
id: concept:batteries-interfaces-reaxff
type: concept
title: "Battery interfaces and electrolytes modeled with ReaxFF"
updated: "2026-04-23"
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

!!! abstract "Entry point: ReaxFF for battery interfaces and electrolytes"
    This page helps readers decide where to start when asking interface-focused battery questions with a reactive force field. In this corpus, the strongest starting points are LATP solid-electrolyte transport, carbonate-electrolyte reduction chemistry near Li metal, and Si-anode degradation under (de)lithiation-linked conditions.

## Scope and user intent

This entry point is for users who need a query-first map from battery interface questions to relevant ReaxFF evidence in this knowledge base. It is intended for triage questions such as "which paper is best for LATP transport trends?", "where is Li0 vs Li+ solvent reactivity treated?", or "which source connects Si morphology change to reactive simulations?"

This page does not claim a complete world-literature review of battery interfaces. It only synthesizes what is currently represented in linked `paper:` pages and `source_refs`.

## Start-here pathways

If your goal is to understand composition-sensitive ion transport in a ceramic solid electrolyte, start with [[2018shin-physical-che-development-reaxff]] and then compare assumptions against [[reaxff-family]].

If your goal is to inspect reduction chemistry in carbonate liquid electrolytes near Li metal, start with [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] and then route to [[reaxff-parameterization-workflow]] for parameter-coverage checks.

If your goal is to connect reactive simulation with experimentally visible Si-anode degradation behavior, start with [[2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism]] and then evaluate transferability caveats in [[transferability-reactive-ff]].

## Decision levers and trade-offs

The first decision lever is chemistry coverage in the force-field training set. For this corpus slice, LATP transport, carbonate solvent/salt decomposition behavior, and Si-focused delithiation processes are represented in different papers with different emphasis, so transfer across subdomains should be treated cautiously.

The second lever is mechanism fidelity versus transferability risk. Reactive MD can expose bond-breaking pathways and morphology evolution, but conclusions are most robust when the study-specific chemistry and conditions are close to the target use case.

The third lever is evidence modality. One route is simulation-focused protocol inference (LATP and electrolyte chemistry papers), while another route combines simulation with microscopy-grounded interpretation (Si degradation paper).

## Canonical starting papers

- [[2018shin-physical-che-development-reaxff]] (`paper:2018shin-physical-che-development-reaxff`) for NASICON/LATP composition-dependent Li transport and disordered-configuration sampling context.
- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] (`paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation`) for carbonate electrolyte decomposition chemistry and Li0 versus Li+ reactivity distinctions.
- [[2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism]] (`paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism`) for Si-anode degradation interpretation that explicitly couples microscopy observations with ReaxFF analysis.

## Related protocols and debates

- Protocol: [[reaxff-parameterization-workflow]] for practical checks on training-data scope, optimization assumptions, and validation expectations before extending to new interface chemistries.
- Debate: [[transferability-reactive-ff]] for cross-chemistry and cross-regime transferability limits that directly affect battery-interface inference quality.
- Debate: [[reaxff-vs-mlip-accuracy]] for when a reactive force-field route is preferable versus alternative interatomic-modeling strategies.
- Adjacent navigation: [[theme-oxides-silica-ceramics]] and [[themes-index]] for broader materials context beyond battery-specific interface questions.

## Failure modes and interpretation pitfalls

A common failure mode is over-generalizing a ReaxFF result from one interface chemistry to another without checking whether the target reactions and charge states were represented in training and validation.

Another pitfall is reading mechanism-level confidence into thinly constrained outputs when the paper itself only supports narrower conclusions. In this corpus, claims should stay tied to the specific paper context and not be promoted to universal battery-interface behavior.

A third pitfall is conflating pathway discovery with predictive ranking. Reactive trajectories can propose plausible decomposition or degradation routes, but ranking rates, selectivity, or long-timescale outcomes typically requires additional validation.

??? info "MAS / retrieval"
    - Stable id: `concept:batteries-interfaces-reaxff`
    - Query synonyms: "battery interface reaxff", "lithium electrolyte decomposition reaxff", "LATP transport reaxff", "Si anode degradation reactive MD"
    - Canonical tags: `domain:batteries-electrochemistry`, `method:reaxff`, `task:application`
    - Primary source anchors: `paper:2018shin-physical-che-development-reaxff`, `paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation`, `paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism`
    - Refresh policy: update `source_refs` and pathway guidance when battery-interface or electrolyte-focused ReaxFF papers are added to the corpus.
