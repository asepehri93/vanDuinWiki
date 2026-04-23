---
id: paper:2018zeng-venue-paper
type: paper
title: 'ReacNetGen: an Automatic Reaction Network Generator for Reactive Molecular
  Dynamic Simulations'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:methods-software
- method:reaxff
- task:software
- task:method-development
- scale:atomistic
paper_keywords:
- keyword:method-development
- keyword:reactive-md
candidate_tags: []
source_refs: []
doi: 10.26434/chemrxiv.7421534.v2
year: 2018
authors:
- Jinzhe Zeng
- Liqun Cao
- John ZH Zhang
- Chih-Hao Chin
- Tong Zhu
venue: ChemRxiv (preprint)
pdf_sha256: 8d4d2de4d4fedeef566b044b966c14feea56e28cee8fce09f4fb08a4b8b74906
pdf_path: papers/ReaxFF_others/Zeng_2018_ReacNetGen__an_Automatic_Reaction_Network_Generator_for_Reactive_Molecular_Dynamic_Simulations_v2.pdf
extraction_quality: partial
group_affiliation: false
---
<!-- id:paper:2018zeng-venue-paper -->

## Summary

ReacNetGen is a post-processing tool that constructs chemical reaction networks automatically from reactive molecular dynamics trajectories, including workflows that combine ReaxFF or related bond-order force fields with classical MD integrators. Instead of relying on hand-curated reaction lists, the software reconstructs molecular species from time-dependent atomic coordinates, then stitches elementary steps into a network graph suitable for kinetic model building and visualization. A hidden Markov model layer addresses noise in connectivity assignments caused by finite timestep discretization and thermal vibration, which otherwise produces spurious bond flicker in raw distance-based parsing. The ChemRxiv preprint documents case studies on oxidation of a four-component RP-3 jet-fuel surrogate and on methane oxidation, illustrating multi-species chemistry at scales that are tedious to annotate manually.

## Methods

**Software workflow.** ReacNetGen ingests unannotated **molecular dynamics** trajectories in which covalent connectivity can change. It clusters **atoms** into molecules with distance/topology rules suited to reactive trajectories, tracks species identities frame-to-frame, and applies a **hidden Markov model** so noisy bond-order flicker from finite **timestep** sampling and thermal motion does not dominate the inferred reaction graph. Outputs are reaction nodes and edges with stoichiometries inferred from species gains and losses, for kinetic post-processing and visualization. Algorithm choices, hyperparameters, and the RP-3 / methane case-study inputs are documented in the ChemRxiv **PDF** at `pdf_path`.

**Relation to upstream MD.** The manuscript positions the tool against **reactive MD** practice where a classical **MD** engine drives **ReaxFF** (the **Introduction** cites literature examples including large **LAMMPS**-class trajectories). ReacNetGen itself does not fix a single production protocol: **ensemble** (**NVE** / **NVT** / **NPT**), **timestep** (**fs**), **thermostat**, **barostat** / hydrostatic **pressure** control, **temperature** ramps, trajectory **duration** (**ps** / **ns**), **PBC** details, **supercell** **composition**, optional **electric field** biasing, and **enhanced sampling** (**umbrella**, **metadynamics**, **replica exchange**) are **N/A on this software page**—they belong to whichever simulation produced each archived trajectory; copy those numbers from the originating study’s **Methods** before reproducing a published network.
## Findings

The authors report that ReacNetGen yields human-interpretable networks for large RP-3 oxidation trajectories where manual reaction counting would be impractical, and that hidden Markov filtering reduces false reaction events relative to naive cutoff-based parsing. The methane demonstration is presented as evidence the pipeline generalizes across small and large mechanistic complexity, subject to the accuracy of the underlying force field. Because the workflow is downstream of MD, any missing pathways or erroneous barriers in the ReaxFF model propagate to network topology quality. For MAS use, treat extracted networks as hypothesis graphs: validate key branching ratios against quantum chemistry or experiment before importing rates into reduced kinetic models.

## Limitations

ChemRxiv status means a peer-reviewed version may differ; cite the published article if one exists beyond the preprint DOI. Network completeness depends on trajectory length, temperature, and sampling of rare channels. Corpus metadata marks extraction quality as partial—use the PDF for authoritative algorithm pseudocode and benchmark settings.

## Relevance to group

**Post-processing** tooling for **ReaxFF** (and reactive MD) trajectories—complements in-house **PuReMD/LAMMPS** combustion and oxidation workflows.

## Citations and evidence anchors

- DOI: `10.26434/chemrxiv.7421534.v2`

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
