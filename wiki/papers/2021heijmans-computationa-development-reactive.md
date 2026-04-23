---
id: paper:2021heijmans-computationa-development-reactive
type: paper
title: "Development of a reactive force field for CaCl2·nH2O, and the application to thermochemical energy storage"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:npt-simulation
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2021.110595"
year: 2021
authors:
  - "Koen Heijmans"
  - "Sophie Nab"
  - "Bern Klein Holkenborg"
  - "Amar Deep Pathak"
  - "Silvia Gaastra-Nedea"
  - "David Smeulders"
venue: "Computational Materials Science, 197 (2021) 110595"
pdf_sha256: "8f9b828e6c7de2c07ce48c39d6e7602d95408226f8732f6d18d2402437edeef6"
pdf_path: "papers/ReaxFF_others/Heijmans_CaCl2_CompMatSci_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021heijmans-computationa-development-reactive -->

## Summary

The authors re-parameterize a **ReaxFF** description of **CaCl\(_2\)·\(n\)**H\(_2\)O (emphasis on **\(n=0,2\)**) building on **Pathak *et al.***’s prior fit, which showed **unphysical** **disintegration** of **higher hydrates** in MD. A **Metropolis Monte Carlo (MMC)** optimizer with **DFT** (and **MD-trajectory** snapshots added iteratively) stabilizes **bulk** **crystals** and reproduces **EOS**, **surface energies**, **reaction** **enthalpies**, and **RDFs**. Applications include **NEMD** **thermal** **conductivity** (anisotropic **x–y–z**), **vacuum-slab** **dehydration** (300–500 K, **0.25 fs**, **NPT** equilibration at **1 bar** with **H\(_2\)O** removal in the **vacuum**), and **cracked** / **porous** **morphologies**; reported **\(\kappa\)** for anhydrous and dihydrate **agree** with **measurements** to the level quoted in the paper.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **Reactive MD** in the workflow described in *Comput. Mater. Sci.* **197** (2021) 110595; text references **NEMD** for **\(\kappa\)** with **Berendsen**-style **region** **thermostats** (hot **330 K** / cold **300 K** **source/sink** with **τ = 100 fs**; **interior** **weak** coupling **τ = 100 ps** to avoid spurious **heat** **leaks** as stated in **§2.4.2**).
- **System & composition:** **CaCl\(_2\)** and **CaCl\(_2\)·2H\(_2\)O** **slabs** and **defective** **crystals**; **6×6** in-plane **slabs** with **vacuum** (e.g. **1000 Å** in one **direction** for **dehydration**); **grain** **boundaries** and **crack** **models** as in **Figs. / sections** on **imperfect** **crystals**. **H\(_2\)O** that **moves** **>30 Å** from the **surface** is **removed** every **0.125 ps** in the **dehydration** **protocol** to preserve **driving** **force**.
- **Boundaries / periodicity:** **3D PBC** in **supercell** **equilibration**; **slabs** with **vacuum** in **one** **direction** for **dehydration**; **NEMD** **\(\kappa\)** uses **in-cell** **thermostat** **zones** as in the article.
- **Ensemble:** **NPT** at **1 bar** for **3×10\(^5\)** **iterations** in **slab** **preequilibration** (0.25 fs); **NEMD** uses **NVT**-like **heating** **control** in **slices** (as described in **NEMD**); **NPT** / **NVT** choices follow each subsection in **Section 2.4** of the PDF.
- **Timestep:** **0.25 fs** in the **equilibration** **example** in **§2.4.1**; NEMD **\(\Delta t\)** per **reactive** **MD** standard in the article.
- **Duration / stages:** **3×10\(^5\)** **steps** **equilibration** before **slab** **extraction**; **300–500 K** **dehydration** **runs**; **\(\kappa\)** at **various** **system** **lengths** to **mitigate** **finite-size** (see **NEMD** **discussion**).
- **Thermostat:** **Berendsen** **(τ = 100 fs)** in **NEMD** **hot/cold** **blocks**; **weaker** **coupling** **(τ = 100 ps)** in the **transit** **region** as quoted.
- **Barostat / pressure:** **NPT** **1 bar** **isotropic** **(Berendsen-style)** in **slab** **preequilibration**; **N/A** for **pure** **NEMD** **\(\kappa\)** **strips** (those **fix** **T** **zones** rather than **bulk** **hydrostat** in the **NEMD** **paragraph**).
- **Temperature:** **300–500 K** **dehydration**; **330/300 K** **NEMD** **\(\Delta T\)**; **heating** **of** **crack** **models** as in **relevant** **§**.
- **Electric field:** N/A.
- **Enhanced sampling:** N/A.

