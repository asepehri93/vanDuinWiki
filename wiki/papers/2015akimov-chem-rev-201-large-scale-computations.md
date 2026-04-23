---
id: paper:2015akimov-chem-rev-201-large-scale-computations
type: paper
title: "Large-Scale Computations in Chemistry: A Bird's Eye View of a Vibrant Field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - task:review
  - scale:multiscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:dft-static
  - keyword:machine-learning-potential
  - keyword:classical-ff
  - keyword:polarizable-ff
  - keyword:enhanced-sampling
candidate_tags: []
source_refs: []
doi: "10.1021/cr500524c"
year: 2015
authors:
  - "Alexey V. Akimov"
  - "Oleg V. Prezhdo"
venue: "Chem. Rev."
pdf_sha256: "3b9dc0f4aa2212d89d85a154d48370d1dfbecab5244b77f151b52159f3156f36"
pdf_path: "papers/ReaxFF_others/ChemRev_ReactiveDynamics_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015akimov-chem-rev-201-large-scale-computations -->

## Summary

Computational chemistry now routinely targets systems and timescales that exceed brute-force high-level electronic structure, motivating a layered toolkit of approximations spanning wave-function theory, density functional theory, semiempirical models, fragmentation and embedding methods, polarizable force fields, bond-order reactive potentials, and machine-learned surrogates. This *Chemical Reviews* article provides a panoramic survey of “large-scale” computations interpreted broadly: large atom counts, long dynamics, combinatorial configuration spaces, and massive parallelism, often requiring combinations of strategies rather than a single acceleration trick. The narrative organizes methods by physical motivation versus computational motivation, then closes with outlook on force-field scope expansion and the persistent need for fast empirical layers even as *ab initio* methods improve.

## Methods

This *Chem. Rev.* article is a **survey**: it does not report a single benchmark MD trajectory, unified force-field refit, or standalone DFT benchmark study authored as new primary data. The “Methods” are instead a **literature comparison protocol**—sections on wave-function and density-functional foundations, physically motivated approximations (semiempirical lines such as CNDO/INDO/MNDO/PM, **DFTB**, and related routes), density-based empirical schemes, bond-order reactive frameworks (**ReaxFF-class** potentials among them), and computationally motivated accelerators (fragmentation, direct optimization / density-matrix ideas, QM/MM and quantal force-field embeddings, polarizable force fields), plus a closing outlook on software ecosystems and why empirical layers remain necessary as *ab initio* hardware and algorithms improve (`papers/ReaxFF_others/ChemRev_ReactiveDynamics_2015.pdf`). **Experimental or continuum** primary studies are outside the review’s organizing frame.

Executable settings (timesteps, functionals, basis sets) for any cited work must be taken from the **original papers** tabulated in each subsection, not inferred from this overview.

## Findings

The review formalizes five meanings of “large scale” in the field: large system size with unfavorable scaling exponents, long physical times requiring enormous integration steps, combinatorial exploration of configurations, use of many compute nodes, and combinations thereof. It argues that practical workflows interleave physically motivated reductions (semiempirical models, DFTB, reactive bond-order potentials, polarizable force fields) with algorithmic accelerators (fragmentation, direct optimization, embedding) tailored to the bottleneck at hand. Bond-order sections position ReaxFF within reactive molecular mechanics lineages alongside related empirical reactive frameworks, so readers can situate reactive MD relative to other empirical reactive frameworks without treating any single survey section as a parameter cookbook. Concluding remarks anticipate force fields that move beyond ground-state energies toward excited states and spin-dependent phenomena, while reaffirming that semiempirical and force-field layers remain essential for mesoscale phenomena.

## Limitations

Any survey risks partial coverage of fast-moving subfields; readers should treat the review as orientation rather than an exhaustive benchmark of modern machine-learning potentials or GPU-era software stacks post-dating some references.

## Relevance to group

The article gives external scholarly context for ReaxFF within large-scale computational chemistry, supporting curriculum-style links from the knowledge base to methods taxonomy pages.

## Citations and evidence anchors

Peer-reviewed DOI: [10.1021/cr500524c](https://doi.org/10.1021/cr500524c); corpus PDF `papers/ReaxFF_others/ChemRev_ReactiveDynamics_2015.pdf`.

## MAS / retrieval notes

Use this review for “big picture” methodology questions—scaling laws, fragmentation, polarizable force fields—rather than specific ReaxFF parameter sets. When answering about bond-order methods, point to Section 3.3 in the PDF outline and downstream citations for implementation details.

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
