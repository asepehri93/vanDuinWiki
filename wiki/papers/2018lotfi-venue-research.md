---
id: paper:2018lotfi-venue-research
type: paper
title: "Molecular dynamics simulations of perfluoropolyether lubricant degradation in the presence of oxygen, water, and oxide nanoparticles using a ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - material:oxide
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b09660"
year: 2018
authors:
  - "Roghayyeh Lotfi"
  - "Adri C. T. van Duin"
  - "Mousumi Mani Biswas"
venue: "J. Phys. Chem. C"
pdf_sha256: "4d9add9bb494ff97e3c8d1dd7678bc66bc7708db8cf1bd2d6c24abc55f3cddb1"
pdf_path: "papers/Lotfi_JPC_C_2018_proof.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018lotfi-venue-research -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** at **high temperature** is used to study **degradation** of a **Demnum-class PFPE lubricant (D4OH)** in **hard-disk-drive–relevant** environments containing **O₂**, **H₂O**, and **oxide nanoparticles** (**SiO₂**, **goethite**, **Fe₂O₃**) with several **pretreatment states** (untreated vs **dry/wet air** exposure). The simulations emphasize that **water** strongly **accelerates** strand **scission chemistry**, while **O₂** plays a comparatively **minor** role under the modeled conditions, and that **nanoparticles** generally **catalyze / accelerate** degradation—with **material-specific** rankings across **oxide** types and **pretreatments**. **Adri C. T. van Duin** is corresponding-group coauthor with **Lotfi** and **Biswas** (Western Digital affiliation on the experimental/industry side).

## Methods

- **ReaxFF reactive MD** of **multi-strand lubricant** systems with explicit **gas**, **water**, and **NP** interfaces.
- **High-temperature** protocol (article uses **1500 K** in the abstract text) to access **reaction events** within accessible MD timescales.

## Findings

- **Water** is the **dominant accelerant** among the small-molecule oxidants treated.
- **Nanoparticle pretreatment** changes **surface hydroxylation / adsorption** and thereby modulates **degradation rates**.


## Limitations

- **Elevated temperature** is a **kinetic accelerator**, not a direct **operating temperature** of devices; extrapolation requires **care**.
- **PFPE chemistry** is complex; **quantitative** product distributions may be **force-field sensitive**.

## Relevance to group

Illustrates **ReaxFF** applied to **tribology / storage** lubricant **pyrolysis-like** chemistry with **industrial coauthorship**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.7b09660` (printed on the **ACS proof** PDF `papers/Lotfi_JPC_C_2018_proof.pdf`).

## Related topics

- [[reaxff-family]]
