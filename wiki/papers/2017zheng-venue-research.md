---
id: paper:2017zheng-venue-research
type: paper
title: "Modeling and in situ probing of surface reactions in atomic layer deposition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - task:application
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b01618"
year: 2017
authors:
  - "Yuanxia Zheng"
  - "Sungwook Hong"
  - "George Psofogiannakis"
  - "G. Bruce Rayner, Jr."
  - "Suman Datta"
  - "Adri C. T. van Duin"
  - "Roman Engel-Herbert"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "5de920e9d6f7025391f4d2fc7d063bd4a0ae4aaeb06f858b969e2229cece7f3f"
pdf_path: "papers/Zheng_Hong_ACS_AMI_ALD_2017_ASAP.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017zheng-venue-research -->

## Summary

Atomic layer deposition of high-κ dielectrics on germanium requires controlling interfacial oxidation, precursor reaction pathways, and defect generation during early cycles. Zheng et al. combine ReaxFF reactive molecular dynamics of trimethylaluminum and water chemistry on hydrogen-terminated versus oxidized Ge(100) with in situ spectroscopic ellipsometry during deposition, supplemented by atomic force microscopy, X-ray photoelectron spectroscopy, and impedance spectroscopy. The joint workflow targets nucleation delays, intermixing at the interface, and electrical consequences of the evolving oxide stack. The study is positioned as a coupled modeling and metrology platform: simulations propose atomistic reaction sequences while ellipsometry tracks film thickness and optical constants during the same chemistries.

## Methods

**Molecular dynamics (reactive).** **ReaxFF molecular dynamics** mirrors the **`[[2017yuanxia-zheng-acs-am7b01618]]`** setup: early **TMA/H₂O** **ALD** cycles on **H-terminated** versus **oxidized Ge(100)** **slabs** with **periodic** **supercells**, explicit **atom** counts, **timestep** (fs), **thermostat**/**barostat** controls, **NVT**/**NPT** staging, **temperature** (**K**) setpoints, and **equilibration**/**production** **duration** (ps/ns) as tabulated in the **ACS AMI** article—confirm any ASAP-specific figure labels in **`papers/Zheng_Hong_ACS_AMI_ALD_2017_ASAP.pdf`**. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in this summary.

**Experiments.** Same **in situ ellipsometry**, **AFM**, **XPS**, and **impedance** workflow as the canonical page, enabling **experimental** validation of **interfacial oxidation** and **nucleation** transients.

**Force-field fitting.** **N/A —** consumes the published **Al/Ge/O/H ReaxFF** description referenced in the article.

**Static QM / DFT.** **N/A —** reactive **MD** plus metrology, not on-the-fly **DFT** **AIMD**.

**Review scope.** **N/A —** duplicate **ASAP**/**preprint-style** **PDF** ingest; scientific locators should prefer **`[[2017yuanxia-zheng-acs-am7b01618]]`** when possible.

## Findings

**Outcomes and mechanisms.** **Simulations** reproduce delayed **nucleation** on **H–Ge(100)** and a **self-cleaning** response on **oxidized** templates that builds an **Al₂O₃/GeO_x** **intermixed** layer, **limiting oxygen diffusion** into **Ge** while still enabling early **dielectric** network formation.

**Comparisons.** **Ellipsometry**, **AFM**, **XPS**, and **impedance** **experiments** align with the modeled **interface** evolution, linking **optical thickness** transients to **ligand** chemistry and **suboxide** **interdiffusion**.

**Sensitivity / design levers.** **Surface preparation** (**hydrogen-terminated** vs **oxidized**) is the dominant lever controlling **nucleation delay** versus **self-cleaning** acceleration.

**Limitations / outlook.** **ASAP** pagination can differ from the issue **PDF**; extending the workflow to other **ALD** chemistries requires revisiting both **force-field** coverage and **optical** stack models.

**Corpus honesty.** Treat this slug as a **duplicate PDF** path for **`10.1021/acsami.7b01618`**; cite **`[[2017yuanxia-zheng-acs-am7b01618]]`** for stable **version-of-record** pointers when available.
## Limitations

ASAP PDF variant in corpus may differ in pagination from the final issue PDF; quantitative agreement depends on ellipsometric modeling assumptions and classical force-field limits.

## Relevance to group

Van Duin coauthored ReaxFF integration with optical diagnostics for gate-stack–relevant ALD.

## Reader notes (navigation)

Siblings: [[2017yuanxia-zheng-acs-am7b01618]], [[2017zheng-venue-research-2]].

## Citations and evidence anchors

- DOI: `10.1021/acsami.7b01618`.

## Related topics

- [[reaxff-family]]
