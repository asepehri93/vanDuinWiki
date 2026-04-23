---
id: paper:2013yue-venue-jp406360u
type: paper
title: "Tribochemistry of phosphoric acid sheared between quartz surfaces: A reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:lammps
  - keyword:silica-silicate
  - keyword:reactive-md
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - domain:reactive-md
  - material:oxide
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp406360u"
year: 2013
authors:
  - "Da-Chuan Yue"
  - "Tian-Bao Ma"
  - "Yuan-Zhong Hu"
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
  - "Hui Wang"
  - "Jianbin Luo"
venue: "J. Phys. Chem. C"
pdf_sha256: "ab97b77378ac06d1eb14d9a50d461735a759925666ead94223887f8b15b4c6f1"
pdf_path: "papers/Yue_Ma_Yeon_JPCC_tribochemistry_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013yue-venue-jp406360u -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. For friction coefficients, temperature ranges, and reaction details, use the peer-reviewed PDF.

## Summary

**ReaxFF** simulations are reported for **tribochemistry** in a **silica / phosphoric acid** sliding contact. The **coefficient of friction** is described as **strongly correlated** with the **number of interfacial hydrogen bonds**, so that a **weaker H-bond network** aligns with **lower friction**. Two temperature regimes are discussed: at **moderate** temperatures (**300–600 K**), friction decreases mainly through **thermal activation** of motion and **weakening** of the H-bond network **without** new tribochemical chemistry; at **higher** temperatures (**800–1400 K**), **tribochemical reactions** produce **polymerized / clustered** phosphoric species and **water** near the interface, enabling a **very low friction** state (reported friction coefficient **~0.02** in the abstract).

## Methods

- **Force field:** **ReaxFF** with **Si/O/H/P** parameters merged from **bulk silica** and **phosphoric acid** training sets and **refined against DFT** for interfacial interactions (as described in the Methods section).
- **Model:** **Hydroxyl-terminated α-quartz (101̄0)** slabs (**~29.46 Å × 21.608 Å × 8.504 Å** each); **44 orthophosphoric acid** molecules fill the gap; the interface is **pre-relaxed at 300 K** to remove bad contacts before sliding.
- **MD protocol (LAMMPS):** **Velocity-Verlet** integration with **Δt = 0.25 fs**; **normal pressure 600 MPa** on the upper slab (**−z**); the **top rigid layer** slides at **100 m/s (1 Å/ps)** along **+x** while the **bottom rigid layer stays frozen**; **Langevin** thermostats (damping **100 fs**) act on the **two layers adjacent** to the rigid plates; **PBC** in plane.
- **Temperature schedule:** Eight runs ramp from **300 K** to target temperatures **300, 400, 500, 600, 800, 1000, 1200, and 1400 K** to span **thermally activated friction** versus **tribochemical** regimes.
- **Ensemble / pressure coupling:** **NVT-like** **constant-temperature** control via **Langevin** on the **thermostated layers** together with **imposed normal stress** (**600 MPa**, **−z**) on the stack; this is **not** a textbook **isotropic NPT** barostat on the entire cell—**hydrostatic NPT** is **N/A —** not the stated protocol.

## Findings

**Outcomes & mechanisms.** The **cumulative friction coefficient μ** correlates **positively** with the **number of interfacial hydrogen bonds**; weaker H-bond networks align with **lower μ**. For **300 K ≤ T ≤ 600 K**, **no tribochemical reaction** is reported; friction falls mainly because **molecular motion accelerates** and the **H-bond network weakens** thermally. For **800 K ≤ T ≤ 1400 K**, **tribochemistry** **polymerizes/clusterizes** phosphoric species and generates **interfacial water**, enabling an **ultralow-friction** branch with **μ ≈ 0.02** in the authors’ high-temperature trajectories.

**Comparisons.** The paper emphasizes **correlation** of **μ** with **interfacial hydrogen-bond counts** rather than a single **Arrhenius** picture across both regimes.

**Sensitivity & design levers.** **Friction** and **chemistry** shift strongly with **temperature** across the **300–1400 K** schedule and with whether **tribochemical** products appear.

**Limitations & outlook.** Idealized **flat quartz**–**acid** contact and high-**T** chemistry; **experimental** superlubricity systems include **roughness** and **additives** not fully represented (**## Limitations**).

**Corpus honesty.** **Production** times in **ps/ns** per stage are **not** duplicated here; read **`pdf_path`** for exact run lengths beyond this summary.

## Limitations

- **Idealized** quartz–acid interface and **high-temperature** conditions for chemistry; **experimental** superlubricity systems include **broader** chemistry and **roughness** not fully represented.

## Relevance to group

**Adri C. T. van Duin** (Penn State) coauthors; exemplifies **ReaxFF** for **oxide–acid tribology** and **interfacial H-bond** control.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jp406360u` (`papers/Yue_Ma_Yeon_JPCC_tribochemistry_2013.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
