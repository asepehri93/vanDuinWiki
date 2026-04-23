---
id: paper:2025eubert-mahofa-acs-manipulating-intrapore
type: paper
title: "Manipulating Intrapore Energy Barriers in Graphene Oxide Nanochannels for Targeted Removal of Short-Chain PFAS"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:water-silica-geo
  - method:reaxff
  - method:classical-md
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:graphene-carbon
  - keyword:validation-experiment
source_refs: []
doi: "10.1021/acsnano.4c15413"
year: 2025
authors:
  - "Eubert Mahofa"
  - "Sally El Meragawi"
  - "Muhammed A. Vilayatteri"
  - "Swarit Dwivedi"
  - "Manas Ranjan Panda"
  - "Petar Jovanović"
  - "Adri C. T. van Duin"
  - "Benny Freeman"
  - "Akshat Tanksale"
  - "Mainak Majumder"
venue: "ACS Nano"
pdf_sha256: "4d8bfc1b3bfbc61fc289e6cc26dca7ea6b2076b1fc6e556ce2444fc581c5c29d"
pdf_path: "papers/Mahofa_Dwivedi_PFAS_ACS_Nano_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025eubert-mahofa-acs-manipulating-intrapore -->

## Summary

The work reports **β-cyclodextrin–intercalated graphene oxide (GO-βCD)** membranes with **asymmetric nanochannels** that combine high **water permeance** with strong retention of **short-chain perfluorinated acids** from multi-component feeds. **Filtration experiments** (dead-end and cross-flow), **diffusion / Arrhenius** analyses, and complementary **ReaxFF molecular dynamics** on **PFAS** binding to **α/β-cyclodextrin** support an **intrapore energy-barrier** picture versus pristine GO and **αCD**-modified GO.

Broader framing highlights persistent **PFAS** contamination and the difficulty of removing short-chain species that pass many membranes; modifying **GO** interlayer chemistry is presented as tuning **host–guest** binding and activation barriers that set selective rejection under realistic mixed feeds.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

- **Membrane fabrication (experimental):** **Shear-alignment printing** of **GO** with added **αCD** or **βCD** (heated **90 °C**, **2 h** stirring), coated on **PVDF** supports; **80 °C** post-bake (**1 h**). Dead-end tests (**Sterlitech HP4750**, **14.6 cm\(^2\)**, **2 bar**, **400 rpm** stirring); cross-flow long-term trials (**CF042** cells, **42 cm\(^2\) active area**). PFAS quantification by **LC–MS** (Agilent workflow described in the article).
- **Diffusion / barriers:** Temperature-dependent diffusion cells (**283–315 K**) used to extract **activation energies** via Arrhenius plots of permeation rates as defined in the paper (Eqs. 1 and 7 in the manuscript).
- **ReaxFF binding simulations:** **Molecular dynamics** in **Amsterdam Modeling Suite (AMS)** using **reactive ReaxFF** and **C/H/O/F** parameters from the **Liu / Gao / Arkoub** fluorinated-organic line; **EEM** charges trained against **HF** atomic charges. At least **15** starting poses per **PFAS×CD** pair, **conjugate-gradient** relaxation (**1 meV/atom**), then **500 ps** **NVT** segments at **300 K** with a **0.25 fs** **time step** and a canonical **thermostat** (type per **PDF**); gas-phase **complexes** use **3D PBC** or large vacuum **cells** as in the article. Minimum-energy frames support **binding energy** decomposition (Eq. 8). **N/A — NPT** **barostat** / isotropic **pressure** control in this **constant-volume** binding pass; **N/A — metadynamics**; **N/A — applied electric field** in the protocol quoted here.

## Findings

- **GO-βCD** achieves **>90%** simultaneous retention of **PFBA, PFPeA, PFHxA, PFOA** from a four-component challenge feed with reported **permeance ~21.7 ± 2 L m\(^{-2}\) h\(^{-1}\) bar\(^{-1}\)** and large **feed up-concentration** (~**300%** in the abstract scenario).
- Simulations report **~20% stronger** **binding** of short-chain **PFAS** to **βCD** versus other **cyclodextrin** models examined, aligning with **barrier** trends versus **GO-αCD** and pristine **GO** (although membrane transport is not fully atomistic, see **Limitations**).
- **Compared** to **NF270**, **GO-βCD** retains far more **short-chain** species (e.g. **PFBA** retention **~35%** vs **~89%** in the quoted table), with **higher water permeance** in the **experiments** summarized—**corpus honesty**: numbers are as stated in the **PDF**, not re-derived here.

## Limitations

**ReaxFF** **binding** runs are **short** **gas-phase** **cyclodextrin** models; **membrane** **transport** and **multicomponent** **fouling** are only partially captured atomistically. **Experimental** feeds and **pH** may extend beyond simulated conditions.

## Relevance to group

**Adri C. T. van Duin** on **ReaxFF** support for **PFAS**–**cyclodextrin** interactions paired with **GO** **membrane** experiments (**Majumder** group context).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acsnano.4c15413](https://doi.org/10.1021/acsnano.4c15413)

## Related topics

- [[reaxff-family]]
