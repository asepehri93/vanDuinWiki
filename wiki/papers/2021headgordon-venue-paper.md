---
id: paper:2021headgordon-venue-paper
type: paper
title: "NewtonNet: A Newtonian message passing network for deep learning of interatomic potentials and forces"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:qm-training-data
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.48550/arXiv.2108.02913"
year: 2021
authors:
  - "Mojtaba Haghighatlari"
  - "Jie Li"
  - "Xingyi Guan"
  - "Oufan Zhang"
  - "Akshaya Das"
  - "Christopher J. Stein"
  - "Farnaz Heidar-Zadeh"
  - "Meili Liu"
  - "Martin Head-Gordon"
  - "Luke Bertels"
  - "Hongxia Hao"
  - "Itai Leven"
  - "Teresa Head-Gordon"
venue: "arXiv:2108.02913 [physics.chem-ph] (6 Aug 2021)"
pdf_sha256: "d67f698ade7fd665e720849ac49a63b7d92c2e7f878b88c4ce97b112afcd1888"
pdf_path: "papers/Others/HeadGordon_NN_Newton_2021.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2021headgordon-venue-paper -->

## Summary

This arXiv preprint introduces NewtonNet as a message-passing neural network for interatomic potentials that is built around Newton-inspired operators and latent vector features, rather than relying only on scalar invariant channels. In the abstract and opening pages of `papers/Others/HeadGordon_NN_Newton_2021.pdf`, the authors frame a concrete modeling gap: many modern graph models for atomistic systems can predict energies, but stable and data-efficient prediction of forces still depends on how directional information is represented and transformed under rotation.

The paper explicitly targets both energies and forces. The authors state that NewtonNet keeps rotational equivariance while using trainable latent force vectors, with the intent that the representation remains physically consistent when the input geometry is rotated. The introduction anchors the method historically in the Behler-Parrinello decomposition of total energy into atomic contributions, then contrasts feature-engineering-heavy approaches (distances, angles, dihedrals and higher-order descriptors) with learned message passing. This motivates their choice to keep end-to-end trainability but inject stronger physics priors into the architecture.

The extract also situates NewtonNet against SchNet-like continuous-filter models, PhysNet-style long-range-aware variants, and angle-aware message passing families, then argues that invariant-only internal representations can be insufficient for some 3D distinctions and vector-output tasks. Within that framing, NewtonNet is presented as an equivariant alternative intended to improve force learning quality and interpretability of the learned many-body interactions.

On benchmark scope, the abstract states that the model is tested on reactive and non-reactive ab initio datasets, including a single small-molecule dynamics setting, a chemically diverse molecular set, and methane/hydrogen combustion reactions. The authors claim state-of-the-art test performance on energies and forces plus improved data and computational efficiency relative to compared deep-learning baselines. Because this corpus extraction is only the first two pages, this wiki page preserves those claims as authored and defers exact table-level numbers and final benchmark deltas to the full preprint text and any later peer-reviewed version.

## Methods

This paper is primarily a machine-learning method paper, so the protocol is model/training/benchmark design rather than a single production molecular dynamics campaign.

- **Engine / code:** The method is described as a deep message-passing architecture (NewtonNet) in the arXiv preprint; no separate classical MD engine benchmark protocol is specified in the p1-2 extract.
- **System size and composition:** Dataset-based training/evaluation spans reactive and non-reactive molecular systems (small-molecule dynamics, chemically diverse molecules, methane/hydrogen combustion datasets), as stated in the abstract.
- **Boundaries / periodicity:** N/A in the extract; simulation-cell boundary conditions are dataset-dependent and not enumerated on the first two pages.
- **Ensemble:** N/A in the extract as a unified setting; the paper reports supervised learning on reference energies/forces rather than one explicit NVE/NVT/NPT production run.
- **Timestep:** N/A in the extract for any single production trajectory setup.
- **Duration / stages:** N/A in the extract; training/validation/test partitioning and dataset-specific trajectory lengths are documented later in the paper.
- **Thermostat:** N/A in the extract for a dedicated MD protocol.
- **Barostat:** N/A in the extract.
- **Temperature:** N/A as a single protocol parameter; inherited from source datasets.
- **Pressure:** N/A in the extract.
- **Electric field:** N/A in the extract.
- **Replica / enhanced sampling:** N/A in the extract.

For the force-field-training blueprint: this is not a ReaxFF or classical FF reparameterization, so parent FF lineage, explicit QM optimization weights, and FF parameter-table updates are N/A by design. Instead, the central methodological choices are (i) equivariant treatment of directional features, (ii) latent force-vector message channels, and (iii) joint energy/force learning on ab initio reference data. The introduction also discusses why rotational equivariance is mathematically necessary for robust vector-output models, giving the group-action perspective for transformed inputs and outputs.

Corpus honesty note: extraction quality is marked partial and limited to p1-2 (`normalized/extracts/2021headgordon-venue-paper_p1-2.txt`), so this page intentionally avoids listing optimizer hyperparameters, full ablation settings, or exact benchmark table values unless directly read from the full PDF.

## Findings

The central reported outcome is that NewtonNet attains very strong test performance for both energies and forces across the listed benchmark families, with the abstract claiming state-of-the-art accuracy and better data/computational efficiency than competing deep-learning potentials in their comparisons. The interpretation offered by the authors is that directional latent vectors and physics-inspired message operators improve force prediction because they keep symmetry handling explicit instead of forcing vector information through purely invariant internal representations.

A second contribution is conceptual rather than numeric: the paper links equivariance requirements to practical model behavior for molecular simulation. In the introduction, the authors emphasize that vectorial quantities cannot be treated as simple scalar labels under rotations. By framing equivariance as a transformation-consistency condition, they position NewtonNet as a model class designed to produce force vectors that transform correctly when molecular geometries are rotated.

The preprint also frames modern atomistic ML as a progression from hand-crafted geometric descriptors toward learned hierarchical representations, and NewtonNet is presented as an effort to retain the flexibility of learned message passing while improving physical faithfulness for dynamics-ready force prediction. In that sense, the findings are both benchmark-oriented (error/efficiency claims) and architecture-oriented (a physics-informed equivariant design rationale).

Comparisons and limits, as grounded in the available corpus text:
- The comparison set includes well-known message-passing architectures discussed in the introduction, but exact per-dataset margins are not copied here from the partial extract.
- Claims about "state-of-the-art" and "far greater efficiency" are preserved as author claims from the abstract and should be tied to specific tables before quoting numeric improvements elsewhere in the wiki.
- This is arXiv v1 in the corpus; final publication status and any revised metrics should be checked before treating these results as archival values.

## Limitations

Preprint: peer review, final benchmarks, and public code may differ from the corpus PDF.

## Relevance to group

General MLIP methodology relevant to comparison with ReaxFF and hybrid workflows; no direct ReaxFF parameterization.

## Citations and evidence anchors

- [10.48550/arXiv.2108.02913](https://doi.org/10.48550/arXiv.2108.02913) — `papers/Others/HeadGordon_NN_Newton_2021.pdf`, abstract, model definition, results.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

