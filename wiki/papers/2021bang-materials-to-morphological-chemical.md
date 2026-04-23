---
id: paper:2021bang-materials-to-morphological-chemical
type: paper
title: "Morphological and chemical evolution of transient interfaces during zinc oxide cold sintering process"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:npt-simulation
source_refs: []
doi: "10.1016/j.mtchem.2022.100925"
year: 2021
authors:
  - "S.H. Bang, M.Y. Sengul, Z. Fan, A. Ndayishimiye, A.C.T. van Duin, C.A. Randall"
venue: "Mater. Today Chem. 24 (2022) 100925"
pdf_sha256: "ef350290f96be30fe6165270482a449c19fad10ddf3060f3b7beafc5e86ffb68"
pdf_path: "papers/Bang_ZnO_coldsintering_MaterialsTodayChemistry_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021bang-materials-to-morphological-chemical -->

## Summary

The study follows zinc oxide cold sintering with acetic acid: gas physisorption quantifies evolving surface area, electron microscopy resolves crystalline grains versus carbon-rich amorphous regions, and ReaxFF molecular dynamics interprets acetate-mediated bonding at ZnO surfaces during the transient chemical interface stage.

Cold sintering aims to densify ceramics below conventional firing temperatures by transient liquid or chemically assisted plasticity; tracking surface area and microstructure ties processing windows to interface chemistry.

## Methods

### MD application (ReaxFF)

- **Engine / code:** ReaxFF **molecular dynamics** for **acetic-acid**/**acetate** interactions with **ZnO** surface models (per *Mater. Today Chem.*; exact MD engine name **N/A —** in this short note—see `pdf_path` if reported).
- **System size & composition:** **Acetate**-involving **ZnO** interface/oxide models; atom counts, surface indices, and cell vectors **N/A —** not restated in this note (see `pdf_path`/SI).
- **Boundaries / periodicity:** **PBC** surface/slab-style cells implied for bulk/interface sampling (**N/A —** explicit boundary list in the indexed wiki draft; confirm `pdf_path`).
- **Ensemble / thermostat / barostat:** **NVT**/**NPT** choices and **thermostat** barostat line **N/A —** not copied into this short summary; the article uses **NPT** in the broader workflow context for cold-sintering *experiments* at moderate **temperature**; atomistic equilibration details live in `pdf_path`/SI.
- **Timestep / duration:** **N/A —** not restated in this short summary; consult `pdf_path` for **fs** integration, **ps**–**ns** run lengths, and equilibration vs production.
- **Temperature / pressure in MD:** Uniaxial **~175 MPa** pressing and **band-heater** schedules apply to the **laboratory** process; in-cell **pressure** control in MD **N/A —** consult `pdf_path` for any **NPT** segments in simulations.
- **Electric field, shear, shock, enhanced sampling:** **N/A —** not part of the stated MD focus.

### Experiments (cold sintering and microstructure)

- **Formulation and pressing:** **ZnO** (Alfa Aesar **40–100 nm** APS) mixed with **15 wt%** of **2 M** **acetic acid** in an agate mortar (**5 min**), loaded in a **13 mm** die with thermocouple access, **uniaxially** pressed at **175 MPa** for **5 min** at **room temperature**, then heated (about **15 °C·min⁻¹** ramp) with isothermal **dwells** of **0–30 min** at the selected processing temperature (see article for the exact setpoint and cooling).
- **Surface area / kinetics:** Gas **physisorption** tracks specific surface area evolution; **Schlaffer-type** analysis of activation energy for surface-area reduction.
- **Imaging:** **TEM** contrasts **grains** vs **carbon-rich** **amorphous** regions as a function of **dwell** time.

### Force-field training / standalone DFT in this work

- **N/A** as a primary DFT/parameterization paper: ReaxFF is applied to interpret **acetate**/**Zn** contact chemistry during transient cold sintering, with the cited ReaxFF line described in the article/SI (not reproduced here).

## Findings

**Densification and microstructure:** Cold sintering yields **low-temperature** dense **polycrystalline** **ZnO** relative to conventional **furnace** firing; the authors connect transient **organics** to **zinc carboxylate**-like chemistries that are **consumed** on the path to **residual-free** **ZnO**. **TEM** with **~30 min** **dwell** shows a falling **amorphous** fraction and **grain** growth, consistent with **recrystallization** and **pore** closure. **BET**/surface-area trends tie macroscopic **surface-area** collapse to these microstructural changes. **ReaxFF** **molecular dynamics** supports **acetate** as a **bridging** **ligand** that can connect **Zn** centers across nascent necks—an **atomistic** handle on early **particle–particle** adhesion in **acetic-acid**-assisted **ZnO** **CSP**, with **kinetic** prefactors in `pdf_path`/TEM for defensible **quantitative** use.

## Limitations

Finite dwell times and lab-scale processing may not capture all industrial cold-sintering heterogeneities; simulation cells summarize interface chemistry rather than full pellet mechanics.

## Relevance to group

A. C. T. van Duin is a co-author; ReaxFF supports interface chemistry for ZnO cold sintering.

## Citations and evidence anchors

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
