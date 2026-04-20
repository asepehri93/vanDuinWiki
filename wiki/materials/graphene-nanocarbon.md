---
id: material:graphene-nanocarbon
type: material
title: "Graphene and nanocarbon (simulation themes in this wiki)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2015yoon-carbon-99-20-atomistic-scale-simulations"
    section: "Abstract"
    note: "Supersonic projectile impact; fracture and specific penetration energy"
  - paper_id: "paper:2015surwade-nat-water-desalination"
    section: "Opening sections"
    note: "Experimental nanoporous graphene membranes for desalination (context for 2D nanopores)"
  - paper_id: "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
    section: "Abstract"
    note: "Large-scale carbonaceous chemistry (coal model); complementary carbon chemistry theme"
aliases:
  - "graphene"
  - "single-layer graphene"
related_ids:
  - "forcefield:reaxff-family"
applies_to: []
evaluates: []
---

<!-- id:material:graphene-nanocarbon -->

## One-paragraph summary

**Graphene** appears in this knowledge base both as a **mechanics and fracture** problem under extreme loading (reactive MD) and as a **membrane / nanopore** platform for separations (experimental). Related **sp2 carbon** chemistry also appears in large-scale **pyrolysis** simulations of complex hydrocarbon solids. The material page ties these threads together without collapsing distinct physical models (ReaxFF impact simulations vs experimental porous membranes).

## Structure and composition notes

Single-layer graphene: hexagonal sp2 carbon network; defects (vacancies, grain boundaries) modify fracture and reactivity. Nanoporous graphene for separations introduces edge chemistry and pore size distributions not captured by pristine sheets.

## Properties relevant to group research

- **Mechanics:** high strength and strain-to-failure under impact; specific penetration energy metrics vs experiments.
- **Transport:** selective water vs ion transport through nm pores (experimental literature cited in Surwade et al.).

## Force fields and parameterizations

Reactive **ReaxFF** studies of graphene often use carbon parameters discussed in the impact paper (`paper:2015yoon-carbon-99-20-atomistic-scale-simulations`), with caveats about elastic nonlinearity vs REBO-like models for some tensile properties.

## Prior simulation protocols

Large nonequilibrium MD for projectile impact; contrasting quasi-static tension is discussed in the same reference set.

## Mechanics vs separations (two literatures)

The wiki intentionally keeps **supersonic impact** simulations ([[2015yoon-carbon-99-20-atomistic-scale-simulations]]) distinct from **experimental nanoporous membranes** for **desalination** ([[2015surwade-nat-water-desalination]]): the former probes **bond-breaking** carbon mechanics; the latter documents **pore statistics** and **transport** measurements that atomistic models may only approximate.

## Links to carbon chemistry at larger scale

**Pyrolysis** and **coal** models ([[2014castro-marcano-journal-of-a-pyrolysis-large-scale]]) share **sp2/sp3** carbon chemistry with graphene studies but operate on **disordered** macroscopic solids—see [[theme-pyrolysis-combustion-organics]].

## Broader navigation

- [[themes-index]] — all theme hubs.  
- [[theme-water-silica-geo]] — aqueous confinement adjacent to 2D pores.

## Key references

- [[2015yoon-carbon-99-20-atomistic-scale-simulations]]
- [[2015surwade-nat-water-desalination]]
- [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] (coal / carbonaceous reactivity context)
