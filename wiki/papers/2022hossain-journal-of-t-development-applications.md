---
id: paper:2022hossain-journal-of-t-development-applications
type: paper
title: "Development and Applications of an eReaxFF Force Field for Graphitic Anodes of Lithium-Ion Batteries"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:ereaxff
  - method:reaxff
  - task:parameterization
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:charge-equilibration
source_refs: []
doi: "10.1149/1945-7111/aca362"
year: 2022
authors:
  - "Md Jamil Hossain"
  - "Gorakh Pawar"
  - "Adri C. T. van Duin"
venue: "J. Electrochem. Soc."
pdf_sha256: "f7be9b5582523667c460049ee97df2b2342cc818e012d4dd324536a2bdb92d6a"
pdf_path: "papers/Hossain_eReaxFF_graphene_2022_J_ElectrochemSoc_169_110540.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022hossain-journal-of-t-development-applications -->

## Summary

The work introduces an **eReaxFF** parametrization for **graphitic** carbon that carries an **explicit electronic degree of freedom**, aimed at large-scale atomistic models of **electron conduction** and **finite-bias**-like scenarios in **Li-ion battery anodes**. The motivation is to move beyond fixed charge-equilibration pictures when excess electrons localize at defects or under applied bias. The parametrization is checked against **quantum-chemistry** reference data (including **electron affinities** and **equations of state**), and simulations reproduce **qualitative** trends in **electron conductivity** for pristine and defective graphitic models across **temperature** and **applied voltage**. **Excess electron localization** near a defect from eReaxFF agrees well with **DFT**. Simulations also show **lithium metal plating** initiated by **electron transfer** from the graphene surface toward exposed Li ions, illustrating a path toward modeling **electrode–electrolyte** phenomena with explicit electronics.

## Methods

### A — eReaxFF parameterization / model

- **eReaxFF:** **ReaxFF** extended with **explicit electronic** degrees of freedom for **graphitic** carbon—**bond-order**-dependent coupling of **nuclei** to **excess charge** / **carrier** populations.

### B — Validation vs QM

- **DFT** (or related **QC**) benchmarks on **energies**, **affinities**, **EOS**; **defect** **charge localization** vs **eReaxFF** on **surface** imperfections.

### C — Production MD (battery-relevant interfaces)

- **Graphite** models with **defects**; **temperature** and **bias**/**voltage** conditions in *J. Electrochem. Soc.* **Methods**.
- **Li** **intercalation** / **plating** trajectories with **interfacial electron transfer** tracked alongside **ion** positions.

### D — Experiments

- None; qualitative comparison to **conductivity** trends from literature as discussed.

Integrated protocol (with locators in the version-of-record **PDF**): **1 — MD / eReaxFF dynamics.** **Engine: LAMMPS**-class **eReaxFF** **molecular dynamics**; **graphene** / **graphitic** **supercell** and **defect** models with **3D PBC**; **NVT**/**NVE**-class integration with a **thermostat** and **fs**-scale **timestep**; **ps**–**ns** **equilibration**/**production** as in *J. Electrochem. Soc.* **169** **110540**. **Bias** and **voltage** enter through the **explicit** **electronic** DOF (**not** “E-field: N/A” in the electrochemical sense). **Barostat: N/A** for the illustrations summarized. **Hydrostatic pressure: N/A** in the main abstract narrative. **N/A** in this short note for full **atom** **counts** and one-line **E-field** magnitudes—read the **Methods**/**SI**. **Replica / enhanced sampling: N/A** to the eReaxFF **demonstrations** highlighted. **2 — eReaxFF training.** **Parent** **ReaxFF**/**eReaxFF**; **DFT**/**QM** **training** **energies**/**forces**, **affinity** and **equation-of-state** targets, **optimization**, and **validation** **data** are described in the article; **N/A** to reproduce every table here.

## Findings

**Outcomes / mechanisms:** **eReaxFF** reports **qualitative** **electronic** **conduction** vs. **temperature** and **voltage**/**bias** in **pristine** and **defective** **graphite**; **DFT**-consistent **excess** **charge** at **imperfections**. **Li** **plating** can be shown from **interfacial** **electron** **transfer** to **lithium** **ions**—a route toward **electrode–electrolyte** **phenomena** with **explicit** **carriers**, but **not** a quantitative **transport** **calibration**. **Comparisons: versus** **QM** on **defects**; **vs** experiment is **trend**-level, not a transport coefficient **benchmark**. **Sensitivity: temperature** and **bias**; **defect** **density** changes **local** **trapping**. **Authored** **limitations** (quantitative **vs** **real** anodes) remain in the **JES** text. **Corpus / KB** — **p1–2** **extract** **misses** full **protocol** **numbers**; use the **open** **PDF** **(169, 110540)** for **citable** **detail** and for **any** **SI** **replica**; **this** page does **not** add **chemistry** beyond those **sources**.

## Limitations

Qualitative conductivity matching; users should check quantitative transport numbers and bias ranges against experiment and higher-level electronic-structure theory for their specific cells. System sizes in interfacial battery modeling often under-resolve long-wavelength polarization and image-charge effects that real electrodes supply, so the eReaxFF stage is best viewed as a mechanistic microscope for local electron–ion coupling rather than a drop-in replacement for continuum transport solvers. **J. Electrochem. Soc.** **169**, **110540** is the citable **volume**/**issue** anchor for the **open** PDF in this corpus.

## Relevance to group

Core **eReaxFF** development at Penn State for **battery anodes** and **graphitic** carbon—extends the ReaxFF lineage toward electrochemical fidelity.

## Citations and evidence anchors

- DOI: [10.1149/1945-7111/aca362](https://doi.org/10.1149/1945-7111/aca362)

## Reader notes (navigation)

- Cluster with [[batteries-interfaces-reaxff]] and [[theme-reactive-md-corpus]] for eReaxFF and electrochemical interface context.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
