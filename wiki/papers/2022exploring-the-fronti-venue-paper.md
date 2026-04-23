---
id: paper:2022exploring-the-fronti-venue-paper
type: paper
title: "Exploring the frontiers of chemistry with a general reactive machine learning potential"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:parameterization
  - domain:reactive-md
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:reactive-md
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.26434/chemrxiv-2022-15ct6-v3"
year: 2022
authors:
  - "Shuhao Zhang"
  - "Małgorzata Z. Makoś"
  - "Ryan B. Jadrich"
  - "Elfi Kraka"
  - "Kipton M. Barros"
  - "Benjamin T. Nebgen"
  - "Sergei Tretiak"
  - "Olexandr Isayev"
  - "Nicholas Lubbers"
  - "Richard A. Messerly"
  - "Justin S. Smith"
venue: "ChemRxiv (preprint)"
pdf_sha256: "37713c4ff26de2ae6f7fd359e9da642580cab157e7f159f97caa1d1063fc05ab"
pdf_path: "papers/Others/exploring-the-frontiers-of-chemistry-with-a-general-reactive-machine-learning-potential.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2022exploring-the-fronti-venue-paper -->

## Summary

The authors train a general reactive machine-learning interatomic potential (denoted ANI-nr in the preprint; later referred to as ANI-1xnr in the Nature Chemistry version of record) using active learning with a nanoreactor-inspired sampler that explores condensed-phase reactions for C/H/N/O compositions without hand-built reaction lists. Benchmark applications span carbon nucleation, graphene formation from acetylene with oxygen, biodiesel-relevant ignition chemistry, methane combustion, and prebiotic glycine formation scenarios. The ChemRxiv abstract stresses that prior reactive **MLIPs** usually required **application-specific datasets** and **known reaction networks**, whereas ANI-nr is trained **without** enumerating reactions beforehand and is tested on **five** distinct condensed-phase systems, matching experiment or prior high-level simulations in each showcase.

## Methods

Training iterates between neural-network potentials (ANI architecture), nanoreactor-like MD sampling that drives rare chemistry, uncertainty-guided selection of new configurations, and DFT labeling of energies/forces. Longer-range cutoff variants (e.g., ANI-nr(lr)) test sensitivity to electrostatic and stacking interactions. Comparisons reference Hartree–Fock/DFT/DFTB, classical reactive models, and non-transferable MLIPs where available. The introduction contrasts **ReaxFF** and related reactive force fields with **QM**, noting that empirical reactive models demand **per-system parameterization** and **expert-curated reaction lists**, whereas **DFT** is transferable but costly for \(\gtrsim\) nanosecond condensed-phase trajectories—motivating **MLIPs** with **active learning** to harvest diverse **bond-making/breaking** configurations automatically.

## Findings

Across the case studies, ANI-nr reproduces experimental observables when available and aligns with high-level electronic-structure references or established reactive simulations without refitting per system. The sampler is reported to populate diverse bond-breaking/forming events needed for condensed-phase reactivity, yielding a single transferable potential for multiple chemistries. The abstract claims ANI-nr is **highly general** and does **not** need refitting per application, enabling **high-throughput in silico** reactive chemistry; the PDF introduction further positions **ANI-1x**-class models as accurate for gas-phase organics while **ANI-nr** targets periodic liquids, supercritical fluids, and solids where earlier ANI releases were not trained.

## Limitations

Training cost and DFT labeling remain bottlenecks; performance outside C/H/N/O chemistries is out of scope. Readers should cite the peer-reviewed Nature Chemistry article (DOI 10.1038/s41557-023-01427-3) for the editorially finalized text and naming (ANI-1xnr).

## Relevance to group

Shows MLIP + active-learning workflows parallel to ReaxFF parameterization efforts; cites ReaxFF as a classical reactive baseline.

!!! note "Later version of record"
    The peer-reviewed article appears in *Nat. Chem.* (2024) under the expanded title “Exploring the frontiers of **condensed-phase** chemistry …” with DOI `10.1038/s41557-023-01427-3`. This corpus PDF matches the earlier ChemRxiv preprint filename.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
