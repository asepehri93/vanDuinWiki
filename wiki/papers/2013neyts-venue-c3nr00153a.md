---
id: paper:2013neyts-venue-c3nr00153a
type: paper
title: "Formation of single layer graphene on nickel under far-from-equilibrium high flux conditions"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - material:graphene-carbon-nano
  - material:metal-surface
  - method:reaxff
  - method:monte-carlo
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1039/c3nr00153a"
year: 2013
authors:
  - "Neyts, Erik C."
  - "van Duin, Adri C. T."
  - "Bogaerts, Annemie"
venue: "Nanoscale"
pdf_sha256: "5af3f1bcafc215281a3807638ae203441d0f584f9fbe91552ab92e9540005bbb"
pdf_path: "papers/Neyts_Nanoscale_2013.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2013neyts-venue-c3nr00153a -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Hybrid reactive MD with uniform acceptance force-bias Monte Carlo (MD/UFMC) is used to study graphene formation on ultrathin Ni(100) under high effective precursor flux. The study argue that under these strongly driven conditions a combined deposition–segregation pathway can yield near-continuous graphene-like films by 900 K and above, complementing literature focused on equilibrium segregation (abstract; introduction, extract pages 1–2).

## Methods

State-of-the-art hybrid MD/UFMC with the same ReaxFF line as prior Ni(111) graphene work (Meng et al., cited in text). Ni(100) is chosen because polycrystalline Ni often exposes (100) after synthesis. The manuscript contrasts unrealistically high flux in pure MD with the UFMC-modulated sampling (introduction, extract pages 1–2).

The article further notes that in this work, we have deliberately chosen to simulate the growth on the Ni(100) facet, instead of the more stable Ni(111) facet, since it is known that on poly-Ni substrates, the most abundant (110) direction, in addition to the (100) and (111) directions, is transformed into the most abundant (100) direc- tion aer graphene synthesis. 26 Note that the Ni(100) surface is less closely packed compared to the Ni(111) structure. Experimentally, it is known that in the segregation process of graphene on nickel surfaces, typically multiple graphene layers are formed. 3,27 This is a direct consequence of the relatively high solubility of carbon in bulk nickel, of about 2.7 at% at the eutectic point (1600 K) and 0.9 at% at about 900 K. In the subsurface region, the solubility is even much higher, reaching up to 25%, corresponding to the metastable Ni 3C composi- tion.20,28 Limiting the amount of carbon that can dissolve in the nickel might therefore avoid the formation of multiple layers and therefore result in single-layer graphene growth.

## Findings

Simulations predict nearly continuous graphene layers at 900 K and above under the modeled high-flux conditions. The discussion ties carbon solubility in Ni and subsurface saturation ideas to limiting multilayer growth and enabling single-layer formation (abstract; introduction).


From the abstract: there- fore, the carbon di ﬀusion barriers for segregation will be smaller on the Ni(100) surface. In this scenario, advantage is taken of the relatively high barrier for di ﬀusion of surface adsorbed carbon into the bulk of the nickel substrate and for di ﬀusion from the bulk to the surface, which has an overall value of about 2.33 eV. 31 In this paper, we demonstrate that such a rapid saturation indeed lea. The most straightforward way to accomplish this would be to reduce the thickness of the nickel lm. However, while physical vapor deposited nickel lms as thin as 1 nm have previously been used for CNT synthesis 29,30 such thin lms inevitably form clusters when heated. Alternatively, the dissolution of carbon in the lm may also be limited by very rapidly saturating the upper layers of the lm, before di ﬀusion to the bulk takes place.

## Limitations

UFMC lacks a strict physical time scale; fluxes remain above typical CVD experiments. Defectivity and comparison to Ni(111) growth remain active caveats in the narrative (introduction, extract pages 1–2).

## Relevance to group

Adri van Duin as coauthor links the ReaxFF Ni/C chemistry used in metal-catalyzed carbon growth studies across the corpus.

## Citations and evidence anchors

- Abstract: mechanism statement and 900 K result.
- Introduction: MD/UFMC rationale, Ni(100) choice, flux discussion (extract pages 1–2).
- DOI: `10.1039/c3nr00153a` (extract footer).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]