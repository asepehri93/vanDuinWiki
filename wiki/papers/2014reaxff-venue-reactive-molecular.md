---
id: paper:2014reaxff-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulations for a better insight in plasma medicine"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:aimd
candidate_tags: []
source_refs: []
doi: "10.1002/ppap.201400084"
year: 2014
authors:
  - "Annemie Bogaerts"
  - "Maksudbek Yusupov"
  - "Jonas Van der Paal"
  - "Christof C. W. Verlackt"
  - "Erik C. Neyts"
venue: "Plasma Processes and Polymers"
pdf_sha256: "140f48558daeb79d65df8f5a7181ebdd5ef35a7d073d98f1fbc0a5c350fffe60"
pdf_path: "papers/ReaxFF_others/ReaxFF_lipids_plasma_Neyts_coworkers_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014reaxff-venue-reactive-molecular -->

!!! abstract "Review-style overview of reactive MD (including ReaxFF examples) for plasma–biomolecule interactions: ROS with bacterial cell envelopes, skin lipids, and species transport into aqueous/biofilm-like water layers, plus outlook on cancer-relevant modeling."

## Summary

This **review** surveys how **reactive molecular dynamics** simulations—often employing **ReaxFF** for bond-making/breaking chemistry—can inform **plasma medicine** mechanisms at the **atomic scale**. Representative topics summarized in the abstract include interactions of **reactive oxygen species** from plasmas with **gram-positive and gram-negative bacterial cell-wall** motifs, interactions with **skin lipids**, and the role of **liquid water / biofilm-like aqueous environments** in modulating species transport and reaction.

The paper closes with a forward-looking discussion of **atomic-scale modeling** opportunities in plasma medicine, including **oncology**-related contexts, as framed by the authors.

## Methods

**Local sources:** the PDF at `papers/ReaxFF_others/ReaxFF_lipids_plasma_Neyts_coworkers_2014.pdf` is present in this workspace; opening pages are captured in `normalized/extracts/2014reaxff-venue-reactive-molecular_p1-2.txt`.

This is a **review** in *Plasma Processes and Polymers* (DOI **10.1002/ppap.201400084**). The article **surveys modeling approaches** spanning **macroscopic** reaction–diffusion and penetration treatments of plasma–surface coupling (including reactive transport across gas–liquid boundaries, with examples such as Babaeva and co-workers’ dielectric-tissue models coupling Poisson and conservation equations) and **atomic-scale** methods, contrasting **ab initio Car–Parrinello MD** (accurate but limited to \(\sim\)100 atoms / ps-scale) with **classical MD** (typically \(10^3\)–\(10^5\) atoms and \(10^{-2}\)–\(10^5\) ps depending on the force field). It explains why **nonreactive classical MD** cannot capture **bond-making/breaking** chemistry of plasma species with biomolecules, motivating **reactive MD** when mechanisms are unknown *a priori*. Within reactive classical frameworks relevant to the review’s examples, it highlights **ReaxFF** and the **Brenner** reactive potential as the reactive force fields applied in plasma-medicine-related simulation literature cited in the article (including the group’s own ROS–peptidoglycan, lipid A, and skin-lipid studies).

## Findings

The review argues that **reactive molecular dynamics** can provide **mechanistic detail** for plasma–biomolecule interactions that are hard to resolve **in situ** experimentally, while acknowledging that outcomes are **force-field-dependent**. Representative threads summarized early in the paper include **reactive oxygen species** interacting with **gram-positive** cell-wall motifs (**peptidoglycan**) and **gram-negative** motifs (**lipid A**), **skin lipids**, and the importance of **liquid water / biofilm-like aqueous environments** for transport and reaction. The paper also sketches a **forward-looking** perspective for **atomic-scale** modeling in **plasma medicine**, including **oncology**-related directions, as framed by the authors.

## Limitations

- As a review, **quantitative claims** should be traced to the **original primary studies** it cites.
- Biological complexity exceeds any single force field’s domain of validity; conclusions are necessarily **model-dependent**.

## Relevance to group

Useful as a **cross-application** pointer for **ReaxFF** in **plasma–surface biochemistry**, adjacent to the corpus’s more materials-focused reactive MD work.

## Citations and evidence anchors

- DOI: [10.1002/ppap.201400084](https://doi.org/10.1002/ppap.201400084)
