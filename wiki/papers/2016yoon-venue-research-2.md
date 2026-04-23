---
id: paper:2016yoon-venue-research-2
type: paper
title: "Atomistic-scale simulations of defect formation in graphene under noble gas ion irradiation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.6b03036"
year: 2016
authors:
  - "Kichul Yoon"
  - "Ali Rahnamoun"
  - "Jacob L. Swett"
  - "Vighter Iberi"
  - "David A. Cullen"
  - "Ivan V. Vlassiouk"
  - "Alex Belianinov"
  - "Stephen Jesse"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: "ACS Nano"
pdf_sha256: "bd28b64be84347e141cbecbc50ac4dc3a3ed6b980f030175e4280add25ad26a3"
pdf_path: "papers/Yoon_ACSNano_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-research-2 -->

## Summary

This ingest tracks **`papers/Yoon_ACSNano_online.pdf`** for **Yoon et al.**, *ACS Nano*, **DOI `10.1021/acsnano.6b03036`**: **ReaxFF MD** of **noble-gas ion irradiation** of **graphene** with **annealing**, validated by **aberration-corrected STEM** and **HIM**. The article argues **dose**, **ion energy**, and **ion species** jointly set **defect motifs** and **vacancy coalescence** into **nanopores**, using nuclear-collision-focused MD that neglects **electronic stopping** with literature justification for **graphene**. This **online** PDF is a **duplicate corpus path** relative to the **VOR** record **`[[2016yoon-venue-nn6b03036]]`**.

## Methods

Same **DOI** as **`[[2016yoon-venue-nn6b03036]]`**. **LAMMPS** **ReaxFF** on **periodic** **graphene** **~52 × 40 Å²** (large **carbon atom** count in the published supercell) receives **25 keV** noble-gas impacts in **~30 × 20 Å²**. **NVE** cores use **0.005–0.02 fs** **timesteps**; **edge** regions stay at **300 K** via **thermostat** coupling described in the article. **Dose rates** space successive cascades. **He\(^+\)** series use **1500 K / 25 ps** then **2000 K / 1.25 ns** **annealing**; heavier ions add **1500 K** plus **3000 K** **annealing** (the **3000 K** segment **duration** is **not** recovered from the Methods text checked here). **Barostat**, **electric fields**, and **replica / enhanced sampling** are **not** used on these irradiation legs. **Hydrostatic pressure** is **not** servo-controlled on these legs (**N/A —** fixed-area **NVE** core; no **NPT** **pressure** target in the summarized protocol). **HIM** and **60 kV STEM** protocols sit under **Experimental methods and details**.

## Findings

**Annealing** after cumulative impacts drives **vacancy coalescence** into **nanopores** with strong **dose** and **ion-mass** sensitivity, i.e. heavier ions and higher dose trend toward larger pores and more surrounding disorder in the simulations. **STEM** **experiment** comparisons show broadly consistent **dose** trends while the text flags **impurities**, **contamination**, and **metal-catalyzed** edge chemistry as **limitations** on one-to-one agreement. **Sensitivity** to **dose rate** (simulated vs experimental beam schedules) is discussed as an authored **caveat**, alongside **model** uncertainty in the reactive **MD** treatment. Defect statistics (**STW** vs **monovacancy** prevalence by ion species) and sputtering-style metrics are reported in the article relative to prior **literature** benchmarks. For **pagination** and figure-level claims, prefer the **version-of-record** PDF **`[[2016yoon-venue-nn6b03036]]`** over this duplicate **`pdf_path`**.

## Limitations

Prefer **`[[2016yoon-venue-nn6b03036]]`** for **pagination** when citing the **VOR** PDF; duplicate corpus PDFs can differ in pagination. Electronic stopping and electronic excitation are neglected in the nuclear-collision framing described in the opening pages—consistent with cited precedents for **graphene** but not universally valid for all **2D** materials.

## Relevance to group

**van Duin** collaboration with **ORNL** on **2D carbon** **radiation** effects.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acsnano.6b03036` (`papers/Yoon_ACSNano_online.pdf`).

## Related topics

- [[reaxff-family]]
