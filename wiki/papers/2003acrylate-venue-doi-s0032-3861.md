---
id: paper:2003acrylate-venue-doi-s0032-3861
type: paper
title: "The kinetics of vinyl acrylate photopolymerization"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/S0032-3861(03)00213-1"
year: 2003
authors:
  - "Tai Yeon Lee"
  - "Todd M. Roper"
  - "E. Sönny Jonsson"
  - "Igor Kudyakov"
  - "K. Viswanathan"
  - "C. Nason"
  - "C. A. Guymon"
  - "C. E. Hoyle"
venue: "Polymer"
pdf_sha256: "95abe3eb10c3ceeead300bfe610c1c4009a1a05bd206711ca462e42e17a7d347"
pdf_path: "papers/Others/acrylate_photopolymerization_Polymer_2003.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2003acrylate-venue-doi-s0032-3861 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Vinyl acrylate carries two distinct polymerizable handles—an acrylate carbonyl–vinyl group and a vinyl ether-type linkage—whose relative reactivity controls branching, network formation, and initiation behavior in UV-curable formulations. This *Polymer* article uses real-time Fourier-transform infrared spectroscopy to follow photopolymerization kinetics, demonstrating that the acrylate moiety reacts far faster than the vinyl group under comparable irradiation conditions. The authors further show that vinyl acrylate can self-initiate polymerization upon exposure to ultraviolet light and can photosensitize polymerization of mono- and difunctional acrylate comonomers, acting analogously to a photoinitiator in some regimes. Control experiments with model monomers indicate that efficient photosensitization toward external acrylates requires both functionalities to be tethered within the same vinyl acrylate molecule, underscoring intramolecular coupling rather than a simple mixture effect.

## Methods

This is an **experimental photochemistry / kinetics** study (no **MD** or **QM** simulations); checklist **D** applies.

- **Kinetic probe:** **real-time FTIR** during **UV**-induced **free-radical polymerization**; **infrared** spectra recorded on a **modified Bruker 88** spectrometer with **fiber-optic** illumination of a **horizontal** sample; **horizontal transmission** cell designed to limit **flow** during measurements (**Fig. 2** in the article). Samples sandwiched between **NaCl** plates with a **Teflon** spacer (the article text lists **15 mm**); edges sealed with **vacuum grease** to limit **oxygen** ingress (**Experimental** section, *Polymer* **44**, 2859–2865).
- **Light source / metrology:** **200 W** **Hg–Xe** lamp (**ScienceTech**); **UV** intensity measured with a calibrated **International Light IL-1400** radiometer; **FTIR** acquired at **5–10 scans/s** under continuous **UV**; **C=C** regions monitored near **1625** and **1645–1646 cm\(^{-1}\)** with **band deconvolution** (Sec. 2).
- **Signals:** time-resolved **deconvolution** of **overlapping** **acrylate** vs **vinyl** bands to quantify **relative** consumption rates of the two **functional groups** (abstract + Sec. 2).
- **Comparative chemistry:** **model monomers** (**ethyl acrylate**, **vinyl propionate**, **vinyl methacrylate**, **hexyl acrylate**, **lauryl acrylate**, **1,6-hexanediol diacrylate**, structures in **Fig. 1**) plus optional **DMPA** photoinitiator—used to test whether **both** **acrylate** and **vinyl** must be **on the same molecule** for **photosensitization** of external **acrylates** (Sec. 2).
- **Dark / follow-on measurements:** authors also report **dark** polymerization after shuttering **UV** once **~25%** **acrylate** conversion is reached; **UV–vis** spectra on a **Cary 5** (Sec. 2).

### MD application (not reported)

The publication does **not** present atomistic **molecular dynamics** trajectories; all kinetic data come from **FTIR** under **UV** illumination. For the standard MD checklist used elsewhere in this wiki: **N/A — engine** (no MD code); **N/A — atom counts / supercell composition** (no atomistic simulation); **N/A — periodic boundaries**; **N/A — NVE/NVT/NPT** ensemble (no MD); **N/A — timestep**; **N/A — trajectory duration**; **N/A — thermostat**; **N/A — barostat** / **NPT** (no pressure-controlled MD); **N/A — simulation temperature** as an MD control parameter; **N/A — stress control** in MD; **N/A — applied electric field** beyond the experimental **UV** photochemical drive; **N/A — umbrella / metadynamics / replica exchange**. Grounding: `pdf_path` (*Polymer* **44**, 2859–2865) and `normalized/extracts/2003acrylate-venue-doi-s0032-3861_p1-2.txt`.

## Findings

- **Reactivity split:** under the article’s **FTIR** protocol, the **acrylate** group polymerizes **much faster** than the **vinyl** handle, enabling quantitative tracking of **differential** conversion (abstract; kinetic curves in the paper).
- **Self-initiation / cross-initiation:** **vinyl acrylate** can **self-initiate** and act as a **photoinitiator** toward **mono- and difunctional acrylates**; **model** studies show **both** functionalities must be **tethered** in one molecule for effective **initiation** of external **acrylate** polymerization (abstract; Sec. 2–3).
- **Mechanistic proposals:** authors outline **possible** **UV**-initiation pathways for **vinyl acrylate** (Sec. 3); these are **hypothesis-level** in the source and should be read alongside their **control** experiments.
- **Limitations (study scope):** **FTIR** reports **chemical conversion**, not **modulus**, **residual stress**, or **network topology**; **thin-film** transmission conditions may differ from industrial **coat** thicknesses or **oxygen**-saturated films.

## Limitations

FTIR kinetics report chemical conversion rather than full three-dimensional network architecture; additional mechanical testing and simulation would be needed for processing stress models relevant to coatings or composites.

## Relevance to group

The article is not a ReaxFF or molecular dynamics study, but it documents photocurable polymer chemistry that may appear alongside experimental processing routes in broader materials workflows referenced from the knowledge base.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1016/S0032-3861(03)00213-1

## MAS / retrieval notes

This entry is photochemistry and polymerization kinetics rather than a reactive MD benchmark; route users interested in UV-cure epoxies or acrylate networks to the theme hub below instead of [[reaxff-family]]. For benchmarking questions, emphasize that FTIR conversion traces are not modulus or shrinkage measurements without additional mechanical data.

## Related topics

- [[theme-pyrolysis-combustion-organics]]
