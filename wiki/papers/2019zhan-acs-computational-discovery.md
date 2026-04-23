---
id: paper:2019zhan-acs-computational-discovery
type: paper
title: "Computational Discovery and Design of MXenes for Energy Applications: Status, Successes, and Opportunities"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:ml-atomistic
  - method:dft-static
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:dft-static
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.9b00439"
year: 2019
authors:
  - "Zhan, Cheng"
  - "Sun, Weiwei"
  - "Xie, Yu"
  - "Jiang, De-en"
  - "Kent, Paul R. C."
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "896d47c33edb1751393e520ed51e8909e947e0bb42615123d7375dd151efeb91"
pdf_path: "papers/Others/MXene_ACS_AMI_CompMat_review_Kent_Jiang_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019zhan-acs-computational-discovery -->

!!! abstract "Scope"

Review of computational work on MXenes (two-dimensional transition-metal carbides/nitrides/carbonitrides) for energy applications, emphasizing high-throughput and data-driven discovery alongside electronic-structure modeling.

## Summary

MXenes form a large and rapidly growing family of two-dimensional materials with metallic character and strong interest for energy storage, electrocatalysis, and related applications. The article surveys computational literature on designing and screening MXene compositions and surface terminations, summarizes progress on predicted intrinsic and tunable properties, and discusses how high-throughput workflows, large datasets, and machine-learning approaches can expand the searchable chemical space. Remaining challenges and research directions toward more predictive, experimentally aligned modeling are outlined. MXenes inherit **metallic** **conductivity** and **tunable** **terminations** from **MAX**-phase etching, so high-throughput **DFT** and **ML**-accelerated **screening** are a natural match for **battery**- and **electrocatalysis**-relevant **surface** **chemistry**. The review synthesizes **workflows** that scale over **compositions** and **functionalized** **surfaces**, and highlights gaps in **alignment** with **synthesis**-dependent **order**/**disorder**; see the **PDF** and **SI** for tables and **benchmark** figures.

## Methods

### Literature scope and comparison protocol (D)

The **Forum** **review** in **ACS Appl. Mater. Interfaces** is a **bibliography**-driven **survey** of **computational** work on **MXenes**; it is **not** a single new **benchmark** run with one **PBE** input deck. The authors **compare** how **DFT** **packages** and **k-point** **sampling** have been used across the **cited** **MXene** **space**, how **surface** **terminations** are **modeled**, and how **ML**-accelerated **screening** is paired with those **static** **QM** **trends**. The **organizing** **sections**—**synthesis/etching** **context**, **terminations**, **stability** and **compositional** **trends**, **batteries**-related **ion** **and** **capacitance** **modeling**, **electrocatalysis** **illustrations**, and **data-driven** **search** over **chemical** **configurations**—are summarized at the **level** of the **published** **outline**; for **lattice** **parameters**, **band** **gaps**, or **barriers**, pull the **cited** **per-MXene** **papers**. The **next** **paragraphs** in the **review** text give **concrete** **PBE**/**GGA**/**HSE**-style **juxtapositions** in **selected** **citations**; the present **wiki** does **not** re-tabulate every **VASP**/**WIEN2k** **input**. **N/A** — a **unified** **NEB** or **rMD** **protocol** across the **entire** **compendium**: **the** **review** is **synthetic**, not a **repro** **package**.

## Findings

Computational work has substantially broadened the range of explored MXene chemistries and highlighted termination chemistry as a central degree of freedom distinct from many other two-dimensional families. Modeling has produced extensive predictions for stability, basic electronic features, and application-motivated trends, while also motivating integrated high-throughput and learning-based search over large configuration spaces. The review frames open needs around **quantitative** **agreement** with **experiment**, **transferability** across **chemistries**, and tighter **coupling** between **synthesis** **pathways**, **surface** **chemistry**, and **property** **models**. At a **synthesis** level, it maps which **DFT**/**k-T**/**ML** layers dominate which **stability**/**intercalation**/**catalysis** **questions**, where **benchmarks** **diverge**, and which **validation** gaps the authors **stress**—**without** inventing new **barriers** or **rates** beyond the **bibliography**. **Sensitivity** (e.g. to **composition**, **termination**, **defects**) is discussed through **cited** **trend** **studies**, not one unified **parameter** **sweep**. **Limitations** and **outlook** reflect **the review’s** **Discussion**: **sampling** in **chemical** **space** outpaces **experimental** **characterization** of real **terminations** and **disorder**. **Corpus honesty:** treat this page as a **bibliography-backed** **map**; any **number** in automation must point to a **cited** **primary** `paper:`.


## Limitations

As a review, numerical results are reported only through citation of the underlying primary studies; the present page summarizes the review’s scope and claims at the level of the article abstract and section outline.

## Relevance to group

Provides corpus context for two-dimensional and energy-storage adjacent modeling; complements reactive atomistic studies on related layered systems elsewhere in the knowledge base.

## Citations and evidence anchors

- https://doi.org/10.1021/acsami.9b00439

## Related topics

- [[reaxff-family]]
