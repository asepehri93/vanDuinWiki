---
id: paper:2020woo-venue-paper
type: paper
title: "Accurate and scalable multi-element graph neural network force field and molecular dynamics with direct force architecture"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:dft-static
  - keyword:gpu-md
  - keyword:machine-learning-potential
  - keyword:nose-hoover
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: ""
year: 2020
authors:
  - "Cheol Woo Park"
  - "Mordechai Kornbluth"
  - "Jonathan Vandermause"
  - "Chris Wolverton"
  - "Boris Kozinsky"
  - "Jonathan P. Mailoa"
venue: "Preprint / institutional PDF (see NeuralNetwork_FF_Kozinsky_Mailoa_2021.pdf)"
pdf_sha256: "759a375fbbda2b6b099de7e0fd048c38b66bdd847b5cd3007a55bd01154761ec"
pdf_path: "papers/Others/NeuralNetwork_FF_Kozinsky_Mailoa_2021.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2020woo-venue-paper -->

Introduces **GNNFF**, a **graph neural network** that predicts **atomic forces** from **translationally invariant**, **rotationally covariant** **local** **features**, enabling **fast** **MD** on **multi-element** systems. The work reports **accuracy** on **several** **inorganic** **benchmarks**, **transfer** from **small**-cell **training** to **larger** **MD**, and a **Li₇P₃S₁₁** **diffusion** run with **~14%** error vs **AIMD** **D**.

## Summary

**GNNFF** targets **direct** **force** **regression** (not energy-then-**differentiate** only). **Training** uses **VASP** **PBE** **AIMD** data on **Li₄P₂O₇**, **Al₂O₃–HF**, **ISO17**, and **Li₇₋ₓP₃S₁₁**; **GNNFF** **NVT** **MD** at **AIMD**-matched **T**, **thermostat**, **time** **step**, and **duration** where reported. A **superionic** **sulfide** **example** shows **Li** **D** within **~14%** of **AIMD** on a **~50** **ps** **window** (Section III of the PDF). Reconcile **year**/**venue**/**DOI** with the final **journal** version when available.

## Methods

**1 — Model (ML interatomic potential, not Reaxff).** **GNNFF** **predicts** **forces** from **graph** **embeddings** with **rotational** **covariance** (Section II). **N/A** — **Reaxff**; this is a **GNN** **FF**.

**2 — Training data (DFT / AIMD reference).** **VASP** **PBE** **AIMD**; **cutoff** **~450** **eV** for **sulfide** **examples**; **Nose–Hoover** **thermostat**; **e.g.** **Li₄P₂O₇** **2** **fs** **time** **step**, **~50** **ps** **(~25k** **frames**); **Al₂O₃–HF** **0.5** **fs**, **~7** **ps** **reactive** **trajectory** (Section III, **SI**). This block is the **DFT**/**AIMD** **parent** of **GNNFF** **supervision**, not a separate **Reaxff** **fit**.

**3 — GNNFF molecular dynamics (application).** **NVT** **MD** **with** **GNNFF** **forces** on **configurations** **paralleling** **AIMD** **(T, thermostat, ts, run** **length** **per** **system**). **Li₇P₃S₁₁** **small** **vs** **large**-**cell** **transfer**; **MSD** → **D** **vs** **AIMD** **(~14%** on **stated** **50** **ps** **window**). **N/A** — **NPT** in the **summary** **line**—confirm **PDF**; **N/A** — **umbrella**; **N/A** — **E-field**. **GPU** timing (NVIDIA **GTX 1080**) **vs** **SchNet** (Section III.A.1). **Hydrostatic** **pressure** **N/A** for the **NVT** **stated** **sulfide** **benchmarks**—**not** a **barostat** **study** in the **curated** **excerpt**.

**4 — Review or non-simulation.** **N/A** — methods + **MD** **paper** (preprint-style **PDF** in **corpus**).

## Findings

**Outcomes and mechanisms.** **GNNFF** **achieves** **strong** **per-force** **errors** and **high** **throughput** on the **published** **suites**; **transfers** from **smaller** **cells** to **larger** **ones** in the **tests** **shown**. **Li** **D** in **Li₇P₃S₁₁** **~14%** of **AIMD** **D** on **comparable** **sampling**.

**Comparisons and sensitivity.** **vs** **AIMD** and **vs** **SchNet** in **selected** **benchmarks**; **cell**-**size** **sensitivity** in **transfer** **tests**.

**Authored limitations and outlook.** **Preprint** **PDF**; **metadata** in **front** **matter** is **incomplete** (**DOI** **empty**). **N/A** — final **peer-reviewed** **pagination** here.

**Corpus honesty.** **Partial** **extraction**; **align** **tables** to **`pdf_path`**.

## Limitations

Corpus slug **`2020woo-venue-paper`** uses a **2021**-dated filename and may not match **publication year**; operators should align **`year`**, **venue**, and **DOI** with the **final** **journal** **version** when ingested.

## Relevance to group

Complements **Reaxff**-centric corpus entries with a **machine-learned** **potential** **workflow** relevant to **solid electrolyte** **ionics**.

## Citations and evidence anchors

Record the **peer-reviewed DOI** once the article metadata is reconciled with the PDF filename.

## Related topics

- [[reaxff-family]]
