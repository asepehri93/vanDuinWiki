---
id: paper:2017fa-venue-acam-2
type: paper
title: "Investigation on pyrolysis mechanism of Shenfu coal based on ReaxFF force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Zhao Lei"
  - "Qingping Ke"
  - "Fei Geng"
  - "Yunhe Zhang"
  - "Ruilun Xie"
  - "Ping Cui"
venue: "2017 International Conference on Coal Science & Technology / 2017 Australia-China Symposium on Energy (Beijing)"
pdf_sha256: "d0e5723a56b6fb20d9049e98c7e9b646780ce2fbd91ae8d147ea643a0858f092"
pdf_path: "papers/ReaxFF_others/Chinese_Coal_Abstracts/Investigation on pyrolysis mechanism of Shenfu coal based on ReaxFF force field.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017fa-venue-acam-2 -->

## Summary

This corpus entry captures a **conference abstract** PDF from the 2017 International Conference on Coal Science & Technology / 2017 Australia–China Symposium on Energy in Beijing on **Shenfu coal pyrolysis** modeled with **ReaxFF molecular dynamics**. Conference abstracts summarize intended or preliminary results without the full experimental and computational detail expected of a journal article; accordingly, this page stays close to the abstract text and avoids inventing kinetic parameters or product distributions not stated in the source. The indexed conference PDF reports **Materials Studio 7.0** model building, **Forcite** optimization with **Dreiding**, then **ADF** **ReaxFF** pyrolysis MD (**HCONSB.ff**); the one-page abstract mentions a **1600–3000 K** ladder in **200 K** steps, while §2.2 lists isothermal **ReaxFF MD** temperatures **1400–2600 K** plus **NVT**/**Berendsen** settings—use the **PDF** if those levels disagree. **Pyrolysis–gas chromatography/mass spectrometry (Py–GC/MS)** experiments are said to validate simulated product trends. Coal structure is macromolecular and heterogeneous; atomistic models necessarily truncate complexity, so agreement statements in the abstract should be read as qualitative validation rather than exhaustive kinetic modeling.

## Methods

**1 — MD application (atomistic dynamics).** The conference PDF describes building a **Shenfu coal** macromolecular model in **Materials Studio 7.0**, **geometry optimization** with the **Forcite** module using the **Dreiding** force field for pre-relaxation, then import into **Amsterdam Modeling Suite / ADF** for **ReaxFF reactive MD** with parameter file **HCONSB.ff**. **Ensemble:** **NVT** for the reactive MD segment described in §2.2, with **Velocity Verlet** integration and an integration **timestep of 1.25 fs**; **Berendsen** thermostat (**0.1 ps** damping constant) for temperature control. **Temperatures:** isothermal runs are listed at **1400, 1600, 1800, 2000, 2200, 2400, and 2600 K** in the indexed text (the one-page abstract elsewhere in the file also mentions a **1600–3000 K** ladder in **200 K** steps—use the PDF for any discrepancy). **Duration / staging:** configurations are saved **every 200 ps**; the same paragraph notes subsequent **NVE** simulations at different temperatures to assess **energy conservation** and **pyrolysis products** (full per-temperature trajectory lengths in nanoseconds are not spelled out in the excerpt). **System size & composition:** elemental targets and **proximate analysis** for Shenfu coal are quoted in §2.2 (**wt %** ash/volatile/moisture/fixed carbon); **atom counts** for the final reactive cell are **not** enumerated in the indexed pages. **Boundaries / periodicity:** **N/A —** explicit **PBC** vs open-boundary treatment for the ReaxFF production cell is **not** stated on the indexed pages (confirm in the full PDF). **Barostat / pressure:** **N/A —** **NVT/NVE** protocol; no **NPT** or stress control reported. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** this contribution **uses** a published **ReaxFF** parameterization (**HCONSB.ff** named in the PDF) rather than reporting a new QM training or refit campaign.

**3 — Static QM / DFT-only.** **N/A —** **QM** is not described as the production engine for pyrolysis trajectories in the indexed excerpt.

**4 — Experiments (validation).** **Pyroprobe 5000** rapid pyrolysis with **DSQ GC/MS** (**EI** source, **473 K** source temperature, **70 eV** ionization) is described; pyrolysis heating rate is quoted as **10,000 K/s** in the indexed text, with additional chromatography settings partially truncated in the extract.

## Findings

**Outcomes / mechanisms.** The abstract and §2.2 report **qualitative agreement** between **simulated** lumped **pyrolysis product distributions** and **Py–GC/MS** measurements, and highlight **radicals** (**·OH**, **·H**, **·CH\(_3\)**) as important in the simulated chemistry. Figure captions in the excerpt reference **200 ps** snapshots for product-class histograms using **CPD-style** carbon-number lumping.

**Comparisons.** **Simulation vs Py–GC/MS** is framed as supporting that the **ReaxFF MD** workflow is “**real and reliable**” at the **qualitative** level stated in the abstract; the indexed excerpt does **not** give quantitative yield tables or error bars.

**Sensitivity / design levers.** **Temperature** is the primary lever explored across the listed isotherms; heating-rate effects in simulation are **not** detailed on the indexed pages.

**Limitations / outlook (as authored).** The indexed material is **conference-length**; readers needing **full cell construction**, **replicate statistics**, and **complete** chromatography parameters should use the **full PDF** or any **archival journal** follow-on.

**Corpus / PDF honesty.** This page is grounded in the **conference PDF** and `normalized/extracts/2017fa-venue-acam-2_p1-2.txt`; claims beyond those sources are not asserted here.

## Limitations

**Conference abstract** format; missing DOI in front matter; full methods and peer review status unknown from this file alone. Operators should upgrade confidence only after aligning with a full publication record. Pyrolysis product lists from abstract-only ingests should never be treated as exhaustive kinetic mechanisms.

## Relevance to group

Additional coal-pyrolysis plus ReaxFF datapoint within the Chinese Coal Abstracts bundle.

## Citations and evidence anchors

- No DOI in metadata; cite PDF path `papers/ReaxFF_others/Chinese_Coal_Abstracts/Investigation on pyrolysis mechanism of Shenfu coal based on ReaxFF force field.pdf`.

## Related topics

- [[reaxff-family]]
