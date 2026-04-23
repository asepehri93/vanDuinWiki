---
id: paper:2023lin-x-paper
type: paper
title: "Recent Advances in 2D Material Theory, Synthesis, Properties, and Applications"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:methods-software
  - task:application
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.2c12759"
year: 2023
authors:
  - "Yu-Chuan Lin"
  - "Riccardo Torsi"
  - "Rehan Younas"
  - "Christopher L. Hinkle"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Joshua A. Robinson"
venue: "ACS Nano (manuscript proof in corpus)"
pdf_sha256: "4223e3ebe1d2b2117623534842d6a67cb645c3f1db734e53c22bc3d1d088f310"
pdf_path: "papers/Lin_Nadire_ACS_Nano_2D_synthesis_review_2023_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023lin-x-paper -->

## Evidence and attribution

!!! note "Alternate proof PDF"

    This slug stores `papers/Lin_Nadire_ACS_Nano_2D_synthesis_review_2023_proof.pdf`. The related ingest **`[[20230000-0003-4958-5073-x-manuscript]]`** points at `papers/Lin_Nayir_Robinson_ACS_Nano_2D_2023_review_galley.pdf`. Both are **proof** variants of the same **ACS Nano** review (DOI [10.1021/acsnano.2c12759](https://doi.org/10.1021/acsnano.2c12759)).

## Summary

ACS Nano review (2023) surveying theory, synthesis, characterization, devices, and quantum physics of two-dimensional materials and heterostructures. The abstract highlights modeling of defects and intercalants; machine learning for synthesis and sensing; growth of MXenes, magnetic layers, epitaxial films, and low-symmetry crystals; oxidation and strain-gradient engineering; optical and phonon properties tied to inhomogeneity; biosensing with ML analytics; mix-dimensional heterostructures; magnetic topological insulators for quantum anomalous Hall devices; and twisted homojunctions with emerging quantum transport. Penn State contributors include Nadire Nayir and Adri C. T. van Duin among a large consortium led by Joshua A. Robinson.

As a **roadmap** article, it is best used to **locate** **primary** studies: each **subsection** points to **specialist** literature for **quantitative** **growth** kinetics, **defect** **spectroscopy**, or **device** **metrics** rather than supplying a unified computational protocol.

## Methods

### Review genre (D)

**Thematic** **ACS Nano** survey with **bibliographic** pointers—no single **DFT/MD** protocol.

### How to trace technical content

Follow **internal citations** for **DFT**, **MLIPs**, **growth** tools, and **transport** measurements.

### Proof-PDF caveat

Two proof paths exist for the same **DOI**—confirm **figure** labels against **VOR** before quoting panels.

### 4 — Reviews, perspectives, non-simulation (primary genre)

**N/A** for a **single** **MD**/**DFT** **case**—this **ACS Nano** **roadmap** aggregates many **subfields**; **any** **timestep**, **k**-mesh, or **slab** **size** must come from the **cited** **primary** work, not this **review** page. **FF training** and **static** **QM** **protocols** likewise **N/A** as **one** table here.

## Findings

### Scope (abstract roadmap)

Covers **defect/intercalant** modeling, **ML** for **synthesis/sensing**, **growth** case studies, **strain/oxidation** engineering, **optical/phonon** inhomogeneity, **biosensing**, **mixed-dimensional** devices, **magnetic TIs**, **twisted** homojunctions—details and **numbers** only in **primary** references.

### Authorship note

**Penn State** coauthors link the review to local **2D** infrastructure; each **quantitative** claim still requires the **cited** **primary** paper.

**Corpus** **honesty:** this **page** is a **thematic** **index**; **ReaxFF**-based **reaction** **kinetics** on **2D** **oxides** or **twisted** **homojunctions** must be **traced** to the **cited** **MD** **paper** with its own **NVT**/**NPT** **and** **temperature** **sensitivity** **analysis**—**not** inferred from the **roadmap** **prose** alone. **Outlook** **sections** in the **review** list **open** **challenges** in **synthesis** **and** **defect** **control**; **compared** to that **laboratory** **outlook**, **ab initio** and **MLIP** **benchmarks** remain **sparse** for some **exotic** **2D** **alloys**—a **limitation** the **review** flags **explicitly** when a **table** is **not** available.

## Limitations

Proof PDF may differ slightly from the final issue layout; confidential watermarks may appear depending on download channel.

## Corpus notes

Deduplicate this entry against **`[[20230000-0003-4958-5073-x-manuscript]]`** in retrieval indexes so agents do not double-count identical DOI content under two `paper_id` stems.

When updating author lists, prefer the published ACS Nano author roster over filename-derived placeholders such as “et al.” in legacy manifests, because multi-hundred-author reviews change between proof and issue.

Retrieval systems should index this DOI once while aliasing both `paper_id` stems so chunk deduplication logic can merge embeddings if desired without losing manifest traceability.

MkDocs exports should surface the DOI prominently in page metadata when this note is published publicly, because the review is a common entry point for newcomers.

## Relevance to group

Documents collaboration network linking **2DCC-MIP** participants to a flagship review article.

## Citations and evidence anchors

- DOI: [10.1021/acsnano.2c12759](https://doi.org/10.1021/acsnano.2c12759)

## Related topics

- [[20230000-0003-4958-5073-x-manuscript]]
- [[reaxff-family]]
