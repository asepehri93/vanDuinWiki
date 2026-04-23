---
id: paper:2021sengul-npj-computat-indeedopt-deep-2
type: paper
title: "INDEEDopt: a deep learning-based ReaxFF parameterization framework (uncorrected proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:ml-atomistic
  - domain:methods-software
  - method:reaxff
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:machine-learning-potential
  - keyword:method-development
source_refs: []
doi: "10.1038/s41524-021-00534-4"
year: 2021
authors:
  - "Mert Y. Sengul"
  - "Yao Song"
  - "Nadire Nayir"
  - "Yawei Gao"
  - "Ying Hung"
  - "Tirthankar Dasgupta"
  - "Adri C. T. van Duin"
venue: "npj Comput. Mater. (proof); same DOI as VOR"
pdf_sha256: "820159024cdff1560182a0b6e9e93335d4a7d129556a2d8267320a6d5b5f4d36"
pdf_path: "papers/Sengul_npj_CompMat_2021_INDEED_opt_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021sengul-npj-computat-indeedopt-deep-2 -->

!!! note "Corpus PDF role"
    **Uncorrected proof** PDF (`Sengul_npj_CompMat_2021_INDEED_opt_galley.pdf`). The **typeset journal PDF** is **`Sengul_npj_CompMat_2021_INDEED_opt.pdf`** on **[[2021sengul-npj-computat-indeedopt-deep]]**.

## Summary

Modern **ReaxFF** projects routinely involve **hundreds** of **bonded** and **off-diagonal** parameters, so **global** search strategies that combine **design of experiments** with **surrogate** models are increasingly attractive for **group-scale** fitting pipelines. ReaxFF optimization is **high-dimensional** and often **non-convex**: conventional searches can stall in **poor local minima** or waste effort exploring **unphysical** regions of parameter space. **INDEEDopt** (**IN**itial-**DE**sign **E**nhanced **D**eep learning-based **OPT**imization) combines **Latin Hypercube Design (LHD)** sampling with a **deep learning** model that learns error structure across sampled parameter vectors. The workflow first **explores broadly**, then uses the learned surrogate to **prune** unpromising domains and **focus** refinement on **low-error** basins. The article demonstrates the approach on **reparameterizing** a **nickel–chromium** alloy ReaxFF and a **tungsten–sulfur–carbon–oxygen–hydrogen** (**quinary**) system, comparing **wall time** and **training-error** metrics against **conventional** optimizers under comparable **QM** training sets.

## Methods

**Corpus PDF.** This page tracks the **uncorrected proof** PDF; **authoritative** tables, **SI** pointers, and typeset text are on **`[[2021sengul-npj-computat-indeedopt-deep]]`**.

**1 — MD application.** The paper centers on **ReaxFF** **parameter** **fit**; any short **MD** in **LAMMPS** to **validate** a field (see the joint article) is **NVT** **molecular dynamics** in **PBC** **supercells** with a **thermostat**, **timestep** in **fs**, and **ps**/**ns** segments as stated there, **temperature** in **K**, and **N/A** / optional **NPT** **barostat** for the cited **validation** snippets. **N/A — external electric field** in the INDEEDopt **workflow**; **N/A — umbrella** as the headline **sampling** (search is in **parameter** space).

**2 — Force-field training (INDEEDopt).** As on the VOR: **LHD** over **ReaxFF** **parameter** vectors, **neural** **surrogate** to rank **low** **error** manifolds, and **conventional** **optimizer** **baselines** on the same **QM** **reference** / **validation** data for **Ni–Cr** and **W–S–C–O–H** demonstrations; **ReaxFF** **equation** (bond/angle/…) **parrex**-style **optimization** and **DFT** **reference** **energies** in the **training** **set** are documented on **`[[2021sengul-npj-computat-indeedopt-deep]]`**.

**3 — Static QM / experiments.** **QM** **reference** data: see VOR. **N/A** — new **laboratory** **experiment** in the methods paper.
## Findings

In the reported **Ni–Cr** and **W–S–C–O–H** tests, **INDEEDopt** identifies parameter sets with **lower** training error **faster** than the conventional route, reflecting reduced wasted effort in **non-viable** regions of parameter space. The **LHD → deep learning** pipeline is presented as a practical way to **escape** poor local minima when initial guesses are weak, complementing (rather than replacing) domain expertise in **training-set** curation.

**Comparisons and corpus honesty.** All quantitative **comparisons** to **conventional** **ReaxFF** **optimization** and **DFT** **errors** should be read from the **typeset** VOR on **`[[2021sengul-npj-computat-indeedopt-deep]]`**; this **proof** **PDF** is **not** a substitute for the **version-of-record**.

## Limitations

Performance depends on **training-set** coverage, **network** architecture, and **LHD** extent; **transfer** to new **element** subsets requires fresh **sampling** and validation. **Proof-PDF** figure/page alignment may differ slightly from the **VOR** on **[[2021sengul-npj-computat-indeedopt-deep]]**. As with any **accelerated** optimizer, reported gains are **demonstration-dependent**: practitioners should still verify **physics** of resulting parameters on **hold-out** **QM** data and **independent** MD benchmarks before production use. Repository automation maps this stable `paper_id` to `normalized/papers/2021sengul-npj-computat-indeedopt-deep-2.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Reader notes (navigation)

- Version-of-record PDF page: **[[2021sengul-npj-computat-indeedopt-deep]]**
- [[reaxff-family]]
