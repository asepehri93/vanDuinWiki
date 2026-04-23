---
id: paper:2017mortavazi-venue-paper
type: paper
title: "Strong thermal transport along polycrystalline transition metal dichalcogenides revealed by multiscale modeling for MoS₂"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:2d-materials
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:gpu-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.apmt.2017.02.005"
year: 2017
authors:
  - "Bohayra Mortazavi"
  - "Romain Quey"
  - "Alireza Ostadhossein"
  - "Aurelien Villani"
  - "Nicolas Moulin"
  - "Adri C. T. van Duin"
  - "Timon Rabczuk"
venue: "Appl. Mater. Today"
pdf_sha256: "9ca4fc8f43d182f10f6680816f103a5426952b3fb87959eda409109524d3b1b6"
pdf_path: "papers/Mortavazi_AMT_MoS2_thermal_proof_2017.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017mortavazi-venue-paper -->

!!! abstract
NEMD with ReaxFF grain-boundary thermal conductances feeds finite-element models of polycrystalline MoS₂ (and validation on graphene/h-BN) to report effective in-plane thermal conductivity vs grain statistics.

## Summary

This **uncorrected proof** matches the **Applied Materials Today** article on **multiscale thermal transport** in **polycrystalline MoS₂**. **Twenty** MoS₂ grain-boundary models (5–7, 4–4, 4–6, 4–8, 6–8 ring motifs from literature TEM/DFT references) span a range of defect concentrations. **Reactive NEMD** supplies **thermal conductance** across boundaries and pristine reference values; results upscaled through **finite-element** continuum meshes of polycrystalline films. The workflow is cross-checked against **graphene** and **h-BN** polycrystals (comparison to equilibrium MD noted in the discussion). **Adri C. T. van Duin** is a co-author on the ReaxFF side. The study is motivated by **thermal management** in **2D** **electronics**: **in-plane** **κ** of **TMD** films can fall sharply when **grain** sizes approach **device** dimensions, so **multiscale** coupling is presented as a way to connect **DFT/ReaxFF** **interface** conductances to **device-scale** **temperature** maps.

## Methods

**Force-field training / fitting.** **ReaxFF** for **MoS₂** is used as published (prior mechanical validation cited in the article); this contribution **does not** introduce a new QM refit.

**MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with **ReaxFF** drives **nonequilibrium molecular dynamics (NEMD)** on **~20** **MoS₂** **grain-boundary** supercells (see Fig. 1 inventory: **4–4**, **4–8**, **5–7**, **4–6**, **6–8** motifs, symmetric/asymmetric variants) plus **pristine single-layer** reference cells. **Boundaries / periodicity:** **In-plane periodic** models along the **grain-boundary** direction. **Timestep:** **Δt = 0.25 fs**. **Protocol / ensembles:** initial **room-temperature (~300 K) equilibration**; **end atoms fixed**; further **NVT** equilibration with a **Nose–Hoover thermostat**; production **NEMD** partitions the cell into **22 slabs** with **hot (310 K)** and **cold (290 K)** **NVT**-controlled end slabs (**ΔT = 20 K**) and **NVE** integration on the **interior 20 slabs** to reach **steady-state heat flux** \(J_x\) and extract **κ** via Fourier’s law (Eq. (2)) for pristine films, and **grain-boundary conductance** from the temperature drop at the interface (Eq. (3)). **Barostat / hydrostatic pressure:** **N/A —** no global **pressure** servo; the **NEMD** geometry instead establishes a **stress/flux** response consistent with fixed-end **thermal** biasing. **Thermostat summary:** **Nose–Hoover** during **NVT** equilibration; **NVT** hot/cold slabs during production **NEMD**; **NVE** in the interior slabs. **Electric field:** **N/A —** not applied. **Enhanced sampling:** **N/A —** direct **NEMD**. **Duration:** **N/A —** explicit **ns** totals are tied to prior protocol **[66]**/SI—confirm numerics on the **VOR** PDF.

**Static QM / DFT.** **Literature TEM/DFT** informs **GB** construction; **DFT** is **not** the thermal-transport calculator here.

**Review / non-simulation framing.** **FE** continuum models (**Neper** tessellations, **~10⁴** grains) upscale atomistic **conductances** to **device-scale** **effective κ** maps; **graphene** and **h-BN** benchmarks compare **NEMD+FE** vs **EMD**. **Corpus note:** this slug tracks an **uncorrected proof** PDF; use **`[[2017mortazavi-applied-mate-strong-thermal]]`** for the **version-of-record** bytes and pagination.

## Findings

**Outcomes & mechanisms.** **Reactive NEMD** yields **thermal conductances** for diverse **MoS₂** **grain boundaries** and **pristine** references; feeding those into **FE** meshes reproduces how **polycrystalline** microstructure suppresses **effective in-plane κ**, with especially strong reductions when **grain sizes** fall **below ~100 nm** in their models.

**Comparisons.** **Graphene** and **h-BN** **polycrystal** calculations contextualize the **multiscale** approach against **fully atomistic EMD** baselines as reported.

**Sensitivity & design levers.** **Non-uniform** grain-size distributions reroute **heat flux** compared with **uniform** approximations at similar averages—**texture** matters.

**Limitations & outlook (as authored).** **Phonon-limited** classical picture; **electronic** thermal transport omitted; **NEMD vs EMD** can shift absolute **κ**—see article discussion.

**Corpus / KB honesty.** Proof PDF; cite **`[[2017mortazavi-applied-mate-strong-thermal]]`** for authoritative tables after corpus alignment.


## Limitations

Proof PDF; absolute κ can differ between EMD and NEMD implementations as discussed; primarily relative trends for polycrystallinity. **Phonon** **isotope** **effects**, **substrate** **coupling**, and **electron–phonon** **transport** in **MoS₂** are outside the **classical** **ReaxFF** **NEMD** scope used here. **Interlayer** **thermal** **resistance** in **few-layer** **films** is another **degree** **of** **freedom** not exhaustively explored in the **proof** **extract**.

## Relevance to group

Group co-authorship; couples **ReaxFF** transport data to **continuum** device-scale predictions.

## Citations and evidence anchors

- DOI: `10.1016/j.apmt.2017.02.005`
- Canonical VOR sibling: [[2017mortazavi-applied-mate-strong-thermal]] (`papers/Mortavazi_AMT_MoS2_thermal_2017.pdf`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
