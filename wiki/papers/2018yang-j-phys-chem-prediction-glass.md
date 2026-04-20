---
id: paper:2018yang-j-phys-chem-prediction-glass
type: paper
title: "Prediction of the Glass Transition Temperatures of Zeolitic Imidazolate Glasses through Topological Constraint Theory"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:zeolite-porous
  - method:reaxff
  - task:application
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.8b03348"
year: 2018
authors:
  - "Yongjian Yang"
  - "Collin J. Wilkinson"
  - "Kuo-Hao Lee"
  - "Karan Doss"
  - "Thomas D. Bennett"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "John C. Mauro"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "8b60ae242d6f9839444651f5816696194c3b0bdf2f21399ff9eccacae714ca01"
pdf_path: "papers/Yang_ZIF_JPCL_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018yang-j-phys-chem-prediction-glass -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

For **agZIF-62** glasses of composition **Zn(Im₂₋ₓbImₓ)**, the work builds a **topological constraint model** for **glass transition temperature (Tg)** that combines **experimental** data with **ReaxFF molecular dynamics** to define a **hierarchy of bond constraints**. The model reproduces **Tg** versus **benzimidazolate** content with reported **~3.5 K** error and is extended to **5-methylbenzimidazolate**, yielding a **ternary Tg diagram** for a **hypothetical** three-ligand framework. **Yang**, **Shin**, and **van Duin** anchor the **reactive MD** contribution; **Mauro** and collaborators provide the **constraint-theory** framework for **MOF glasses**.

## Methods

- **ReaxFF MD** to inform **constraint** assignments and **network** rigidity inputs used in **topological constraint theory (TCT)**.
- **TCT** construction and extension to **multicomponent** ligand mixtures (see **J. Phys. Chem. Lett.** for equations and fitting).

The article further notes that following Angell’sd e ﬁnition, 13,14 Tg is the temperature at which the supercooled liquid has a viscosity of 10 12 Pa·s. We look at the [Zn(Im 2−xbImx)] glass-forming system by considering its fundamental building units: the ZnN 4 tetrahedra and Im/bIm ligands, and the constraints able to be imposed ( Figure 1). As the central quantity in TCT is the network connectivity, hydrogen atoms are not considered since they have only one bond and will never a ﬀect the connectivity of the [Zn(Im 2−xbImx)] network. In general, all the network- forming species should have a coordination number r ≥ 2. Such network-forming species are subject to two types of constraints: (1) two-body constraints (bond stretching, BS), e.g., the α constraint in Figure 1 , and (2) three-body constraints (angular bond bending, BB), e.g., the γ constraint in Figure 1 . According to TCT, 16,24 the average number of atomic constraints n for an atom depends on its average coordination number ⟨r⟩, = ⟨⟩ +⟨ ⟩ −n r r2 (2 3) (1) where ⟨r⟩/2 is for BS and 2 ⟨r⟩ − 3 is for BB.

## Findings

- **Tg** scaling with **benzimidazolate** concentration is captured with **small** error versus the **experimental** reference used in the letter.
- **Ternary Tg** predictions illustrate how **constraint theory** plus **ReaxFF** can probe **unsynthesized ZIF glass** formulations.


From the abstract: here, we present a topological constraint model for predicting Tg, a fundamental glass property that de ﬁnes both the upper temperature limit for ZIF glasses to be practically used and the lower limit of liquid formation. Experimentally, it can be obtained from the temperature where di ﬀerential scanning calorimetry (DSC) indicates a change in heat capacity, when a sample is scanned at a rate of 10 K/min. 15 Topological constraint theory (TCT, originally developed by Phillips and Thorpe 16) considers the change of atomic degrees of freedom due to bond constraints and proposes that the optimal glass compositions possess atomic degrees of freedom of zero. By considering the connectivity of the glass network, TCT can predict many glass properties including T g,17,18 fragility,17,18 chemical durability, 19 and hardness 20 and has been widely used. 21−24 Our model incorporates a hierarchy of constraints from both the metal and organic ligands. The calculated Tg from the model and the experimental measurement 25−27 are in very good agreement, with an error less than 4 K. This model can be expanded to predict T g of other ZIF glasses with di ﬀerent organic ligands. See https://pubs.acs.org/sharingguidelines for options on how to legitimately share published articles. transition temperatures have been reported. 25−29 ZIF-4 at x = 0 was initially found to form a glass, 11 and ZIF-62 ( x = 0.25) was later found to be an exceptionally stable glass former. 25,26 Table 1 details the counting of the bond constraints for each unit in [Zn(Im 2−xbImx)], where all constraints are considered to be rigid. Depending on the sign of f, the glass network can be ﬂoppy ( f > 0), isostatic ( f = 0), or stressed-rigid ( f < 0). If we consider only α, β, and γ constraints, their onset temperatures could have the following sequence Tβ < Tγ < Tα (N−Zn−N angle is quite ﬂexible, even at low temperature 30 and the energy barrier of Zn −N bond breaking is fairly high according to Gaillac et al. 31). On the basis of this sequence, the [Zn(Im2−xbImx)] network is stressed-rigid at T < Tβ with a negative f, as shown in Figure 2 . When the temperature increases and reaches the onset temperature of a certain constraint, e.g., Tβ, f will increase and become positive, as shown by the blue curves.

## Limitations

- **TCT** assumes a **coarse** decomposition of **rigidity**; **local** chemical detail may require **full MD** cooling curves for **borderline** compositions.
- **ReaxFF** must be **trusted** for each **ligand chemistry** before **constraint** parameters are exported to **theory**.

## Relevance to group

Links **Penn State ReaxFF** on **ZIF** **glasses** to **Mauro-group** **topological constraint** methods for **Tg** design.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpclett.8b03348` (`papers/Yang_ZIF_JPCL_2018.pdf`).

## Related topics

- [[reaxff-family]]