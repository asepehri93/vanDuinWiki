---
id: paper:2023heesoo-park-chem-mater-2-toward-atomistic
type: paper
title: "Toward Atomistic Understanding of Materials with the Conversion–Alloying Mechanism in Li-Ion Batteries"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:dft-static
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.2c03603"
year: 2023
authors:
  - "Heesoo Park"
  - "Adri C. T. van Duin"
  - "Alexey Y. Koposov"
venue: "Chem. Mater."
pdf_sha256: "12fc318b0ccac8583910d0b402b6b7a94c364870e0852dd919677ca7588124a1"
pdf_path: "papers/Park_Alloying_Li_batteries_ChemMat_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023heesoo-park-chem-mater-2-toward-atomistic -->

## Summary

Alloying anodes can exceed graphite’s capacity, but large volume changes drive failure; conversion–alloying materials (CAMs) combine conversion chemistry with embedded alloying domains so an amorphous conversion matrix can buffer strain while reversible Li–Si (or related) chemistry contributes capacity. CAM products are often amorphous and heterogeneous, which makes diffraction-based structure assignment difficult and motivates local probes such as pair distribution function (PDF) analysis. This *Chemistry of Materials* study uses **amorphous substoichiometric silicon nitride (SiNₓ)** as a tractable CAM model: the authors develop a **Si–N–Li ReaxFF** parameterization against **DFT** references, build atomistic models of lithiated and delithiated states, and compare **computed PDFs** to **experimental** PDFs across electrochemical stages. The work is positioned as a general computational methodology for connecting atomistic reaction pathways in CAMs to experimentally measurable diffuse scattering.

## Methods

### ReaxFF parameterization (A)

Fit **bond-order**, **vdW**, and **QEq** terms to **QM** data for **Si–N–Li** chemistry.

### DFT training data (C)

**VASP** and **ORCA** at **PBE** (Methods §2.1): **EOS**, **cohesive energies**, bonding motifs for **lithiation/delithiation**; see **SI** figures **S1–S3** for parts of the landscape.

### Reactive MD and structural sampling (B)

**LAMMPS** **ReaxFF MD** at **300 K**; **OVITO** extracts **amorphous** snapshots at different electrochemical stages.

### PDF comparison pipeline

Compute **G(r)** with **X-ray** weighting and **XaNSoNS** form factors to mimic **laboratory PDF** contrast.

The **Computational Methods** section also ties the **SiN\(_x\)** **CAM** model to **pair-distribution** analysis because **amorphous** **lithiation** products lack long-range **Bragg** peaks: **PDF** comparisons therefore act as the primary **experimental** anchor for **atomistic** models across **lithiation** stages, rather than **crystallographic** **Rietveld** fits alone.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with the fitted **ReaxFF** for **Si–N–Li** chemistry; **300 K** sampling is stated in Methods §2 for structural snapshots. **System & composition:** amorphous **SiN\(_x\)** models in lithiated and delithiated states (sizes and stage definitions in the article and SI). **Boundaries / periodicity:** 3D **PBC** **bulk** amorphous cells. **Ensemble, timestep, thermostat, barostat, run duration:** the **stated** **300** **K** **NVT** **sampling** for amorphous **SiN\(_x\)** models is a concrete **NVT** example; other **(de)lithiation** **replicas** in the article can use different **NVT**-like **controls** over **ps**-scale **spans** to compare **G(r)**—**N/A** to duplicate the full table here (see the **Chem. Mater.** **SI** and **main** text for **NVT** and **ns**-scale **production** choices). **Pressure / stress, electric field, shock, non-equilibrium drive:** **N/A** in this abstracted summary. **Post-processing:** **G(r)** via **X-ray**-weighted form factors; **OVITO** for amorphous **snapshots** as above.

### 2 — Force-field training

**Parent** description: ReaxFF-style **Si–N–Li** parameter set built on prior **C/H/O/Si** **ReaxFF** lines (as referenced in the paper). **QM reference (training):** **PBE**-level data from **VASP** and **ORCA**—**EOS**, **cohesive** energies, bonding for **(de)lithiation**; SI figures on parts of the landscape. **Training set** scope: **lithiation**-connected structures and **defect**/**disorder** motifs as in Methods §2.1. **Optimization:** **weighted** fit of **ReaxFF** to **DFT** observables (form and weighting in article). **External validation:** comparison of **model PDFs** to **experiment**—see **Findings**.

### 3 — Static QM / DFT (reference data for the fit)

**PBE**-level **VASP** and **ORCA** data in Methods §2.1 supply the **ReaxFF** training set (including SI figures S1–S3). The paper does not center on a static-QM application track separate from the **ReaxFF** validation design beyond that training set.

## Findings

### Lithiation microstructure

Early **lithiation** forms a **connected Si-rich network** within the **nitride** matrix that remains **reactive** in later lithiation steps.

### Delithiation reorganization

**Delithiation** drives **N-rich** vs **Si-rich** **spatial separation**, consistent with a **conversion + alloying** **CAM** picture for **SiN\(_x\)**.

### PDF cross-validation

**Simulated PDFs** track **experimental** PDF evolution across **cycling**, supporting that **ReaxFF** models capture **coarse** **amorphous** architecture features.

### Methodological takeaway

Framed as a reusable **ReaxFF + PDF** workflow for **heterogeneous amorphous** conversion–alloying anodes.

For **heterogeneous** **CAM** microstructures, **pair-distribution** evolution during **cycling** can remain informative even when **Bragg** peaks stay **broad**, which is why the article pairs **ReaxFF** models with **PDF** measurements rather than relying on **crystallographic** indexing alone.

## Limitations

Amorphous, compositionally heterogeneous systems require large models and long runs; kinetics may be under-sampled relative to experimental cycle times.

## Relevance to group

Demonstrates **ReaxFF + PDF** integration for **complex amorphous battery materials** with **van Duin** authorship.

## Citations and evidence anchors

- DOI: [10.1021/acs.chemmater.2c03603](https://doi.org/10.1021/acs.chemmater.2c03603)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
