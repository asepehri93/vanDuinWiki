---
id: paper:2017ostadhossein-venue-research
type: paper
title: "ReaxFF Reactive Force-Field Study of Molybdenum Disulfide (MoS₂)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.6b02902"
year: 2017
authors:
  - "Alireza Ostadhossein"
  - "Ali Rahnamoun"
  - "Yuanxi Wang"
  - "Peng Zhao"
  - "Sulin Zhang"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "55789272ba671c7beaaea095528b640589cbf25342d4d578088dacbb283c5aac"
pdf_path: "papers/Ostadhossein_MoS2_JPC_Letters_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ostadhossein-venue-research -->

!!! abstract
New ReaxFF for MoS₂ fit to Jaguar B3LYP/LAV3P** molecular data and VASP PBE-PAW periodic data; applications to vacancies, migration barriers, 2H↔1T pathways, ripplocations, and elastic response with PBC uniaxial/biaxial strain.

## Summary

The letter develops a **Mo/S/H ReaxFF** trained against **DFT**: **Jaguar** optimizations (**B3LYP** with the **LAV3P** basis) for molecules in the training set and **VASP** (**PBE**, **PAW**, **400 eV** cutoff, **Γ-centered** k-grids, forces **<0.02 eV/Å**), including **bilayer** spacing scans with constrained Mo planes and **NEB** barriers where needed (see Methods and SI). **ReaxFF** energies combine bonded, torsion, lone-pair, over/under-coordination, **vdW**, and **Coulomb** terms (eq. 4 in paper). The fitted potential reproduces **bond/angle** dissociation and condensed-phase benchmarks tabulated against DFT/experiment (**Table 1–2**). **MD applications** use **periodic boundary conditions** in-plane; **uniaxial/biaxial** strain increments extract **2D elastic constants** and **ultimate strengths** (~**24–26 GPa** for SL MoS₂ depending on direction). **2H↔1T** pathways and **vacancy** formation/migration energetics, **ripplocation** defects, and interplay with **S vacancies** are explored at ReaxFF level. The parameterization targets **mechanochemistry** and **defect** physics in **TMDs** where **fixed-bond** potentials are insufficient.

## Methods

**Force-field training / fitting.** **Mo/S/H ReaxFF** is fit to **Jaguar** **B3LYP/LAV3P\*\*** molecular training data and **VASP** **GGA-PBE** **PAW** periodic data (**400 eV** plane-wave cutoff, **Γ-centered** k-grids, force threshold **<0.02 eV Å⁻¹**), including **bilayer** spacing scans with constrained **Mo** planes and **nudged elastic band (NEB)** barriers where cited. **Optimization** follows the standard **ReaxFF** least-squares / genetic workflow with **SI** tables (**S1**, **S2**, **S4**) and **`trainset.in` listings** in **[[2017ostadhossein-venue-microsoft-word-3]]** documenting weights and geometries.

**MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** is used for **ReaxFF** **molecular dynamics** and **force-field NEB** (the letter explicitly contrasts **CI-NEB** at **DFT** in **VASP** with **NEB** at **ReaxFF** level in **LAMMPS** for the **2H↔1T** pathway). **System size & composition:** **Monolayer and few-layer MoS₂** supercells for **defect**, **phase**, **ripplocation**, and **mechanical** tests—exact atom counts vary by figure and are **N/A —** not duplicated tabularly on this wiki page (see article structures). **Boundaries / periodicity:** **In-plane periodic** **MoS₂** cells under **uniaxial/biaxial** strain protocols described in the letter (**PBC** implied for extended sheets). **Ensemble / thermostat / timestep / duration:** **N/A —** the **JPCL** main text available to this pass emphasizes **energy models**, **barriers**, and **elastic** extraction workflows without restating a single consolidated **NVT/NVE** table, explicit **timestep** (**fs**) settings, or **nanosecond-scale** production clocks—confirm per-figure simulation cards in the **PDF/SI** when auditing trajectories. **Barostat:** **N/A —** not highlighted for the mechanical strain excerpts summarized here. **Temperature:** **thermal** equilibration and **MD** segments are referenced figure-by-figure, but a unified **300 K** (or other) thermostat table is **not** consolidated on this wiki page—see **VOR/SI**. **Pressure / electric field / enhanced sampling:** **N/A —** not central to the summarized **strain / defect / NEB** protocol beyond standard **NEB** restraint.

**Static QM / DFT.** **Jaguar** and **VASP** calculations above supply **QM** **training** and **validation** energies/structures tabulated against **ReaxFF** in **Tables 1–2**.

**Review / non-simulation framing.** **N/A —** primary **JPCL** **parameterization + application** letter.

## Findings

**Outcomes & mechanisms.** The fitted **Mo/S/H ReaxFF** reproduces selected **DFT** and **experimental** structural/elastic benchmarks for **2H MoS₂** while enabling **reactive** sampling of **vacancy** formation and **migration**, **2H↔1T** pathways, **ripplocations** coupled to **sulfur vacancies**, and **nonlinear mechanics** under **strain**.

**Comparisons.** **ReaxFF** **barriers** and **energy ordering** are compared explicitly to **DFT** (e.g., **2H–1T** energetics and barrier scaling discussed in the text) and to **nanoindentation/AFM** mechanical trends cited by the authors.

**Sensitivity & design levers.** **Strain direction** (**uniaxial vs biaxial**) and **defect** content modulate **elastic response** and **failure strengths** reported near **~24–26 GPa** ultimate tensile strengths for **SL MoS₂** depending on orientation (see letter).

**Limitations & outlook (as authored).** **DFT** band-gap limitations carry over to **defect-level** interpretations; absolute **kinetic rates** from **ReaxFF** require the down-scaled barrier caveats noted in the discussion.

**Corpus / KB honesty.** **SI** parts **[[2017ostadhossein-venue-microsoft-word]]**, **[[2017ostadhossein-venue-microsoft-word-2]]**, **[[2017ostadhossein-venue-microsoft-word-3]]** hold machine-readable training artifacts; refresh MD numerics from the **VOR** PDF if any figure–text mismatches appear after corpus updates.


## Limitations

Standard DFT band-gap limitations noted; structural energetics focus avoids excited-state physics. **Charge transport** and **excitonic** effects in **MoS₂** devices are therefore outside the scope of the **mechanical** and **defect** benchmarks emphasized here.

## Relevance to group

Core **group** ReaxFF publication for **TMD** chemistry and mechanics. Subsequent **corpus** pages on **2D** **layered** materials frequently cite this letter as the **MoS₂** **parameterization** anchor.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpclett.6b02902`

## Related topics

- [[reaxff-family]]
- [[2017ostadhossein-venue-microsoft-word-2]]

## Reader notes (navigation)

- SI packages: [[2017ostadhossein-venue-microsoft-word]], [[2017ostadhossein-venue-microsoft-word-2]], [[2017ostadhossein-venue-microsoft-word-3]].
