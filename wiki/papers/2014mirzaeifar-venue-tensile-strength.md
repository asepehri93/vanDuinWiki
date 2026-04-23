---
id: paper:2014mirzaeifar-venue-tensile-strength
type: paper
title: "Tensile strength of carbyne chains in varied chemical environments and structural lengths"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1088/0957-4484/25/37/371001"
year: 2014
authors:
  - "Reza Mirzaeifar"
  - "Zhao Qin"
  - "Markus J. Buehler"
venue: "Nanotechnology 25, 371001 (2014)"
pdf_sha256: "745a0f4ac8c8b68eff0000597c2532d104643d69d8500610642378e36b231996"
pdf_path: "papers/ReaxFF_others/Mirzaeifar_Zhao_Buehler_carbyne_Nanotech_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014mirzaeifar-venue-tensile-strength -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **Nanotechnology** Fast Track Communication (`doi`). This work uses **classical MD**-style modeling (not ReaxFF-centric in the abstract).

## Summary

**Carbyne** (sp-hybridized carbon chains) **tensile strength** is studied as a function of **chain length**, **temperature**, and **environment** using **molecular dynamics** and a **statistical-mechanics** framework linked to MD-derived **rupture forces**. **Water** interactions are reported to **increase** both **strength** and **rupture strain** relative to the dry case in the abstract’s framing. **Carbyne** is discussed as a **theoretical** **1D** **carbon** allotrope with **extreme** **stiffness**, but **synthesis** and **stabilization** remain difficult—motivating **computational** **mechanics** that explore **ideal** **chains** as **upper** bounds (introduction themes).

## Methods

Grounding: **`papers/ReaxFF_others/Mirzaeifar_Zhao_Buehler_carbyne_Nanotech_2014.pdf`** and `normalized/extracts/2014mirzaeifar-venue-tensile-strength_p1-2.txt` (Nanotechnology **25**, 371001; DOI in front matter).

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **Molecular dynamics simulations** are used to study **carbyne** chains (abstract); **N/A — specific MD package** not stated in the indexed excerpt.
- **System size & composition:** **Carbyne** chains of varied **length** in **dry** versus **water**-influenced environments (abstract); **N/A — atom counts** not in `p1–2` excerpt.
- **Boundaries / periodicity:** **N/A — not stated** in the indexed excerpt.
- **Ensemble:** **N/A — NVT**/**NPT**/**NVE** choice **not stated** in `2014mirzaeifar-venue-tensile-strength_p1-2.txt` (see full **Nanotechnology** article).
- **Timestep / duration / thermostat / barostat:** **N/A — not stated** in the indexed excerpt.
- **Temperature:** **MD** scans across **temperature** values (abstract); exact set points **N/A — not in excerpt**.
- **Pressure:** **N/A — not stated** as a controlled variable in the excerpt.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated.**

### Post-processing (statistical mechanics)

A **theoretical framework** based on **statistical mechanics** and **Bell theory** links **MD** results to **rupture force** and interprets the **physical mechanism** (abstract).

### 2 — Force-field training

**N/A —** this work is an **application**/**mechanics** study, not a **ReaxFF**/**MEAM** parameterization paper.

### 3 — Static QM / DFT-only

**N/A —** not the focus of the abstract in the indexed excerpt (introduction cites broader literature including **first-principles** studies of **carbyne**).

## Findings

### Outcomes and mechanisms

The abstract reports **water** interactions **increase** both **tensile strength** and **rupture strain** versus the **dry** case, and presents the **MD** + **Bell**-linked framework as a rapid way to estimate **rupture force** and mechanism for **carbyne** across **length**, **temperature**, and **environment**.

### Comparisons

The **dry** versus **hydrated** comparison is the primary **experimental design** contrast stated in the abstract for environmental effects on mechanics.

### Sensitivity

**Chain length**, **temperature**, and **chemical environment** are explicit **sensitivity** axes in the abstract’s problem statement.

### Limitations and corpus honesty

Discussion-level **solvent**/**hydrogen-bonding** rationalizations in older wiki text should be treated cautiously unless reproduced from the **full PDF**; prefer **`papers/ReaxFF_others/Mirzaeifar_Zhao_Buehler_carbyne_Nanotech_2014.pdf`** for authoritative mechanism wording beyond the abstract.

## Limitations

Classical interaction model dependence; finite-length **carbyne** remains challenging experimentally—simulation focuses on idealized chains.

**Bell**-theory **extrapolations** depend on **loading rate** and **temperature** windows used in **MD**; **quantitative** **rupture** **forces** should be **recomputed** if **pulling** **protocols** change.

**Carbyne** **stability** under **ambient** conditions remains **experimentally** **challenging**; treat **simulated** **chains** as **model** **systems** for **scaling** trends rather than **guaranteed** **synthesizable** **structures**.

**Environment sweep:** comparing **dry** vs **hydrated** **pulling** highlights how **solvent** can **plasticize** or **stabilize** **strained** **segments**—a useful **template** for other **1D** **nanomechanics** studies.

## Relevance to group

**Carbon nanostructure mechanics** at MIT **Buehler** group; useful neighbor to **ReaxFF carbon** work without being a ReaxFF parameterization paper.

## Citations and evidence anchors

- https://doi.org/10.1088/0957-4484/25/37/371001 — Abstract (Nanotechnology **25**, 371001).

## Related topics

- [[graphene-nanocarbon]]
