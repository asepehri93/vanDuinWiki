---
id: paper:2017yuanxia-zheng-acs-am7b01618
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
pdf_sha256: "e22efd7ed6f9e0bc1225caac0a6401580441f19509fd7a8d92c3aa44647162cf"
pdf_path: "papers/Zheng_Hong_ACS_AMI_ALD_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017yuanxia-zheng-acs-am7b01618 -->

## Summary

The work combines **ReaxFF** reactive molecular dynamics with **in situ real-time spectroscopic ellipsometry** (and complementary ex situ AFM and XPS) to interpret atomic layer deposition (ALD) of Al\(_2\)O\(_3\) from trimethylaluminum and water on **hydrogen-terminated and oxidized Ge(100)**. The goal is molecular-level insight into how surface preparation changes nucleation, intermixing, and electrical interface quality. **Ge** channel devices motivate **high-κ** **Al\(_2\)O\(_3\)** gate stacks, but **ALD** **nucleation** on **Ge** is sensitive to **native oxide** versus **H-terminated** starting surfaces; linking **atomistic** chemistry to **in situ** optical thickness tracks helps separate **interfacial oxidation** from **dielectric** **growth** transients.

## Methods

**Molecular dynamics (reactive).** **ReaxFF molecular dynamics** resolves **trimethylaluminum (TMA)** and **water** half-reactions during the first **ALD** cycles on **H-terminated Ge(100)** versus **oxidized Ge(100)** **slabs**, tracking **adsorption**, **ligand elimination**, and **oxygen insertion** that couple to **GeO_x** formation at the **temperature** (**K**) setpoints listed in **ACS AMI** **Methods**. **Periodic** **supercells** with explicit **atom** inventories, **timestep** (fs), **thermostat**/**barostat** choices, **NVT**/**NPT** staging, and **equilibration**/**production** **duration** (ps/ns) are given in **ACS Appl. Mater. Interfaces** **2017**, **9**, **15848–15856** (`pdf_path`). **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the abstract-level summary used here.

**Experiments (integrated diagnostics).** **In situ spectroscopic ellipsometry** follows **film thickness** and optical constants during **TMA/H₂O** exposure; **AFM**, **XPS**, and **impedance** spectroscopy provide **ex situ** morphology, **chemical state**, and **interface trap** metrics tied to the simulated **intermixing** trends.

**Force-field fitting.** **N/A —** the manuscript employs a published **Al/Ge/O/H ReaxFF** parameterization suited to **ALD** on **Ge**; no new **training** loop is summarized in the excerpted abstract.

**Static QM / DFT.** **N/A —** the coupled workflow centers on **ReaxFF MD** plus laboratory probes, not on-the-fly **DFT** dynamics.

**Review scope.** **N/A —** primary **experiment**-integrated research article (sibling ingests: **`[[2017zheng-venue-research]]`**, **`[[2017zheng-venue-research-2]]`**).

## Findings

**Outcomes and mechanisms.** **Reactive** trajectories rationalize a **nucleation delay** on **H–Ge(100)** while **oxidized** templates undergo a **self-cleaning** response that builds an **Al₂O₃/GeO_x** **intermixed** layer, **suppressing oxygen diffusion** into **Ge** relative to the hydrogen-terminated case in the modeled chemistry.

**Comparisons.** **In situ ellipsometry**, **AFM**, and **XPS** **benchmarks** align with the simulated early-cycle trends, and **impedance** data argue the **intermixed** layer is critical for **low interface trap density** and well-behaved **dielectric/Ge** contacts.

**Sensitivity / design levers.** Contrasting **hydrogen-terminated** versus **oxidized** starting **surfaces** is the primary **experimental**/**computational** lever controlling **nucleation** timing and **suboxide** **interdiffusion**.

**Limitations / outlook.** The combined workflow is positioned as extensible to other **ALD** precursors, but each new chemistry requires refreshed **simulation** targets and **optical** modeling assumptions.

**Corpus honesty.** Duplicate **PDF** ingests exist for ASAP/**proof** variants; this slug uses the **AMI** article **PDF** named in front matter—confirm figure numbering against siblings before external citation.
## Limitations

Full numerical protocol for ReaxFF runs (supercell sizes, temperatures, cycle definitions) is not summarized on this page; use the article and SI.

## Relevance to group

Co-authored by Adri C. T. van Duin; demonstrates ReaxFF paired with in situ optics for semiconductor dielectric deposition.

## Reader notes (navigation)

Related corpus entries for the same study under alternate PDFs: [[2017zheng-venue-research]], [[2017zheng-venue-research-2]].

## Citations and evidence anchors

- DOI: `10.1021/acsami.7b01618`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
