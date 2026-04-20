---
id: forcefield:reaxff-family
type: forcefield
title: "ReaxFF reactive force fields (group corpus scope)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Abstract"
    note: "LATP solid electrolyte parameterization and ionic conductivity trends"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Abstract"
    note: "Organic carbonate electrolyte extension; Li0 vs Li+ behavior"
  - paper_id: "paper:2015yoon-carbon-99-20-atomistic-scale-simulations"
    section: "Abstract"
    note: "Graphene impact mechanics with reactive C / projectile chemistry"
aliases:
  - "ReaxFF"
related_ids:
  - "material:graphene-nanocarbon"
  - "concept:batteries-interfaces-reaxff"
applies_to:
  - "material:graphene-nanocarbon"
evaluates: []
---

<!-- id:forcefield:reaxff-family -->

## One-paragraph summary

**ReaxFF** is the bond-order-based reactive force field used throughout much of this corpus for systems where bonds break and form, from **oxide ceramics and alloys** to **organic electrolytes**, **2D carbon**, and **MOF/ZIF** chemistries at elevated temperature or under mechanical load. The wiki treats “ReaxFF” as a *family* of parameterizations fit to quantum data and validated for specific element ranges; coverage is not universal and must be checked paper-by-paper.

## Functional form and training data

ReaxFF expresses energies via bond orders derived from interatomic distances, enabling continuous formation and rupture of bonds without preset connectivity. Parameter sets are trained to DFT (and sometimes experiment) for subsets of chemistry; the group’s publications typically document training reactions, equations of state, and barrier data used in the fit (see cited papers).

## Applicable materials and elements

Depends on the specific parameterization: examples in this repository include **NASICON-type LATP** electrolytes, **Li–organic electrolyte** species, **Ni–O** metal oxidation, **Fe–Al–Ni** alloys, **BaTiO3** ferroelectrics, **hydrocarbon / fuel** pyrolysis, and **graphene / nanocarbon** under extreme mechanics.

## Known limitations and failure modes

Transferability is limited to chemistries represented in training; quantitative rates and conductivities may require validation against experiment or higher-level theory. Some studies explicitly discuss known FF weaknesses (e.g., moderate-strain elasticity of carbon allotropes) while still using ReaxFF for the relevant coupled chemistry.

## Validation benchmarks

Illustrative validation hooks referenced in `source_refs`: ionic conductivity trends for LATP; DFT alignment for electrolyte initiation energetics; qualitative \(E_p^\*\) behavior for graphene impact.

## Related parameterizations and software

Group workflows commonly pair ReaxFF with **LAMMPS**-style MD and, where noted, hybrid Monte Carlo / MD schemes for electronic-state or stoichiometry sampling.

## How the group uses ReaxFF (corpus-level pattern)

Across the wiki, **ReaxFF** is the default when **bond topology changes** during a simulation: **solid electrolytes**, **liquid electrolytes at reducing electrodes**, **metal oxidation**, **hydrocarbon pyrolysis**, **graphene impact**, and **MOF** frameworks at high temperature. Papers rarely treat the FF as a black box—most document **which elements** are covered and **which observables** were used for sanity checks (ionic conductivity trends, qualitative barrier ordering, mechanical response).

## Relationship to other methods in the KB

- **Classical non-reactive** models appear where connectivity is fixed; the KB still cites ReaxFF where **reactions** gate the science question.  
- **MLIPs** and **JAX-differentiable** variants are indexed under [[theme-ml-atomistic-potentials]] and [[reaxff-vs-mlip-accuracy]].  
- **Parameterization discipline** is summarized in [[reaxff-parameterization-workflow]].

## Cross-links (navigation)

- Battery-facing work: [[batteries-interfaces-reaxff]].  
- Oxide / silica / Ni oxidation: [[theme-oxides-silica-ceramics]].  
- Catalysis: [[theme-catalysis-surfaces]].  
- Pyrolysis / fuels: [[theme-pyrolysis-combustion-organics]].  
- 2D carbon mechanics: [[graphene-nanocarbon]].

## Key references

- See `source_refs` for entry points; browse [`papers/index.md`](../papers/index.md) for the full parameterization bibliography.
