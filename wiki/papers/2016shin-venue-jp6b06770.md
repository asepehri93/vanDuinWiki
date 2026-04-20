---
id: paper:2016shin-venue-jp6b06770
type: paper
title: "Development of a ReaxFF reactive force field for the Pt–Ni alloy catalyst"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b06770"
year: 2016
authors:
  - "Yun Kyung Shin"
  - "Lili Gai"
  - "Sumathy Raman"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A"
pdf_sha256: "d40410ed85d95cff7a8057df0c227dbedaa99c30a469cbe4781bd92ab6f230b2"
pdf_path: "papers/Shin_PtNiCHO_JPCA_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016shin-venue-jp6b06770 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

This paper develops a **ReaxFF** description of **Pt/Ni/C/H/O** aimed at **heterogeneous catalysis**, fitting to **DFT** data on **Pt–Ni alloy** equations of state, **surface energies** of **Pt\(_x\)Ni\(_{1-x}\)** facets, and **adsorption** of **O**, **H**, **C**, **hydrocarbon fragments**, **CO**, **OH**, and **H\(_2\)O**. **GCMC** and **MD** on **slabs** and **nanoparticles** probe **Pt** vs **Ni segregation** under **vacuum**, **H\(_2\)**, and **O\(_2\)**, matching trends for **Pt-rich** compositions while noting weaker behavior for **Ni-rich** alloys. **ExxonMobil** coauthorship reflects **industrial catalysis** context.

## Methods

- **ReaxFF** optimization against **DFT** **EOS**, **surface energies**, and **adsorption** trends.
- **Grand-canonical Monte Carlo** and **MD** for **segregation** under different **gas environments**.

## Findings

- **Adsorbate-dependent segregation**: species such as **H** and **CH\(_3\)** favor **Pt** surface enrichment, whereas **oxidation intermediates** tend to draw **Ni** to the surface.
- **Binding-strength ordering** varies with **composition**, as designed to track **DFT**.
- Performance degrades for **Ni-rich** (**x < ~0.6**) compositions, motivating further training.

## Limitations

- **Bimetallic** reactive spaces are large; remaining errors map to specific **composition**/**adsorbate** corners.

## Relevance to group

Core **ReaxFF parametrization** publication from **van Duin**’s group on **alloy catalyst** modeling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.6b06770` (`papers/Shin_PtNiCHO_JPCA_2016.pdf`).

## Related topics

- [[reaxff-family]]
