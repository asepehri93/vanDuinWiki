---
id: paper:2021kozinsky-venue-paper
type: paper
title: "SE(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials (NequIP)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:qm-training-data
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.48550/arXiv.2101.03164"
year: 2021
authors:
  - "Simon Batzner"
  - "Tess E. Smidt"
  - "Lixin Sun"
  - "Jonathan P. Mailoa"
  - "Mordechai Kornbluth"
  - "Nicola Molinari"
  - "Boris Kozinsky"
venue: "arXiv:2101.03164 [physics.comp-ph] (8 Jan 2021)"
pdf_sha256: "b3b14d98153be186dbdc53748817fad43db393d84c8a2855c090db36659af2aa"
pdf_path: "papers/Others/Kozinsky_Invariant NNs_2101.03164.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2021kozinsky-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes the **arXiv preprint** identified by **`pdf_path`** and **arXiv:2101.03164**. Machine-learning interatomic potentials evolve quickly; for **journal-of-record** benchmarks, software defaults, and revised numerical tables, confirm the **peer-reviewed version** if your bibliography requires it.

## Summary

**Neural Equivariant Interatomic Potentials (NequIP)** are introduced as **SE(3)-equivariant graph neural networks** that learn **energies and forces** for **molecular dynamics** from **ab initio** reference data. The central methodological distinction emphasized in the preprint is architectural: whereas many symmetry-aware models apply **invariant** convolutions and operate primarily on **scalar** features, NequIP uses **SE(3)-equivariant convolutions** built from **geometric tensors** derived from **relative position vectors**, not only distances. The authors argue this preserves **directional** information in atomic environments and yields a more faithful representation for force prediction.

The abstract claims **state-of-the-art accuracy** on a **diverse** benchmark suite spanning **small molecules**, **condensed phases of water**, an **amorphous solid**, a **surface reaction** example, and a **lithium superionic conductor**, while reporting **exceptional data efficiency**—including training from **fewer than 1,000** and in some cases **as few as ~100** reference calculations where prior neural potentials required **orders of magnitude** more data. A further demonstration uses **coupled-cluster-quality** molecular training data to show that high data efficiency can make **expensive quantum-chemical references** practical for potential construction. The introduction frames the work against the **accuracy–cost trade-off** of **classical force fields** versus **DFT**, and the **data-collection bottleneck** that has limited adoption of earlier **neural network potentials**.

## Methods

**Model (ML interatomic potential).** NequIP is an SE(3)-equivariant graph network: local neighborhoods within a spatial cutoff; messages use relative position vectors and equivariant filters; targets are reference energies and forces. Training data: DFT for most benchmark panels; a subset uses higher-level molecular reference data (e.g. coupled-cluster quality) as stated in the preprint. Baselines: rotation-invariant graph models (e.g. SchNet-class) and kernel-style comparators in the discussion. **N/A** for a single LAMMPS production run defined in this note—`extraction_quality: partial` means full hyperparameters, cutoffs, and MD validation should be read from the PDF and supplement. **ReaxFF / classical FF reparameterization:** N/A. **Laboratory experiment:** N/A.

## Findings

The preprint reports that **NequIP** **matches** or **exceeds** **prior** **MLIPs** on the **diverse** **tasks** in the **abstract** (molecules, water phases, an amorphous solid, a **surface** **reaction** example, a Li superionic conductor) while using **smaller** **training** **sets**—**orders** of **magnitude** **fewer** **structures** in some **comparisons** to **invariant** **GNNs**. The **equivariant** **architecture** is implicated in **improved** **force** **learning**; **AIMD** is used as a **kinetic** / **structural** **benchmark** in **later** **sections** (per the **abstract**). **Comparisons** to **SchNet**-class and **kernel**-style **baselines** **and** **limitations** of **data**-**hungry** **NN**-**IPs** are part of the **narrative**. **Sensitivity** to **training** **set** **size** and to **chemistry** **pocket** ( **water** **vs** **reaction** **at** a **interface** ) is the **core** **design** **lever** the **paper** **highlights**; **however** **long**-**time** **MD** under **extreme** **T** or **pressure** is **out**-**of**-**scope** of this **2**-**page** **wiki** **excerpt**—**read** the **VOR** **at** `pdf_path` **(arXiv:2101.03164)**. **Limitations (authored + KB):** **preprint**; **final** **journal** **tables** and **code** may **differ**; **uncertain** **transfer** to **new** **reactive** **chemistries** without **retraining** **(not** a **universal** **reaction** field **like** Reaxff). **Corpus** **/ KB** **honesty** **(PDF**-**grounding**): **numerical** **claims** **(orders**-**of**-**magnitude** **gains**)** should **come** from **the** **PDF** or **a** **peer**-**reviewed** **reprint** **(not** **this** **paraphrase** **in** **isolation** for **external** **citation** of **exact** **%**). **Open** **directions** in **ML**-**IP** **literature** **(post**-**2021** **models**)** are** **N/A** **on** this **page**.

## Limitations

**Preprint status:** citations for **final** peer-reviewed text, **exact** benchmark numbers, and **code release** details may differ from the arXiv v1 excerpt in the corpus. **Coverage** is defined by the training chemistry of each benchmark; **reactivity** and **electrolyte** interfaces still require careful **domain validation**, as for any MLIP. NequIP is **not** a **ReaxFF** replacement in the sense of a universal **reactive** organics/metals training lineage—it is a **machine-learned potential** family with its own **data** and **scope** assumptions.

## Relevance to group

Methodological neighbor to **ReaxFF** workflows: where **ReaxFF** emphasizes **hand-parameterized** reactive chemistry across broad elements, **NequIP**-class models emphasize **data-driven** accuracy with **strong symmetries** and **efficient learning**. Together they illustrate the **toolbox** for long-time atomistic simulation in **materials** and **electrochemistry**.

## Citations and evidence anchors

- arXiv:2101.03164v1 (8 Jan 2021); see `normalized/extracts/2021kozinsky-venue-paper_p1-2.txt` for excerpt alignment.

## Related topics

- [[reaxff-family]]
