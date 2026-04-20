---
id: paper:2019liu-j-phys-chem-formation-alfx
type: paper
title: "Formation of AlFx Gaseous Phases during High Temperature Etching: A Reactive Force Field Based Molecular Dynamics Study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - material:oxide
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.9b03957"
year: 2019
authors:
  - "Yongli Liu"
  - "Yang Qi"
  - "Xianwei Hu"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 123:16823-16835 (2019)"
pdf_sha256: "bf9a5e02f4dd35b3e74d1360d81465ab696811f32921e1092cbe255e977f654f"
pdf_path: "papers/Liu_AlF_etching_JPCC_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019liu-j-phys-chem-formation-alfx -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work develops a ReaxFF parameterization for Al–F interactions fitted to QM-derived training data for gaseous AlFx species and Al–F crystal phases, then apply it to reactive MD of high-temperature etching. Simulations scan fluorine source strength (F/Al = 1–6) and temperature (1000–1500 K), resolving how gaseous AlFx products emerge in a multi-step sequence. A critical F/Al ratio near 3 separates regimes where clustered AlFx remains largely nonvolatile from a “fifth step” regime producing isolated gas-phase species such as AlF4, AlF5, and AlF6 with more favorable formation energies.

## Methods

ReaxFF development against QM structures, equations of state, and energetics for Al–F systems. Reactive MD at high temperature with varied F/Al and temperature; analysis of reaction sequences and gaseous product formation.

## Findings

ReaxFF reproduces the training QM data well. Below F/Al ≈ 3 the chemical driving force is insufficient for full volatilization of certain AlFx phases; above it, additional steps yield gaseous AlFx. Temperature and inferred discharge/voltage effects are discussed as secondary levers on product quantities.


## Limitations

Specific to Al–F high-temperature etching chemistry; plasma and reactor-level transport are not resolved. Parameter set should be checked before transfer to unrelated Al chemistry.

## Relevance to group

van Duin co-authorship; demonstrates ReaxFF for halide etching and multicomponent gas-phase speciation relevant to processing and preparative Al–F chemistry.

## Citations and evidence anchors

`papers/Liu_AlF_etching_JPCC_2019.pdf` — abstract (mechanism summary, F/Al = 3 threshold), methods for FF training. https://doi.org/10.1021/acs.jpcc.9b03957

## Related topics

- [[reaxff-family]]