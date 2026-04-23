---
id: paper:2015bhoi-rsc-advances-insights-combustion
type: paper
title: "Insights on the combustion and pyrolysis behavior of three different ranks of coals using reactive molecular dynamics simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - domain:carbon-hydrocarbon
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1039/C5RA23181G"
year: 2015
authors:
  - "Sanjukta Bhoi"
  - "Tamal Banerjee"
  - "Kaustubha Mohanty"
venue: "RSC Adv."
pdf_sha256: "153bd1a32766d0ab568539ce7d2099fa3540a5352fc80a54398eb8607a33535c"
pdf_path: "papers/ReaxFF_others/Bhoi_RSC_Advances_coal_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015bhoi-rsc-advances-insights-combustion -->

## Summary

Coal **combustion** and **pyrolysis** depend on **rank-dependent** composition and nanostructure, while experiments rarely resolve **atomistic** pathways for **oxygen-containing** products and light gases. This **RSC Advances** paper constructs structural models for **lignite**, **bituminous**, and **anthracite** and drives **ReaxFF molecular dynamics** in **ADF** across **2000–4000 K** to make bond-breaking events accessible within **nanosecond-scale** trajectories, then compares **CO/CO\(_2\)** evolution and light-gas intermediates across ranks. The high temperatures are a **computational acceleration** choice; the discussion relates qualitative simulation trends to literature experiments.

## Methods

**Force-field training.** **N/A —** the authors adopt the **ReaxFF** parameterization bundled with **ADF** for coal chemistry rather than reporting a new fit in this article.

**MD application (ADF ReaxFF MD on rank-specific coal models).** **Engine / code:** **ADF**’s **ReaxFF molecular dynamics** module, as stated in the introduction to `papers/ReaxFF_others/Bhoi_RSC_Advances_coal_2016.pdf`. **System size & composition:** structural models for **lignite**, **bituminous**, and **anthracite** coals are constructed in the article (atom counts, packing, and cell vectors tabulated in the **Computational methods** section of that PDF). **Boundaries / periodicity:** **three-dimensional periodic** simulation boxes for the packed coal models. **Ensemble, timestep, thermostat/barostat, staging, and trajectory lengths:** the indexed p1–2 extract for this slug carries abstract-level motivation only (including **2000–4000 K** temperatures to make chemistry visible within affordable MD time); **full protocol lines** (minimization/equilibration durations, timestep choices, thermostat identity and coupling, heating ramps, and production segment lengths) must be taken from the manuscript **Computational methods** section and any SI tables—do not infer them from this wiki note alone. **Pressure control:** **N/A —** the abstract/introduction framing emphasizes constant-volume high-temperature chemistry rather than documented **NPT** production targets. **Replica / electric field:** **N/A —** not reported.

## Findings

**CO** and **CO\(_2\)** are the dominant **oxygen-containing** products in both pyrolysis and combustion trajectories sampled in the study. **Lignite** shows the fastest **CO** and **CO\(_2\)** formation rates among the three ranks, matching the qualitative experimental ordering cited by the authors. **Methane**, **ethane**, and **ethylene** appear as major light hydrocarbon intermediates across ranks; their abundances vary with temperature between **2000 K** and **4000 K** but remain substantial throughout that range in the simulations shown. The rank ordering discussion is most reliable as a **qualitative** trend (lignite fastest among the three ranks for CO/CO\(_2\) evolution in the authors’ setup) rather than as quantitative pyrolysis yields transferable to furnace conditions without additional kinetics modeling.

## Limitations

High-temperature acceleration can alter branching ratios relative to laboratory heating rates; ReaxFF parameterization governs oxygen chemistry accuracy.

## Reader notes (MAS / retrieval)

Best for **coal rank comparisons** in **ReaxFF** combustion/pyrolysis benchmarks; cite **ADF** implementation explicitly when discussing software reproducibility.

Temperatures are **accelerated**; use qualitative trends first.

## Relevance to group

**Fuel chemistry** application of **ReaxFF** to **coal** pyrolysis/combustion with explicit software context (**ADF**).

## Citations and evidence anchors

- DOI: [10.1039/C5RA23181G](https://doi.org/10.1039/C5RA23181G)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
