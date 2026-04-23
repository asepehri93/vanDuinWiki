---
id: paper:2016islam-venue-ct6b00432
type: paper
title: "eReaxFF: a pseudoclassical treatment of explicit electrons within reactive force field simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - method:reaxff
  - task:method-development
  - domain:methods-software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00432"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Grigory Kolesov"
  - "Toon Verstraelen"
  - "Efthimios Kaxiras"
  - "Adri C. T. van Duin"
venue: "J. Chem. Theory Comput."
pdf_sha256: "785eb9c8dcbbf11351c7d9a2752ab2578ebc90aafd32285836069df87d45b0c8"
pdf_path: "papers/Islam_JCTC_eReaxFF_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016islam-venue-ct6b00432 -->

## Summary

The paper introduces **eReaxFF**, extending **ReaxFF** with **pseudoclassical explicit electrons** (and holes) while retaining the bond-order reactive framework. **ACKS2** (atom-condensed Kohn–Sham DFT to second order) is integrated for charge-related quantities. The authors train the extension so that **electron affinities (EAs)** of saturated, unsaturated, and radical species track experiment and selected **DFT** checks, then illustrate **explicit-electron molecular dynamics** on conjugated hydrocarbon radicals and compare to **Ehrenfest** reference dynamics. The abstract emphasizes **orders-of-magnitude** cost reduction relative to **quantum chemistry dynamics** and states that **literature ReaxFF parameters** largely transfer into **eReaxFF** with optimization focused on explicit-electron-related terms.

## Methods

**MD application (Section IV.A).** Two conjugated hydrocarbon radicals, **C₁₂H₁₉•** and **C₁₄H₂₃•**, carry an extra electron on the conjugated segment to mimic an excited state. After **NVT** relaxation at **1 K**, **NVT** production runs at **400**, **500**, and **600 K** use a **Berendsen** thermostat (**100 fs** damping), **velocity Verlet** integration, and **Δt = 0.1 fs**, probing temperature-driven electron migration among the conjugated chain, aliphatic linker, and radical site; the same setups are compared to **Ehrenfest** reference dynamics. Section IV.A and Figures 3–4 discuss **multi‑ps** evolution of energy and charge localization rather than a single headline production length. Gas-phase radical models do not use **NPT** barostats, applied electric fields, or bias-based enhanced sampling in the protocol described. Boundary conditions are not spelled out on the opening pages summarized here; the indexed **JCTC** text does not name a commercial MD package.

**Force-field formulation and training.** **eReaxFF** retains the standard ReaxFF bonded and nonbonded decomposition while adding explicit electron–nuclear couplings for pseudoclassical carriers and integrating **ACKS2** for charge-related quantities (Sections I–II). Training targets electron affinities across bonding classes; a successive one-parameter search minimizes weighted squared error against literature EA data, adjusting only explicit-electron-related parameters (including Gaussian electron width) while leaving the bulk of literature ReaxFF parameters fixed. **M06-2X/aug-cc-pVTZ** calculations in **Jaguar 7.5** provide spot checks for selected unsaturated species where **eReaxFF** and experiment disagree, showing DFT also underestimates those EAs in the cases discussed.

**Static QM as a standalone campaign.** **N/A** — DFT supports EA training and validation only.

## Findings

The abstract reports qualitatively correct electron affinities versus experiment for the training set and good agreement between **eReaxFF** MD and **Ehrenfest** dynamics for the radical demonstrations, while conventional ReaxFF fails many of the same EA targets (Figure 2). Section IV.A describes how temperature changes the timescale for electron migration from the polyacetylene-like segment toward the radical site, including transient localization on the aliphatic linker at elevated temperature; the **400 / 500 / 600 K** comparison for **C₁₂H₁₉•** illustrates thermally accelerated pathways that are rarer at lower temperature. The authors note that full quantum calculations delocalize the added electron more than the pseudoclassical treatment—an explicit limitation—and position **eReaxFF** as a large-scale alternative to costly time-dependent DFT nonadiabatic dynamics.

## Limitations

- **Pseudoclassical electrons** are not a full **quantum electronic** solution; accuracy limits near **conical intersections** and **strongly correlated** states must be monitored.
- **Parameter portability** still requires systematic validation per **chemically distinct** subsystem.

## Relevance to group

Landmark **method paper** from the **van Duin + Harvard + Ghent** collaboration defining **eReaxFF**, a cornerstone of the group’s **next-generation reactive FF** roadmap.

## Citations and evidence anchors

- Abstract and Sec. I in `papers/Islam_JCTC_eReaxFF_2016.pdf`; **DOI:** `10.1021/acs.jctc.6b00432`.

## Related topics

- [[reaxff-family]]
