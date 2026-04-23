---
id: paper:2017mishra-venue-paper
type: paper
title: "CEMFF: A force field database for cementitious materials including validations, applications and opportunities"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:cement-mineral
  - domain:methods-software
  - domain:classical-ff-specialized
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cemconres.2017.09.003"
year: 2017
authors:
  - "Ratan K. Mishra"
  - "Aslam Kunhi Mohamed"
  - "David Geissbühler"
  - "Hegoi Manzano"
  - "Tariq Jamil"
  - "Rouzbeh Shahsavari"
  - "Andrey G. Kalinichev"
  - "Sandra Galmarini"
  - "Lei Tao"
  - "Hendrik Heinz"
  - "Roland Pellenq"
  - "Adri C. T. van Duin"
  - "Stephen C. Parker"
  - "Robert J. Flatt"
  - "Paul Bowen"
venue: "Cem. Concr. Res."
pdf_sha256: "1ffdcf7f36ca57fd7ed4657e8bf90ec9c6893c9ae64d9c0fec82b91bdee979e1"
pdf_path: "papers/Mishra_CEMFF_proof_2017.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017mishra-venue-paper -->

## Summary

Atomistic simulations of **cementitious** materials—**C–S–H**, **portlandite**, **C\(_3\)S**, and related phases—are scattered across dozens of **force-field** families with inconsistent validation. This **Cement and Concrete Research** review introduces **CEMFF**, a web database cataloging **atomistic potentials** applied to cementitious minerals, summarizing **functional forms**, **benchmarks**, and **validation** against **experiment** and **quantum** references for each entry. The scope spans **Born–Mayer–Huggins**, **ClayFF**, **IFF**, **ReaxFF**, **UFF**, and specialized cement parameterizations. **Adri C. T. van Duin** coauthors alongside an international consortium, positioning **reactive** options where **bond-making/breaking** is essential. The local **`pdf_path`** is a **proof** PDF; confirm pagination against the **final** issue when citing page-level details.

## Methods

**Force-field training / fitting.** Same **cementitious force-field survey** as **`[[2017mishra-cement-and-c-cemff-force]]`** (**DOI 10.1016/j.cemconres.2017.09.003**); this slug tracks **proof** PDF bytes only.

**MD application (atomistic dynamics).** **Literature-level** summary of how surveyed groups run **classical** and **reactive MD** for **cement** phases; **no** new unified **MD** dataset accompanies the review text.

**Static QM / DFT.** **DFT** and broader **QM** benchmarks appear as **reference** data in the surveyed **fitting** stories summarized in the tables.

**Review / database framing.** **CEMFF** registry narrative (**http://cemff.epfl.ch**) plus **community upload** guidance; **prefer `[[2017mishra-cement-and-c-cemff-force]]`** when citing **VOR** pagination. The abstract inventories **Born–Mayer–Huggins**, **IFF**, **ClayFF**, **C–S–H FF**, **CementFF**, **GULP**-style ionics, **ReaxFF**, and **UFF** as representative families applied to **C₃S**, **portlandite**, and **C–S–H** models.

## Findings

The review highlights **diversity** of force-field choices and **validation gaps** when moving potentials between **chemistries**, **water models**, and **interface** configurations. It explicitly positions **ReaxFF** among options when **reactive** chemistry cannot be neglected, while warning that **reactive** cost and training scope must match the modeling question. The overarching message is **pragmatic**: practitioners need **property-targeted** selection guidance rather than a single universal cement force field. For knowledge-base maintenance, treat **CEMFF** as a living inventory: when new cementitious parameterizations appear in the literature, the database entry (not this static article alone) may update faster than the review text, so verify current entries at the EPFL site when planning simulations.

## Limitations

**Proof** ingest may differ in layout from the final article; the **database** evolves independently of the paper’s static snapshot.

## Reader notes (MAS / retrieval)

Database-first queries should still verify **CEMFF** entries at the live site; treat this review as narrative context, not a live parameter dump.

## Relevance to group

Situates **van Duin** **reactive** cement-related developments within community-wide **FF** governance and tooling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.cemconres.2017.09.003` (`papers/Mishra_CEMFF_proof_2017.pdf`).

## Related topics

- [[reaxff-family]]
