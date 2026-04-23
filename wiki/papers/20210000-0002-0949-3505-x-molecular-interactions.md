---
id: paper:20210000-0002-0949-3505-x-molecular-interactions
type: paper
title: "Molecular Interactions and Layer Stacking Dictate Covalent Organic Framework Effective Pore Size"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
  - material:zeolite-porous
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c10866"
year: 2021
authors:
  - "Phuoc H. H. Duong"
  - "Yun Kyung Shin"
  - "Valerie A. Kuehl"
  - "Mohammad M. Afroz"
  - "John O. Hoberg"
  - "Bruce Parkinson"
  - "Adri C. T. van Duin"
  - "Katie D. Li-Oakey"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "788a7c45b93d0854d58b8a032a32112204a14be3d0a9d7cd8a4e4fba01fa509e"
pdf_path: "papers/Duong_Shin_ACS_AMI_COF_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20210000-0002-0949-3505-x-molecular-interactions -->

!!! note "Galley PDF"

    Corpus path **`Duong_Shin_ACS_AMI_COF_2021_galley.pdf`** is a **galley**; prefer the **version-of-record** PDF at the DOI when available locally. See also [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) context for **proof/galley** handling.

## Summary

Duong *et al.* combine **ReaxFF molecular dynamics** with **experiments** on an **imine-linked carboxylated covalent organic framework (C-COF)** membrane platform used for **organic solvent nanofiltration (OSN)**. The scientific claim is that **effective pore size**—what actually governs **selectivity**—is not fixed by nominal **crystal** design alone, but emerges from **layer stacking**, **framework flexibility**, and **molecule–framework** interactions in **swollen** or **solvated** environments. **Reactive MD** captures **hydrogen-bonding**, **conformational** rearrangements, and **pore breathing** that static **pore metrics** omit, while **experiments** provide **permeance/selectivity** benchmarks under **solvent** conditions relevant to **OSN**. **Adri C. T. van Duin** is a coauthor, connecting the work to the group’s **porous materials** and **liquid-interface** simulation portfolio.

## Methods

**1 — MD application.** **ReaxFF** **reactive MD** of a **2D** **imine**-**linked** **carboxylated** **C-COF** in explicit **organic** **solvents**, modeling **pore** **morphology**, **layer** **stacking**/**spacing**, and **solute**/**solvent** **structure** inside **channels** **(PBC** **membrane** **supercells**; **NVT**/**NPT** choices and **1 fs**-class **timesteps** as in *ACS Appl. Mater. Interfaces* **2021** **Methods**). **Thermostat** class and time constant, **NPT** **Parrinello**–**Rahman** barostat settings (if any), and target **temperature** in K are given in the article/**SI**—not transcribed in this short note. **Equilibration** and **multi-ns**-scale **trajectory** **lengths** (where given) support **G(r,t)**-like and **pore** **diameter** analyses; confirm **ps**/**ns** **duration** in the full text. **Electric** **field**, **replica** **exchange**, and **shock** loading—**N/A**.

**2 — Experiments (integrated with MD).** **OSN** **(organic** **solvent** **nanofiltration**)** **permeation** and **selectivity** **data** for the same **C-COF** **chemistry** supply **macroscopic** **benchmarks**; **N/A** **DFT** **replica** in this paper’s main workflow beyond **ReaxFF** **parametrization** context.

**3 — Force-field / QM context.** The article uses a **published**/**fitted** **ReaxFF** suitable for **COF**-**solvent** **C/H/O**/**N**-rich chemistry; **N/A** here to restate the **full** **training** set—see **JACS**-family **SI**-level detail in the **VOR** **PDF** **(galley** in corpus; confirm **table** **IDs**).

**4 — Galley.** Ingested **ACS** file is a **proof/galley**; prefer **VOR** **pagination**.

## Findings

**Conclusion in the abstract.** **Aligned,** **crystalline** **1D** **pores** can deliver **ultrahigh** **permeance** while still allowing **tunable** **selectivity**; **MD** and **OSN** **experiments** show **effective** (not just **designed**) **pore** **aperture** and **solvated** **solute** **size** **depend** on **solvent** **environment**, so **stacking**/**flexure** and **molecule**–**framework** **interactions** matter. **Comparisons** are **ReaxFF** **trajectory**-derived **pore** metrics versus **laboratory** **filtration** **performance**. **Sensitivity** to **solvent** and **pore** **morphology** (including **pore** **“breathing”**/**stacking** **defects**) is the mechanistic point. **Limitation:** a **classical** **reactive** **FF** is not a **DFT** **thermometer**; **ReaxFF** **transfer** to other **COFs** is **uncertain** without retraining. The **local** **galley** file limits **citation** **precision**—use the **VOR** **PDF** (see **## Limitations**).

## Limitations

**Galley** formatting may differ slightly from **VOR**; **ReaxFF** transferability to other **COF** chemistries requires case-by-case validation. **OSN** performance depends on **membrane defects** and **macroscopic** flow fields not fully represented in atomistic cells.

## Relevance to group

Demonstrates **ReaxFF** applied to **COFs** and **liquid–membrane** transport with **experimental** grounding.

## Citations and evidence anchors

- DOI: [10.1021/acsami.1c10866](https://doi.org/10.1021/acsami.1c10866)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- `paper_keywords` includes **`keyword:galley-or-proof-pdf`**.

