---
id: paper:2011physrevb-84-075460-venue-paper
type: paper
title: "Reparameterization of the REBO-CHO potential for graphene oxide molecular dynamics simulations"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:2d-layered, material:graphene-carbon-nano, method:classical-md, task:parameterization, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.84.075460"
year: 2011
authors: ["Fonseca, Alexandre F.", "Lee, Geunsik", "Borders, Tammie L.", "Zhang, Hengji", "Kemper, Travis W.", "Shan, Tzu-Ray", "Sinnott, Susan B.", "Cho, Kyeongjae"]
venue: "Physical Review B"
pdf_sha256: "c249f461a3e1484ee4c9756c350c34131b67f28864c0f6af8ddaf920f7a0c8af"
pdf_path: "papers/Others/PhysRevB.84.075460.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2011physrevb-84-075460-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Physical Review B** article modifies the **second-generation REBO-CHO** reactive empirical bond-order potential (carbon/hydrogen/oxygen) to better describe **graphene oxide (GO)**. Using **DFT** as reference data, the authors optimize parameters affecting **oxygen binding to graphene** and **C–O bond distances**, focusing changes on the **bond-order term** so prior REBO-CHO training for other uses is largely preserved. The introduction positions GO as technologically relevant (e.g., reduction routes to graphene, battery electrodes mentioned in context) and contrasts **REBO efficiency** with **ReaxFF/DFT** cost for large-scale GO simulations.

## Methods

- **Classical MD** with **REBO-CHO**, selectively **reparameterizing the bond-order component** against DFT energetics/structures for oxygen–graphene interactions.
- Benchmarking against DFT for binding energies, equilibrium C–O distances, and selected GO sample properties (per paper outline in extract).

<!-- enrich-from-extract:v2 -->

- INTRODUCTION Classical molecular dynamics (MD) methods are powerful tools for atomistic simulations of many physical properties of diverse material systems composed from thousands to billions of atoms, especially when quantum mechanics simulations are prohibited by computational limitations.
- The consequence is that many different potentials have been developed for different classes of elements and for different purposes, including, for example, the ﬁrst- and second-generation reactive bond order potentials (REBO), 1,2 which together with the adaptive intermolecular reactive bond order potential (AIREBO) 3 are optimized for hydrocarbon materials; the embedded atom method (EAM) 4 and modiﬁed EAM (MEAM), 5 which are optimized for metals and alloys but include some parametrizations for metal oxides; and the chemistry at Harvard macromolecular mechanics (CHARMM) force ﬁeld, 6 which is targeted to- ward biomolecules.
- For example, the charge-optimized many-body (COMB) potential is suitable for a variety of metals, covalent semiconductors, and their oxides, 7–10 and the reactive force ﬁeld (ReaxFF) 11 has been parameterized for a large variety of systems, including covalently bound, metallic, and ionic materials.
- Recent theoretical studies of GO were performed using both density functional theory (DFT) 32,34–36 and ReaxFF,37,38 but there is no application of the REBO or AIREBO potential to GO.
- Based on DFT calculations, new parameters were obtained to simulate C–O, O–O, O–H bonds within the REBO formalism, giving rise to a “REBO-CHO” potential.
- It is important and useful to modify the REBO-CHO potential to optimize its description of GO because it is orders of magnitude more computationally efﬁcient than either ReaxFF or DFT because it lacks explicit treatment of charge.
- We also describe our method for modifying the REBO-CHO potential to provide physical properties of GOs in accordance with DFT, without altering the results for which original REBO-CHO was parameterized.
- We then present a list of the discrepancies between REBO-CHO and DFT results.
- IV, we describe the method for changing REBO-CHO parameters to correctly simulate the physical properties of GOs.
- In this work, the approach toward the optimization is based on modifying the bond order term.


## Findings

- Identifies shortcomings of the prior REBO-CHO parameterization for GO and proposes a bond-order-focused remedy aligned with DFT references in the excerpted introduction and methods outline.

### Additional results (article abstract)

- The challenge of empirical potential development is to obtain an accurate interatomic potential energy function of the system which not only captures most of physical and chemical properties of the atoms that compose the system and their interactions but also generates good predictions of the physical properties of all system environments.
- They are largely used to study the physical and chemical properties of carbon structures. 12–18 Recent examples of successful studies performed with REBO and AIREBO are the stiffness of graphene with grain boundaries, 19 carbon nanobelts,20 load transfer behavior in multiwalled carbon nanotubes (MWNTs) with defects connecting their walls, 21–23 thermal conductivity of C 13 graphene,24 and the mechanical properties of graphane.25 Another member of the graphitic structure family is graphene-oxide (GO).
- It was originally developed 39 and applied 40,41 to study polymer chains, and preliminary tests performed by us demonstrated that REBO-CHO was not suitable to simulate GO.
- Importantly, we demonstrate that all these issues can be solved by recalculating only the bond order term of the potential.
- We also show some tests performed with the modiﬁed REBO-CHO.
- PHYSICAL REVIEW B 84, 075460 (2011) to simulate hydrocarbon-oxide molecules.
- In this paper, we compare the predictions of DFT and REBO-CHO for oxygen binding energies to graphene, equi- librium C–O bond distances, and other GO properties.
- II, we present the main expressions of REBO-CHO formalism needed for the reparametrization.
- III, we show the GO systems used to test REBO-CHO and to provide, from DFT calculations, the binding energies and equilibrium C–O bond distances.
- V, we summarize and discuss the results and conclusions.


## Limitations

- This is **REBO**, not ReaxFF; transferability across oxygen chemistries and defects should be validated case-by-case.
- Extract is **partial**; quantitative error tables and full GO test cases are not captured in pages 1–2 alone.

## Relevance to group

Useful cross-reference for **reactive carbon–oxygen classical potentials** and GO modeling choices adjacent to ReaxFF-centric workflows.

## Citations and evidence anchors

- Title page and Secs. I–II introduction: motivation, REBO vs ReaxFF discussion, GO focus (Phys. Rev. B 84, 075460; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
