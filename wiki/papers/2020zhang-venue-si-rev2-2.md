---
id: paper:2020zhang-venue-si-rev2-2
type: paper
title: "Supporting Information: Atomistic-Scale Simulations of Graphene Growth on Silicon Carbide (Thermal Decomposition and CVD)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:supporting-information
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: ""
year: 2020
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Chem. Mater. (Supporting Information)"
pdf_sha256: "9528c4fed888d897a3f20fce194828d8feaed89ce9f66b9d6e0d2f1dc3327618"
pdf_path: "papers/Zhang_ChemMat_2020_SiC_graphene_Supplement.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020zhang-venue-si-rev2-2 -->

Supporting Information for atomistic-scale simulations of graphene formation on silicon carbide by thermal decomposition and chemical vapor deposition (CVD). The SI documents comparisons between ReaxFF and DFT, Si-removal-rate sensitivity on Si-terminated surfaces, and extensive snapshot series for ECM, TDM/CVDM model families, graphene defects and grain boundaries, and growth sequences on C-face versus Si-face SiC.

## Summary

This PDF is **Supporting Information** for the *Chemistry of Materials* work on graphene growth on SiC (see companion article and any VOR-linked paper page in this wiki). It compiles **ReaxFF versus DFT** benchmarks (figures and tables), studies of **Si removal rate** on Si-terminated surfaces, and trajectory-style **snapshots** for multiple modeling setups (ECM, TDM, CVDM) including high-carbon-concentration models, C-face and Si-face growth, defects and grain boundaries, and captions for supplementary videos.

## Methods

This file is **Supporting Information** for the *Chemistry of Materials* graphene-on-**SiC** study; the indexed opening is a **table of contents** listing **figures** and **video** captions, not a standalone simulation protocol. **ReaxFF/DFT** comparisons, **Si removal** sensitivity, and **ECM**/**TDM**/**CVDM** snapshot series are organized as **Fig. S1–S14** and **Videos S1–S3** (see `normalized/extracts/` for the ToC text).

**1 — MD application (atomistic dynamics).** The parent publication describes **reactive MD** of **graphene** growth on **SiC**; this SI PDF does **not** reprint full **LAMMPS**-style run cards on its first pages. **Engine** — follow the **version-of-record article** for the MD code and ReaxFF call pattern; **N/A** to recover from the **ToC page** alone. **System** — **SiC** **slab**/**surface** models with **carbon** enrichment, **graphene** **defects**, and **GB** examples appear across **Figs. S5–S14**; **atom** counts and lateral cell vectors are in figure-level text in the full SI, not the one-page contents list. **Boundaries** — **3D periodic** **PBC** **slabs** as in the parent work; **N/A** in the ToC. **Ensemble** — **NVE**/**NVT**-type segments as reported in the main text; **N/A** in the ToC. **Timestep** — sub-**1 fs** integration is standard for this ReaxFF line; list values from the main article. **Duration** — **ps–ns** **production** segments per panel are in the article/SI figure captions, not the extract. **Thermostat**/**barostat** — **NVT**-style **thermal** control for annealing paths where stated; **NPT** and **hydrostatic pressure** **control** — **N/A** unless a panel explicitly uses a **barostat** (check main text). **Temperature** — **thermal** decomposition and **CVD** sections span stated **K** **ranges** in the main paper. **Electric field** — **N/A** in the ToC. **Shear / shock** — **N/A** here. **Long-range forces / QEq** — use the parent’s **ReaxFF** + **EEM** description. **Replica / enhanced sampling** — **N/A**.

**2 — Force-field training.** The SI is **not** a parameter release note; **Figs. S1–S3** and **Table S1** give **ReaxFF vs DFT** checks tied to the article’s training/validation program—see the **parent** for **QM** reference data used in fitting.

**3 — Static QM / DFT.** **DFT** data enter through **comparative** **figures**/**tables**; **functional** and **k-point** **settings** for those references are in the main **Methods**/**SI** of the primary paper.

**4 — SI / duplicate roles.** Cite the **VOR** article and DOI for scientific claims; use this PDF for **supplementary** **figure** and **media** **locators**.

## Findings

**Outcomes and mechanisms (SI scope).** The **SI** assembles **ReaxFF/DFT** **benchmarks** (S1–S3, T1), probes **Si removal** rate on **Si-terminated** surfaces (S4), and provides **trajectory**/**snapshot** support for **ECM**, **TDM**/**CVDM** paths, **defect** and **GB** **morphology**, and **growth** on **C-** vs **Si-face** SiC (S5–S14) plus **Videos S1–S3**. **Comparisons** are **QM vs ReaxFF** and **inter-model** (ECM vs TDM vs CVDM) in figure space. **Sensitivity** to **reaction path** and **face termination** is visible across the parallel figure series. **Authored limitations** of any **force field** for **CVD** kinetics live in the **main** discussion. **Corpus note:** this KB page is **SI-only**; **numerical** run parameters must be **verified** against the **VOR** **PDFs**, not the ToC snippet alone.

## Limitations

Supporting information does not substitute for the main article text; boundary conditions, full parameter lists, and convergence settings for production runs should be taken from the **primary article** and its extended SI sections where available.

## Relevance to group

Penn State–authored ReaxFF modeling of **2D carbon on SiC** with explicit benchmarking to **quantum data**, consistent with the group’s reactive MD line on surfaces and wide-band-gap substrates.

## Citations and evidence anchors

Prefer the parent *Chem. Mater.* DOI and main-text sections when citing scientific claims; use this file for **SI figure/video** locators.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

- This slug is an **SI PDF**; pair with the **version-of-record article** PDF or wiki page when available.
