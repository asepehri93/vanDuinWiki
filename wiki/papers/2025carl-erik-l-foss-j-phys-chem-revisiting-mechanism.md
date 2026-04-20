---
id: paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism
type: paper
title: "Revisiting Mechanism of Silicon Degradation in Li-Ion Batteries: Effect of Delithiation Examined by Microscopy Combined with ReaxFF"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.4c03620"
year: 2025
authors:
  - "Carl Erik L. Foss"
  - "Mahdi K. Talkhoncheh"
  - "Asbjørn Ulvestad"
  - "Hanne F. Andersen"
  - "Per Erik Vullum"
  - "Nils Peter Wagner"
  - "Kenneth Friestad"
  - "Alexey Y. Koposov"
  - "Adri van Duin"
  - "Jan Petter Mæhlen"
venue: "J. Phys. Chem. Lett. 2025, 16, 2238–2244"
pdf_sha256: "788d1647367c38c65d2ef3109e1f40f275699c461cabed3fe5544d70b24d393d"
pdf_path: "papers/Foss_JPCL_2025_Si_battery.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Combining electron microscopy of cycled Si electrodes with ReaxFF modeling, this Letter argues that **delithiation**—not only lithiation-driven fracture—plays a major role in Si anode degradation. Micrographs show substantial morphological evolution and Si redistribution, including Si-rich features within the SEI, interpreted as Si migration during cycling. Reactive MD supports a picture in which delithiation steps drive much of this reorganization, so particle cracking is not the sole degradation mode; prolonged cycling dramatically alters Si surfaces and can produce Si dendrite-like structures embedded in SEI.

## Methods

- **Experiment:** Microscopy-focused characterization of Si electrode components under electrochemical cycling (delithiation emphasis in interpretation).
- **Simulation:** ReaxFF molecular dynamics to probe atomistic processes consistent with observed morphological changes (details in main text and SI).

## Findings

- Degradation mechanisms discussed in the literature often center lithiation stress and cracking; this work highlights experimental evidence for ongoing morphological change where **delithiation** is implicated as a dominant driver of Si migration and SEI-embedded Si structures.
- Reframes design considerations for Si anodes toward models that treat **reversed** electrochemical steps and interfacial chemistry more explicitly.

## Limitations

- Complex electrode microstructures and long-time cycling chemistry challenge direct one-to-one mapping from finite MD to device-scale behavior; microscopy provides mesoscale context that simulations complement rather than fully replicate.

## Relevance to group

Strong **battery + ReaxFF** integration paper with van Duin co-authorship—useful anchor for Si anode SEI and (de)lithiation chemistry in the wiki.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.4c03620](https://doi.org/10.1021/acs.jpclett.4c03620)
- Abstract and introduction: `normalized/extracts/2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism_p1-2.txt`

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
- Silicon anodes, SEI, and reactive modeling of lithiation/delithiation
- Coupled experiment–ReaxFF workflows for electrochemical interfaces
