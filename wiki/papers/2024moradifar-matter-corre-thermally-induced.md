---
id: paper:2024moradifar-matter-corre-thermally-induced
type: paper
title: "Thermally induced structural evolution and nanoscale interfacial dynamics in Bi-Sb-Te layered nanostructures"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.matt.2024.08.006"
year: 2024
authors:
  - "Moradifar, P."
  - "Wang, T."
  - "Nayir, N."
  - "Sharifi, T."
  - "Wang, K."
  - "Ajayan, P."
  - "van Duin, A. C. T."
  - "Alem, N."
venue: "Matter"
pdf_sha256: "3ec1f8c6a5db2c51189cf7f09acc4e2cb6c319ef3ebb783e873f0e74eabe34f1"
pdf_path: "papers/Moradifar_SeBiTe_Matter_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024moradifar-matter-corre-thermally-induced -->

## Summary

Moradifar and colleagues study **thermal evolution and sublimation** in **Bi–Sb–Te** layered systems—**\( \mathrm{Bi}_2\mathrm{Te}_3/\mathrm{Sb}_2\mathrm{Te}_3 \) in-plane heterostructures** and **\( \mathrm{Sb}_{2-x}\mathrm{Bi}_x\mathrm{Te}_3 \) alloys**—using **in situ transmission electron microscopy (TEM/STEM)** at elevated temperature together with **density functional theory (DFT)** for **defects and edge energetics**. The work links **heterointerfaces**, **native point defects**, and **edge configurations** to **anisotropic Te loss**, **layer-by-layer** processes, and **polygonal nanopores** observed during annealing.

## Methods

**Synthesis and samples.** **Bi\(_2\)Te\(_3\)** nanoplates are grown **solvothermally** with **Te-seeded** pathways; **heterostructures** are obtained by **growing Sb\(_2\)Te\(_3\)** on **Bi\(_2\)Te\(_3\)** seeds, while **alloys** co-introduce **Bi and Sb** precursors (see **Experimental procedures** in the PDF).

**In situ electron microscopy.** Samples are prepared by **solvent-assisted exfoliation** (IPA/water), deposited on a **fusion in situ heating** holder. Imaging uses a **Talos F200X** STEM with **heating stage** and **EDS**; **HAADF-STEM**, **TEM**, **EDP**, and **XEDS maps** characterize structure and composition. **In situ annealing** is performed under **vacuum** with parameters such as **5 °C/min** ramp and **2 s** per frame; the beam is **blanked** during heating to emphasize **thermal** rather than **beam-driven** dynamics, with **80 kV** primary voltage to reduce knock-on damage (a **200 kV** comparison is noted).

**DFT.** Native **defect** and **edge** energies for **2D Bi\(_2\)Te\(_3\)**-like units use **VASP**, **PAW** potentials, and the **PBE** GGA functional (see **DFT simulation** subsection). **Cutoff, k-mesh, dispersion, NEB, TS searches:** if not in this page, **Matter** **7** (2024) **PDF** *DFT simulation*; **N/A** to treat this note as a full DFT methods dump. **1 — MD** production: **N/A** (TEM experiment + DFT). **2 — ReaxFF** training: **N/A**. **3 — DFT** focus: **defect** / **edge** **formation** **energetics** vs **Te** **chemical potential**; **formation energy** and **reaction**-path **barrier**-like **stability** **properties** as in the *Matter* *DFT simulation* section (full **band gap** or **phonon** tables: **N/A** in this TEM-first summary).
## Findings

**Microscopy.** During heating, the structures show **edge evolution**, **layer-by-layer sublimation**, and **formation/coalescence of polygonal nanopores**. **Heterostructures** exhibit **triangular** and **quasi-hexagonal** pore motifs; **preferential Te loss** at reactive regions reduces **thermal stability**, especially near **heterointerfaces** and **defect-rich** areas.

**Theory.** **Antisite defects** (**Te\(_\mathrm{Sb}\)**, **Te\(_\mathrm{Bi}\)**) are highlighted as **low-formation-energy** native defects that participate in **defect-assisted sublimation**. **Edge formation energies** vs Te chemical potential rationalize **which edge terminations** dominate **growth vs sublimation** regimes and help interpret **morphology changes** (e.g., **hexagonal-to-triangular** transformations) with temperature.

The paper’s narrative connects **microscopy movies** to **defect thermodynamics**: regions that **lose Te** fastest are not arbitrary, but track **heterointerfaces** and **antisite-rich** neighborhoods predicted to be **thermodynamically** favored in the DFT models. **T**-dependent **TEM/STEM** behavior and **200 kV** control experiments are in the main **Methods**; use the **Matter** **PDF** for **T** **ramps** and **beam**-mitigation detail.
## Limitations

**In situ TEM** can still couple **temperature** with **finite electron dose** despite mitigation; **DFT** models simplify **finite temperature** and **beam chemistry**. **Synthesis** variability may influence **defect populations** compared with idealized calculations.

## Relevance to group

**Adri C. T. van Duin** is a co-author; the study is **experiment-forward** on **layered chalcogenides** with **DFT** interpretation—useful cross-reference for **defect and interface** chemistry relevant to **2D materials** modeling.

## Citations and evidence anchors

- Experimental procedures and DFT: **Experimental procedures** / **DFT simulation** sections (*Matter* **7**, 1–16 (2024)); DOI above.

## Related topics

- [[reaxff-family]]
