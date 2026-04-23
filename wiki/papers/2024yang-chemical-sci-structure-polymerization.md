---
id: paper:2024yang-chemical-sci-structure-polymerization
type: paper
title: "Structure and polymerization of liquid sulfur across the λ-transition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:reactive-md
  - method:ml-potential
  - method:aimd
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:aimd
  - keyword:enhanced-sampling
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: "10.1039/D3SC06282A"
year: 2024
authors:
  - "Manyi Yang"
  - "Enrico Trizio"
  - "Michele Parrinello"
venue: "Chem. Sci."
pdf_sha256: "6e0d76d8f0af9ef3d8e96d8141c4c0a6f38e284b0739a1a3d92dd42681de9f06"
pdf_path: "papers/Others/Parinello_group_liquid_sulfur_ChemSci_2023.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024yang-chemical-sci-structure-polymerization -->

Machine-learned interatomic potentials (DeepMD-style), CP2K reference DFT, and on-the-fly probability enhanced sampling (OPES) with a graph-spectral “Deep-TDA” collective variable are used to study ring–polymer equilibria and reaction mechanisms in liquid sulfur near the λ-transition (\(T_\lambda \approx 432\) K at 1 atm).

## Summary

The paper targets the λ-transition of liquid sulfur, associated with conversion of S\(_8\) rings to polymeric chains. Reference data use CP2K AIMD (PBE, GTH pseudopotentials, m-DZVP + plane waves, 300 Ry density cutoff for AIMD; 350 Ry with D3 for training snapshots) and single-point training on 128- and 512-atom cells. ML potentials are trained with DeepMD-kit and driven in LAMMPS; enhanced sampling uses PLUMED with OPES (well-tempered target, kernel deposition frequency 250, barrier-related parameters in the 100–200 kJ/mol range as stated) and a neural collective variable from Deep-TDA / mlcolvar, built from smoothed adjacency-matrix eigenvalue histogram inputs. Unbiased NN-driven MD (NVT, 1 fs timestep, global velocity rescaling thermostat, τ = 0.05 ps) evaluates \(g(r)\), \(S(k)\), and displacement statistics on 3456-atom and 512-atom cells; biased runs at 512 atoms explore polymerization pathways. Bader charges from DFT densities support mechanistic interpretation.

## Methods

- **Electronic structure and datasets:** CP2K 9.2; PBE; GTH pseudopotentials; AIMD in NPT (2 fs timestep, Nosé–Hoover thermostat and barostat); training snapshots with higher cutoff and D3; Bader analysis for charges on selected mechanistic snapshots.
- **NN potentials:** DeepMD-kit training; LAMMPS integration; attention-based Deep Potential variant described in the article.
- **Enhanced sampling:** PLUMED + OPES along Deep-TDA CV; adjacency matrix from pairwise cutoff switching (e.g., \(d_\text{cutoff} \approx 2.6\) Å for sulfur bonds), eigenvalue histogram featurization, NN architecture [100, 64, 32, 1], ReLU, two-state training data from ring-rich vs polymer-rich samples.
- **Structural analysis:** Radial distribution functions and structure factors compared to experiment via linear mixing of pure ring and pure polymer references; Gaussian broadening noted for \(g(r)\) comparison; displacement histograms over 10–100 ps at several ring fractions.

**1 — MD application (MLIP + reference AIMD).** Unbiased **NVT** **LAMMPS** runs (1 fs timestep, global velocity rescaling thermostat, τ = 0.05 ps) on 512- and 3456-atom periodic **bulk** **liquid** **sulfur**; **CP2K** **NPT** **AIMD** (2 fs, **Nosé–Hoover** thermostat and **barostat**) for reference trajectories and training data (article). **N/A** — no external **electric** **field** in the summarized protocol. **N/A** — no **metadynamics** or **replica** **exchange** in the *brief* list here; **rare** **ring**–**chain** **events** are targeted with **OPES** (see below).

**2 — Machine-learned potential (MLIP).** **DeepMD**-**kit** training on **CP2K** **PBE** snapshots; attention-based **Deep** **Potential** as described in the **article** (not a ReaxFF parameterization in the **AGENTS** **sense**).

**3 — Static QM (CP2K DFT).** **PBE** with **GTH** **pseudopotentials** and **m**-**DZVP** + **plane** **waves**; **300** **Ry** density cutoff (AIMD) and **350** **Ry** with **D3** for select training; **Bader** charges on **path** **frames**.

**4 — Enhanced sampling.** **PLUMED** with **on-the-fly** **probability**-**enhanced** **sampling** (**OPES**, well-tempered target) along a **graph**-**spectral** **Deep**-**TDA** **neural** **CV**; kernel deposition frequency 250; barrier-related OPES parameters in the 100–200 kJ/mol range as **reported** (article).
## Findings

1. Mixed \(g(r)\) and \(S(k)\) along experimental ring-fraction tracks match X-ray data around \(T_\lambda\), including evolution of the ~4.5 Å \(g(r)\) third peak linked to S\(_8\) neighbors; a small-\(k\) pre-peak in \(S(k)\) is less pronounced than experiment, attributed partly to finite system size.
2. Atomic mobility drops as polymer content increases, with growing population of sub-2 Å displacements consistent with sluggish polymer segments and elevated viscosity above \(T_\lambda\).
3. Polymerization mechanisms resemble ring-opening polymerization: thermal opening of an S\(_8\) ring polarizes terminal atoms; subsequent attack on other rings propagates chains; depolymerization pathways are also sampled (figures and ESI schemes).
4. The approach is presented as extending prior short AIMD by combining ab initio–accurate potentials with rare-event sampling for connectivity-changing sulfur chemistry.

**Corpus honesty** — **Parrinello**-group work, not **ReaxFF**; see **`## Limitations`** for **ML** **fidelity** and **finite** **size**.
## Limitations

Finite cell sizes and ML potential fidelity to full DFT for all transition states remain approximate; experimental ring-fraction assignments retain uncertainty that the authors acknowledge.

## Relevance to group

Complementary methodology (MLIPs + OPES) for reactive liquids; not a van Duin / ReaxFF study but relevant to reactive MD and enhanced-sampling benchmarks in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/D3SC06282A](https://doi.org/10.1039/D3SC06282A)

## Related topics

- [[reaxff-family]]
