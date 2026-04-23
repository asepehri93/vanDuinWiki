---
id: paper:2016chemrev-venue-cr5b00644
type: paper
title: "Modeling molecular interactions in water: from pairwise to many-body potential energy functions"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:methods-software
  - task:review
  - method:classical-md
  - method:aimd
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemrev.5b00644"
year: 2016
authors:
  - "Gerardo Andrés Cisneros"
  - "Kjartan Thor Wikfeldt"
  - "Lars Ojamäe"
  - "Jibao Lu"
  - "Yao Xu"
  - "Hedieh Torabifard"
  - "Albert P. Bartók"
  - "Gábor Csányi"
  - "Valeria Molinero"
  - "Francesco Paesani"
venue: "Chem. Rev."
pdf_sha256: "6fc812873486e810b6a394dff8a129f47c028b71425d16ca509093efefe098a8"
pdf_path: "papers/Others/ChemRev_water_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016chemrev-venue-cr5b00644 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Chemical Reviews** article surveys **analytical potential energy functions** for **water**, organized around the **many-body expansion** of interaction energies. It contrasts **pairwise-additive** models with **implicit** and **explicit many-body** corrections, emphasizing how modern potentials that correctly encode **two- and three-body short-range terms** plus **long-ranged many-body polarization / coupling** can reproduce **gas- through condensed-phase** benchmarks from **high-level electronic structure** and **experiment**. The review is a methodological map for choosing **force fields vs. ab initio MD** when simulating **aqueous interfaces, solvation, and phase behavior**. Readers approaching **ReaxFF** or **oxide–water** simulations benefit from the article’s clarification of when **pairwise** **SPC/E**-class models suffice versus when **polarizable** or **explicit many-body** water models are needed to match **interfacial** **dielectric** response and **hydration** structure.

## Methods

This **Chemical Reviews** article is a **literature and methods survey**, not a single new simulation study. It organizes **analytical potential energy functions** for **water** using the **many-body expansion**—from **pairwise-additive** models through **implicit** and **explicit many-body** corrections—and synthesizes how potentials are **fitted** and **validated** against **gas-phase cluster** data, **condensed-phase** observables (**ice** and **liquid** **density**, **diffusion**, **vibrational** spectra), and discussions of **long-ranged polarization** and **many-body induction** beyond **fixed-charge** schemes.

**MD application (atomistic dynamics):** **N/A —** no single production MD protocol is defined; timesteps, thermostats, ensembles, and system sizes belong to **cited** primary studies only.

**Force-field training:** **N/A —** the article surveys how empirical, polarizable, and explicit many-body water models are constructed and tested; it is not itself a parameterization run.

**Static QM / DFT:** **N/A —** the review cites diverse **high-level electronic structure** benchmarks from the literature rather than reporting one consolidated DFT study.

For **ReaxFF**-heavy workflows in this knowledge base, the taxonomy is a reminder that **solute–water** and **oxide–water** behavior may still need **water-specific** validation beyond the reactive framework when matching **interfacial tension**, **hydration free energies**, or **spectroscopic** targets. **Barostat / controlled pressure:** **N/A —** not defined for this review artifact. **External electric fields:** **N/A —** not part of the review’s scope.

## Findings

- **Hierarchy of models** (pairwise → polarizable → explicit many-body) is tied to **accuracy vs. cost** trade-offs documented with extensive citations in the review.
- **Recent potentials** are argued to approach a **“universal”** water model class for broad thermodynamic and structural observables when many-body physics is treated consistently.
- **Takeaway for practitioners:** **interface** and **electrolyte** problems often expose **deficiencies** of **fixed-charge** water models; the review’s taxonomy helps match **model complexity** to the **observable** (e.g., **surface tension**, **hydration free energies**, **IR** lineshapes) being validated.

## Limitations

As a **review**, it does not substitute for **primary validation** on a user-specific electrolyte or interface composition. Readers should also remember that **ReaxFF** simulations often embed **fixed-charge** or **EEM**-style **water** coupling that may not match the **many-body** **water** models surveyed here—**cross-comparison** between **FF** families requires explicit **benchmarking** on **interfacial** **water** **structure**.

- **Corpus honesty:** This wiki page is a **literature map**, not a **PDF** replacement; pull numerical benchmarks from the cited primary studies.

## Relevance to group

Provides **external methodological context** for any **ReaxFF / classical / QM** simulation of **aqueous electrolytes, silica, and oxide interfaces** common in the group’s applied papers.

## Citations and evidence anchors

- Title page and TOC in `papers/Others/ChemRev_water_2016.pdf`; **DOI:** `10.1021/acs.chemrev.5b00644`.

## Related topics

- [[reaxff-family]]
