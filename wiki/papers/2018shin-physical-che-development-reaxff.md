---
id: paper:2018shin-physical-che-development-reaxff
type: paper
title: Development of a ReaxFF reactive force field for lithium ion conducting solid
  electrolyte Li1+xAlxTi2−x(PO4)3 (LATP)
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
doi: 10.1039/c8cp03586e
year: 2018
authors:
- Yun Kyung Shin
- Mert Y. Sengul
- A. S. M. Jonayat
- Wonho Lee
- Enrique D. Gomez
- Clive A. Randall
- Adri C. T. van Duin
venue: Physical Chemistry Chemical Physics (2018)
pdf_sha256: e47d269e33285c1672fcf036ef261b0edd073f92b178a2cdc5cf93678e7f86bb
pdf_path: papers/Shin_LATP_PCCP_2018.pdf
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

**Force-field training (ReaxFF for Li–Al–Ti–P–O).** The authors develop a **ReaxFF** **reactive force field** for **NASICON-type** **Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\)** (**LATP**), starting from parent **ReaxFF** libraries for **oxides**/**phosphates** and extending interaction classes needed for **Li** transport in the **Ti/Al**-substituted framework. **QM reference data** come from **DFT** calculations of **equations of state**, **heats of formation** for reference crystals (**Li\(_x\)TiO\(_2\)**, **Al\(_2\)TiO\(_5\)**, **LiAlO\(_2\)**, **AlPO\(_4\)**, **Li\(_3\)PO\(_4\)**, **LiTi\(_2\)(PO\(_4\))\(_3\)** (**LTP**)), and **Li** **migration** **barriers** in **TiO\(_2\)** and **LTP** via **vacancy** and **interstitial** pathways. **Optimization** follows the standard **ReaxFF** **parameter** **fitting** workflow described in *PCCP* (least-squares-style minimization of **QM** vs **force-field** errors across the **training set**). **Validation / reference data** additionally include **experimental** **lattice** trends used to judge **Al** substitution effects.

**MD application + hybrid MC/MD.** **Engine:** **molecular dynamics** with the fitted **ReaxFF** potential, combined with **hybrid Monte Carlo / MD** sampling to explore **disordered** **Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\)** arrangements (**reactive MD** in the sense of variable **Li** site occupancy moves plus **dynamics**). **System:** **periodic** **supercells** of **LATP** compositions spanning the **\(x\)** range studied (**atom** counts in article tables). **PBC:** **three-dimensional periodic** boundaries. **Ensemble:** production **ionic conductivity** trajectories are **canonical** **NVT**-style **MD** segments as reported in *PCCP* (**NPT** details **N/A — not emphasized** in the abstract-level summary on this page). **Temperature:** **ionic conductivity** and **diffusion** analyses span **300–1100 K** as reported. **Timestep / thermostat / barostat / production length:** **N/A — explicit fs timestep, thermostat family, and multi-ns production tables** should be copied from the *PCCP* **Methods** rather than inferred from this summary. **Pressure:** **N/A — not emphasized** in the excerpted abstract-style summary on this page. **Electric field:** **N/A — not used**. **Enhanced sampling:** **hybrid MC/MD** beyond straight **MD**; **N/A — umbrella / metadynamics** not indicated in the indexed excerpt.
## Findings

LiTi\(_2\)(PO\(_4\))\(_3\) (LTP) shows low room-temperature conductivity (\(\sim 5.9\times 10^{-5}\) S cm\(^{-1}\)). Substitution toward LATP at \(x=0.2\) raises conductivity modestly (\(\sim 8.4\times 10^{-5}\) S cm\(^{-1}\)) but remains below reported values for \(x\approx 0.3\)–\(0.5\). Hybrid MC/MD sampling at \(x=0.5\) produces a thermodynamically stable arrangement with conductivity \(\sim 7.4\times 10^{-4}\) S cm\(^{-1}\) near 300 K—about an order of magnitude above LTP and the \(x=0.2\) composition, matching the order of magnitude of independent measurements (\(\sim 2.5\times 10^{-4}\) S cm\(^{-1}\)). The strong composition dependence of conductivity highlights solid-solution disorder in NASICON-type electrolytes and supports hybrid MC/MD as a practical tool for sampling these configurations.

Across **300–1100 K**, the study tracks **Li** **diffusion** mechanisms and **ionic conductivity** trends in **LTP** vs **LATP**, emphasizing that **experimental** conductivities on the order of **\(10^{-4}\)–\(10^{-3}\) S cm\(^{-1}\)** for **\(x \approx 0.3\)–\(0.5\)** are only approached in the **ReaxFF** model once a **hybrid MC/MD**-sampled **\(x=0.5\)** arrangement is used, while a simpler **\(x=0.2\)** realization remains sub-**experimental**. The authors argue this supports both the **transferability** of the **LATP** **force field** for **solid electrolyte** screening and the **sensitivity** of **conductivity** to **solid-solution** **disorder**. **Limitations / outlook:** **conductivity** remains sensitive to structural realization and sampling length scales, as noted under **## Limitations**. **Corpus honesty:** tabulated **conductivity** values here follow the article abstract language mirrored in `normalized/extracts/2018shin-physical-che-development-reaxff_p1-2.txt`; confirm against `pdf_path` for final typesetting.

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
