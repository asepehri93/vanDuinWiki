---
id: paper:2015valega-venue-jp5105328
type: paper
title: "Study of Metal/Epoxy Interfaces between Epoxy Precursors and Metal Surfaces Using a Newly Developed Reactive Force Field for Alumina–Amine Adhesion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:neb
  - keyword:dft-static
  - keyword:classical-md
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/jp5105328"
year: 2015
authors:
  - "F. O. Valega Mackenzie"
  - "B. J. Thijsse"
venue: "J. Phys. Chem. C"
pdf_sha256: "91681ecc0830d1dc0efde8f2f7ddf13b093a84114c409f54d7b1aac91232ad34"
pdf_path: "papers/ReaxFF_others/Valega_Thijsse_JPC_C_2015_epoxide_amine_alumina.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015valega-venue-jp5105328 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi` and `pdf_path`.

## Summary

Valega Mackenzie and Thijsse develop a **ReaxFF** extension for **Al–N** interactions, merge it with prior **alumina–water** and **glycine** subsets, and study **amine-containing epoxy precursors** on **alumina** surfaces relevant to **aerospace** and **microelectronics adhesion**. **DFT + NEB** supplies **reaction-profile** training data; **room-temperature MD** compares **ammonia adsorption** between **ab initio MD** and **ReaxFF** as a spot check. **Dimethylamine** and **DETA** adsorption energies are sampled across **terminations** with **10** **approach conditions** each (abstract). **Mean** and **rms adsorption energies** vary strongly with **molecule/surface** pairing, and **precursor adhesion** decreases **linearly** with increasing **surface hydroxyl coverage** in the reported scans (abstract).

## Methods

**Force-field training.** **New terms:** **Al–N** ReaxFF parameters fit to **cluster** models and **interfacial reaction paths** for **amine** chemistry on **alumina**, merged with existing **Al–O/H** and **organics** blocks (abstract). **QM reference:** **DFT** with **NEB** for **reaction profiles** used as training targets. **Optimization workflow:** standard ReaxFF least-squares fitting as described in Methods (`pdf_path`).

**Static QM / DFT.** **DFT + NEB** for **reaction profiles** and **adsorption** references feeding the fit (abstract/introduction).

**MD application (validation + sampling).** **Engine:** **molecular dynamics** with **ReaxFF** as implemented in the software cited in **Computational methods** (`pdf_path`). **System:** **atomistic** **alumina** **slab** supercells with **amine** adsorbates (**NH₃**, **dimethylamine**, **DETA**) at **oxide** surfaces (atom counts in **`pdf_path`**). **Boundaries:** **3D PBC** in-plane with vacuum gap normal to the surface as defined there. **Room-temperature MD:** compare **NH₃ adsorption** on **alumina** between **ab initio MD** and **ReaxFF MD** (abstract). **Adsorption sweeps:** **dimethylamine** and **DETA** on multiple **alumina terminations** with **10** **approach** orientations each (abstract). **Ensemble:** **NVT** sampling at **room temperature** for these validation/sweep trajectories unless Methods specify otherwise. **Timestep / thermostat / duration:** tabulated in **`pdf_path`** (fs timestep, **production** lengths in **ps**/**ns**). **Barostat:** **N/A** for the headline **NVT** adsorption workflows unless Methods add **NPT** equilibration. **Pressure:** **N/A** — not a bulk **hydrostatic pressure** study in the abstract framing. **Electric field / enhanced sampling:** **N/A** in the abstract framing.

## Findings

**Parametrization quality:** The combined field reproduces targeted **geometries**, **binding energies**, and **NEB profiles** for the training sets described in the abstract.

**Adsorption variability:** **Mean** and **rms** **adsorption energies** depend strongly on the specific **molecule/surface** combination (abstract).

**Coverage trend:** **Epoxy precursor adhesion** decreases **linearly** with increasing **hydroxyl coverage** on the **alumina** surfaces studied (abstract).

**Comparisons:** **Ab initio MD** vs **ReaxFF MD** for **NH₃** adsorption is used as a **spot validation** of the new **Al–N** cross-terms (abstract).

**Sensitivity:** **Hydroxyl coverage** and **molecule/surface** pairing are the dominant levers on **mean**/**rms** binding statistics.

**Limitations / outlook:** **Cure chemistry**, **humidity**, and **contamination** superstructures remain beyond the sampled **precursor** **adsorption** models.

**Mechanistic context (intro):** Prior **DFT** on **methylamine** motivates **covalent Al–N** character via **lone-pair donation** to **undercoordinated Al**—consistent with treating these interfaces reactively rather than with pure **nonbonded** mixing rules.

## Limitations

**Interface models** omit full **bulk cure** chemistry, **humid aging**, and **contamination** superstructures. **ReaxFF transferability** is limited outside the **Al/O/N/C/H** training chemistry. Numerical **MD** settings and the full set of **surface terminations** are tabulated on **`pdf_path`**.

## Relevance to group

**Oxide–organic adhesion** **ReaxFF** methodology in the spirit of broader **interface** simulation work, authored at **TU Delft**.

## Citations and evidence anchors

- DOI `10.1021/jp5105328` — `papers/ReaxFF_others/Valega_Thijsse_JPC_C_2015_epoxide_amine_alumina.pdf`.
- `normalized/extracts/2015valega-venue-jp5105328_p1-2.txt`.

## Related topics

- [[reaxff-family]]
