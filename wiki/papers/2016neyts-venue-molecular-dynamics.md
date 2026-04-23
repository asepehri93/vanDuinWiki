---
id: paper:2016neyts-venue-molecular-dynamics
type: paper
title: "Molecular dynamics simulations for plasma-surface interactions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:classical-md
  - method:aimd
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:oxide-surface
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1002/ppap.201600145"
year: 2016
authors:
  - "Erik C. Neyts"
  - "Pascal Brault"
venue: "Plasma Processes Polym. 2017, 14, 1600145"
pdf_sha256: "e4e505ae2bb752bc13d8b7a520395c4d586f936f237366a4098be91c13f238f0"
pdf_path: "papers/ReaxFF_others/Neyts_et_al-2017-Plasma_Processes_and_Polymers.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016neyts-venue-molecular-dynamics -->

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Plasma–surface interactions couple ion bombardment, neutral fluxes, photon absorption, electric fields, and evolving surface chemistry, so no single atomistic model reproduces a full reactor discharge. This tutorial-style review in *Plasma Processes and Polymers* restricts attention to **low-temperature non-thermal plasmas** and explains how MD nonetheless yields mechanistic insight for sputtering, etching, implantation, and thin-film growth. The roadmap is explicit: which plasma ingredients can sometimes be modeled explicitly (ground and excited species, fields, ions, photons, electrons) versus what must be approximated or dropped; Section 2 stresses plasma-specific MD constraints and the usual time/length-scale mismatch with experiment; Section 3 describes how fundamental processes are encoded in classical versus *ab initio* MD; Section 4 surveys literature examples; the close reiterates both the value and the limits of atomistic plasma–surface modeling.

## Methods

This is a **review** in *Plasma Processes and Polymers*, so the “methods” are bibliographic and pedagogical rather than a single new simulation campaign. The authors organize plasma–surface modeling as a literature survey: which plasma ingredients (ions, neutrals, excited species, fields, photons, electrons) can sometimes be treated explicitly in atomistic models versus which are idealized or omitted; how classical and *ab initio* MD encode gas–surface reactions; and what time/length-scale gaps remain relative to discharge experiments. When they summarize generic classical MD practice, they note that timesteps are typically **sub-femtosecond up to about 2 fs** so the fastest vibrational modes remain resolved.

**MD application (authored data).** **N/A —** the article does not publish new production trajectories, system sizes, integrator settings, or thermostat/barostat protocols as primary results.

**Force-field training.** **N/A —** not a parametrization paper.

**Static QM / AIMD.** **N/A —** no new DFT or AIMD benchmark suite is reported as first-party data; QM methods appear through citations and conceptual comparison.
## Findings

Atomistic MD is presented as uniquely informative for following plasma-driven surface evolution, but bounded by accessible time and length scales and by the fidelity of interatomic models for reactive gas–surface chemistry. The abstract and introduction stress which plasma components are sometimes explicit in models versus which are omitted or idealized, and they emphasize the persistent gap between simulation windows and experiment. The conclusions repeat that MD case studies explain mechanisms while no single trajectory captures reactor-scale discharge physics. Section 4’s figure-heavy case studies should be read in the publisher PDF when assigning secondary citations to specific primary works.
## Limitations

As a review, it does not substitute for primary studies on any single material system; force-field limitations for specific chemistries must be taken from cited work.

## Relevance to group

Useful retrieval spine for plasma–surface MD methodology adjacent to reactive materials simulations (including cases where ReaxFF or AIMD appear in cited primary literature).

## Citations and evidence anchors

- DOI: [10.1002/ppap.201600145](https://doi.org/10.1002/ppap.201600145)

## Reader notes (navigation)

- Plasma–surface MD survey adjacent to reactive materials work: [[reaxff-family]], [[theme-oxides-silica-ceramics]].

## Related topics

- [[reaxff-family]]
