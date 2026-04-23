---
id: paper:2018confined-water-diele-venue-science-journals
type: paper
title: "Anomalously low dielectric constant of confined water"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:hexagonal-boron-nitride
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1126/science.aat4191"
year: 2018
authors:
  - "L. Fumagalli"
  - "A. Esfandiar"
  - "R. Fabregas"
  - "S. Hu"
  - "P. Ares"
  - "A. Janardanan"
  - "Q. Yang"
  - "B. Radha"
  - "T. Taniguchi"
  - "K. Watanabe"
  - "G. Gomila"
  - "K. S. Novoselov"
  - "A. K. Geim"
venue: "Science 360(6395), 1339–1342 (2018)"
pdf_sha256: "dcf20afc3e5a521f22df26fd2f6c37215ca14b1fe87cf4324bdf9f0b62a8e7ff"
pdf_path: "papers/Others/Confined.Water.Dielectric.Constant.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018confined-water-diele-venue-science-journals -->

## Summary

**Nanocapacitance microscopy** measures the **out-of-plane dielectric constant** **ε⊥** of **water** confined in **slit channels** between **atomically flat** **graphite** and **hexagonal boron nitride (hBN)** walls for **heights** down to **~1 nm**, revealing an **interfacial** “**electrically dead**” layer with **ε⊥ ~ 2** extending **two–three molecular layers**, much weaker than **bulk water (~80)** and stronger than many **MD** predictions. The **Science** report is **experimental** **nanoelectrostatics** on **water** under **extreme** **confinement**, with direct implications for **electrolyte** **models** that assume **bulk** **dielectric** **response** near **walls**.

## Methods

Experimental **Science** report (`pdf_path`); no atomistic MD in this paper.

- **Device:** **vdW** stack: **graphite** ground electrode, **hBN** side walls + spacers, top **hBN** lid, on a **SiN** membrane window; **water** back-filled into slit channels (**Fig. 1**). Channel **width ~200 nm** (figure caption); **h** varied across devices (e.g. **~1.4 nm**, **~3.8 nm**, **~10 nm** examples in **Fig. 2**).
- **Metrology:** **AFM** **dC/dz** (**capacitance gradient**) imaging; **tip bias** e.g. **4 V** at **1 kHz** (other voltages/frequencies including **300 Hz** reported as similar); **commercial** cantilevers, **tip radius ~100-200 nm** for sensitivity; tip in **dry N2**. **epsilon_perp** extracted by matching measured **dC/dz** to a **3D electrostatic** model of the tip+device geometry (**Fig. 2H**, **figs. S3-S4**); fit gives e.g. **epsilon_perp ~ 15.5 / 4.4 / 2.3** for the three illustrated **h** values. **>40** devices with **h ~ 1-300 nm** summarized in **Fig. 3**; bulk-like **epsilon_perp ~ 80** only for **~100 nm** water thickness in their geometry.

**Materials** **stack** **fabrication**, **channel** **fill** **procedure**, and **finite-element** **electrostatic** **mesh** **details** appear in `papers/Others/Confined.Water.Dielectric.Constant.pdf` and **supplementary** sections referenced therein.

## Findings

- **ε⊥** of confined water **depends strongly on h**, trending toward **bulk-like** response only at larger separations; for **few-nm** confinement, **ε⊥** can fall **below** **hBN**’s own **ε⊥**, giving **unambiguous** contrast.
- An **interfacial layer** with **vanishingly small polarization** yields **ε⊥ ~ 2** (order-of-magnitude **10×** weaker than common **MD** estimates that still struggle with **bulk water ε**).
- The **dead layer** thickness is **2–3 water molecules**, providing experimental bounds for **electrostatic** models of **interfacial water**.

The **authors** contrast their **measured** **ε⊥** **trends** with **common** **MD** **estimates**, arguing that **interfacial** **suppression** of **polarization** fluctuations is **larger** than many **simulation** **studies** had assumed for **nm-scale** **slits**.

## Limitations

- **Frequency** window and **ion** screening effects follow the article’s measurement caveats; not a **ReaxFF** / atomistic simulation study.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Related topics

- [[theme-water-silica-geo]]
- [[2018c-ulises-gonzalez-va-j-phys-chem-investigation-wetting]]
