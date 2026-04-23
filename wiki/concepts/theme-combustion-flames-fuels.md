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
---

<!-- id:concept:theme-combustion-flames-fuels -->

!!! abstract "TL;DR"

    This hub gathers **fuel** and **combustion-forward** simulations documented in vanDuinWiki—**high-temperature oxidation**, **flame-relevant** chemistry, and **soot**/**coke** stories—**separately** from [[theme-pyrolysis-combustion-organics]], which foregrounds **slow thermal** pyrolysis and **carbonaceous** decomposition when that is the paper’s emphasis. Many papers are cross-listed; follow each **`[[slug]]`** for authoritative scope.

## Scope (in / out)

**In corpus:** notes whose **headline** is **combustion**, **flame**, **deflagration**, **oxidizer-rich** high-T organic networks, or **petroleum coke** under **combustion** framing.

**Out of scope here:** **heterogeneous catalysis** on well-defined catalysts (see [[theme-catalysis-surfaces]]); **slow** coal **pyrolysis** without combustion framing (see pyrolysis theme first).

## How this theme is organized in the corpus

Use **`domain:fuel-combustion`** and **`domain:organics-polymers-pyrolysis`** tags on paper pages together with this hub: the **first** `domain:` tag still drives [[paper-index-by-domain]], so combustion-first papers may appear under organics—this page compensates for that sort ambiguity.

## Literature review (this knowledge base)

### Coke, sulfur, and high-T oxidation

[[2018qifan-combustion-a-reaxff-simulations]] develops **petroleum coke** chemistry with explicit **combustion** framing in the KB summary—pair with [[theme-pyrolysis-combustion-organics]] when the same **C/H/O/S** network is discussed as **pyrolysis**.

### Combustion phenomenology and reactive pathways

[[2018jain-j-phys-chem-understanding-combustion]] and [[2017joshi-combustion-a-observation-deflagration]] anchor **combustion** and **deflagration** threads. [[2025li-fuel-404-202-critical-nanoparticle]] appears in **fuel**-oriented venues; read the paper note for the exact **system** and **claims**.

### Aviation and fuel molecules

[[2021lele-fuel-297-202-reaxff-molecular]] documents **aviation-fuel** bicyclic **decomposition** with Arrhenius-style reporting—use for **high-T fuel** chemistry; when the question is **slow pyrolysis** of large carbonaceous models, prefer the pyrolysis hub’s coal-centric anchors.

## Analysis and cross-cutting patterns

Where papers report **barriers** and **temperature** windows, treat comparisons as **paper-local** unless the same paper explicitly benchmarks models. **ReaxFF** combustion studies in this corpus often emphasize **reaction network** exploration over **experimental flame-speed** matching—check each note.

## Debates, tensions, and limitations

- **Pyrolysis vs combustion** boundaries are **not** always sharp in tags—use both hubs and the paper page.  
- **Transferability** of reactive parameters: [[transferability-reactive-ff]], [[reaxff-family]].  
- **MLIPs** vs ReaxFF for organics: [[reaxff-vs-mlip-accuracy]], [[theme-ml-atomistic-potentials]].

## Gaps and open directions (corpus view)

Not every **fuel** paper in the KB is yet summarized here; expand this narrative as additional **`domain:fuel-combustion`** pages are curated. **Experimental** flame diagnostics are rarely reproduced in atomistic detail—state limitations per paper.

## Representative entry points

- **Petroleum coke / combustion:** [[2018qifan-combustion-a-reaxff-simulations]].  
- **Combustion MD surveys:** [[2018jain-j-phys-chem-understanding-combustion]].  
- **Deflagration:** [[2017joshi-combustion-a-observation-deflagration]].  
- **Aviation fuel:** [[2021lele-fuel-297-202-reaxff-molecular]].  
- **Fuel index:** [[paper-index-by-domain]] (`domain:fuel-combustion`, `domain:organics-polymers-pyrolysis`).

## Methods and limitations

**Reactive MD** trajectories may be **short** relative to laboratory **residence times**; **ignition** and **branching** chemistry require **careful** interpretation against the cited source.

??? info "MAS / retrieval"

    **id:** `concept:theme-combustion-flames-fuels`. Prefer `domain:fuel-combustion` when ingesting **combustion-first** papers; cross-link [[theme-pyrolysis-combustion-organics]] when both themes apply.
