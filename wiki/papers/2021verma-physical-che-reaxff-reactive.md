---
id: paper:2021verma-physical-che-reaxff-reactive
type: paper
title: "ReaxFF reactive molecular dynamics simulations to study the interfacial dynamics between defective h-BN nanosheets and water nanodroplets"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - domain:water-silica-geo
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP00546D"
year: 2021
authors:
  - "Akarsh Verma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. 23, 10822–10834 (2021)"
pdf_sha256: "2c28fde33824b6e0b14ababd17f9b23037b1dff24d8c7ad7b50ef5abb5edd63c"
pdf_path: "papers/Verma_PCCP_BN_water_2021.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2021verma-physical-che-reaxff-reactive -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work develops a B/N/O/H **ReaxFF** description to study **vacancy-defective hexagonal boron nitride (h-BN)** in contact with **water**: interfacial structure, water dissociation near vacancies, layered water under confinement, fracture initiation at defects, temperature-dependent droplet behavior (including contact angle trends vs. temperature and pore size), and hydrogen-bond-driven water organization near functionalized pores. The work positions defective h-BN/water interfaces as relevant to filtration, desalination, and nanofluidic device contexts where both chemistry and mechanical failure matter.

## Methods

Reactive MD with ReaxFF (bond order + charge equilibration) for B/N/O/H; setups include water nanodroplets on defective sheets, confined water between sheets, and elevated-temperature trajectories to probe dynamics near pores.

The article further notes that this work develops a reactive force field (ReaxFF) to investigate the eﬀect of water molecules on the interfacial interactions with vacancy defective hexagonal boron nitride (h-BN) nanosheets by introducing parameters suitable for the B/N/O/H chemistry. Initially, molecular dynamics simulations were performed to validate the structural stability and hydrophobic nature of h-BN nanosheets. Simulations at elevated temperatures were carried out to explore the water molecule trajectory near the functionalized h-BN pores, and it was observed that the intermolecular hydrogen bonds lead to agglomeration of water molecules near these pores when the temperature was lowered to room temperature. The study was extended to observe the eﬀect of pore sizes and temperatures on the contact angle made by a water nanodroplet on h-BN nanosheets, and it was concluded that the contact angle would be less at higher temperatures and larger pore sizes.

## Findings

Pristine h-BN nanosheets are treated as structurally stable and hydrophobic in the validation-style discussion; near **boron/nitrogen vacancies**, water can dissociate with terminal N/B sites participating in H- and OH-containing products. Under compression between sheets, water **layers**; fracture can **nucleate from vacancy defects**. Simulations explore how **contact angle** depends on **temperature** and **pore size** (higher T and larger pores associated with smaller contact angles in the trends reported).


From the abstract: the water molecule dissociation mechanism in the vicinity of vacancy defective h-BN nanosheets was investigated, and it was shown that the terminal nitrogen and boron atoms bond with a hydrogen atom and hydroxyl group, respectively. Furthermore, it is predicted that the water molecules arrange themselves in layers when compressed in between two h-BN nanosheets, and the h-BN nanosheet fracture nucleates from the vacancy defect site. This study provides important information for the use of h-BN nanosheets in nanodevices for water desalination and underwater applications, as these h-BN nanosheets possess the desired adsorption capability and structural stability.

## Limitations

Parameter set is specific to B/N/O/H chemistry in this application window; quantitative agreement with experiment for contact angles and kinetics requires cross-checking against measurements and higher-level electronic structure where polarization and long-ranged electrostatics dominate.

## Relevance to group

Extends the group’s ReaxFF line to **2D BN defects + aqueous interfaces**, linking reactivity, mechanics, and nanoconfined water behavior relevant to collaborative work on BN-related synthesis and devices.

## Citations and evidence anchors

https://doi.org/10.1039/D1CP00546D — Abstract and Introduction (~pp. 1–2) frame motivation and ReaxFF validation stance; Results sections detail interfacial chemistry and droplet/contact-angle behavior.

## Related topics

- [[reaxff-family]]
- [[20220000-0002-1558-1560-x-reaxff-force]]