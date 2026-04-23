---
id: paper:2021dundar-e-yilmaz-j-chem-theor-machine-learning-assisted
type: paper
title: "Machine Learning-Assisted Hybrid ReaxFF Simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:ml-atomistic
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:machine-learning-potential
  - keyword:polymer
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.1c00523"
year: 2021
authors:
  - "Dundar E. Yilmaz"
  - "William Hunter Woodward"
  - "Adri C. T. van Duin"
venue: "J. Chem. Theory Comput. 2021, 17, 6705-6712"
pdf_sha256: "adbacf5877e71b69f05ab7e863a95c0b2dd4f912d3aa4f0c76ddaa53d08032bc"
pdf_path: "papers/Yilmaz_Hybrid_ReaxFF_JCTC_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021dundar-e-yilmaz-j-chem-theor-machine-learning-assisted -->

## Summary

Long-timescale **reactive polymer chemistry** with **ReaxFF** often hits a wall: fully reactive trajectories are expensive, yet **non-reactive** stages are needed for relaxation between rare reaction events. This **Journal of Chemical Theory and Computation** article introduces **Hybrid/Reax**, a workflow that **alternates** **reactive ReaxFF MD** with **non-reactive** equilibration stages. Between cycles, **machine learning (ML)** models predict parameters for a **non-reactive** classical force field from **updated bond topology** determined after reactive segments. A specialized **reactive-stage tracker** accelerates detection of chemistry events. The demonstration case is **cross-linking** of a **polyethylene-like** system built from **decane** with **dicumyl peroxide** initiators; the abstract reports that long hybrid trajectories on a **4660-atom** test system finish in under **48 hours** on a single **Xeon** versus about a **month** for pure ReaxFF on the same hardware (timing details in the paper).

## Methods

### MD application (Hybrid/Reax staging)

- **Engine / code:** Staged **reactive ReaxFF** **molecular** **dynamics** in **LAMMPS**-class workflows (stated in the **paper**) with **reactive**-stage event tracking; interleaved **ML**-mapped **classical** energy expressions for **non-reactive** equilibration segments, iterated until the authors’ cross-linking **chemistry** targets are met (`pdf_path`).
- **System & composition:** The benchmark uses a **decane**-parent **polymer**-like system with peroxide **initiator**s at **4660** **atoms** in the test box as quoted in the abstract; exact **stoichiometry** and box vectors: `pdf_path`.
- **Boundaries / periodicity:** The cross-linking **supercell** is treated with **3D** **PBC** as usual for **bulk** **polymer** **melts** unless the article specifies a **slab** setup; any non-**periodic** or fixed ends: `pdf_path`.
- **Ensemble, timestep, duration, thermostat, barostat, temperature:** **NVT** is typical for the **reactive** and **classical** **isothermal** stages, but the article should be followed for the actual **NVT**/**NPT** split, **thermostat** choices, and **NPT** **barostat** **pressure** when a **NPT** block is used. Set **temperature**s (e.g. in **K**) and **time step** in **fs** are in `pdf_path`. The wall-clock-quoted **~48 h** on one **Xeon** vs **1 month** pure-ReaxFF comparison refers to *aggregate* wall time; **ps** / **ns** of **reactive** vs **classical** **production** **run** segments: `pdf_path`.
- **Shear, electric field, MSST, umbrella, enhanced sampling:** **N/A** in the **abstract**-level **summary** unless a rare-event or **replica** scheme is **named**; **bond**-topology tracking is not umbrella sampling.

### Force-field training and ML (supporting the hybrid scheme)

- **N/A** as a classical “new CMA-ES” training article: the published **ReaxFF** and **ML** featurization support the hybrid workflow, with any new **QM** training details in **SI** (`pdf_path`).

### Static QM (DFT) — in this JCTC paper

- **DFT** or **CCSD(T)**-class references used to validate pieces of the **hybrid** pipeline (if any) are cited where the **authors** put them; **N/A** to restate a full DFT table here without `pdf_path` in hand.

## Findings

The benchmark achieves **cross-linking** of more than half of **80** PE molecules after hybrid cycling under the stated protocol, with a **large wall-time reduction** compared to brute-force ReaxFF MD for the same system on the quoted machine configuration. The paper frames this as evidence that **staged** reactive/non-reactive coupling with topology-aware ML can unlock chemistries that are otherwise inaccessible within practical compute budgets, while acknowledging dependence on ML coverage. For MAS documentation, preserve the explicit **hardware timing** caveat: reported speedups migrate with GPU/CPU generations and parallel efficiency.


## Reader notes (MAS / retrieval)

Anchor hybrid-workflow questions to **`10.1021/acs.jctc.1c00523`** and cite **Hybrid/Reax** staging explicitly when comparing to brute-force ReaxFF baselines.

## Relevance to group

**Adri C. T. van Duin** is senior author; defines **Hybrid/Reax** for long-time **reactive polymer** workflows in the **ReaxFF** ecosystem.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.1c00523](https://doi.org/10.1021/acs.jctc.1c00523)

## Related topics

- [[reaxff-family]]
