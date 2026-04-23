---
id: paper:2017n-m-anoop-krishnan-acs-revealing-effect
type: paper
title: "Revealing the Effect of Irradiation on Cement Hydrates: Evidence of a Topological Self-Organization"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b09405"
year: 2017
authors:
  - "N. M. Anoop Krishnan"
  - "Bu Wang"
  - "Gaurav Sant"
  - "James C. Phillips"
  - "Mathieu Bauchy"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "73ecc8e83710e03e0b76f82f988b9ee7d8d3ee15e261d1c4f04148f9838f9b5a"
pdf_path: "papers/ReaxFF_others/Krishnan_Bauchy_ACS_irradiation_CSH.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017n-m-anoop-krishnan-acs-revealing-effect -->

!!! abstract
Reactive MD in LAMMPS with iterative neutron-collision cascades (300 eV PKA, ReaxFF + Manzano parameters) on Pellenq C–S–H models shows radiation-induced self-organization and optimal damage resistance near isostatic Ca/Si ≈ 1.5.

## Summary

**C–S–H** models across **Ca/Si** ratios are prepared from **tobermorite**-based workflows (**GCMC water**, **ReaxFF relaxation** for hydroxylation—see Methods in paper) so that initial **silicate chain** statistics and **pore water** content reflect composition before irradiation. **Irradiation** is modeled with **iterative reactive MD in LAMMPS**: choose **primary knock-on atoms** weighted by **neutron cross sections** (Table 1), impart **300 eV**, evolve **ballistic cascade** with **NVE** in a **10 Å** sphere (**variable timestep**, max displacement **0.0001 Å** per step) and **0.5 fs** otherwise for **20 ps**; outer shell **Berendsen 300 K**; post-cascade **NPT 300 K, 0 bar** for **5 ps**; repeat until **enthalpy/density saturate**. Systems ~**6000 atoms** with box sizes chosen to avoid cascade self-interaction. **ReaxFF** parameters from **Manzano et al.**; **ZBL** short-range corrections noted unnecessary at this incident energy. **Topological constraint theory** enumerates rigidity metrics vs composition to connect **network connectivity** changes to **mechanical** **eigenstress** release under **damage accumulation**.

## Methods

**Force-field training / fitting.** **Manzano *et al.* C–S–H ReaxFF** with **EEM**-style charge treatment is used as published (**no** new QM refit in this *ACS Appl. Mater. Interfaces* article).

**MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** integrates **iterative collision cascades** on **Pellenq-type C–S–H** models prepared with **GCMC water** and prior **ReaxFF relaxation** (see article **Methods**). **System size & composition:** **~6000-atom** cells whose **periodic** extents are chosen **≥2×** the maximum **PKA** travel distance (per the “avoid self-interaction under **periodic boundary conditions**” criterion stated in the article). **PKA selection:** weighted by **neutron cross sections** (**Table 1**). **Cascade energy:** **300 eV** per primary knock-on. **Spatial partitioning:** **10 Å** spherical **hot core** treated in **microcanonical (NVE)** dynamics with **variable timestep** (max displacement **0.0001 Å** per step) switching to **fixed Δt = 0.5 fs** outside the high-collision regime; **20 ps** ballistic segment. **Shell thermostat:** atoms outside the sphere held at **300 K** with a **Berendsen** thermostat. **Post-cascade relaxation:** **NPT** at **300 K**, **0 bar**, for **5 ps** to allow **density** adjustment. **Iteration:** repeat with new **PKAs** until **enthalpy** and **density** **saturate**. **Barostat:** **N/A —** applied only during the short **NPT** relaxation windows, not during the **NVE** core cascade. **Electric field:** **N/A —** not applied. **Enhanced sampling:** **N/A —** direct cascade protocol.

**Static QM / DFT.** **N/A —** **DFT** is **not** the cascade integrator; **DFT** enters only indirectly via the **Manzano** **ReaxFF** training lineage referenced in the paper.

**Review / non-simulation framing.** **N/A —** primary **application** article (not a review).

## Findings

**Outcomes & mechanisms.** **C–S–H** **reorders** under accumulated radiation: **silicate chain** statistics, **pore water**, and **medium-range order** shift even though the gel is comparatively **radiation-tolerant** versus crystalline silicates in their comparison. **Topological constraint theory (TCT)** links **network rigidity** changes to **stress release**; **mobile water** is argued to facilitate **eigenstress** relaxation during **self-organization**.

**Comparisons.** The manuscript contrasts **irradiated** vs **pristine** structures across **Ca/Si** and against crystalline silicate benchmarks as summarized in the article.

**Sensitivity & design levers.** **Damage resistance** vs **Ca/Si** is **non-monotonic**, with a highlighted **optimum** near **Ca/Si ≈ 1.5** tied to **isostatic** rigidity in their **TCT** analysis.

**Limitations & outlook (as authored).** **300 eV** **PKA** energy is a modeling choice; **C–S–H** construction inherits **Pellenq-model** limitations noted in the article.

**Corpus / KB honesty.** Protocol details above follow the **indexed PDF**; use **DOI-linked** tables for quantitative **TCT** metrics.


## Limitations

Model C–S–H construction inherits known limitations of the Pellenq approach; cascade energy fixed at 300 eV.

## Relevance to group

Uses **ReaxFF** cement parametrizations central to group-related cement simulations.

## Citations and evidence anchors

- DOI: `10.1021/acsami.7b09405`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
