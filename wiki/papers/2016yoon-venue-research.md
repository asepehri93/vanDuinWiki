---
id: paper:2016yoon-venue-research
type: paper
title: "Atomistic-scale simulations of defect formation in graphene under noble gas ion irradiation"
updated: "2026-04-20"
confidence: med
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
pdf_sha256: "5cf532af2878515f977c91ded813a61cabebc381cd63375b39072025d58e2db4"
pdf_path: "papers/Yoon_ACSNano_galley_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-research -->

## Summary

**Ion irradiation** is used to engineer **defects** and **nanopores** in **graphene** for separations and electronics, but linking **beam parameters** to **atomic defect** populations requires joint **simulation** and **microscopy**. This **ACS Nano** article uses **ReaxFF molecular dynamics** to simulate **noble gas ion** bombardment of **graphene** followed by **annealing**, correlating **ion species**, **energy**, and **dose** with **defect** classes and **pore** formation. Experimental collaborators provide **aberration-corrected STEM** and **helium ion microscopy** benchmarks that the paper uses to test whether simulations capture **dose-dependent** damage evolution and **morphology** trends. **Adri C. T. van Duin** coauthors the ORNL–PSU collaboration line on **reactive nanocarbon** mechanics. **Corpus note:** this slug registers the **galley/proof** PDF bytes; the canonical in-corpus **version-of-record** article PDF is **[[2016yoon-venue-nn6b03036]]** (`papers/Yoon_ACSNano_2016.pdf`). This galley ingest is listed in the maintainer catalog: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md). Scientifically, the study targets the coupling between **ion mass**, **dose**, and **defect identity**: **He\(^+\)**-like conditions emphasize one family of **reconstruction** defects, while heavier ions drive different **vacancy** populations and **amorphization** thresholds. Pairing **ReaxFF** with **microscopy** is meant to keep simulated **defect statistics** tied to observables used in the **nanocarbon** experimental literature, rather than reporting chemistry-only metrics with no imaging counterpart. The work is also a useful reminder that **beam** parameters are not just a **dose** knob: they change which **defect classes** dominate, which matters for downstream **etching** and **transport** applications of irradiated **graphene**. See the VOR page for figures.

## Methods

This slug registers the **galley/proof** bytes (`papers/Yoon_ACSNano_galley_proof.pdf`); protocols match **DOI `10.1021/acsnano.6b03036`** and align with **`[[2016yoon-venue-paper]]`** / **`[[2016yoon-venue-nn6b03036]]`**. **ReaxFF** reactive **MD** in **LAMMPS** treats **periodic** **graphene** about **52 × 40 Å²** (thousands of **carbon atoms**) with **25 keV He\(^+\)/Ne\(^+\)/Ar\(^+\)/Kr\(^+\)** impacts in a **~30 × 20 Å²** window. **PBC** apply in-plane; **NVE** in the cascade core pairs with **300 K** edge regions coupled via a **Nosé–Hoover thermostat** on **edge** sink atoms. **Hydrostatic pressure** is **not** servo-controlled on these legs (**N/A —** fixed-area **NVE** impact core; no **NPT** **pressure** target in the summarized protocol). Species-dependent **timesteps** **0.005–0.02 fs** bracket successive impacts separated by engineered **dose rates**. **He\(^+\)** trajectories add **1500 K / 25 ps** then **2000 K / 1.25 ns** **annealing** after dose steps; heavier ions add **1500 K** plus **3000 K** **annealing** (the **3000 K** segment **duration** is **not** recovered from the Methods text checked here). **Barostat**, **electric fields**, and **replica / enhanced sampling** are **not** used on these constant-area irradiation legs. **HIM** and **60 kV STEM** appear under **Experimental methods and details**. For stable pagination cite **`[[2016yoon-venue-nn6b03036]]`**.

## Findings

Simulations plus microscopy describe **dose-dependent** **nanopore** growth **qualitatively consistent** with **experiment**, while noting **Ne\(^+\)** cases where simulated pores stay **smaller** than **STEM** suggests. **Ion dose**, **ion mass**, and **annealing temperature** are the main **sensitivity** knobs. **Vacancy coalescence**, **amorphization**, and **STW** versus **monovacancy** statistics come from trajectory analysis compared to images. The authors cite **dose-rate** mismatch, **impurity** / **contamination** / **metal-catalyzed** edge chemistry, and **model** uncertainty as limitations.

## Limitations

This **galley/proof** path can differ cosmetically from the **version-of-record** **`[[2016yoon-venue-nn6b03036]]`** for pagination and figure layout; take quantitative values from the **VOR** PDF and DOI-resolved publisher copy when possible.

## Relevance to group

Alternate corpus path for the **van Duin** / **ORNL** **graphene ion irradiation** article.

## Citations and evidence anchors

- **DOI:** [10.1021/acsnano.6b03036](https://doi.org/10.1021/acsnano.6b03036) — galley: `papers/Yoon_ACSNano_galley_proof.pdf`; VOR: `papers/Yoon_ACSNano_2016.pdf`.

## Related topics

- [[2016yoon-venue-nn6b03036]]
- [[reaxff-family]]
