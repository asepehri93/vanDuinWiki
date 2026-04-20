---
id: paper:2016rimsza-venue-jp6b07939
type: paper
title: "Water interactions with nanoporous silica: Comparison of ReaxFF and ab initio based molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - method:aimd
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b07939"
year: 2016
authors:
  - "J. M. Rimsza"
  - "Jejoon Yeon"
  - "A. C. T. van Duin"
  - "Jincheng Du"
venue: "J. Phys. Chem. C"
pdf_sha256: "d3170c8e85355d7001264f6cc194620e9920ad3ca974f3d482096e052e1d931a"
pdf_path: "papers/Rimsza_JPC_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016rimsza-venue-jp6b07939 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Reactive MD** with **ReaxFF** and comparison to **DFT-based AIMD** are used to study **water** interacting with **nanoporous silica**, comparing two **Si/O/H ReaxFF** parametrizations (**Yeon et al.** vs **Fogarty et al.**). The authors analyze **local structure**, **water dissociation**, **barriers**, **diffusion**, and **defect** chemistry (**two-membered ring** removal, **hydroxylation**), concluding that **Yeon et al.** better matches **AIMD** for **high-defect**, **strained** silica–water scenarios. **Adri C. T. van Duin** is a coauthor.

## Methods

- **Classical MD** with **ReaxFF** (two parametrizations) on **nanoporous silica** plus **water**.
- Reference **AIMD** data for structural and kinetic comparison.

## Findings

- Competing **reaction pathways** and **intermediate** structures govern **2-ring defect** removal and **hydroxylation** rates.
- **Nanoconfinement** reduces **water diffusion**; **H** can diffuse faster than **O** via **hopping**-like behavior.
- **Yeon et al.** parametrization aligns more closely with **AIMD** for the targeted **Si/O/H** chemistry.


## Limitations

- Parametrization dependence shows **force-field uncertainty** remains for **complex amorphous** silica surfaces.

## Relevance to group

Direct **ReaxFF** development and validation for **geochemical**/**materials** **silica–water** interfaces involving **van Duin**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.6b07939` (`papers/Rimsza_JPC_2016.pdf`).

## Related topics

- [[reaxff-family]]
