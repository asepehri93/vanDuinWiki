---
id: paper:2023gaikwad-npj-computat-enhancing-faradaic
type: paper
title: "Enhancing the Faradaic efficiency of solid oxide electrolysis cells: progress and perspective"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:methods-software
  - task:review
  - scale:multiscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:galley-or-proof-pdf
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-023-01044-1"
year: 2023
authors:
  - "Prashik S. Gaikwad"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
venue: "npj Computational Materials"
pdf_sha256: "76ce411546ff88eed0a9cc4ac44cd77fbfff6696127069fc33132a83409c11ed"
pdf_path: "papers/Gaikwad_npj_CompMat_SOFC_review_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2023gaikwad-npj-computat-enhancing-faradaic -->

## Summary

Solid oxide electrolysis cells promise efficient hydrogen production at high temperature, but Faradaic efficiency losses from parasitic reactions, microstructural degradation, and transport limitations remain practical barriers. Gaikwad, Shin, and van Duin review how electrode, electrolyte, and interconnect materials, together with operating conditions, influence Faradaic efficiency in SOEC stacks. The article synthesizes experimental and modeling literature, highlighting multiscale simulation opportunities—including atomistic reactive modeling along ReaxFF-related lineages where chemistry at oxide surfaces matters—for diagnosing loss channels and guiding materials design. The review is positioned for computational materials audiences who must couple device metrics with atomistic mechanisms. It also stresses that Faradaic efficiency is an integrative metric: losses can originate in any stack layer, so localized fixes require systems thinking.

The review’s **Methods** stance is explicitly **literature synthesis**: it compares how **experimental** **gas** analytics, **electrochemical impedance**, **microscopy**, and **multiscale** **models** each constrain **where** **Faradaic** losses arise (electrode **kinetics**, **electrolyte** **leakage**, **interconnect** **oxidation**, **steam** **starvation**, etc.), rather than presenting one new **in-house** **benchmark** cell.

## Methods

### Review organization (D)

- **Axes:** **Stack components** (**anode**, **cathode**, **electrolyte**, **interconnect**), **operating conditions** (**T**, **current density**, **steam fraction**), and **degradation** modes tied to **Faradaic efficiency** losses.
- **Literature types synthesized:** **Experiments**, **continuum** transport/reactor models, **kinetic Monte Carlo**, **electronic-structure** studies, and **atomistic** surface models (including **reactive** approaches where cited). **Comparative protocol (implicit):** the **review** asks how **local** **loss channels** and **interfacial** chemistry in **cited** works map onto **cell-level** **Faradaic** metrics—**not** a new **kinetic** **benchmark** in one **simulation** code. **N/A** — the article does not introduce a **single** **DFT/MD/continuum** **training** **dataset**; it **surveys** **primary** studies. **N/A** — the **Methods** of **cited** **experiments** (**gas** analytics, **EIS**, **T**, **p**) vary by source; the **review** ties them to **phenomenological** **categories** of **inefficiency**.

### Modeling chapter structure

Contrasts **continuum** **mass/charge** transport with **atomistic** **elementary-step** resolution; **no single new benchmark** simulation is central to the review.

### Corpus PDF note

The ingested file may be a **galley**; layout can differ from final **npj Computational Materials** typesetting. **N/A** — this **page** is **not** a **laboratory** **Methods** log; **VOR** should be used for final **section** **pagination**.

## Findings

### Problem framing

**Low Faradaic efficiency** and **high** **$/kg H\(_2\)** persist as practical barriers despite favorable **thermodynamic** efficiency vs some **low-T** electrolyzers.

### Mechanisms and modeling gaps

**Parasitic** chemistry, **microstructural** evolution, and **transport** limits **siphon** current from the **oxygen evolution** / **hydrogen** product channels; the review maps these to **multiscale** modeling opportunities (**DFT**, **kMC**, **continuum**, **microstructure**).

### Outlook

Emphasizes **integrated** workflows rather than isolated **DFT** snapshots; **Faradaic efficiency** should be tracked alongside **microstructure** evolution, not **current density** alone.

### How to use this page safely

**Quantitative** **efficiency** values are **second-hand**—verify **gas compositions**, **seals**, and **operating windows** in each **cited primary** study before reuse in **MAS** claims. **Comparisons** between **cited** **SOEC** and **protonic**/**other** **oxide** **systems** follow the **primary** references, not new **fits** in this **review**. **Open directions** the **authors** highlight (integrated **continuum+atomistic** **loss** accounting) are **opinion**-level **outlook**—treat as **review** **synthesis** with **caveats**.

## Limitations

As a review, quantitative values are second-hand; consult primary references for uncertainties and experimental conditions.

## Relevance to group

Positions Shin and van Duin within hydrogen and solid-oxide modeling discourse; complements application-focused articles such as `paper:2023gaikwad-journal-of-t-modeling-dynamic` where present in the corpus.

## Citations and evidence anchors

- DOI: [10.1038/s41524-023-01044-1](https://doi.org/10.1038/s41524-023-01044-1)

## Related topics

- [[2023gaikwad-journal-of-t-modeling-dynamic]]
- [[reaxff-family]]
