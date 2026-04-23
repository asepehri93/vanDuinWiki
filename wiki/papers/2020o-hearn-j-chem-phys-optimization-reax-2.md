---
id: paper:2020o-hearn-j-chem-phys-optimization-reax-2
type: paper
title: "Optimization of the Reax force field for the lithium–oxygen system using a high fidelity charge model"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:charge-equilibration
  - keyword:galley-or-proof-pdf
  - keyword:qm-training-data
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1063/5.0014406"
year: 2020
authors:
  - "Kurt A. O'Hearn"
  - "Michael W. Swift"
  - "Jialin Liu"
  - "Ilias Magoulas"
  - "Piotr Piecuch"
  - "Adri C. T. van Duin"
  - "H. Metin Aktulga"
  - "Yue Qi"
venue: "The Journal of Chemical Physics"
pdf_sha256: "46171ff3142805355a7947eb32968735404bb8305dd2e61c15af9a551f62bc72"
pdf_path: "papers/OHearn_JCP2020_Li2O_ACKS2_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020o-hearn-j-chem-phys-optimization-reax-2 -->

!!! note "Non-primary PDF"

    **AIP proof** PDF (`papers/OHearn_JCP2020_Li2O_ACKS2_proof.pdf`). For final layout and pagination, prefer **`[[2020o-hearn-j-chem-phys-optimization-reax]]`** when that slug references the **accepted / VOR** PDF. See `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md` (proof duplicate pattern).

## Summary

Lithium oxide chemistry underpins solid-state electrolytes, battery interfaces, and ceramic fracture phenomena where **charge redistribution** during bond breaking challenges classical **QEq/EEM** schemes within ReaxFF. This **J. Chem. Phys.** article replaces **EEM/QEq**-style charge equilibration with **ACKS2** (atom-condensed Kohn–Sham DFT to second order) embedded in ReaxFF for the **Li–O** system. Parameters are optimized with **genetic algorithms** against **DFT**, **MRCI**, and **MRCI+Q** bond-breaking training data, then validated in **LAMMPS** builds with ACKS2 enabled. The new fit improves **charge evolution** along Li–O dissociation versus a **2016 QEq** parameter set, yields qualitatively different **Li\(_2\)O** melt behavior, but **still does not** reproduce full **brittle fracture** in showcased **notched slab** tests.

The **proof** PDF path flags **pagination** risk; operators should mirror **numerical** benchmarks against **`[[2020o-hearn-j-chem-phys-optimization-reax]]`** using the **accepted**/**VOR** PDF when reconciling **figure** labels and **Supporting Information** references.

## Methods

Aligned with **`[[2020o-hearn-j-chem-phys-optimization-reax]]`**: **OGOLEM** / **genetic** optimization; **LAMMPS** with **ACKS2**; **NPT** equilibration of **Li\(_2\)O** bulk at **300 K** and **0** pressure; **timestep** stability checks (**0.25 fs** in **NVE**); **NVT** **plane-strain fracture** of notched slabs at **300 K**. Full tabulated settings and convergence criteria reside on the VOR page.

**Reproducibility detail.** ACKS2 integrations need a **compatible** LAMMPS build; mirror `[[2020o-hearn-j-chem-phys-optimization-reax]]` and the article inputs.

**1 — MD application (atomistic dynamics).** **Engine / code:** LAMMPS with ACKS2-enabled ReaxFF (staged protocols summarized on the VOR page). **System size & composition:** Li₂O bulk melt cubes and notched fracture slabs; counts and box sizes on `[[2020o-hearn-j-chem-phys-optimization-reax]]`. **Boundaries / periodicity:** PBC for bulk; plane-strain fracture geometry as in the article figures (VOR). **Ensemble / timestep / duration:** NVE checks at 0.25 fs timestep; NPT preequilibration of bulk Li₂O at 300 K near 0 pressure; NVT plane-strain fracture at 300 K. **Thermostat:** ensemble-control details (including any thermostat and damping) are in the VOR `pdf_path`; this proof stub does not duplicate them. **Barostat / pressure:** NPT only for bulk preequilibration; NVT fracture stage has no barostat. **Electric field: N/A —** not used. **Replica / enhanced sampling: N/A —** not used in the melt/fracture showcases.

**2 — Force-field training.** ReaxFF for Li–O reoptimized with ACKS2 against DFT and MRCI/MRCI+Q reference data (genetic / OGOLEM-style workflow in the paper); see `[[2020o-hearn-j-chem-phys-optimization-reax]]` for citable parameter and validation tables.

## Findings

**ACKS2**-coupled ReaxFF reproduces **training-set** charge evolution and **Li–O** bond-breaking targets more faithfully than the **2016 QEq** parameter set. **NPT** melt simulations of **Li\(_2\)O** show different **amorphization** and **RDF** signatures than QEq on the same benchmarks. **Fracture** tests on **notched** **Li\(_2\)O** slabs remain **partly ductile** relative to expected **brittleness**—i.e. improved **electrostatics** along dissociation does not by itself fix **long-range** **crack** **physics** in the classical model. **Headline** numbers, **tables**, and **thermostat**/**barostat** **labels** for reproduction: **`[[2020o-hearn-j-chem-phys-optimization-reax]]`** (VOR). **Corpus honesty:** this wiki slug tracks the **AIP proof** `pdf_path`; **pagination** and **figure** placement may differ from the VOR—reconcile **QEq-2016** vs **ACKS2** **comparisons** on the **non-proof** **PDF** when **precision** matters.

## Limitations

**Proof** PDF: page numbers and figure placement may differ from the **final** issue PDF—reconcile locators on the VOR sibling.

## Relevance to group

Duplicate ingest for **AIP** proof workflow (van Duin co-author); **charge fidelity** for Li–O **ceramic** and **battery-adjacent** chemistry.

## Reader notes (navigation)

- **`[[2020o-hearn-j-chem-phys-optimization-reax]]`**
**Proof duplicate.** Reconcile timestep, ACKS2 build flags, and fracture slab geometries with `[[2020o-hearn-j-chem-phys-optimization-reax]]` using the non-proof PDF when available.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
