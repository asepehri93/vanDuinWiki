---
id: paper:2020dasgupta-j-phys-chem-simulations-biodegradation
type: paper
title: "Simulations of the Biodegradation of Citrate-Based Polymers for Artificial Scaffolds Using Accelerated Reactive Molecular Dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:application
  - task:validation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.0c03008"
year: 2020
authors:
  - "Nabankur Dasgupta"
  - "Dundar E. Yilmaz"
  - "Adri van Duin"
venue: "J. Phys. Chem. B 124:5311-5322 (2020)"
pdf_sha256: "d836bd4e827e526cd18607a93907661ed8bf9c5cc7997cea178e3d1aec1ec6b5"
pdf_path: "papers/Dasgupta_Citrate_JPC_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020dasgupta-j-phys-chem-simulations-biodegradation -->

**ReaxFF** simulations of **poly(1,6-hexanediol-co-citric acid)** use **CHON-2017_weak** with a **bond-boost / restrain-energy** protocol (after Vashisth *et al.*) to make room-temperature hydrolysis accessible, benchmark barrier trends against **literature QM**, and compare **chemical** plus **uniaxial mechanical** degradation of **polymer bundles** in water at **300 K**.

## Summary

The authors study two citrate-based polymer classes—**polyester (PE)** and **polyester–ether (PEE)**—that carry both **ester** and **ether** linkages, using **accelerated ReaxFF MD** so that hydrolysis can be forced at 300 K despite nanosecond affordable windows. A **restrain (bond-boost) potential** adds targeted energy to tagged atom pairs once pre–transition-state geometries are met, with parameters \((F_1, F_2, R_{12})\) scanned in **NVT** runs to minimize ReaxFF barriers for each hydrolysis channel; those barriers are compared to **DFT/MP2 literature** values for model ester and ether hydrolysis. Large **bundles** (10 chains × 20 monomers, ~20 Å bundle diameter, **3000** water molecules) are built in-house, relaxed with **NVT** then **NPT** equilibration, and subjected to **bond-boosted NVT** hydrolysis in boxes listed in the paper (e.g. **33.5 × 33.5 × 150 Å** for PE at **0.868 g cm\(^{-3}\)**). A second set of **restraint parameters** illustrates **selectivity** (favor ester over ether by lowering boost). **Longitudinal** tensile tests at **\(1\times 10^8\)** and **\(2\times 10^8\ \mathrm{s}^{-1}\)** probe modulus on pristine and **partially hydrolyzed** bundles.

## Methods

**1 — MD application (reactive, polymer + water).**

- **Engine / integrator:** ReaxFF with **leapfrog Verlet** integration; **QEq** charges; **CHON-2017_weak** parameter set for **hydrocarbon–water** weak interactions; short-range **5 Å** cutoff, Coulomb **10 Å** (as stated in *Computational Details*). **N/A** — the article text does not name a standalone MD package (see SI for implementation notes).
- **System size & composition:** **PE** and **PEE** bundles: **10** chains, **20** monomers each, bundle diameter **~20 Å**; **3000** explicit water molecules. Final hydrolysis cells: **PE** box **33.50 × 33.50 × 150 Å**, density **0.868 g cm\(^{-3}\)**; **PEE** **31.40 × 31.40 × 245 Å**, **0.885 g cm\(^{-3}\)** (Table 1).
- **Boundaries / periodicity:** **Three-dimensional periodic** simulation cells for bulk **bundle** models (as standard for the reported box dimensions).
- **Ensemble / stages:** Energy minimization; **NVT** **100 ps**; **NPT** **~200 ps** to reach **~0.8–1.0 g cm\(^{-3}\)**; production **bond-boosted** hydrolysis in **NVT** at **300 K**. For **restraint activation**, when all distance criteria are met the extra **\(E_\mathrm{res}\)** is applied for **15,000** steps (**3.75 ps** at the paper’s step length—see **timestep**). **N/A** — **NVE** is not the production ensemble for the large-bundle hydrolysis stage.
- **Timestep:** **0.25 fs** (inferred: **3.75 ps / 15,000** steps in the **restraint** subprotocol).
- **Duration / stages:** **100 ps** **NVT** + **200 ps** **NPT** equilibration; hydrolysis and mechanical runs continue as in *Results* (multi-segment, **N/A** for a single “production” length in one line—stated per figure/table in the PDF). **N/A** — **metadynamics / umbrella / replica exchange** are **not** used; **enhanced** chemistry uses **bond-boost / restrain** only.
- **Thermostat:** **Berendsen**, temperature damping **100 fs**, applied in “all MD simulations” per *Computational Details*.
- **Barostat: N/A** — *NPT* is only the **~200 ps** equilibration stage; the analysis narrative focuses on **NVT** hy­droly­sis. **Hydrostatic pressure** servicing is implied only in that equilibration window, not in the final **NVT** **bond-boost** runs. **N/A** — anisotropic stress control not detailed in the main text.
- **Temperature:** **300 K** for biodegradation and mechanical tests; **N/A** for broad multi-\(T\) sweeps in this study (barrier search uses isothermal NVT as described).
- **Pressure: N/A** in the **NVT** **bond-boost** **production** windows (isochoric **NVT** for those segments).
- **Electric field: N/A** — no applied field in the **MD** protocol.
- **Replica / enhanced sampling: N/A** for umbrella or metadynamics; **bond-boost / restrain energy** accelerates **specific** **hydrolysis** pathways.

