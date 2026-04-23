---
id: paper:2023nabankur-dasgupta-j-phys-chem-hydrophobic-nanoconfinement
type: paper
title: "Hydrophobic Nanoconfinement Enhances CO2 Conversion to H2CO3"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - method:enhanced-sampling
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:water-interfaces
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.3c00124"
year: 2023
authors:
  - "Nabankur Dasgupta"
  - "Tuan A. Ho"
  - "Susan B. Rempe"
  - "Yifeng Wang"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "3514a2a122f23770981b80c7dbf208283c5c49c4f5faf0642c3a7982f8ffef25"
pdf_path: "papers/ReaxFF_others/Dagupta_JPCL_2023_CO2_confinement.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023nabankur-dasgupta-j-phys-chem-hydrophobic-nanoconfinement -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *J. Phys. Chem. Lett.* article identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF metadynamics** is used to study **CO\(_2\)** hydration to **carbonic acid** in **bulk vs nanoconfined** water, reporting **free-energy** differences and mechanistic roles of **confinement** and **surface chemistry**. Carbonic acid formation from CO\(_2\) in water matters for **geologic carbonation**, **clay interlayers**, and **CCUS** contexts. The authors compare **potential of mean force (PMF)** profiles for **CO\(_2\) → H\(_2\)CO\(_3\)** in bulk water and in **hydrophobic nanoconfined** aqueous environments, including effects on **barriers**, **thermodynamics**, and **charged intermediates**. **Nanoconfinement** is modeled as a **structured** **pore** environment intended to **mimic** **clay-like** **interfacial** **water** **networks**, where **dielectric** **screening** and **hydrogen-bond** **topology** differ from **isotropic** **bulk** **liquid**.

## Methods

**Scope.** The *J. Phys. Chem. Lett.* letter uses **ReaxFF** with **well-tempered metadynamics** in **LAMMPS** (via **COLVARS**) to compare **CO\(_2\)** → **H\(_2\)CO\(_3\)** free-energy landscapes in **bulk** versus **nanoconfined** water between **pyrophyllite** (hydrophobic) walls. The main text points to the **Supporting Information** for the full ReaxFF choice, equilibration schedule, and metadynamics “hill” parameters; the main text is sufficient for the cell definitions and two CVs.

### 1 — MD application (reactive ReaxFF + well-tempered metadynamics)

- **Engine / code:** **LAMMPS** with the **COLVARS** **package**; **well-tempered metadynamics** is applied **after** **equilibration** (as referenced in the main text and **SI**).
- **System size & composition (Figure 1):** **Bulk** model—cubic **12.5 × 12.5 × 12.5 Å³** with **one** **CO\(_2\)** and **64** **H\(_2\)O** molecules. **Confined (nanopore)** models—**pyrophyllite** + **pph (hydrophobic) surface**: **(b)** two water layers, cell **20.64 × 17.93 × 15 Å³**, **one** **CO\(_2\)** + **92** **H\(_2\)O**; **(c)** one water layer, **20.64 × 17.93 × 12 Å³**, **one** **CO\(_2\)** + **54** **H\(_2\)O** (1W/2W notation in the article).
- **Boundaries / periodicity:** **Periodic boundary conditions** in **all** three dimensions for the cells quoted above (main text, Figure 1).
- **Ensemble / FES construction:** The **FES (Figure 2)** is a **two-dimensional** function of the two **collective variables** below; the main text defers the detailed **NVT** thermostating and ReaxFF integration details to the **SI**.
- **Timestep / thermostat / metadynamics weights:** **N/A in the main text**—exact **timestep**, **NVT** **thermostat** settings, **hill** height, **pace**, and **well-tempered** **ΔT** for metadynamics are in the **Supporting Information** of the *JPCL* article, not in the first pages excerpted for this curation.
- **Duration / stages (main text only):** **FES** maps in **Figure 2**; for **bulk** water the minimum-energy path in **Figure 2a** uses the **finite-temperature string method** (cited; **see SI**). **N/A in main text** for a single consolidated **ps/ns** “production” label for every panel—the article presents **FES** surfaces rather than a one-line trajectory length.
- **Temperature / pressure:** **N/A in main text** for the explicit **K** and **1 atm** setpoints; **N/A**—no **NPT** barostat is described in the main-text free-energy story (confinement is a **quasi-1D/2D** water slab between walls).
- **Electric field:** **N/A**—no static or oscillating **E-field** in the free-energy problem as set up in the main text.
- **Enhanced sampling (CVs):** **Two collective variables** (CV1, CV2) span the **2D** **FES**: (i) **CV1**—coordination of **C(CO\(_2\))** to **O** of **H\(_2\)**O; (ii) **CV2**—coordination of **O(CO\(_2\))** to **H** of water (main-text equations; cutoffs **1.6** Å and **1.3** Å as printed).

### 2 — Force-field training (ReaxFF)

**N/A** in the sense of a *new* fit publication—this work **applies** ReaxFF to aqueous **CO\(_2\)/H\(_2\)**O chemistry; parameter lineage and any training references are in the **SI**/**Methods** of the *JPCL* article.

### 3 — Static QM

**N/A** as a primary workflow—the letter cites prior **ab initio** literature for **barriers** in **bulk** water (Introduction) to motivate the problem. **No** new **DFT** table is the main deliverable; **FES** and **reactive** **MD** are **ReaxFF**-level.

## Findings

**Outcomes and mechanisms (main text).** The **2D** **FES (Figure 2)** show a **reduced** barrier to **H\(_2\)** **CO\(_3\)** formation in **confinement** and can **reverse** the net **thermodynamics** from **endothermic in bulk** to **exothermic** in the most confined (1W) case compared with bulk, as summarized in the abstract. **Charged** intermediates appear more often in **confined** water, and the authors connect **stronger** **hydration** and more favorable **proton** **transfer** under **confinement** to the shifted **kinetics/thermodynamics** (see abstract and *JPCL* discussion).

**Comparisons and caveats.** **Well-tempered metadynamics** and **2D** **FES** choices determine apparent barriers and minima; **convergence** and **hysteresis** must be read against the **SI** and **ReaxFF** error bars. The abstract positions the work in **clay–CO\(_2\)/water** and **CCUS**-adjacent **nanopore** contexts and stresses dependence on **confinement geometry**, **surface** chemistry, and **CO\(_2\)** loading—transferable trends are **not** a single set of “bulk-like” **PMF** numbers.

## Limitations

**ReaxFF** and **metadynamics** limitations: **proton** **transfer** and **charged** **species** energetics are not **DFT**-exact; **FES** depend on **CV** definitions, **well-tempered** parameters, and equilibration (see **SI** for what the authors actually ran). The local **PDF** includes a **ResearchGate** **cover** page; the **full** **article** text (including **cell** sizes, **CV** cutoffs, and **Figure 1–2**) starts after that front matter in the same file. **Hill** **reweighting** and **2D** **FES** projections can mask **kinetic** prefactors; treat **barriers** as **ReaxFF**-level for **order-of-magnitude** **mechanistic** use, not absolute **rates** without **QM** **validation** on a subset of paths.

## Relevance to group

Shows **ReaxFF + metadynamics** for **environmental aqueous interfaces**, adjacent to van Duin-group **clay/water/electrolyte** experience.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.3c00124](https://doi.org/10.1021/acs.jpclett.3c00124)

## Related topics

- [[reaxff-family]]
