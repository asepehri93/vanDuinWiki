---
id: paper:2018shin-physical-che-development-reaxff
type: paper
title: "Development of a ReaxFF reactive force field for lithium ion conducting solid electrolyte Li1+xAlxTi2−x(PO4)3 (LATP)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:ceramic-electrolyte
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c8cp03586e"
year: 2018
authors:
  - "Yun Kyung Shin"
  - "Mert Y. Sengul"
  - "A. S. M. Jonayat"
  - "Wonho Lee"
  - "Enrique D. Gomez"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics (2018)"
pdf_sha256: "e47d269e33285c1672fcf036ef261b0edd073f92b178a2cdc5cf93678e7f86bb"
pdf_path: "papers/Shin_LATP_PCCP_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018shin-physical-che-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This work develops and benchmarks a ReaxFF parameterization for NASICON-type Li1+xAlxTi2−x(PO4)3 (LATP), a solid electrolyte candidate for all-solid-state Li-ion batteries. Parameters are trained against DFT data on equations of state, heats of formation for relevant oxides and phosphates, and Li diffusion barriers in TiO2 and LiTi2(PO4)3 (LTP). ReaxFF reproduces structural trends with composition—including site preference of Li near Al versus Ti and lattice contraction with Al substitution—and explores Li transport and ionic conductivity from 300–1100 K. Hybrid MC/MD is used to sample disordered LATP configurations; at x = 0.5 the model yields conductivity in closer agreement with experiment than lower-x structures, illustrating composition-sensitive transport and the utility of reactive MD for solid electrolyte screening.

## Methods

The reactive model is trained to DFT equations of state, formation enthalpies of relevant oxides and phosphates (including Li\(_x\)TiO\(_2\), Al\(_2\)TiO\(_5\), LiAlO\(_2\), AlPO\(_4\), Li\(_3\)PO\(_4\), LiTi\(_2\)(PO\(_4\))\(_3\)), and Li migration barriers in TiO\(_2\) and LiTi\(_2\)(PO\(_4\))\(_3\) via vacancy and interstitial pathways. Molecular dynamics and hybrid Monte Carlo/MD equilibrate disordered Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\) cells and yield ionic conductivities from 300–1100 K. Structural checks include Li site preference (interstitial sites adjacent to Al versus Ti) and lattice contraction when Ti is partially replaced by Al, consistent with experiment; higher Al content increases configurational disorder from substitution and compensating Li insertion.

## Findings

LiTi\(_2\)(PO\(_4\))\(_3\) (LTP) shows low room-temperature conductivity (\(\sim 5.9\times 10^{-5}\) S cm\(^{-1}\)). Substitution toward LATP at \(x=0.2\) raises conductivity modestly (\(\sim 8.4\times 10^{-5}\) S cm\(^{-1}\)) but remains below reported values for \(x\approx 0.3\)–\(0.5\). Hybrid MC/MD sampling at \(x=0.5\) produces a thermodynamically stable arrangement with conductivity \(\sim 7.4\times 10^{-4}\) S cm\(^{-1}\) near 300 K—about an order of magnitude above LTP and the \(x=0.2\) composition, matching the order of magnitude of independent measurements (\(\sim 2.5\times 10^{-4}\) S cm\(^{-1}\)). The strong composition dependence of conductivity highlights solid-solution disorder in NASICON-type electrolytes and supports hybrid MC/MD as a practical tool for sampling these configurations.

## Limitations

- Conductivity still depends strongly on structural realization and composition; reaching experimental values requires careful sampling and may need further refinement of training data or dynamics length scales.
- High-temperature MD may not capture all long-time defect equilibria relevant near room temperature.

## Relevance to group

Core example of ReaxFF parameterization for **battery-relevant ceramic electrolytes** with direct van Duin group authorship; connects reactive FF development to measurable transport properties for solid-state battery materials.

## Citations and evidence anchors

- DOI: [10.1039/c8cp03586e](https://doi.org/10.1039/c8cp03586e)
- Primary numerical results and fitting rationale: early sections and Results in PCCP paper; see normalized extract `normalized/extracts/2018shin-physical-che-development-reaxff_p1-2.txt` for text-aligned pointers.

## Reader notes (navigation)

- **Theme hub:** [[batteries-interfaces-reaxff]] — how this paper fits next to liquid-electrolyte work ([[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]).  
- **Force-field overview:** [[reaxff-family]].  
- **Benchmark:** listed as a **gold** source for ceramic electrolyte questions in [`docs/benchmarks/V1_FROZEN.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md) (FF1).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- Solid NASICON / LATP electrolytes and Li transport in oxide frameworks
- Hybrid MC/MD for disordered ionic conductors
