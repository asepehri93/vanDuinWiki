---
id: paper:2025grajales-gonz-xe1-physical-che-methanol-to-hydrocarbon-initiation
type: paper
title: "Methanol-to-hydrocarbon initiation reactions over a zeolite catalyst: reactive molecular dynamics simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:zeolite-porous
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:npt-simulation
  - keyword:qm-training-data
  - keyword:silica-silicate
  - keyword:catalysis-surface
doi: "10.1039/D5CP02704G"
year: 2025
authors:
  - "E. Grajales-González"
  - "Adri C. T. van Duin"
  - "S. Mani Sarathy"
venue: "Phys. Chem. Chem. Phys., 2025, 27, 22776–22798"
pdf_sha256: "908018b033c8cde23b1bf725ad869abcbce71f5d11e079d6d040a191bd9fdf80"
pdf_path: "papers/Gonzalez_zeolite_HCO_PCCP_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025grajales-gonz-xe1-physical-che-methanol-to-hydrocarbon-initiation -->

## Summary

The work reports a **ReaxFF reactive force field** tailored to the **equilibration stage** of **methanol-to-hydrocarbons (MTH)** chemistry in **H-ZSM-5**, studied with **reactive MD** to capture **dynamic** acidity, **cations**, and **water** inside the zeolite—phenomena that static **DFT** studies often omit. The repository includes the **PCCP** article PDF at `pdf_path`; the summary is aligned with the **journal abstract**, introduction context, and **`normalized/extracts/2025grajales-gonz-xe1-physical-che-methanol-to-hydrocarbon-initiation_p1-2.txt`**. The **PCCP** framing distinguishes **pre-steady-state** **dehydration** chemistry from later **olefin**/**hydrocarbon-pool** stages that dominate **long-time** **MTH** **kinetics** in many **mechanistic** **discussions**. A **galley**-labelled PDF is registered separately as [[2025gonzalez-x-paper]] for the same **DOI**.

## Methods

- **Reactive FF (training):** Extends the **Pitman–van Duin** **C/Si/O/Al/Ca** **ReaxFF** line with **C/O** **bond/angle/torsion** terms fit to **DFT** **energies** and **reaction** **profiles** for first **methanol** **conversion** **steps**; **parameter** **optimization** by **least-squares** (or equivalent) **objective** on those **QM** **reference** **data** (full **training** **set** and **weighting** in **PCCP** **Section 2**; mirror [[2025gonzalez-x-paper]] for parallel prose).
- **MD application (LAMMPS):** **LAMMPS** **reactive** **molecular dynamics**; **minimization**, then **NPT** **equilibration** and **heating** **ramps** as in the **manuscript**; **production** **NPT** at target **temperature**s; **0.1** **fs** **time** **step**; **Nosé–Hoover** **thermostat** and **NPT** **barostat** in the **NVT**/**NPT** **stages** described in **PCCP** (≈**1000** **ps** per **600–1200** **K** isothermal **window** as in the **abstract**).
- **PBC and system:** **H-ZSM-5** in **3D** **PBC** **supercells**; **lattice** **and** **atom** **counts** in the **article**.
- **Focus (chemistry):** **Equilibration**-stage **dehydration** toward **DME**, **water**, and **surface methoxy species (SMS)** (before **olefin** / **hydrocarbon-pool** **kinetics**).

**Zeolite** **unit** **cell** **setup**, **Brønsted** **site** **representation**, **Al** **distribution** **assumptions**, and **analysis** of **acid** **speciation** are in the **PCCP** **Computational** sections of `pdf_path` (and **force-field** training in **Section 2** of the paper as referenced on [[2025gonzalez-x-paper]]). **N/A** — external **electric field**; **N/A** — **umbrella sampling** / **metadynamics** / **replica exchange** (not stated for this study in the abstract-level summary).

## Findings

- **Temperature trends (abstract):** **Methanol conversion** rises between **800 K** and **1000 K**, producing **water** and **SMS**; **SMS** formation **drops at 1200 K** as **undesired methane** becomes prevalent. The authors caution that **T > 1200 K** can make reactions **unreliable** in the model owing to **entropy** effects.
- **Humidity at 800 K (abstract):** Water shifts zeolite acidity from **static** to **dynamic**, with **hydronium**-like species; **hydrogen transfer** and **framework activation** (water protonation leaving a **negatively charged framework**) are said to favor **protonated methanol** conversion to **water** and **SMS**.
- **Cations (abstract):** **Cation diffusion** is widespread; the authors **hypothesize** it lowers **entropic barriers** for key steps, highlighting **dynamic** effects beyond static **DFT** pictures.

The **abstract** **cautions** readers that **very** **high** **temperature** **MD** may become **unreliable** when **entropy**-sensitive **steps** dominate, motivating **careful** **interpretation** of **absolute** **rates** from **classical** **reactive** **runs**. **Corpus:** the **VOR** **PDF** at `pdf_path` is the main evidence anchor; **p1–2** **extract**s are **not** a substitute for **section**-level **tables**.

## Limitations

Wiki prose here is a **navigation aid**; **definitive** **numbers** and full **force-field** **training** tables are in the **PCCP** article and **SI** at `pdf_path` (and any **Supporting Information** referenced there), not on this page alone.

## Relevance to group

**Van Duin**-group **ReaxFF** development and **zeolite / MTH** chemistry aligned with **reactive catalysis** simulation lines.

## Citations and evidence anchors

https://doi.org/10.1039/D5CP02704G — *Phys. Chem. Chem. Phys.* **27**, 22776–22798 (2025).

## Reader notes (navigation)

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]

## Related topics

- [[reaxff-family]]
