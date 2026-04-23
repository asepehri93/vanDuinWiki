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
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2016kiwi-venue-paper -->

## Summary

**Reactive MD (ReaxFF)** in **LAMMPS** is used to study **He behavior in Ni matrices** containing an **embedded carbon nanotube (CNT)**. For **defect-free** tubes, **He** is reported to **diffuse along metal–CNT interfaces** and accumulate without **permeating** the **graphene wall**, consistent with **impermeable perfect graphene**. When **vacancy defects** are introduced as a proxy for **radiation damage**, **He** can **penetrate** the CNT, which then acts as a **“nano-chimney”** facilitating **outgassing** and **reducing bubble formation** in the metal. The study connect the mechanism to improved **radiation tolerance** of **metal–CNT composites**. The **nano-chimney** picture is explicitly offered as a **microstructural** strategy to **reroute** **He** away from **matrix** bubble nucleation sites that would otherwise embrittle **structural** alloys.

## Methods

**LAMMPS** reactive MD with **ReaxFF** for Ni–C–He combines parametrizations for Ni/C, C/noble gas, and related interactions as referenced in the article. Three-dimensional periodic Ni supercells (**2.5–4.5 nm** lateral sizes) embed single **(10,0)** or **(20,0)** carbon nanotubes along **z**; helium is added either by replacing **10%** of Ni sites or by placing a **~1 nm** He slab (with **3×** replication along **z** in one variant). The protocol uses **NPH** integration with **Nose–Hoover**-style thermostat and barostat controls (**500 fs** pressure damping toward **~1 atm**) plus auxiliary temperature rescaling every **10** steps when kinetic temperature drifts by about **5%** from the **1000 K** target, as described in the *Appl. Phys. Lett.* article. Timestep **0.5 fs**; the authors describe multi-ns relaxation followed by **4–5 ns** production at **1000 K**. Dynamic charge equilibration (QEq-like) runs each timestep per the manuscript. Applied electric fields and umbrella, metadynamics, or replica-exchange sampling are not used.

**Force-field training.** **N/A** — combines literature ReaxFF sets with Morse treatment of noble-gas interactions as described in the paper rather than reporting a de novo fit here.

**Static QM / DFT.** **N/A** — classical reactive MD study.

## Findings

For defect-free CNTs, He diffuses along Ni–CNT interfaces and accumulates without crossing an ideal graphene wall (abstract). For vacancy-containing CNTs as a radiation-damage proxy, He penetrates the wall and the CNT acts as a “nano-chimney” for outgassing, reducing matrix bubble formation relative to Ni+He without a CNT in the baseline described. Discussion cites experimental Al+CNT composites with bubble-free matrices as motivation while the MD supplies a mechanistic picture of He transport. Structural knobs include CNT chirality **(10,0)** versus **(20,0)**, He loading (**uniform 10%** versus localized implant layer), and vacancy-induced permeability. The text notes that strain at Ni–CNT interfaces is modest in the samples shown but could modify He storage at higher strain, and that dislocation–CNT interactions could add free volume.

**Corpus note.** Local `pdf_path` is an **APL proof** PDF—confirm figure pagination against the final *Appl. Phys. Lett.* issue when auditing visuals.

## Limitations

- **Simplified radiation damage** (random vacancies) omits **cascade mixing**, **dislocation networks**, and **transmutation chemistry**.
- **Proof PDF** may differ cosmetically from the **final APL** layout.
- **CNT** **chirality** and **metal–CNT** **interface** chemistry are idealized; real composites include **interfacial** **oxides** and **strain** fields not represented in the baseline **Ni** matrix models summarized here.

## Relevance to group

**International collaboration** with **van Duin** providing **ReaxFF parameter expertise** for **nuclear materials / He embrittlement** modeling.

## Citations and evidence anchors

- Abstract-level summary supported by `papers/Kiwi_APL_2016_proof.pdf`; **DOI:** `10.1063/1.4959246`.
- **Corpus catalog (proof PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) — confirm figure pagination against the **final APL** issue when available.

## Related topics

- [[reaxff-family]]
