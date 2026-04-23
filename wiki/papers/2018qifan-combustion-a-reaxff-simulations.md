---
id: paper:2018qifan-combustion-a-reaxff-simulations
type: paper
title: ReaxFF simulations of petroleum coke sulfur removal mechanisms during pyrolysis
  and combustion
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:carbon-hydrocarbon
- domain:fuel-combustion
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- method:reaxff
- task:application
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1016/j.combustflame.2018.09.005
year: 2018
authors:
- Qifan Zhong
- Qiuyun Mao
- Jin Xiao
- Adri C. T. van Duin
- Jonathan P. Mathews
venue: Combust. Flame
pdf_sha256: b5a319b4d56e0c8b2d9fdba93ebaedc8e17f44b5b5d73426a8a6a16afadd73cb
pdf_path: papers/Zhong_CombFlame_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018qifan-combustion-a-reaxff-simulations -->

## Summary

**Petroleum coke** is a carbon-rich refinery stream whose **utilization** and **emissions** profile depend strongly on **heteroatom** content, especially **sulfur** trapped in complex **carbonaceous** matrices. This **Combustion and Flame** article applies **ReaxFF reactive molecular dynamics** to model **S removal** pathways during **pyrolysis**-like and **combustion**-like **high-temperature** scenarios, connecting **atomistic** bond events to macroscopic narratives of **S release** during thermal processing. The work combines **PSU** expertise in **reactive hydrocarbon** chemistry (**van Duin**) with **Mathews**-group experience in **coal/coke** combustion modeling, targeting mechanisms that are difficult to isolate experimentally when matrices are **disordered** and **multi-phase**. The framing is explicitly chemistry-forward: which **C–S** cleavage channels, **oxygenated** attack routes, and **small-molecule** sulfur carriers appear under different thermal histories. From an applications perspective, the manuscript is most useful when read as a **mechanism generator** for **S** release from **disordered** carbon hosts: rather than committing to a single global pyrolysis scheme, ReaxFF trajectories can reveal **competing** channels whose prominence shifts when **O\(_2\)**-related attack becomes accessible versus purely **pyrolytic** environments. That distinction matters for **emissions** interpretations because **SO\(_x\)** precursors can emerge through different sequences depending on whether oxygen is present at the **local** scale modeled.

## Methods
**1 — MD application (petcoke pyrolysis + combustion).** The authors build a **large atomistic Qingdao petcoke** surrogate (**C₁₆₄₈H₇₇₂O₅₉N₂₄S₄₇**) consistent with **HRTEM**, **XRD**, **FTIR**, and **XPS** constraints, then run **ReaxFF molecular dynamics** using the **ReaxFF CHONSSi** parameter set in the **ADF** software package under the **constant-volume, constant-temperature (NVT)** ensemble with **0.3 Å** bond-order cutoffs for **molecule recognition** (analysis only) and **0.001 Å** cutoffs for valence/torsion monitors as stated in *Combust. Flame*. **Equilibration:** **100 K** damping MD with **0.25 fs** timestep and **Berendsen** thermostat to relax geometry without chemistry. **Production:** **pyrolysis** trajectories at **3000 K** for **250 ps** (abstract-reported yields **44.7 wt % gas**, **11.0 wt % tar** at those conditions); **combustion** runs add an **O₂** environment on the same initial structure (see article for stoichiometry/cell). **PBC:** **three-dimensional PBC** for the periodic petcoke cell. **Barostat:** **N/A —** **NVT** protocols without **NPT** barostat in the excerpted workflow. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies published **ReaxFF CHONSSi** parameters (cited in paper).

**3 — Static QM / continuum.** **N/A —** not the primary methods beyond **ReaxFF**’s underlying **QM** training heritage.

## Findings
**Outcomes / mechanisms:** **Pyrolysis** first converts **thiophenic** sulfur to **C₁–₄S** (mostly **C₂S**), **COS**, and **CNS** with overlapping **heteroatom** release at **3000 K** in the **250 ps** window summarized in the abstract. **Combustion** shows **earlier COS formation** from **thiophenic** sites; **N–S** motifs do not persist in the **O-rich** run as **pyrrolic/pyridinic N** oxidize to **CON/NO** species. **S** sequences during combustion are described as **COS → CO₂S → CO₃S → CO₄S**, while **H** attacks **COS/C₂S/CNS** gases forming **HS/H₂S** rather than directly stripping **coke-bound S** in the modeled trajectory class.

**Comparisons:** the atomistic picture complements **industrial** narratives about **S** retention in **high-S petcoke** versus **calcined** products.

**Sensitivity:** **O₂ availability** switches dominant **S** carriers between **pyrolysis**-like and **combustion**-like timelines.

**Limitations:** a single **structural** surrogate cannot capture all **petcoke** heterogeneity; **3000 K**/**250 ps** windows are **accelerated** relative to plant reactors.

**Corpus honesty:** yields and temperature/time stamps are taken from the **abstract** on `papers/Zhong_CombFlame_2018.pdf`; use the **PDF** for species traces.

## Limitations

**Petroleum coke** is structurally diverse; any atomistic matrix is a **simplified** surrogate. **High-temperature** MD requires scrutiny of **temperature** ramping and **equilibration** when comparing to experiment.

## Relevance to group

Extends **ReaxFF** into **heavy fuel / coke** **S chemistry** relevant to **combustion** and **environmental** impacts.

## Citations and evidence anchors

- **DOI:** [10.1016/j.combustflame.2018.09.005](https://doi.org/10.1016/j.combustflame.2018.09.005) (`papers/Zhong_CombFlame_2018.pdf`).

## Related topics

- [[reaxff-family]]
