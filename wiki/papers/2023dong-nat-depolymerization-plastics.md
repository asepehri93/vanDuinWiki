---
id: paper:2023dong-nat-depolymerization-plastics
type: paper
title: "Depolymerization of plastics by means of electrified spatiotemporal heating"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:thermal-decomposition
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41586-023-05845-8"
year: 2023
authors:
  - "Qi Dong"
  - "Aditya Dilip Lele"
venue: "Nature"
pdf_sha256: "307683b8ce1ce63a998813cc415de5fc747be507c6fdcbef3b02c0c07881c3f9"
pdf_path: "papers/ReaxFF_others/Dong_Lele_Nature_depolymerization_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023dong-nat-depolymerization-plastics -->

## Summary

The authors report **catalyst-free** thermochemical **depolymerization** of commodity **polypropylene (PP)** and **poly(ethylene terephthalate) (PET)** using **electrified spatiotemporal heating (STH)**: a **spatial temperature gradient** through a **bilayer porous carbon felt** stack combined with a **pulsed** temporal heating profile that reaches high peak temperatures for short intervals, aiming to favor monomer-forming pathways over equilibrium side products. The *Nature* abstract emphasizes a **far-from-equilibrium** pyrolysis strategy that avoids **catalyst** durability issues while using **spatial** and **temporal** control jointly: the **felt** stack sustains **continuous melting, wicking, vaporization, and reaction** as plastic traverses hotter regions, while **short** high-**T** pulses (example **~0.11 s** on-time discussed for **~600 °C** peaks in the PP-focused illustration) limit time at temperature to suppress unwanted **deep** cracking/aromatization chemistry.

## Methods

### Experimental reactor engineering (no atomistic MD in the main claim)

- **STH stack:** **Bilayer porous carbon felt**—**electrically heated** top layer + lower **reaction** layer—above a **solid plastic** reservoir, mounted in a **quartz tube** (**~10.5 mm** **inner diameter**) with **Ar** carrier gas and **Cu** **electrode** connections (see **Nature** figures).
- **Spatial control:** **Vertical temperature gradient** drives **melt**, **wicking**, **vaporization**, and **reaction** as material traverses hotter regions of the felt.
- **Temporal control:** **Pulsed current** produces short **high-T** peaks (**~600 °C** for **PP**-focused discussion; **~1050 °C** for **PET** in schematic text) with example **0.11 s on / 0.99 s off** programmes and rapid **inter-pulse** cooling to suppress **deep cracking**/**aromatization** equilibration.

### Product analytics

**Gas-phase** (and related) **effluent** analysis for **monomer** **yields** and **byproduct** distributions (**Methods** / **Extended Data** in the article).

## Findings

### Monomer yields (authors’ reporting)

- **PP → propylene:** **~36%** **monomer yield** (non-catalytic **STH**), higher than **conventional pyrolysis** benchmarks cited in the paper for **PP**.
- **PET → terephthalic-acid monomer:** **~43%** yield along the targeted route vs **conventional pyrolysis** comparisons summarized by the authors.

### Concept and sustainability framing

**STH** is demonstrated as **catalyst-free** in the main story—performance comes from **spatiotemporal** **T–t** control. The authors discuss **renewable electricity** integration and **CO₂ intensity** comparisons in supporting analysis.

The opening summary in *Nature* positions **STH** as a potential contributor to **plastic waste** mitigation by improving **monomer** recoveries from **PP** and **PET** without relying on **heterogeneous catalysts**, while still acknowledging broader **collection**, **sorting**, and **scale-up** challenges beyond this laboratory demonstration.

## Limitations

Yields and selectivities depend on the specific pulse programme and reactor geometry; scale-up and feed variability are not fully captured in a single laboratory demonstration.

## Relevance to group

Co-authored by **Aditya Dilip Lele** (Princeton) with ties to the group’s broader **reactive systems** network; paper is **experimental thermochemistry** rather than ReaxFF-centric, but catalogued here for **corpus linkage** to plastics depolymerization.

## Citations and evidence anchors

- DOI: [10.1038/s41586-023-05845-8](https://doi.org/10.1038/s41586-023-05845-8)

## Related topics

- [[2023dong-nat-depolymerization-plastics-2]]
