---
id: paper:2018yang-j-phys-chem-prediction-glass
type: paper
title: "Prediction of the Glass Transition Temperatures of Zeolitic Imidazolate Glasses through Topological Constraint Theory"
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
doi: "10.1021/acs.jpclett.8b03348"
year: 2018
authors:
  - "Yongjian Yang"
  - "Collin J. Wilkinson"
  - "Kuo-Hao Lee"
  - "Karan Doss"
  - "Thomas D. Bennett"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "John C. Mauro"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "8b60ae242d6f9839444651f5816696194c3b0bdf2f21399ff9eccacae714ca01"
pdf_path: "papers/Yang_ZIF_JPCL_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018yang-j-phys-chem-prediction-glass -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

For **agZIF-62** glasses of composition **Zn(Im₂₋ₓbImₓ)**, the work builds a **topological constraint model** for **glass transition temperature (Tg)** that combines **experimental** data with **ReaxFF molecular dynamics** to define a **hierarchy of bond constraints**. The model reproduces **Tg** versus **benzimidazolate** content with reported **~3.5 K** error and is extended to **5-methylbenzimidazolate**, yielding a **ternary Tg diagram** for a **hypothetical** three-ligand framework. **Yang**, **Shin**, and **van Duin** anchor the **reactive MD** contribution; **Mauro** and collaborators provide the **constraint-theory** framework for **MOF glasses**.

## Methods

- **ReaxFF MD** to inform **constraint** assignments and **network** rigidity inputs used in **topological constraint theory (TCT)**.
- **TCT** construction and extension to **multicomponent** ligand mixtures (see **J. Phys. Chem. Lett.** for equations and fitting).

## Findings

- **Tg** scaling with **benzimidazolate** concentration is captured with **small** error versus the **experimental** reference used in the letter.
- **Ternary Tg** predictions illustrate how **constraint theory** plus **ReaxFF** can probe **unsynthesized ZIF glass** formulations.

## Limitations

- **TCT** assumes a **coarse** decomposition of **rigidity**; **local** chemical detail may require **full MD** cooling curves for **borderline** compositions.
- **ReaxFF** must be **trusted** for each **ligand chemistry** before **constraint** parameters are exported to **theory**.

## Relevance to group

Links **Penn State ReaxFF** on **ZIF** **glasses** to **Mauro-group** **topological constraint** methods for **Tg** design.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpclett.8b03348` (`papers/Yang_ZIF_JPCL_2018.pdf`).

## Related topics

- [[reaxff-family]]
