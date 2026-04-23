---
id: paper:2025li-fuel-404-202-critical-nanoparticle
type: paper
title: "Critical nanoparticle formation in iron combustion: single particle experiments with in-situ multi-parameter diagnostics aided by multi-scale simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - method:continuum-or-mesoscale
  - task:experiment-integrated
  - scale:multiscale
paper_keywords:
  - keyword:combustion
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2025.136303"
year: 2025
authors:
  - "Tao Li"
  - "Bich-Diep Nguyen"
  - "Yawei Gao"
  - "Leon Elsässer"
  - "Daoguan Ning"
  - "Arne Scholtissek"
  - "Adri C. T. van Duin"
  - "Christian Hasse"
  - "Benjamin Böhm"
venue: "Fuel, 404 (2026) 136303"
pdf_sha256: "88b63b812b11a1bac4aa0c84dd4e563ef159a0bff105ce027ad00bcc7a8ff8d3"
pdf_path: "papers/Li_Gao_Iron_Combustion_Fuel_2026.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025li-fuel-404-202-critical-nanoparticle -->

!!! abstract

Single iron particles were burned in post-flame oxidizing environments while high-speed diagnostics tracked particle size, nanoparticle-cloud evolution, and surface temperature; complementary CFD of the particle boundary layer and ReaxFF molecular dynamics of precursor formation and agglomeration interpreted how oxygen level and Stefan flow affect when and how iron oxide nanoparticles appear.

## Summary

Iron combustion can release iron oxide nanoparticles, affecting efficiency and emissions. The work combines experiments in a laminar flow reactor on a flat-flame burner with multi-scale modeling: axisymmetric two-phase CFD around a lumped particle model, and ReaxFF molecular dynamics for gas-phase precursor chemistry and cluster agglomeration. Post-flame oxygen mole fractions of 20, 30, and 40 vol% were used at about 1800 K gas temperature.

## Methods

### Experiments and diagnostics

- **Reactor and atmosphere:** Single iron particles were burned in a well-characterized laminar flow reactor with defined thermal, chemical, and aerodynamic conditions. Post-flame conditions used a laminar flat-flame arrangement with oxygen mole fractions of 20, 30, and 40 vol% and approximately 1800 K gas temperature (as stated in the article).
- **Imaging:** Three 10 kHz imaging paths were used: two-color pyrometry for surface temperature history and two diffuse backlight-illumination (DBI) channels for microparticle size and nanoparticle cloud evolution.
- **Particle sizing:** In-situ DBI sizing was cross-checked against CamSizer measurements; particles were grouped by diameter (e.g., ranges centered near 40, 50, and 60 µm) for conditional statistics.

### CFD (nanoparticle transport near the particle)

- **Setup:** Two-dimensional axisymmetric simulations resolved the boundary layer around a lumped particle model (solid and liquid regimes combined from cited submodels), following a detailed setup referenced in the paper. A two-fluid Eulerian–Eulerian treatment was used for gas and nanoparticle phases, including a transport equation for nanoparticle volume fraction, thermophoretic velocity, and Stefan flow at the particle surface driven by oxidation and evaporation mass fluxes.
- **Nanoparticle formation in CFD:** Nanoparticle formation rate was modeled as condensation of gaseous iron species upon supersaturation (with analogy to cited models for other oxides). Evaporation feeding precursors used Fe(g) partial pressure from chemical equilibrium at the surface (other species neglected as Fe(g) dominated). Nanoparticle volume fraction was integrated in a region analogous to the experimental field of view, with a gap excluding the microparticle near-field region to match detectability.

### ReaxFF molecular dynamics

- **Force field:** Reactive MD used the ReaxFF formalism with Fe/O parameters from Shin et al., trained on iron oxide thermodynamics and iron redox energetics (as cited in the paper).
- **Phase I (precursors):** A BCC Fe sphere (radius 12 Å) was annealed, then placed in an 80 Å × 80 Å × 80 Å periodic box with 500 O₂ molecules. After energy minimization, **NVE** runs lasted **500 ps** at initial temperatures of **1500 K, 2000 K, and 2500 K** with **0.1 fs** time step and charge updates each step (velocity Verlet).
- **Phase II (agglomeration):** Four precursor mixtures (two from Phase I and two from thermodynamic equilibrium references) at number density **1/256 Å⁻³** in a periodic cube, with **1000 Fe** and **2000 O** atoms. **NVT** simulations ran for **2 ns** with **0.25 fs** time step, **Nosé–Hoover** thermostat, and charges updated each step. Constant-temperature cases at **1000 K, 2000 K, and 3000 K** bracketed cooling from hot gas to cooler surroundings. MD data were Gaussian-smoothed for presentation.

## Findings

- **Diagnostics:** Multi-parameter imaging quantified nanoparticle release onset time and onset temperature; both depended on particle size and ambient oxygen mole fraction.
- **CFD:** Increased Stefan flow with higher oxygen strengthened convection toward the parent particle, transporting nanoparticles back toward it and delaying the appearance of detectable nanoparticle clouds; this raised the apparent microparticle temperature at nanoparticle release onset and helped explain why release temperature rises with oxygen level.
- **ReaxFF MD:** Precursor formation and agglomeration pathways were explored; initial temperature strongly affected gas-phase precursor amounts and nanocluster composition, with **Fe(II) favored at higher temperatures** and **Fe(III) at lower temperatures** in the agglomeration-stage simulations described.

## Limitations

- Full iron combustion spans evaporation, gas-phase chemistry, and oxide condensation across microsecond scales and large particles; ReaxFF MD is limited to nanosecond/nanometer regimes, so the MD study uses staged precursor and agglomeration models rather than a single end-to-end particle burn.

## Relevance to group

Reactive Fe/O chemistry and ReaxFF methodology align with the group’s reactive force-field work; co-author **Adri C. T. van Duin** contributed to the reactive MD strand.

## Citations and evidence anchors

- DOI: `10.1016/j.fuel.2025.136303` — *Fuel* (version-of-record PDF in corpus).

## Related topics

- [[reaxff-family]]
