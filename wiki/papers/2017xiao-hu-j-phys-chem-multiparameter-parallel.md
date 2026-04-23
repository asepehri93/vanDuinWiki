---
id: paper:2017xiao-hu-j-phys-chem-multiparameter-parallel
type: paper
title: "Multiparameter and Parallel Optimization of ReaxFF Reactive Force Field for Modeling the Atomic Layer Deposition of Copper"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - material:metal-surface
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:catalysis-surface
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b09948"
year: 2017
authors:
  - "Xiao Hu"
  - "Jörg Schuster"
  - "Stefan E. Schulz"
venue: "The Journal of Physical Chemistry C 121, 28077–28089 (2017)"
pdf_sha256: "53af45c5bea8a058ad0957e10c068fa70b954076ab0e2db2945d288580732366"
pdf_path: "papers/ReaxFF_others/Hu_Copper_JPCC_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017xiao-hu-j-phys-chem-multiparameter-parallel -->

## Summary

This *Journal of Physical Chemistry C* article develops a **multiparameter, parallel optimization** workflow—organized with **Taguchi experimental-design** ideas—to refine **ReaxFF** parameters for **Cu/C/H/N/O** chemistry aimed at **atomic layer deposition (ALD)** modeling. The practical target is **copper metallization** from **organometallic precursors** with **atomic hydrogen** as a coreactant, a regime where ligand fragmentation, surface contamination, and incomplete elimination can undermine film purity. The authors position the work as extending prior **Cu** ReaxFF descriptions by tightening interactions needed for **ALD-relevant** bond-making and bond-breaking events on **Cu surfaces**.

## Methods

**Force-field training (ReaxFF).** The authors extend an existing **Cu** reactive description to **Cu/C/H/O/N** by **optimizing** **Cu–C**, **Cu–N**, and **Cu–H** (plus oxygen-containing) interaction blocks needed for **copper ALD**. **Density functional theory (DFT)** reference **energies**, **forces**, and reaction pathways supply the **training set**, while a **Taguchi-inspired multiparameter parallel optimization** workflow searches parameter space efficiently before **validation** on organometallic motifs. **QM** details (functional, **basis set**, **k-point** sampling) belong to the article **Methods** and should be read from **`papers/ReaxFF_others/Hu_Copper_JPCC_2017.pdf`**.

**Molecular dynamics (reactive).** After the fit, **reactive molecular dynamics** (**RMD**) simulations implement abbreviated **ALD** cycles on **Cu** for **[Cu(iPr-amd)]\(_2\)** versus **Cu(dmap)\(_2\)** with **H-radical** coreactant pulses, monitoring **adsorption**, **fragmentation**, and **residue** populations at **temperature** setpoints (**K**) and **thermal** coupling recipes tabulated in the **JPCC** **Methods**. The indexed abstract does not restate **supercell** sizes, exact **atom** counts, **timestep** (fs), **thermostat**/**barostat** choices, **NVT**/**NPT** labels, or **equilibration**/**production** **duration** (ps/ns); extract those from the **JPCC** **PDF** rather than this wiki summary. **Periodic** models are implied for metallic **slabs** with periodic images. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the excerpted pages.

**Static QM / DFT.** **DFT** supplies the **training** references; it is **not** used as the production **AIMD** engine for large-cycle **RMD**.

**Review scope.** **N/A —** primary **parameterization** plus demonstration trajectories.

## Findings

**Outcomes and mechanisms.** For **[Cu(iPr-amd)]\(_2\)**, the first half-cycle favors **dissociative adsorption** into **Cu(iPr-amd)**-derived surface species; the **H-radical** pulse eliminates some fragments but leaves **nitrogen-containing residues** such as **C\(_5\)H\(_{12}\)N\(_2\)** and **C\(_2\)H\(_4\)N** that can contaminate the interface. For **Cu(dmap)\(_2\)**, adsorption splits into **Cu(dmap)** plus **dmap**, and a subsequent **hydrogen-transfer** sequence drives **dmap** ligands into the gas phase more completely.

**Comparisons.** **Versus** the amidinate route, **Cu(dmap)\(_2\)** exposes **simpler** surface **reaction** sequences with fewer persistent **C–N** fragments in the abbreviated-cycle model, aligning with the abstract’s “cleaner ALD chemistry” message.

**Sensitivity / design levers.** **Precursor** identity (amidinate **versus** alkoxide) is the dominant lever in the modeled abbreviated cycles; **H-radical** exposure controls how completely **ligands** are stripped versus trapped as **contamination**.

**Limitations / outlook.** Abbreviated cycles omit full industrial pulse/purge timing; **ReaxFF** barriers remain empirical relative to **experiment**.

**Corpus honesty.** Protocol numerics beyond the abstract must be taken from the **PDF** at `pdf_path`; the local extract stops early in the introduction.


## Limitations

Abbreviated cycles omit full industrial pulse/purge timing and chamber chemistry; contamination predictions are force-field dependent.

## Reproducibility notes

For LAMMPS-style workflows, operators should archive the distributed **ReaxFF** parameter file used with the publication, the **element** typing rules for organometallic ligands, and the **H-radical** introduction protocol (flux, coverage, and thermostat coupling), because reactive ALD outcomes can be sensitive to radical flux approximations. When extending the model to new precursors, re-run the **Taguchi** optimization stage rather than borrowing parameters piecemeal from unrelated Cu datasets.

The **Taguchi** framing is not decorative: it is intended to reduce the number of explicit **multiparameter** trials while exploring **coupled** corrections to **Cu–C**, **Cu–N**, and **Cu–H** terms that would otherwise explode combinatorially. Reproducing the optimization therefore requires logging which **parameter groups** were varied together, the **levels** tested, and the **objective function** used to score training-data agreement—details that belong in the article/SI rather than being inferred from a single final parameter file.

## Relevance to group

Demonstrates **modern ReaxFF optimization workflows** (parallel/Taguchi) for **metallization** chemistry relevant to interconnect processing.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.7b09948](https://doi.org/10.1021/acs.jpcc.7b09948)

## Related topics

- [[reaxff-family]]
- Copper surfaces and ALD
