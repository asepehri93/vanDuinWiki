---
id: paper:2024shen-construction-unveiling-intricacies-2
type: paper
title: "Unveiling the intricacies of steel corrosion induced by chloride: Insights from reactive molecular dynamics simulation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - task:application
  - domain:oxides-ceramics
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:water-interfaces
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1016/j.conbuildmat.2024.137839"
year: 2024
authors:
  - "Fangmin Shen"
  - "Minhao Li"
  - "Guojian Liu"
  - "Adri C. T. van Duin"
  - "Yunsheng Zhang"
venue: "Construction and Building Materials"
pdf_sha256: "38f321a11a7ee1ae16f004bd614b1e260de4c23a39546082ff3dff5e90b6a432"
pdf_path: "papers/Shen_steel_corrosion_Construction_Building_Materials_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024shen-construction-unveiling-intricacies-2 -->

!!! abstract "Scope"
    Reactive molecular dynamics with a **Fe/Cl-augmented ReaxFF** (trained against DFT) is used to interpret **chloride-induced corrosion** of reinforcing steel at the atomistic scale, emphasizing initiation, charge transfer, and corrosion-product formation.

## Summary

Chloride-induced corrosion of reinforcing steel in concrete is difficult to resolve experimentally at atomic resolution. Shen and colleagues develop a **reactive force field (ReaxFF) incorporating Fe/Cl chemistry** using **density functional theory (DFT)** reference data, then apply **ReaxFF molecular dynamics** in **LAMMPS** to follow **chloride-driven attack** on an **Fe(100)** surface in **alkaline aqueous electrolyte**. The introduction frames longstanding debates—whether **chloride** acts primarily as a **catalyst** versus a **direct initiator**—and argues for atomistic models that capture **electron transfer**, **oxide** formation, and **dissolution** dynamics beyond macroscopic coupon tests. This slug is a **duplicate ingest** of DOI `10.1016/j.conbuildmat.2024.137839` (alternate `pdf_path` versus [[2024shen-construction-unveiling-intricacies]]); the scientific claims are the same peer-reviewed article.

## Methods

**1 — MD application (ReaxFF, §2.3).** **Engine / code:** **LAMMPS** **molecular** **dynamics** with **ReaxFF**. **System:** **Fe(100)** in **~34.4 × 34.4 × 66.3 Å³** with **3168** **Fe**, **1160** **H₂O**, **27** **Na⁺**, **20** **Cl⁻**, **7** **OH⁻** (**pH 13.5**, **1 mol/L Cl⁻**). **Boundaries:** **PBC** in **x,y**; **fixed** **z**; **reflective** upper **wall**. **Ensemble / T:** **NVT** at **300 K** with **NVT** **thermostat** per §2.3 (see **VOR** for full coupling). **Timestep / duration:** **Δt = 0.1** **fs**; **500** **ps**; snapshots each **1000** steps; **OVITO** visualization. **Barostat, pressure, E-field, enhanced sampling:** **N/A** for the summarized **NVT** **slab** run.

**2 — Force-field training.** **Fe/Cl** **ReaxFF** refit against **B3LYP-D3(BJ)/6-311++G(2df,2p)** **cluster** and **CASTEP** **GGA-PW91** **periodic** **Fe(100)+Cl** data (see [[2024shen-construction-unveiling-intricacies]] for the same **equation**-of-state style summary).

**3 — Static QM** — **training/validation** roles only; not a stand-alone DFT **application** **report** beyond the fit.

*(Duplicate **DOI** and alternate **`pdf_path`**: prefer **[[2024shen-construction-unveiling-intricacies]]** for full **parameter** tables in one place.)*
## Findings

**Corrosion sequence.** Early dynamics show **oxide initiation** from **OH/O** interaction at the metal surface, followed by **Cl⁻** accumulation that **weakens Fe–Fe** bonding and promotes **Fe dissolution** and **vacancy** formation—consistent with a **catalytic** chloride role emphasized in the discussion. **Charge analysis** tracks **Fe oxidation**, **O reduction**, and **Cl⁻**-mediated **electron transfer** patterns across the **5–500 ps** window.

**Mechanistic detail (§3.2.2).** The paper traces **short-lived intermediates** (including **Fe(OH)⁺** formation and **Cl substitution** steps) toward **Fe(OH)₂**-like products, arguing that **Cl⁻** can remain **surface-catalytic** rather than requiring bulk **chloride** intercalation—supporting catalyst-style pictures over naive bulk chlorination.

**RDF and morphology.** **Fe–O** and **Fe–Cl** **radial distribution functions** align with literature **Fe–Cl** bond lengths near **~2.35 Å** versus **~2.32 Å** experimental averages cited in the text. **Surface roughening** and **pitting** progress through **nucleation–growth–stabilization** stages by **500 ps** in the reported trajectory analysis.

**Corpus honesty** — this duplicate **slug** mirrors the **same** **DOI**; numeric **citations** should follow **[[2024shen-construction-unveiling-intricacies]]** when the two **PDFs** **diverge**.
## Limitations

Prefer **[[2024shen-construction-unveiling-intricacies]]** for evidence-grounded numbers; this duplicate page exists for **manifest/PDF** tracking. Atomistic models omit full **concrete** **pore** transport and **long-time** **passivation** kinetics.

## Relevance to group

Co-authorship by **Adri C. T. van Duin** links the work to the group’s **ReaxFF development and corrosion-related applications**.

## Citations and evidence anchors

- DOI: [10.1016/j.conbuildmat.2024.137839](https://doi.org/10.1016/j.conbuildmat.2024.137839)

## Reader notes (navigation)

Canonical **Methods**/**Findings** with full protocol: [[2024shen-construction-unveiling-intricacies]]. Theme retrieval: [[paper-index-by-domain]].

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
