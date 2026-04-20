---
id: paper:2016rassoulinejad-mousav-venue-evaluation-copper
type: paper
title: "Evaluation of copper, aluminum, and nickel interatomic potentials on predicting the elastic properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:methods-software
  - method:classical-md
  - task:validation
  - material:alloy-bulk
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4953676"
year: 2016
authors:
  - "Seyed Moein Rassoulinejad-Mousavi"
  - "Yijin Mao"
  - "Yuwen Zhang"
venue: "J. Appl. Phys."
pdf_sha256: "b6ae7c5b4b19a1be8fa68071c41052abdb7bea921532021cceef71d643c49e79"
pdf_path: "papers/Others/NiAl_review.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2016rassoulinejad-mousav-venue-evaluation-copper -->

## One-paragraph summary

This **Journal of Applied Physics** study benchmarks **embedded-atom method (EAM)**-style **interatomic potentials** for **Cu**, **Al**, and **Ni** by computing **single-crystal elastic constants** \(C_{11}\), \(C_{12}\), \(C_{44}\) with **molecular dynamics** at room temperature and converting them to **polycrystalline moduli** via the **Voigt–Reuss–Hill** average. Potentials were taken from **NIST**, **Sandia**, and **LAMMPS** repositories; results are compared to **experimental** elastic data to recommend which parameterization is most reliable for each pure metal and elastic property. The work is **classical non-reactive MD** focused on **mechanical property** prediction rather than **ReaxFF** chemistry.

## Methods

- **Classical MD** with **EAM** potentials from public databases for **fcc Cu, Al, Ni** single crystals.
- Extraction of **\(C_{11}\), \(C_{12}\), \(C_{44}\)** and reduction to **bulk**, **shear**, **Young’s modulus**, and **Poisson’s ratio** using **VRH** averaging.

## Findings

- **Elastic moduli** are **sensitive to the specific potential** chosen; potentials fit for **alloys** may not transfer to **pure-element** elastic behavior.
- Tabulated **simulation vs experiment** comparisons support **screening potentials** before large-scale **nanomechanics** studies.

## Limitations

- **Room-temperature** focus; **temperature** and **size** effects in **nanowires** or **interfaces** may differ from bulk crystal benchmarks.
- The registered **PDF path** in the corpus manifest should be verified against the **JAP** article identity if sources are reconciled.

## Relevance to group

Provides **force-field benchmarking** context adjacent to **reactive** and **metallic** simulation workflows used in broader materials modeling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1063/1.4953676` (`papers/Others/NiAl_review.pdf` per manifest).

## Related topics

- [[reaxff-family]]
