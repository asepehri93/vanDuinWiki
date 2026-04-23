---
id: paper:2019maksov-npj-computat-deep-learning
type: paper
title: "Deep learning analysis of defect and phase evolution during electron beam-induced transformations in WS2"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:ml-atomistic
  - material:tmd
  - task:method-development
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-019-0152-9"
year: 2019
authors:
  - "Artem Maksov"
  - "Ondrej Dyck"
  - "Kai Wang"
  - "Kai Xiao"
  - "David B. Geohegan"
  - "Bobby G. Sumpter"
  - "Rama K. Vasudevan"
  - "Stephen Jesse"
  - "Sergei V. Kalinin"
  - "Maxim Ziatdinov"
venue: "npj Computational Materials"
pdf_sha256: "ee61aee5c75cd5d83b74d641a4e6427769722ef08820047702d623cf3ec8fb7c"
pdf_path: "papers/Others/Maksov_2D_Deep_learning_NPJ_CompMat_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019maksov-npj-computat-deep-learning -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the npj Computational Materials article identified by `doi`, `title`, and `pdf_path`.

## Summary

Scanning transmission electron microscopy (STEM) can capture beam-induced structural evolution in monolayer transition-metal dichalcogenides, producing large image stacks where manual defect counting becomes a bottleneck. This work studies Mo-doped WS\(_2\) under 100 kV electron irradiation by combining deep learning–based defect detection with unsupervised clustering of defect motifs extracted from dynamic STEM movies. The pipeline yields statistical descriptions of defect populations, sulfur-vacancy diffusion, and transition probabilities among complexes involving Mo dopants and sulfur vacancies, enabling quantitative kinetics of solid-state “beam chemistry” that would be arduous to obtain by hand.

The central problem is **throughput**: **dynamic** STEM produces **time series** where **defect** identities change frame-to-frame, so **manual** annotation cannot keep pace with **dose** accumulation and **radiolysis** chemistry. The authors therefore treat **defect** **localization** as a **supervised** **vision** task (once trained) and treat **taxonomy** discovery as an **unsupervised** **clustering** problem over **local** **patches**, separating **“find defects”** from **“name defects.”**

## Methods

**4 — Experiment- and analysis-centric study (not atomistic MD in the primary sense).** The work is built around **in situ** / **dynamic** **STEM** of **Mo-doped WS\(_2\)** with **100 kV** **electron** **beam** exposure (see **Fig. 1** and **Results** in *npj Comput. Mater.*). **“MD application,” “FF training,” and “static DFT”** blocks in **AGENTS** terms are **N/A** for the **primary** evidence chain: there is **no** **LAMMPS**/**ReaxFF** **trajectory** reported as the main result. Instead, the authors: (i) **train a deep network** to detect **lattice defects** in **raw STEM** **movies**; (ii) use **unsupervised clustering** to group **local** **defect patches**; and (iii) from **time series** of **defect** **classes** and **spatial** statistics, **infer effective** **S-vacancy** **diffusion**-related parameters and **transition** rates among **Mo-dopant / S-vacancy** **complexes**. **Instrument** parameters (**dose**, **scan**, **sample** handling) and **ML** **architecture** details are given in the article and **Supplementary** material. **Interfacial** **electric fields** in the TEM sense are intrinsic to the **beam–sample** interaction; there is no separate user-applied **E-field** parameter in the sense of a **pristine MD** “**electric field**” line item—**N/A** in the **molecular** **simulation** sense.

**Replica / rare-event “enhanced sampling” in MD:** **N/A** — the paper does not report **metadynamics**, **umbrella sampling**, etc. on a **PES**; statistics come from **imaging** time series.

## Findings

**1 — Outcomes & mechanisms.** The **deep network** **localizes** **lattice** **defects** in **raw** **STEM** **movie** **frames** **orders**-**of**-**magnitude** **faster** than **hand**-**annotation**, enabling **dense** **time** **series** of **defect** **populations** during **100 kV** **beam**-**driven** **transformation** of **Mo**-**doped** **WS\(_2\)**. **Unsupervised** **clustering** on **local** **patches** produces a **data**-**driven** **taxonomy** of **defect** **motifs** and **tracks** **transition** **frequencies** among **Mo**-**related** **and** **S**-**vacancy**-**related** **configurations** as the **solid** **evolves** **in** **the** **beam**.

**2 — Comparisons.** The **work** **contrasts** **implicitly** with **prior** **manual** **ex**-**situ** **STEM** **analyses** that **could** **not** **scale** to **the** **throughput** **needed** for **kinetic** **inference** on **long** **dynamic** **datasets**; it **does** **not** **replace** **DFT**/**ReaxFF** **barrier** **calculations**—**those** **live** in **separate** **theory** **pipelines**.

**3 — Sensitivity & levers.** **Reported** **kinetics** **(effective** **S**-**vacancy** **diffusion**-**like** **parameters** **and** **complex**-**switching** **probabilities**)** are **necessarily** **functions** of **beam** **current/dose**, **dwell**, **frame** **rate**, and **sample** **preparation** as **set** in the **Methods**; **varying** **any** of **these** **control** **knobs** can **change** the **inferred** **rates** **even** **at** **fixed** **thermodynamic** **T**.

**4 — Limitations & outlook (as framed in the paper).** **Transfer** to **other** **TMDs** or **microscopes** **expects** **re**-**training** **or** **at** **least** **recalibration**; **the** **authors** **position** the **method** as a **general** **template** but **not** a **universal** **off**-**the**-**shelf** **black** **box**. **5 — Corpus / KB honesty.** This **page** **summarizes** **the** **peer**-**reviewed** **article**; **if** a **locator** **(page/Supp** **movie)** **is** **required** for **reproducibility**, **use** the **publisher** **PDF** **and** **Supplementary** **not** **only** this **note**.

## Limitations

Network architecture, training data, and defect taxonomy are tied to the experimental setting; transfer to other materials or microscopes generally requires retraining and validation. The study does not replace atomistic reactive force-field simulations but complements them as an experimental characterization layer.

## Relevance to group

Complements reactive MD and ReaxFF studies of 2D materials by providing a microscopy + machine-learning template for quantifying beam-driven defect kinetics in TMDs.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/s41524-019-0152-9](https://doi.org/10.1038/s41524-019-0152-9) (`papers/Others/Maksov_2D_Deep_learning_NPJ_CompMat_2019.pdf`).

## Related topics

- [[theme-2d-epitaxy-growth]]
