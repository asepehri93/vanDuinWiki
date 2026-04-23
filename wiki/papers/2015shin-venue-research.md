---
id: paper:2015shin-venue-research
type: paper
title: "Development of a ReaxFF reactive force field for Fe/Cr/O/S and application to oxidation of butane over a pyrite-covered Cr2O3 catalyst"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.5b01766"
year: 2015
authors:
  - "Yun Kyung Shin"
  - "Hyunwook Kwak"
  - "Alex V. Vasenkov"
  - "Debasis Sengupta"
  - "Adri C. T. van Duin"
venue: "ACS Catal."
pdf_sha256: "18e2ffbb2b57550408f9326be26c56501d9f1dc14f81ce8fcb6ffd7d8d2df7b2"
pdf_path: "papers/Shin_ACS_Catalysis_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015shin-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. Definitive protocol tables and numbers remain in the **PDF** / [[2015shin-venue-microsoft-word]] SI package.

## Summary

Shin *et al.* develop a **ReaxFF** parametrization for **Fe/Cr/O/S** against **QM** data and apply it to **reactive MD** of **butane** oxidation on **Cr oxide** surfaces, comparing **clean chromia** with **pyrite (FeS₂)**-modified models motivated by **coal-derived fuels** and **slagging** mineralogy. At **1600 K** (abstract), simulations highlight **surface oxygen species** that drive **dehydrogenation** to **radicals** and subsequent **C–O** coupling, producing **CH₂O** as a major partial-oxidation product on **clean** surfaces while **FeS₂** accelerates **complete oxidation** to **CO** and **CO₂** with **surface reconstruction** and **SOH** release pathways.

## Methods

**Force-field training.** **Scope:** new **Fe/Cr/O/S** cross-terms within **ReaxFF**, parametrized against **QM** energies/reaction data for **oxide**, **sulfide**, and **hydrocarbon** motifs relevant to **Cr–O**, **Fe–S**, and **S–O** chemistry (Computational Methods + SI). **QM reference level, training set composition, optimizer, and weighting:** **`pdf_path`** and SI tables.

**MD application (surface oxidation).** **System chemistry:** **butane + O₂** reacting on **Cr₂O₃** slabs with optional **FeS₂** patches (initial layouts summarized in SI captions; main text defines slab stoichiometries). **Temperature:** headline oxidation trajectories at **1600 K** (abstract). **Engine**, **timestep**, **thermostat**, **duration** (**ps**/**ns**), **PBC**, and any **NPT** segments are specified in **Computational Methods** on `pdf_path` (not enumerated on this page from the short abstract excerpt). **Electric field / enhanced sampling:** **N/A** in the abstract framing. **Barostat:** **N/A** unless Methods explicitly add **NPT** for these combustion-style runs (see `pdf_path`).

**Static QM / DFT:** **QM** enters as **training/validation** for ReaxFF, not as standalone **AIMD production** for the headline **1600 K** catalytic trajectories.

## Findings

**Clean Cr oxide:** **Dehydrogenation** initiated by **surface oxygen** yields **butane radicals** and **surface OH**; radical intermediates form **C–O** bonds or **C=C** when neighboring carbons dehydrogenate, producing **light alkenes**; **CH₂O** is the major partial oxidation product on **clean** surfaces under the simulated conditions (abstract).

**Pyrite-modified oxide:** **FeS₂** accelerates **complete oxidation** to **CO₂** and **CO**; **surface reconstruction** by pyrite is proposed as the origin of the **selectivity** shift (abstract). **SOH** release appears on the **modified** surface whereas **clean** surfaces favor **reoxidation** via **H₂O** desorption and **O₂** adsorption at **vacancies** in the abstract’s mechanistic sketch.

**Sensitivity:** The abstract frames results at **1600 K** “combustion-like” conditions; lower-temperature **ODH** relevance is not claimed there.

## Limitations

**Single high-temperature window** in the abstract is far from many industrial **ODH** conditions. **ReaxFF** cannot subsume all **electronic redox** subtleties of **sulfide–oxide** interfaces without targeted validation.

## Relevance to group

Illustrates **multi-element ReaxFF parameterization** for **sulfur-bearing fossil-catalyst** chemistries central to Shin/van Duin collaborations.

## Citations and evidence anchors

- DOI `10.1021/acscatal.5b01766`; `papers/Shin_ACS_Catalysis_2015.pdf`.
- `normalized/extracts/2015shin-venue-research_p1-2.txt`.

## Related topics

- [[2015shin-venue-research-2]]
- [[2015shin-venue-microsoft-word]]
- [[reaxff-family]]
