---
id: paper:2017mishra-cement-and-c-cemff-force
type: paper
title: "cemff: A force field database for cementitious materials including validations, applications and opportunities"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:classical-ff-specialized
  - task:application
paper_keywords:
  - keyword:classical-ff
  - keyword:review-or-perspective
  - keyword:oxide-surface
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
pdf_sha256: "c032f504c2be385c25e060649d2299c00780b3db094de579a3868f7fb98751c9"
pdf_path: "papers/Mishra_cemff_Cement_Concrete_Res_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mishra-cement-and-c-cemff-force -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

!!! abstract "Scope"
    Review of atomistic force fields for cement hydrates and related minerals, comparing families (ClayFF, CSH-FF, ReaxFF, IFF, etc.) and introducing the **cemff** web database for parameters and validation benchmarks.

## Summary

This Cement and Concrete Research review introduces cemff, a web-accessible force-field database for atomistic simulations of cementitious materials, coauthored by a broad consortium including Adri C. T. van Duin. The article argues that concrete-scale performance questions—hydration kinetics, additive interactions, substitution of clinker with supplementary materials, and degradation pathways—ultimately depend on nanoscale chemistry at interfaces that is difficult to probe experimentally, motivating systematic atomistic modeling. Rather than proposing one universal potential, the manuscript surveys major families used for hydrated and anhydrous cement phases, including Born–Mayer–Huggins models, InterfaceFF, ClayFF, CSH-FF, CementFF, GULP-related schemes, ReaxFF, UFF, and others, discussing strengths, known failures, and typical validation observables such as structure, mechanics, and spectroscopic benchmarks.

## Methods

**Force-field training / fitting.** **Survey** of **cementitious** **force-field** families (**Born–Mayer–Huggins**, **InterfaceFF (IFF)**, **ClayFF**, **C–S–H FF**, **CementFF**, **GULP**-style ionic models, **ReaxFF**, **UFF**, and related specialized fits): how **parameters** are obtained, which **structures** they target (**C₃S**, **portlandite**, **C–S–H** motifs, etc.), and how **validation** against **experiment** or **QM** is typically reported. **No** new **universal** potential is fit inside this review.

**MD application (atomistic dynamics).** **Literature-scope** description of how each **potential class** is used in **minimization**, **NVT/NPT** production workflows, and **interfacial** simulations across cited studies—**not** a single new **MD** benchmark dataset generated for this manuscript.

**Static QM / DFT.** **DFT** appears throughout as **QM reference** data for **parameter fitting**, **equation-of-state** benchmarks, and **spectroscopic** comparisons in the surveyed literature.

**Review / database framing.** **Narrative review** plus introduction of the **cemff** web registry (**http://cemff.epfl.ch**) for **energy expressions**, **parameter files**, and **validation hooks**, including **community upload** expectations and **governance** notes as described in the article.

## Findings

The review emphasizes that many incompatible force-field choices coexist in the literature, producing simulations that are not always comparable to one another or to experiment without careful calibration. A central practical conclusion is that users must match the potential class to the phenomenon: nonreactive clay and C–S–H models may suffice for structural questions, whereas bond-making and bond-breaking chemistry may require reactive frameworks such as ReaxFF or other specialized reactive fits. The cemff initiative is framed as reducing duplicated benchmarking effort and making limitations explicit, including where ReaxFF adds value for reactivity but still demands system-specific validation. The article also situates cement’s large carbon footprint and the need for scientifically guided reformulation of binders as motivation for transparent, reproducible atomistic benchmarks rather than ad hoc parameter reuse.

The introduction’s bullet list of atomistic-scale phenomena—including dissolution and growth of hydrates, additive interactions, substitution of clinker with supplementary cementitious materials, degradation mechanisms, waste immobilization, and mechanical anisotropy—illustrates why the review treats force-field choice as problem-dependent rather than as a single best potential for all cementitious simulations. The abstract explicitly names representative phases such as tricalcium silicate, portlandite, and C–S–H model systems as targets for the surveyed potentials and for database benchmarking. The database URL given in the article is `http://cemff.epfl.ch`, described as a curated registry of energy expressions, parameters, and validation comparisons.

## Limitations

Review scope is database- and literature-driven; it does not replace system-specific validation for new compositions.

## Relevance to group

Adri C. T. van Duin is a co-author; situates **ReaxFF** within the broader cement FF ecosystem.

## Citations and evidence anchors

- DOI: `10.1016/j.cemconres.2017.09.003`

## Reader notes (navigation)

- Cement FF survey + **cemff** database; [[theme-oxides-silica-ceramics]], [[reaxff-family]].

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
