---
id: paper:2013yang-chemical-phy-self-weakening-lithiated
type: paper
title: "Self-weakening in lithiated graphene electrodes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - method:reaxff
  - domain:reactive-md
  - domain:mechanics-tribology
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cplett.2013.01.048"
year: 2013
authors:
  - "Yang, Hui"
  - "Huang, Xu"
  - "Liang, Wentao"
  - "van Duin, Adri C. T."
  - "Raju, Muralikrishna"
  - "Zhang, Sulin"
venue: "Chemical Physics Letters"
pdf_sha256: "da9fdabd46aa7af125dcb75d8d3ac66f81405f3d61dce4fa8ba086abd4f96985"
pdf_path: "papers/CP_Letter_LiC_galley.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2013yang-chemical-phy-self-weakening-lithiated -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Chemical Physics Letters** article (**Chem. Phys. Lett.** **563**, **58–62**, 2013) studies **mechanochemical coupling** in **lithiated graphene** models relevant to **Li-ion battery anodes**. A **reactive force field (ReaxFF-class)** parametrization is used so that **lithium uptake**, **stress**, and **fracture** can be treated in the same **large-scale MD** framework. The work emphasizes that **Li diffusion** and **mechanical stress** are strongly coupled in these **carbonaceous** systems: **Li** tends to migrate toward **crack tips**, where accumulation can **modulate crack growth and instability**, linking atomistic behavior to electrode **degradation** and **lifetime** questions for **graphene-based** architectures. The local corpus PDF is a **proof/galley** (`CP_Letter_LiC_galley.pdf`); the **version-of-record** text and figures are defined by **DOI `10.1016/j.cplett.2013.01.048`**.

## Methods

**Reactive MD** with a **ReaxFF-type** description of **C–H–O–Li** chemistry for **lithiated graphene** geometries; simulations probe **crack tip** environments under **Li concentration** and **mechanical loading** patterns appropriate to electrode stress states (see the article for system sizes, boundary conditions, and electromechanical protocols).

## Findings

Atomistic trajectories support a picture in which **Li transport** and **mechanical failure** are not separable: **Li** segregation near **cracks** feeds back on **crack stability**, informing how **graphene-based** electrodes may **weaken** under **lithiation**-driven stress beyond simple elastic estimates.

## Limitations

The local **normalized extract** on file is **proof correspondence plus highlights only**; quantitative values, figures, and full methodological detail should be taken from the **published CPL article** at the DOI above.

## Relevance to group

van Duin and Raju coauthorship on Li–graphene mechanical coupling relevant to battery anode modeling.

## Citations and evidence anchors

- Highlights list (extract).
- DOI taken from normalized bibliography venue string `doi:10.1016/j.cplett.2013.01.048` in `normalized/papers/2013yang-chemical-phy-self-weakening-lithiated.json`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
