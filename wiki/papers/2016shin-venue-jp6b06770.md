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

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This paper develops a **ReaxFF** description of **Pt/Ni/C/H/O** aimed at **heterogeneous catalysis**, fitting to **DFT** data on **Pt–Ni alloy** equations of state, **surface energies** of **Pt\(_x\)Ni\(_{1-x}\)** facets, and **adsorption** of **O**, **H**, **C**, **hydrocarbon fragments**, **CO**, **OH**, and **H\(_2\)O**. **GCMC** and **MD** on **slabs** and **nanoparticles** probe **Pt** vs **Ni segregation** under **vacuum**, **H\(_2\)**, and **O\(_2\)**, matching trends for **Pt-rich** compositions while noting weaker behavior for **Ni-rich** alloys. **ExxonMobil** coauthorship reflects **industrial catalysis** context.

## Methods

- **ReaxFF** optimization against **DFT** **EOS**, **surface energies**, and **adsorption** trends.
- **Grand-canonical Monte Carlo** and **MD** for **segregation** under different **gas environments**.

The article further notes that a ReaxFF description was developed the ReaxFF force ﬁeld for Pt/Ni/C/H/O interactions, speci ﬁcally targeted for heterogeneous catalysis application of the Pt−Ni alloy. The force ﬁeld is trained using the DFT data for equations of state of Pt 3Ni, PtNi 3 and PtNi alloys, the surface energy of the PtxNi1−x(111) (x = 0.67−0.83), and binding energies of various atomic and molecular species (O, H, C, CH, CH 2,C H3, CO, OH, and H 2O) on these surfaces. The relative order of binding strengths among adsorbates is a function of alloy composition and the force ﬁeld is trained to describe the trend observed in DFT calculations, namely, H 2 <H 2O<C H 3 ≈ O2 ≈ CO < OH < CH 2 <C ≈ CH on Pt8Ni4,H 2 <H 2O<C O ≈ O2 <C H3 <O H<C H 2 <C H<Co nP t 9Ni3, and H 2 <H 2O<O 2 <C O<C H 3 <O H<C H 2 <C ≈ CH on Pt 10Ni2. Using this force ﬁeld, we performed the grand-canonical Monte Carlo (GCMC) and molecular dynamics (MD) simulations for a Pt 3Ni slab and a truncated cuboctahedral nanoparticle terminated by (111) and (100) faces, to examine the surface segregation trend under diﬀerent gas environments. These results suggest that the Pt/Ni alloy force ﬁeld can be successfully used for the preparation of Pt −Ni nanobimetallic catalysts structure using GCMC and run MD simulations to investigate its role and the catalytic chemistry in catalytic oxidation, dehydrogenation and coupling reactions. We recently published a ReaxFF reactive force ﬁeld for Pt/ C/H/O 15 by coupling a Pt/O force ﬁeld16 with Pt/H and Pt/C parameters, and evaluated the performance of this force ﬁeld to predict the adsorption structure and isotherms of oxygen, hydrogen and OH over di ﬀerent surfaces of platinum and on nanoparticles of di ﬀerent sizes and shapes. ReaxFF, which is trained against the ﬁrst-principles data set, is computationally less expensive than DFT and more e ﬃ cient for a large-scale molecular dynamics simulation, and is uniquely capable of describing chemical reactions at a low computational cost but of reasonable accuracy. Importantly, bimetallic systems are associated with reactive surface segregation in the presence of adsorbates which could be addressed using reactive molecular dynamics or hybrid Monte Carlo −Molecular dynamics methods more readily in comparison to theoretically rigorous and computationally involved cluster expansion approaches 22 at the DFT level to account for the e ﬀect of adsorbates 23,24 on surface segregation and ordering of alloy surfaces. Though cluster expansion approaches coupled with Monte Carlo simulations 25−27 are increasingly being employed, reactive molecular dynamics or hybrid Monte Carlo −molecular dynamics methods provide added advantage for modeling a large −scale complex alloy surface of which chemical composition and structure may not be well-de ﬁned, and for examining reaction processes on it. In addition, this work also highlights the e ﬀorts and challenges involved in developing a reactive force ﬁeld that is capable of describing all possible bonding scenarios among ﬁve atoms (Pt, Ni, C, H, and O).

## Findings

- **Adsorbate-dependent segregation**: species such as **H** and **CH\(_3\)** favor **Pt** surface enrichment, whereas **oxidation intermediates** tend to draw **Ni** to the surface.
- **Binding-strength ordering** varies with **composition**, as designed to track **DFT**.
- Performance degrades for **Ni-rich** (**x < ~0.6**) compositions, motivating further training.


From the abstract: the ReaxFF force ﬁeld shows a Pt surface segregation at x ≥ 0.67 for the (111) surface and x ≥ 0.62 for the (100) surface in vacuum. In addition, from the investigation of the preferential alloy component of the adsorbates, it is expected that H and CH 3 on the alloy surface to induce a segregation of Pt whereas the oxidation intermediates and products such as C, O, OH, H 2O, CO, CH, and CH 2 are found to induce Ni segregation. It is found that Pt segregates to the alloy surface when the surface is exposed to vacuum and/or H 2 environment while Ni segregates under the O 2 environment. The current Pt/Ni force ﬁeld still is found to have di ﬃ culties in describing the observed segregation trend in Ni-rich alloy compositions ( x < 0.6), suggesting the need for additional force ﬁeld training and evaluation for its application to describe the characteristics and chemistry of Ni-rich alloys. ■ INTRODUCTION Platinum is one of the most important and e ﬃ cient metal catalysts. As is shown below, the force ﬁeld developed in this work performs reasonably well with a Pt to Ni ratio of greater than 0.6. In the presence of O 2 species, Ni segregates to the surface of PtNi nanoparticle, whereas Pt segregates under the H 2 or the vacuum environment due to the di ﬀerence of their a ﬃ nity to Pt and Ni. Thus, it is of great importance to study the correlation between the surface composition and the adsorption strength in the presence of various adsorption species on the Pt −Ni alloy catalysts. We have earlier published a validated Ni/C/H/O force ﬁeld17,18 and our goal in this work is to develop a modular Pt/Ni bimetallic alloy parameters and couple them with Pt/C/H/O and Ni/C/H/O force ﬁelds to obtain a bimetallic reactive force ﬁeld for Pt/Ni/ C/H/O, which is capable of describing the hydrocarbon conversion on a bimetallic catalyst. It is well accepted that ab initio or ﬁrst-principles based DFT predictions are valuable to guide synthesis of new and/or improved catalytic materials by providing fundamental properties of reaction energetics and kinetics together with the stability of the catalyst. 19−21 However, the DFT method is computationally expensive and is still limited to small system sizes of tens of ångstroms and a very short time scale of few picoseconds.

## Limitations

- **Bimetallic** reactive spaces are large; remaining errors map to specific **composition**/**adsorbate** corners.

## Relevance to group

Core **ReaxFF parametrization** publication from **van Duin**’s group on **alloy catalyst** modeling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.6b06770` (`papers/Shin_PtNiCHO_JPCA_2016.pdf`).

## Related topics

- [[reaxff-family]]