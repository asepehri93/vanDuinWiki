---
id: paper:2016yoon-venue-microsoft-word
type: paper
title: "Supporting information: ReaxFF short-range repulsion training for noble gas ion irradiation of graphene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: null
year: 2016
authors:
  - "Kichul Yoon"
  - "Ali Rahnamoun"
  - "Jacob L. Swett"
  - "Vighter Iberi"
  - "David A. Cullen"
  - "Ivan V. Vlassiouk"
  - "Alex Belianinov"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: null
pdf_sha256: "724a1acf490af3ba44dfe468756819eab959b497cdc73836ec8a740148e89a11"
pdf_path: "papers/Yoon_ACSNano_SI.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-microsoft-word -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **supporting information** excerpt documents **ReaxFF** fitting of **short-range nuclear repulsion** for **noble gas ion** impacts on **graphene**, using **DFT** energies for **noble gas + benzene** geometries as a **planar aromatic** proxy and comparing to **ZBL**-style references. Three impact sites (**ring center**, **bond center**, **atop C**) anchor the parameter comparison shown in **Fig. S1** references. It accompanies the **ACS Nano** study on **defect formation** under **ion irradiation** coauthored by **van Duin** and **ORNL** collaborators.

## Methods

- **DFT** (**B3LYP** with basis sets noted in SI) vs **ReaxFF** vs **ZBL** for **repulsive** interactions.
- Geometry scans across **impact positions** relevant to **graphene** irradiation modeling.

The article further notes that atomistic-Scale Simulations of Defect Formation in Graphene Under Noble Gas Ion Irradiation Kichul Yoon a, Ali Rahnamoun a, Jacob L. Force field parameterization results In order to develop the ReaxFF force field for the description of short-range nuclear repulsion, the study obtained energies in the geometry that consists of a noble gas ion and benzene by using DFT and ZBL potential 1. DFT calculation was performed with 6-311G ** (for the interaction of benzene with He, Ne, Ar ions) and LACV3P ** basis set (for the interaction of benzene with Kr ion) and B3LYP functional. The relative energies obtained from DFT, ZBL potential, and the ReaxFF force field are in good agreement with each other. Vlassiouk f, Alex Belianinov d, g, Xiahan Sang d, Olga S.

## Findings

- Reported **relative energies** align across **DFT**, **ZBL**, and **ReaxFF** for the showcased **training** configurations.


From the abstract: note that the benzene molecule, which is similar to graphene in that it is also a planar structure, was used for the interaction of ions with graphene. Three impact positions (center of ring, center of bond, and top of C atom) were considered for the short-range repulsive interactions between ions and graphene, as indicated in the subset images in Fig.

## Limitations

- **SI fragment** only—consult the bundled **main article** PDF for **full irradiation** protocols and **experimental** benchmarks.

## Relevance to group

Supports **ReaxFF** parametrization for **2D carbon** **ion-beam** damage workflows led by **van Duin**.

## Citations and evidence anchors

- Companion article: **Yoon et al.**, *ACS Nano* **2016**, noble gas irradiation of graphene (`papers/Yoon_ACSNano_SI.pdf`).

## Related topics

- [[reaxff-family]]