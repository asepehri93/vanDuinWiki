---
id: paper:2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g
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
candidate_tags: []
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:batteries-interfaces
source_refs: []
doi: "10.1080/08927022.2019.1646911"
year: 2019
authors:
  - "Karthik Ganeshan"
  - "Md. Jamil Hossain"
  - "Adri C. T. van Duin"
venue: "Molecular Simulation (author proof PDF)"
pdf_sha256: "0d9d42c48feec2fbb028914790b772aa8019c594f8dc3b35ac6ea8a97c8e180c"
pdf_path: "papers/Ganeshan_Hossain_MolSym_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g -->

## Summary

Reactive molecular dynamics with **ReaxFF** can follow bond-breaking chemistry, but rare reactive events often demand **enhanced sampling** or **parallelism** to reach laboratory time scales. This **Taylor & Francis** **author-proof** PDF carries the same **scientific** **text** as the **version** **of** **record** *Molecular Simulation* article (**DOI** **10.1080/08927022.2019.1646911**): **Ganeshan**, **Hossain**, and **van Duin** combine **collective-variable hyperdynamics** (**CVHD**) with **parallel replica dynamics** (**PRD**) so **ReaxFF** **LAMMPS** jobs can **stack** two **orthogonal** **accelerators**—**biased** **dynamics** plus **replica**-level **parallelism**—and **report** **measured** **speedups** on **n-dodecane** **pyrolysis** and an **ethylene** **carbonate**/**Li** electrolyte **stand-in**. This **Molecular Simulation** article (ingested here as a **Taylor & Francis author proof** PDF) combines **parallel replica dynamics (PRD)** with **collective-variable hyperdynamics (CVHD)** to stack accelerations for **ReaxFF MD**. The benchmarks include **n-dodecane pyrolysis** and an **ethylene carbonate / lithium** system intended as a stand-in for a **highly reactive electrolyte** environment. **Adri C. T. van Duin** is a coauthor, marking the work as part of the group’s methods portfolio for long-timescale reactive simulations. Substantive scientific content is duplicated with **`[[2019ganeshan-molecular-si-multiply-accelerated]]`**; prefer the **journal** PDF for authoritative pagination and final figure resolution.

## Methods

### ReaxFF, CVHD, and PRD (A/B)

**CVHD** + **PRD** with **ReaxFF** in **LAMMPS**-class workflows; **GPU** context and **collective-variable** definitions per benchmark appear in the **published** article—**not** inferred from the proof filename. **Full** parameter sets: **[[2019ganeshan-molecular-si-multiply-accelerated]]** / **[[2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g-2]]** (detailed proof variant).

The **benchmark** suite contrasts **long-chain** **n-dodecane** **pyrolysis**, where **parallel** **replicas** materially help **first-passage** sampling, against **EC/Li** **electrolyte**-like chemistry where **CVHD** already accelerates **bond** **rearrangements** enough that **PRD** adds **little** incremental speedup—an explicit **diminishing-returns** lesson for **stacked** **enhanced-sampling** pipelines.

### Corpus note (D)

**Author proof** PDF—cite **VOR** DOI for stable pagination.

**Reactive MD integration.** Production **molecular dynamics** uses **LAMMPS** / **PuReMD** with **ReaxFF** bond-order updates on **periodic** cubic **cells** (**50 Å** side for **n-dodecane** benchmarks) containing **24** molecules (order **10³ atoms** total). **Temperature:** **1200 K** and **1500 K** **thermal** setpoints as reported. **Timestep:** sub-**femtosecond** **timestep** values appropriate to **ReaxFF** stability are quoted in the article’s **Computational Methods** (see `pdf_path`). **Duration:** **CVHD** bias deposits on **0.2 ps** intervals with **1 ps** event waits; **PRD** uses **t_corr = 10 ps** and **t_dephase = 5 ps** as stated above. **Ensemble:** **NVT**-style **thermal** control during biased production (details in article). **Thermostat:** specified with the **CVHD** implementation in **Molecular Simulation** (see **PDF**). **Barostat / pressure:** **N/A** — constant-volume **supercells** without **GPa** **pressure** coupling in the summarized benchmarks. **External electric field:** **N/A**. **Enhanced sampling:** **parallel replica dynamics** plus **collective-variable hyperdynamics** are the core **accelerated dynamics** workflow. **Corpus note:** **author proof** PDF—prefer the **VOR** DOI landing page for pagination.

## Findings

### Mechanisms

**PRD + CVHD** speeds **n-dodecane** vs **CVHD** alone when **replicas** help **first-passage** statistics; **EC/Li** shows **diminishing** **PRD** benefit when **CVHD** already dominates rates.

**Interpretation:** The **benchmark** section already shows **diminishing** **returns** when **CVHD** **dominates** **rates** (notably **EC/Li**), so **PRD** **speedups** are **system-dependent**—read the **journal** **tables** before assuming **linear** **scaling** from **replica** **count**.

### Limitations / outlook

**Hardware**, **CV** quality, and **system size** affect measured speedups; keep **proof** vs **VOR** provenance in citations.

## Limitations

**Author proof** PDFs can differ slightly from the final XML layout; **hyperdynamics** validity depends on collective-variable choices and transition-state assumptions.

## Reader notes (MAS / retrieval)

Prefer **`[[2019ganeshan-molecular-si-multiply-accelerated]]`** for clean PDF pagination when quoting long passages.

## Relevance to group

**van Duin-group** methods contribution for **accelerated ReaxFF**; proof ingested for corpus completeness alongside cleaner PDF variants.

## Citations and evidence anchors

- [10.1080/08927022.2019.1646911](https://doi.org/10.1080/08927022.2019.1646911)

## Reader notes (navigation)

- [[2019ganeshan-molecular-si-multiply-accelerated]]
- [[2019ganeshan-molecular-si-multiply-accelerated-2]]

## Related topics

- [[2019ganeshan-molecular-si-multiply-accelerated]]
- [[reaxff-family]]
