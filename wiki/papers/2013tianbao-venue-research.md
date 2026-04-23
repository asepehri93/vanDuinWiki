---
id: paper:2013tianbao-venue-research
type: paper
title: "Tribochemistry of phosphoric acid sheared between quartz surfaces: A reactive molecular dynamics study"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:silica-silicate
  - keyword:lammps
  - keyword:galley-or-proof-pdf
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:silicate-glass
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
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "cbad33f30b331d65ce36544cdb46bf44686d3290a3e9cf041112975cd1f541ad"
pdf_path: "papers/Tianbao_JPCA_phosphate_treibology_proof.galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013tianbao-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. The corpus filename references **Tianbao** and **proof/galley**; the first author on the article is **Yue**.

## Summary

**ReaxFF** sliding simulations of **phosphoric acid** confined between **quartz** surfaces probe **tribochemical** mechanisms behind low friction in this system. The **friction coefficient correlates positively** with the **number of interfacial hydrogen bonds**—weaker H-bond networks favor lower friction. Two regimes appear: for **300–600 K**, no chemistry is required; friction drops as molecular motion accelerates and H-bonds weaken. For **800–1400 K**, reactions **polymerize** phosphoric species and release **interfacial water** that lubricates, reaching **\(\mu \approx 0.02\)** in the reported conditions.

## Methods

**Force field:** **ReaxFF** with **Si/O/H/P** parameters merged from **bulk silica** and **phosphoric acid** training sets and **refined against DFT** for interfacial interactions (as described in the article).

**Model:** **Hydroxyl-terminated α-quartz (101̄0)** slabs (**~29.46 Å × 21.608 Å × 8.504 Å** each); **44 orthophosphoric acid** molecules fill the gap; the interface is **pre-relaxed at 300 K** to remove bad contacts before sliding.

**MD protocol (LAMMPS):** **Velocity-Verlet** integration with **\(\Delta t = 0.25\) fs**; **normal pressure 600 MPa** on the upper slab (**−z**); the **top rigid layer** slides at **100 m/s (1 Å/ps)** along **+x** while the **bottom rigid layer stays frozen**; **Langevin** thermostats (damping **100 fs**) act on the **two layers adjacent** to the rigid plates; **PBC** in plane.

**Temperature schedule:** Eight runs ramp from **300 K** to target temperatures **300, 400, 500, 600, 800, 1000, 1200, and 1400 K** to span **thermally activated friction** versus **tribochemical** regimes. The peer-reviewed PDF for the same article is on [[2013yue-venue-jp406360u]] (`papers/Yue_Ma_Yeon_JPCC_tribochemistry_2013.pdf`). Corpus proof/galley PDF: `papers/Tianbao_JPCA_phosphate_treibology_proof.galley.pdf` (first author on the article is **Yue**).

**Barostat / pressure control:** the protocol applies a **target normal stress** (**600 MPa** along **−z**) via the rigid-plate setup described above rather than a textbook **isotropic NPT** barostat on the full supercell (**Methods** narrative as curated from the article text on [[2013yue-venue-jp406360u]]). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used. **Total trajectory length per condition:** **N/A —** confirm in the **J. Phys. Chem. C** PDF if operators need exact **ps/ns** production times beyond this galley-oriented wiki layer.

## Findings

The **cumulative friction coefficient \(\mu\)** correlates **positively** with the **number of interfacial hydrogen bonds**; weaker H-bond networks align with **lower \(\mu\)**. For **300 K ≤ T ≤ 600 K**, **no tribochemical reaction** is reported; friction falls mainly because **molecular motion accelerates** and the **H-bond network weakens** thermally. For **800 K ≤ T ≤ 1400 K**, **tribochemistry** **polymerizes/clusterizes** phosphoric species and generates **interfacial water**, enabling an **ultralow-friction** branch with **\(\mu \approx 0.02\)** in the authors’ high-temperature trajectories.

**Comparisons & sensitivity.** Trends are organized primarily vs **temperature** across the **eight** target states and vs **interfacial H-bond** statistics as summarized above; comparisons to experiment or broader tribology literature, if any, belong to the **Discussion** in the **VOR** PDF.

**Limitations & outlook.** Idealized **flat quartz**–**acid** contact and high-**T** chemistry limits are noted under **## Limitations**; galley/proof PDFs may differ slightly from final pagination.

**Corpus honesty.** This slug uses a **proof/galley** filename; use **`paper:2013yue-venue-jp406360u`** for the **version-of-record** PDF path when citing canonical layout.

## Limitations

Ideal crystalline quartz vs amorphous silica in experiments; proof PDF may differ from final layout.

## Relevance to group

Demonstrates **ReaxFF tribochemistry** on **oxide–acid** interfaces with van Duin parametrization support.

## Citations and evidence anchors

- DOI: [10.1021/jp406360u](https://doi.org/10.1021/jp406360u)
- Extract: `normalized/extracts/2013tianbao-venue-research_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Superlubricity and phosphate-based tribofilms
