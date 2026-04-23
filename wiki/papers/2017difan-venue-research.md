---
id: paper:2017difan-venue-research
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
  - keyword:galley-or-proof-pdf
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
pdf_sha256: "bb425eae0d426af0af99cd4ef9066d49d18f7d152cdfc216271a3b2d0dd8c86a"
pdf_path: "papers/Difan_MXene_O_defect_ACS_AMI_proof_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017difan-venue-research -->

## Summary

This corpus PDF is an **ACS Applied Materials & Interfaces proof / accepted manuscript** of the MXene friction study (**same work** as [[2017difan-zhang-acs-computational-study]]). **PBE(+vdw-DF2) DFT** maps **minimum-energy sliding paths**; **LAMMPS** **ReaxFF MD** for **Ti\_{n+1}C\_nO2** uses a **Ti/C/O/F/OH-class** parameter set with **Langevin thermostat** at **10 K and 298 K** and **0.1 fs** timestep. **Static** load–friction analysis gives **coefficients of friction ~0.24–0.27** below **1.2 GPa** normal load (DFT and ReaxFF aligned). **Ti vacancies** and **terminal O vacancies** increase friction but keep **μ < 0.31**. **Ti3C2** with **−OH** or **−OCH3** lowers **μ** to about **0.10–0.14** vs **−O**.

Application context in the article highlights **MXenes** as tunable solid lubricants where oxygen-terminated stacks can exhibit ultralow interlayer shear resistance, and emphasizes quantifying how **Ti** or **O** vacancies and mixed **−OH/−OCH3** terminations perturb friction coefficients under GPa-class contact pressures.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

**Static QM (DFT).** **VASP**, **PAW**, **PBE GGA**; **vdw-DF2** dispersion; **spin-polarized**; **k**-mesh density **~1000 points per atom**; **520 eV** cutoff; **bilayer** supercells with **~10 Å** vacuum normal to layers (**c** lattice fixed to preserve vacuum in the optimization protocol described in *ACS Appl. Mater. Interfaces*); **MEP** analysis of **interlayer sliding**; force/stress thresholds per paper.

**MD application (ReaxFF).** **LAMMPS** drives **ReaxFF** with the **Ti\_{n+1}C\_nT\_x** parameterization (**T = O, F, OH** class) on **O-terminated** **Ti₂CO₂**, **Ti₃C₂O₂**, and **Ti₄C₃O₂** bilayers, including **Ti** sublayer and **terminal O** **vacancies** and **Ti₃C₂** surfaces functionalized with **−O**, **−OH**, or **−OCH₃**. **Protocol highlights** in the **accepted manuscript / proof** mirror **§2** of the **VOR**: **conjugate-gradient** relaxation of **in-plane** lattice vectors, **Langevin** thermostats at **10 K** and **298 K**, and an integration **timestep of 0.1 fs**, with **PBC** in-plane as in the **DFT** supercells. **Friction** is analyzed along **static** loading / **sliding** pathways to extract **μ** vs **normal stress**, **cross-compared** to **DFT** in the paper’s tables.

**Force-field training** is **N/A**. **Electric fields** and **enhanced sampling** are **N/A** in the indexed framing.

Any **additional MD** details (**NPT** segments, **production** times, **shear-rate** studies beyond the **static** friction workflow) should be read from the **version-of-record** PDF/**SI** at the DOI or from **[[2017difan-zhang-acs-computational-study]]** (canonical **`pdf_path`** in this corpus).

**MD blueprint honesty.** **LAMMPS** **molecular dynamics** with **PBC** **bilayers** uses **Langevin** thermostats and **0.1 fs** timesteps as quoted above. **Equilibration**/**production** segment lengths (**ps**/**ns**) for any finite-temperature sampling beyond the **static** friction workflow, plus explicit **barostat**/**pressure** control if **NPT** appears, are **N/A** on this proof-route summary—see **VOR**/**SI**.

## Findings

Same substantive conclusions as **[[2017difan-zhang-acs-computational-study]]**: **low-barrier** sliding paths for **n = 1–3** stacks; **μ ≈ 0.24–0.27** for **p < 1.2 GPa** on **O-terminated** surfaces (**DFT** and **ReaxFF** agreement); **Ti** and **terminal O** **vacancies** increase **μ** but keep **μ < ~0.31**; **−OH** / **−OCH₃** on **Ti₃C₂** drop **μ** to about **0.10–0.14** vs **−O**. **Comparisons:** **DFT** vs **ReaxFF** for **μ**; **defect** vs pristine; **functionalization** vs **−O**. **Sensitivity:** **normal load** (**GPa** range), **defect** density, and **surface chemistry** shift **μ**. **Limitations:** **static** friction estimates and limited **temperature** sampling may miss thermally activated slip; see manuscript discussion. **Corpus honesty:** this path is a **proof PDF**—prefer **[[2017difan-zhang-acs-computational-study]]** for **VOR** tables.

## Limitations

This file path points to a **proof** PDF; for pagination and final figures, prefer the **version of record** at the DOI or the duplicate corpus entry **[[2017difan-zhang-acs-computational-study]]** (different `pdf_path`).

## Relevance to group

**van Duin** co-authored **ReaxFF** validation against **DFT** for **MXene tribology**—a clear **2D materials + mechanics** anchor in the corpus.

## Reader notes (navigation)

- Canonical article PDF in corpus: [[2017difan-zhang-acs-computational-study]].

## Citations and evidence anchors

- DOI: [10.1021/acsami.7b09895](https://doi.org/10.1021/acsami.7b09895)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
