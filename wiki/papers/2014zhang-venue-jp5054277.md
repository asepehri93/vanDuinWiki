---
id: paper:2014zhang-venue-jp5054277
type: paper
title: "Development of a ReaxFF reactive force field for tetrabutylphosphonium glycinate/CO2 mixtures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1021/jp5054277"
year: 2014
authors:
  - "Bo Zhang"
  - "Adri C. T. van Duin"
  - "J. Karl Johnson"
venue: "Journal of Physical Chemistry B 2014, 118, 12008–12016"
pdf_sha256: "afa01e785856fd907e673d7b40880bb3b4691aefae16f11dfa55a82e1354eb5f"
pdf_path: "papers/Zhang_JPC_B_IL_CO2_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014zhang-venue-jp5054277 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Zhang, van Duin, and Johnson develop a **ReaxFF** description for **\[P(C\(_4\))\(_4\)\]\[Gly\]** ionic liquid interacting with **CO\(_2\)**, targeting simultaneous **physical sorption**, **complexation**, and **chemisorption** channels that fixed-bond force fields cannot represent. The training set combines **periodic DFT** reaction pathways in the condensed phase, **condensed-phase MD** configurations, and **gas-phase cluster** interactions for intra-ion and ion–CO\(_2\) contacts. The abstract reports that optimized parameters reproduce key **DFT/experiment/classical** benchmarks and that **MD** distributions of **C(CO\(_2\))–N(anion)** distances and **CO\(_2\)** bending angles broadly match **DFT-MD**. A predicted **density increase** with CO\(_2\) loading up to at least **50 mol %** is attributed partly to the compact effective volume of **chemically bound** CO\(_2\). The introduction motivates **amino-acid-derived ionic liquids** as tunable sorbents where **IR** and **NMR** evidence in prior work already indicates **carbamate-like** reaction channels that fixed-charge force fields cannot follow consistently.

## Methods

**Force-field training (ReaxFF for \[P(C\(_4\))\(_4\)\]\[Gly\] + CO\(_2\)).** The parametrization trains against **periodic DFT** **reaction pathways** between **CO\(_2\)** and **\[Gly\]\(^{-}\)** in the **condensed phase**, **condensed-phase MD** configurations, **gas-phase** **CO\(_2\)–anion** and **CO\(_2\)–cation** interactions, and **gas-phase cluster** models for **intra-ion** contacts (abstract). Optimized parameters are stated to reproduce **physical** and **chemical** interactions against **experiment**, **DFT** with **van der Waals** corrections, and—where purely **physical**—selected **classical** benchmarks (abstract). **QM** program settings, optimization weights, and full tables live in **`papers/Zhang_JPC_B_IL_CO2_2014.pdf`**/**SI** (**N/A** for transcription here).

**MD application (condensed-phase benchmarks).** **ReaxFF** **molecular dynamics** (**MD**) on **\[P(C\(_4\))\(_4\)\]\[Gly\]**/**CO\(_2\)** **supercells** samples probability distributions for the **C(CO\(_2\))–N(anion)** distance and the **CO\(_2\)** **bend angle**, compared to **DFT-based MD** for the same observables (abstract). **MD** also predicts **mixture density** versus **CO\(_2\)** mole fraction up to at least **50 mol %** **CO\(_2\)** (abstract). **Periodic** (**PBC**) condensed-phase **boundary** conditions are implied by the **DFT-based MD** comparisons. Concrete **LAMMPS** **NVT**/**NpT** staging, timestep, **thermostat**/**barostat** settings (including **Nosé–Hoover** damping values on the sibling methods page), **equilibration**/**production** **durations** (**ps**/**ns**), **temperature** setpoints, and **pressure** control (**1 atm** **NpT** density benchmarks) for this **DOI** are summarized on **`[[2014zhang-venue-research]]`** and in **`papers/Zhang_JPC_B_IL_CO2_2014.pdf`** (**N/A** for full numeric transcription on this page).

**Static QM.** **Periodic DFT** pathways and **DFT-based MD** supply training/validation references (abstract); detailed functional/basis/k-mesh tables are **N/A** on this page.

## Findings

The parametrization is framed as capturing **multiple** **CO\(_2\)–IL** interaction strengths—**physisorption**, **complexation**, and **chemisorption**—within one **reactive** model so sampling does not require ad hoc mixing of pre- and post-reacted phases (abstract + introduction themes on **IR**/**NMR** evidence for **carbamate-like** chemistry). **ReaxFF MD** versus **DFT-based MD** agreement on key **distance** and **angle** distributions supports using the field for **ionic-liquid** **CO\(_2\)** screening workflows. The authors further predict **density** increases with **CO\(_2\)** loading up to at least **50 mol %**, attributing part of the trend to the comparatively **small effective volume** of **chemisorbed** **CO\(_2\)**—presented as a **testable** experimental signature (abstract).

## Limitations

- Viscosity and transport of real supported-IL configurations (noted in related experimental literature in the introduction) remain partially outside the excerpted scope.
- Quantitative binding free energies and full reaction networks require full-text tables.

## Relevance to group

**Adri C. T. van Duin** co-authorship; extends **ReaxFF** to **CO\(_2\)+ionic-liquid** reactive sorption, connecting to separations and carbon-capture modeling use cases.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp5054277](https://doi.org/10.1021/jp5054277)

## Related topics

- [[reaxff-family]]