**Mechanical testing:** uniaxial **strain** along the **longitudinal** **bundle** axis at **\(1 \times 10^8\)** and **\(2 \times 10^8\ \mathrm{s}^{-1}\)** on prehydrolyzed and partially hydrolyzed systems.

**2 — Force-field / QM validation.** **N/A** — the paper does **not** re-fit ReaxFF parameters; it **adopts** **CHON-2017_weak** and **benchmarks** **ReaxFF** ester/ether **barrier heights** (reported as **~23** and **~49 kcal mol\(^{-1}\)** in the discussion) against **published** **DFT/MP2** literature on model hydrolyses.

## Findings

- **Chemical degradation:** ReaxFF barrier estimates for model **ester** and **ether** **hydrolyses** are reported to agree **semiquantitatively** with **prior *ab initio*** studies, supporting use of the force field in this **polymer + water** context. In **PEE**, **RDFs** and **restraint energies** show **faster** **ester** scission and **favorable selectivity** when **boost** parameters are tuned; lowering parameters can **nearly** **suppress** **ether** **hydrolysis** while leaving **ester** reactivity, demonstrating **restraint selectivity** between **functional** groups in one polymer.
- **Comparisons:** **QM** **literature** barriers and mechanisms for **methyl** **acetate**-like and **ether** model reactions serve as the **DFT/MP2** **references**; **N/A** — the paper is **not** a direct head-to-head **new** DFT PES study of the full polymer, but a **ReaxFF-vs-literature** consistency check.
- **Sensitivity / levers:** **restraint** \((F_1, F_2, R_{12})\) sets control **which** **bonds** **react** and **reaction** **priority**; **lower** **boosts** **reduce** **ether** paths **relative** to **ester**. **Strain rate** increases the **tensile** **modulus** in the two simulated rates, showing **rate-dependent** **mechanical** response. **PEE** exhibits a **higher** **tensile** **modulus** but **yields** **sooner** than **PE** under the reported tests, so **PE** is described as more **ductile** than **PEE** in this comparison.
- **Limitations (as in the work):** **Accelerated** **MD** is **not** a literal **laboratory** **timescale**; **enzymatic** pathways, **pH** variation, and **device-scale** **transport** are **outside** the **atomistic** model. **Viscous** **losses** and **very** **long** **creep** of **entangled** **matrices** are not resolved.

## Limitations

**Bond-boost** trajectories are biased toward reaction; **clinical** **in vivo** **degradation** includes **biological** and **continuum** transport physics not in the model.

## Relevance to group

**Penn State / van Duin-group** ReaxFF on **biodegradable** **elastomers** with a documented **restraint** / **Vashisth**-type **ReaxFF** **acceleration** **workflow** tied to **QM** **barrier** **checks** and **mechanics**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcb.0c03008](https://doi.org/10.1021/acs.jpcb.0c03008)

## Related topics

- [[reaxff-family]]
