---
id: paper:2020ndayishimiye-open-ceramic-roadmap-densification-2
type: paper
title: "Roadmap for densification in cold sintering: chemical pathways"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:review
paper_keywords:
  - keyword:review-or-perspective
  - keyword:galley-or-proof-pdf
  - keyword:oxide-surface
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.oceram.2020.100019"
year: 2020
authors:
  - "Arnaud Ndayishimiye"
  - "Mert Y. Sengul"
  - "Takao Sada"
  - "Sinan Dursun"
  - "Sun Hwi Bang"
  - "Zane A. Grady"
  - "Kosuke Tsuji"
  - "Shuichi Funahashi"
  - "Adri C. T. van Duin"
  - "Clive A. Randall"
venue: "Open Ceramics (journal pre-proof PDF in corpus)"
pdf_sha256: "866a99a34f7a4597415ffbda209c2947885641b09d9ab14e2b222b5850fa96cf"
pdf_path: "papers/Ndayishimiye_Roadmap_ColdSintering_preproof_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020ndayishimiye-open-ceramic-roadmap-densification-2 -->

## Summary

**Cold sintering (CSP)** densifies ceramics at unusually low temperatures (**often below ~400 °C**) by coupling **pressure** with **transient chemical media** (solvents, hydrates, salt additives) that mediate mass transport at interfaces without requiring full high-temperature lattice diffusion. This *Open Ceramics* roadmap article—co-authored by **Adri C. T. van Duin**—provides a **taxonomy** of **chemical pathways** observed or proposed across ceramic and composite families, emphasizing that many recipes rely on **transient phases** that are not present in the final microstructure. The local **`pdf_path`** is a **journal pre-proof** (`papers/Ndayishimiye_Roadmap_ColdSintering_preproof_2020.pdf`); a sibling wiki page may track a cleaner PDF variant (**`[[2020ndayishimiye-open-ceramic-roadmap-densification]]`**).

## Methods

This *Open Ceramics* contribution is a **qualitative review and process taxonomy** for **cold sintering (CSP)**, not a single numerical benchmark. **4 — Reviews / non-simulation (literature scope).** The text synthesizes **transient-solvent**, **additive**, and **interfacial-reaction** classes across ceramic families, cites how **XRD, microscopy, calorimetry,** and related methods are used in the field, and situates **pressure-solution** style densification next to other creep limits. It references **reactive MD** and **ReaxFF**-style work as *examples* in the **cited literature** rather than reporting one new MD protocol here. For **sintering** “methods” the manuscript illustrates typical **lab** flows (**manual** mixing, **~10 min** **room-temperature** press to reorder particles, **~20 °C min⁻¹** ramps, dwells, and **uniaxial** tooling with process parameters collected in **Supplementary Table S1** as referenced in §2.1. **1–3 (MD, FF, static QM):** **N/A —** no primary **atomistic** dataset is executed in the roadmap itself; read cited papers for **ReaxFF** and **DFT** settings. **N/A (full MD checklist)** for this page by design. **Provenance:** local **`pdf_path`** is a **journal pre-proof**; for presentation details prefer **`[[2020ndayishimiye-open-ceramic-roadmap-densification]]`** when the **VOR** is needed.

## Findings

The roadmap argues that **CSP** chemistry is **heterogeneous** across materials classes: what limits densification is often a **chemical** step (dissolution–reprecipitation, complexation, interfacial amorphization) rather than purely mechanical compaction, but the dominant mechanism can change with **solvent chemistry**, **particle size**, and **electric field** history in field-assisted variants. The authors stress a need to separate **rate-limiting chemical steps** from **mechanical** contact-area evolution to mature predictive processing models. **Reactive MD** is positioned as a tool to propose atomistic sequences for interfacial reactions when paired with experimental validation.

## Limitations

**Pre-proofs** can differ from **version-of-record** text in minor editorial details; prefer the sibling page noted above for stable reader citation when both PDFs exist in the corpus.

## Reproducibility notes

Cold sintering studies that cite atomistic models should specify **solvent activity**, **particle** surface chemistry, and whether **electric fields** are present—each pathway class has distinct timescales. When using **ReaxFF** snapshots to interpret interfacial reactions, pair them with **in situ** evidence where possible because CSP often involves **amorphous** interlayers not obvious from ideal crystal interfaces.

Pre-proof PDFs sometimes omit final **editorial** figure polish; when two corpus paths exist, compare schematic **process flow** diagrams between pre-proof and VOR siblings before citing a specific panel label in downstream automation.

## Relevance to group

**Manifest** record for the **pre-proof** file path (van Duin co-author); links to **CSP** + **ReaxFF** literature.

## Reader notes (navigation)

- [[2020ndayishimiye-open-ceramic-roadmap-densification]]
- [[2020ndayishimiye-journal-of-t-comparing-hydrothermal]]

## Related topics

- [[reaxff-family]]
