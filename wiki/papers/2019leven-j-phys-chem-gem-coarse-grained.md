---
id: paper:2019leven-j-phys-chem-gem-coarse-grained
type: paper
title: "C-GeM: Coarse-Grained Electron Model for Predicting the Electrostatic Potential in Molecules"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:semiempirical-tightbinding
  - task:method-development
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.9b02771"
year: 2019
authors:
  - "Itai Leven"
  - "Teresa Head-Gordon"
venue: "J. Phys. Chem. Lett. 10:6820-6826 (2019)"
pdf_sha256: "4fefc06bacfadd178f054e476e321fc47185090e51dd9086ee8531c8a66c2b7c"
pdf_path: "papers/Others/C-GeM_Leven_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019leven-j-phys-chem-gem-coarse-grained -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

C-GeM introduces a coarse-grained electron picture in which each atom has a positive core and a Gaussian “electron shell,” with core–shell energetics tied to elemental electronegativity. Relaxing shell positions in the field of fixed cores yields molecular electrostatic potentials and intermolecular interactions without full ab initio cost. Tests on H/C/O/Cl-containing molecules show accurate electrostatic potentials; the model also describes dissociation of HCl to ionic species in solution versus neutral fragments in the gas phase, and is positioned as a fast alternative to reactive charge-equilibration schemes in some use cases.

## Methods

Coarse-grained electron model with Gaussian charge distributions; energy minimization over shell positions for given nuclear geometry. Validation against reference electrostatic properties and selected dissociation scenarios.

## Findings

High accuracy for electrostatic potential on tested sets; correct qualitative behavior for HCl dissociation in different environments. The approach limits unphysical long-range charge transfer compared with some classical charge models and can represent features such as sigma holes when charge is not strictly atom-centered.

## Limitations

Training/validation scope in the letter is finite (stated H/C/O/Cl set); transferability to broader chemistries and coupling to full MD for large condensed-phase systems is not the same problem as parametrizing ReaxFF.

## Relevance to group

Methodological context for polarizable and charge-aware simulations adjacent to ReaxFF/QEq discussions; co-authors at Berkeley/LBNL, not a van Duin-group paper.

## Citations and evidence anchors

Primary: `papers/Others/C-GeM_Leven_2019.pdf` — abstract and validation discussion. https://doi.org/10.1021/acs.jpclett.9b02771

## Related topics

- [[2021itai-leven-j-chem-theor-recent-advances]]
- [[reaxff-family]]
