---
id: paper:2018tao-liang-j-phys-chem-applied-potentials
type: paper
title: "Applied Potentials in Variable-Charge Reactive Force Fields for Electrochemical Systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:catalysis-surfaces
  - domain:methods-software
  - method:reactive-md-generic
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.7b06064"
year: 2018
authors:
  - "Tao Liang"
  - "Andrew C. Antony"
  - "Sneha A. Akhade"
  - "Michael J. Janik"
  - "Susan B. Sinnott"
venue: "J. Phys. Chem. A"
pdf_sha256: "569e2b7af7a89199373ea7a177827802b6180d0013ee77060800d1a692dcdbec"
pdf_path: "papers/Others/2018_Liang_JPCA.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2018tao-liang-j-phys-chem-applied-potentials -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. A** article uses **molecular dynamics** with the **third-generation charge-optimized many-body (COMB3)** potential—a **variable-charge**, **reactive** framework distinct from **ReaxFF**—to treat **Cu electrode / aqueous electrolyte** cells with tunable **OH⁻** and **H⁺** concentrations. **Applied electrochemical bias** is represented by an **electronegativity offset** on **metal** atoms, embedded in COMB3’s **charge equilibration** scheme; the authors compare this **offset** approach with **QEq-style** equilibration and propose a **charge-neutral electrolyte** protocol suited to **electrochemical** boundary conditions. The paper is **Penn State**–authored (**Liang**, **Sinnott**, **Janik**, **Akhade**, **Antony**) and is a **methods** reference for **biased metal–water interfaces** adjacent to **ReaxFF / eReaxFF** electrochemistry workflows.

## Methods

- **COMB3 MD** of **two Cu electrodes** flanking **water** with **acid/base** loading as specified in the article.
- Analysis of **electronegativity offset** vs **standard charge equilibration** in **variable-charge** simulations under **applied-potential** targeting.

## Findings

- The **electronegativity-offset** route is integrated with COMB3’s **variable charge** treatment and used to explore **interfacial water dynamics** and **electrochemical** response trends in the model cells.
- A **modified equilibration** strategy is proposed so that **external potentials** act via **electrode electronegativity shifts** while keeping the **electrolyte** charge-neutral, with **qualitative** agreement on **voltages** after **precalibration** (as stated in the abstract).


## Limitations

- Results are tied to the **COMB3** parameterization and **Cu/water** chemistry; **transfer** to other **metals**, **electrolytes**, or **ReaxFF** implementations is **not automatic**.
- **Classical** treatment of **electrochemical** interfaces omits **explicit electron transfer** chemistry at full **ab initio** fidelity.

## Relevance to group

**Conceptual overlap** with how **variable-charge reactive** models implement **electrode bias**—useful when comparing **COMB3** and **ReaxFF / eReaxFF** routes for **electrified interfaces**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.7b06064` (`papers/Others/2018_Liang_JPCA.pdf`).

## Related topics

- [[reaxff-family]]
