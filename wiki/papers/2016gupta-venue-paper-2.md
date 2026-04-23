---
id: paper:2016gupta-venue-paper-2
type: paper
title: "Supporting Information: Carbonization with misfusion (Advanced Materials, 2016)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1002/adma.201603009"
year: 2016
authors:
  - "Nitant Gupta"
  - "Vasilii I. Artyukhov"
  - "Evgeni S. Penev"
  - "Boris I. Yakobson"
venue: "Advanced Materials (Supporting Information)"
pdf_sha256: "30dff1a5bc00ebfd1b960592148c130e126b1858d70857f4cbd276edd45c651b"
pdf_path: "papers/ReaxFF_others/Gupta_D_Loops_AdvMat_SupportingInfo.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-application
  - keyword:lammps
---
<!-- id:paper:2016gupta-venue-paper-2 -->

## Summary

This PDF is the **Supporting Information** for *Carbonization with misfusion: Fundamental limits of carbon fiber strength revisited* (*Adv. Mater.* 2016). It documents **simulation design** (periodic **D-loop pairs** vs **single D-loop** non-periodic cells), **von Mises stress** definitions, **strain/stress protocols**, and **length-contraction** simulations of **N-terminated graphene nanoribbons** referenced in the main article, plus an **elliptical-hole** elasticity discussion relating idealized holes to **non-elliptical** D-loop stress concentration (**SI** §4). Read strengths and mechanisms together with [[2016gupta-venue-paper]].

## Methods

- **von Mises stress:** Explicit **Cauchy stress tensor** formula (Eq. (SI.1)) used with simulation stresses.
- **Configuration (i) — periodic D-loop pairs:** **Strain-controlled** loading along **x** via **unit cell deformation**; engineering strain from **L_x**; stress from **LAMMPS stress tensor**; **16 θ orientations** with **Table S1** cell dimensions **L_x, L_y** and chiral indices **(n,m)**; **W > w** width scaling rule for wider pairs; initial **θ** grid chosen so **initial cell dimension** drift is **< 2%** despite **graphene anisotropy** (SI text).
- **Configuration (ii) — single D-loop:** **Non-periodic** (free-standing) sheet with **edge “handles”** constrained in-plane; **stress-controlled** ramped opposing forces; fracture stress from **force–distance** slope breaks.
- **Length contraction:** **N-terminated** nanoribbons of length **150** graphene unit cells; widths **w–5w**; **Langevin** thermostat heating; segment-resolved **end-to-end** vectors used in Eq. (SI.2–SI.3) style analysis; **Figure S1** reports **contraction %** vs **T** up to **1500 K** with **linear** **K·T** fit for the plotted regime.

**Ensemble / controls (SI):** Heating and contraction segments use **NVT**-style **Langevin** **thermostat** control as written in the **SI** text. **Time step** (**fs**) and total heated **duration** in **ps**/**ns** for each width series: **N/A — not copied** from the **SI** into this wiki page—read **`papers/ReaxFF_others/Gupta_D_Loops_AdvMat_SupportingInfo.pdf`**. **Barostat / hydrostatic pressure:** **N/A — not used** for these **NVT** heating sweeps.

## Findings

- SI tables tie **crystallographic orientation** of D-loop pairs to **simulation cell** vectors used in strength statistics.
- **Length-contraction** curves vs **temperature** show **width-dependent** contraction amplitudes, supporting the main text’s link between **carbonization** heating and **misfusion** defect formation.
- **Figure S1b** indicates differences in **contraction** between ribbon widths can reach **~3%** at the **highest** temperatures shown, underscoring **finite-width** effects on **thermomechanical** response in the **SI** model.
- **Table S1** lists representative **chiral indices** **(n,m)** and **L_x, L_y** for each **θ** used in **periodic D-loop** studies, enabling readers to map **simulation boxes** to **graphene** **orientations** (SI PDF).

## Limitations

Corpus holds **SI only**; interpret **scientific claims** together with the **primary article** wiki page [[2016gupta-venue-paper]].

## Relevance to group

Mechanical **protocol details** for **ReaxFF/LAMMPS** D-loop models—useful for reproducibility notes when comparing to other **graphene** fracture studies.

## Citations and evidence anchors

- Parent article DOI: [10.1002/adma.201603009](https://doi.org/10.1002/adma.201603009).

## Related topics

- [[2016gupta-venue-paper]]
- [[reaxff-family]]
