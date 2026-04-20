---
id: paper:2020wenbo-zhu-j-phys-chem-jp0c02573
type: paper
title: "Development of a Reactive Force Field for Simulations on the Catalytic Conversion of C/H/O Molecules on Cu-Metal and Cu-Oxide Surfaces and Application to Cu/CuO-Based Chemical Looping"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:parameterization
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c02573"
year: 2020
authors:
  - "Wenbo Zhu"
  - "Hao Gong"
  - "You Han"
  - "Minhua Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 124:12512-12520 (2020)"
pdf_sha256: "3d54d6d748d38086a04d431078447f5f8f50aef3dc77d262844c333c58c83afd"
pdf_path: "papers/Zhu_JPCC_CuCHO_2020.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2020wenbo-zhu-j-phys-chem-jp0c02573 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A Cu/C/H/O ReaxFF is assembled by reoptimizing Cu interactions on expanded cluster training data, merging with an existing C/H/O description, and fitting Cu–C/H/O cross-terms to DFT reaction and adsorption sets. The authors implement transition-state search utilities in the ReaxFF context for elementary steps. MD demonstrations show H transfer and H2/CHO-type chemistry on Cu surfaces, and two chemical-looping scenarios: oxidation of metallic Cu with glucose to form CuO, and fuel oxidation by copper oxide as oxidizer—claiming differentiation of redox performance among fuels.

## Methods

Three-stage ReaxFF fitting; custom TS search algorithms; surface reactive MD for C/H/O on Cu and CuO.

## Findings

Qualitative capture of expected elementary reactions on Cu; case-study chemical-looping trajectories illustrating fuel/oxidizer roles.


## Limitations

Surface models and coverages are idealized; industrial catalysts involve promoters, alloying, and long-timescale coking not covered.

## Relevance to group

Extends group ReaxFF portfolio into Cu catalysis and redox carriers—relevant to energy conversion and heterogeneous catalysis workflows.

## Citations and evidence anchors

`papers/Zhu_JPCC_CuCHO_2020.pdf` — abstract (fitting strategy, TS tools, chemical looping demonstrations). https://doi.org/10.1021/acs.jpcc.0c02573

## Related topics

- [[reaxff-family]]
