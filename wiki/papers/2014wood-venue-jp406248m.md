---
id: paper:2014wood-venue-jp406248m
type: paper
title: "Coupled thermal and electromagnetic induced decomposition in the molecular explosive α-HMX: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
source_refs: []
doi: "10.1021/jp406248m"
year: 2014
authors:
  - "Mitchell A. Wood"
  - "Adri C. T. van Duin"
  - "Alejandro Strachan"
venue: "Journal of Physical Chemistry A 2014, 118, 885–895"
pdf_sha256: "4e5c3ea0d176293776252e8d2caef7e7009088aa1a7c69555413075ef9a91bc0"
pdf_path: "papers/Wood_HMX_JPCA_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014wood-venue-jp406248m -->

## One-paragraph summary

Wood, van Duin, and Strachan use **ReaxFF MD** to study **α-HMX** decomposition under **rapid heating** and under **sinusoidal electric fields** at multiple frequencies and strengths, focusing on how **insult type** and **energy input rate** change the **energy thresholds** for initial chemistry and for onset of **exothermic** reaction cascades. The abstract argues both thresholds rise with heating/input rate and plateau toward **athermal** regimes at very fast loading, with **insult-type-dependent** thresholds especially for exothermic onset. The introduction frames the work within **vibrational energy transfer**, **anharmonic coupling**, and **mode-targeted excitation** debates in energetic materials, and the methods section notes a **nitramine ReaxFF** parameterization integrated with broader **C/H/O combustion** training for improved transferability.

## Methods

- **LAMMPS** reactive MD with **ReaxFF** parametrization for **nitramines** (HMX training includes dissociation pathways and barriers from **DFT** at B3LYP basis levels described in extract).
- Protocols include **direct heating ramps** and **time-dependent electric fields** intended to couple selectively to modes, plus spectral analysis sections referenced in the paper outline.

## Findings

- **Field frequency/strength** and **thermal ramp rate** alter early decomposition timing and energy accounting in the abstract-level claims.
- Parameter checks quoted: **NO\(_2\)** dissociation energy close to DFT; **HONO** vs **concerted ring-opening** pathways differ in exothermicity and barrier, influencing initiation pathway discussion.

## Limitations

- Classical reactive MD cannot capture **electronic excitations** explicitly; electric-field driving is a **classical energy-delivery** model subject to interpretation.
- Extract is early pages; quantitative thresholds and spectra need full-text review.

## Relevance to group

**Adri C. T. van Duin** as co-author ties the study to **ReaxFF** parametrization for **energetic materials** and coupled **thermal/nonthermal** insult modeling pursued in collaboration with **Purdue**-side HED modeling expertise.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp406248m](https://doi.org/10.1021/jp406248m)

## Related topics

- [[reaxff-family]]
