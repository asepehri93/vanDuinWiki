---
id: paper:2015surwade-nat-water-desalination
type: paper
title: "Water desalination using nanoporous single-layer graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:2d-layered
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1038/nnano.2015.37"
year: 2015
authors:
  - "Sumedh P. Surwade"
  - "Sergei N. Smirnov"
  - "Ivan V. Vlassiouk"
  - "Raymond R. Unocic"
  - "Gabriel M. Veith"
  - "Sheng Dai"
  - "Shannon M. Mahurin"
venue: "Nature Nanotechnology (2015)"
pdf_sha256: "c742f307d5cd24fdc5bbe6ac7bc61eafa53abacfd9fc91cf813bb3b3e1678bff"
pdf_path: "papers/Others/nnano.2015.37.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015surwade-nat-water-desalination -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **Nature Nanotechnology** article identified by `doi` and `pdf_path`. This is an **experimental membrane** study, not an atomistic simulation paper.

## Summary

Surwade *et al.* demonstrate **desalination** through **nanoporous single-layer graphene**: **oxygen-plasma etching** introduces **nm-scale** pores whose density/size can be tuned, yielding membranes with **nearly 100% salt rejection** and **high water permeance**. Under **pressure-driven** flow, water fluxes up to **~10⁶ g m⁻² s⁻¹** at **40 °C** are reported in the abstract, whereas **osmotic-pressure-driven** measurements remain **≤70 g m⁻² s⁻¹ atm⁻¹** in the same abstract framing. The work connects to prior **theoretical** predictions that **sub-nm** pores can reject ions while transmitting water, and to an emerging **experimental** literature on **graphene / graphene-oxide** membranes.

## Methods

**Experimental fabrication and metrology (no atomistic MD headline).** **Graphene growth/transfer:** **CVD** **single-layer graphene** on **Cu** with **polymer-assisted transfer** onto **SiN** microchips containing a **~5 µm** suspended aperture; **SEM** screens membrane integrity (fractions of successful devices reported in the article). **Pore generation:** **oxygen plasma** exposure with controlled dose; **Raman** tracks **defect metrics** (e.g., **I_D/I_G**) versus plasma time. **Structure–transport links:** **aberration-corrected STEM** correlates **pore statistics** with separation performance. **Transport tests:** **pressure-driven** permeation and **osmotic-driving-force** permeation configurations as described in Methods (numerical tables on `pdf_path`). **Control experiments:** the article contrasts **plasma** pore formation with alternate **electron** / **ion** damage routes, emphasizing cases where **Raman** changes do **not** imply useful **nanopore** permeation.

**MD application:** **N/A** — not an MD/AIMD methods paper.

**Force-field training:** **N/A**.

**Static QM / DFT:** **N/A** as a reported author workflow in the abstract/opening framing (the article cites prior **theoretical** literature).

## Findings

**Separation:** **Near-complete salt rejection** with **very high water permeance** under the reported **pressure-driven** conditions (abstract).

**Processing–structure:** **Oxygen plasma** yields **tunable** **nm-scale** pores tracked by **Raman**; **STEM** ties **pore morphology/density** to **transport**.

**Mechanistic nuance:** **Not all** radiation-induced defects that change **Raman** produce **useful water pores**—some **e-beam** / **ion** routes show **negligible water transport** despite **defect indicators**, underscoring that **defect chemistry and connectivity** matter beyond a single **Raman** proxy (article discussion; see `pdf_path`).

**Comparisons:** The abstract contrasts **pressure-driven** permeance (up to **~10⁶ g m⁻² s⁻¹** at **40 °C**) with **osmotic** driving-force results (≤**70 g m⁻² s⁻¹ atm⁻¹**) and cites prior **theoretical** graphene-membrane literature.

**Sensitivity:** **Pore size** and **plasma dose** tune **salt rejection** vs **water flux**; **driving force** (pressure vs osmotic) changes reported **permeance** metrics.

**Limitations / outlook:** **Fouling**, **long-term stability**, and **scale-up** remain open; the article positions results as a demonstration rather than a deployed technology.

## Limitations

**Pore-size distributions**, **long-term fouling/scaling**, and **manufacturing scalability** remain open engineering concerns outside a single demonstration. **Transport interpretation** depends on **pore chemistry** and **hydration** details not fully captured by **macroscopic** metrics alone. Tabulated transport **numbers** and **microscopy** statistics should be read from **`pdf_path`** when precision matters.

## Relevance to group

Corpus **reference** for **2D carbon membranes** and **water transport** adjacent to atomistic **graphene** modeling papers.

## Citations and evidence anchors

- DOI: [10.1038/nnano.2015.37](https://doi.org/10.1038/nnano.2015.37)
- `normalized/extracts/2015surwade-nat-water-desalination_p1-2.txt`

## Related topics

- [[graphene-nanocarbon]]
