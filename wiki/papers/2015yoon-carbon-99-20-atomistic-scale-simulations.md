---
id: paper:2015yoon-carbon-99-20-atomistic-scale-simulations
type: paper
title: "Atomistic-scale simulations of the chemomechanical behavior of graphene under nanoprojectile impact"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2015.11.052"
year: 2015
authors:
  - "Kichul Yoon"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
venue: "Carbon, 99 (2016) 58–64"
pdf_sha256: "1bdb01e1fb2e05795b21499c8d4ef9451b37c4528178d902d0340806cfbf1f88"
pdf_path: "papers/Yoon_Carbon_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015yoon-carbon-99-20-atomistic-scale-simulations -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses ReaxFF to simulate supersonic impact of nanoscale silica and nickel projectiles on single-layer graphene, enabling bond-breaking chemistry at the projectile–graphene interface beyond fixed-bond carbon potentials. Reported penetration energies \(E_p^*\) are related to pre-crack deformation, defect content (mono-vacancies, grain boundaries), and projectile chemistry, including crack-edge structures such as pentagon–heptagon pairs during penetration. Simulated \(E_p^*\) values are compared with multilayer graphene experiments (Lee et al., Science 2014), supporting large energy absorption under extreme strain-rate loading.

## Methods

- **Reactive MD:** ReaxFF (C-2013 parameter set discussed in context of prior graphene studies) in LAMMPS-style large-scale impact simulations.
- **Systems:** Pristine and defective graphene sheets; SiO2 and Ni projectiles at supersonic initial velocities.
- **Analysis:** Crack topology, armchair vs zigzag edge counts, \(E_p^*\) from projectile kinetic energy loss vs mass.

Reactive impact simulations treat bond formation and rupture explicitly across the projectile–graphene interface; supersonic silica and nickel projectiles are compared under the protocols described in the primary article.

## Findings

ReaxFF reproduces chemomechanical coupling between Ni or silica projectiles and graphene, including fracture patterns that nonreactive carbon potentials omit. Simulated \(E_p^*\) magnitudes align with experimental trends; maximum deformation diameter before crack initiation correlates with \(E_p^*\). Defect content and projectile composition modulate crack morphology and energy uptake. Quantitative \(E_p^*\) from the simulations agrees in order of magnitude with Lee et al. (Science 2014) for multilayer graphene. During penetration, pentagon–heptagon pairs appear at crack edges, and edge reactivity depends on pre-crack deformation of graphene; defects and projectile identity shift the specific penetration energy \(E_p^*\).

## Limitations

- ReaxFF C-2013 tensile response differs from REBO families at moderate strain; the reported impact studies operate in large-strain fracture regimes where this parametrization was judged applicable in the original work.
- Direct comparison to experiment is indirect (multilayer experimental graphene vs simulated single-layer).

## Relevance to group

Demonstrates ReaxFF for **2D carbon under extreme mechanical loading** with van Duin group leadership—useful reference for reactive simulations of graphene in contact with metals/oxides.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2015.11.052](https://doi.org/10.1016/j.carbon.2015.11.052)
- Abstract and Methods: `normalized/extracts/2015yoon-carbon-99-20-atomistic-scale-simulations_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- Graphene fracture and reactive impact mechanics
- ReaxFF carbon (C-2013) for nanomechanics
