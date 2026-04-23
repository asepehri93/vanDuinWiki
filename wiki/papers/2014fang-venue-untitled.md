---
id: paper:2014fang-venue-untitled
type: paper
title: "First-principles studies on vacancy-modified interstitial diffusion mechanism of oxygen in nickel, associated with large-scale atomic simulation techniques"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - method:dft-static
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:metallic-systems
  - keyword:reaxff-application
  - keyword:validation-experiment
source_refs: []
doi: "10.1063/1.4861380"
year: 2014
authors:
  - "Fang, H. Z."
  - "Shang, S. L."
  - "Wang, Y."
  - "Liu, Z. K."
  - "Alfonso, D."
  - "Alman, D. E."
  - "Shin, Y. K."
  - "Zou, C. Y."
  - "van Duin, A. C. T."
  - "Lei, Y. K."
  - "Wang, G. F."
venue: "Journal of Applied Physics"
pdf_sha256: "01f253d0c09556b57888615abd2b370eca18cf2dfaed111cbf2e2e01ddde74af"
pdf_path: "papers/Fang_J_App_Phys_NiO_diffusion_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014fang-venue-untitled -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Oxygen diffusivity in fcc Ni is reassessed by combining first-principles thermodynamics with large-scale atomistic techniques. A simple octahedral–tetrahedral–octahedral interstitial path alone underestimates migration barriers and overpredicts diffusivities versus experiment; incorporating vacancy effects brings diffusivities in line with measurements. At high temperature, vacancy concentration is argued to be comparable to oxygen solubility, with strong O–vacancy binding and charge redistribution that couples oxygen transport to the vacancy field (abstract; introduction opening, extract). The **J. Appl. Phys.** article motivates a **multiscale** workflow where **DFT-based** **free energies** seed **kinetic** models that are **cross-checked** by **ReaxFF**/**MEAM**/**kMC** tools.

## Methods

Oxygen diffusivity in dilute fcc Ni is formulated with an interstitial jump-rate expression consistent with **Eyring transition-state theory**, using **finite-temperature migration free energies** built from **0 K DFT energies** plus **vibrational** (phonon DOS or Debye) and **thermal electronic** contributions to the Helmholtz free energy \(F(V,T)\). This first-principles thermodynamic route is combined with **large-scale atomistic kinetics**: **ReaxFF molecular dynamics**, **MEAM molecular dynamics**, and **kinetic Monte Carlo** as complementary tools to the DFT-based diffusion framework (abstract; computational methods section opening, extract pages 1–2).

**Supercell** sizes, **diffusion** **jump** **networks**, and **convergence** tests for **Ni–O–vacancy** **interactions** are specified in `papers/Fang_J_App_Phys_NiO_diffusion_2014.pdf` alongside **tables** linking **computed** **diffusivities** to **experimental** **ranges** cited in the paper.

### 1 — MD application (ReaxFF / MEAM MD)

- **Engine / code:** **ReaxFF MD** and **MEAM MD** are used as **large-scale atomistic** complements to the **DFT-based** diffusion framework (abstract; computational overview).
- **System size & composition:** **Ni–O** bulk and **defect** supercells containing **thousands of atoms** in the reported **MD** benchmarks (qualitative scale statement—confirm exact counts in **`pdf_path`**).
- **Boundaries / periodicity:** bulk **MD** benchmarks use **3D PBC** supercells as standard for **Ni** diffusion studies; confirm cell choices in the article.
- **Ensemble:** **NVT** molecular dynamics is typical for these **diffusion** benchmarks unless the authors specify **NPT** segments—**N/A in this wiki summary** for explicit labels.
- **Timestep / thermostat / duration:** **N/A in this wiki summary**—see **`pdf_path`** for **fs** timestep, thermostat, and **ps**/**ns** production lengths.
- **Barostat / pressure control:** **N/A — hydrostatic pressure** control is **not** stated for the summarized **MD** portions; confirm whether any **NPT** segments appear in the PDF.
- **Pressure targets:** **N/A —** not specified in this wiki summary for **MD** trajectories.

### 2 — Force-field training

**N/A —** not a ReaxFF parameterization paper; **ReaxFF**/**MEAM** are **interatomic models** used for kinetics comparisons as described in the article.

### 3 — Static QM / DFT and kinetic modeling

- **Functional / dispersion / basis / k-sampling:** specified in the **J. Appl. Phys.** computational methods for **0 K DFT** energies and **finite-temperature** corrections (**phonon**/**Debye** and **thermal electronic** contributions to **\(F(V,T)\)**) feeding **Eyring-type** jump rates.
- **Structures / pathways:** **O** diffusion in dilute **fcc Ni** with **interstitial** paths and **vacancy-coupled** scenarios as developed in the paper.
- **Properties:** **migration free energies**, **diffusivities**, and comparison to **experiment** (abstract; tables in PDF).
- **Kinetic Monte Carlo:** **kMC** is included among the **atomistic kinetics** tools alongside **MD** (abstract).

## Findings

### 1 — Outcomes and mechanisms

Considering only the **octahedral–tetrahedral–octahedral** interstitial path **underestimates** the migration barrier and **overpredicts** diffusivities by orders of magnitude versus experiment. **Incorporating vacancies** brings predicted diffusivities in line with measurements. First-principles analysis further argues that at **high temperature** the **vacancy concentration can be comparable to oxygen solubility**, with **strong O–vacancy binding** and **charge redistribution**, so oxygen transport is coupled to the vacancy field rather than behaving as a simple interstitial gas (abstract; extract pages 1–2).

### 2 — Comparisons

- **Computed diffusivities** vs **experimental** ranges and vs **interstitial-only** models (abstract; tables in **`pdf_path`**).

### 3 — Sensitivity / design levers

- **Vacancy content** and **O–vacancy binding** strongly modulate effective **O** transport versus simple **interstitial** pictures (abstract).

### 4 — Limitations / outlook

- **Experimental** **O** diffusion data in **Ni** remain scattered; **Eyring**-type rate modeling carries approximations stated in the article (**## Limitations**).

### 5 — Corpus / KB honesty

The **discussion** frames this **coupling** as a **practical** correction to **interstitial-only** pictures used in some **alloy oxidation** models; **quantitative** barriers and **kMC** network details must be taken from **`pdf_path`**, not this page alone.

## Limitations

Experimental oxygen diffusion data in Ni remain scattered; modeling focuses on selected pathways and approximations in Eyring-type rate formulations as presented in the article.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Citations and evidence anchors

- DOI `10.1063/1.4861380` (extract).
- Abstract and introduction (extract pages 1–2).

## Related topics

- [[reaxff-family]]
