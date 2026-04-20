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

The article further notes that a ReaxFF description was developed a ReaxFF reactive force ﬁeld for Al/C interactions to investigate carbon coating and its e ﬀect on the oxidation of aluminum nanoparticles (ANPs). The ReaxFF parameters were optimized against quantum mechan- ics-based (QM-based) training sets and validated with additional QM data and data from experimental literature. ReaxFF-molecular dynamics (MD) simulations were per- formed to determine whether this force ﬁeld description was suitable to model the surface deposition and oxidation on complex materials (i.e., carbon-coated ANPs). The results of the MD simulations indicate that a carbon coating layer was formed on the surface of the bare ANPs, while H atoms were transferred from the hydrocarbons to the available Al binding sites typically without breaking C −C bonds. Moreover, the MD simulations of the oxidation of the carbon-coated ANPs indicate that the carbon-coated ANPs were less reactive at low temperatures, but they became very susceptible to oxidation when the coating layer was removed at elevated at elevated temperatures. These results are consistent with the experimental literature, and thus, the ReaxFF description that was developed in this study enables us to gain atomistic-scale insights into the role of the carbon coating in the oxidation of ANPs.

## Findings

- **Carbonaceous coatings** form on **bare ANPs** with **H migration** to undercoordinated **Al** without necessarily fragmenting all **C–C** frameworks (per abstract-level summary).
- **Oxidation resistance** is **temperature-dependent**: coatings can **passivate** at low \(T\) yet fail dramatically when **removed/heated**.
- **Qualitative agreement** with selected **experimental oxidation** observations is claimed for the modeled scenarios.


From the abstract: the reported results show that the ReaxFF description correctly reproduced the Al/ C interaction energies obtained from the QM calculations and qualitatively captured the processes of the hydrocarbons ’ binding and their subsequent reactions on the bare ANPs. The growth of the carbon layer depended strongly on the hydrocarbon precursors that were used.

## Limitations

- **Combustion-relevant** conditions span **pressure, size polydispersity, and oxide polymorphism** beyond any single MD study.
- **ReaxFF** cannot capture **electronically excited** or **plasma-driven** chemistry without additional extensions.

## Relevance to group

Core **Hong + van Duin** line on **energetic Al nanoparticles** and **passivation engineering**, tightly coupled to **ReaxFF parameterization practice**.

## Citations and evidence anchors

- Abstract in `papers/Hong_AlCOx_JPCC_2016.pdf`; **DOI:** `10.1021/acs.jpcc.6b00786`.

## Related topics

- [[reaxff-family]]