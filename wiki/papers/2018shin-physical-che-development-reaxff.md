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

- **Force field:** ReaxFF reactive force field for the LATP system, fitted to DFT energies and barriers for bulk phases, Li vacancy/interstitial paths, and related ternary oxides/phosphates.
- **Simulations:** Molecular dynamics and hybrid Monte Carlo / molecular dynamics to equilibrate substituted LATP configurations and compute ionic conductivity.
- **Validation:** Comparison of lattice parameters, Li site preferences, and conductivity trends to experimental and literature values across compositions.

<!-- enrich-from-extract:v2 -->

- We developed a ReaxFF reactive force field for NASICON-type Li 1+xAlxTi2/C0 x(PO4)3 (LATP) materials, which is a promising solid-electrolyte that may enable all-solid-state lithium-ion batteries.
- The force field parameters were optimized based on density functional theory (DFT) data, including equations of state and the heats of formation of ternary metal oxides and metal phosphate crystal phases ( e.g.,L i xTiO2, Al2TiO5, LiAlO 2, AlPO 4,L i 3PO4 and LiTi 2(PO4)3 (LTP)), and the energy barriers for Li diﬀusion in TiO 2 and LTP via vacancies and interstitial sites.
- Using ReaxFF, the structural and the energetic features of LATP were described properly across various compositions – Li occupies more preferentially the interstitial site next to Al than next to Ti.
- Also, as observed in experimental data, the lattice parameters decrease when Ti is partly substituted by Al because of the smaller size of the Al cation.
- At higher x (higher Al composition), LATP has a configurational diversity due to the Al substitution and the concomitant insertion of Li.


## Findings

- Li favors interstitial sites adjacent to Al over Ti in the parametrized model; lattice parameters shrink when Ti is partially replaced by Al, consistent with experiment.
- Ionic conductivity in LTP is low; modest improvement appears for LATP at x = 0.2, while a thermodynamically stable configuration at x = 0.5 (from hybrid MC/MD) shows conductivity ~10⁻⁴ S cm⁻¹ at 300 K, aligning with measured order of magnitude for higher-Al compositions.
- Demonstrates MC/MD for capturing configurational complexity in substituted NASICON-type electrolytes and linking it to transport.

### Additional results (article abstract)

- Using this force field, the diffusion mechanism and the ionic conductivity of Li in LTP and LATP were investigated at T = 300– 1100 K.
- Low ionic conductivity (5.9 × 10−5 S cm−1 at 300 K) was obtained in LTP as previously reported.
- In LATP at x = 0.2, the ionic conductivity was slightly improved (8.4 × 10−5 S cm−1), but it is still below the experimental value, which is on the order of 10−4 to 10−3 S cm−1 at x = 0.3–0.5.
- The ionic conductivity of this LATP configuration was calculated to be 7.4 × 10−4 S cm−1 at 300 K, which is one order of magnitude higher than the ionic conductivity for LTP and LATP at x = 0.2.
- This value is in good agreement with our experimental value (2.5 × 10−4 S cm−1 at 300 K) and the literature values.
- The composition-dependent ionic conductivity of LATP was successfully demonstrated using the ReaxFF reactive force field, verifying the applicability of the LATP force field for the understanding of Li diffusion and the design of highly Li ion conductive solid electrolytes.
- Furthermore, our results also demonstrate the feasibility of the MC/MD method in modeling LATP configuration, and provide compelling evidence for the solid solution sensitivity on ionic conductivity.
- By performing a hybrid MC/MD simulation for LATP at x = 0.5, a thermodynamically stable LATP configuration was obtained.


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
