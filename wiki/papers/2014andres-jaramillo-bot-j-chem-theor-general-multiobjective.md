---
id: paper:2014andres-jaramillo-bot-j-chem-theor-general-multiobjective
type: paper
title: "General multiobjective force field optimization framework, with application to reactive force fields for silicon carbide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - material:alloy-bulk
  - method:reaxff
  - task:parameterization
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:method-development
source_refs: []
doi: "10.1021/ct5001044"
year: 2014
authors:
  - "Andres Jaramillo-Botero"
  - "Saber Naserifar"
  - "William A. Goddard III"
venue: "J. Chem. Theory Comput."
pdf_sha256: "2df8a6b2afbb640e8f29c2afd52000b0a2e40365fda7b734429f3dc212622f73"
pdf_path: "papers/ReaxFF_others/Jaramillo_Garfield.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014andres-jaramillo-bot-j-chem-theor-general-multiobjective -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Algorithmic detail and parameter counts belong to the article and SI.

## Summary

The paper presents **GARFfield**, a **multiobjective**, **genetic-algorithm**-centric **optimizer** for **reactive** and other **complex** force fields. It frames **ReaxFF** (and related engines) as having **large**, **nonconvex** parameter spaces and proposes **Pareto-optimal** **search** with **GA**, **hill-climbing**, and **gradient** refinements. **Demonstration** applications include a **ReaxFF** parameterization line for **SiC** **growth** chemistry from **methyltrichlorosilane**-related training scenarios and a separate **electron force field (eFF)** / **ECP** example for **nonadiabatic** problems, highlighting the **framework**’s flexibility. Readers should treat the **SiC** and **eFF** blocks as **worked examples** that illustrate **optimizer** behavior rather than as finalized **production** parameter sets for unrelated chemistries.

## Methods

### Optimization framework (GARFfield)

- **GARFfield** combines **genetic algorithms**, **hill-climbing**, and **conjugate-gradient** refinement to search **large**, **nonconvex** parameter spaces while returning **Pareto-optimal** parameter sets rather than a single weighted minimum (**Section II**).

### Objective construction

- Users specify **multiple simultaneous objectives** against **QM** references (energies, forces, and additional metrics per application) and may employ **weight randomization** to sample the **Pareto front** (**Summary**).

### Demonstration 1 — ReaxFF for SiC CVD chemistry

- A worked **ReaxFF** fit targets **silicon carbide** **growth** chemistry relevant to **methyltrichlorosilane**-class **CVD** training scenarios (**Summary**).

### Demonstration 2 — eFF + ECP for nonadiabatic problems

- A separate example applies **electron force field (eFF)** models with **effective core pseudopotentials** to **nonadiabatic** excited-state problems, showcasing **optimizer** flexibility beyond **ReaxFF** alone (**Summary**).

### Reproducibility note

- Hyperparameters, population sizes, and stopping criteria live in **JCTC** + **SI**—this wiki entry is **not** a substitute for rerunning **GARFfield** with documented settings.

**1 — MD application (atomistic dynamics).** This **JCTC** contribution centers on **GARFfield** optimization rather than tabulating a single production **molecular dynamics** protocol. For readers checking downstream **MD** reproducibility: **system size / atom counts** for any optional validation cells are **N/A — not copied here** (**see SI**). **Periodic boundary conditions (PBC)** details for those cells are **N/A — confirm in SI/PDF**. **Ensemble (NVT/NPT), timestep (fs), trajectory duration (ps/ns), thermostat family, and barostat** settings for any brief **LAMMPS** validation runs are **N/A — not restated on this wiki page** (consult the article/SI rather than inferring defaults). **Temperature (K) and hydrostatic pressure targets** for such demos are likewise **N/A — not summarized here**. **Electric field and replica-exchange / metadynamics-style enhanced sampling:** **N/A —** not part of the **GARFfield** narrative summarized above.

**2 — Force-field training.** **Parent FF / elements:** **ReaxFF** for **Si/C/H/Cl** (and related) **CVD**-relevant **SiC** chemistry in the primary demonstration; a separate example uses **eFF** with **ECP** for **nonadiabatic** problems (**Summary** / article). **QM reference:** **DFT**/**QM** objectives include **energies**, **forces**, and additional metrics configured per application (**Section II**). **Training set:** **methyltrichlorosilane**-class **SiC growth** motifs and related structures (**Summary**; full list in article/SI). **Optimization:** **GARFfield** combines **genetic algorithms**, **hill-climbing**, and **conjugate-gradient** refinement to explore **Pareto-optimal** parameter sets. **Reference data / validation:** **QM** scores along **Pareto** fronts in **JCTC** figures; treat demonstrations as **proof-of-concept** fits rather than finalized production parameter files (**Findings**).

## Findings

- The **SiC ReaxFF** and **eFF/ECP** case studies are presented primarily as **proof-of-concept fits** with **QM validation** metrics; large-scale **production MD benchmarks** are explicitly **out of scope** for the methods paper.
- The central claim is **algorithmic**: **multiobjective Pareto** search surfaces **trade-offs** (accuracy on one training objective vs another) that single-objective fits can obscure.
- From a **practitioner** standpoint, the manuscript emphasizes that **automated** search can return **families** of parameter sets; downstream **MD** studies should document **which Pareto point** was selected and **why**, because **transferability** is not guaranteed by **training-score** alone.
- **Compared to single-objective fits:** **multiobjective** **Pareto** sets expose **accuracy**/**stiffness** trade-offs that scalar weights can hide (**Summary**).
- **Sensitivity:** **objective weights**, **training-set** coverage, and **population** settings shift which **Pareto** branches appear (**## Limitations**).
- **Limitations / outlook:** **transferability** must be tested outside the **training** manifold (**## Limitations**).
- **Corpus note:** this page is a **framework** summary—**numerical** **parameters** live in **JCTC**/**SI**, not here.

## Limitations

- **Optimizer** performance depends on **training-set** design and **objective** choices; **transferability** must be tested outside **training**.
- **JCTC** methods papers can evolve **notation** and **SI** layouts across publisher versions—when automating ingestion, anchor workflows to **DOI-resolved** PDFs rather than filename-only duplicates under `papers/ReaxFF_others/`.
- Wiki summaries cannot capture every **hyperparameter** of **GARFfield** runs; reproduce optimizer settings from the **article** and **SI** when benchmarking against other **parameterization** tools.

## Relevance to group

**Parameterization culture** reference adjacent to **Penn State** **ReaxFF** workflows; useful for comparing **GA** / **multiobjective** **strategies** vs other optimizers documented in the wiki.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/ct5001044` (`papers/ReaxFF_others/Jaramillo_Garfield.pdf`).

## Related topics

- [[reaxff-family]]
- [[2019ganna-shchygol-j-chem-theor-reaxff-parameter]]
