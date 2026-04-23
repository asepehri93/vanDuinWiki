---
id: paper:2024small-small-2024-2-watching-de
type: paper
title: "Watching (De)Intercalation of 2D Metals in Epitaxial Graphene: Insight into the Role of Defects (Small 11/2024)"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:graphene-carbon
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1002/smll.202470092"
year: 2024
authors:
  - "Falk Niefind"
  - "Qian Mao"
  - "Nadire Nayir"
  - "Malgorzata Kowalik"
  - "Jung-Joon Ahn"
  - "Andrew J. Winchester"
  - "Chengye Dong"
  - "Rinu A. Maniyara"
  - "Joshua A. Robinson"
  - "Adri C. T. van Duin"
  - "Sujitra Pookpanratana"
venue: "Small"
pdf_sha256: "da03f46c5d840d1a9c1413269be2af9d1559ecf2eea0d36c86a8060945055118"
pdf_path: "papers/Small - 2024 - Niefind - Watching  De Intercalation of 2D Metals in Epitaxial Graphene  Insight into the Role of Defects .pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2024small-small-2024-2-watching-de -->

!!! abstract "Scope"
    **Epitaxial graphene** on SiC is used as a platform to study **(de)intercalation of two-dimensional metals**, with emphasis on how **defects** influence the process (journal issue **Small** 20(11), article **2470092**).

## Summary

This ingest tracks DOI [10.1002/smll.202470092](https://doi.org/10.1002/smll.202470092) (*Small* **20**(11), article **2470092**) and the corpus PDF named in **`pdf_path`**. The closely related version-of-record narrative with fuller extraction support is curated at [[2024niefind-small-2024-2-watching-de]] (DOI [10.1002/smll.202306554](https://doi.org/10.1002/smll.202306554)); bibliographic packaging can differ by issue/article number even when the scientific content matches. Following the primary article’s description, Niefind and colleagues combine **photoemission electron microscopy (PEEM)** with **atomic force microscopy (AFM)**, **SEM-EDX**, **XPS**, **ReaxFF molecular dynamics**, and **DFT** to compare **defect-gated (de)intercalation** of **two-dimensional Ag and Ga** sandwiched between **bilayer epitaxial graphene (EG)** and **SiC**. **PEEM** tracks **Ag-rich** features during **in situ annealing** (e.g. toward **436 K** in the discussed traces), while microscopy and spectroscopy tie **Ag** redistribution to **3D particles** atop graphene with representative **AFM heights** near **15.2 nm ± 2.1 nm** and steep sidewalls in the analyzed regions.

## Methods

**Samples and intercalation context.** **2D metals** are prepared at the **EG/SiC** interface using **confinement heteroepitaxy (CHet)**-style processing in which **oxygen plasma** generates **graphene defects** that act as **entry paths** for metal intercalation under elevated **temperature/pressure** conditions summarized in the article introduction.

**PEEM and complementary microscopy.** **In situ PEEM** follows **intensity changes** associated with **Ag** redistribution during **annealing cycles** up to about **575 K** (with detailed ROI traces discussed around **405–494 K**). **AFM** documents **3D Ag particles** atop graphene; **SEM-EDX** and **laterally integrated XPS** support **Ag** surface enrichment after annealing. Multiple **regions of interest** are used to argue for **zero-order-like** kinetics where **intercalation speed** depends weakly on **Ag structure size**, interpreted as **rate limitation by window/defect pathways**.

**Atomistic modeling.** **ReaxFF MD** explores **de-intercalation pathways** for **Ag** and **Ga** at the **EG/SiC** stack, including differences in **reversibility**, **interlayer accumulation** (especially **Ga**), and **defect healing**; **DFT** supports **relative binding** trends for **Ga versus Ag** on **graphene**. If any numerical setting in your local PDF disagrees with [[2024niefind-small-2024-2-watching-de]], treat the PDF you are holding as authoritative for that copy.

The checked-in extract **`normalized/extracts/2024small-small-2024-2-watching-de_p1-2.txt`** is **masthead-only**; full instrument and simulation tables require the PDF or the sibling page above.

**Corpus mapping.** **1 — MD (ReaxFF) / 2 — DFT:** **N/A** to restate **timestep**, **ensemble**, and **QM** settings on *this* stub—use **[[2024niefind-small-2024-2-watching-de]]** or the **PDF** you have locally. **3 — PEEM/AFM** — experimental **T**/**ROI** context is summarized above from the **shared** article narrative.

## Findings

**Ag** exhibits **semi-reversible** **de- and re-intercalation** mediated by **persistent graphene defects/windows** after CHet-like processing; imaging relates **window geometry** (including **multiple windows** in some ROI) to **intercalation rate** and estimates an **intercalation front speed** near **0.5 nm s⁻¹** (±**0.2 nm s⁻¹**) from combined **PEEM/AFM** analysis in the primary article. **Ga** **de-intercalates irreversibly** under the explored thermal protocol, with **faster kinetics** and **non-circular** window shapes; **MD** connects **Ga pile-up** between graphene sheets before egress to stronger **metal–graphene** interactions and **Ga** thermophysical behavior emphasized in the text (including a low bulk melting point). Together, the experimental and modeling threads argue that **defect-mediated gating** and **metal-specific graphene healing** **co-determine** intercalation kinetics.

## Limitations

**In-repo** extract is **masthead-only** unless the PDF is read manually. **PEEM** projection and **ReaxFF** energetics carry usual model limitations.

## Relevance to group

**Adri C. T. van Duin** is a co-author; the topic aligns with **2D materials / graphene** work in the broader corpus.

## Citations and evidence anchors

- DOI: [10.1002/smll.202470092](https://doi.org/10.1002/smll.202470092)

## Related topics

- [[graphene-nanocarbon]]
