---
id: paper:2015376-377-000-venue-mergedfile
type: paper
title: "Electrocatalytic Polysulfide Traps for Controlling Redox Shuttle Process of Li-S Batteries"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:graphene-carbon
  - keyword:validation-experiment
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.5b04472"
year: 2015
authors:
  - "Hesham Al Salem"
  - "Ganguli Babu"
  - "Chitturi V. Rao"
  - "Leela Mohana Reddy Arava"
venue: "J. Am. Chem. Soc."
pdf_sha256: "9473346d71be63f928128bf5a3ba9ee4047b4fa346ba2451f47c305e0cec6590"
pdf_path: "papers/Others/Reddy_Arava_papers/JACS (2015).pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015376-377-000-venue-mergedfile -->

??? info "Corpus note"

    The registered PDF filename **`JACS (2015).pdf`** is non-descriptive; identity is pinned by **DOI `10.1021/jacs.5b04472`** and the abstract in `normalized/extracts/2015376-377-000-venue-mergedfile_p1-2.txt`. This work is **experimental** electrochemistry with microscopy/spectroscopy—not atomistic MD.

## Summary

Lithium–sulfur batteries promise high theoretical energy density, but the **polysulfide shuttle**—dissolution and migration of lithium polysulfide intermediates—causes capacity fade, poor Coulombic efficiency, and lithium-anode passivation. Porous carbons improve conductivity and can confine sulfur, yet **weak adsorption** of polar polysulfides on carbon limits performance. Prior work showed that **electrocatalytic current collectors** (e.g., thin **Pt** or **Ni** films) can improve kinetics and cycle life by catalyzing polysulfide conversion, but planar metal films offer limited surface area for loading. This **Journal of the American Chemical Society** article investigates **graphene-supported catalyst nanoparticles** to combine **high surface area** with **electrocatalytic** sites that **preferentially adsorb** soluble polysulfides formed during discharge and promote their **conversion** toward longer-chain species in subsequent redox steps, aiming to **control shuttle** while maintaining practical sulfur loadings.

## Methods

This *J. Am. Chem. Soc.* contribution is **experimental electrochemistry** with **microscopy and spectroscopy**; it does **not** report atomistic molecular dynamics or ReaxFF trajectories.

**Literature / design scope (non-simulation).** The authors position **graphene-supported catalyst nanoparticles** as **electrocatalytic polysulfide traps**: on discharge, soluble lithium polysulfides adsorb preferentially on catalyst sites decorating graphene and are driven toward longer-chain polysulfides in subsequent redox steps, aiming to suppress the polysulfide shuttle while retaining usable sulfur loadings (abstract in `normalized/extracts/2015376-377-000-venue-mergedfile_p1-2.txt`).

**Electrode fabrication and cell testing.** Catalyst nanoparticles are dispersed on graphene layers and compared with **pristine graphene** cathodes under matched fabrication and cycling protocols (electrolyte, sulfur loading, and cell geometry detailed in the article and SI). **Galvanostatic** cycling furnishes specific capacity, rate capability, and Coulombic efficiency; the abstract highlights roughly **40%** higher specific capacity versus pristine graphene, **100** cycles at **0.2 C**, and **99.3%** Coulombic efficiency for the highlighted catalyst–graphene configuration.

**Ex situ / in situ characterization.** **XPS** and **electron microscopy** probe catalyst–polysulfide interactions under electrochemical staging described in the paper.

**MD / reactive FF application:** **N/A —** not part of this publication.

## Findings

Uniform catalyst decoration on graphene delivers higher specific capacity than pristine graphene in the reported tests, with the abstract quoting **~40%** gain, **100** cycles at **0.2 C**, and **99.3%** Coulombic efficiency for the featured configuration (full electrochemical conditions in the article/SI). XPS and microscopy data are interpreted as evidence for preferential polysulfide interaction with catalyst sites versus bare graphene, consistent with an electrocatalytic trapping picture that accelerates polysulfide interconversion and mitigates shuttle losses relative to the carbon-only baseline. Capacities, efficiencies, and rate capability depend on electrolyte volume, sulfur loading, and catalyst loading as specified in the experimental section; treat the abstract metrics as headline values anchored to those protocols. The registered PDF path `papers/Others/Reddy_Arava_papers/JACS (2015).pdf` is non-descriptive; bibliographic identity is pinned by **DOI `10.1021/jacs.5b04472`** and this `paper:` slug for stable linking. Interface electrochemistry remains electrolyte- and loading-sensitive; atomistic simulation was not attempted here, so any downstream ReaxFF modeling must reconstruct morphologies and electric double-layer conditions independently.

## Limitations

Atomistic ReaxFF modeling is **not** part of this publication; mechanistic claims are interface-scale and electrolyte-dependent. The merged filename in `papers/Others/` should be replaced with a citation-friendly name in future corpus hygiene passes without altering PDF bytes.

## Relevance to group

Provides **experimental** context for **graphene–catalyst** cathodes in **Li–S** chemistry alongside simulation-forward papers in `wiki/papers/`.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/jacs.5b04472](https://doi.org/10.1021/jacs.5b04472) (`papers/Others/Reddy_Arava_papers/JACS (2015).pdf`).
- Extract: `normalized/extracts/2015376-377-000-venue-mergedfile_p1-2.txt` (abstract with **40% / 100 cycles / 99.3%** metrics).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
- [[reaxff-family]]
