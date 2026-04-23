---
id: paper:2021shin-computationa-impact-three-body-2
type: paper
title: "Impact of three-body interactions in a ReaxFF force field for Ni and Cr transition metals and their alloys (corrected proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:metallic-systems
  - keyword:qm-training-data
  - keyword:nvt-simulation
source_refs: []
doi: "10.1016/j.commatsci.2021.110602"
year: 2021
authors:
  - "Yun Kyung Shin"
  - "Yawei Gao"
  - "Dongwon Shin"
  - "Adri C. T. van Duin"
venue: "Comput. Mater. Sci. (corrected proof); same DOI as VOR"
pdf_sha256: "5088fe4b91fb0d2f5a8a6c13cd9239ff602a6172d1f50763e691464c95af558e"
pdf_path: "papers/Shin_CompMatSci_NiCr_metal_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021shin-computationa-impact-three-body-2 -->

!!! note "Corpus PDF role"
    **Corrected proof** PDF (`Shin_CompMatSci_NiCr_metal_2021_galley.pdf`). The **journal PDF** is **`Shin_CompMatSci_NiCr_metal_2021.pdf`** on **[[2021shin-computationa-impact-three-body]]**.

## Summary

**fcc** **nickel** elasticity and **defect** energetics are sensitive to **angular** restoring forces that **two-body**-centric **ReaxFF** metal descriptions can mishandle: in particular, **C\(_{12}\)** and **C\(_{44}\)** can collapse to **equality**, and **stacking-fault** energies can become **negative**, spuriously accelerating **fcc→hcp** transformations. This work augments **Ni** and **Cr** **ReaxFF** parameterizations with **explicit three-body (valence-angle)** terms, then benchmarks **thermal** and **mechanical** responses against **DFT** and experiment. **Finite-temperature** **elastic constants** for **fcc Ni** and **bcc Cr**, **thermal expansion** from **0** to **1700 K**, **melting** temperatures via **hysteresis** MD with **large** cells and **voids**, and **Ni–Cr** **alloy** **formation** energetics (**Ni\(_3\)Cr** ordering vs **bcc** solid solutions) are reported. The overarching claim is that **three-body** physics is **necessary** for **semiquantitative** **metal** property prediction within the **ReaxFF** framework for these systems.

Abstract-level motivation stresses that prior Ni/Cr ReaxFF metals omitted explicit angular terms, producing unphysical elastic degeneracies and unstable stacking faults that bias phase transformation kinetics; adding optimized valence-angle interactions is presented as restoring cubic elastic structure and sensible fault energies before finite-temperature melting and alloy tests.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

**Authoritative protocol:** Use **`[[2021shin-computationa-impact-three-body]]`** (journal PDF) for tables, **timestep**, and **thermostat** settings; this slug documents only the **corrected-proof** PDF path.

### A — ReaxFF (Ni / Cr / Ni–Cr)

- Same **three-body-augmented** **Ni** and **Cr** metal parameterization and **Ni–Cr** **cross** terms as the VOR page (**[[2021shin-computationa-impact-three-body]]**).

### B — MD benchmarks

- **Elastic**, **thermal expansion**, **melting** (**hysteresis** with **voids**) as summarized on the VOR page.

### C — DFT

- Reference **alloy** **formation energies** and **0 K** **elastic** data for comparison to ReaxFF.

### D — Experiments

- Literature **elastic** and **melting** benchmarks as cited on the VOR page.

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.

### 2 — Force-field training (when applicable)

- **Parent FF / elements:** parent **ReaxFF** (or other reactive) **force field** / **parameter set** names and element coverage follow the tables in the **PDF**.
- **QM reference:** **DFT**/**QM** reference calculations (functional, **basis set**, **k-point** or cutoff conventions) underpin the **training** data described in the article.
- **Training set:** **Training** geometries, **reaction** subsets, **equation of state** targets, or other **reference data** sets are enumerated in the fitting section of the **PDF**.
- **Optimization:** **optimization** / least-squares or packaged (**CMA-ES**, genetic algorithm, etc.) **parameter** **fit** procedures appear in the Methods as implemented by the authors.
- **Reference data:** additional **experimental** or literature **DFT** **benchmark** sets cited for validation are listed in the publication.
## Findings

**Three-body** terms remove the **C\(_{12}\)=C\(_{44}\)** degeneracy and improve **stacking-fault** energetics for **fcc Ni** relative to the prior **two-body**-limited description. **Melting** temperatures land near **1698 K** for **Ni** (~**1.7%** of experiment) and **2410 K** for **Cr** (~**10%**), with **hysteresis** sensitivity discussed in the text. **Ni\(_3\)Cr** **heat of formation** is **negative** (favoring order) while **bcc** **solid-solution** motifs show **positive** heats in the tests shown, **consistent** with **DFT** trends. **Elastic** constants at **0 K** match **DFT** within roughly **5–10%** except where the abstract flags a **larger** deviation in **C\(_{33}\)**.

**Comparisons (corpus).** Cite the **VOR** **`[[2021shin-computationa-impact-three-body]]`** for final **typeset** **figures** and any **table**-level **agreement** **with** **experiment**; this **proof** path is for **ingest** **provenance** only.

## Limitations

Remaining **elastic** discrepancies (notably **C\(_{33}\)**) and **melting** **hysteresis** dependence on **simulation** setup are acknowledged in the paper. **Proof** pagination may differ from the **VOR** PDF on **[[2021shin-computationa-impact-three-body]]**.

## Reader notes (navigation)

- Version-of-record PDF page: **[[2021shin-computationa-impact-three-body]]**
- [[reaxff-family]]
