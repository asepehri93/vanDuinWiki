---
id: paper:2013castro-marcano-combustion-a-comparison-thermal
type: paper
title: "Comparison of thermal and catalytic cracking of 1-heptene from ReaxFF reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:lammps
  - keyword:berendsen-thermostat
  - keyword:oxide-surface
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.combustflame.2012.12.007"
year: 2013
authors:
  - "Castro-Marcano, Fidel"
  - "van Duin, Adri C. T."
venue: "Combustion and Flame"
pdf_sha256: "59ad769b94196918fff7a560de6019a0897b3c23dae89ecac3cb11525f8a19c2"
pdf_path: "papers/Castro_CombFlame_heptene_online_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013castro-marcano-combustion-a-comparison-thermal -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

**ReaxFF** reactive MD is used to compare **thermal** versus **catalytic** initiation pathways for **1-heptene** cracking on **amorphous silica**, **hydrated silica**, and **aluminosilicate** nanoparticle interfaces at **1750–1950 K** in large (~2250-atom-class) interface models with **100** heptene molecules. Cracking is described as a **complex network** producing **H₂** and a distribution of saturated/unsaturated fragments, qualitatively consistent with experiment-oriented expectations for high-temperature hydrocarbon chemistry. Trajectory analysis contrasts initiation motifs: **thermal** cracking is described as proceeding mainly via **C–C scission** followed by **radical** propagation, whereas **catalytic** pathways emphasize **C–C scission** together with **protonation/dehydrogenation**-like events at the oxide surface.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with the **ReaxFF** reactive formalism and the **C/H/O** parameterization cited in the article (**Chenoweth**-type **hydrocarbon**/**silica** training line as referenced there). **System size & composition:** **~45 Å** cubic **supercells** at **0.2–0.3 g/cm³** with **100** **1-heptene** molecules plus an **amorphous silica**, **hydrated amorphous silica**, or **amorphous aluminosilicate** nanoparticle (**~2250 atoms** total per the abstract and `normalized/extracts/2013castro-marcano-combustion-a-comparison-thermal_p1-2.txt`). **Boundaries / periodicity:** **three-dimensional periodic boundary conditions** on the cubic cell (condensed-phase interface setup consistent with the published protocol). **Ensemble:** **NVT** high-temperature production after staged heating (as summarized on the sibling proof page [[2013castro-marcano-combustion-a-comparison-thermal-2]]; confirm any staging tables in **`pdf_path`**). **Timestep:** **0.25 fs** (**velocity Verlet** integration as in the article Methods). **Duration / stages:** **~5000 ps** production segments at each temperature after equilibration / heating stages described in the paper (indexed excerpt points to **5000 ps** production at **1750–1950 K**; full ramp tables in **`pdf_path`**). **Thermostat:** **Berendsen** with **τ = 100 fs** (as on the parallel author-copy page [[2013castro-venue-paper]] aligned with this DOI). **Barostat:** **N/A —** production protocol is **constant-volume** **NVT** reactive **MD** without **Parrinello–Rahman** pressure coupling. **Temperature:** **1750 K**, **1850 K**, and **1950 K** production windows. **Pressure:** **N/A —** no **GPa**/**bar** hydrostatic target in the **NVT** production legs summarized here (the **Introduction** motivates **~4–7 MPa** **supercritical** engine fluid pressures as physical context, distinct from the MD barostat coupling). **Electric field:** **N/A —** no applied field in the protocol described. **Replica / enhanced sampling:** **N/A —** no umbrella, metadynamics, or replica exchange reported.

**2 — Force-field training.** **N/A —** application of a published **ReaxFF** parameter set; parameter derivation is not the focus.

**3 — Static QM / DFT.** **N/A —** not a **DFT**-centric study in the sense of AGENTS block **3** (reactive **MD** is the computational engine).

## Findings

- **Cracking** of **1-heptene** proceeds through a **dense reaction network** that yields **H₂** and a broad distribution of **saturated and unsaturated** **C₁–C₇** hydrocarbon fragments, qualitatively consistent with high-temperature cracking expectations discussed in the article.
- **Thermal** initiation is described as dominated by **C–C scission** followed by **radical** propagation, whereas **catalytic** channels on the **oxide** surfaces emphasize **C–C scission** together with **protonation**/**dehydrogenation**-like events involving surface **H** (see mechanistic subsection and pathway tables in the paper).
- The study positions **ReaxFF** as a tractable tool to interrogate **atomistic initiation chemistry** for **hydrocarbon** **cracking** on **oxide** interfaces at **1750–1950 K**, acknowledging limitations in quantitative agreement with experiment for full product distributions.

## Limitations

- Elevated temperatures, finite simulation times, and empirical reactive parameters limit quantitative agreement with experimentally measured product distributions and rates.

## Relevance to group

Direct **van Duin** co-authorship on **aviation-fuel relevant** cracking chemistry using **ReaxFF**.

## Citations and evidence anchors

- Abstract and Sec. 1: problem framing; methods/results for temperature sets and system composition (Combust. Flame; DOI above).

## Reader notes (navigation)

- Elsevier **author proof** PDF: [[2013castro-marcano-combustion-a-comparison-thermal-2]]; **author personal copy** PDF: [[2013castro-venue-paper]].

## Related topics

- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
