---
id: paper:2025ken-ichi-nomura-j-phys-chem-allegro-fm-toward
type: paper
title: "Allegro-FM: Toward an Equivariant Foundation Model for Exascale Molecular Dynamics Simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:methods-software
  - material:cement-mineral
  - method:ml-potential
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:method-development
  - keyword:gpu-md
doi: "10.1021/acs.jpclett.5c00605"
year: 2025
authors:
  - "Ken-ichi Nomura"
  - "Shinnosuke Hattori"
  - "Satoshi Ohmura"
  - "Ikumi Kanemasu"
  - "Kohei Shimamura"
  - "Nabankur Dasgupta"
  - "Aiichiro Nakano"
  - "Rajiv K. Kalia"
  - "Priya Vashishta"
venue: "J. Phys. Chem. Lett. 2025, 16, 6637–6644"
pdf_sha256: "a2512dd39503d6660d0a2c798d11974851c722acc392e4bf7eaf280522b81952"
pdf_path: "papers/Others/allegro-fm-toward-an-equivariant-foundation-model-for-exascale-molecular-dynamics-simulations.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2025ken-ichi-nomura-j-phys-chem-allegro-fm-toward -->

## Summary

**Allegro-FM** is an **E(3)-equivariant** **Allegro**-type **neural** **network** trained on **merged** **organic** and **inorganic** **datasets** with **Total** **Energy** **Alignment** (**TEA**), aimed at **exascale** **molecular** **dynamics** spanning **reactions**, **mechanics**, and **dissolution** without **task**-specific **retraining** for every **benchmark**. The authors introduce Allegro-FM, marketed as a foundation-model machine-learning force field built on the strictly local Allegro architecture and trained by fusing large organic and inorganic corpora using the Total Energy Alignment (TEA) framework so that heterogeneous quantum-chemistry levels can be combined without regenerating every reference calculation. The abstract claims coverage across 89 elements, strong agreement with high-level quantum chemistry for structural, mechanical, and thermodynamic observables, and emergent skill on structural correlations, reaction kinetics, fracture, and solid–liquid dissolution despite not being explicitly trained on every downstream task. Benchmarks include the Transition-1x organic reaction set (including transition-state configurations) and reactive simulations of calcium silicate hydrate (tobermorite-11 Å) in water. Scaling tests report multi-billion-atom runs on the Aurora supercomputer with parallel efficiency 0.975. Prose below aligns with the abstract and `normalized/extracts/2025ken-ichi-nomura-j-phys-chem-allegro-fm-toward_p1-2.txt`; the corpus PDF is `papers/Others/allegro-fm-toward-an-equivariant-foundation-model-for-exascale-molecular-dynamics-simulations.pdf`.

## Methods

The model keeps Allegro’s strictly local, E(3)-equivariant architecture suited to large parallel MD. Training merges MPtrj and OFF23 organic and inorganic corpora through Total Energy Alignment so heterogeneous quantum-chemistry levels contribute without recomputing every reference from scratch. Validation includes Transition-1x (organic reactions with transition-state geometries) and reactive aqueous simulations of tobermorite-11 Å calcium silicate hydrate. The abstract reports multi-billion-atom scaling tests on the Aurora system with parallel efficiency 0.975.

## Findings

The abstract states 89-element coverage and agreement with high-level quantum references for structural, mechanical, and thermodynamic targets. It further claims emergent accuracy on structural correlations, reaction kinetics, mechanics, fracture, and solid–liquid dissolution tasks that were not each explicitly included in training. The locality of the network is cited as enabling the observed efficiency at extreme atom counts on Aurora-class hardware.

## Limitations

Allegro-FM is a machine-learned potential distinct from ReaxFF; retrieval agents should not conflate its training and error modes with bond-order reactive force fields without reading the methods and SI. Foundation-model claims depend on benchmark selection and TEA assumptions across theory levels.

## Relevance to group

Context for large-scale MLIP workflows adjacent to ReaxFF in the corpus; Nabankur Dasgupta appears as a coauthor but the work is not a van Duin-group ReaxFF study.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpclett.5c00605 — *J. Phys. Chem. Lett.* **16**, 6637–6644 (2025).

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
