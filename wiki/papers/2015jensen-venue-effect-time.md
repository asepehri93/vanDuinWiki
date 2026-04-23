---
id: paper:2015jensen-venue-effect-time
type: paper
title: "The Effect of Time Step, Thermostat, and Strain Rate on ReaxFF Simulations of Mechanical Failure in Diamond, Graphene, and Carbon Nanotube"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:nose-hoover
  - keyword:graphene-carbon
  - keyword:lammps
source_refs: []
doi: "10.1002/jcc.23970"
year: 2015
authors:
  - "Benjamin D. Jensen"
  - "Kristopher E. Wise"
  - "Gregory M. Odegard"
venue: "J. Comput. Chem."
pdf_sha256: "9ce746df1d397ff79aa11bf835bd1fc3672d9f47083747da04c0edbacb3afeb0"
pdf_path: "papers/ReaxFF_others/Jensen_et_al-2015-Journal_of_Computational_Chemistry.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015jensen-venue-effect-time -->

## Summary

Reactive simulations of **mechanical failure** are sensitive to numerical choices: **integration timestep**, **thermostat** algorithm and coupling strength, and **loading rate** can shift predicted strength and failure mode even when the same **ReaxFF** parameterization is used. This study systematically varies these controls for **ReaxFF** simulations of **tensile fracture** in **diamond**, **single-layer graphene**, and a **carbon nanotube** using the **Chenoweth C/H/O** reactive force field. **Stress–strain** curves are compared across thermostat choices, timestep sweeps, and strain-rate decades, and results are discussed relative to **literature** mechanical benchmarks for carbon allotropes.

The paper’s practical message is **controls-first**: before debating **force-field** **physics**, simulations of **failure** should document **timestep**, **thermostat** coupling, and **strain rate** because those knobs can move **peak** **stress** and **ductility** as much as small **parameter** tweaks.

## Methods

**Potential (force-field training context).** All fracture sensitivity tests use the **Chenoweth *et al.* ReaxFF C/H/O** parameterization—the combustion-oriented fit whose **mechanical** performance is being stress-tested.

**MD application — systems, code, and stress model.** **ReaxFF** tensile tests are run in **LAMMPS** on three **periodic** carbon models used throughout the parameter sweeps: **bulk diamond** (**864 atoms**, **[111]** tensile axis), **single-layer graphene** (**1008 atoms**, in-plane periodicity, **0.34 nm** effective thickness for stress reporting), and a **(12,0)** **CNT** (**1152 atoms**, axial periodicity, cylindrical shell volume definition for stress). **True strain** and **virial (true) stress** definitions follow the **Computational Details** section.

**Ensembles, barostat, temperature.** Samples are **equilibrated at 300 K** for **10–40 ps** (multiple seeds reported) before **deformation**. **Diamond** and **graphene** runs use a **Berendsen barostat** to keep **zero lateral pressure** while axially loading, allowing **Poisson contraction**; the **CNT** uses axial periodicity with the lateral treatment described in the article.

**Timestep sensitivity.** The timestep study strains each system with **Δt** from **1.0 fs down to 0.1 fs** at the fixed **high strain rate** used in Fig. 5 (**~2.2×10⁹ s⁻¹**; the publisher PDF line-breaks the exponent) to probe stability near fracture.

**Thermostat sensitivity.** The authors compare **Berendsen**, **Nosé–Hoover**, and **Langevin** thermostats, including a **wide sweep of coupling constants** (**2, 25, 250, 2500 fs**) for the **Berendsen** case (other thermostats discussed with the same representative damping where plotted).

**Strain-rate sensitivity.** Additional sweeps vary **applied strain rate** to identify a **rate-independent** regime and a **high-rate** regime where **inertial** effects appear.

**Loading ensemble.** **Stress–strain** production runs are **thermostatted** **constant-volume** tensile tests at **300 K**; **diamond** and **graphene** use a **Berendsen barostat** on **lateral** directions to maintain **~zero lateral pressure** while axially loading (**Computational Details**), rather than **NPT** hydrostatic control of the full cell.

**Force-field reparameterization / static QM.** **N/A —** this paper is a **controls** study on an existing **ReaxFF** table, not a new QM training manuscript.

## Findings

**Thermostat and coupling.** **Stress–strain** curves are **largely insensitive** to thermostat **algorithm** if coupling is **not too weak**; **very small** damping (**~2 fs** in their Berendsen sweep) can **artificially quench** distant segments after fracture, whereas **very large** damping (**~2500 fs**) fails to hold **300 K** faithfully during rapid **exothermic** bond rupture—see **Figs. 9–11** for the detailed argument.

**Timestep.** **1.0 fs** can **shift** predicted **failure strain** (example discussed for **graphene**) and even show **energy drift** precursors in **diamond**; **≤0.25 fs** behaves more consistently in the tests shown.

**Strain rate.** Below a **material-dependent maximum strain rate**, responses are approximately **rate-independent**; above it, **inertial** effects contaminate the **measured** strength.

**Comparisons to references.** Benchmarked **elastic** and **failure-related** quantities for **Chenoweth** carbon models deviate from selected **experimental/QM** literature values in ways the authors tabulate—highlighting **validation** needs when using this parameter set for **mechanics** rather than combustion chemistry alone.

## Limitations

Finite simulation cells cannot capture long-wavelength **crack** instabilities; thermostats alter **heat** transport near **crack tips** and may bias ductile versus brittle appearance.

## Relevance to group

Practical **sensitivity-analysis** guidance for **ReaxFF mechanical failure** workflows distinct from reaction-focused training.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1002/jcc.23970](https://doi.org/10.1002/jcc.23970) (`papers/ReaxFF_others/Jensen_et_al-2015-Journal_of_Computational_Chemistry.pdf`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
