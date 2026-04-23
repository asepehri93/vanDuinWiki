---
id: paper:2015srinivasan-venue-jp-2014-10274e
type: paper
title: "Development of a ReaxFF Potential for Carbon Condensed Phases and Its Application to the Thermal Fragmentation of a Large Fullerene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1021/jp510274e"
year: 2015
authors:
  - "Sriram Goverapet Srinivasan"
  - "Adri C. T. van Duin"
  - "P. Ganesh"
venue: "J. Phys. Chem. A"
pdf_sha256: "99937fa99c5893ef99d2eb59c080c62afc852c7eebf3d6791fe202ae3e0bcbe8"
pdf_path: "papers/Srinivasan_JPC_graphene_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015srinivasan-venue-jp-2014-10274e -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the article identified by `doi` and `pdf_path`. Sibling [[2015srinivasan-venue-research]] is a **proof** duplicate for the same work.

## Summary

Srinivasan, van Duin, and Ganesh introduce **ReaxFF C-2013**, a **reparametrization** of the **CHO** carbon subset using **DFT** data for **graphite** and **diamond** equations of state, **defect** and **amorphous** carbon energetics derived from **fullerene-related** structures, and related **condensed-phase** benchmarks. The abstract states that **ReaxFF C-2013** reproduces the **graphite atomization energy**, the **DFT graphite–diamond energy difference** and **graphite→diamond** transformation barrier, and the **DFT Stone–Wales barrier** in **C₆₀(Ih)** via concerted **C₂** rotation. **Reactive MD** of **C₁₈₀** shows **thermal fragmentation** whose decay is an **exponential function of time**; an **Arrhenius** fit to the decay rate gives an **activation energy of 7.66 eV** for **carbon loss**. **C₂** loss dominates, while probability of **larger fragment** loss grows with **temperature**. The work is positioned toward **coal pyrolysis**, **soot**, **graphitic nozzle erosion**, and **spacecraft ablation** modeling.

## Methods

**Force-field training.** The authors **reparametrize** the carbon subset of **ReaxFF CHO** against **DFT** data: **equations of state** for **graphite** and **diamond**, formation energies of **graphene defects** and **amorphous** carbon structures derived from **fullerene-related** configurations, and related **condensed-phase** benchmarks, yielding **ReaxFF C-2013** (abstract). **QM program, functional, basis, k-sampling, and least-squares weighting** for the fit are documented in **Computational methods** on `pdf_path`.

**Static QM / DFT.** The same **DFT** database supplies **Stone–Wales** barriers in **C₆₀(Ih)** (concerted **C₂** rotation), **graphite–diamond** energetics, and **graphite→diamond** transformation barriers used both as **training targets** and as **post-fit** checks (abstract).

**MD application (C₁₈₀ fragmentation).** **Reactive MD** uses **ReaxFF C-2013** on an isolated **C₁₈₀** fullerene (order **10³** carbon atoms) to study **thermal fragmentation** kinetics. **Temperature** is varied to build an **Arrhenius** plot of the decay rate (abstract). **Engine**, **timestep**, **thermostat**, **boundary conditions** (vacuum vs large periodic box), **equilibration vs production** segment lengths, and total **trajectory** time are tabulated in **`pdf_path`** and are **not** present in the short indexed excerpt. **Ensemble:** **NVT**-class **canonical** heating for the fragmentation campaigns as stated in Methods. **Barostat / hydrostatic pressure:** **N/A**. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

## Findings

**Force-field fidelity:** **ReaxFF C-2013** matches the quoted **DFT** benchmarks for **graphite/diamond** thermochemistry and the **C₆₀ Stone–Wales** barrier within the training scope summarized in the abstract.

**C₁₈₀ fragmentation:** Decay follows an **exponential** time law; **Arrhenius** analysis yields **7.66 eV** activation energy for **C atom loss** from the fullerene (abstract). **C₂** elimination is the **primary** channel, but **larger fragments** become **more probable** as **temperature** increases (abstract).

**Positioning:** The introduction ties **large fullerene fragmentation** to broader **pyrolysis / ablation** literature on **fullerene** decomposition mechanisms.

## Limitations

**Reactive FF** accuracy outside the **training** chemical space (e.g., oxygenated soot) needs separate validation. **Finite molecular models** do not replace **bulk graphite ablation** without extrapolation.

## Relevance to group

**PSU / ORNL** collaboration on **carbon ReaxFF** for **extreme-environment** carbon chemistry.

## Citations and evidence anchors

- DOI `10.1021/jp510274e` — `papers/Srinivasan_JPC_graphene_2015.pdf`.
- `normalized/extracts/2015srinivasan-venue-jp-2014-10274e_p1-2.txt`.

## Related topics

- [[2015srinivasan-venue-research]]
- [[reaxff-family]]

## Reader notes (navigation)

Proof duplicate: [[2015srinivasan-venue-research]].
