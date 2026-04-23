---
id: paper:2015hong-venue-research
type: paper
title: "Molecular dynamics simulations of the oxidation of aluminum nanoparticles using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jpcc.5b04650"
year: 2015
authors:
  - "Sungwook Hong"
  - "Adri C.T. van Duin"
venue: "Journal of Physical Chemistry C (ASAP PDF in corpus; see DOI)"
pdf_sha256: "6974038ec96656cf9e22642917f384bd696f2822abb69a6d6626a0a0612ad676"
pdf_path: "papers/Hong_AlOx_JPCA_2015_ASAP.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015hong-venue-research -->

## Summary

Hong and van Duin report **ReaxFF molecular dynamics** of **aluminium nanoparticle (ANP)** oxidation at **300, 500, and 900 K** for two **initial oxygen densities** (**0.13** and **0.26 g cm\(^{-3}\)**). The article argues that **O\(_2\)** adsorption and dissociation create **localized hot regions** and **void**-like disrupted metal/oxide regions at the surface; a **bond-restraint** barrier scan reported in the paper finds that **voids** can **lower** an illustrative **oxygen diffusion barrier** by up to **~92%** and change the step from endothermic to **exothermic** in that model setup, after which **oxide** growth proceeds by **accelerated oxygen transport**. The authors further relate **oxide thickness** and **density** to the **combined** effects of **temperature** and **oxygen density**, and state **qualitative agreement** with selected **experimental** literature on aluminium oxidation kinetics.

## Methods

**Force-field lineage (Al/O).** Simulations use the **ReaxFF** reactive force field for **aluminium/oxygen** chemistry as summarized in the article (energy decomposition and QEq-style charge treatment as referenced there), including a **validation** trajectory set on a **bare Al (431) slab** with oxygen before the **ANP** cases discussed in the Results section.

**MD application — engine, cells, boundaries.** **ReaxFF MD** is carried out with the **29 Jan 2014** **LAMMPS** build cited in the paper. **Two** primary setups are reported: (**i**) a **504-atom Al (431) slab** in a **1.40 × 1.28 × 10.0 nm** cell with **150 O\(_2\)** molecules for the **low-pressure validation** trend study (additional high-density validation case described in the article); and (**ii**) an **864-atom amorphous Al cluster** (~**2.8 nm** diameter) in a **5.0 × 5.0 × 5.0 nm** box with **300** or **600** **O\(_2\)** molecules, giving the **0.13** and **0.26 g cm\(^{-3}\)** initial oxygen densities used for the ANP oxidation sweeps. **Three-dimensional periodic boundary conditions** are used as stated for these gas–particle cells.

**Ensemble, thermostat, timestep, duration.** For the canonical **ANP oxidation** production runs, the authors use the **NVT** ensemble (**constant volume**) with a **Nosé–Hoover** thermostat (**temperature damping parameter 100 fs**) and an integration **timestep of 0.2 fs**, for **5,000,000** steps (**1.0 ns** total) at each reported temperature/density combination. A separate **NVE** demonstration at **low oxygen density** (**0.01 g cm\(^{-3}\)**) is described to examine **energy-conserving** heating from oxidation exothermicity without thermostatting.

**Barostat / pressure.** **N/A —** the primary **ANP** runs are **constant-volume NVT**; the article’s **NVE** subsection is used to discuss **microcanonical** behavior at low oxygen density rather than constant-pressure control.

**Electric field, replica sampling.** **N/A —** not used as a driving force in the protocol described for these oxidation trajectories.

## Findings

**Mechanism and microstructure.** The authors connect **highly exothermic early oxygen consumption** to **short-lived hot surface regions**, **void** formation near the outer surface, and rapid initial **oxide** thickening, then analyze how **temperature** and **oxygen density** modulate **oxide thickness/density** and **oxidation-state** partitioning along the trajectory.

**Comparisons.** **Bare-slab** simulations at elevated oxygen density are used to recover **qualitative** trends of **temperature-dependent limiting oxide growth** relative to an cited **XPS** study, while acknowledging **time-scale** and **pressure** gaps between simulation and experiment.

**Sensitivity / design levers.** Reported sweeps vary **system temperature** (**300–900 K** for the ANP cases in Section 3.3) and **initial oxygen density** (**0.13 vs 0.26 g cm\(^{-3}\)**), and include the **NVE** low-density control to argue that **void-assisted** pathways are not an artefact of the **thermostat** alone.

**Limitations (as framed in the article).** The manuscript discusses **high oxygen densities** relative to ambient STP, **nanosecond** horizons, and the role of the **thermostat** as a stand-in for **environmental heat transfer** for small nanoparticles—see the **Discussion** for the authors’ caveats.

## Limitations

- Nanoscale MD still uses high **effective pressures/temperature ramps** compared to many experiments; quantitative burning rates require careful upscaling analysis.
- ASAP PDF may differ slightly in pagination from the final issue version.
- **Particle** **size** **polydispersity**, **native** **oxide** **thickness** distributions, and **alloying** **additives** in **technical** **Al** powders can shift **oxidation** **kinetics** beyond the **idealized** **ANP** **cores** modeled here.

## Relevance to group

**Adri C. T. van Duin** co-authorship; strengthens the **Al/Al\(_2\)O\(_3\)** **ReaxFF** storyline used across combustion, propellants, and corrosion-related modeling.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5b04650](https://doi.org/10.1021/acs.jpcc.5b04650)

## Related topics

- [[reaxff-family]]
