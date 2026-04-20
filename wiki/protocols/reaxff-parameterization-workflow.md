---
id: methodprotocol:reaxff-parameterization-workflow
type: methodprotocol
title: "ReaxFF parameterization workflow (literature-shaped checklist)"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, task:validation, scale:atomistic]
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Example of electrolyte-focused training and validation"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    note: "Organic electrolyte bond types and Li speciation"
aliases: []
related_ids:
  - "forcefield:reaxff-family"
  - "concept:theme-ml-atomistic-potentials"
applies_to:
  - "forcefield:reaxff-family"
evaluates: []
---

<!-- id:methodprotocol:reaxff-parameterization-workflow -->

!!! abstract "For readers"

    This is a **high-level checklist** distilled from how **group publications** describe **QM training**, **validation**, and **simulation deployment**—not a substitute for software manuals (e.g. **LAMMPS**, **PuReMD** ecosystem).

## One-paragraph summary

Successful **ReaxFF** projects in this KB typically: (1) define **target chemistries** and **phases**; (2) build **QM datasets** for **bond formation/dissociation** and **equations of state**; (3) fit **bond-order parameters** and screen **unphysical minima**; (4) validate with **macroscopic** observables (conductivity, mechanical response) where available; (5) document **limitations** honestly.

## Prerequisites

- **QM engine** access for training data (DFT level documented per paper).  
- **MD engine** supporting ReaxFF (**LAMMPS** common in corpus).  
- **Expertise** in the **application domain** to choose reactions that matter.

## Steps

1. **Scope chemistry:** list elements and **forbidden** extrapolations (see [[transferability-reactive-ff]]).  
2. **Select training reactions:** include **barriers** and **phases** relevant to the target application ([[2018shin-physical-che-development-reaxff]], [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]).  
3. **Fit and freeze** parameters; run **short MD** sanity checks for **energy drift** and **unphysical products**.  
4. **Validate** against **experimental** or **higher theory** metrics reported in the paper (conductivity trends, etc.).  
5. **Publish** training scope alongside results—KB pages rely on this for the `confidence` field in paper frontmatter.

## Expected outputs and checks

- **Stable** MD without explosions for intended **T** and **density**.  
- **Qualitative** agreement with **DFT** on sampled **reaction coordinates**.  
- **Documented** failure modes when data are **partial** (`extraction_quality` in paper frontmatter).

## Pitfalls and troubleshooting

- **Missing reaction class** in training → spurious products; add QM data.  
- **Phase change** not sampled → bad **melting** or **glass** behavior.  
- **Electrolyte** chemistry: distinguish **Li0** vs **Li+** pathways ([[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]).

## Key references

- [[reaxff-family]]  
- [[batteries-interfaces-reaxff]]  
- [[2018shin-physical-che-development-reaxff]]  
- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]  
