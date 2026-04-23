---
id: paper:2018smith-j-chem-phys-less-is
type: paper
title: 'Less is more: Sampling chemical space with active learning'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:ml-atomistic
- method:ml-potential
- scale:atomistic
- task:method-development
paper_keywords:
- keyword:machine-learning-potential
- keyword:method-development
candidate_tags: []
source_refs: []
doi: 10.1063/1.5023802
year: 2018
authors:
- Justin S. Smith
- Ben Nebgen
- Nicholas Lubbers
- Olexandr Isayev
- Adrian E. Roitberg
venue: J. Chem. Phys.
pdf_sha256: b88b7a47e5012a19e22868f386f40fe698b11b4ed33f183724ed7584bb7ebd35
pdf_path: papers/Others/Smith_Isayev_Roitberg_NN_CHO_JCP_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018smith-j-chem-phys-less-is -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JCP article identified by `doi`, `title`, and `pdf_path`.

## Summary

The paper presents an **automated active-learning (AL)** workflow (**query-by-committee**, QBC) to grow training data for **ANI**-style neural network potentials: ensemble disagreement flags **high-error** regions of **configuration space** for additional **quantum** (DFT) labeling. On the **COMP6** organic benchmark suite, AL-trained models match or exceed **ANI-1** trained from random sampling using **only 10–25%** of the data, culminating in an **ANI-1x** universal model with competitive accuracy across COMP6. The central claim is **data efficiency**: **neural** **potentials** need not consume uniformly dense **DFT** grids if training focuses on **regions** where the model is already **uncertain**.

## Methods

- **Models:** Deep learning **ANI** potentials trained on **C/H/N/O** organics; ensemble used for **QBC** disagreement.
- **Active learning:** Iterative loop adds configurations where committee potentials disagree most on **energy/force** predictions; contrasted with **random** sampling baselines.
- **Benchmarks:** **COMP6** suite (public on GitHub per abstract) aggregates diverse organic molecules for out-of-sample testing.
- **Reference data:** **DFT** labels supply energies and forces for new training points (details of electronic structure level in the Methods section of the paper).
- **Committee training:** Independent **ensemble** members are trained on the same accumulated set; **disagreement** metrics prioritize **configurations** that reduce **expected** **generalization** error fastest.

## Findings

- **Data efficiency:** AL reaches better overall accuracy than the original **ANI-1** with **~10%** of the training data; continued AL to **~25%** yields large gains versus **ANI-1** on **COMP6**.
- **Universal potential:** The resulting **ANI-1x** model achieves **accurate energies and forces** across the **COMP6** benchmark, approaching the accuracy of specialized models while retaining **broad organic** coverage.
- The authors position **ANI-1x** as a practical **default** for **organic** **conformer** sampling workflows where **ANI-1** accuracy was previously **patchy** on **out-of-sample** **chemistries**.

**Comparisons, sensitivity, and limitations.** The headline result is a **benchmark**-driven **comparison** between **active learning** and **random** **DFT** labeling on **COMP6**, emphasizing **data efficiency** as a **sensitivity** lever for **machine-learning** **potential** quality. **Limitations** include **coverage** limited to the training **chemistry** and the dependence of **committee** disagreement on **DFT** label noise, as discussed in the article and echoed under **## Limitations**. **Corpus honesty:** detailed **DFT** settings and **architecture** hyperparameters should be taken from `pdf_path`, not inferred here.
## Limitations

Coverage is limited to the elements and chemical space represented in training; extrapolation outside COMP6-like organics remains risky without further labeling. **Active learning** also inherits **DFT** **noise** and **basis-set** choices from the label pipeline, so committee disagreement can reflect **label** inconsistency as well as model error.

**Curation note:** this **ANI** / **active-learning** entry complements **[[2017smith-chemical-sci-ani-1-extensible]]** and the **theme** hub [[theme-ml-atomistic-potentials]]; it is **not** a **ReaxFF** paper but is retained because **ML** **potentials** frequently sit beside **reactive** **FF** workflows in the group’s **method** **portfolio**. The **COMP6** benchmark remains the recommended **out-of-sample** **stress** test when judging **ANI-1x** generalization.

## Related topics

- [[theme-ml-atomistic-potentials]]
- [[2017smith-chemical-sci-ani-1-extensible]]
