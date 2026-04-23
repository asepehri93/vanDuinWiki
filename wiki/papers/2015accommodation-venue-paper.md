---
id: paper:2015accommodation-venue-paper
type: paper
title: "Molecular Dynamics Derived Gas-Surface Models for Use in Direct Simulation Monte Carlo"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:classical-ff
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
  - keyword:graphene-carbon
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: ""
year: 2015
authors:
  - "Neil Mehta"
  - "Deborah A. Levin"
venue: ""
pdf_sha256: "56c1626d29e98a72053f4047e4ac651f59a70a3b5f19cc6a4b1eaec2a7c04e7d"
pdf_path: "papers/Accommodation_paper_Dec15submitB.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015accommodation-venue-paper -->

## Summary

Molecular nitrogen–surface collisions on atomistically generated graphene and quartz sheets supply accommodation coefficients and post-collision velocity distributions for comparison with Maxwell and velocity-sampling gas-surface models in DSMC. The motivation is **aerothermodynamics** and **rarefied gas** applications where **wall** models must bridge **atomistic** scattering statistics and **continuum** or **DSMC** solvers; the paper’s graphene preparation uses **ReaxFF** relaxation to obtain **realistic** roughness and chemistry before extracting **scattering** kernels.

## Methods

This contribution is **experimental / computational fluid–surface coupling** in spirit: classical molecular dynamics generates nitrogen–surface collision statistics that feed gas–surface interaction models in DSMC (`papers/Accommodation_paper_Dec15submitB.pdf`). The authors do **not** report a new force-field fit—they apply existing empirical models, using **ReaxFF** relaxation to prepare corrugated graphene and Lennard-Jones-style non-reactive dynamics for N\(_2\) impingement as stated in the manuscript.

**Surface preparation (graphene).** Expanded graphene supercells (up to **512** carbon atoms) sit in a nominally **~17.08 × 19.72 × 25.00 Å** periodic box. **ReaxFF** relaxation is followed by **NPT** annealing at **1 atm** with a **Berendsen** barostat (**100 fs** damping) and **Berendsen** thermostat (**10 fs** coupling) while the temperature is stepped **300 K → 1000 K → 300 K** in **100 K** segments of **2 ps** each (**40 ps** total).

**Surface preparation (quartz).** Random **SiO\(_2\)** placement is minimized for **125 ps** at **0.25 fs** per step, then the slab is annealed with combined **NVT**/**NPT** segments from **300 K** toward **4000 K** in **100 K** increments of **2 ps**, yielding a **532**-atom quartz slab (**~17.32 × 19.98 × 22.53 Å**).

**N\(_2\) impingement trajectory bank.** Non-reactive van der Waals trajectories integrate **36,000** steps at **0.25 fs** (**9.0 ps** wall time per trajectory) with **<0.05%** energy drift as reported. About **2000** trajectories per incidence condition are accumulated on graphene at **1503** and **1100 m s⁻¹** with incidence angles **0°–80°**, and on quartz at **750**, **500**, and **250 m s⁻¹** with angles **10°–40°**. The checked-in PDF excerpt does **not** name the MD program explicitly—confirm the software string in the full PDF when auditing reproducibility.

**Not emphasized in the collision protocol:** replica exchange or other enhanced sampling; applied electric fields; production-stage reactive bond formation during the N\(_2\) impact ensemble (ReaxFF is used for graphene **preparation**, not as the integrator for the accommodation statistics bank).

## Findings

Post-collision trajectories partition into single-bounce, multiple-bounce-with-escape, and multiple-bounce-without-escape classes whose probabilities depend strongly on incidence angle, speed, and whether the prepared surface is smooth versus intentionally rough—a simple **mechanism**-level picture of how momentum is thermalized at the wall. Energy accommodation coefficients track the kinematic variables and surface topology. A velocity-sampling gas–surface interaction model implemented in DSMC reproduces Maxwell-model predictions when fed MD statistics from rough (diffuse) surfaces under the conditions tested, i.e. close **agreement** with Maxwell baselines **versus** the velocity-resolved kernel built from MD. **Sensitivity** to incidence **speed** and angle is strong: the **rate** at which trajectories escape after multiple encounters shifts the accommodation distribution enough that angle-averaged coefficients alone can mislead DSMC boundary models. **However**, the manuscript’s MD bank is non-reactive N\(_2\) scattering after **ReaxFF** surface prep, so catalytic chemistry and electronic stopping are outside scope. **Limitations** include dependence on the specific **temperature** annealing used to roughen graphene and on finite slab **thickness**; **future work** would extend the same MD→DSMC workflow to oxidized or contaminated skins once validated against molecular beams. Corpus **honesty**: quantitative tables beyond this summary live in the registered **PDF** `papers/Accommodation_paper_Dec15submitB.pdf`.

## Limitations

The manuscript excerpt in the corpus may omit some **figure** details; **DOI** is not populated in front matter here—anchor claims to the checked-in **PDF** and any updated **normalized** bibliography record when available. **Non-reactive** N\(_2\)–surface treatment limits chemistry beyond **physisorption**; **oxidized** or **contaminated** spacecraft materials may require extended models.

## Relevance to group

**Gas–surface** MD with **ReaxFF-prepared** carbon surfaces connects to broader **hypersonic** and **materials** simulation interests; use this page when tracing how **atomistic** trajectories feed **DSMC** boundary models rather than as a standalone **ReaxFF** reactivity study.

## Citations and evidence anchors

- Manuscript PDF: `papers/Accommodation_paper_Dec15submitB.pdf` (DOI not populated in front matter for this ingest).

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
