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

## One-paragraph summary

This work develops and benchmarks a ReaxFF parameterization for NASICON-type Li1+xAlxTi2−x(PO4)3 (LATP), a solid electrolyte candidate for all-solid-state Li-ion batteries. Parameters are trained against DFT data on equations of state, heats of formation for relevant oxides and phosphates, and Li diffusion barriers in TiO2 and LiTi2(PO4)3 (LTP). ReaxFF reproduces structural trends with composition—including site preference of Li near Al versus Ti and lattice contraction with Al substitution—and explores Li transport and ionic conductivity from 300–1100 K. Hybrid MC/MD is used to sample disordered LATP configurations; at x = 0.5 the model yields conductivity in closer agreement with experiment than lower-x structures, illustrating composition-sensitive transport and the utility of reactive MD for solid electrolyte screening.

## Methods

- **Force field:** ReaxFF reactive force field for the LATP system, fitted to DFT energies and barriers for bulk phases, Li vacancy/interstitial paths, and related ternary oxides/phosphates.
- **Simulations:** Molecular dynamics and hybrid Monte Carlo / molecular dynamics to equilibrate substituted LATP configurations and compute ionic conductivity.
- **Validation:** Comparison of lattice parameters, Li site preferences, and conductivity trends to experimental and literature values across compositions.

## Findings

- Li favors interstitial sites adjacent to Al over Ti in the parametrized model; lattice parameters shrink when Ti is partially replaced by Al, consistent with experiment.
- Ionic conductivity in LTP is low; modest improvement appears for LATP at x = 0.2, while a thermodynamically stable configuration at x = 0.5 (from hybrid MC/MD) shows conductivity ~10⁻⁴ S cm⁻¹ at 300 K, aligning with measured order of magnitude for higher-Al compositions.
- Demonstrates MC/MD for capturing configurational complexity in substituted NASICON-type electrolytes and linking it to transport.

## Limitations

- Conductivity still depends strongly on structural realization and composition; reaching experimental values requires careful sampling and may need further refinement of training data or dynamics length scales.
- High-temperature MD may not capture all long-time defect equilibria relevant near room temperature.

## Relevance to group

Core example of ReaxFF parameterization for **battery-relevant ceramic electrolytes** with direct van Duin group authorship; connects reactive FF development to measurable transport properties for solid-state battery materials.

## Citations and evidence anchors

- DOI: [10.1039/c8cp03586e](https://doi.org/10.1039/c8cp03586e)
- Primary numerical results and fitting rationale: early sections and Results in PCCP paper; see normalized extract `normalized/extracts/2018shin-physical-che-development-reaxff_p1-2.txt` for text-aligned pointers.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- Solid NASICON / LATP electrolytes and Li transport in oxide frameworks
- Hybrid MC/MD for disordered ionic conductors
