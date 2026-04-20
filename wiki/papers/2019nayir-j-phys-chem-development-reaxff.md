---
id: paper:2019nayir-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF Reactive Force Field for Interstitial Oxygen in Germanium and Its Application to GeO2/Ge Interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:widegap-semiconductor
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b08862"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "J. Phys. Chem. C 123:1208-1218 (2019)"
pdf_sha256: "076ea7746bef0efc7405eb183604704f0ff8d218ffae4379c05a718282012f37"
pdf_path: "papers/Nayir_JPC_C_GeOx_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019nayir-j-phys-chem-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A Ge/O/H ReaxFF is extended from prior work with additional QM training on O interstitial energies and migration in diamond Ge and on bulk GeO/GeO2 condensed-phase data. The refined FF reproduces equations of state and heats of formation and ranks O-interstitial sites (bond-centered, split, tetrahedral, hexagonal) consistently with DFT. Oxygen diffusion between bond-centered sites and through the split-like transition state matches the intended DFT picture; ReaxFF predicts an effective barrier near 50 kcal/mol over 800–2000 K. GeO2/Ge interface oxidation simulations show oxide thickening and Ge consumption with temperature and time, unlike Tersoff-based runs that miss this behavior.

## Methods

ReaxFF reparameterization with expanded training sets from DFT; MD for O diffusion in bulk Ge and for heated Ge/GeO2 stacks; comparison against a Tersoff potential for interface oxidation.

<!-- enrich-from-extract:v2 -->

- We developed the ReaxFF force ﬁeld parameters for Ge/O/H interactions, speci ﬁcally targeted for the applications of Ge/GeO 2 interfaces and O-di ﬀusion in bulk Ge.
- The original training set, taken from the Zheng et al. work, includes quantum mechanics (QM) data for equations of state and heats of formation of GeO and GeO 2 condensed phases as well as dissociation energies for single and double bonds of Ge and angle distortion of O −Ge−O.
- We expanded this training set with the additional crystal data containing the formation energies of di ﬀerent O-interstitial centers and the minimum energy migration pathway of O atoms in diamond Ge.
- After re ﬁtting the force ﬁeld parameters based upon the extended training set, the ReaxFF results show that the equations of state and heats of formation of the GeO and GeO 2 condensed phases retain a good ﬁt with the QM calculations.
- Furthermore, O atoms di ﬀuse along a pathway between neighboring bond-centered (BC) interstitial sites and go through the asymmetric transition state at the split site as in DFT.
- We also examined the temperature dependence of O di ﬀusion in bulk Ge and subjected the GeO 2/Ge interface to heat treatment based on the ReaxFF and Terso ﬀ potential.
- At the temperatures over 1400 K, ReaxFF allows the O atom to di ﬀuse along the theoretically reported pathway between the adjacent BC centers, whereas Terso ﬀ potential contradicts the DFT reports by resulting in di ﬀusion between the BC and H interstitial sites.
- In addition, the ReaxFF correctly predicts the relative stability of the O-interstitial centers in the diamond Ge to be bond-center → split → tetrahedral → hexagonal from most stable to least stable with the energies showing a quantitative agreement with density functional theory (DFT).


## Findings

Interstitial ordering and migration pathway align with DFT. Diffusion barrier and thermal onset of migration are in family agreement with literature-style expectations. ReaxFF captures oxidation kinetics at interfaces qualitatively consistent with experiment where cited; Tersoff contrasts fail on diffusion pathway and interface evolution.

### Additional results (article abstract)

- Based on the results of molecular dynamics simulations, the ReaxFF accurately predicts the di ﬀusion barrier value as 50.02 kcal/mol within the temperature range of 800 −2000 K.
- For the Ge/GeO 2 interface, the ReaxFF results show that the thickness of GeO 2 increases and the Ge substrate is consumed depending on the temperature and the oxidation time, supported by the experiments, while no change was observed in the thicknesses of the Ge substrate and GeO 2 slab in the Terso ﬀ-based simulations.


## Limitations

Still an empirical reactive model—quantitative barriers and rates need continued benchmarking across defect configurations. Interface studies are specific to the prepared initial geometries and thermal protocol.

## Relevance to group

Core group contribution on semiconductor oxidation and defect diffusion with ReaxFF, relevant to Ge CMOS dielectric stacks.

## Citations and evidence anchors

- Local PDF: `papers/Nayir_JPC_C_GeOx_2019.pdf`
- DOI: https://doi.org/10.1021/acs.jpcc.8b08862

## Related topics

- [[reaxff-family]]
