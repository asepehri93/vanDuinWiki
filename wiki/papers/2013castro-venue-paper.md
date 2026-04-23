---
id: paper:2013castro-venue-paper
type: paper
title: "Comparison of thermal and catalytic cracking of 1-heptene from ReaxFF reactive molecular dynamics simulations (author manuscript PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:combustion
source_refs: []
doi: "10.1016/j.combustflame.2012.12.007"
year: 2013
authors:
  - "Castro-Marcano, Fidel"
  - "van Duin, Adri C. T."
venue: "Combustion and Flame"
pdf_sha256: "9cc986f8906547b2305b27c2af55695539cb2399679eceda1e3e23b69eb9d184"
pdf_path: "papers/Castro_CombFlame_heptene_2013.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013castro-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This corpus PDF is an **Elsevier author’s personal copy** with repository/copyright banner pages; extraction quality is **partial**. Prefer the **journal version-of-record** for stable pagination.

## Summary

This slug tracks an **Elsevier author’s personal copy** (repository/copyright banners) of the Castro–van Duin **Combustion and Flame** article: **ReaxFF** reactive MD comparing **thermal** versus **catalytic** **1-heptene** cracking on **amorphous silica**, **hydrated silica**, and **aluminosilicate** interfaces at **1750–1950 K**. The primary curated narrative and stable pagination sit on [[2013castro-marcano-combustion-a-comparison-thermal]]. Scientifically, the paper targets **aviation-relevant** **hydrocarbon** **pyrolysis** in contact with **acidic** **oxide** surfaces—contrasting **gas-phase**-like **thermal** cracking with **surface-mediated** routes that matter for **catalytic** combustors and **soot** precursor chemistry (article framing; sibling page).

## Methods

- **ReaxFF** in **LAMMPS** with the **hydrocarbon/silica** parameter line cited in the paper; **~45 Å** cubic cells under **three-dimensional periodic boundary conditions** (**PBC**) at **0.2–0.3 g/cm³** with **100** **1-heptene** molecules plus an **oxide** nanoparticle (**~2250 atoms** total); **0.25 fs** integration, **Berendsen** thermostat (**τ = 100 fs**), staged heating then **5000 ps** **NVT** production at **1750**, **1850**, and **1950 K** (full table on [[2013castro-marcano-combustion-a-comparison-thermal]]).
- **Barostat / pressure coupling:** **N/A** — production segments summarized here are **NVT** **molecular dynamics** without a Parrinello–Rahman **barostat**; initial density is set by the **cubic** cell construction rather than a constant **GPa** target during production.
- **This PDF:** same article text with **banner** pages; `extraction_quality: partial`.
- **Observables:** **species** inventories and **reaction** **pathways** are extracted from **bond-order**-based **ReaxFF** output to classify **C–C** scission vs **surface** **H-transfer** events as a function of **oxide** composition and **temperature** (see sibling page for figure pointers).

## Findings

- Cracking yields **H₂** and a distribution of **C₁–C₇** fragments through a **dense reaction network**; **thermal** paths emphasize **C–C scission** and **radical** propagation, while **catalytic** paths add **protonation/dehydrogenation**-like events at **oxide** surfaces (see [[2013castro-marcano-combustion-a-comparison-thermal]]).
- **Comparative readout:** **Brønsted** **acidity** and **water** content on **aluminosilicate** motifs shift the **branching** between **gas-like** products and **oxygenated**/**surface-bound** intermediates relative to **dry silica** scenarios (article emphasis; sibling page).
- **Comparisons:** The article frames product families against **experimental** hydrocarbon **cracking** **literature** at a qualitative level (see sibling VOR page for citations).
- **Sensitivity:** Reported **mechanistic** differences track **temperature** (**1750–1950 K**) and **oxide** composition (**silica** vs hydrated vs **aluminosilicate**) as primary **levers**.
- **Limitations & outlook:** **Banner** PDFs and **partial** extraction motivate caution for automated pipelines; authors acknowledge **elevated** **temperature** and **empirical** reactive parameters when discussing quantitative agreement with **experiment** (see **Limitations** below and VOR page).
- **Corpus honesty:** This slug tracks **`papers/Castro_CombFlame_heptene_2013.pdf`** (author personal copy bytes); prefer **`[[2013castro-marcano-combustion-a-comparison-thermal]]`** for **version-of-record** pagination and **`[[2013castro-marcano-combustion-a-comparison-thermal-2]]`** for the Elsevier **proof** lineage when provenance matters.

## Limitations

**Banner** pages and non-VOR layout hinder automated extraction; **elevated T** and **empirical** reactive parameters limit quantitative **product** agreement with experiment.

For **literature** citations, prefer **`[[2013castro-marcano-combustion-a-comparison-thermal]]`** for stable **pagination**; use this slug only when **provenance** must reference **`papers/Castro_CombFlame_heptene_2013.pdf`** bytes specifically.

**Operator note:** if **banner** text ever pollutes **extracts**, strip it before **automated** **snippet** **pipelines**; the science lives in the **same** **DOI** as the **VOR** entry above.

## Relevance to group

**van Duin** co-authorship on **aviation-fuel-relevant** **ReaxFF** cracking; this entry records **alternate** corpus bytes only.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2012.12.007](https://doi.org/10.1016/j.combustflame.2012.12.007) — this artifact: `papers/Castro_CombFlame_heptene_2013.pdf`.

## Reader notes (navigation)

- **Online / VOR-style PDF:** [[2013castro-marcano-combustion-a-comparison-thermal]]; **author proof:** [[2013castro-marcano-combustion-a-comparison-thermal-2]].

## Related topics

- [[2013castro-marcano-combustion-a-comparison-thermal]]
- [[theme-pyrolysis-combustion-organics]]
