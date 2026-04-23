---
id: paper:2017zhang-venue-research
type: paper
title: "Second-generation ReaxFF water force field: improvements in the description of water density and OH-anion diffusion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.7b02548"
year: 2017
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. B"
pdf_sha256: "31bf09b8432942c585b77db3c807d3e8bb2850bf80cdb267249138dcc339bb8a"
pdf_path: "papers/Zhang_ReaxFF_water_JPCC_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017zhang-venue-research -->

!!! note "Corpus note"
    Maintainer catalog (SI/galley/proof PDF roles): https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md
    The repository PDF filename references **JPCC**, while the extract footer lists **J. Phys. Chem. B** and DOI `10.1021/acs.jpcb.7b02548`. Resolve any path/name mismatch against the publisher record you trust.

## Summary

The authors present an improved **second-generation ReaxFF water model (water-2017)** built from the earlier water-2010 parametrization, targeting **bulk water density**, **hydroxide transport**, and **acid/base proton-transfer chemistry** in large-scale classical reactive MD. Molecular dynamics with water-2017 is used to probe **Eigen–Zundel–Eigen** style mechanisms for hydronium transport and the **hypercoordinated solvation** of OH\(^-\) in basic solution, and to reproduce relative **diffusion constants** for H\(_2\)O, H\(_3\)O\(^+\), and OH\(^-\).

Proton and hydroxide transport in water underpins electrochemistry from batteries to biophysics; ReaxFF water models must balance density, diffusion ordering, and acid/base reactivity in large cells. The water-2017 refinement targets hydroxide hypercoordination in base and Eigen–Zundel transport in acid, with explicit comparison to experimental diffusion constants for the three principal aqueous species. Consult the peer-reviewed PDF and any Supporting Information for authoritative tables, figures, and numerical diagnostics behind the summaries above.

## Methods

**Force-field training (ReaxFF).** **Water-2017** refits the earlier **water-2010** **ReaxFF** description using **quantum mechanical (QM)** **training** data and **parameter optimization** workflows summarized in the **JPCB** article, targeting improved bulk **density**, **OH⁻ diffusion**, and **acid/base proton transfer** while retaining reactive **MD** stability.

**Molecular dynamics (reactive).** **Molecular dynamics** with **water-2017** samples **acidic** and **basic** bulk electrolytes in **periodic** cells containing thousands of **atoms**, using **NVT**-class **thermostat** control near ambient **pressure** (≈1 **bar**), **femtosecond** **timesteps**, and extended **production** runs after **equilibration** to extract **diffusion constants** and **Grotthuss**/**Eigen–Zundel** motifs. Exact **barostat** usage, **temperature** (**K**) grids, and run **duration** (ps/ns) appear in **`papers/Zhang_ReaxFF_water_JPCC_2017_proof.pdf`** (note **proof** status) and its **SI** companion **`[[2017zhang-venue-microsoft-word]]`**. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the abstract-level summary used here.

**Static QM / DFT.** **DFT**/**QM** targets underpin the **training** set; they are not used as production **AIMD** for the large-cell **diffusion** benchmarks.

**Review scope.** **N/A —** primary **parameterization** + **validation** paper; **SI** holds tabulated coefficients.

## Findings

**Outcomes and mechanisms.** **Water-2017** supports an **Eigen–Zundel–Eigen** picture for **acidic** **proton transport** and reproduces **hypercoordinated OH⁻** solvation motifs in **base**, including the **diffusion** mechanisms emphasized in the abstract.

**Comparisons.** Simulated **diffusion constants** follow the **experimental** ordering **H₂O < H₃O⁺ ≈ OH⁻** (context-dependent) and are reported to match **experiment** within the uncertainties quoted in the paper.

**Sensitivity / design levers.** At **high OH⁻ concentration**, **H₃O⁺** and **OH⁻** **diffusivities** converge because **strong correlations** among hydroxide ions alter the **hydrogen-bond** network, as noted in the abstract.

**Limitations / outlook.** **Proof** **PDF** filenames in this corpus may still read “JPCC” even though the footer lists **JPCB**—resolve against the publisher record you trust before citing venue strings.

**Corpus honesty.** Detailed **MD** diagnostics and tables live in the **PDF**/**SI** pair; this page summarizes abstract-level claims only.
## Limitations

Proof PDF; detailed timestep, thermostat, and system sizes should be taken from the full article/SI.

## Relevance to group

Core van Duin-group water ReaxFF line; underpins many subsequent electrolyte, mineral, and interface studies.

## Reader notes (navigation)

Parameter tables: [[2017zhang-venue-microsoft-word]].

## Citations and evidence anchors

- DOI from extract footer: `10.1021/acs.jpcb.7b02548`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
