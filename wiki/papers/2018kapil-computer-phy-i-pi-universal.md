---
id: paper:2018kapil-computer-phy-i-pi-universal
type: paper
title: "i-PI 2.0: A universal force engine for advanced molecular simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:enhanced-sampling
  - method:pimd
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cpc.2018.09.020"
year: 2019
authors:
  - "Venkat Kapil"
  - "Mariana Rossi"
  - "Ondrej Marsalek"
  - "Riccardo Petraglia"
  - "Yair Litman"
  - "Thomas Spura"
  - "Bingqing Cheng"
  - "Alice Cuzzocrea"
  - "Robert H. Meißner"
  - "David M. Wilkins"
  - "Benjamin A. Helfrecht"
  - "Przemysław Juda"
  - "Sébastien P. Bienvenue"
  - "Wei Fang"
  - "Jan Kessler"
  - "Igor Poltavsky"
  - "Steven Vandenbrande"
  - "Jelle Wieme"
  - "Clemence Corminboeuf"
  - "Thomas D. Kühne"
  - "David E. Manolopoulos"
  - "Thomas E. Markland"
  - "Jeremy O. Richardson"
  - "Alexandre Tkatchenko"
  - "Gareth A. Tribello"
  - "Veronique Van Speybroeck"
  - "Michele Ceriotti"
venue: "Comput. Phys. Commun."
pdf_sha256: "413940892ee3e27869b7546f945d41ed61c160bf0321e0a0c3aa93eb441e8d2b"
pdf_path: "papers/Others/Kapil_PIMD_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018kapil-computer-phy-i-pi-universal -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**i-PI 2.0** is presented as a **modular, Python-driven client** that drives **ab initio** and **empirical** “**forces engines**” (external codes such as **DFT packages** or **MD engines**) to implement **path-integral MD**, **advanced thermostats**, **ring-polymer contraction schemes**, and other **enhanced sampling / nuclear quantum** workflows. The article is a **methods/software** contribution to the **molecular simulation ecosystem**, not a **ReaxFF parameterization** paper; it is included in the corpus as a **general tooling** reference. **Note:** the repository `paper_id` slug uses **2018** while the **journal volume (236, 2019)** reflects **publication timing**—frontmatter **`year`** follows the **bibliographic** year in the normalized record’s venue string.

## Methods

- Software architecture description: **client–server** coupling, **communicators**, and **example workflows** (see article sections).

## Findings

- Documents **capabilities new to i-PI 2.0** relative to earlier releases and provides **usage patterns** for **PIMD** and related **advanced sampling**.

## Limitations

- Practical performance depends on **engine latency**, **parallelization**, and **network** coupling choices; these are **deployment-specific**.

## Relevance to group

Useful **infrastructure** adjacent to **LAMMPS/ReaxFF** workflows when **nuclear quantum effects** or **advanced sampling** is required; **not** a **van Duin group** authorship paper.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.cpc.2018.09.020` (`papers/Others/Kapil_PIMD_2019.pdf`).

## Related topics

- [[reaxff-family]]
