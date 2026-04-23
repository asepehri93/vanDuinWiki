---
id: paper:2017admin-venue-microsoft-word
type: paper
title: "Supporting Information: Simulation Protocol for Prediction of a Solid-Electrolyte Interphase on Silicon-Based Anodes (ReaxFF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - material:li-metal-anode
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
  - keyword:qm-training-data
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Kang-Seop Yun"
  - "Sung Jin Pai"
  - "Byung Chul Yeo"
  - "Kwang-Ryeol Lee"
  - "Sun-Jae Kim"
  - "Sang Soo Han"
venue: "Supporting information (J. Phys. Chem. Lett.; see sibling article record)"
pdf_sha256: "8f216c35e5b0d811c1d6c90f82af98a5e4e29fd818394b623ae7dfa199d449df"
pdf_path: "papers/ReaxFF_others/Kang_Seop_Yun_SiC_EC_JPC_Lett_2017_SI.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017admin-venue-microsoft-word -->

## Summary

This corpus PDF is **supporting information** for a **ReaxFF** study of **solid-electrolyte interphase (SEI)** formation on **Si / SiO\(_x\)** anodes in lithium-ion cells, extending an earlier **Si–Li–O** reactive parameterization toward **Si–Li–O–C–H–F** chemistry to represent **carbonate** electrolytes and **additives** such as **fluorinated** species. The SI documents **DFT** training data choices, **ReaxFF** optimization scope for additional **bond/angle/torsion** terms, and **simulation protocol** notes tied to the **parent letter**, enabling reproducibility checks for the **parameter** extension without duplicating the **main text** narrative. For corpus-wide notes on **SI/galley/proof** roles, see [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Methods

**Force-field extension (SI).** Yun *et al.* extend prior **Si–Li–O ReaxFF** parameters (**Refs. S1/S2**) with literature **C–H** and **O–H** blocks (**Refs. S3/S4**), then **develop and optimize** new **bond, angle, and torsion** terms for **Si–C, Li–C, O–C, Si–H, Li–H, F–F, C–F, H–F, Li–F, Si–F** to reach a **Si–Li–O–C–H–F** training space suited to **carbonate** electrolytes and **F-containing additives** (`papers/ReaxFF_others/Kang_Seop_Yun_SiC_EC_JPC_Lett_2017_SI.pdf`). **QM reference data** come from **Q-Chem** **B3LYP/6-311G\*\*** scans of **bond dissociation**, **angle bending**, and **torsions** on molecular training sets, plus **VASP PBE PAW** **plane-wave** **EOS** work on **SiC** crystals (**400 eV** cutoff, **Monkhorst–Pack k-grids**). **EC** reduction pathways and an **EC–vinylene carbonate (VC)** complex supply additional **DFT** targets called out on **SI pp. S1–S2**. **Optimizer software** (**CMA-ES** *vs.* least-squares): **N/A — not stated on the indexed SI pages** used here.

**Production MD for SEI morphology.** The SI states that **large-scale ReaxFF molecular dynamics** will probe **SEI** formation on **Si / SiO\(_x\)**, but the indexed SI pages used here do **not** spell out **supercell size**, **PBC**, **timestep**, **thermostat/barostat**, **temperature** programs, **pressure**, **electric fields**, or **production duration**—those details belong to the **parent *J. Phys. Chem. Lett.* article**, not this SI excerpt alone. **Ensemble** (**NVT** *vs.* **NPT**) for those production trajectories is **not** stated on the indexed SI pages (**N/A —** see parent article).

**Standalone static QM discovery:** **N/A — DFT** entries are **training** data for **ReaxFF**, not separate materials predictions in this file.

## Findings

This **SI** documents **which QM surfaces** anchor the new **Si–C / Li–C / O–C / F** interactions and how **EC/VC** chemistry constrains **carbonate** reduction energetics; **table residuals** between **B3LYP**/**PBE** and the fitted **ReaxFF** energies are the right place to judge fit quality. **Morphology**, **cycling**, and **experimental SEI** validation remain in the **parent letter**—do not cite this PDF alone for those **results**.

## Limitations

Wiki metadata here tracks the **SI PDF**; for full scientific conclusions and validation against experiments, pair this page with the **parent J. Phys. Chem. Lett.** article PDF/metadata in the corpus.

## Relevance to group

ReaxFF parameterization workflow for **battery interphases** on silicon anodes—adjacent to group interests in reactive MD for electrochemical interfaces.

## Citations and evidence anchors

- Treat as SI companion to the KIST/Sejong **SiC/electrolyte ReaxFF** letter; confirm parent DOI from your VOR PDF when available.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Reader notes (navigation)

Use this page together with the **parent** **J. Phys. Chem. Lett.** article for **quantitative** **SEI** claims; the **SI** PDF records **QM** **training** **curves** and **parameter** **ranges** that **main-text** **abstracts** typically omit. When citing **EC**/**VC** **reaction** **energetics**, point readers to **tables** in the **SI** and the **letter** **figures** for **validation** against **experiment**. **Charge** **equilibration** schedules and **cutoff** choices for **QM** **training** geometries appear in the **SI** narrative and should be mirrored if **re-fitting** parameters.
