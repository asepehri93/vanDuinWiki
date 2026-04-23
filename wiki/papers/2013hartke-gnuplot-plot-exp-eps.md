---
id: paper:2013hartke-gnuplot-plot-exp-eps
type: paper
title: "Approximate photochemical dynamics of azobenzene with reactive force fields"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:method-development
  - keyword:reaxff-parameterization
  - keyword:reactive-md
source_refs: []
doi: "10.1063/1.4837237"
year: 2013
authors:
  - "Li, Yan"
  - "Hartke, Bernd"
venue: "The Journal of Chemical Physics"
pdf_sha256: "7504f177281e8d85b348caf9514cc04a4c7acc59140cae352163321205fda2b8"
pdf_path: "papers/Others/Hartke_JCP_2013_azobenzene.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013hartke-gnuplot-plot-exp-eps -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Fits **ReaxFF-type** potentials separately to **ground** and **first excited** electronic states of **azobenzene** using **genetic-algorithm** global optimization. Coupled to a simple **energy-gap** transition probability model, the authors report **force-field-only** trajectories that reproduce **cis↔trans** photoisomerization with **qualitatively reasonable quantum yields**, aimed at enabling large-scale **photochemical MD** of molecular machines where both **bond rearrangement** and **optical excitation** matter. The approach sidesteps full **surface-hopping** on **ab initio** surfaces while retaining **empirical** **reactive** flexibility.

## Methods

**1 — MD application (atomistic dynamics).** **Photodynamics** integrates **S₁** dynamics using **Langevin** **molecular dynamics** with a **0.1 fs** timestep, coupled to a simple **energy-gap** transition-rate model (**κ**, **χ** parameters defined in the article; `normalized/extracts/2013hartke-gnuplot-plot-exp-eps_p1-2.txt` is abstract-only—confirm details in **`pdf_path`**). **System size & composition:** gas-phase **azobenzene** (order **10¹ atoms**). **Boundaries / periodicity:** **N/A —** isolated-molecule **photodynamics** as described in **J. Chem. Phys.** **139**, 224303 (2013); confirm whether any **PBC** appears in **`pdf_path`**. **Ensemble:** **Langevin** implies stochastic **thermal** coupling (treat as **NVT**-like sampling of **S₁**; confirm target **temperature** in **`pdf_path`**). **Timestep:** **0.1 fs** (abstract). **Duration / stages:** **2000** independent trajectories per **cis→trans** and **trans→cis** direction reported in the abstract (full segment lengths in **`pdf_path`**). **Thermostat:** **Langevin** thermostat coupling as stated. **Barostat:** **N/A —** not used. **Temperature:** **N/A —** explicit **K** thermostat target not in the indexed excerpt (read **`pdf_path`**). **Pressure:** **N/A —**. **Electric field:** **N/A —** photoexcitation handled via the **energy-gap** model rather than a static **field** bias. **Replica / enhanced sampling:** **N/A —** not reported.

**2 — Force-field training.** **Parent FF / elements:** **ReaxFF**-type reactive **bond-order** forms for **azobenzene** on ground (**S₀**) and first excited (**S₁**) surfaces. **QM reference:** **FOCI-AM1** via development **MOPAC** for reference **energies** and **gradients** (**Section 2** in the article). **DFT** is **not** the training **QM** engine here (**N/A —** **plane-wave DFT** benchmarks are outside the stated **FOCI-AM1** protocol). **Training set:** **S₀** and **S₁** **PES** sampling targets for **azobenzene** as described in **`pdf_path`**. **Optimization:** **genetic algorithm (GA)** global search with hybrid **global/local** moves tailored to the underdetermined many-parameter **ReaxFF**-type form. **Reference data / validation:** **quantum yields** from the **force-field** + **gap** workflow are **compared** to reference **Langevin** simulations at the **FOCI-AM1** level (abstract claim).

**3 — Static QM / DFT.** **N/A —** **FOCI-AM1** semiempirical **QM** is the reference model rather than **plane-wave DFT** in this work.

## Findings

**1 — Outcomes & mechanisms.** Coupling fitted **S₀**/**S₁** **ReaxFF**-type surfaces to the **energy-gap** transition model enables **cis↔trans** **photoisomerization** trajectories with **bond breaking**/**formation** handled by the reactive **force field** while **electronic** hopping is approximated without full **surface hopping**.

**2 — Comparisons.** The abstract reports **qualitatively acceptable** **quantum yields** **versus** reference **Langevin** simulations at the **FOCI-AM1** level for both **cis→trans** and **trans→cis** directions.

**3 — Sensitivity & design levers.** **2000**-trajectory ensembles per direction stabilize **yield** estimates against **rare** **branching** in the **gap** model; **κ**/**χ** parameters control the transition **rate** model (see **`pdf_path`**).

**4 — Limitations & outlook.** The approach is framed as a **proof of principle**; accuracy is limited versus higher-level **nonadiabatic** methods, and **reparameterization** is needed for new substituents or condensed-phase environments.

**5 — Corpus honesty.** The repo filename `gnuplot…eps` is an ingest artifact; authoritative **Methods**/**Results** locators are the **JCP** article cited in front matter and **`pdf_path`** (`papers/Others/Hartke_JCP_2013_azobenzene.pdf`). The **`normalized/extracts`** file on record is **abstract-only**.

## Limitations

- Simple transition model; accuracy limited compared to **ab initio** nonadiabatic dynamics; transferability to substituted azobenzenes and condensed phases requires reparameterization.
- **Solvent** **friction** and **environmental** **screening** of **excited** states are omitted in the gas-phase **azobenzene** benchmarks.

## Relevance to group

Methodological bridge between **ReaxFF** culture and **photochemistry**, complementary to ground-state hydrocarbon/battery-focused parameter lines in the corpus.

## Citations and evidence anchors

- Abstract and methods: GA + gap model + isomerization benchmarks (J. Chem. Phys. **139**, 224303 (2013); DOI above).

## Reader notes (navigation)

- Corpus filename `gnuplot…eps` reflects an ingest artifact; the scholarly article is the **JCP** paper cited above.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
