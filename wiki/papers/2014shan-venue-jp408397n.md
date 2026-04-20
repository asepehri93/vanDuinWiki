---
id: paper:2014shan-venue-jp408397n
type: paper
title: "Development of a ReaxFF reactive force field for ammonium nitrate and application to shock compression and thermal decomposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1021/jp408397n"
year: 2014
authors:
  - "Tzu-Ray Shan"
  - "Adri C. T. van Duin"
  - "Aidan P. Thompson"
venue: "Journal of Physical Chemistry A 2014, 118, 1469–1478"
pdf_sha256: "9b9c494a43d290eff4af24e4ce0d3e41b1ca2ecf67350d9bff8982c2b32eb5cd"
pdf_path: "papers/Shan_Thompson_AN_JPCA_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014shan-venue-jp408397n -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Shan, van Duin, and Thompson report a **ReaxFF** reparameterization for **ammonium nitrate (AN)** starting from an existing **nitramine/TATB** description, training against **electronic-structure** data for **barriers**, **heats of formation**, and **crystal** properties of AN phases. Applications shown in the abstract include **isothermal compression** of phase-IV AN (claimed agreement with DFT/experiment within about **10%** over the studied compression range), **unreacted principal Hugoniot** states (noted as stiffer than experiment by about **17%** in the abstract statement), and **thermal decomposition** simulations up to **2500 K** with pathways said to align with experimental findings. Simulations are executed in **LAMMPS** using the group's ReaxFF workflow.

## Methods

- **ReaxFF** optimization anchored to **DFT** targets for AN chemistry and phase-IV crystallography.
- **MD** for equation-of-state, Hugoniot-related states, and high-temperature decomposition trajectories.

## Findings

- AN is positioned as an **energetic ionic crystal** with multiple solid phases; phase **IV** is the room-temperature focus.
- The manuscript contrasts multiple experimental **Hugoniot** parametrizations from the literature to motivate scatter and modeling challenges.


## Limitations

- Hugoniot-level agreement is explicitly imperfect in the abstract; users should treat **shock** observables as **validation-sensitive** outputs.
- Extract is early pages only; quantitative plots and full barrier sets require the PDF body.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties this to **ReaxFF** development for **energetic nitrogen/oxygen** chemistry used across combustion and initiation modeling threads.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp408397n](https://doi.org/10.1021/jp408397n)

## Related topics

- [[reaxff-family]]