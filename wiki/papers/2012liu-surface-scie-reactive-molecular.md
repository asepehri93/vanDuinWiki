---
id: paper:2012liu-surface-scie-reactive-molecular
type: paper
title: "Reactive molecular dynamic simulations of hydrocarbon dissociations on Ni(111) surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:nose-hoover
source_refs: []
doi: "10.1016/j.susc.2011.11.035"
year: 2012
authors:
  - "Liu, Bin"
  - "Lusk, Mark T."
  - "Ely, James F."
venue: "Surface Science"
pdf_sha256: "f57177ba717b570ade4596106600c85116c7ce43ab4a1a94fd18414ce6ca31f9"
pdf_path: "papers/ReaxFF_others/Liu_Lusk_NiCH_SurfSci2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012liu-surface-scie-reactive-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF** parameters for **H, C, and Ni** are developed using **DFT** training data on **hydrogen** and **methane** reactions with **Ni(111)**. The fitted field is used in **MD** to study **dissociative adsorption** of **methane**, **ethane**, and **n-butane** on **Ni(111)**. The work reports estimates for **methane** **sticking** (zero-coverage limit) and **activation energy** for the first **C–H** cleavage, **elementary** **CH_x** step rates** via surface-species monitoring and a **microkinetic** construction, and qualitative networks for **ethane** / **n-butane** decomposition.

## Methods

**QM training (DFT):** Geometries and energies for **Ni/C/H** training data use a real-space **numerical atomic orbital** extended **DFT** code (**PW91** exchange-correlation, **DNP** basis, **semi-core pseudopotential** for **Ni** with **p** valence, spin polarization). Convergence criteria and **Monkhorst-Pack** sampling are given in Section 2.2; surface reactions use a **five-layer** **p(3x3)** **Ni(111)** slab with the **bottom two layers fixed**, **2x2x1** **k**-points, and **LST/QST** transition-state searches with frequency confirmation.

**ReaxFF development:** **Ni-H**, **Ni-C**, and related **valence** terms are fit to the **DFT** set (parameters in **SI** tables); the article compares **ReaxFF** to **DFT** for **Ni** **EOS** and key **adsorption** geometries.

**Reactive MD (GRASP):** **NVT** simulations of **methane**, **ethane**, and **n-butane** on **Ni(111)** use a **six-layer** **rectangular** slab (**720** **Ni** atoms in the main setup; a **four-times** larger **2880-atom** slab for some **methane** runs), **lateral** periodicity, **~49.7 A** vacuum normal to the surface, and up to **200** **methane** (or **60** **ethane** / **30** **n-butane**) molecules as stated. **Alkane** dissociation is studied from **700 K** to **1500 K**. **Equilibration:** **10^4** steps at **Delta t = 0.25 fs** with temperature rescaling; **C-Ni/H-Ni** reactive terms **disabled** during equilibration. **Production:** reactive terms **enabled**, **Nose-Hoover** thermostat (**Q = 100**), neighbor list every step, runs up to **~1 ns** for sampling.

**Microkinetics:** **Surface** species counts from **MD** are coupled to a **microkinetic** model for **methane** stepwise **CH4 -> CHx*** kinetics (**Eqs. 5-6** in the paper).

### MD application (GRASP reactive MD on Ni(111))

**Engine / code:** **Reactive MD** in **GRASP** (as stated in Section 2.3 of the article).

**System size & composition:** **Six-layer** rectangular **Ni(111)** slabs with **720 Ni** atoms in the primary setup (and **2880 Ni** atoms for selected larger **methane** runs), plus adsorbate loadings up to **200** **CH\(_4\)**, **60** **C\(_2\)H\(_6\)**, or **30** **n-C\(_4\)H\(_10\)** molecules as reported.

**Boundaries / periodicity:** **Lateral** **periodic** boundary conditions with **~49.7 Å** vacuum normal to the surface.

**Ensemble:** **NVT** during production after equilibration.

**Timestep:** **0.25 fs** (**Δt**) after equilibration.

**Duration / stages:** **Equilibration:** **10⁴** steps with temperature rescaling while **C–Ni**/**H–Ni** reactive terms are **disabled**; **production:** reactive terms **enabled** with runs up to **~1 ns** for sampling.

**Thermostat:** **Nosé–Hoover** thermostat with thermostat mass parameter **Q = 100** (units as defined in the article).

**Barostat / pressure control:** **N/A —** **NPT** barostat not used for these **NVT** surface simulations.

**Temperature:** **700 K** to **1500 K** range surveyed for **alkane** chemistry.

**Pressure / stress:** **N/A —** external **hydrostatic pressure** control not stated for these **NVT** slab runs.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training (Ni–C–H ReaxFF)

**Parent FF / elements:** **ReaxFF** parameters for **H**, **C**, and **Ni** developed for **Ni(111)** **hydrocarbon** chemistry.

**QM reference:** Real-space **numerical atomic orbital** extended **DFT** with **PW91** and **DNP** basis; **spin-polarized** **Ni**; **Monkhorst-Pack** **k**-sampling and convergence settings in Section 2.2.

**Training set / reference data:** **DFT** geometries/energies for a subset of **hydrogen** and **methane** reactions with **Ni(111)** surfaces; **EOS** and key **adsorption** motifs included in the fit.

**Optimization:** Parameters optimized to the **DFT** training set (implementation details and weighting in **`pdf_path`**).

**Reference data used:** **DFT** reaction and **EOS** data; **ReaxFF** vs **DFT** comparisons for **Ni** **EOS** and **adsorption** geometries as reported.

## Findings

**Methane:** **MD** plus fitting give a **zero-coverage** sticking prefactor and an **activation energy** for **dissociative adsorption** in line with prior literature orders of magnitude; **microkinetic** rates fitted to the same trajectories reproduce **surface** **CHx** evolution, with **CH** decomposition **rate-limiting** at lower **T** and **carbon** buildup at **1500 K**. **Ethane** / **n-butane:** trajectories illustrate **multi-step** decomposition networks on **Ni(111)** without the same quantitative **kinetic** closure as for **methane**.

## Limitations

Empirical **ReaxFF** vs **QM** accuracy; finite **surface** models and **coverage** effects; extract is **p1–2**—full paper holds complete numerical tables.

## Relevance to group

**Ni** **hydrocarbon** **ReaxFF** development and **catalytic** **MD** comparable in spirit to group **metal**/**hydrocarbon** reactive simulations.

## Citations and evidence anchors

- DOI **10.1016/j.susc.2011.11.035** — *Surface Science* **606**, 615–623 (2012).
- Extract: `normalized/extracts/2012liu-surface-scie-reactive-molecular_p1-2.txt`.

## Related topics

- [[reaxff-family]]
