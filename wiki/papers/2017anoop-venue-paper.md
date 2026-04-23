---
id: paper:2017anoop-venue-paper
type: paper
title: "Irradiation-driven amorphous-to-glassy transition in quartz: The crucial role of the medium-range order in crystallization"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:silica-silicate
  - keyword:lammps
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevMaterials.1.053405"
year: 2017
authors:
  - "N. M. Anoop Krishnan"
  - "Bu Wang"
  - "Yann Le Pape"
  - "Gaurav Sant"
  - "Mathieu Bauchy"
venue: "Phys. Rev. Mater."
pdf_sha256: "41cdeb1003652383b30855d25f9420d65f9e59e6c161e5b626cb792592b08418"
pdf_path: "papers/ReaxFF_others/Anoop_Bauchy_Amorphous-Glassy-Transition2017.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2017anoop-venue-paper -->

## Summary

**Reactive molecular dynamics** simulations of **neutron-like irradiation damage** in **α-quartz** show a disordering pathway where an **amorphous-to-glassy (ATG) transition** emerges once **medium-range order (MRO)** defects appear that **kinetically block crystallization** upon heating. The work ties the Gupta-style distinction between **glassy** and **amorphous** solids to **MRO defect percolation** from short-range damage. The **silica** community context is **nuclear** waste glass and **radiation**-damaged **minerals**, where **recrystallization** propensity controls **long-term** **phase** stability.

## Methods

**RMD (LAMMPS).** **§II.A** describes **reactive molecular dynamics** cascades in **α-quartz** with the **SiO₂** reactive model referenced in the article (`papers/ReaxFF_others/Anoop_Bauchy_Amorphous-Glassy-Transition2017.pdf`). Each **primary knock-on atom (PKA)** receives **600 eV** along a random direction, with **Si** vs **O** PKA selection weighted by **neutron cross sections**. Around each impact, a spherical **NVE** core hosts the ballistic cascade for **~15 ps** while outer atoms remain at **300 K** with a **Nosé–Hoover thermostat**; a **variable timestep** handles the violent phase, reverting to **0.5 fs** otherwise. The cell then relaxes **~5 ps** in **NPT** at **300 K** and **zero pressure** (**~20 ps** total per PKA in the excerpt). Impacts repeat until **enthalpy** and **density** saturate. **Supercell lattice vectors**, **total atom count**, **explicit PBC** description, **NPT barostat** family, **electric fields**, and **enhanced sampling** are **not** restated in the **§II.A** excerpt mirrored here—confirm in **`pdf_path`** for reproduction.

**Force-field training:** **N/A —** the study **applies** a published **SiO₂** **ReaxFF** parameterization cited in the article rather than reporting a new fit.

**Static QM / DFT:** **N/A —** not a DFT discovery paper; **QM** enters through the **ReaxFF** training literature.

## Findings

**Low** deposited-energy tracks yield **disordered quartz** that can **recrystallize** on heating (with a **first-order** melt signature in the authors’ Gupta-style framing), whereas **high** deposited-energy tracks cross an **amorphous-to-glassy** threshold once **medium-range order (MRO)** defects **percolate**, **kinetically blocking** **crystallization**. The narrative is tied to prior **irradiated silica** literature (**Introduction** references) without reproducing benchmark tables here. **Sensitivity** centers on **dose** (deposited energy) because **MRO** similarity to **α-quartz** sets **crystallization** propensity. **MD flux** and **PKA** energies do not map one-to-one to reactor spectra; **O** diffusion between cascades and **ReaxFF** barrier fidelity remain **model-dependent** caveats unless revalidated with **QM**.

## Limitations

The on-disk extract is **partial** (early sections only); **ring statistics**, longer **annealing** segments, and full parameter tables are in the **full PDF** (`extraction_quality: partial` in front matter). **Cumulative** **damage** from **many** **PKA** events can alter **thermal** **spike** **overlap** statistics; the **stopping** **criterion** based on **enthalpy**/**density** **saturation** should be read in the **full** **methods** when comparing to other **irradiation** **codes**. **MRO** **metrics** are sensitive to **cooling** **rates** after **cascades**; align **annealing** **segments** with the **published** **protocol** before comparing **ATG** **thresholds** across **studies**.

## Relevance to group

Benchmark irradiation **RMD** methodology for **silica** in the PARISlab line of work (UCLA).

## Citations and evidence anchors

- DOI: `10.1103/PhysRevMaterials.1.053405`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
