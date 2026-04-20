---
id: paper:2018yang-j-phys-chem-enabling-computational
type: paper
title: "Enabling Computational Design of ZIFs Using ReaxFF"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - material:zeolite-porous
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.8b08094"
year: 2018
authors:
  - "Yongjian Yang"
  - "Yun Kyung Shin"
  - "Shichun Li"
  - "Thomas D. Bennett"
  - "Adri C. T. van Duin"
  - "John C. Mauro"
venue: "J. Phys. Chem. B 2018, 122, 9616–9624"
pdf_sha256: "19f06853f13174da01e0dad19f8f1da2975be5428325fa389bb1e9ad13428435"
pdf_path: "papers/Yang_ZIF_JPC_B_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018yang-j-phys-chem-enabling-computational -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Zeolitic imidazolate frameworks (ZIFs) increasingly require simulations that handle **bond breaking/forming** (melts, defects, chemical stability), beyond classical nonreactive FF applications. This paper demonstrates ReaxFF on representative ZIFs: melt–quench of ZIF-4 reproduces glassy **aZIF-4** structure, density, thermal response, and pore morphology consistent with experiment and ab initio MD; ZIF-62 melting highlights ligand chemistry (benzimidazolate) effects on melting trends; ZIF-77 with electron-withdrawing substituents illustrates how electronic/steric balance shifts predicted melting and chemical stability. The overarching claim is that ReaxFF’s cost and transferability can support computational screening of disordered and defect-laden ZIF behavior.

## Methods

- **Reactive MD:** ReaxFF simulations of heating, melting, and quench protocols for ZIF crystals.
- **Comparison:** Experimental observables and first-principles MD references where available.

## Findings

- Qualitative/quantitative agreement for glass formation properties for ZIF-4 glass from melt–quench.
- Mechanistic insight into substituent effects on melting and stability across ZIF chemistries.

## Limitations

- Transferability across full ZIF chemical space still requires validation per family; reactive FF accuracy for complex organometallic linkers must be checked against higher-level benchmarks.

## Relevance to group

Key **MOF/ZIF + ReaxFF** capability demonstration from the van Duin and Mauro collaboration—important for porous framework entries in the wiki.

## Reader notes (navigation)

- **Cluster:** [[theme-porous-mof-zeolite]] — **ZIF1** gold in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcb.8b08094](https://doi.org/10.1021/acs.jpcb.8b08094)
- Abstract: `normalized/extracts/2018yang-j-phys-chem-enabling-computational_p1-2.txt`

## Related topics

- [[reaxff-family]]
- ZIF glasses and melt–quench reactive MD
- Metal–organic frameworks beyond fixed-bond force fields
