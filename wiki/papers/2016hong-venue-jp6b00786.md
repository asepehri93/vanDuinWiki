---
id: paper:2016hong-venue-jp6b00786
type: paper
title: "Atomistic-scale analysis of carbon coating and its effect on the oxidation of aluminum nanoparticles by ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b00786"
year: 2016
authors:
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "0d4a4f29a408a9ebdddd4d7b9865ac139f424a5a32e9659cf72bbb76f07dc1f4"
pdf_path: "papers/Hong_AlCOx_JPCC_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016hong-venue-jp6b00786 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

An **Al/C ReaxFF** is developed against **QM training sets** and exercised in **ReaxFF MD** to study **hydrocarbon-derived carbon coatings** on **aluminum nanoparticles (ANPs)** and their influence on **subsequent oxidation**. Simulations report **hydrogen transfer to Al sites**, **C–C bond-preserving** binding modes for some precursors, and **precursor-dependent carbon layer growth**. **Oxidation** of **coated** particles is compared to **bare** ANPs, highlighting **reduced reactivity at low temperature** but **high susceptibility once the coating is disrupted at elevated temperature**, consistent with the **experimental literature** cited in the article.

## Methods

- **ReaxFF parameter optimization** for **Al–C–O–H** chemistry with **QM validation** data described in the paper.
- **Reactive MD** trajectories for **deposition** sequences followed by **oxidation** stages.

## Findings

- **Carbonaceous coatings** form on **bare ANPs** with **H migration** to undercoordinated **Al** without necessarily fragmenting all **C–C** frameworks (per abstract-level summary).
- **Oxidation resistance** is **temperature-dependent**: coatings can **passivate** at low \(T\) yet fail dramatically when **removed/heated**.
- **Qualitative agreement** with selected **experimental oxidation** observations is claimed for the modeled scenarios.

## Limitations

- **Combustion-relevant** conditions span **pressure, size polydispersity, and oxide polymorphism** beyond any single MD study.
- **ReaxFF** cannot capture **electronically excited** or **plasma-driven** chemistry without additional extensions.

## Relevance to group

Core **Hong + van Duin** line on **energetic Al nanoparticles** and **passivation engineering**, tightly coupled to **ReaxFF parameterization practice**.

## Citations and evidence anchors

- Abstract in `papers/Hong_AlCOx_JPCC_2016.pdf`; **DOI:** `10.1021/acs.jpcc.6b00786`.

## Related topics

- [[reaxff-family]]
