---
id: paper:2022clares-at-ah-at-at-tx-abs-2
type: paper
title: "Increasing density and mechanical performance of binder jetting processing through bimodal particle size distribution"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:alloy-bulk
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.18063/msam.v1i3.20"
year: 2022
authors:
  - "Ana Paula Clares"
  - "Yawei Gao"
  - "Ryan Stebbins"
  - "Adri C. T. van Duin"
  - "Guha Manogharan"
venue: "Mater. Sci. Addit. Manuf."
pdf_sha256: "50f737ca5a52bc6578caf4f0ebdba7ca277113c8155f4698ead558a015a46749"
pdf_path: "papers/Clares_Bimodal_Binder_Jetting_MSAM_2022_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022clares-at-ah-at-at-tx-abs-2 -->

## Summary

Binder jetting spreads powder without melting, avoiding fusion defects but often yielding lower green and sintered density than energy-beam powder-bed processes. Clares et al. investigate stainless steel 316L builds that mix coarse and fine powders to raise packing density and strength after sintering. Four unimodal feedstock groups and two bimodal mixtures are processed under comparable binder jetting and sintering conditions, with density and flexural strength reported relative to the best unimodal baseline. Reactive molecular dynamics interprets why bimodal packing strengthens interparticle contacts at necks. The introduction motivates binder jetting for tooling and biomedical markets where cost and throughput favor binder-based routes if density can be recovered through powder engineering.

## Methods

**1 — MD application (atomistic dynamics).** **ReaxFF** simulations in **LAMMPS**-class / **PuReMD**-style **workflows** (per *Mater. Sci. Addit. Manuf.*) build **sintering-like** **neck** **models** of **stainless 316L** to contrast **unimodal** and **bimodal** **packing-induced** **contact** **geometries**.
System size & composition: **SS316L** coarse/fine particle-contact configurations (bimodal vs unimodal); atom counts and exact box dimensions are **not stated in the indexed p1-2 extract**.
Ensemble: **not stated in the indexed p1-2 extract** (NVT/NPT selection should be taken from the full article/SI when available).
Duration / stages: MD trajectory lengths and equilibration/production staging are **not stated in the indexed p1-2 extract**.
Temperature: simulation setpoint(s) or schedule are **not stated in the indexed p1-2 extract**.
Pressure: **N/A in the indexed p1-2 extract** (no pressure-control protocol is reported in the extracted text).
Boundaries/periodicity, timestep, thermostat/barostat details, and ReaxFF electrostatics/QEq/cutoff settings are reported in the full article/SI.
The runs **rationalize** **trends** in **neighbour**-to-neighbour **bonding**; they are **not** a **time-resolved** **map** of **furnace**-scale **densification**. **N/A** — applied static **electric** field in the ReaxFF protocol; **N/A** — umbrella or metadynamics.

**2 — Force-field training.** **N/A**.

**3 — Static QM / DFT-only.** **N/A**.

**4 — Binder jetting, sinter, and tests.** **Layerwise** **binder** **deposition** on **four** **unimodal** and **two** **bimodal** **powder** **groups** at **fixed** **AM**+**furnace** **settings** apart from the **size** **distribution** (table in the **PDF**). **Sintering** in **inert** **atmosphere**; **sintered** **density** and **three-point** **flexure** with the **statistical** **treatment** summarized in the **abstract**. **Paired** wiki **`[[2022clares-at-ah-at-at-tx-abs]]`** (galley for a sibling **MSAM** **DOI**) is the same scientific work.

## Findings

**Outcomes and mechanisms.** The **abstract** reports about **+20%** sintered **density** and about **+170%** ultimate **flexure** **strength** for **bimodal** **packs** vs the **strongest** **unimodal** **control** in their comparison, with **in-manuscript** **statistical** **analysis** (re-verify **%**s from the **VOR** if citing numerically). The authors couple **higher** **sintered** **density** from **better** **packing** to **gains** in **strength**, and they use **ReaxFF** to argue that **fines** **filling** **pores** around **coarse** **grains** can **increase** **the** **number** of **strong** **neighbour**-to-neighbour **bridges** **relative** to unimodal beds **under** the same **furnace** **window**—a **mechanistic** **rationale** **(simulation)**, not a full **continuum** **kinetics** model.

**Comparisons and levers.** Bimodal vs unimodal at shared **furnace** **profile**; **lever** = **coarse**/**fine** **blend**; cite **n**-**replicates** and **CIs** from the **paper** when reusing the headline **%** **numbers**.

**Corpus / KB honesty.** Prefer **`[[2022clares-at-ah-at-at-tx-abs]]` only** when you need the **galley** **PDF**; this slug uses the **online-issue** **path**—see the **duplicate** **admonition** in **`## Limitations`** and the note below the **Relevance** **section**.
## Limitations

Duplicate PDFs for this article may exist under a galley sibling slug; cite the PDF you read for pagination. Industrial scatter in powder chemistry and binder absorption can shift absolute numbers.

## Relevance to group

Penn State additive-manufacturing collaboration with reactive MD interpretation of powder-bed contacts.

!!! note "Duplicate ingest"
    Paired with `paper:2022clares-at-ah-at-at-tx-abs` (galley PDF) for the same scientific article.

## Citations and evidence anchors

- DOI: [10.18063/msam.v1i3.20](https://doi.org/10.18063/msam.v1i3.20)

## Related topics

- [[reaxff-family]]
