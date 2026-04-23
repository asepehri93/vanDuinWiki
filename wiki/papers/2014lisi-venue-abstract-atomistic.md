---
id: paper:2014lisi-venue-abstract-atomistic
type: paper
title: "Atomistic investigation of lithiation behaviors in silicon nanowires: reactive molecular dynamics simulation (IMLB 2014 abstract)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:reaxff-parameterization
candidate_tags: []
source_refs: []
doi: ""
year: 2014
authors:
  - "H. Jung"
  - "J. Joo"
  - "K. R. Lee"
  - "S. S. Han"
venue: "17th International Meeting on Lithium Batteries (IMLB 2014), poster abstract"
pdf_sha256: "e29eb905a5abdf47a60411075da4c7d6a692e36dbb48f5b2bf6af4f59f4a0093"
pdf_path: "papers/ReaxFF_others/LiSi_abstract_Han_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014lisi-venue-abstract-atomistic -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes a **conference poster abstract** (ECS/IMLB web program text), **not** a full journal article. Claims below follow the abstract wording; there is **no DOI** in the corpus record.

## Summary

Poster abstract on **lithiation of silicon nanowires** using **ReaxFF** trained for **Si–Li** chemistry from **DFT** references. Motivation is **high capacity** vs **large volume expansion** of Si anodes; nanowires are presented as a geometry that can **relax** without pulverization. **Reactive MD** is stated to reproduce **anisotropic expansion** and **Li diffusion** trends consistent with experiment, as a route to **atomistic lithiation mechanism** insight for electrode design. The abstract situates the work in the broader **Li-ion** literature on **alloy anodes**, where **stress** and **diffusion** couple strongly at **interfaces** and **wire** geometries are often invoked to mitigate **particle fracture** in **composite** electrodes.

## Methods

### Source type (conference abstract only; checklist D)

- This page summarizes an **IMLB 2014 poster abstract** text captured in `normalized/extracts/2014lisi-venue-abstract-atomistic_p1-2.txt`—not a peer-reviewed full article.

### Force field and simulation class (as claimed in the abstract)

- **ReaxFF** parameters for **Si–Li** chemistry are stated to be trained against **DFT** reference data (**abstract**).
- **Reactive MD** of **Si nanowire** lithiation is reported at **nanosecond-accessible** timescales in the abstract wording (**abstract**).

### Missing protocol detail (explicit)

- **System sizes**, **timestep**, **ensemble**, **thermostat**, **cutoffs**, and **quantitative validation metrics** are **not** present in the one-page ingest—do **not** infer them for MAS answers.

### 1 — MD application (Si nanowire lithiation)

- **Engine / code:** **Reactive molecular dynamics** is stated in the poster **abstract**; **N/A — MD engine string not in the one-line abstract ingest**.
- **System size & composition:** **Silicon nanowire** models are named in the **abstract**; **atom counts**/**supercell** dimensions are **N/A — not present in the IMLB 2014 poster abstract text ingested as `papers/ReaxFF_others/LiSi_abstract_Han_2014.pdf` / `normalized/extracts/2014lisi-venue-abstract-atomistic_p1-2.txt`**.
- **Boundaries / periodicity / timestep / thermostat / duration:** **N/A — not present in the abstract-only ingest**.
- **Ensemble:** **NVT**/**NPT**/**NVE** are **not** specified in the poster **abstract** ingest—**N/A — confirm in any subsequent journal article**.
- **Temperature:** **N/A — explicit simulation temperature (e.g., 300 K) not present in the abstract-only ingest**.
- **Hydrostatic pressure / barostat:** **N/A — not present in the abstract-only ingest**.
- **Electric field:** **N/A — not stated** in the abstract-only ingest.
- **Replica / enhanced sampling:** **N/A — not stated** in the abstract-only ingest.

### 2 — Force-field training (Si–Li ReaxFF)

- **QM reference / training set / optimization:** stated only at the level of **DFT-trained ReaxFF** for **Si–Li** chemistry (**abstract**); **N/A — no functional/basis/training-set tables in this ingest**.

## Findings

### Outcomes and mechanisms

The **abstract** reports motivation from **high capacity** of Si (**~4200 mA h g⁻¹** for **Li₄.₂Si** vs **~372 mA h g⁻¹** for **LiC₆** graphite) and **large volume change (~300%)** driving pulverization, with **nanowires** proposed to relax without breaking.

### Comparisons to experiment

It states that **ReaxFF MD** reproduces **experimental** **anisotropic volume expansion** during lithiation and **Li diffusion** behavior (poster **abstract** wording).

### Sensitivity and design levers

**Nanowire** geometry is presented as a **design** lever to mitigate fracture versus bulk particles; **quantitative** trends are **not** in the one-page ingest.

### Limitations and corpus honesty

This is an **IMLB 2014 poster abstract**, not a peer-reviewed full article (**## Limitations**). **Quantitative** **diffusion** coefficients and **validation** protocols must come from a **journal** version if/when ingested—do **not** infer them from this **PDF** alone.

## Limitations

**Abstract-only** source; no peer-reviewed article text in this ingest; numerical benchmarks and system sizes are **not** verified from this PDF. Conference **posters** may summarize **ongoing** work; any **quantitative** diffusion coefficients or **strain** fields should be confirmed against a **journal** article or **preprint** if one becomes available in the corpus. This page is intentionally **thin** on **methods** detail because the **ECS** web program excerpt does not provide **timestep**, **ensemble**, or **validation** protocols at the level expected of a **full** **article** note.

## Relevance to group

**Si anode / ReaxFF** line adjacent to broader **Li-ion interface** work; overlaps thematically with [[batteries-interfaces-reaxff]] and Si NW lithiation studies in the corpus.

## Citations and evidence anchors

- ECS Confex web program entry (abstract text reproduced in `normalized/extracts/` for this slug)—**no journal DOI** in front matter.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
