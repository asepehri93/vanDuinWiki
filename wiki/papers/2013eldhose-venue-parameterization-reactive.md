---
id: paper:2013eldhose-venue-parameterization-reactive
type: paper
title: "Parameterization of a reactive force field using a Monte Carlo algorithm"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:monte-carlo-sampling
  - keyword:qm-training-data
source_refs: []
doi: "10.1002/jcc.23246"
year: 2013
authors:
  - "Iype, E."
  - "Hütter, M."
  - "Jansen, A. P. J."
  - "Nedea, S. V."
  - "Rindt, C. C. M."
venue: "Journal of Computational Chemistry"
pdf_sha256: "add125b92cacaea144d82c2d1defde217828006e930caae472085425028c959c"
pdf_path: "papers/ReaxFF_others/Eldhose_Nedea_JCC_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013eldhose-venue-parameterization-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

The paper replaces **single-parameter** optimization for **ReaxFF** with a **Metropolis Monte Carlo** search combined with **simulated annealing** to explore **high-dimensional** parameter spaces. The approach is demonstrated by fitting to **QM reference data** for **MgSO₄ hydrates**, reproducing targeted **structures**, **equations of state**, and **water binding** trends. A **transferability** test illustrates limited portability when moving across distinct hydrate chemistries—used as a cautionary lesson on **over-extrapolating** a fit intended for a narrow training manifold.

## Methods

**1 — MD application (atomistic dynamics).** The **Background** of the article discusses **ReaxFF** as a **molecular dynamics** (**MD**) reactive **force field** and reviews generic **MD** practice, but the **`normalized/extracts/2013eldhose-venue-parameterization-reactive_p1-2.txt`** snippet does **not** reproduce the paper’s full validation **MD** protocol table. Until the full **`pdf_path`** is transcribed here: **Engine / code:** **N/A —** explicit **MD** program name not in the indexed excerpt (likely **LAMMPS** in the article—confirm in **`pdf_path`**). **System size & composition:** **atom** counts / **supercell** **stoichiometry** for any reported validation cells—**N/A —** not in the excerpt. **Boundaries / periodicity:** **PBC** vs cluster details—**N/A —** not in the excerpt. **Ensemble:** **NVT**/**NPT** choices for validation trajectories—**N/A —** not in the excerpt. **Timestep:** **fs**-scale integration step—**N/A —** not in the excerpt. **Duration / stages:** **ps**/**ns** equilibration or production lengths—**N/A —** not in the excerpt. **Thermostat:** **Berendsen**/**Nosé–Hoover** settings—**N/A —** not in the excerpt. **Barostat:** **N/A —** not stated for any **NPT** validation leg in the excerpt. **Temperature:** **K**-resolved thermostat targets for validation **MD**—**N/A —** not in the excerpt. **Pressure:** **N/A —** not stated for **MD** legs in the excerpt. **Electric field:** **N/A —** not stated. **Replica / enhanced sampling:** **N/A —** not stated.

**2 — Force-field training (ReaxFF + MMC/SA).** **Parent FF / elements:** **ReaxFF** reactive **bond-order** potential for **MgSO₄ hydrates** (motivated by **seasonal heat storage** applications in the **Introduction**). **QM reference:** **DFT** reference **energies** and **structures** for **hydrate** phases (functional, **basis**, **k-mesh**: **N/A —** not stated in the **p1–2** excerpt; read **`pdf_path`** **Methods**). **Training set:** **crystal structures**, **equations of state**, and **water-binding** curves for **MgSO₄** hydrates used as optimization targets (abstract). **Optimization:** **Metropolis Monte Carlo (MMC)** moves in parameter space combined with **simulated annealing (SA)** after **Kirkpatrick et al.**, replacing the traditional **single-parameter parabolic search**; search targets a **global** minimum in a high-dimensional space with on the order of **~100 parameters per atom** class as stated in the **Background**. **Reference data / validation:** optimized potential reproduces training-set **QM** observables; a **held-out** subset is used for the **transferability** test described in the article.

**3 — Static QM / DFT.** **N/A as standalone block** — **DFT** appears as **QM reference data** for **ReaxFF** training rather than as a separate “production **DFT** application paper” split here.

## Findings

**1 — Outcomes & mechanisms.** The **MMC/SA** optimization finds **ReaxFF** parameter sets that reproduce the targeted **QM** training properties for **MgSO₄ hydrates** (**structures**, **EOS**, **water binding**—abstract-level summary).

**2 — Comparisons.** The workflow is compared against the legacy **single-parameter** optimization strategy as an **efficiency** / **robustness** argument in the article framing.

**3 — Sensitivity & design levers.** **Transferability** is explicitly probed by withholding part of the **hydrate** dataset from the fit; performance **degrades** on this **held-out** chemistry, illustrating sensitivity to **training-set coverage**.

**4 — Limitations & outlook.** The abstract concludes that **ReaxFF** is **not indefinitely transferable** beyond the chemistry represented in the training data; broader **parameter** search cost and **QM** coverage remain practical constraints (**Discussion** in **`pdf_path`**).

**5 — Corpus honesty.** This summary is grounded in the **abstract**/**intro** extract on file; detailed **DFT** settings and any **MD** validation metrics require the full **`pdf_path`** text.

## Limitations

- Computational cost of global search; need for careful QM reference coverage and weighting.

## Relevance to group

Methodological reference for **automated ReaxFF optimization** workflows and for **salt hydrate** systems that appear in thermal/seasonal storage motivations discussed in the article.

## Citations and evidence anchors

- Abstract and Sec. 1: algorithm and MgSO₄ hydrate results (J. Comput. Chem.; DOI above).

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geo]]
