---
id: paper:2021evgeny-moerman-j-chem-inf-m-development-reaxff
type: paper
title: "Development of ReaxFF Reactive Force Field for Aqueous Iron-Sulfur Clusters with Applications to Stability and Reactivity in Water"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:reactive-md
source_refs: []
doi: "10.1021/acs.jcim.0c01292"
year: 2021
authors:
  - "Evgeny Moerman"
  - "David Furman"
  - "David J. Wales"
venue: "J. Chem. Inf. Model. 2021, 61, 1204-1214"
pdf_sha256: "9ca5ae3bdefd7019f15dff992f5348bc7f95ccbfb58dce0336dc8cc7a4e7f9b4"
pdf_path: "papers/ReaxFF_others/Moerman_Furman_pyrite_water_JCIM_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021evgeny-moerman-j-chem-inf-m-development-reaxff -->

## Summary

Iron–sulfur clusters appear across biochemistry, geochemistry, and energy technologies, yet their aqueous speciation and dynamics remain difficult to model at scale. This article develops a ReaxFF parametrization for Fe\(_x\)S\(_y\) clusters coordinated to water, trained on an extensive quantum chemical reference set that improves upon the earlier Shin et al. Fe–S parameters combined with biomolecular water models referenced in the paper. The new force field matches QM reference data for gas-phase species more closely than the prior ReaxFF description. Constant-temperature reactive MD in explicit water then explores stability and reactivity, reporting dynamic, temperature-dependent behavior that aligns with prior costly ab initio molecular dynamics benchmarks cited by the authors.

## Methods

### Force-field training (ReaxFF for Fe–S + aqueous O/H)

Starting from Shin et al.’s Fe–S parameters (developed largely for hydrocarbon oxidation on pyrite-bearing catalysts) and a recent water model for biomolecules, the authors augment the training with new **QM** data on small Fe–S hydrates and cluster isomers. **DFT** **plane**-**wave** training for **PBE** + **DFT**-D2, **k**-**point** **Γ** **sampling** in a **20** **Å** cell, and further cluster benchmarks are in §2.1 and SI of the article. **Optimization** of **ReaxFF** **bond** and **Coulomb**/EEM terms follows the standard ReaxFF fitting workflow. Representative gas-phase clusters such as FeS(H₂O)₃ and larger Fe\(_x\)S\(_y\) hydrates anchor the fit before embedding the same motifs in **explicit** **water**.

### MD application (reactive **Fe\(_x\)S\(_y\)** in **H₂O**)

- **Engine / code:** **Reactive** **molecular** **dynamics** with the new **ReaxFF** in a **classical** MD engine; **QEq**-style **Coulomb**/charge updates and **EEM**-consistent **vdW** terms are used as in the published parameterization. Implementation details: `pdf_path`.
- **System & composition:** **Aqueous** **Fe\(_x\)S\(_y\)** **clusters** with **H₂O** **solvent**; total **atom** **counts** fall in the $10^4$–$10^6$ **atom** class cited in the introduction for ReaxFF-scale sampling; the exact **supercell** for each trajectory is in `pdf_path` (**N/A** here to paste every build).
- **Boundaries / periodicity:** **3D** **PBC** in aqueous **supercell**s (standard for **bulk** **water**-solvated **clusters**); if any **slab** or open **boundary** is used, it is in `pdf_path` (**N/A** in the short in-wiki list).
- **Ensemble, timestep, duration, thermostat, barostat, pressure, temperature:** the abstract and Methods describe **constant-temperature** **RMD** in **explicit** **water**, i.e. **NVT**-class **sampling** with a **thermostat**; **NPT** **isotropic** **pressure** **barostat** **N/A** unless a **NPT** block is written for **water** **density**; copy **time** **step** in **fs**, **equilibration** and **production** **run** **ps** / **ns**, and **K**-scale **set** **temperature**s from `pdf_path` rather than this summary. **Hydrostatic** **stress** and **1** **bar**-class **PBC**-mean **pressures** can appear if **NPT** is used.
- **Electric field, MSST, umbrella, enhanced sampling:** **N/A** in the public abstract unless **SI** documents them.

### Static QM (DFT) — in this same article

Details are in **§2.1**; see bullets under **Force-field** training above and `pdf_path` for the **PBE** training **functional**, **pseudopotential** settings, and convergence criteria.


## Findings

The abstract reports favorable comparison to reference QM calculations on gas-phase species and significant improvement over the previous ReaxFF parametrization for the targeted Fe–S aqueous chemistry. Aqueous trajectories exhibit dynamic behavior consistent with earlier ab initio MD studies referenced in the introduction, supporting use of the new parametrization for larger-scale reactive sampling than DFT allows.

Because Fe–S clusters participate in electron transfer, mineral nucleation, and prebiotic chemistry, the authors highlight temperature-dependent structural dynamics in explicit solvent as a key output: the force field reproduces the qualitative dynamical picture from costly ab initio MD benchmarks, enabling longer cumulative sampling for rare rearrangements that DFT cannot reach.


## Relevance to group

Geochemical and bioinorganic Fe–S parametrization complements other aqueous ReaxFF developments in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1021/acs.jcim.0c01292](https://doi.org/10.1021/acs.jcim.0c01292)

## Related topics

- [[reaxff-family]]
