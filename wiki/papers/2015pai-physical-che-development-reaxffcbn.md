---
id: paper:2015pai-physical-che-development-reaxffcbn
type: paper
title: "Development of the ReaxFF CBN reactive force field for the improved design of liquid CBN hydrogen storage materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:polymer-organic
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1039/C5CP05486A"
year: 2016
authors:
  - "Sung Jin Pai"
  - "Byung Chul Yeo"
  - "Sang Soo Han"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "1d3b74a203bb4e5a1af4a73dfe521c6217c9f5d9a74487bf8338a90d85de6b96"
pdf_path: "papers/ReaxFF_others/Pai_BNCH_PCCP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015pai-physical-che-development-reaxffcbn -->

!!! abstract "Year vs slug"
The stable wiki `id` retains the **`2015pai-…`** slug for link stability; bibliographic **year** is **2016** per the published **PCCP** issue pages.

## Summary

**Liquid CBN (carbon–boron–nitrogen)** carriers such as **3-methyl-1,2-BN-cyclopentane** are attractive because they can plug into **existing liquid-fuel infrastructure**, but **liquid-phase** **hydrogenation/dehydrogenation** pathways are hard to map experimentally. This **PCCP** article develops **ReaxFF_CBN** from **B3LYP** **QM** data on **BN-substituted** cycles and small molecules, then validates that the fitted field reproduces **QM** **dehydrogenation** **pathways** and **energetics** for training cases. **ReaxFF MD** in **LAMMPS** on **~500**-monomer **liquid** cells (density set from **experiment**) compares **unimolecular** versus **bimolecular** dehydrogenation as temperature rises and contrasts **pentagonal** versus **hexagonal** liquid **CBN** motifs for **thermal stability** and **dehydrogenation kinetics**.

## Methods

### Force-field training

**QM reference:** **DFT** with the **B3LYP** hybrid functional (basis sets and SCF settings in the article/SI) supplies **bond dissociation** curves, reaction **energetics**, and **BN-substituted** cyclic **geometries** for **C/B/N/H** liquid **CBN** carriers. **Training set / targets:** reactions and RMSE tables enumerated in the main text and **ESI**. **Optimization:** **ReaxFF_CBN** parameters are adjusted until those **QM** benchmarks are satisfied within the reported tolerances. **Experimental** liquid **mass densities** constrain supercell volumes.

### MD application (atomistic dynamics)

**Engine:** **LAMMPS** with **ReaxFF_CBN** after **Cerius2**/**Dreiding** **pre-relaxation** of liquid cells. **System:** cubic **3D PBC** boxes of **~500** monomer units sized to **experimental** density for each **CBN** liquid composition (atom totals depend on monomer choice—see **PCCP** tables). **Ensemble / timestep:** **NVT** at fixed volume with **Nosé–Hoover** thermostat (**damping 1.0** in the paper’s units) and **Δt = 0.1 fs**. **Protocol:** equilibration near **300 K**, then **linear heating 300 → 2000 K** at **34 K/ps** to accelerate **dehydrogenation** while respecting stated **boiling** constraints for the modeled liquids. **Barostat / applied pressure:** **N/A** — volume set from experimental density, not **NPT** pressure control. **Electric field / enhanced sampling:** **N/A**.

## Findings

**Validation:** **ReaxFF_CBN** reproduces **QM** **dehydrogenation** **pathways** and **energetics** for the highlighted training reactions (additional tables in **ESI**). **Mechanism vs temperature:** **unimolecular** dehydrogenation dominates at **lower T**, while **bimolecular** channels grow in importance as **temperature** increases—consistent with higher collision rates in dense liquid. **Motif comparison:** **hexagonal** liquid **CBN** motifs are reported as preferable to **pentagonal** analogs when weighing combined **thermal stability** and **dehydrogenation kinetics** under the same heating ramps. **Outlook (authored framing):** the parametrization is positioned as a screening tool for **new liquid CBN hydrogen carriers** ahead of synthesis, with **accelerated heating** and finite system size as practical caveats on full kinetic convergence.

## Limitations

Accelerated **heating** protocols and finite **system sizes** for liquids leave **kinetic** **branching** only partially converged; **ReaxFF** accuracy for **B–N** organics must be tracked against new **QM** data whenever **functional** groups move outside the **training** manifold. **Regeneration** **cyclability** claims in the introduction are **engineering** targets that are **not** fully resolved by short **MD** windows alone.

## Relevance to group

**ReaxFF** **parameterization** case study on **heteroatomic** **organic** hydrogen storage.

## Citations and evidence anchors

DOI `10.1039/C5CP05486A`.

## Related topics

- [[reaxff-family]]
