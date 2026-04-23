---
id: paper:2016jovana-andrejevic-j-chem-theor-ct5b00918
type: paper
title: "Simple molecular reactive force field for metal–organic synthesis"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:classical-ff-specialized
  - domain:catalysis-surfaces
  - method:reactive-md-generic
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:classical-ff
  - keyword:qm-training-data
  - keyword:reactive-md
source_refs: []
doi: "10.1021/acs.jctc.5b00918"
year: 2016
authors:
  - "Jovana Andrejevic"
  - "James Stevenson"
  - "Paulette Clancy"
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "113382b3e1098973ff01403c795059c2def24062fa4dcd94d02a0d5d25744c6e"
pdf_path: "papers/Others/Simple Molecular Reactive Force Field for Metal–Organic Synthesis.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016jovana-andrejevic-j-chem-theor-ct5b00918 -->

## Summary

Colloidal synthesis of PbS quantum dots involves bond making and breaking in solution at scales where ab initio molecular dynamics is impractical and fixed-bond force fields miss chemistry. This *J. Chem. Theory Comput.* article introduces a deliberately minimal reactive potential—Morse, Lennard-Jones, and Coulomb terms tailored to PbS cores passivated by lead oleate–like ligands—parameterized so large-scale reactive sampling is feasible while retaining enough physics for nucleation-relevant events. The abstract states that the model reproduces reactions across a broad range of quantum dot sizes with good accuracy and that validation includes comparison to ab initio calculations for a reaction between two dots. This is not a ReaxFF paper; it is included in the corpus as a comparator for reactive force-field design outside bond-order formalisms.

## Methods

The authors motivate solution-phase nucleation of PbS quantum dots capped by lead oleate complexes and argue that five interacting elements (Pb, S, and ligand chemistry) make transferable bond-order potentials cumbersome for this target system. They construct a custom reactive potential from Morse, Lennard-Jones, and Coulomb components so bonds can form and break during dynamics, and they fit parameters to an ab initio / DFT benchmark set spanning dot sizes and surface or ligand configurations along nucleation pathways, using nonlinear least-squares–style refinement described in the full **Methods** section of the paper. Figure 1 sketches how passivated PbS dots are partitioned into core and surface complex regions.

The introduction motivates **molecular dynamics** of colloidal **PbS** nucleation at **300 K**-class solution-processing temperatures while noting that **atoms**-scale reactive sampling is the target capability. Figure 1 delineates passivated dot **composition** (core versus surface complex); **boundary** conditions, integrator package, timestep, thermostat, barostat, and trajectory length for production runs are **not** stated on the indexed excerpt—consult the *JCTC* **Methods** (DOI above). **N/A — production ensemble (NVT vs NPT vs NVE):** not specified on the excerpted pages. **N/A — hydrostatic pressure control:** not stated where dynamics protocols are omitted. **N/A — applied electric field:** not discussed on the excerpted pages. **Force-field training:** as above—purpose-built reactive model fit to DFT benchmarks (this paper’s core contribution). **Standalone DFT materials campaign:** **N/A**—DFT supplies training and validation data, including the dot–dot reaction highlighted in the abstract.

## Findings

The abstract reports that the custom potential reproduces reactions across a broad range of PbS quantum dot sizes with good accuracy and captures a dot–dot reaction pathway consistent with ab initio reference data. The introduction positions the model as a pragmatic bridge between DFT accuracy on small clusters and the need to sample nucleation free-energy landscapes at larger scales, with explicit trade-offs in generality versus specialized reactive potentials such as COMB or ReaxFF. Transferability to other ligands, solvents, or surface reactions outside the training manifold is not claimed on the excerpted pages.

## Limitations

Transferability to ligands, solvents, and surface reactions outside the training manifold requires reparameterization; interoperability with ReaxFF datasets is not automatic.

## Reader notes (MAS / retrieval)

Tag as non-ReaxFF reactive FF for PbS quantum-dot synthesis; cite *JCTC* Methods for reproducibility.

## Relevance to group

Peripheral corpus reference illustrating alternative reactive force-field strategies complementary to ReaxFF-centric workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.5b00918](https://doi.org/10.1021/acs.jctc.5b00918) — *J. Chem. Theory Comput.* **12**, 825–838 (2016).

## Related topics

- [[reaxff-family]]
