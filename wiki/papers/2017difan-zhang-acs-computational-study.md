---
id: paper:2017difan-zhang-acs-computational-study
type: paper
title: "Computational Study of Low Interlayer Friction in Ti_{n+1}C_n (n = 1, 2, and 3) MXene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b09895"
year: 2017
authors:
  - "Difan Zhang"
  - "Michael Ashton"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
  - "Richard G. Hennig"
  - "Susan B. Sinnott"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "e0e583c9cc54c4772559b8df5cd61a167887d27eb75150fbe14e08337d47a6fc"
pdf_path: "papers/Zhang_Difan_MXene_friction_ACI_AMI_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017difan-zhang-acs-computational-study -->

## Summary

The study combines **PBE + vdw-DF2 DFT** for **energy paths** and **LAMMPS ReaxFF** simulations using a **Ti\_{n+1}C\_nT\_x**-compatible reactive potential (**T = O**, etc.). MD uses **Langevin** thermostats at **10 K and 298 K** with **0.1 fs** integration. **Friction coefficients** from **static** loading analyses fall near **0.24–0.27** for **normal loads under 1.2 GPa** for **both DFT and ReaxFF**. **Ti** sublayer and **terminal O** **vacancies increase friction** but leave **μ < 0.31**. **Hydroxyl and methoxy** surface groups on **Ti3C2** reduce **μ** to roughly **0.10–0.14**. The work targets **solid lubrication** and **MXene** **flake** contacts where **interlayer** **shear** dominates **macroscopic** **friction**.

## Methods

**Static QM (DFT).** **VASP** with **PAW** pseudopotentials; **PBE** + **vdw-DF2**; **spin-polarized** initialization as stated; **k**-mesh **~1000 points per atom**; **520 eV** plane-wave cutoff; **bilayer** cells with **10 Å** vacuum separating the stack from its periodic image along **c** (**c** fixed while relaxing atomic positions, per §2); **Hellmann–Feynman** forces **< 1 meV/Å** and **in-plane** stresses **< 0.1 GPa** convergence targets; **MEP** characterization of **interlayer sliding**.

**MD application (ReaxFF).** **LAMMPS** integrates **Ti\_{n+1}C\_nT\_x** **ReaxFF** (**T = O, F, OH**) for the same **bilayer** chemistries as **DFT**—**Ti₂CO₂**, **Ti₃C₂O₂**, **Ti₄C₃O₂**, plus **Ti**/**O** **vacancy** models and **Ti₃C₂** with **−O**, **−OH**, or **−OCH₃** terminations. **Setup (§2):** **conjugate-gradient** relaxation of **in-plane** (**x,y**) cell parameters for **Ti\_{n+1}C\_nO\_2** stacks; **Langevin** thermostats at **10 K** and **298 K**; **timestep 0.1 fs**; **PBC** in-plane consistent with the **DFT** cells. **Friction readout** comes from **static** **loading / constrained sliding** pathways rather than a dedicated **high-shear-rate** production campaign in the indexed **Methods** summary.

**Force-field training** is **N/A** (**published** **MXene** parameters).

**Equilibration/production durations**, **NPT** usage, **barostat** settings, **electric bias**, and **metadynamics** (if any) beyond the **static** friction workflow are **not captured** in the short indexed **Methods** excerpt—confirm in the full **PDF**/**SI**.

## Findings

**Sliding pathways** show **low barriers** for **n = 1–3** **O-terminated** stacks. **Friction coefficients ~0.24–0.27** for **normal loads < 1.2 GPa** agree between **DFT** and **ReaxFF** (**Ti₂CO₂**, **Ti₃C₂O₂**, **Ti₄C₃O₂** table in the paper). **Vacancies** raise **μ** through **roughness** and **added adhesion** but keep **μ < ~0.31**. **−OH** and **−OCH₃** on **Ti₃C₂** reduce **μ** to about **0.10–0.14** vs **−O**. Authors use the **DFT/ReaxFF** match on **μ** to argue **ReaxFF** is suitable for **larger/longer** tribology sampling where **DFT** **MEP** work is costly. **Comparisons:** side-by-side **DFT** vs **ReaxFF** **μ** tables; **vacancy** vs pristine; **−OH/−OCH₃** vs **−O**. **Sensitivity:** **normal load** (**GPa**), **defect** type, and **termination** chemistry. **Limitations / outlook:** authors note **static** friction analysis and **MXene** chemistry transferability limits; humidity/intercalants may alter **adhesion** vs **vacuum bilayer** models. ## Limitations

**Static friction estimates** and **limited MD temperatures** may not capture **thermally activated** slip at all operating conditions; **force field** transferability to **other MXene chemistries** is not claimed. **Humidity** and **intercalated** **solvent** could modify **adhesion** relative to **vacuum** **bilayer** models.

## Relevance to group

Joint **DFT + ReaxFF** benchmark on **MXene friction** with **van Duin** involvement—useful reference for **2D tribology** parameter choices.

## Reader notes (navigation)

- Alternate corpus path (proof PDF): [[2017difan-venue-research]]. Prefer the **AMI** **VOR** PDF cited in `pdf_path` when reconciling **table** entries for **μ**.

## Citations and evidence anchors

- DOI: [10.1021/acsami.7b09895](https://doi.org/10.1021/acsami.7b09895)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
