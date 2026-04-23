---
id: paper:2016islam-venue-research
type: paper
title: "eReaxFF: A pseudoclassical treatment of explicit electrons within reactive force field simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:ereaxff
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00432"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Grigory Kolesov"
  - "Toon Verstraelen"
  - "Efthimios Kaxiras"
  - "Adri C. T. van Duin"
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "c2feb5c0bfd1a201db42d45ec6f24537ed02aa74a59b49ca4adb27c0a67be038"
pdf_path: "papers/Islam_JCTC_eReaxFF_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:method-development
  - keyword:charge-equilibration
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
---
<!-- id:paper:2016islam-venue-research -->

## Summary

Same **J. Chem. Theory Comput.** article as **`[[2016islam-venue-ct6b00432]]`** (DOI `10.1021/acs.jctc.6b00432`): **eReaxFF** augments **ReaxFF** with **pseudoclassical explicit electrons**, integrates **ACKS2** charging, trains on **electron affinities**, and benchmarks **MD** against **Ehrenfest** dynamics for hydrocarbon radicals. The abstract claims large speedups over **quantum chemistry dynamics** while keeping most **literature ReaxFF** parameters fixed during the explicit-electron extension.

## Methods

Same article as [[2016islam-venue-ct6b00432]] (DOI `10.1021/acs.jctc.6b00432`). This slug’s `pdf_path` is an **ACS proof** export (`papers/Islam_JCTC_eReaxFF_2016_proof.pdf`); pagination may differ from the version-of-record PDF on [[2016islam-venue-ct6b00432]].

**MD application.** Section IV.A uses **molecular dynamics** in **NVT** relaxation at **1 K**, then **NVT** production at **400**, **500**, and **600 K** with a **Berendsen** thermostat (**100 fs** damping), **0.1 fs** timestep, and **velocity Verlet** on **C₁₂H₁₉•** and **C₁₄H₂₃•** hydrocarbon radicals (stoichiometry per formulas) with explicit excess electrons, compared to **Ehrenfest** references. **Boundary** conditions are gas-phase isolated radical models without **NPT** barostats or applied electric driving; segment lengths follow Figures 3–4 and Section IV.A (multi‑ps evolution).

**Force-field training.** **eReaxFF** augments ReaxFF with explicit Gaussian electrons and **ACKS2** charging (Section II). A successive one-parameter search fits electron affinities across bonding classes while freezing most literature ReaxFF parameters. **M06-2X/aug-cc-pVTZ** in **Jaguar 7.5** provides spot checks where **eReaxFF** and experiment disagree (Section III).

**Standalone static QM study.** **N/A** — DFT supports EA training and validation only.

## Findings

**eReaxFF** reproduces qualitative EA trends versus experiment for the training set while standard ReaxFF fails many of the same targets (Figure 2). MD captures electron transfer along the conjugated–aliphatic–radical pathway for **C₁₂H₁₉•** at **400–600 K**, with faster hopping at higher temperature (Section IV.A). Benchmarks include experiment, Ehrenfest dynamics, and DFT spot checks. The authors note that quantum calculations delocalize the added electron more than the pseudoclassical carriers and position **eReaxFF** as a scalable alternative to expensive time-dependent DFT dynamics.

**Corpus honesty.** Prefer [[2016islam-venue-ct6b00432]] for version-of-record pagination.

## Limitations

Corpus file is an **ACS proof** PDF; cite **JCTC version-of-record** for final pagination.
- Pseudoclassical electrons are **not** full TD-DFT; accuracy is **method-dependent**.
- Explicit-carrier dynamics should be validated on a case-by-case basis when migrating parameters between chemistries, because redox environments can stress pieces of the ACKS2 coupling that were not included in the training targets highlighted in the abstract.

## Relevance to group

Foundational **eReaxFF** methods paper from the **van Duin** collaboration—prerequisite reference for [[2016islam-venue-jp6b08688]] and later **battery interface** studies.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.6b00432](https://doi.org/10.1021/acs.jctc.6b00432) — *J. Chem. Theory Comput.* **12**, 3463–3472 (2016).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[2016islam-venue-jp6b08688]]

## Reader notes (navigation)

- **JCTC** **eReaxFF** methods article (DOI `10.1021/acs.jctc.6b00432`); battery **application**: [[2016islam-venue-jp6b08688]].
