---
id: paper:2021wilkinson-acta-materia-hybrid-machine
type: paper
title: "Hybrid machine learning/physics-based approach for predicting oxide glass-forming ability"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - material:silicate-glass
  - task:method-development
  - domain:methods-software
  - scale:multiscale
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2021.117432"
year: 2022
authors:
  - "Collin J. Wilkinson"
  - "Cory Trivelpiece"
  - "Rob Hust"
  - "Rebecca S. Welch"
  - "Steve A. Feller"
  - "John C. Mauro"
venue: "Acta Materialia"
pdf_sha256: "1144cb9755dd8f612683da01931e715e52c02f172003415d24f152939592f2df"
pdf_path: "papers/Others/Wilkinson_ML_glass_ActaMaterialia_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021wilkinson-acta-materia-hybrid-machine -->

## Summary

**Glass-forming ability (GFA)** is commonly operationalized as the **critical cooling rate** required to bypass crystallization on quench from the melt. Industrial oxide glass development still relies heavily on **empirical** composition maps and heuristics, while physics-based models struggle to deliver **quantitative**, composition-specific GFA predictions across large formulation spaces. This *Acta Materialia* article proposes a **hybrid** approach: a deliberately simplified **toy potential energy landscape** captures essential **liquid thermodynamics** and **kinetic accessibility** features associated with vitrification, and **machine learning** maps those structured descriptors to **critical cooling rates** or closely related GFA surrogates for **oxide** compositions. The intent is to combine **interpretable physics** with data-driven flexibility rather than treating ML as a black-box fit to composition vectors alone.

## Methods

**Reviews / non-atomistic methods (per AGENTS block 4).** This is **not** a LAMMPS production paper. The authors couple a **toy landscape** model of **liquid** thermodynamics and kinetics (to access **vitrification** and **critical quench rate** / **GFA** behavior) with **machine learning** to predict **critical quench rates** from composition (abstract: “toy landscape model … combined with machine learning … calculate the critical quench rate”). The landscape is meant to access the **physics** controlling **glass-forming ability** by **simulating** **liquid** thermodynamics and kinetics in a reduced model, then feeding results into **ML**; training uses **published** GFA and related data (see main text and **supplementary** material for sources and **train/test** design). **1 — MD application:** **N/A** — explicit atomistic **MD** is not the core engine; the **toy landscape** replaces bulk melt **MD** in this workflow. **2 — ReaxFF / classical FF training:** **N/A** — not a **ReaxFF** or **EAM** parameterization study. **3 — Static QM:** **N/A** as the primary result. **4 — Experiments:** **N/A** for new lab work—**experimental** GFA labels come from the **literature** compilation used for training.

## Findings

The paper positions the **toy landscape + machine learning** combination as a way to estimate **critical quench rates** / **glass-forming ability (GFA)** with an explicit **liquid** thermodynamics and kinetics story (abstract: “toy landscape model … combined with machine learning”), rather than a black-box map from composition alone. **Outcomes** in the main text are the **trained models’** performance on published GFA / **r\_{crit}** labels and the **interpretation** of which landscape-derived descriptors matter—**N/A** in this note to reproduce every benchmark table; see *Acta Materialia* and SI. **Comparisons** include discussion of prior **empirical** and **physics-based** GFA routes (Zachariasen-style rules, constraint theories, calorimetric parameters) in the introduction; hybrid scores should be read against those baselines in the paper. **Sensitivity** to training splits and feature sets is a methodological theme for ML; detailed sweeps are in the article. **Limitations and outlook** follow the authors’ discussion of industrial impact, physical insight, and what the glass community would need for better **GFA** prediction (abstract and conclusions).

## Limitations

This is **not** a **ReaxFF** or atomistic MD paper; **reactive pathways**, **phase separation**, and **heterogeneous nucleation** on experimental timescales are outside the model class unless added as extensions.

## Reproducibility notes

Hybrid GFA models should be evaluated with **train/validation splits** that respect chemically related compositions; otherwise ML can memorize families rather than learn transferable landscape features. When integrating with atomistic pipelines, treat the toy landscape outputs as **priors** for composition screening rather than replacements for **nucleation** measurements.

For industrial readers, the key reproducibility artifact is the **toy landscape** parameterization itself: any change to basin depths or barrier heights shifts predicted **critical cooling rates**, so sensitivity analysis should accompany single-point GFA predictions. Where available, compare predicted rankings against **experimental** critical cooling measurements or surrogate metrics from dilatometry rather than trusting cross-validated scores alone.

## Reader notes (navigation)

_(No dedicated corpus hub page yet for toy-landscape GFA.)_
