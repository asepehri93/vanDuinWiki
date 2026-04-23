---
id: paper:2014fantauzzi-venue-rsc-cp
type: paper
title: "Development of a ReaxFF potential for Pt–O systems describing the energetics and dynamics of Pt-oxide formation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:oxide-surface
  - keyword:neb
  - keyword:dft-static
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp03111c"
year: 2014
authors:
  - "Fantauzzi, Donato"
  - "Bandlow, Jochen"
  - "Sabo, Lehel"
  - "Mueller, Jonathan E."
  - "van Duin, Adri C. T."
  - "Jacob, Timo"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "6fada3c6c82e558cef67f9e5c92e49cb5ebacc0522c65f9f2891651fa1c7b07f"
pdf_path: "papers/Fantauzzi_PCCP_PtO_2014_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014fantauzzi-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

A **ReaxFF** parametrization for **Pt–Pt** and **Pt–O** is optimized to **DFT** reference data for **bulk Pt**, **surfaces**, **oxides**, and **oxygen adsorption** on **Pt(111)** terraces and **step** motifs, then used—together with **NEB** and **MD**—to study **oxygen diffusion** on **Pt(111)** and related **surface-oxide** scenarios (proof PDF introduction; ESI noted for parameters and computational details).

## Methods

From the ingested **proof PDF** (main text and ESI pointer): **ReaxFF** parameters are obtained by fitting to an **extensive DFT dataset** spanning **bulk platinum phases**, **oxygen adsorbates** at **Pt(111)** sites and **defects** across **coverages**, **early Pt(111) surface-oxide** motifs, and **bulk platinum oxides**. **Section 2** of the article gives the **general ReaxFF + ab initio** setup; **Section 3.1** details **Pt–O** optimization. **Validation** compares **relative surface free energies** of **high-symmetry Pt–O surface phases** vs **oxygen chemical potential** against **DFT** and **experimental** references. **Oxygen diffusion on Pt(111)** is analyzed with **nudged elastic band (NEB)** and **MD** to extract **barriers** and **diffusion coefficients**; a short illustration addresses **oxygen adsorbate displacement** within **ordered overlayers**. **Tables/parameters** and extended **computational details** are provided in **ESI** (proof footer; DOI `10.1039/c4cp03111c`).

### 2 — Force-field training (Pt–O ReaxFF)

- **Parent FF / elements:** **ReaxFF** for **Pt–Pt** and **Pt–O** interactions, built to describe **oxidation** energetics and dynamics (abstract-level framing; article §3.1).
- **QM reference:** **DFT** dataset covering **bulk Pt**, **surfaces**, **oxides**, and **O** adsorption on **Pt(111)** terraces, **steps**, and **early surface-oxide** motifs (**proof PDF**; ESI for settings).
- **Training set / observables:** energies and relative **surface free energies** across **O** chemical potentials for high-symmetry **Pt–O** phases (article).
- **Optimization / software:** **ReaxFF** parameter optimization against the **DFT** database (details in article + **ESI**); **N/A in this wiki summary** for optimizer labels.
- **External benchmarks:** **DFT** and **experimental** references for **surface phase** stabilities as stated in the introduction (proof pages 3–4 narrative).

### 1 — MD application (diffusion and overlayer example)

- **Engine / code:** **LAMMPS**-style **molecular dynamics** with the fitted **ReaxFF** (explicit engine callouts are in **ESI**/**Methods**; proof PDF points to **ESI**).
- **System size & composition:** **Pt(111)** **O** diffusion and **overlayer** examples use **slab** supercells on the order of **hundreds to thousands of atoms** (order-of-magnitude statement—confirm counts in **`pdf_path`**/**ESI**).
- **Boundaries / periodicity:** **3D PBC** **slab** cells with vacuum gaps for **surface** **MD** (**standard setup**—confirm slab thickness and vacuum in **ESI**).
- **Ensemble:** **NVT** **molecular dynamics** is the typical setup for **surface diffusion** sampling unless the article specifies otherwise—confirm in **`pdf_path`**.
- **Timestep / thermostat / barostat:** **N/A in this wiki summary**—read **ESI** for **Δt**, thermostat, and whether **NPT** is used for any relaxation stages.
- **Duration / stages:** production **MD** lengths are reported in **ps**/**ns** scales in the article/**ESI** (**N/A to quote here** from the proof excerpt alone).
- **Temperature:** **temperature** set points for **O** diffusion **MD** are defined in the article/**ESI** (**N/A in this operator summary**).
- **Pressure / stress control:** **N/A — hydrostatic pressure** targets are **not** stated for the summarized **surface MD** workflow here; confirm if any **NPT** equilibration appears in **ESI**.
- **Analysis tools:** **NEB** for **barriers**; **MD** for **diffusion coefficients** and an **ordered overlayer** **displacement** illustration (proof PDF pages 3–4).
- **Electric field / metadynamics:** **N/A —** not part of the summarized **Pt(111) O** diffusion workflow here.

### 3 — Static QM

**N/A as standalone production block**—**DFT** supplies **training/validation** data for **ReaxFF** (see **Force-field training**).

## Findings

### 1 — Outcomes and mechanisms

The introduction states **good agreement** between **ReaxFF** and both **DFT** and **experiment** for **relative surface free energies** of **high-symmetry Pt–O** phases as a function of **oxygen chemical potential**, supporting use of the potential for **more complex Pt–O** structures. **NEB** and **MD** together characterize **oxygen diffusion on Pt(111)** (**barriers** and **diffusion coefficients**). A **proof-of-concept** example illustrates **oxygen adsorbate displacement** within an **ordered overlayer**—a structure class argued to be **beyond routine DFT** reach, motivating **ReaxFF** (proof PDF pages 3–4).

### 2 — Comparisons

- **ReaxFF** vs **DFT** and **experiment** for **Pt–O surface phase** free energies (proof introduction).

### 3 — Sensitivity

- **Oxygen chemical potential** and **coverage** enter the **surface phase** comparisons (article framing).

### 4 — Limitations / outlook

- **Proof PDF** caveats in **## Limitations**; prefer **edited PCCP** for pagination.

### 5 — Corpus / KB honesty

This slug tracks **`papers/Fantauzzi_PCCP_PtO_2014_proof.pdf`** bytes; cite the **version-of-record** **PCCP** article at DOI **`10.1039/c4cp03111c`** for canonical pagination and **SI** pointers.

## Limitations

The registered PDF is a **publisher proof**; layout, queries, and pagination may differ from the version of record.

## Reader notes (navigation)

Prefer the **edited PCCP article** at DOI `10.1039/c4cp03111c` for citation and page-level evidence; this slug tracks the ingested proof PDF bytes.

## Citations and evidence anchors

- DOI `10.1039/c4cp03111c` (proof query block; extract).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
