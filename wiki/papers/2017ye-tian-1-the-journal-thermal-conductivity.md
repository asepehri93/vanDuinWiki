---
id: paper:2017ye-tian-1-the-journal-thermal-conductivity
type: paper
title: "Thermal conductivity of vitreous silica from molecular dynamics simulations: The effects of force field, heat flux and system size"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:classical-md
  - method:reaxff
  - material:silicate-glass
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1063/1.4975162"
year: 2017
authors:
  - "Ye Tian"
  - "Jincheng Du"
  - "Wei Han"
  - "Xiaotao Zu"
  - "Xiaodong Yuan"
  - "Wanguo Zheng"
venue: "The Journal of Chemical Physics 146, 054504 (2017)"
pdf_sha256: "2eacbee21588ec0d18a47f603ec281e31e4bed26d3f1e9a59c32b47b9e3f948c"
pdf_path: "papers/ReaxFF_others/2017-JCP-TianYe-thermal-conductivity-SiO2-ReaxFF-BKS-Teter.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017ye-tian-1-the-journal-thermal-conductivity -->

## Summary

Thermal conductivity of vitreous silica is computed with nonequilibrium molecular dynamics using the **direct method** under imposed heat flux. Three empirical models—BKS, Teter, and ReaxFF—are compared for the same glass preparation philosophy so that differences reflect potential form rather than distinct amorphization recipes. The study evaluates statistical uncertainty from thermal noise and finite-size effects by varying heat-flux magnitude and cross-sectional area. The abstract reports that all three potentials yield realistic amorphous structures, but ReaxFF agrees best with experimental thermal conductivity near 300 K, attributed to improved low-frequency vibrational content relative to BKS and Teter. Increasing heat flux and cross-section lowers the estimated standard deviation of the conductivity estimate from fluctuations, improving practical convergence.

## Methods

**Molecular dynamics (nonequilibrium thermal transport).** **Molecular dynamics** simulations apply the **direct method** (nonequilibrium **MD** / **NEMD**) to vitreous **silica** **supercells**, imposing a steady **heat flux** and reading **thermal conductivity κ** from the induced **temperature** gradient once a steady profile appears. The study **benchmarks** three empirical potentials—**BKS**, **Teter**, and **ReaxFF**—on **identically prepared amorphous** structures so differences trace to the **force field** rather than distinct quench recipes. The abstract documents sweeps of **heat-flux magnitude** and cross-sectional area to trade **thermal** noise in **κ** estimates against **finite-size** effects and mild nonlinearity at large imposed flux. **Engine** naming (e.g., **LAMMPS**), exact **atom** counts, **PBC** details, **timestep** (fs), **NVE**/**NVT** staging, **equilibration**/**production** **duration** (ps/ns), and **thermostat** implementations for the hot/cold slabs are specified in **J. Chem. Phys.** **146**, **054504** and should be taken from the **PDF** at `pdf_path`—the local extract is headline-only. **NPT barostat**-based **pressure** control is **not** the focus of the quoted abstract (conductivity work typically uses **constant-volume** hot/cold regions); confirm any **stress** control from the article text. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** indicated for this **κ** study.

**Force-field fitting.** **N/A —** literature **BKS**, **Teter**, and **ReaxFF** **SiO₂** parameter sets are compared **as published**; this paper does not refit them.

**Static QM / DFT.** **N/A —** **κ** extraction is classical **MD**; no on-the-fly **DFT** trajectories are reported for the conductivity workflow.

**Review scope.** **N/A —** primary research article benchmarking empirical silica models.

## Findings

**Outcomes and mechanisms.** All three potentials reproduce realistic amorphous **silica** structures in the authors’ preparation, but **ReaxFF** tracks **experimental κ** near **300 K** (**~1.3–1.4 W m⁻¹ K⁻¹**) better than **BKS** and **Teter** in this head-to-head study; the discussion attributes the gain chiefly to improved **low-frequency** vibrational content relative to rigid-ion models that historically **overpredict κ** for **BKS**-class fits.

**Comparisons.** **Versus** prior literature values cited in the introduction, **BKS** tends to **overestimate κ**; here **ReaxFF** aligns more closely with the **experimental** window under the same **NEMD** diagnostics.

**Sensitivity / design levers.** Increasing imposed **heat flux** and cross-sectional area lowers the **standard deviation** of **κ** caused by **thermal** fluctuations, improving statistical precision but moving the protocol farther into nonlinear-response territory if pushed too far.

**Limitations / outlook.** Classical models omit quantum corrections to heat capacity and **phonon** lifetimes in glasses; even when **κ** matches, elastic constants from **ReaxFF** may still deviate from **experiment** elsewhere—authors caution readers accordingly in the broader discussion.

**Corpus honesty.** Indexed text is abstract-level only; reproduce numerics, **Green–Kubo** comparisons (if any), and figure citations from **`papers/ReaxFF_others/2017-JCP-TianYe-thermal-conductivity-SiO2-ReaxFF-BKS-Teter.pdf`**.
## Limitations

Classical simulations omit quantum corrections to heat capacity and phonon lifetimes in glasses; elastic constants from ReaxFF may still deviate from experiment even when κ matches well.

## Relevance to group

Side-by-side **ReaxFF vs rigid-ion silica** thermal transport benchmarking relevant to laser-damage and fused-silica modeling contexts.

## Citations and evidence anchors

- DOI: [10.1063/1.4975162](https://doi.org/10.1063/1.4975162)

## Related topics

- [[reaxff-family]]
