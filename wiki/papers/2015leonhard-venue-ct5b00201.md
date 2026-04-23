---
id: paper:2015leonhard-venue-ct5b00201
type: paper
title: "Automated discovery of reaction pathways, rate constants, and transition states using reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:methods-software
  - method:reaxff
  - method:dft-static
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:neb
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.5b00201"
year: 2015
authors:
  - "Malte Döntgen"
  - "Marie-Dominique Przybylski-Freund"
  - "Leif C. Kroeger"
  - "Wassja A. Kopp"
  - "Ahmed E. Ismail"
  - "Kai Leonhard"
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "f50ded287ec9fbb7d3fc6393016506e705b0143b733dc52c87d09c3472d3188a"
pdf_path: "papers/ReaxFF_others/Leonhard_ReaxFF_analysis_JCTC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015leonhard-venue-ct5b00201 -->

## Summary

Kinetic models of combustion and polymerization networks are widely used, but their rate parameters are hard to measure for elementary steps that are not isolated experimentally, and hand-built mechanisms can embed incorrect topology or kinetics. Döntgen et al. present a workflow that turns reactive molecular dynamics trajectories into quantitative reaction models by automatically identifying elementary reactions from changing atom connectivities, integrating species production along individual channels to infer rate constants, and harvesting transition-state geometries from trajectory segments for nudged elastic band refinement and optional ab initio follow-up. They demonstrate the pipeline on the inception stage of methane oxidation using ReaxFF simulations, comparing inferred pathways and rates to literature benchmarks. The introduction contrasts prior heuristic mechanism generators and expensive ab initio nanoreactor approaches with the authors’ graph-based analysis of classical reactive trajectories, emphasizing that their goal is quantitative agreement with established methane oxidation references rather than discovery chemistry at extreme artificial temperatures alone.

## Methods

**Reactive MD (methane oxidation inception).** **LAMMPS** **ReaxFF** trajectories use the **Chenoweth *et al.* hydrocarbon oxidation** parameterization cited in the article. **System composition:** **30 CH\(_4\)** and **60 O\(_2\)** molecules in a **cubic** **periodic** cell sized from the target **density 1125 mol m\(^{-3}\)** via the **ideal gas law** as described. **Temperatures:** **2000–2400 K**, corresponding to **~185–222 atm** ideal-gas pressures as stated. For each temperature, **ten** independent **Maxwell–Boltzmann** velocity samples are drawn for the same initial positions; each run lasts **5 ns** with **Δt = 0.1 fs** and a **Nosé–Hoover** thermostat (**damping 10 fs**). The first **~1 ns** is discarded for **vibrational thermalization** diagnostics described in the paper.

**Post-processing (ChemTraYzer).** **Bond-order** filtering (ReaxFF-style) plus **graph** algorithms identify molecules and **elementary reactions**; integrated **production** along channels feeds the **rate-constant** estimates validated for **first-order** cases in **SI Section S1**. **Transition-state** candidates harvested from trajectories seed **NEB** refinements and optional **QM** follow-up as described.

**Force-field training / static QM.** **N/A —** the manuscript **consumes** an existing **ReaxFF** table; **QM** appears as **validation/refinement**, not as a full new DFT parametrization workflow in the main text.

**Barostat, electric fields.** **N/A —** constant-volume **gas-phase** **NVT**-style thermalization as implemented in the protocol above.

## Findings

The abstract states that pathways and rates from the automated analysis agree with available literature data for the demonstration system sufficiently to illustrate the method’s potential for building quantitative reaction models from reactive MD. The article positions reactive MD not only as a qualitative pathway discovery tool but as a source of parameters that can feed mechanism files when sampling is adequate and the force field is trustworthy for the chemistry at hand. Practically, the demonstration shows that automated post-processing can reduce manual bookkeeping for large reactive networks while still permitting quantum refinement on selected channels. Readers should treat the inferred network as a hypothesis to be tested against independent sampling or higher-fidelity electronic structure where stakes are high.

## Limitations

Accuracy is bounded by ReaxFF fidelity to quantum chemistry and by finite sampling; rare events may be missed, and automatic transition-state harvesting depends on trajectory density near dividing surfaces.

## Relevance to group

Methodological bridge between ReaxFF trajectories and kinetic models relevant to combustion and reactive MD post-processing.

## Citations and evidence anchors

DOI `10.1021/acs.jctc.5b00201`.

## Related topics

- [[reaxff-family]]