**Corpus note:** The **extracted** **text** may use **"MD"** without a **dedicated** **LAMMPS** **string**; **reactive** **dynamics** **are** run with **ReaxFF** in the **software** **stack** **cited** in the **article** (confirm **in** the **VOR** **PDF** for **version-specific** **keywords**).

### 2 — Force-field training

- **Parent / scope:** **Pathak *et al.*** **CaCl\(_2\)** / **hydrate** **ReaxFF** as **starting** **point**; **goal:** fix **crystal** **stability** for **higher** **hydrates** and **condensed** **phases** used in **TCM** **modeling**. **QM reference:** **ADF** **GGA-PW92** on **molecular** / **non-periodic** **training** **geometries**; **VASP** **PBE** + **PAW** + **DFT-D3(BJ)** on **periodic** **training** **crystals**; **force** **convergence** **<0.026 eV/Å** as in **§2.1**. **Training set:** **reactions**, **condensed** **phases**, **and** (critically) **recomputed** **QM** **on** **“bad”** **MD** **frames** from **unstable** **intermediate** **ReaxFF** **fits**, **iteratively** **appended** (**Fig. 2** **loop**). **Optimization:** **MMC** **(Metropolis** **Monte** **Carlo)** **reoptimization** of **ReaxFF** **parameters** against **the** **augmenting** **QM** **set**. **External** **validation:** **\(\kappa\)** **vs** **experiment**; **(de)hydration** **trends** **vs** **T** **/ vapor** **pressure** **assumptions** in **the** **main** **text**, **Figs. 1–3** **et** **seq.**

### 3 — Static QM (training reference)

**Covered** under **§2.1** **as** the **source** of **Energies/structures** **for** **ReaxFF**; **N/A** as a **separate** **conclusion** **—** the **manuscript** **is** **centered** on **reactive** **FF** + **MD**.

### 4 — Review

N/A.

## Findings

**Force-field quality:** The **refined** **ReaxFF** **eliminates** **unphysical** **melting** of **dihydrate** **/ bulk** **samples** in **the** **cases** **shown** while **matching** **reaction** **enthalpies** **(Fig. 1)**, **EOS** **(Fig. 6)**, and **elastic/thermal** **data** as **tabulated/figured** in the **article**. **\(\kappa\):** **~1.1 W m\(^{-1}\) K\(^{-1}\)** **(anhydrous CaCl\(_2\))** and **~0.5 W m\(^{-1}\) K\(^{-1}\)** **(dihydrate)** align with **measurements** in the **quoted** **comparison**. **Anisotropy / microstructure:** **Layered** **stacks** and **grain** **boundaries** **reduce** **\(\kappa\)** and **slow** **z-direction** **dehydration** (initial **rates** **~1.9–2.5×** **slower** **along** **z** **in** the **cited** **result**). **Pores** **/ cracks** **open** **fast** **H\(_2\)O** **egress** **pathways** **(Figure** **/ section** **on** **heating** **+** **cracks**). **Comparisons:** **Experiment** **(thermal** **conductivity)**, **prior** **ReaxFF** **/ literature** **DFT** **(training)**. **Limitations (authored + empirical):** **ReaxFF** **is** **still** **empirical**; **NEMD** **\(\kappa\)** **suffers** **finite-size** **effects** **(mitigation** **described)**. **Corpus** **/ KB** **honesty** **: numeric** **detail** from **`pdf_path`** **and** **SI** **citation** in **the** **VOR** **file**.

## Limitations

ReaxFF may **extrapolate** **poorly** **outside** the **calibrated** **(de)hydration** and **T** **window**; **NEMD** and **reactive** **kinetics** **remain** **models**, **not** **reactor-scale** **continua**.

## Relevance to group

Salt-hydrate **ReaxFF** **development** **(not** **PSU** **author** **list)**; **relevant** to **reactive** **FF** **practice** **in** **energy** **storage** **materials**.

## Citations and evidence anchors

Sections **2.1–2.4** and main **figures** on **training**, **NEMD** **\(\kappa\)**, **dehydration** **/ cracks**, *Comput. Mater. Sci.* **197** (2021) 110595.

## Related topics

- [[reaxff-family]]
