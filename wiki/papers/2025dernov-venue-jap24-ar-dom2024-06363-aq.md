---
id: paper:2025dernov-venue-jap24-ar-dom2024-06363-aq
type: paper
title: "Mapping the structural–mechanical landscape of amorphous carbon with ReaxFF molecular dynamics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:reactive-md
source_refs: []
doi: "10.1063/5.0246126"
year: 2025
authors:
  - "A. Dernov"
  - "M. Kowalik"
  - "A. C. T. van Duin"
  - "T. Dumitrică"
venue: "J. Appl. Phys."
pdf_sha256: "5294642426f08dd40ce43416a34fb1b8cd0698286751533ba256241a8d6d67a4"
pdf_path: "papers/Dernov_Kowalik_amorphous_carbon_JAP2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025dernov-venue-jap24-ar-dom2024-06363-aq -->

!!! note "Corpus note"
    The primary PDF is an AIP **author-query / proof** galley (`Dernov_Kowalik_amorphous_carbon_JAP2025_galley.pdf`); pagination in the extract may read `000000` pending final issue assignment.

## Summary

The paper uses **ReaxFF molecular dynamics** with **C-2013** and **CHON-2019** parameter sets to generate **liquid-quenched** models of **amorphous carbon (a-C)** spanning **0.96–3.29 g cm\(^{-3}\)**, then performs **uniaxial tensile** simulations to relate **ring statistics** and **hybridization** to **elasticity**, **plasticity**, and **fracture**, including **oxidative** scenarios with added **O\(_2\)** and selected **nanostructures** (slabs, **a-CNTs**, **partially amorphous CNTs**).

## Methods

- **Force fields:** **ReaxFF** **C-2013** and **CHON-2019** (same carbon parameters; differs in angle/dihedral terms; **CHON-2019** used where **oxygen chemistry** in fractured gaps is relevant).
- **a-C generation (liquid quench):** **8000 C** **atoms** in an orthorhombic **3D PBC** **periodic** cell; target **density** via box volume; **heat 300→3000 K** at **200 K ps\(^{-1}\)**; **hold 3000 K** for **0.5–1 ns**; **cool to 300 K** at **5 K ps\(^{-1}\)** under **NVT** with **Berendsen** **thermostat** (**100 fs** damping); **Δt = 0.1 fs** during melt/quench. **Post-quench NPT** **equilibration** at **300 K**, **1 atm** **isotropic pressure**, **Δt = 0.25 fs**, **Berendsen** **barostat** (**100 fs** damping). Ensembles of **three** lowest-energy replicas per target **density** were analyzed.
- **Derived structures:** **Slabs**, rolled **a-C nanotubes**, and a **partially amorphous** tube on a crystalline **double-walled** template built from sliced/rolled a-C models with additional heating/annealing as described.
- **Mechanical loading:** **Room-temperature**, **1 bar**, **NPT** integration (**Martyna–Tobias–Klein**), **uniaxial tensile strain** typically **0.5% ps\(^{-1}\)**. Selected runs paused to insert **100 O\(_2\)** molecules in opened cracks, then resumed. **AMS** and **LAMMPS** used for MD; **ISAACS** for structural analysis; ring detection with **King** shortest-path rules (**≤36** rings, neighbor cutoff **1.9 Å**). **N/A — electric field**; **N/A — umbrella / metadynamics** (tensile MD is the primary rare-event tool here).
## Findings

- **Structure:** Low-density **a-C** shows **bimodal** ring statistics (small **6-rings** plus medium **~12-rings**); **ta-C** at higher density shows **unimodal** small-ring dominance; **g(r)** and angle distributions shift from graphite-like toward diamond-like as density increases.
- **Elasticity:** Reported **Young’s moduli** rise strongly with density (e.g., **a-C ~34–156 GPa** and **ta-C up to ~535 GPa** depending on model/density in the article’s Fig. 3). **Elastic isotropy** in bulk responses is emphasized.
- **Plasticity and fracture:** Post-yield behavior is tied to **ring-size expansion** and **C–C** bond reactivity; **ta-C** shows much larger **plastic strain** before failure, associated with **sp\(^3\)→sp\(^2\)** conversion during loading. Ultimate failure involves **reactive cracks** with long **sp** chains; **O\(_2\)** in the crack **reduces** stress-bearing capacity by attacking chains (**Fig. 7** scenario).
- **Nanostructures:** **a-CNT** fracture is **circumferential**; **pa-CNT** fails from the **outer a-C wall** inward, while **crystalline** walls exhibit **helical** cracking patterns as described in the text and figures.
## Limitations

**ReaxFF** **C/H/O** models may miss some **defect** and **oxidation** channels; **quench** protocol sets **a-C** topology; **proof/galley** PDF may differ from final **pagination**. **Tensile** rates and **O\(_2\)** insertion are **idealized** crack scenarios.

## Relevance to group

**Dernov**, **Kowalik**, **van Duin**, **Dumitrică**: **a-C** **structure–mechanics** and **oxidative** **fracture** with **ReaxFF**—relevant to **carbon** **tribology** and **mechanics** threads.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1063/5.0246126](https://doi.org/10.1063/5.0246126)

## Related topics

- [[reaxff-family]]
