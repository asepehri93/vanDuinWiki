---
id: paper:2016gai-venue-research
type: paper
title: "Atomistic adsorption of oxygen and hydrogen on platinum catalysts by hybrid grand canonical Monte Carlo/reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - method:monte-carlo
  - material:metal-surface
  - task:validation
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b01064"
year: 2016
authors:
  - "Lili Gai"
  - "Yun Kyung Shin"
  - "Muralikrishna Raju"
  - "Adri C. T. van Duin"
  - "Sumathy Raman"
venue: "J. Phys. Chem. C"
pdf_sha256: "9c51c72f55e9e6045c41d4461e819f9a8615a5e21cd1ec876ac962f1bcd3ed26"
pdf_path: "papers/Gai_PtHO_JPC_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016gai-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study combines **hybrid grand canonical Monte Carlo with reactive MD (GCMC/RMD)** and a **Pt/O/H ReaxFF** to predict **coverage-dependent adsorption** of **oxygen and hydrogen** on **Pt facets**, **reconstructed Pt(110)**, and **Pt nanoparticles** across **pressure–temperature** conditions relevant to **operando catalysis**. The study reports **isotherm-style** behavior, **subsurface/bulk penetration** at aggressive chemical potentials, and **spot validation** of **O binding on Pt(321)** outside the primary training set. Industrial coauthorship (**ExxonMobil**) signals application targeting **reactor-relevant adsorbate structure preparation** for follow-on reaction MD.

## Methods

- **GCMC/RMD** moves that insert/delete **O or H** while relaxing configurations with **ReaxFF**.
- **Nanoparticle** and **extended surface** models spanning multiple **Miller indices**.

## Findings

- **Adsorption isotherms** map how **O and H** populate **surface, subsurface, and bulk** regions as a function of imposed **gas-phase potential**.
- **Pt(321)** tests indicate **transferable** qualitative performance for **step/kink** sites not explicitly in the training data (as claimed in the abstract narrative).
- Results are cross-compared to **DFT and experiment** where available in the article body.

## Limitations

- **GCMC/RMD** still inherits **ReaxFF uncertainties** for **oxidized, hydroxylated, and reconstructed** Pt under electrochemical potentials not identical to the gas-phase grand potential used here.
- **Proof PDF** path may differ cosmetically from the final issue layout.

## Relevance to group

Showcases **time-accelerated sampling + ReaxFF** for **Pt catalysis**, a recurring theme in collaborations between **Penn State** and **industry partners**.

## Citations and evidence anchors

- Abstract and metadata in `papers/Gai_PtHO_JPC_2016_proof.pdf`; **DOI:** `10.1021/acs.jpcc.6b01064`.

## Related topics

- [[reaxff-family]]
