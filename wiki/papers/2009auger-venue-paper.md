---
id: paper:2009auger-venue-paper
type: paper
title: "Mechanisms of Auger-induced chemistry derived from wave packet dynamics"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:carbon-hydrocarbon, domain:methods-software, method:reactive-md-generic, scale:atomistic, task:application]
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.0812087106"
year: 2009
authors: ["Su, Julius T.", "Goddard, William A., III"]
venue: "Proceedings of the National Academy of Sciences"
pdf_sha256: "9ad920f4eaabb8e5544142cb63b323f4e46ded2711aa32eaf47a6b49f54bb96e"
pdf_path: "papers/Others/Auger_eFF_Su_PNAS.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2009auger-venue-paper -->

## One-paragraph summary

This PNAS contribution uses the **electron force field (eFF)**—a dynamics model in which electrons are represented as floating Gaussian wave packets and nuclei move classically—to follow Auger-related relaxation after core ionization in a hydrogen-terminated diamond nanoparticle **C₁₉₇H₁₁₂**. The work distinguishes **surface** core ionizations (leading toward fragment and proton emission via a direct Auger picture) from **deeper** ionizations (hydrides emitted via “remote heating”), and discusses consistency with photon-stimulated desorption literature. The opening pages also summarize the eFF equations of motion and show ground-state electron density comparisons to DFT for simple hydrocarbons.

## Methods

- **eFF / fermionic molecular dynamics:** Valence and core electrons are modeled as spherical Gaussian wave packets; a Pauli exclusion term controls overlap-dependent repulsion; parameters are referenced as fitted to small-molecule ground-state data in the article.
- **System:** Hydrogenated diamond nanoparticle **C₁₉₇H₁₁₂** with selective core removal at surface vs subsurface sites to probe distance-dependent relaxation and desorption channels.
- **Core-hole lifetime:** The extract reports a modeled CH₄ core-hole lifetime example and compares to experimental linewidth-based estimates.

## Findings

- Surface vs depth-dependent core ionization is argued to produce qualitatively different desorption channels (direct Auger-related emission vs heating-driven emission), linking simulation to experimental PSD themes.
- Illustrative dynamics on the nanoparticle show core-hole filling, secondary electron ejection, and lingering valence excitation over tens of femtoseconds in the excerpted trajectory discussion.

## Limitations

- The normalized record marks extraction as **partial**; quantitative numbers beyond the excerpt should be verified in the full PDF.
- This is **not** a ReaxFF study; methodology is eFF-specific and should not be conflated with reactive bond-order force fields.

## Relevance to group

Provides a precedent for **large-scale excited-state surface chemistry** modeling using inexpensive dynamical models, complementary to reactive FF workflows used elsewhere in the corpus for ground-state bond making/breaking.

## Citations and evidence anchors

- Opening abstract and introduction: Auger mechanisms, C₁₉₇H₁₁₂ model, PSD comparison (PDF pp. 1–2 per extract scope).

## Related topics

- [[reaxff-family]]
