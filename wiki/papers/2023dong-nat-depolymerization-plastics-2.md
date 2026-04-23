---
id: paper:2023dong-nat-depolymerization-plastics-2
type: paper
title: "Depolymerization of plastics by means of electrified spatiotemporal heating (duplicate PDF registration)"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1038/s41586-023-05845-8"
year: 2023
authors:
  - "Qi Dong"
venue: "Nature"
pdf_sha256: "307683b8ce1ce63a998813cc415de5fc747be507c6fdcbef3b02c0c07881c3f9"
pdf_path: "papers/ReaxFF_others/Dong_Lele_plastic_depoly_Nature_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023dong-nat-depolymerization-plastics-2 -->

## Evidence and attribution

!!! note "Duplicate bytes"

    **`pdf_sha256`** matches **`paper:2023dong-nat-depolymerization-plastics`**; only **`pdf_path`** differs (`papers/ReaxFF_others/Dong_Lele_plastic_depoly_Nature_2023.pdf` vs `papers/ReaxFF_others/Dong_Lele_Nature_depolymerization_2023.pdf`). Narrative below is duplicated for reader convenience; long-term maintenance may consolidate to one canonical path.

## Summary

This *Nature* article (also summarized on **`[[2023dong-nat-depolymerization-plastics]]`**) reports **catalyst-free** thermochemical **depolymerization** of commodity **polypropylene (PP)** and **poly(ethylene terephthalate) (PET)** using **electrified spatiotemporal heating (STH)**. The core idea is to combine a **sharp spatial temperature gradient** through a **bilayer porous carbon felt** stack with a **pulsed** temporal heating profile that reaches high peak temperatures for short intervals, aiming to favor **monomer-forming** chemistries over slower equilibrium routes that produce more **cracked** and **aromatized** side products. This wiki slug exists because the corpus stores an alternate **filename** for the **same SHA-256** bytes. Scientifically, the article is unchanged from **`[[2023dong-nat-depolymerization-plastics]]`**: **catalyst-free** **STH** depolymerization of **PP** and **PET** using a **bilayer porous carbon felt** reactor with **spatial** **T** gradients and **pulsed** electrical heating, reporting **~36%** and **~43%** **monomer** yields respectively in the abstract accounting.

## Methods

### Duplicate-ingest note

**`pdf_sha256`** matches **`[[2023dong-nat-depolymerization-plastics]]`**; only **`pdf_path`** differs. Protocol text below mirrors the primary page for reader convenience.

### STH reactor (experimental)

**Bilayer porous carbon felt** stack over a **plastic** reservoir in a **~10.5 mm** **quartz** tube with **Ar** carrier gas; **spatial** **T** gradient couples **melt/wick/vaporize/react**; **pulsed** heating hits peaks ~**600 °C** (**PP** discussion) / ~**1050 °C** (**PET** schematic) with short **on** pulses (example **0.11 s on / 0.99 s off**).

### Analytics

**Effluent**-based **yield**/**selectivity** metrics per *Nature* **Methods**/**Extended Data**. The main text motivates **STH** as **far-from-equilibrium** pyrolysis: **short** high-temperature transients (example **~0.11 s** on-times paired with **~600 °C** peak discussion for **PP** in the abstract) are intended to enable **depolymerization** while limiting side reactions that dominate under **long** **isothermal** pyrolysis.

## Findings

**PP → propylene ~36%** and **PET → terephthalic-acid monomer ~43%** (authors’ accounting), framed vs **conventional pyrolysis** baselines in the article; **electricity**/**CO₂** discussion appears in supporting analysis.

**Mechanism (as reported):** **STH** couples a **bilayer** **porous** **carbon** **felt** **stack** with **pulsed** **Joule** **heating** so **plastic** **melt**/**wick**/**vaporize**/**react** along a **spatial** **T** gradient while **short** high-**T** **pulses** (example **~0.11 s** on at **~600 °C** for **PP** in the abstract discussion) limit time-at-temperature routes that drive **deep** **cracking**/**aromatization**. **Sensitivity:** **monomer** **yield** is **expected** to track **pulse** **program**, **felt** **geometry**, and **feed**—**not** re-quantified on this **duplicate** page.

**Comparisons:** **catalyst-free** **STH** **monomer** **yields** are **contrasted** with **conventional** **pyrolysis** in the **Nature** text. **No new claims** vs **`[[2023dong-nat-depolymerization-plastics]]`**—use one **wiki** page for **reader-facing** prose to avoid duplicate **chunks**. **Limitations & outlook (authored):** **scale-up**, **feed** **variability**, and **collection**/**sorting** remain **open** **engineering** questions beyond the **lab** **demonstration**; **however** the **article** still positions **STH** as a **lever** for **waste** **plastics** **valorization** when **renewable** **electricity** is available.

**Index hygiene:** downstream **retrieval** jobs should **deduplicate** by **DOI** and prefer **`paper:2023dong-nat-depolymerization-plastics`** for **canonical** **chunks**, keeping this slug only when **manifest** **hash** provenance requires the alternate **`pdf_path`**. **Corpus honesty:** same **content** as **`[[2023dong-nat-depolymerization-plastics]]`**.

## Limitations

Yields depend on the specific pulse programme and reactor geometry; scale-up and feed variability require engineering validation. Automation pipelines should treat the two `pdf_path` values as **identical content** unless the manifest changes.

## Relevance to group

**Provenance** duplicate for a **Lele**-linked **Nature** plastics **STH** article tracked in this corpus.

## Citations and evidence anchors

- DOI: [10.1038/s41586-023-05845-8](https://doi.org/10.1038/s41586-023-05845-8)

## Related topics

- [[2023dong-nat-depolymerization-plastics]]
