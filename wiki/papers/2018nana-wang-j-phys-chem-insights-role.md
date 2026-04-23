---
id: paper:2018nana-wang-j-phys-chem-insights-role
type: paper
title: Insights into the Role of H2O in the Carbonation of CaO Nanoparticle with CO2
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:oxides-ceramics
- domain:reactive-md
- material:cement-mineral
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:lammps
- keyword:nvt-simulation
- keyword:reactive-md
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b05517
year: 2018
authors:
- Nana Wang, Yuchuan Feng, Xin Guo, and Adri C.T. van Duin
venue: J. Phys. Chem. C
pdf_sha256: 1dc1bfdf0979eb6b66179e2766062862ebdd4c15c7498024961810c3c5bee915
pdf_path: papers/Wang_CaO_H2O_JPCC_2018_accepted.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018nana-wang-j-phys-chem-insights-role -->

## Summary

Reactive molecular dynamics with a Ca/Al/C/H/O ReaxFF parametrization is combined with thermogravimetric experiments to clarify how water changes CaO carbonation by CO2 for a model CaO nanoparticle. The authors argue that steam mainly accelerates the diffusion-controlled stage by improving transport and promoting hydroxide-assisted carbonate growth, with limited impact on the initial kinetic-controlled stage.

Context in the article notes that **CaO** carbonation is central to **CO\(_2\)** capture and **cement** chemistry, and that **H\(_2\)O** is almost always present in flue gases or atmospheric exposure, so separating **kinetic** versus **diffusion-limited** stages with paired **TGA** and atomistic models targets operando-relevant humidity effects on product-layer growth.

## Methods
**1 — MD application (reactive carbonation).** **ReaxFF** reactive MD is run in **LAMMPS** for a **spherical CaO nanoparticle** (**~1.8 nm** radius) carved from a **CaO** crystal (Materials Studio), placed in a **cubic** cell (**88 × 88 × 88 Å³**) with **three-dimensional PBC**. **CO₂** and **H₂O** are packed externally (Packmol) with a **1:1 H₂O:CO₂** ratio and **~300 CO₂** molecules to accelerate product-layer formation as described in *J. Phys. Chem. C*. Simulations use the **canonical (NVT)** ensemble with a **Berendsen** thermostat (**100 fs** coupling), **0.25 fs** timestep, **4 ns** aggregate trajectory length, and output every **1000** steps. **Temperature** scans supporting the figures span **400, 600, 800, and 1000 K** in the article’s MD/TGA comparison. **Barostat / hydrostatic pressure control:** **N/A —** production trajectories are **constant-volume NVT** (no NPT barostat in the excerpted LAMMPS protocol). **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Experiments.** **Thermogravimetric analysis (TGA)** probes **kinetic-controlled** versus **diffusion-controlled** carbonation with and without steam, including elevated temperatures discussed up to **≥800 °C** in the introduction’s experimental context.

**3 — Force-field training.** **N/A —** the publication applies a published **Ca/Al/C/H/O ReaxFF** parametrization trained in prior work; this article focuses on **application** to CaO/CO₂/H₂O chemistry.

**4 — Static QM.** **N/A —** not the primary methodology beyond the ReaxFF QM training heritage.

## Findings
**Outcomes / mechanisms:** **H₂O** is reported to **accelerate carbonation primarily in the diffusion-controlled stage**, with **limited** impact on the **early kinetic-controlled** stage. **MD** rationalizes this via **faster product-layer thickening**, improved **CO₂/ion transport**, **OH⁻-assisted carbonate** formation, and **proton penetration / hydroxylation** that disrupts the oxide interior during diffusion-limited regimes.

**Comparisons:** **MD** trends are juxtaposed with **TGA** traces across **temperature** (including **400–1000 K** MD conditions paired with **400–800 °C** experimental discussion in the text).

**Sensitivity:** both **MD** and **TGA** emphasize **temperature** and **humidity (H₂O presence)** as levers on **stage partitioning** and **conversion** kinetics.

**Limitations / outlook:** the nanoparticle geometry is an **idealized model** of real **CaO** sorbents; readers should treat **absolute reaction rates** as **ReaxFF-dependent** and confirm details in the **PDF/SI**.

**Corpus honesty:** quantitative **T**/**time** windows above follow machine-readable text from `papers/Wang_CaO_H2O_JPCC_2018_accepted.pdf`; cite the **VOR** for authoritative tables.

## Limitations

Local extract coverage is limited to early pages; quantitative comparisons should be checked against the full PDF and any supporting information for complete boundary conditions and sensitivity tests.

## Relevance to group

Includes Adri C. T. van Duin (RxFF Consulting) as co-author; demonstrates ReaxFF application to CaO/CO2/H2O carbonation relevant to calcium looping and mineral carbonation.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.8b05517](https://doi.org/10.1021/acs.jpcc.8b05517)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
