---
id: paper:2021aya-k-buckley-acs-approaching-selectivity
type: paper
title: "Approaching 100% Selectivity at Low Potential on Ag for Electrochemical CO2 Reduction to CO Using a Surface Additive"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:batteries-electrochemistry
  - method:reaxff
  - material:metal-surface
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:catalysis-surface
  - keyword:nvt-simulation
source_refs: []
doi: "10.1021/acscatal.1c00830"
year: 2021
authors:
  - "Aya K. Buckley, Tao Cheng, Myoung Hwan Oh, Gregory M. Su, Jennifer Garrison, Sean W. Utan, Chenhui Zhu, F. Dean Toste, William A. Goddard, and Francesca M. Toma"
venue: "ACS Catal. 2021, 11, 9034-9042"
pdf_sha256: "9a7d8aaf0d3b7588743d0f6ef1a564dd433a6a2cd0963fafbda14ed03cfe3860"
pdf_path: "papers/ReaxFF_others/Buckley_Goddard_ACS_Catalysis_Ag_CO2_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021aya-k-buckley-acs-approaching-selectivity -->

## Summary

The work combines electrochemical measurements on polycrystalline Ag foil modified by drop-cast quaternary ammonium bromide salts with reactive molecular dynamics (RMD) using ReaxFF to relate CO2 reduction selectivity to interfacial structure and local CO2/H2O availability at −0.8 V versus RHE.

## Methods

### MD application (reactive ReaxFF)

- **Engine / code:** ReaxFF **reactive molecular dynamics** (RMD) as described in the article, following a prior Cu–electrolyte interfacial workflow with parameters transferred to **Ag** (per *ACS Catal.*). Specific package name (**N/A —** not quoted in this note; *ACS Catal.* / SI for LAMMPS-style implementation details if reported).
- **System size & composition:** Aqueous electrochemical **Ag** interface models including **H₂O**, **CO₂**, and **Br⁻**; charge-neutral variants with about **26 Br⁻** (and 24–25 **Br⁻** variants reported as similar) plus associated quaternary ammonium cation arrangements from the modifier series.
- **Boundaries / periodicity:** **Slab**/**interfacial** **periodic** cells implied by the standard RMD setup (full boundary prescription in `pdf_path`/SI).
- **Ensemble / temperature:** **NVT** at **298 K**; **2 ns** equilibration (reported as sufficient in the paper).
- **Timestep:** **N/A —** not restated in this note (see `pdf_path`/SI).
- **Duration / stages:** **2 ns** equilibration; production/analysis segments as in the full Methods/SI; additional staging **N/A —** not itemized in this short summary.
- **Thermostat / barostat:** Thermostat as implemented for **NVT** in the RMD setup (**N/A —** type string not restated in this note). **N/A —** **NPT** barostat: constant-volume interfacial sampling, not a bulk hydrostatic **pressure**-controlled segment.
- **Pressure:** Interfacial effective **pressure** / **stress** in the classical RMD is not a direct stand-in for **electrochemical** potential; treat electrochemical **bias** in experiments separately.
- **Electric field / bias in MD:** RMD is used with an implicit electrochemical framing in the text; the classical trajectory does not embed the full **−0.8 V RHE** bias as an explicit `efield` (**N/A —** see **## Limitations** and `pdf_path` for the stated modeling approximation).
- **Widom / post-processing:** **CO₂** local distributions near the interface are analyzed (including **Widom** test-particle style sampling after equilibration as described in the paper). H-bond coordination used a **0.4 nm** cutoff; **interfacial tension** from RMD is compared to measured **contact angles** (SI).

### Experiments and characterization

- **Chronoamperometry / product analysis:** **35 min** chronoamperometry in a **previously reported** cell, extracting **Faradaic efficiency** and partial currents for **CO** and **H₂** at controlled potentials.
- **GIWAXS / wettability:** **GIWAXS** on **drop-cast** quaternary ammonium modifiers; **NMR** of **rinsed** electrodes (SI); **contact angle** goniometry (SI) linked to the MD surface-tension discussion.

### Force-field training and standalone QM in this work

- **N/A** as a new ReaxFF reparameterization article—the study reuses/extends an established interfacial ReaxFF setup for **Ag** from a prior **Cu** workflow, with DFT/continuum details for training referenced in the main text rather than re-derived here.

## Findings

With **2-C16** (dihexadecyldimethylammonium bromide), **FE_CO** reaches about **~97%** at **~−0.75 to −0.8 V** versus **RHE** while the **geometric** **CO** partial current rises roughly **~9×** (e.g. **0.14 → 1.21 mA·cm⁻²** in a quoted comparison) and **H₂** partial current drops to **~0.001 mA·cm⁻²** from **~0.44 mA·cm⁻²** (values as tabulated/quoted in the article). **Longer C16** chain modifiers improve **CO** selectivity relative to **C10** in ways the authors argue exceed **contact-angle** hydrophilicity alone.

**Simulation/experiment link:** RMD with **2-C16** is associated with **higher** interfacial **CO₂** population (more **CO₂** in the first interfacial monolayer and out to about **4 nm** versus other modifiers) while maintaining enough **H₂O** to service **HOCO\***-mediated **CO** formation without excess water that would drive the **HER** branch. **2-C16** adopts a **bilayer** with inward-facing headgroups that can concentrate **CO₂**; a **1-C16**-class arrangement forms a monolayer with **chains toward** the metal. **GIWAXS** is used to connect **larger d-spacing** and more **gauche** content for **2-C16** to **looser** packing and higher **interfacial CO₂** solubilization.

**Caveat / limitations:** RMD omits a full first-principles treatment of the applied **bias**; numerical settings for **NVT** **MD** and **2 ns** staging should be verified in `pdf_path` before quantitative reuse (see **## Limitations**).

## Limitations

The atomistic models treat a simplified electrolyte interface and finite simulation times; electrochemical potentials are not fully replicated in the classical reactive MD framework.

## Relevance to group

Co-authors include W. A. Goddard III; ReaxFF is used to interpret electrochemical interface structure and selectivity.

## Citations and evidence anchors

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
