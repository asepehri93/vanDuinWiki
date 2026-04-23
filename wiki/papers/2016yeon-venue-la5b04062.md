---
id: paper:2016yeon-venue-la5b04062
type: paper
title: "Effects of water on tribochemical wear of silicon oxide interface: Molecular dynamics study with reactive force field (ReaxFF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.5b04062"
year: 2016
authors:
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Langmuir"
pdf_sha256: "858dff4771a5126bbb2aff37aef480d459655a83000fbb1ea4cd313f1c5ccf5c"
pdf_path: "papers/Yeon_Langmuir_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:tribology
  - keyword:oxide-surface
  - keyword:water-interfaces
---

<!-- id:paper:2016yeon-venue-la5b04062 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This Langmuir article reports molecular dynamics simulations with the ReaxFF reactive force field to elucidate atomistic mechanisms of tribochemical reactions at a sliding interface between fully hydroxylated amorphous silica and oxidized silicon, with the amount of interfacial water treated as a controlled variable. The motivation is nanoscale friction and wear of silicon materials in humid environments, including atomic force microscopy observations in which silicon wear can depend strongly on relative humidity and in which Si–O–Si bridge formation across contacting surfaces has been proposed as a key tribochemical channel. The simulations adopt a slab-on-slab contact intended to mimic experimentally relevant contact widths while allowing explicit control of water confined under periodic boundary conditions. Jejoon Yeon, Adri C. T. van Duin, and Seong H. Kim connect these reactive trajectories to the broader literature on humidity-dependent silicon tribology.

## Methods

**1 — MD application (ReaxFF tribochemistry).** **Force field:** **Fogarty *et al.*** **Si/O/H\(_2\)O** **ReaxFF** set (cited as the authors’ **Si/O/water** choice). **Engine / code:** **LAMMPS** reactive MD. **Geometry:** **slab-on-slab** contact between **hydroxylated amorphous SiO\(_2\)** and **oxidized Si(100)** in a **3.19 × 3.19 × 7.0 nm\(^3\)** periodic cell (**~3.2 nm** in-plane width to mimic **AFM**-scale contacts). **Surface preparation:** **a-SiO\(_2\)** prepared by **melt/quench** (**3000 K → 300 K**); **Si(100)** oxidized with **300 O\(_2\)**-equivalent oxygen insertions at **300 K** for **400 ps** (**100 fs** damping noted for that oxidation segment); both slabs **hydroxylated** with **300 H\(_2\)O** at **300 K** **NVT** until silanol densities plateau (**SI Figures S1–S2**, **Table S1**). **Shear protocol:** (i) **vertical compression**, (ii) **equilibration**, (iii) **1 ns** lateral slide at **10 m/s** (**0.01 nm/ps** along **x** on the **top rigid** silica block), (iv) **100 ps** pull-off at **20 m/s** along **z**. **Normal load:** **1 GPa** maintained on the **top rigid** body during sliding (**mimicking cited AFM studies**). **Water coverage:** **0**, **20**, **50**, or **100** interfacial **H\(_2\)O** molecules (**100 ≈ full monolayer**, **50 ≈ 60–70%**, **20 ≈ 30–40%** of the interface in their cell). **Temperatures:** **300**, **500**, and **700 K** cases reported for thermal sensitivity. **Ensemble:** **NVT** with **Nosé–Hoover** thermostat for all MD segments described. **Timestep:** **0.25 fs** (explicit statement in **Simulation Methods**). **Barostat:** **N/A —** load is imposed mechanically (**1 GPa** target) rather than a **stress-fluctuation barostat**. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** the study **uses** the published **Fogarty** parametrization without refitting here.

**3 — Static QM.** **N/A —** not used.

**4 — Experiments cited.** **N/A as new experiment** — **AFM**/**tribology** literature motivates boundary conditions only.

## Findings

**Dry interface.** With **no** interfacial **water**, **ReaxFF-MD** shows **substantial cross-interface atom transfer** during **1 GPa** sliding; mixing begins with **dehydroxylation** followed by **Si–O–Si** bridges spanning the **a-SiO\(_2\)** and **oxidized Si(100)** slabs (**abstract**).

**Submonolayer water.** **20** or **50** **H\(_2\)O** molecules enable **dissociative** pathways that still produce **Si–O–Si** bridges and **sustain transfer**, consistent with **humidity-assisted** tribochemistry discussed for **AFM** wear.

**Near-monolayer water.** **100** **H\(_2\)O** (**~full monolayer** in their cell) **suppresses transfer** because **Si** sites at the sliding plane are **hydroxyl-terminated** instead of forming as many **interfacial Si–O–Si** bridges (**abstract**).

**Temperature.** Additional runs at **500 K** and **700 K** (with the same mechanical protocol) probe how **thermal activation** alters **reaction pathways** (**Simulation Methods** paragraph).

**Experimental context.** The **Introduction** links these **coverage-resolved** mechanisms to **non-monotonic relative-humidity** wear trends in **AFM** (including **high-RH** separation of asperities by **multilayer water**).

## Limitations

- Idealized **planar** contact vs **asperity-dominated** real interfaces.

## Relevance to group

Foundational **Langmuir** tribochemistry paper from **van Duin**’s group on **silicon oxide** sliding.

## Citations and evidence anchors

- **DOI:** [10.1021/acs.langmuir.5b04062](https://doi.org/10.1021/acs.langmuir.5b04062) (`papers/Yeon_Langmuir_2016.pdf`).
- Text-aligned pointers: `normalized/extracts/2016yeon-venue-la5b04062_p1-2.txt`

## Reader notes (navigation)

- Companion tribochemistry: [[2016wen-applied-surf-atomic-insight]]; hub: [[reaxff-family]], [[theme-oxides-silica-ceramics]].

## Related topics

- [[reaxff-family]]
