---
id: paper:2021danielle-reifsnyder-nano-lett-20-illuminating-invisible
type: paper
title: "Illuminating Invisible Grain Boundaries in Coalesced Single-Orientation WS2 Monolayer Films"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:tmd
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:lammps
source_refs: []
doi: "10.1021/acs.nanolett.1c01517"
year: 2021
authors:
  - "Danielle Reifsnyder Hickey, Nadire Nayir, Mikhail Chubarov, Tanushree H. Choudhury, Saiphaneendra Bachu, Leixin Miao, Yuanxi Wang, Chenhao Qian, Vincent H. Crespi, Joan M. Redwing, Adri C. T. van Duin, Nasim Alem"
venue: "Nano Lett. 2021, 21, 6487-6495"
pdf_sha256: "a2414ebcc8cbefd1631d000bc57c4e5d7f9977e154a113b010e8b584a346f6d3"
pdf_path: "papers/Hickey_NanoLetters_WS2_GBs_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021danielle-reifsnyder-nano-lett-20-illuminating-invisible -->

## Summary

Achieving **wafer-scale** **single-crystal** **TMD** films requires understanding **coalescence** defects that may be **invisible** in **bright-field** imaging yet limit **electronic** homogeneity. Hickey et al. combine **electron microscopy** and **ReaxFF molecular dynamics** to connect **MOCVD** growth conditions to **grain-boundary** microstructure in **coalesced monolayer WS₂** films on **2 in. c-plane sapphire** substrates. **Dark-field TEM** reveals **defect arrays** in films that **selected-area electron diffraction** and imaging show are **nearly single-orientation** yet **imperfectly stitched**; **atomic-resolution STEM** classifies **translational** grain boundaries. Films **tilt out-of-plane** when **released** from the substrate. The authors use **statistical facet analysis** over **>1300** facets to relate **nanoscale** building blocks to **multimicrometer** morphology, bridging **sub-Ångstrom** structure with **wafer-scale** texture.

## Methods

### Experiments (CVD, microscopy, morphology)

**Monolayer 2H-WS₂** is grown by **MOCVD** on **2 in. c-plane sapphire** as described in *Nano Lett.* transferred films are imaged on **TEM** grids. **SAED** and **bright-field TEM** show **millimeter-scale** **single-orientation** regions; **dark-field TEM** (DF-TEM) reveals **sub-micron** **faceted** **contrast** not obvious in **bright-field**. **ADF-STEM** classifies local **GB** **structures**; the article reports **>1300** **facet** measurements to connect **nm-scale** **building blocks** to **μ**m-scale **texture** when **Wulff**-type arguments are invoked.

### MD application (ReaxFF)

Hickey *et al.* use **ReaxFF molecular dynamics**—implemented in a **LAMMPS**-class workflow consistent with the cited **ReaxFF** literature and figure captions (see `pdf_path`/SI for the precise **parameter** set and **input** decks). Representative panels show **ReaxFF MD** structures **equilibrated** at **300 K** alongside **STEM**-derived local models for **type A** vs **type B** **translational** boundaries and their **transition** segment. **Boundary / periodicity:** **PBC** **slab** **supercells** for the freestanding GB models as in the SI—**N/A —** full **lateral** cell vectors if not copied into this note. **N/A —** full **supercell** **atom** counts, **0.25 fs**-class **timestep** if used, **NVT** **thermostat** name, and **ps**–**ns** run lengths: take from **Supporting Information** rather than this note. **N/A —** **NPT** barostat, **external electric field**, and **shock**/**MSST** in the main GB workflow. **N/A —** umbrella or metadynamics **sampling** for the primary GB case unless the SI states otherwise.

### Force-field training in this work

**N/A —** this article **applies** an established **2D TMD**/**ReaxFF** description (with references in the *Nano Lett.* text) to support GB models; the paper is not primarily a *de novo* **CMA-ES**/**ParReax** **training** **report** for a new **parameter** set.

## Findings

- **Multiscale structure:** **Statistical facet** analysis and **TEM/STEM** together show that **nearly** **single-crystal** **SAED** can **coexist** with **widespread** **re-entrant** **faceting** and **invisible** (in **bright-field**) **defect** arrays exposed by **DF** contrast.
- **GB types:** The work distinguishes at least **two** **translational**-mismatch **GB** **classes** in **coalesced** films (including **type** **A** and **B** **motifs** in the figures) and a **transition** **zone** with mixed **3|W** and **4|W**-like **W**-site arrangements at the boundary core.
- **Kinetics link:** The authors connect **faster** growth conditions to the observed **defect** catalog (see main text for the growth-rate **comparison** and figure references).
- **Simulations / experiment link:** **ReaxFF** **simulations** **(300 K** **equilibration** in the figure captions) **reproduce** the **out-of-plane** **tilt** and **AB**-stacking motifs discussed for **free-standing** **type B** regions, **supporting** a **chemically** **reasonable** **atomistic** picture **versus** the **imaging**-derived models.
- **Comparisons / limitations:** Where edge **energetics** or **Wulff** arguments appear, those **benchmarks** are in the **paper**; **ab initio** **agreement** is not the headline—**## Limitations** and the **version-of-record** **PDF** carry **caveats** for **ReaxFF** on **S–W** edges and for **TEM** **projection** effects. **Corpus honesty:** do not reuse **lattice** constants or **angle** labels without checking **VOR** `pdf_path` and **supplementary** figures.

## Limitations

**MD** accesses **local** segments and **short times** relative to **CVD** reactor-scale processes; **STEM** contrasts may miss certain **defect** types. **ReaxFF** accuracy for **WS₂** edges depends on the **parameterization** cited in the paper.

**Confidence rationale:** `high`—primary *Nano Lett.* article with abstract-level alignment to extract.

## Citations and evidence anchors

DOI: [10.1021/acs.nanolett.1c01517](https://doi.org/10.1021/acs.nanolett.1c01517). *Nano Lett.* **2021**, **21**, 6487–6495. **ACS** provides **supporting information** downloads alongside the article page; consult there for **extra** micrographs or **methods** not duplicated in this wiki.

## Reader notes (navigation)

**Coalescence** **microscopy** pairs naturally with **kinetic Wulff** discussions on **growth** pages; keep **cross-links** explicit so **retrieval** can hop from **TEM** evidence to **ReaxFF** **edge** models.

- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
