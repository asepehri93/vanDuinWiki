---
id: paper:2013wheeler-venue-paper
type: paper
title: "A polarizable reactive force field for water to enable molecular dynamics simulations of proton transport"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:polarizable-ff
  - keyword:charge-equilibration
  - keyword:water-interfaces
  - keyword:method-development
canonical_tags:
  - domain:classical-ff-specialized
  - domain:water-silica-geo
  - method:classical-md
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4798457"
year: 2013
authors:
  - "Abhishek Asthana"
  - "Dean R. Wheeler"
venue: "The Journal of Chemical Physics"
pdf_sha256: "82ce2176da558b810538c867e9839deeaf154d0e6e1c3f95a0c0fe81cf72f5b0"
pdf_path: "papers/Others/Wheeler_ReactiveWater_JChemPhys_138_174502.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2013wheeler-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. This is a **custom polarizable reactive water model** (not ReaxFF).

## Summary

The authors build a **polarizable, reactive** water model for **proton transport** MD: **Coulombics** use a **diffuse charge density**; **bond making/breaking** and **vdW** are separate submodels; **fluctuating charges and dipoles** respond to the electrochemical environment. Most parameters come from **ab initio** data for an isolated water molecule. **Bulk liquid water** at room temperature reproduces key **thermodynamic and transport** checks in their tests. A preliminary **PT** run shows **multiple transfers** but **underestimates** the net rate by about **5×** vs experiment. The intent is to merge explicit bond rearrangement with polarizable electrostatics so that proton hopping is not hard-wired to fixed charge paths. The *J. Chem. Phys.* article positions the model class as a bridge between **fixed-charge** water models and **empirical valence bond** proton-transfer schemes.

## Methods

**1 — MD application (atomistic dynamics).** After defining the **polarizable reactive water** potential, the authors report **molecular dynamics** validation on **bulk liquid water** at **room temperature** and a **preliminary proton-transfer (PT)** study in which **multiple PT events** occur (`papers/Others/Wheeler_ReactiveWater_JChemPhys_138_174502.pdf`; abstract in `normalized/extracts/2013wheeler-venue-paper_p1-2.txt`). **Engine / code:** **N/A —** integration package not named in the indexed excerpt (confirm in **JCP** **Methods**—typically a classical **MD** code for **bulk** **H₂O**). **System size:** the **bulk** **liquid water** validation implies a finite **atom** count **periodic** **supercell** (exact **N** and **box** vectors in **`pdf_path`**). **PBC:** **three-dimensional periodic** **boundary** conditions are standard for the reported **bulk** **H₂O** **MD** in **JCP** **174502** unless the **Methods** specify otherwise. **Timestep:** **N/A —** not in the **p1–2** excerpt. **Duration:** **production** **MD** lengths are reported in **ps**/**ns** units in the article body (**N/A —** exact **ps/ns** not in the indexed excerpt). **Thermostat / ensemble:** **NVT**/**canonical** **MD** at **298–300 K** is the usual reporting convention for **ambient liquid water** validation in this paper class—confirm thermostat and target **T** in **`pdf_path`**. **Barostat:** **NPT** equilibration may precede **NVT** production for **density** (**N/A —** not confirmed in the excerpt). **Pressure:** **N/A —** no applied **GPa**/**bar** targets stated in the abstract excerpt. **Electric field:** **N/A —** not stated. **Replica / enhanced sampling:** **N/A —** not stated.

**2 — Force-field training.** The **interatomic model** is split into **electrostatics** (polarizable **diffuse charge density**), **bond making/breaking**, and a **van der Waals** submodel for **exchange–correlation** effects; **fluctuating charges and dipoles** respond to the electrochemical environment, with most parameters from **ab initio** data for an **isolated water molecule** (abstract-level description).

**3 — Static QM / DFT-only.** **N/A —** **MD** is used for validation and pilot **PT** statistics, not as a pure static **DFT** application paper.

## Findings

**Outcomes & mechanisms.** The abstract reports **good agreement** with **bulk liquid water** **thermodynamic and transport** properties at **room temperature** under their tests, while the **pilot PT study** **under-predicts** the **proton-transfer rate by a factor of ~5** relative to experiment despite observing **multiple transfer events**.

**Comparisons.** Explicit **experiment** comparison for **PT rate**; broader **literature** context on **Eigen/Zundel** and spectroscopic **PT** studies appears in the introduction of the **PDF**.

**Sensitivity & design levers.** **N/A at abstract resolution** beyond noting that **PT** kinetics are sensitive to cooperative **Grotthuss** rearrangements the model struggles to capture at experimental timescales.

**Limitations & outlook.** Prototype **PT** accuracy; extending to **electrodes**, **ions**, and **confinement** adds polarization physics beyond the highlighted isolated-molecule parameter sourcing.

**Corpus honesty.** This is a **custom polarizable reactive water** model (**not ReaxFF**); **`extraction_quality: partial`** reflects AIP boilerplate in the corpus extract header.

## Limitations

Prototype accuracy for PT rates; publisher wrapper text affects `extraction_quality` rating. Extending the reactive water framework to interfaces with ions, electrodes, or confinement introduces additional polarization physics not exhaustively covered by the isolated-molecule parameter fits highlighted in the JCP article.

## Relevance to group

Adjacent **aqueous reactivity** literature for comparing against **ReaxFF water** and **MS-EVB**-class approaches in proton studies. The polarizable-reactive split showcased here is conceptually parallel to later eReaxFF efforts even though the mathematical machinery differs, which helps place explicit-electron developments in historical context.

## Citations and evidence anchors

- DOI: [10.1063/1.4798457](https://doi.org/10.1063/1.4798457)
- Extract: `normalized/extracts/2013wheeler-venue-paper_p1-2.txt`

## Reader notes (navigation)

- Custom **polarizable reactive water** model (not ReaxFF); compare proton-transport framing with [[batteries-interfaces-reaxff]] and [[reaxff-family]] aqueous work.

## Related topics

- [[reaxff-family]]
