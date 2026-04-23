---
id: paper:2017babu-venue-mergedfile
type: paper
title: "Electrocatalysis of Lithium Polysulfides: Current Collectors as Electrodes in Li/S Battery Configuration"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:sulfur-cathode
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/srep25194"
year: 2017
authors:
  - "Ganguli Babu"
  - "Khalid Ababtain"
  - "K. Y. Simon Ng"
  - "Leela Mohana Reddy Arava"
venue: "Sci. Rep."
pdf_sha256: "f1ffce93cab72c8275c68f92ca96af6bd0ed975f431e708c96d3d352206d8eb7"
pdf_path: "papers/Others/Reddy_Arava_papers/Nature Scientific Reports (2015).pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017babu-venue-mergedfile -->

## Summary

The study reports **non-aqueous Li/S cells** in which **Ni current collectors** are used not only as conductors but as **electrocatalytic surfaces** for **dissolved lithium polysulfides**, avoiding a **porous carbon matrix** and its binders/additives. **Galvanostatic** testing compares **planar 2D Ni** with **engineered 3D Ni** collectors. The authors report **~700 mAh g\(^{-1}\)** (vs sulfur) on **2D Ni** and **up to ~900 mAh g\(^{-1}\)** on **3D Ni**, with **capacity tracked over ~100 charge–discharge cycles** under their stated test conditions.

## Methods

This is an **experimental electrochemistry** study; there is **no atomistic MD, ReaxFF, or standalone QM** in the reported workflow.

**Li/S cells** use a **polysulfide catholyte** with **metal current collectors** that double as working electrodes. Besides **Ni**, the manuscript compares **Pt** and **Au** catalyst coatings (thin films, order **50 nm**) on **Al** and **stainless-steel** foils, with **Al** as a **non-catalytic** control. **2032-type coin cells** are assembled under **Ar** with **Li metal** anode, **catholyte** volume on the order of **10 mL**, and a **quartz** separator. **Galvanostatic** cycling is reported at **0.1 C** (normalized to **sulfur** in the cell) with monitoring over **tens to ~100** charge–discharge cycles in the main comparison figures.

A **parametric** survey varies **effective collector surface area**, **temperature**, **current rate**, and **polysulfide concentration** to tie kinetics to **discharge capacity** (mAh g\(^{-1}\) vs **sulfur**) and **polarization** of the charge–discharge plateaus. **CV, EIS, XRD of films, and supplementary figures** for extended cycling live in the **Scientific Reports** PDF and SI—not duplicated here.

## Findings

**Outcomes:** **Ni** collectors are argued to **accelerate polysulfide redox** vs **carbon-matrix** approaches, with **higher delivered capacity** on **3D** vs **2D Ni** under the reported tests. **Comparisons:** performance is tied explicitly to **collector architecture** and **kinetic parameters** in the **parametric** study. **Limitations (as framed):** the article motivates the approach against **porous-carbon processing** and **polysulfide shuttle** issues; **microscopy**, **EIS**, and **full electrolyte recipes** should be taken from the **figures** and **methods** in the **PDF** bundled under `pdf_path` (this corpus path may be a **merged** volume—see **Limitations**).

## Limitations

The repo **`pdf_path`** may be a **merged Scientific Reports** PDF; **pagination and DOI routing** should be checked against the **publisher PDF** for the article identified in front matter. This note does not reproduce **CV**, **EIS**, or **post-mortem** imaging from the primary text.

## Relevance to group

Experimental **Li–S** interfaces adjacent to computational **electrolyte/interphase** themes; **not** a ReaxFF paper.

## Citations and evidence anchors

- DOI: `10.1038/srep25194` (verify against PDF header).

## Related topics

- [[batteries-interfaces-reaxff]]
