---
id: paper:2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g-2
type: paper
title: "Multiply accelerated ReaxFF molecular dynamics: coupling parallel replica dynamics with collective variable hyperdynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reactive-md
  - method:reaxff
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:method-development
  - keyword:gpu-md
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1080/08927022.2019.1646911"
year: 2019
authors:
  - "Karthik Ganeshan"
  - "Md. Jamil Hossain"
  - "Adri C. T. van Duin"
venue: "Molecular Simulation"
pdf_sha256: "18770bc1d0dd5a3aa57c3fb53a17792ebd9b757c4f51af152690146e02b4a1d4"
pdf_path: "papers/Ganeshan_Hossain_MolSym_2019_proof_v2.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019ganeshan-venue-eg2-pdf-author-tandf201907230943247415-g-2 -->

!!! abstract "Scope"
  Proof-stage PDF in the corpus. The methods below follow the article text on combining **parallel replica dynamics (PRD)** with **collective-variable hyperdynamics (CVHD)** in a ReaxFF setting, with application benchmarks on n-dodecane pyrolysis and a more reactive ethylene carbonate/Li example.

## Summary

The work reviews and implements **PRD + CVHD** within reactive ReaxFF molecular dynamics to reach longer effective times for rare chemical events. **PRD** accelerates escape from a potential basin by running multiple independent replicas and summing their simulated time; **CVHD** applies a history-dependent bias on collective variables to lower barriers. The authors compare **standard MD, CVHD, PRD, and PRD + CVHD** for **n-dodecane pyrolysis** (ReaxFF C/H/O parameters of Chenoweth et al.) and discuss a second case (**ethylene carbonate/Li**), where CVHD strongly accelerates reactions so that adding PRD yields less extra benefit.

## Methods

### Theory: PRD, CVHD, and combination (A/B)

**Section 2** defines **PRD** (replica workflow, dephasing, correlation time \(t_\mathrm{corr}\), event detection) and **CVHD** (collective variables, global distortion, bias deposition). **Section 2.3** derives **PRD + CVHD**; **PRD** acceleration scales **inversely** with **transition rate**, so when **CVHD** already raises rates sharply, **PRD** adds less marginal gain.

### n-Dodecane pyrolysis benchmark (B)

**24** **n-dodecane** molecules, **50 Å** cube, **0.054 kg dm⁻³**, **1200 K** and **1500 K**. **CVHD** (**Bal and Neyts**): Gaussian height **0.25 kcal mol⁻¹**, half-width **0.025**, deposit every **0.2 ps**, **1 ps** event wait; **ReaxFF C/H/O** (**Chenoweth et al.**); **bond-order cutoff 0.3** for intact dodecane. **PRD**: **t_corr = 10 ps**, **t_dephase = 5 ps**; **bash** replica control; primary reaction example **C₄H₉ + C₈H₁₇** (Fig. 3).

### Ethylene carbonate / Li (B)

Second benchmark where **CVHD** already drives very fast chemistry—**PRD** benefit **small** (details in article).

### Corpus / citation note (D)

**Proof** PDF—prefer **version-of-record** DOI for pagination.

**Reactive MD integration.** Production **molecular dynamics** uses **LAMMPS** / **PuReMD** with **ReaxFF** bond-order updates on **periodic** cubic **cells** (**50 Å** side for **n-dodecane** benchmarks) containing **24** molecules (order **10³ atoms** total). **Temperature:** **1200 K** and **1500 K** **thermal** setpoints as reported. **Timestep:** sub-**femtosecond** **timestep** values appropriate to **ReaxFF** stability are quoted in the article’s **Computational Methods** (see `pdf_path`). **Duration:** **CVHD** bias deposits on **0.2 ps** intervals with **1 ps** event waits; **PRD** uses **t_corr = 10 ps** and **t_dephase = 5 ps** as stated above. **Ensemble:** **NVT**-style **thermal** control during biased production (details in article). **Thermostat:** specified with the **CVHD** implementation in **Molecular Simulation** (see **PDF**). **Barostat / pressure:** **N/A** — constant-volume **supercells** without **GPa** **pressure** coupling in the summarized benchmarks. **External electric field:** **N/A**. **Enhanced sampling:** **parallel replica dynamics** plus **collective-variable hyperdynamics** are the core **accelerated dynamics** workflow. **Corpus note:** second **proof** PDF variant in the corpus; same science as [[2019ganeshan-molecular-si-multiply-accelerated]].

## Findings

### Comparisons, sensitivity, and limitations

**Comparisons:** stacked **PRD + CVHD** wall-clock gains are contrasted with **CVHD-only** and **plain MD** baselines in the **Molecular Simulation** tables (see **journal** PDF for exact factors). **Sensitivity:** **PRD** benefit drops when **CVHD** already raises **reaction** rates (**ethylene carbonate/Li** vs **n-dodecane**), illustrating **temperature**- and chemistry-dependent accelerator **efficiency**. **Limitations / outlook:** **hyperdynamics** bias alters **kinetics**; **PRD** assumes approximately **memoryless** first-passage statistics—authors discuss when **secondary** **reactions** fall outside the **PRD** event detector. **Corpus honesty:** this note tracks a **proof** `pdf_path`; cite the **DOI** **version-of-record** on [[2019ganeshan-molecular-si-multiply-accelerated]] for authoritative figure pagination.

### Mechanisms (accelerator interplay)

**PRD + CVHD** can beat **CVHD** alone in **wall-clock** for **n-dodecane** by harvesting **rare** primary events. When **CVHD** dominates rates, **PRD** adds **little**—consistent with **inverse** **PRD** scaling. **EC/Li** shows the same **trade-off** at higher intrinsic reactivity.


## Limitations

**Hyperdynamics** bias alters **kinetics**; **PRD** assumes approximately **memoryless** transitions. Secondary reactions and **PRD** event-check targeting: **PRD** acceleration for follow-on chemistry can drop if secondary events are excluded from the **PRD** check while **CVHD** continues—see article. Parallel narrative with **journal** PDF: **[[2019ganeshan-molecular-si-multiply-accelerated]]**.

## Relevance to group

Develops **accelerated reactive MD** methodology in the **ReaxFF** ecosystem with **van Duin** affiliation; connects to **combustion/pyrolysis** and **battery electrolyte**-motivated chemistry.

## Citations and evidence anchors

- Full text: `papers/Ganeshan_Hossain_MolSym_2019_proof_v2.pdf`.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
