---
id: paper:2017s-jain-journal-of-a-molecular-dynamics
type: paper
title: "Molecular dynamics simulations of flame propagation along a monopropellant PETN coupled with multi-walled carbon nanotubes"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:energetic-materials
  - keyword:graphene-carbon
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1063/1.4975472"
year: 2017
authors:
  - "S. Jain"
  - "G. Mo"
  - "L. Qiao"
venue: "Journal of Applied Physics 121, 054902 (2017)"
pdf_sha256: "3395e3bdebcf9bcf7f84a2915e30a70074a18ae9d6c87b6ff9baca875ab652a0"
pdf_path: "papers/ReaxFF_others/Jain_Mo_Qiao_PETN_CNT_JAP_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017s-jain-journal-of-a-molecular-dynamics -->

## Summary

Jain, Mo, and Qiao simulate **flame-front** **propagation** in **pentaerythritol tetranitrate (PETN)** **coatings** on **multi-walled carbon nanotubes (MWCNTs)** using **ReaxFF** **reactive molecular dynamics** (*J. Appl. Phys.* **121**, **054902**, **2017**, DOI `10.1063/1.4975472`). The physical idea is **multiphysics coupling**: **exothermic** **decomposition** of **PETN** supplies heat, while **MWCNTs** provide **anisotropic** **thermal conduction** that can **re-route** temperature fields relative to **bulk** **PETN**, potentially accelerating or modulating a **reaction** **wave** traveling along the **composite**. The authors scan **PETN** **shell** **thickness** and **nanotube** **diameter** to map how **CNT** **loading** and **geometry** alter **burn** **front** **speed** in idealized **annular** architectures.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF reactive molecular dynamics** (*J. Appl. Phys.* **121**, **054902**, **2017**) studies **flame-front propagation** in an **annular PETN coating** around **multi-walled carbon nanotubes (MWCNTs)**, varying **PETN shell thickness** and **nanotube diameter** to map **MWCNT loading** effects. The abstract/indexed pages emphasize **ReaxFF**’s inclusion of **bond breaking/forming** plus **thermal transport**, but **do not** print **timestep**, **thermostat**, or **ensemble** labels—treat those as **`N/A` from the indexed excerpt** and read **`pdf_path`**.

- **Engine / code:** **ReaxFF MD** as implemented in the article (software named in **Methods** section of PDF).
- **System size & composition:** **Annular PETN + MWCNT** composite geometries with tunable **shell thickness** and **tube diameter** (explicit atom totals in article tables/figures).
- **Boundaries / periodicity:** **N/A** — **PBC** vs finite cluster details not stated in the indexed excerpt.
- **Ensemble:** **N/A** — **NVE/NVT/NPT** not stated in the indexed excerpt.
- **Timestep:** **N/A** — **Δt (fs)** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — ignition + production segment lengths not stated in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt.
- **Barostat:** **N/A** — **NPT** not indicated on indexed pages.
- **Temperature / pressure:** **Hot reactive combustion** conditions implied by **flame** propagation studies; numeric **T/P** schedules are **N/A** here—see PDF.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — direct **ReaxFF** reactive trajectories.

### 2 — Force-field training

**C/H/N/O ReaxFF** parametrization **trained to first-principles data** for **PETN** and related **energetic** chemistry as cited in the article (**not** a new fit performed in this **JAP** paper).

### 3 — Static QM / DFT-only

**QM** supplies **ReaxFF** training/reference data; **on-the-fly AIMD** is **not** the reported production protocol.

## Findings

### Outcomes and mechanisms

**Flame speeds** can reach **~3×** the **bulk PETN** value for selected **annular** geometries; authors attribute enhancement to **PETN layering** around the **MWCNT** that **accelerates heat transport** among **near-surface** PETN molecules, biasing the **reaction wave** along the **conductive** axis.

### Comparisons

Relative to **neat PETN**, composites can demand a **stronger ignition source** because **anisotropic axial conduction** moves **ignition energy** away from the initiation zone more efficiently—yielding a **nonmonotonic** optimum in **MWCNT loading**.

### Sensitivity / design levers

**PETN thickness**, **MWCNT diameter** (loading ratio), and **ignition strength** jointly set whether **preheating** wins over **energy leakage**—producing the **optimal loading** noted in the abstract.

### Limitations and corpus honesty

**CNTs remain largely unreacted** in the simulations summarized—supporting a **thermal conduit** picture rather than a **secondary fuel**. Indexed text is **early pages only**; quantitative **tables** and **safety-relevant** performance numbers belong to the **PDF**. **Idealized single-tube** models omit **bundle morphology**, **defect distributions**, and **interfacial thermal resistance** present in real **energetic composites**.

## Relevance to group

Shows **ReaxFF** used to merge **reactive chemistry** with **anisotropic thermal transport** in carbon-filled energetic composites.

## Citations and evidence anchors

- DOI: [10.1063/1.4975472](https://doi.org/10.1063/1.4975472)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
