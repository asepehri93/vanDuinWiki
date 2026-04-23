---
id: paper:2023tsai-venue-paper
type: paper
title: "Supporting Information: Effect of electrode/electrolyte coupling on birnessite (δ-MnO2) mechanical response and degradation"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:batteries-electrochemistry
  - task:experiment-integrated
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:validation-experiment
candidate_tags:
  - "AFM-multivariate-conductivity"
source_refs: []
doi: ""
year: 2023
authors:
  - "Wan-Yu Tsai"
  - "Shelby B. Pillai"
  - "Karthik Ganeshan"
  - "Saeed Saeed"
  - "Yawei Gao"
  - "Adri C. T. van Duin"
  - "Veronica Augustyn"
  - "Nina Balke"
venue: "ACS Appl. Mater. Interfaces (Supporting Information; primary article text not in this corpus PDF)"
pdf_sha256: "0a5175db788d3587357eb18f5fc9a0344cd3b0826c2982fb20859b9cd7c44c89"
pdf_path: "papers/Tsai_Ganeshan_Gao_ACS_AMI_2023_Birnessite_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023tsai-venue-paper -->

!!! note "Corpus note"
    The checked-in PDF is **Supporting Information** for an ACS *Applied Materials & Interfaces* study on birnessite (δ-MnO₂). The main article PDF is **not** represented as a separate primary file in this slice; methods and findings below are limited to what the SI extract documents.

## Summary

This entry documents **Supporting Information** for work on **electrode/electrolyte coupling**, **mechanical response**, and **degradation** of **birnessite (δ-MnO₂)** in a sulfate electrolyte context, with Penn State co-authorship including **Adri C. T. van Duin**. The SI package is treated here as **ancillary** to the parent *ACS Applied Materials & Interfaces* article: it supplies **figure-level** workflows for **scanning-probe** data processing rather than standalone conclusions about **capacitance** or **long-term** electrochemical cycling, which require the **main text** and **full figure set**.

## Methods

### Corpus role (SI-focused ingest)

Supports **`[[20230000-0002-4731-7051-x-effect-electrolyte]]`** (**birnessite** **AFM**/mechanics story) with **Supporting Information** analysis detail.

### mCV / k-means workflow (data processing)

**Figure S1**: **topography** + **k-means** (**3** clusters) on **topography** and **mCV** maps; **subtracted k-means** map; **height** extraction with **thermal drift** correction; **pixel** masks along **x/y**.

**N/A (LAMMPS, ReaxFF, NPT, E-field, metadynamics).** This **SI** supports **SPM** **data** **processing** (k-means on topography and mCV), not an atomistic **RMD** or static **DFT** study—**N/A** for **thermostat** time constants, **PBC** cell sizes, or **E-field** **RMD** on this page. The front matter has **no** `doi` because the **parent** *ACS Appl. Mater. Interfaces* article is not yet the canonical cite for this work—ingest the **VOR** parent to anchor `doi` and full **Methods**/**Findings**.

## Findings

The SI figure caption states that **k-means segmentation** separates regions in both **topographic** and **mCV** channels and that **subtracting** cluster maps highlights coupled structure–activity contrasts; **non-zero pixel counts** versus spatial offset quantify how sensitive the extracted mCV features are to alignment. Together, these processing steps are presented as a way to **co-register** mechanical and **conductivity** maps when **thermal drift** and **line-by-line** scanning artifacts complicate simple height–current overlays. Full quantitative conclusions about electrochemical degradation require the **main article** text and figures, which are not in the current extract.

## Limitations

Only the **first pages of Supporting Information** are captured in extracts bundled for this slug; **no DOI** is recorded in the normalized bibliography stub, and **primary-article** PDF text is not in the corpus slice used here. Operators should treat this page as a **navigation** record for **SI-specific** workflows until the **parent** article PDF is ingested alongside a complete **bibliography** update. External citations of **scientific** claims should use the **journal** **version-of-record** for **birnessite** **electrochemistry**, not this SI fragment alone.

## Relevance to group

Co-authorship links the work to **interfacial electrochemistry** and **multimodal scanning-probe** characterization relevant to **energy materials** workflows in the broader collaboration.

## Citations and evidence anchors

Prefer the **version-of-record** DOI for the parent article when citing scientific claims; use this page for **SI-specific** procedural notes only.

## Related topics

- [[batteries-interfaces-reaxff]]
