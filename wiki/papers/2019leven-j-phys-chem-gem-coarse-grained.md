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

### Model definition (not ReaxFF QM training) (A)

**C-GeM** assigns each atom a **positive core** plus a **Gaussian “electron shell”**; **shell** positions are **relaxed** in the field of fixed **nuclei** using **electronegativity**-linked **core–shell** energetics so the resulting **charge distribution** reproduces **molecular electrostatic potentials (ESP)** and **intermolecular** interactions without full **Kohn–Sham** solves at every **geometry**.

### Validation scenarios (C-style benchmarks)

Tests on **H/C/O/Cl** molecular sets compare **ESP** accuracy to references; selected **dissociation** cases (e.g. **HCl** in different environments) probe **qualitative** **ionic** vs **neutral** products.

### Molecular dynamics coupling (B)

**Not a production MD engine paper**—the emphasis is **fast ESP/interaction** evaluation as an alternative to **reactive charge equilibration** in some workflows.

## Findings

### Mechanisms / behavior

Reported **high** **ESP** accuracy on tested sets and **qualitatively correct** **HCl** dissociation behavior across environments; **sigma-hole**-like features can appear when **charge** is not strictly **atom-centered**, with **reduced** spurious **long-range** charge transfer vs some classical models.

### Limitations and scope

Validation set is **finite** (**H/C/O/Cl** in the Letter); coupling to **large** condensed-phase **MD** and broader **chemistries** is **not** demonstrated to the same level as **ReaxFF** **parameterization** studies.

## Limitations

Training/validation scope in the letter is finite (stated H/C/O/Cl set); transferability to broader chemistries and coupling to full MD for large condensed-phase systems is not the same problem as parametrizing ReaxFF. **JPCL** communications also compress **benchmark** tables—readers should pull **numerical** **targets** and **error** metrics from the **PDF** rather than from short wiki summaries. **C-GeM** is **not** interchangeable with **QEq** or **ACKS2** without checking **energy** **units**, **cutoffs**, and **minimization** **protocols** in the original implementation notes.

## Relevance to group

Methodological context for polarizable and charge-aware simulations adjacent to ReaxFF/QEq discussions; co-authors at Berkeley/LBNL, not a van Duin-group paper.

## Citations and evidence anchors

Primary: `papers/Others/C-GeM_Leven_2019.pdf` — abstract and validation discussion. https://doi.org/10.1021/acs.jpclett.9b02771

## Related topics

- [[2021itai-leven-j-chem-theor-recent-advances]]
- [[reaxff-family]]
