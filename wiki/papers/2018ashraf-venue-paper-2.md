---
id: paper:2018ashraf-venue-paper-2
type: paper
title: "Application of ReaxFF-Reactive Molecular Dynamics and Continuum Methods in High-Temperature/Pressure Pyrolysis of Fuel Mixtures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: ""
year: 2018
authors:
  - "Chowdhury Ashraf"
  - "Sharmin Shabnam"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Book chapter proof, Computational Approaches for Chemistry Under Extreme Conditions (Springer)"
pdf_sha256: "b3b96dad42903ecfd08c122d5d5c9a966adc9a8da21fb5dd5a9de1d4f75ca218"
pdf_path: "papers/Ashraf_Sharmin_Chapter7_FuelMixtures_2019_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2018ashraf-venue-paper-2 -->

??? info "Corpus role"
    This slug registers a **Springer proof** PDF. Full chapter protocols and numerical results are curated on [[2018ashraf-venue-paper]] (annotated chapter PDF). `doi` is empty in front matter because the ingest targets a publisher workflow file rather than a resolved Crossref row.

## Summary

The registered PDF is a publisher proof for Chapter 7 in *Computational Approaches for Chemistry Under Extreme Conditions*, titled “Application of ReaxFF-Reactive Molecular Dynamics and Continuum Methods in High-Temperature/Pressure Pyrolysis of Fuel Mixtures.” The SpringerLink metadata captured in the extract states that rocket engines, gas turbines, and similar devices often exceed critical pressures of fuels or oxidizers, and that modeling combustion under such conditions is needed to build chemical kinetic models that remain valid when pressure is raised from low- to high-pressure regimes. The chapter abstract describes using ReaxFF molecular dynamics to study how a highly reactive fuel alters the behavior of a less reactive fuel as concentration, temperature, and density or pressure vary, comparing activation energies from Arrhenius-type rate laws to continuum simulations and discussing where simple first-order Arrhenius relations break down when initial reaction mechanisms and product distributions differ between the two fuels. Toluene and n-dodecane appear among the keywords in the extract as representative mixture components.

## Methods

Duplicate **Springer proof** ingest—protocol matches [[2018ashraf-venue-paper]]:

- **Engine / code:** **LAMMPS** **ReaxFF** **molecular dynamics** with **CHO-2016**-class parameters (chapter citation).
- **System size & composition:** **Periodic cubic** cells (**toluene**, **n-dodecane**, and mixtures) sized to **0.2** and **0.4 kg dm⁻³** targets with **40** molecules per neat species and **Table 7.1** compositions for blends (**atom** counts implicit in box lengths quoted on the canonical page).
- **Boundaries / periodicity:** **3D PBC** cubic boxes.
- **Ensemble:** **NVT** with **Berendsen** thermostat (**100 ps** damping cited on [[2018ashraf-venue-paper]]).
- **Timestep:** **0.1 fs** integration **timestep** throughout.
- **Duration:** **10 ps** equilibration at **1500 K**; **50–200 ps** **production** depending on species reactivity; mixture runs **200 ps** at **2000–2600 K** in **100 K** steps (canonical chapter).
- **Barostat:** **N/A — NVT** at fixed volume; continuum side uses matching **constant-volume** **isothermal** integration.
- **Temperature:** **1500 K** equilibration; **2000–2600 K** production sweeps (**K**).
- **Pressure:** Initial **pressures** **~26–75 MPa** over first **5 ps** of high-**T** runs as summarized on [[2018ashraf-venue-paper]] (real-gas **EOS** in continuum companion).

## Findings

The chapter identifies **pressure**–**temperature**–**mixing** regimes where simple **Arrhenius** kinetics fail because **initial mechanisms** and **product distributions** differ between fuels (**abstract**). **ReaxFF** **MD** plus **0D** **continuum** comparisons yield **activation energies** and mechanistic insight for **supercritical** mixtures where **experiments** are difficult—full plots and tables live on [[2018ashraf-venue-paper]] (**corpus honesty**: do not cite this **proof** PDF for fine numerical pagination).


## Limitations

Proof PDFs can differ in pagination and typography from the final Springer chapter. The extract is metadata- and abstract-heavy relative to full methods text. Prefer the version-of-record chapter or the primary wiki slug for citation-ready reading.

## Relevance to group

Penn State (Mechanical and Nuclear Engineering) van Duin-group chapter on high-pressure pyrolysis and multiscale coupling for fuels research.

## Reader notes (navigation)

- Canonical chapter summary and tables: [[2018ashraf-venue-paper]]
- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
