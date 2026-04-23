---
id: paper:2025nature-nat-generative-model
type: paper
title: "A generative model for inorganic materials design"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:methods-software
  - task:method-development
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41586-025-08628-5"
year: 2025
authors:
  - "Claudio Zeni"
  - "Robert Pinsler"
  - "Daniel Zügner"
  - "Andrew Fowler"
  - "Matthew Horton"
  - "Xiang Fu"
  - "Zilong Wang"
  - "Aliaksandra Shysheya"
  - "Jonathan Crabbé"
  - "Shoko Ueda"
  - "Roberto Sordillo"
  - "Lixin Sun"
  - "Jake Smith"
  - "Bichlien Nguyen"
  - "Hannes Schulz"
  - "Sarah Lewis"
  - "Chin-Wei Huang"
  - "Ziheng Lu"
  - "Yichi Zhou"
  - "Han Yang"
  - "Hongxia Hao"
  - "Jielan Li"
  - "Chunlei Yang"
  - "Wenjie Li"
  - "Ryota Tomioka"
  - "Tian Xie"
venue: "Nature"
pdf_sha256: "5e298395553f3e4f7311df432a1b16df2796463dc02a93f8025618bb206d3b6c"
pdf_path: "papers/Others/Nature_25_A generative model for inorganic materials design.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2025nature-nat-generative-model -->

!!! abstract

MatterGen is a diffusion-based generative model for inorganic crystals that jointly denoises atom types, fractional coordinates, and the periodic lattice, with optional adapter-based fine-tuning toward composition, symmetry, and scalar properties; the manuscript reports higher rates of stable, unique, novel structures and closer DFT-relaxed geometries than prior generative baselines, plus laboratory synthesis of one designed compound with measured property within about 20% of target.

## Summary

The paper introduces **MatterGen**, framed as a **diffusion** process tailored to **periodic crystals**: corruption and denoising operate on **atom types**, **coordinates**, and the **lattice**. A pretrained **equivariant score network** is **fine-tuned** with **adapters** so generation can be steered toward **chemistry**, **space-group symmetry**, and properties such as **magnetic density**. **Density functional theory (DFT)** relaxation is used to assess **stability** and **proximity to local energy minima** relative to prior generative models. A **laboratory synthesis** example compares a measured physical property to a **target** value.

## Methods

### Generative modeling

- **Architecture:** **Diffusion model** reversing a corruption of crystal structures; **equivariant score network** jointly denoises **atom types**, **coordinates**, and **lattice** (Fig. 1 in the paper).
- **Training / fine-tuning:** **Pretraining** on a large stable-structure corpus; **adapter modules** encode **property** or **constraint** labels for **fine-tuning** (chemistry, symmetry, scalar targets).
- **Baselines:** Comparisons include earlier **generative** crystal models and, for some tasks, **substitution** / **random structure search** style baselines (as presented in the figures).

### Validation

- **DFT:** Generated structures are evaluated with **DFT** relaxation to quantify **stability** and **structural closeness** to relaxed ground states (formation-energy and structure-matching metrics in the main text).
- **Experiment:** At least one **synthesized** compound is reported with a **measured** property **within ~20%** of the **target** (Fig. 6 in the paper).

## Findings

- **Performance:** MatterGen is reported to more than **double** the fraction of **stable, unique, novel (S.U.N.)** structures versus selected prior models and to produce structures **>10× closer** to **DFT-relaxed** geometries in the stated benchmark.
- **Conditioning:** After fine-tuning, the model can target **multiple constraints** (illustrative figure shows **high magnetic density** with **composition** chosen for **supply-chain** considerations).
- **Experiment:** The proof-of-concept synthesis aligns a measured property with the **target** within about **20%**. The **PDF** in `pdf_path` is a **Nature** **accelerated** **article** **preview**; use the **VOR** for final **table** and **supplement** **numbers**.

## Limitations

The corpus PDF is a **Nature accelerated article preview** (pre-copyedit disclaimer). DFT settings, full training data, and experimental protocols appear in the **main text / Supplement** rather than fully in the first pages alone.

## Relevance to group

Not a ReaxFF paper; useful as **inverse materials design** and **generative-model** context adjacent to **ML atomistic** workflows.

## Citations and evidence anchors

- DOI: `10.1038/s41586-025-08628-5` — *Nature* (accepted manuscript PDF in corpus).

## Related topics

- [[paper-index-by-domain]]
