---
id: paper:2019ganeshan-molecular-si-multiply-accelerated-2
type: paper
title: "Multiply accelerated ReaxFF molecular dynamics: coupling parallel replica dynamics with collective variable hyper dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:fuel-combustion
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:enhanced-sampling
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:lammps
source_refs: []
doi: "10.1080/08927022.2019.1646911"
year: 2019
authors:
  - "Karthik Ganeshan"
  - "Md. Jamil Hossain"
  - "Adri C. T. van Duin"
venue: "Molecular Simulation (2019) NSF report PDF"
pdf_sha256: "f6353cef6f20713a88d58fc445be2e5ac5f963eeebca6d8874b3cf5ad40b94f6"
pdf_path: "papers/Ganeshan_Hossain_MolSym_2019_forNSF.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019ganeshan-molecular-si-multiply-accelerated-2 -->

## Summary

**Rare-event** **reactive** simulations of **pyrolysis** and **electrolyte** decomposition often require **enhanced sampling** because **bond-breaking** events are **infrequent** on **nanosecond** scales accessible to brute-force **MD**. The **published** **Molecular Simulation** article therefore **stacks** **collective-variable hyperdynamics** with **parallel replica dynamics** on top of **GPU-accelerated** **ReaxFF** in **LAMMPS**, reporting **effective** **speedups** relative to **plain** **MD** and **CVHD-only** **runs** for **hydrocarbon** and **battery-relevant** benchmarks. **`papers/Ganeshan_Hossain_MolSym_2019_forNSF.pdf`** is an **NSF-reporting** PDF export of the *Molecular Simulation* article (DOI `10.1080/08927022.2019.1646911`) on **stacking** **collective-variable hyperdynamics (CVHD)** with **parallel replica dynamics (PRD)** for **ReaxFF** simulations. The scientific content matches **`[[2019ganeshan-molecular-si-multiply-accelerated]]`** (journal PDF) and the **author proof** variant **`[[2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g]]`**. Case studies include **n-dodecane pyrolysis** and **ethylene carbonate / lithium** chemistry relevant to **batteries** and **thermal decomposition** kinetics.

## Methods

### Canonical protocols (A/B)

**PRD + CVHD** with **ReaxFF** (**LAMMPS**/**PuReMD** workflow), **n-dodecane** and **EC/Li** benchmarks, **acceleration factors** vs **plain MD**/**CVHD-only**—full **collective-variable**, **replica**, and **timestep** tables: **[[2019ganeshan-molecular-si-multiply-accelerated]]** (journal PDF). This **NSF** export matches science; **pagination** may differ.

**CVHD** biases **bond-order** **dynamics** using a **collective variable** tied to **reaction** progress so that **rare** **pyrolysis** or **electrolyte** **decomposition** steps are visited more often than in **brute-force** **MD**. **PRD** runs **independent** **replicas** of the **biased** dynamics to harvest **first-passage** **times** for the same **rare** event, then **combines** **statistics**—stacking both methods targets **wall-clock** gains when **either** accelerator alone is insufficient.

### DFT (C)

**Not applicable**—method paper for **accelerated** **ReaxFF** **MD**.

**Reactive MD integration.** Production **molecular dynamics** uses **LAMMPS** / **PuReMD** with **ReaxFF** bond-order updates on **periodic** cubic **cells** (**50 Å** side for **n-dodecane** benchmarks) containing **24** molecules (order **10³ atoms** total). **Temperature:** **1200 K** and **1500 K** **thermal** setpoints as reported. **Timestep:** sub-**femtosecond** **timestep** values appropriate to **ReaxFF** stability are quoted in the article’s **Computational Methods** (see `pdf_path`). **Duration:** **CVHD** bias deposits on **0.2 ps** intervals with **1 ps** event waits; **PRD** uses **t_corr = 10 ps** and **t_dephase = 5 ps** as stated above. **Ensemble:** **NVT**-style **thermal** control during biased production (details in article). **Thermostat:** specified with the **CVHD** implementation in **Molecular Simulation** (see **PDF**). **Barostat / pressure:** **N/A** — constant-volume **supercells** without **GPa** **pressure** coupling in the summarized benchmarks. **External electric field:** **N/A**. **Enhanced sampling:** **parallel replica dynamics** plus **collective-variable hyperdynamics** are the core **accelerated dynamics** workflow. **Corpus note:** this **NSF** PDF export mirrors the journal article; cite [[2019ganeshan-molecular-si-multiply-accelerated]] for canonical pagination.

## Findings

### Mechanisms, limitations, outlook

**PRD** on **CVHD** helps **n-dodecane**; **EC/Li** is already **fast** under **CVHD**, so **PRD** adds **little**—**diminishing returns** when stacking accelerators. Prefer **[[2019ganeshan-molecular-si-multiply-accelerated]]** for figure locators.

**Takeaway:** **Wall-clock** gains depend on **how** **tight** the **CVHD** **bias** is—when **CVHD** already **dominates** **first** **bond** **events**, **extra** **replicas** mainly **duplicate** **work**; when **CVHD** is **weak**, **PRD** **statistics** recover **meaningful** **parallelism** across **independent** **trajectories** seeded from the **same** **initial** **state**.

## Limitations

Users reproducing **acceleration factors** must reproduce **CVHD** **bias** **parameters** and **PRD** **replica** **exchange** rules exactly as in the **journal** **Methods**; otherwise **reported speedups** are not meaningful. **NSF** formatting may differ from **Taylor & Francis** layout. **Hyperdynamics** biases require **careful validation** (reweighting, barrier estimates). This slug is **provenance** for a specific **pdf_sha256**; cite **`[[2019ganeshan-molecular-si-multiply-accelerated]]`** for **bibliography** unless the NSF file itself must be referenced.

**Confidence rationale:** `med`—duplicate collateral PDF; science aligned with canonical journal page.

## Citations and evidence anchors

**Taylor & Francis** hosts *Molecular Simulation* content under the DOI below; use the publisher landing page for **volume**, **issue**, and **page** numbers when exporting **BibTeX**. [10.1080/08927022.2019.1646911](https://doi.org/10.1080/08927022.2019.1646911)

## Reader notes (navigation)

**NSF** **reports** sometimes circulate with **different** **figure** compression; if **image** **OCR** differs between PDFs, trust **equations** and **tables** in the **journal** **PDF** for **numerical** **benchmarks**.

- **Canonical article:** [[2019ganeshan-molecular-si-multiply-accelerated]]
- Author proof: [[2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g]]
- [[theme-reactive-md-corpus]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2019ganeshan-molecular-si-multiply-accelerated]]
- [[reaxff-family]]
