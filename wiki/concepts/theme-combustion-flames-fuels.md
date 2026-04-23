---
id: concept:theme-combustion-flames-fuels
type: concept
title: "Theme: fuels, flames, and combustion chemistry (corpus)"
updated: "2026-04-21"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2018qifan-combustion-a-reaxff-simulations"
    note: "Petroleum coke sulfur chemistry; combustion framing"
  - paper_id: "paper:2018jain-j-phys-chem-understanding-combustion"
    note: "Combustion chemistry understanding with reactive MD"
  - paper_id: "paper:2017joshi-combustion-a-observation-deflagration"
    note: "Deflagration / combustion phenomenology in corpus"
  - paper_id: "paper:2021lele-fuel-297-202-reaxff-molecular"
    note: "Aviation-fuel bicyclic chemistry (high-T oxidation networks)"
  - paper_id: "paper:2025li-fuel-404-202-critical-nanoparticle"
    note: "Fuel-adjacent nanoparticle combustion context (read note for scope)"
supported_by:
  - "paper:2018qifan-combustion-a-reaxff-simulations"
  - "paper:2018jain-j-phys-chem-understanding-combustion"
  - "paper:2017joshi-combustion-a-observation-deflagration"
  - "paper:2021lele-fuel-297-202-reaxff-molecular"
  - "paper:2025li-fuel-404-202-critical-nanoparticle"
---

<!-- id:concept:theme-combustion-flames-fuels -->

!!! abstract "TL;DR"

    This theme hub summarizes how the current corpus treats fuel combustion and flame-relevant chemistry, with emphasis on reactive MD studies of high-temperature oxidation, deflagration-related behavior, and coke- or soot-adjacent reaction networks. It is intentionally paired with [[theme-pyrolysis-combustion-organics]], because several papers can be read through either a combustion-first or pyrolysis-first lens depending on the question.

## Scope (in / out)

In scope are corpus pages where combustion is the stated framing: flame chemistry, deflagration, oxidizer-rich high-temperature fuel networks, and petroleum-coke oxidation discussed as combustion behavior. Out of scope are catalyst-focused heterogeneous reaction studies that are better centered in [[theme-catalysis-surfaces]], and slow thermal decomposition studies that are primarily pyrolysis narratives in [[theme-pyrolysis-combustion-organics]].

## How this theme is organized in the corpus

The corpus uses both `domain:fuel-combustion` and `domain:organics-polymers-pyrolysis` for some overlapping studies. Because domain index views can privilege one primary domain tag, this hub acts as a retrieval bridge so combustion-relevant papers remain discoverable even when they are filed under adjacent organic or pyrolysis categories elsewhere.

## Literature review (this knowledge base)

### Coke, sulfur, and high-T oxidation

[[2018qifan-combustion-a-reaxff-simulations]] is the core petroleum-coke anchor in this theme. In the corpus framing, it connects sulfur-containing C/H/O/S chemistry to combustion-relevant high-temperature oxidation pathways. The same underlying chemistry can also appear in pyrolysis discussions, so cross-reading with [[theme-pyrolysis-combustion-organics]] is often necessary for interpretation.

### Combustion phenomenology and reactive pathways

[[2018jain-j-phys-chem-understanding-combustion]] and [[2017joshi-combustion-a-observation-deflagration]] provide the main combustion and deflagration-oriented thread in this corpus slice. They are useful as conceptual entry points for reaction-network reasoning and qualitative combustion behavior in reactive simulations. [[2025li-fuel-404-202-critical-nanoparticle]] is included as a fuel-adjacent combustion context, but users should rely on the associated paper page for exact system boundaries and claim strength.

### Aviation and fuel molecules

[[2021lele-fuel-297-202-reaxff-molecular]] contributes a molecular-level aviation-fuel decomposition example with high-temperature kinetics framing. Within this theme, it functions as a bridge between combustion chemistry questions and fuel-specific mechanism exploration. For questions centered on slow thermal conversion of larger carbonaceous feedstocks, the pyrolysis hub remains the better first stop.

## Analysis and cross-cutting patterns

Across the current corpus, combustion-oriented ReaxFF studies are stronger at exploring possible reaction pathways than at reproducing full experimental flame diagnostics. Reported barriers, temperature windows, and kinetic trends should therefore be interpreted as study-local unless the originating paper explicitly performs cross-model or experiment-facing benchmarking. A recurring pattern is methodological value for hypothesis generation, paired with explicit transferability limits for quantitative prediction outside the trained or validated regime.

## Debates, tensions, and limitations

The boundary between pyrolysis and combustion is not always clean in tagging or narrative emphasis, so retrieval frequently requires checking both this hub and [[theme-pyrolysis-combustion-organics]]. Parameter transferability remains a standing tension for reactive force fields, especially when moving across fuel classes, oxidizer conditions, or thermodynamic regimes; see [[transferability-reactive-ff]] and [[reaxff-family]]. A second active tension is how ReaxFF compares with MLIP-style alternatives for organic combustion chemistry, discussed in [[reaxff-vs-mlip-accuracy]] and [[theme-ml-atomistic-potentials]].

## Gaps and open directions (corpus view)

The combustion slice is still incomplete relative to the full corpus, and this hub should expand as additional `domain:fuel-combustion` paper pages are curated to blueprint depth. The corpus also remains thinner on direct links between atomistic outputs and experimental flame observables, which limits confident cross-paper synthesis on quantitative combustion performance. In practical terms, this page should continue to emphasize what is present in curated notes and avoid extrapolating beyond paper-level evidence.

## Methods and limitations

Most evidence in this hub is derived from reactive atomistic simulations and review-style synthesis rather than one-to-one laboratory flame replication. As a result, combustion interpretations should be read with attention to simulation timescale limits, sampling constraints, and force-field transferability assumptions stated on each paper page. Where a linked page is metadata-thin or fuel-adjacent rather than flame-centered, this hub treats it as contextual support rather than definitive combustion evidence.

## Representative entry points

- For petroleum-coke combustion framing, start with [[2018qifan-combustion-a-reaxff-simulations]].
- For combustion-mechanism overview and reactive MD context, start with [[2018jain-j-phys-chem-understanding-combustion]].
- For deflagration-focused context, start with [[2017joshi-combustion-a-observation-deflagration]].
- For aviation-fuel molecular decomposition under high-temperature conditions, start with [[2021lele-fuel-297-202-reaxff-molecular]].
- For broader discovery across domain tags, use [[paper-index-by-domain]] with `domain:fuel-combustion` and related organics/pyrolysis labels.

??? info "MAS / retrieval"

    **id:** `concept:theme-combustion-flames-fuels`.
    Prefer `domain:fuel-combustion` for combustion-first pages and add cross-links to [[theme-pyrolysis-combustion-organics]] when both framings are valid.
    Refresh `source_refs` and `supported_by` whenever new combustion-focused paper pages are promoted from stubs to evidence-bearing summaries.
