---
id: paper:2024kehan-wang-j-phys-chem-multiple-fidelity-method
type: paper
title: "A Multiple-Fidelity Method for Accurate Simulation of MoS2 Properties Using JAX-ReaxFF and Neural Network Potentials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:reaxff-lineage
  - method:ml-potential
  - method:reaxff
  - material:tmd
  - task:method-development
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:neb
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.3c03080"
year: 2024
authors:
  - "Kehan Wang"
  - "Longkun Xu"
  - "Wei Shao"
  - "Haishun Jin"
  - "Qiang Wang"
  - "Ming Ma"
venue: "J. Phys. Chem. Lett. 2024, 15, 371-379"
pdf_sha256: "91170be150747dafa18fe7cd3717774115eb0e2d249540f6541e7d6e8f4f1671"
pdf_path: "papers/ReaxFF_others/wang-et-al-2024-a-multiple-fidelity-method-for-accurate-simulation-of-mos2-properties-using-jax-reaxff-and-neural.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024kehan-wang-j-phys-chem-multiple-fidelity-method -->

## Summary

The authors combine **JAX-ReaxFF** (automatic-differentiation ReaxFF optimization against DFT) with **neural network potentials**: ReaxFF-generated data **pretrain** SchNet, then **DFT** finetunes ("multiple fidelity"), improving MoS2 property modeling; a **Mo-S-H** extension with **MACE** reports **~20%** lower energy RMSE versus training from scratch.

## Methods

**Step A:** Fit **ReaxFF for MoS2** with **JAX-ReaxFF** using DFT training items from prior work (cited **ref 17** in the letter): **372** total training items split into **3** charge-based, **78** geometry-based, and **291** energy-based items over **425** geometries (**D1**), including **88** Mo-S-only energy items on **109** geometries (**D2**). Loss is weighted MSE between ReaxFF and DFT targets (weights from ref 17). **Step B:** Train **NNP-SchNet** on **10,000** MD samples from **JAX-ReaxFF-MoS2**. **Step C:** Finetune on **400** held-out **DFT** points (**D2**) without new DFT. **Mechanical tests:** **LAMMPS** stress-strain and **stress-fluctuation** elastic properties (details in **SI Section S2**). **NEB** in **LAMMPS** with **JAX-ReaxFF-MoS2** for **1T to 2H** barriers (**Table 4**, comparison to literature **~1.04 eV** per formula unit from Guo et al.). **Mo-S-H:** **NNP-MACE** pretrained on ReaxFF data then finetuned.

**Software/autodiff context.** **JAX-ReaxFF** uses automatic differentiation through the **ReaxFF** energy expression so gradients with respect to **parameters** accelerate **weighted least-squares** optimization versus finite-difference parameter sweeps. **SchNet** training consumes **MD** snapshots from the optimized **ReaxFF** field to build **local** environment embeddings before **DFT** finetuning on held-out **energies**/**forces**.

**1 — MD application (property / stress runs).** **Engine:** **LAMMPS** (stress-strain, **NEB** paths cited) with **JAX-ReaxFF-MoS2** as stated. **System:** **MoS2** **supercell**s / unit cells in **3D PBC** for the mechanical and kinetics **production** work (**~400+ atom**-scale **cells** in letter/SI, exact counts: **see PDF**). **NVT** **Molecular dynamics** to generate the **10,000**-snapshot **ReaxFF**-trained **trajectory** pool; **1 ns**-class **equilibration** and **production** **duration** in **SI S2** (if not in this blurb, treat as **N/A** here and read **SI**). **Thermostat, timestep, barostat, GPa** **stress** targets: **0 GPa** isotropic **hydrostatic** not assumed—use **NPT** only where the letter specifies (otherwise **N/A** in this one-page summary). **T**-controlled sampling as in the letter. **Electric field:** **N/A**. **Replica / umbrella / metadynamics:** **N/A**; **NEB** is the barrier tool. **2 — Force-field training (JAX-ReaxFF, SchNet, MACE).** The steps **A–C** in **Methods** above. **3 — Static QM (DFT training).** DFT from reference **17** and held-out **D2**; **M06-2X** etc. not the headline—**see cited training literature** for the exact functional in each training item.
## Findings

**JAX-ReaxFF-MoS2** yields **tensile strength ~22 GPa**, closer to **experiment and DFT (~21-22 GPa)** than original ReaxFF (**~24 GPa**). Elastic properties and Poisson ratio show **reduced overestimation** versus legacy ReaxFF (**Table 3**, **SI Table S2**). **NEB** paths for **SL MoS2** **1T-2H** match DFT reference barriers better in the **transition region** than original ReaxFF. **SchNet** with ReaxFF pretraining plus DFT finetune improves **thermodynamic** descriptors (e.g. **convex hull**, **sulfur vacancy** formation, **S8** interaction tests in the letter). **MACE** on **Mo-S-H** reports **~20%** lower energy **RMSE** versus from-scratch training. The authors state the pipeline generalizes as **transfer learning** from a high-throughput cheap model to a data-sparse accurate model. **Comparisons** to **experiment**/**literature** (**Table 3**, **Guo et al.**, bulk moduli) are in the main bullets; **sensitivity** to data splits and pretraining is discussed in the letter/ **SI** rather than re-derived here. Use the **J. Phys. Chem. Lett.** **PDF** and **SI** for numerical authority.
## Limitations

**JAX-ReaxFF**, **SchNet**, and **MACE** inherit **training-set** and **functional** biases; the **multiple-fidelity** pipeline is demonstrated for **MoS₂** and **Mo–S–H** extensions—transfer to other **TMDs** or **electrode** environments requires refitting and validation.

## Relevance to group

Illustrates **transfer learning** from **ReaxFF**-generated data to **neural** potentials for **2D** chalcogenides—adjacent to **ReaxFF** and **MLIP** methodology threads in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.3c03080](https://doi.org/10.1021/acs.jpclett.3c03080)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
