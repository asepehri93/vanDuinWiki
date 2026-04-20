---
id: paper:2015islam-physical-che-interactions-hydrogen
type: paper
title: "Interactions of hydrogen with the iron and iron carbide interfaces: a ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - method:monte-carlo
  - task:application
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1039/C5CP06108C"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Chenyu Zou"
  - "Adri C. T. van Duin"
  - "Sumathy Raman"
venue: "Physical Chemistry Chemical Physics 2016, 18, 761–771"
pdf_sha256: "916b398c5c01518367cdc80093961e6de634edbff50304efec4645548ae86b1e"
pdf_path: "papers/Islam_FeC_PCCP_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015islam-physical-che-interactions-hydrogen -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Islam *et al.* study **hydrogen embrittlement (HE)** phenomena in **α-iron**, **cementite (Fe\(_3\)C)**, and **ferrite–cementite** interfaces using a **merged ReaxFF Fe/C/H** description: they combine an **Fe/C/H** parameterization originally aimed at **Fischer–Tropsch** surface chemistry with updated **carbon parameters** from a specified Srinivasan–van Duin–Ganesh **J. Phys. Chem. A** line, refitting **Fe/C** interactions on the same training manifold. Simulations include **hydrogen diffusion** in ferrite and cementite, **hydrogen-induced decohesion** metrics (work of separation vs hydrogen content at the interface), **MD**-observed **hydrogen accumulation** at interfaces, and **grand canonical Monte Carlo (GCMC)**-style exploration of **nanovoid** growth in α-iron framed in the extract as part of the mechanistic portfolio.

## Methods

- **ReaxFF MD** for hydrogen in **Fe** and **Fe\(_3\)C** phases and at **interfaces** with defects (vacancy cluster scenario referenced).
- **GCMC**-related protocol mentioned for nanovoid studies (see paper body for ensemble details).

## Findings

- **Diffusion coefficients** for hydrogen in ferrite and cementite phases are reported in the abstract framing as supporting subsequent interface decohesion analysis.
- **Work of separation** decreases with increasing hydrogen concentration at the **ferrite–cementite** interface, interpreted as **hydrogen-assisted decohesion** behavior consistent with experimental expectations cited in the introduction.


## Limitations

- HE mechanisms (**HELP vs HEDE**, trap distributions) remain debated; this paper contributes **atomistic** evidence for a subset of hypotheses.
- Corpus slug uses **2015** while the downloaded PDF header shows **2016** publication metadata; cite by **DOI**.

## Relevance to group

**Adri C. T. van Duin** co-authorship; extends **ReaxFF** to **steel-relevant Fe/C/H** interfaces with direct ties to **hydrogen damage** problems in infrastructure and refining.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1039/C5CP06108C](https://doi.org/10.1039/C5CP06108C)

## Related topics

- [[reaxff-family]]
