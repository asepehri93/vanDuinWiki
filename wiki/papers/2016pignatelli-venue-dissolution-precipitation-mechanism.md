---
id: paper:2016pignatelli-venue-dissolution-precipitation-mechanism
type: paper
title: "A dissolution-precipitation mechanism is at the origin of concrete creep in moist environments"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - method:reaxff
  - material:cement-mineral
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1063/1.4955429"
year: 2016
authors:
  - "Isabella Pignatelli"
  - "Aditya Kumar"
  - "Rouhollah Alizadeh"
  - "Yann Le Pape"
  - "Mathieu Bauchy"
  - "Gaurav Sant"
venue: "J. Chem. Phys. 145, 054701 (2016)"
pdf_sha256: "75ee42ad5453db9f645fe3e97e67b6880a3332bbe3e75c433035eb19e56f562b"
pdf_path: "papers/ReaxFF_others/Bauchy_Concrete_creep_JCP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016pignatelli-venue-dissolution-precipitation-mechanism -->

## Summary

Macroscopic **creep** of cementitious **calcium–silicate–hydrate (C–S–H)** gels influences long-term deformation of concrete structures, especially under sustained load in **moist** environments. This **Journal of Chemical Physics** article advances a **nanoscale** explanation: **basic creep** at **relative humidity ≥ 50%** with fixed moisture content follows a **stress-driven dissolution–reprecipitation** mechanism at grain contacts, analogous to **pressure solution** in geological minerals. The argument is built from **micro-indentation** creep rates, **vertical scanning interferometry** tracking surface height under load, and **atomistic simulations** of C–S–H compositions spanning the compositional variability relevant to real pastes. The synthesis aims to connect composition-dependent **dissolution propensity** from simulations to measured **macroscopic creep** rates.

## Methods

**Experiments.** **Basic creep** is probed at **relative humidity \(\geq 50\%\)** with **fixed moisture content** using **micro-indentation** creep rates and **vertical scanning interferometry** of **surface height** under load—the combination is used to connect **macroscopic** creep response to **nanoscale** processes at grain contacts.

**Atomistic simulations.** The authors build **Pellenq**-type **C–S–H** supercells spanning Ca/Si ratios, hydrate interlayers with **Grand Canonical Monte Carlo** (**GCMC**) against bulk water at **constant volume** and room temperature, then propagate **ReaxFF** **molecular dynamics** with a **0.25 fs** **timestep** so that interlayer water can dissociate into hydroxyls. Structures are relaxed toward **zero stress** before further analysis. **Topological constraints**’ enumeration then analyzes **MD** trajectories at **300 K** to classify rigid versus floppy network modes; those **MD** segments are described as **canonical** (constant-volume) sampling in the sense of fixed-cell thermalization at **300 K**, with detailed thermostat couplings and **production** run lengths (multi-**ns** segments in the cited protocol papers) spelled out in Refs. 29 and 35 rather than re-tabulated here. **Periodic** in-plane models follow the defective tobermorite construction summarized in Section II.E of the **PDF**. Experimental dissolution benchmarks in the article reference **1 bar**-class aqueous conditions for VSI rate measurements, distinct from the **zero stress** mechanical relaxation applied to the atomistic cells before further **MD** assessment. **N/A — umbrella / metadynamics / replica exchange**; **N/A — applied electric field**. **N/A — standalone new ReaxFF training** in this paper—the authors “retain the original **ReaxFF** potential” from prior parametrizations while focusing on dissolution–creep correlation.

**Interpretation.** The combined protocol links atomistic kinetics to macroscopic creep metrics for basic creep at relative humidity \(\geq 50\%\) with fixed moisture content, arguing for a stress-driven dissolution–reprecipitation picture at nanoscale grain contacts rather than viscoelastic grain sliding alone in that regime.
## Findings

**Creep rates** correlate with **computed dissolution rates** across the C–S–H chemistries examined, supporting dissolution–precipitation as a governing mechanism under the stated humidity and loading conditions rather than only viscoelastic flow of grains. The framework links **composition-dependent nanoscale kinetics** to **long-timescale** macroscopic deformation, with implications for durability modeling when moisture and stress are simultaneously present. Other creep mechanisms may still contribute outside the emphasized regime; the paper focuses where moisture-enabled dissolution is expected to be active. Interpretations hinge on the **relative humidity \(\geq 50\%\)** window and **fixed moisture content** assumptions stated for the experiments, because concrete creep mechanisms can switch sharply when environmental constraints change.

## Limitations

Idealized atomistic models omit full **microstructure** complexity (porosity distribution, ionic strength variations, alkali effects) present in real concrete.

## Reader notes (MAS / retrieval)

Pair with **cement** microstructure pages when translating nanoscale dissolution arguments to paste-scale creep forecasts.

Also link [[theme-oxides-silica-ceramics]] for broader **silicate** context.

See also the **JCP** figure supplements for creep curves.

## Relevance to group

Provides experiment-integrated **atomistic** perspective on **silicate** materials and aqueous interfaces adjacent to oxide and cement literature in the corpus.

## Citations and evidence anchors

- DOI: [10.1063/1.4955429](https://doi.org/10.1063/1.4955429)

## Related topics

- [[theme-oxides-silica-ceramics]]
