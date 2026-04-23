---
id: paper:2017zheng-venue-research-2
type: paper
title: "Modeling and in situ probing of surface reactions in atomic layer deposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - task:application
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b01618"
year: 2017
authors:
  - "Yuanxia Zheng"
  - "Sungwook Hong"
  - "George Psofogiannakis"
  - "G. Bruce Rayner, Jr."
  - "Suman Datta"
  - "Adri C. T. van Duin"
  - "Roman Engel-Herbert"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "d1104cabee2adf9233634acaad0d68d3a1940dba7e63817b58b9ab540b7ee91e"
pdf_path: "papers/Zheng_Hong_ACS_AMI_ALD_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017zheng-venue-research-2 -->

!!! note "Corpus note"
    **`pdf_path`** points to **`papers/Zheng_Hong_ACS_AMI_ALD_2017_proof.pdf`**, an **ACS author proof**. The **version-of-record** narrative with stable figure numbering is on [[2017yuanxia-zheng-acs-am7b01618]] (and [[2017zheng-venue-research]]). See [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) for proof-duplicate policy.

## Summary

The underlying ACS AMI article investigates **atomic layer deposition (ALD)** of **alumina** from **trimethylaluminum** and **water** on **germanium** surfaces that are either **hydrogen-terminated** or **oxidized**, a stack relevant to **high-κ** gate stacks and **interface trap** control in **semiconductor** processing. Zheng et al. combine **ReaxFF reactive molecular dynamics** with **in situ spectroscopic ellipsometry** (alongside **AFM**, **XPS**, and **impedance** measurements) to study **trimethylaluminum / water** **atomic layer deposition** of **alumina** on **Ge(100)** substrates prepared in **hydrogen-terminated** versus **oxidized** states. The scientific goal is to connect **early-cycle surface chemistry**—**nucleation**, **suboxide intermixing**, and **trap-related** electrical response—to **atomistic** models of **precursor adsorption**, **ligand elimination**, and **oxygen insertion**. This wiki slug holds the **proof PDF bytes**; the **canonical prose** for the same DOI **`10.1021/acsami.7b01618`** lives on **`[[2017yuanxia-zheng-acs-am7b01618]]`**.

## Methods

**Molecular dynamics (reactive).** This slug tracks the **ACS author proof** bytes (`papers/Zheng_Hong_ACS_AMI_ALD_2017_proof.pdf`); the **ReaxFF molecular dynamics** story matches **`[[2017yuanxia-zheng-acs-am7b01618]]`**: **TMA/H₂O** **ALD** on **H–Ge(100)** versus **oxidized Ge(100)** inside **periodic** **supercells** with explicit **atom** counts, **timestep** (fs), **thermostat**/**barostat** settings, **NVT**/**NPT** staging, **temperature** (**K**) setpoints, and **equilibration**/**production** **duration** (ps/ns) as published in the **version-of-record**. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted here.

**Experiments.** **In situ ellipsometry**, **AFM**, **XPS**, and **impedance** protocols mirror the canonical article; use **`[[2017yuanxia-zheng-acs-am7b01618]]`** for figure-quality references.

**Force-field fitting.** **N/A —** identical published **Al/Ge/O/H ReaxFF** consumption as the canonical page.

**Static QM / DFT.** **N/A —** not the primary engine for the coupled workflow summarized here.

**Review scope.** **N/A —** **proof** **PDF** duplicate for cataloguing alternate hashes.

## Findings

**Outcomes and mechanisms.** **Reactive** trajectories again tie **delayed nucleation** on **H–Ge** to sluggish **ligand** elimination, whereas **oxidized** templates undergo **self-cleaning** that seeds an **Al₂O₃/GeO_x** **intermixed** layer moderating **oxygen diffusion** into **Ge**.

**Comparisons.** **Ellipsometry**/**AFM**/**XPS**/**impedance** **benchmarks** on the **proof** **PDF** should be cross-checked against **`[[2017yuanxia-zheng-acs-am7b01618]]`** before citing panel letters or **Supporting Information** pointers.

**Sensitivity / design levers.** **Surface termination** (**hydrogen** vs **native oxide**) remains the central lever controlling early-cycle **growth** transients.

**Limitations / outlook.** **Proof** files may contain layout queries or non-final typography—confirm against the **issue PDF** before archival citation.

**Corpus honesty.** Prefer **`[[2017yuanxia-zheng-acs-am7b01618]]`** for reader-facing science; keep this slug for **duplicate** **PDF** provenance only.
## Limitations

**Proof** PDFs may include **layout artifacts**, **color query marks**, or **non-final** panel labels. **Pagination** and **Supporting Information** numbering must be verified against **`[[2017yuanxia-zheng-acs-am7b01618]]`** before external citation. **Figure** **lettering** in **proofs** sometimes differs from **XML** **typesetting**, so **SI** **cross-references** should be checked against the **publisher** **PDF** when **building** **bibliographies**.

**Confidence rationale:** `med`—duplicate proof; science summarized by pointer to VOR.

## Reader notes (navigation)

- Canonical narrative: [[2017yuanxia-zheng-acs-am7b01618]]
- Sibling ASAP/duplicate: [[2017zheng-venue-research]]
- [[theme-oxides-silica-ceramics]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2017yuanxia-zheng-acs-am7b01618]]
- [[reaxff-family]]
