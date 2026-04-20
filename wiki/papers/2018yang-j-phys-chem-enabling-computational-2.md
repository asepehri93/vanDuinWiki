---
id: paper:2018yang-j-phys-chem-enabling-computational-2
type: paper
title: "Enabling Computational Design of ZIFs Using ReaxFF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:zeolite-porous
  - method:reaxff
  - task:application
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.8b08094"
year: 2018
authors:
  - "Yongjian Yang"
  - "Yun Kyung Shin"
  - "Shichun Li"
  - "Thomas D. Bennett"
  - "Adri C. T. van Duin"
  - "John C. Mauro"
venue: "J. Phys. Chem. B"
pdf_sha256: "602cf1f2144e6c8bf9160f6a6fa1dafe01873ee7a2f6bdd5598975ea3b924bd7"
pdf_path: "papers/Yang_ZIF_JPC_B_2018_proof.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018yang-j-phys-chem-enabling-computational-2 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. B** article lays out a **ReaxFF-first modeling strategy** aimed at **computationally assisted design** of **zeolitic imidazolate frameworks (ZIFs)**, emphasizing **bond-making/breaking** events that matter during **processing**, **mechanical loading**, or **guest–framework** interactions that **fixed-bond** MOF-FFs may mishandle. **Coauthors** span **Penn State reactive simulation** (**Yang**, **Shin**, **van Duin**) and **glass / disordered framework** expertise (**Mauro**, **Bennett**), reflecting the paper’s **materials-informatics** angle on **ZIF** chemistry. The ingested file is an **ACS proof** PDF for the **JPCB** article.

## Methods

- **ReaxFF parameter sets** and **simulation protocols** for **ZIF**-relevant **metal–organic** bond topologies (see Methods for training scope).
- **Reactive MD** case studies supporting **design** claims in the publication.

## Findings

- Argues that **ReaxFF** unlocks **simulation modes** (explicit **reaction** and **failure**) needed for **practical ZIF design loops** beyond **elastic** lattice models.


## Limitations

- **MOF/ZIF** parameterization is **chemically specific**; **transfer** to new **linkers/metals** requires **re-fitting** or **validation**.
- **Proof PDF** pagination may differ slightly from the **final** issue page numbers.

## Relevance to group

Foundational **ZIF + Reaxff** methodology paper in the **group’s porous framework** portfolio.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcb.8b08094` (`papers/Yang_ZIF_JPC_B_2018_proof.pdf`).

## Related topics

- [[reaxff-family]]
