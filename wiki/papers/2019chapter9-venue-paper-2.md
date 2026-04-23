---
id: paper:2019chapter9-venue-paper-2
type: paper
title: "Molecular dynamics simulations of MXenes: ab initio, reactive, and non-reactive empirical force fields"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - material:tmd
  - method:reaxff
  - method:classical-md
  - method:aimd
  - task:review
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:batteries-interfaces
source_refs: []
doi: "10.1007/978-3-030-19026-2_9"
year: 2019
authors:
  - "Roghayyeh Lotfi"
  - "Dundar E. Yilmaz"
  - "Lukas Vlcek"
  - "Adri van Duin"
venue: "In: 2D Metal Carbides and Nitrides (MXenes), Springer (2019)"
pdf_sha256: "01e3a3871993145a7a141b0445c8897dfe69e5501b40d27ddf35f767d57f8dbd"
pdf_path: "papers/Chapter9_MXenes Book_Final_Sept2019.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2019chapter9-venue-paper-2 -->

## Summary

This wiki slug is an alternate ingest of **Springer** book chapter **9** in *2D Metal Carbides and Nitrides (MXenes)* (**[DOI 10.1007/978-3-030-19026-2_9](https://doi.org/10.1007/978-3-030-19026-2_9)**), tracking the PDF filename **`papers/Chapter9_MXenes Book_Final_Sept2019.pdf`**. The chapter is a methods-oriented **review** of how **molecular dynamics** at different fidelity levels—**ab initio MD (AIMD)**, **ReaxFF reactive MD**, and **non-reactive classical** force fields—has been applied to **MXenes** in problems spanning **energy storage**, **adsorption/intercalation**, **catalysis**, **exfoliation**, and **water-related** interfacial chemistry. Scientific content matches **`[[2019chapter9-venue-paper]]`**; the duplication exists for manifest provenance when multiple PDF filenames refer to the same chapter text.

## Methods

As a review, the chapter organizes the literature by **simulation cost** versus **chemical explicitness**: **AIMD** for short-time validation of local structures, reaction barriers, and stability windows; **ReaxFF** for bond-making and bond-breaking in electrolytes, intercalants, and tribological contacts where fixed-bond models fail; and **classical fixed-bond** potentials for large cells or slow processes such as electrode charging dynamics where reactivity is secondary. The Methods section of the chapter itself is primarily bibliographic—pointing readers to representative studies—rather than reporting a single new computational benchmark.

## Findings

The chapter’s synthesis is that **non-reactive MD** remains indispensable for throughput on large MXene stacks and electrochemical double-layer problems where chemistry is frozen, while **ReaxFF** is positioned where **explicit chemistry** governs intercalation pathways, **water** transport, friction, or corrosion-like reactions. **AIMD** anchors the parameterizations and sanity-checks local motifs that lower-cost models must reproduce. Application clusters (storage, catalysis, exfoliation) are mapped to these capability tiers on **`[[2019chapter9-venue-paper]]`**.

**Comparisons and evidence style.** Because the chapter is a **review**, quantitative claims (diffusion barriers, elastic constants, intercalation voltages) live in the **cited primary literature** rather than in this duplicate-path wiki note; readers should treat each subsection’s references as the authoritative **experiment**/**simulation** comparison set.

**Sensitivity and transferability.** The text repeatedly stresses **surface termination** (**–O**, **–OH**, **–F**) as a lever that changes both **reactivity** and the appropriate **force field** choice; **temperature**, **electrolyte** composition, and **water** content appear throughout cited case studies as knobs that move systems between **AIMD**-necessary and **classical**-sufficient regimes.

**Limitations and outlook.** Coverage is bounded by the **2019** print date and the cited corpus; newer **MXene** compositions, **machine-learned** potentials, and refined **ReaxFF** parameter lines may supersede specific numerical examples while leaving the **tiered MD** logic intact.

**Corpus honesty.** This slug tracks an alternate **PDF** byte stream for the same **DOI** as **`[[2019chapter9-venue-paper]]`**; substantive **figure** numbering should be checked against whichever **PDF** your checkout treats as canonical.

## Limitations

PDF variants can differ in **front matter** and **pagination**; cite the **DOI** and use **`[[2019chapter9-venue-paper]]`** when unsure which filename is canonical in your checkout.

## Reproducibility notes

Readers porting recommendations into simulation input decks should still consult **primary** studies cited in the chapter: review prose compresses **ensemble choices**, **electrode potentials**, and **water models** that differ across the MXene literature. When choosing **ReaxFF** versus classical FF, document **termination chemistry** (**–O/–OH/–F**) explicitly because MXene reactivity is termination-sensitive.

Because this slug duplicates **`[[2019chapter9-venue-paper]]`**, maintain identical bibliographic strings in both places when DOIs or editor lists are corrected during corpus hygiene—divergent metadata is a common failure mode for automated citation exporters. If the chapter receives **errata**, update both wiki pages in the same commit so downstream `paper_id` consumers do not see conflicting titles.

## Relevance to group

**Adri van Duin** co-authored the MXenes simulation review; duplicate-path record for PDF provenance.

## Citations and evidence anchors

- DOI: [10.1007/978-3-030-19026-2_9](https://doi.org/10.1007/978-3-030-19026-2_9)

## Reader notes (navigation)

- Primary chapter page: [[2019chapter9-venue-paper]]  
- [[batteries-interfaces-reaxff]], [[reaxff-family]]

## Related topics

- [[2019chapter9-venue-paper]]
- [[reaxff-family]]
