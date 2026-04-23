---
id: paper:2020gao-venue-stable-metal
type: paper
title: "Stable metal anodes enabled by a labile organic molecule bonded to a reduced graphene oxide aerogel"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - material:li-metal-anode
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:graphene-carbon
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.2001837117"
year: 2020
authors:
  - "Yue Gao"
  - "Daiwei Wang"
  - "Yun Kyung Shin"
  - "Zhifei Yan"
  - "Zhuo Han"
  - "Ke Wang"
  - "Md Jamil Hossain"
  - "Shuling Shen"
  - "Atif AlZahrani"
  - "Adri C. T. van Duin"
  - "Thomas E. Mallouk"
  - "Donghai Wang"
venue: "Proc. Natl. Acad. Sci. U.S.A."
pdf_sha256: "bde1e1148c09c22326907f8fa879721a409c16612a308b4730bf93abaf7c5b70"
pdf_path: "papers/Gao_Shin_Hossain_PNAS_2020_SEI_design.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020gao-venue-stable-metal -->

**Benzenesulfonyl fluoride** grafted to **reduced graphene oxide aerogel** releases **benzenesulfonate** and **LiF**-contributing species during plating, homogenizing **Li/Na/Zn** deposition and improving **SEI** stability at **high current** and **sub-zero** temperatures.

## Summary

The study targets **dendritic plating** and **unstable SEI** on **Li, Na, Zn** metals by anchoring an **electrochemically labile** molecule (**benzenesulfonyl fluoride**, BSF) on a conductive **rGO aerogel** scaffold. During operation, BSF fragments generate **metal-coordinating sulfonate** species that steer **uniform flux**, while **fluoride**-containing fragments enrich **LiF** in the SEI for passivation. **Li||LiCoO\(_2\)** cells are reported with strong **cycling** at **6 mA cm\(^{-2}\)** and **−10 °C** tolerance; analogous benefits are claimed for **Na** and **Zn**. The PNAS abstract emphasizes that prior artificial layers, electrolytes, additives, and scaffolds still leave **inhomogeneous nucleation** and **unstable SEI** especially under **high current** or **low temperature**; the BSF strategy is presented as a **molecular** handle on the **interface** within **conventional carbonate** electrolytes rather than an exotic solvent system.

## Methods

The study is **experiment-led** on **BSF-grafted reduced graphene oxide (rGO) aerogel** anode hosts with unmodified rGO and other organic controls. **N/A** — the main text does not report **production ReaxFF** or long **reactive MD** of the full cell; the supporting computation is **static DFT** on interfacial **Li** binding. **N/A** — a single end-to-end **MD application** table (one engine, timestep, and production run length for a full reactive anode cell) is not the focus of the article.

**Experiments (electrochemistry and characterization).** **Li**, **Na**, and **Zn** cells use **conventional carbonate** electrolytes (e.g. **1 M LiPF\(_6\)** in **EC/EMC** for Li, with **Na**/**Zn** details in the **article** and **SI**). The paper reports high-rate **Li** plating at **6.0 mA cm\(^{-2}\)**, and in the **Results** and **abstract** a **6.0 mAh cm\(^{-2}\)** areal capacity with **Coulombic efficiency** metrics; **Li||LiCoO\(_2\)** and related full cells are cycled for many hundreds of cycles, including **−10 °C** operation compared to room-temperature baselines. **SEM**, **cryo/HR-TEM**, **XPS**, and **EIS** tie deposit morphology to **SEI** chemistry (full protocols in the **PNAS** text and **SI**).

**3 — Static QM / DFT.** DFT screening compares **Li** binding on **rGO** functionalized with the **BSF**-derived **benzenesulfonate** and other conjugated candidates versus **bare** graphene (Fig. 2; extended structures in **SI**). The manuscript reports **Li** binding energies of **−3.79 eV** (sulfonate-related model) and **−1.84 eV** (bare graphene), and nucleation overpotentials of **~20 mV** on **BSF-rGO** versus **~72 mV** on bare rGO at **6.0 mA cm\(^{-2}\)**.

**2 — Force-field training** — **N/A** (not a **ReaxFF** parameterization study).

## Findings

- **Outcomes and mechanism.** The BSF-grafted **interface** is argued to decompose during plating into **benzenesulfonate**-bearing motifs that act as **lithiophilic** nucleation sites, while **fluoride**-containing fragments enrich **LiF** in the **SEI**; these effects together steer more homogeneous **Li** deposition than on unmodified rGO **hosts**.

- **Comparisons (experiment and DFT).** Versus **bare** rGO, the work reports a lower **nucleation** overpotential on BSF-rGO (~20 mV vs ~72 mV at **6.0 mA cm\(^{-2}\)**; Fig. 2) and, in DFT, stronger **Li** adsorption on the **sulfonate**-functionalized model (−3.79 eV vs −1.84 eV for **bare** **graphene**). The PNAS text also compares the approach to prior **artificial** interlayers and **additives** that still perform poorly under **high** current and **low** **temperature** (see Introduction).

- **Cycling and metrics.** The abstract reports 99.2% **Coulombic** efficiency at **6.0 mAh cm\(^{-2}\)** and 6.0 mA cm\(^{-2}\). The manuscript also gives ~85.3% **capacity** retention after 400 **cycles** for a **Li||LiCoO\(_2\)** cell in one place and ~83.6% over 400 **cycles** for a **Li|LCO** cell in 1 M **LiPF\(_6\)** **EC/EMC** in another; the **figure** **captions** in the **PDF** disambiguate which **experiment** each number refers to. **Low-temperature** (−10 °C) **Li||LCO** cycling is reported without **extra** fade **versus** room-**temperature** **comparison** runs; **Na** and **Zn** demonstrations use the same molecular design idea.

- **Limitations and outlook (as authored).** The article does not resolve long **calendar**-life, **lean**-electrolyte, or manufacturing **challenges**; those remain open and are also noted in **## Limitations** here.

- **Corpus honesty.** This note tracks the **version-of-record** PNAS **PDF** at `pdf_path`; the paper has **no** ReaxFF trajectories, only the published **DFT** and **cell** **data**.

## Limitations

Long-term **calendar aging**, **lean electrolyte**, and **industrial scale-up** of aerogel electrodes are not fully de-risked within a single article.

## Relevance to group

**van Duin-group** coauthorship on **rational SEI design** via **surface-bound reactive molecules** for **metal anodes**.

## Citations and evidence anchors

- DOI: [10.1073/pnas.2001837117](https://doi.org/10.1073/pnas.2001837117)

## Related topics

- [[batteries-interfaces-reaxff]]
