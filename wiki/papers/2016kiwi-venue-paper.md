---
id: paper:2016kiwi-venue-paper
type: paper
title: "Metal-nanotube composites as radiation resistant materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reaxff-lineage
  - method:reaxff
  - material:graphene-carbon-nano
  - material:alloy-bulk
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4959246"
year: 2016
authors:
  - "Rafael I. González"
  - "Felipe Valencia"
  - "José Mella"
  - "Adri C. T. van Duin"
  - "Kang Pyo So"
  - "Ju Li"
  - "Miguel Kiwi"
  - "Eduardo M. Bringa"
venue: "Appl. Phys. Lett."
pdf_sha256: "e70b96302b011f09ad8c4f006da1002a2dced9180459489638c101ecdad14f82"
pdf_path: "papers/Kiwi_APL_2016_proof.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2016kiwi-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Reactive MD (ReaxFF)** in **LAMMPS** is used to study **He behavior in Ni matrices** containing an **embedded carbon nanotube (CNT)**. For **defect-free** tubes, **He** is reported to **diffuse along metal–CNT interfaces** and accumulate without **permeating** the **graphene wall**, consistent with **impermeable perfect graphene**. When **vacancy defects** are introduced as a proxy for **radiation damage**, **He** can **penetrate** the CNT, which then acts as a **“nano-chimney”** facilitating **outgassing** and **reducing bubble formation** in the metal. The authors connect the mechanism to improved **radiation tolerance** of **metal–CNT composites**.

## Methods

- **ReaxFF MD** with **dynamic charge equilibration** (QEq-style treatment as described in the paper) for **Ni–C–He** systems.
- **NPH** ensemble simulations at **~1000 K** with **He** concentrations and **vacancy** patterns outlined in the article.

## Findings

- **Defect-free CNT**: **interfacial He accumulation** without trans-wall leakage in the baseline scenario summarized in the abstract.
- **Defective CNT**: **He penetration** and **fast axial transport** enabling **outgassing** pathways.
- Positions **CNT metal-matrix composites** as candidates for **He-management** in **irradiated structural metals**.


## Limitations

- **Simplified radiation damage** (random vacancies) omits **cascade mixing**, **dislocation networks**, and **transmutation chemistry**.
- **Proof PDF** may differ cosmetically from the **final APL** layout.

## Relevance to group

**International collaboration** with **van Duin** providing **ReaxFF parameter expertise** for **nuclear materials / He embrittlement** modeling.

## Citations and evidence anchors

- Abstract-level summary supported by `papers/Kiwi_APL_2016_proof.pdf`; **DOI:** `10.1063/1.4959246`.

## Related topics

- [[reaxff-family]]
