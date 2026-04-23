---
id: paper:2023yousefian-venue-paper
type: paper
title: "Improved prediction for failure time of multilayer ceramic capacitors (MLCCs): a physics-based machine learning approach"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - material:perovskite-oxide
  - task:application
  - domain:methods-software
  - scale:multiscale
paper_keywords:
  - keyword:validation-experiment
candidate_tags:
  - "XGBoost-reliability"
  - "HALT-accelerated-life-testing"
  - "physics-based-ML-MTTF"
source_refs: []
doi: "10.1063/5.0158360"
year: 2023
authors:
  - "Pedram Yousefian"
  - "Alireza Sepehrinezhad"
  - "Adri C. T. van Duin"
  - "Clive A. Randall"
venue: "APL Materials (accepted manuscript PDF in corpus)"
pdf_sha256: "e38ec34700f42d8e8241783626851cebd69bb4d0a6fba35111fffe56d50b3e47"
pdf_path: "papers/Yousefian_Sepherinezhad_AML_2023.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023yousefian-venue-paper -->

## Summary

**Multilayer ceramic capacitors (MLCCs)** are ubiquitous in electronics; as dielectrics are made thinner and operating fields rise, **reliability** and **mean time to failure (MTTF)** estimation under **accelerated stress** becomes a central engineering problem. This **APL Materials** manuscript develops a **physics-informed machine learning** approach based on **gradient-boosted trees (XGBoost)** to predict **MTTF** for **X7R** MLCCs across **temperature** and **voltage** conditions, comparing against classical **Eyring** extrapolation and a newer **tipping-point** reliability model described in the dielectrics literature. A **transfer-learning** framing is used to improve accuracy when labeled **HALT**-style data are sparse for some stress splits and to support predictions for stress points **without direct measurements**. Penn State authorship includes **Adri C. T. van Duin** alongside MLCC reliability experts, linking the group’s **multiscale materials** footprint to **electronic component** lifetime modeling rather than atomistic reaction chemistry. The corpus PDF is an **accepted manuscript**; copy-edited **version-of-record** layout may differ.

## Methods

### Data-driven reliability modeling (not atomistic MD)

**Supervised** learning on **HALT** lifetime data; **physics-informed features** + **XGBoost** for **MTTF** vs **Eyring**/**tipping-point** baselines.

### Transfer learning

Improves predictions when some **T–V** cells have **sparse** failure labels; targets **extrapolation** with **uncertainty** controls.

### Materials context (continuum)

**BaTiO\(_3\)** **MLCC** processing motivates **oxygen-vacancy** degradation framing—**ReaxFF** is **not** the computational engine here.

**1 — MD / ReaxFF (N/A).** **N/A** for LAMMPS, NVT/NPT **RMD**, **timestep** values, **E-field** **RMD**, and **metadynamics/umbrella**—this work is **HALT**-data **XGBoost** **reliability** modeling (non-simulation “Methods” in the **AGENTS** review sense).

**2 — ReaxFF training and static DFT (N/A).** **N/A** as a ReaxFF parametrization or PBE+DFT kinetics study; see the **APL Materials** **Methods**/**SI** for **feature** design, **train/test** **splits**, and **baselines** (Eyring, tipping-point).

## Findings

The abstract reports that the **machine-learning model consistently outperforms** both **Eyring** and **tipping point** models in the compared conditions, with favorable **stability** across splits. The approach is also described as yielding **reasonable MTTF estimates** for **untested** voltage–temperature combinations, supporting use as a practical reliability tool for **X7R**-class **BaTiO₃** capacitors under accelerated stress. Claims about ranking and extrapolation should be read against the manuscript’s **metrics** sections and any **SI** tables in the published article. At a high level, the manuscript argues that **physics-aware features** help XGBoost respect known **stress–life** monotonicities and **Arrhenius-like** temperature trends while still learning **nonlinear** interactions between **voltage**, **temperature**, and manufacturing-driven variability that pure empirical laws miss. The framing is explicitly reliability-oriented: improve **MTTF** estimates where **HALT** data are abundant while still producing defensible predictions when some stress cells are **sparse**, which is common in industrial qualification campaigns. From a knowledge-base perspective, the paper is primarily a **reliability ML** contribution: it should not be read as atomistic **BaTiO\(_3\)** chemistry, even though **oxygen vacancy** narratives motivate degradation phenomenology at a continuum level.

## Limitations

Accepted-manuscript PDF may differ from final publisher typesetting. The paper does not resolve atomistic degradation chemistry; it is a **data-driven reliability** model at component scale.

## Relevance to group

Connects **van Duin** co-authorship to **dielectric reliability** and **ML** failure-time modeling for **ferroelectric ceramic** components.

## Citations and evidence anchors

- DOI: [10.1063/5.0158360](https://doi.org/10.1063/5.0158360)

## Related topics

- [[reaxff-family]]
