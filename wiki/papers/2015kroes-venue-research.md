---
id: paper:2015kroes-venue-research
type: paper
title: "Atom vacancies on a carbon nanotube: to what extent can we simulate their effects?"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:dft-static
  - task:validation
  - material:graphene-carbon-nano
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jctc.5b00292"
year: 2015
authors:
  - "Jaap M. H. Kroes"
  - "Fabio Pietrucci"
  - "Adri C. T. van Duin"
  - "Wanda Andreoni"
venue: "Journal of Chemical Theory and Computation (see DOI; ASAP header in extract)"
pdf_sha256: "660d367b29ad38918cbf1afd9bf0533552ee1a069f8c19c7fc7fa976650c734c"
pdf_path: "papers/Kroes_JCTC_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015kroes-venue-research -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Kroes *et al.* benchmark **single- and double-vacancy** physics in a **(10,0) zigzag carbon nanotube** across **DFT** (PBE, BLYP, partial PBE0 repeats) and several **classical** potentials (**AIREBO**, **LCBOP**, **ReaxFF15**, **Tersoff**, with **REBO** mentioned for SI). Quantities compared include **formation energies**, **relaxed structures**, and **barriers** for **reconstruction**, **migration**, and **vacancy coalescence**. The abstract warns that **characterization of these processes differs markedly** across methods, motivating cautious use of classical carbon models when building **DFT-informed** parametrizations. **ReaxFF15** is highlighted as a modern reactive carbon parametrization included in the comparison suite.

## Methods

- **Plane-wave pseudopotential DFT** via **CPMD** for nanotube supercells (Γ-only sampling noted).
- **Classical potentials** evaluated on the same defect motifs with convergence checks on supercell sizes (special attention to a **5r8r5r-Z** double-vacancy case).

## Findings

- Some **long-ranged relaxations** require large cells for both **DFT** and **ReaxFF** in specific double-vacancy configurations described in the extract.


## Limitations

- Benchmark scope is a **single chirality/diameter** nanotube; transferability of conclusions to **metallic** tubes or **wide** diameter regimes is not established here.
- ASAP header placeholders appear in the extract; use **DOI** for bibliographic certainty.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties the benchmark to **ReaxFF carbon** quality control and cross-method uncertainty quantification important for downstream **reactive carbon** applications.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jctc.5b00292](https://doi.org/10.1021/acs.jctc.5b00292)

## Related topics

- [[reaxff-family]]
