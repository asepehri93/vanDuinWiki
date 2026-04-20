---
id: paper:2017jejoon-yeon-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF force field for Cu/S/C/H and reactive MD simulations of methyl thiolate decomposition on Cu(100)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.7b06976"
year: 2017
authors:
  - "Jejoon Yeon"
  - "Heather L. Adams"
  - "Chad E. Junkermeier"
  - "Adri C. T. van Duin"
  - "Wilfred T. Tysoe"
  - "Ashlie Martini"
venue: "J. Phys. Chem. B"
pdf_sha256: "f8a35a32ee421caa2984debab920e39166a271254889a2d8bdec735468e7e84c"
pdf_path: "papers/Yeon_CuSCH_JPCB_2017.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2017jejoon-yeon-j-phys-chem-development-reaxff -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A new **Cu/S/C/H ReaxFF** parametrization is trained to study **methyl thiolate** decomposition on **Cu(100)**, motivated by **tribochemical** observations that **sliding** can accelerate **organosulfur** chemistry on **copper**. **DFT** references inform **Cu sulfide** lattice behavior, **Cu–S** bonding, **thiolate** decomposition paths, and **adsorption** energetics; **MD** demonstrates **C–S** scission initiation and subsequent **ethane-forming** chemistry consistent with **UHV** experiments. Leadership spans **UC Merced**, **UWM**, **van Duin** at **PSU**, and **Martini** group **tribology** expertise.

## Methods

- **ReaxFF** fitting to **DFT** data on **CuS**, **CuS\(_2\)**, **Cu\(_2\)S** cells, **Cu–S–C** bending, **binding** energies, and **decomposition** profiles.
- **Reactive MD** thermal simulations of **CH\(_3\)S** chemistry on **Cu(100)**.

## Findings

- **C–S** bond breaking initiates decomposition; **methyl** species recombine toward **ethane** desorption as observed experimentally.


## Limitations

- Scope centers on **Cu(100)** **methyl thiolate** family chemistry; broader **additive** chemistry requires further validation.

## Relevance to group

Shows **van Duin** **ReaxFF** deployment for **organosulfur** **Cu** interfaces linking **surface science** and **tribochemistry**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcb.7b06976` (`papers/Yeon_CuSCH_JPCB_2017.pdf`).

## Related topics

- [[reaxff-family]]
