---
id: paper:2018wei-physical-che-molecular-dynamics
type: paper
title: Molecular dynamics simulation on the mechanical properties of natural-rubber-graft-rigid-polymer/rigid-polymer
  systems
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:organics-polymers-pyrolysis
- material:polymer-organic
- method:classical-md
- scale:atomistic
- task:application
paper_keywords:
- keyword:polymer
- keyword:classical-ff
candidate_tags: []
source_refs: []
doi: 10.1039/C7CP07807B
year: 2018
authors:
- Meng Wei
- Pengxiang Xu
- Yizhong Yuan
- Xiaohui Tian
- Jinyu Sun
- Jiaping Lin
venue: Phys. Chem. Chem. Phys.
pdf_sha256: b84ed2e4a46802475a7658fa02100be06ccd7dd7137f3ea9ae2cc1c0fc1534e2
pdf_path: papers/Others/Wei-2018-Molecular-dynamics-simulation-on-th.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018wei-physical-che-molecular-dynamics -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **PCCP** article identified by `doi`, `title`, and `pdf_path`. It paraphrases the publication’s stated models and conclusions without adding independent scientific claims.

## Summary

Wei *et al.* study **mechanical response** of **natural rubber** that is **grafted** with **rigid polymer** chains and blended with additional **rigid polymer**, using a **coarse-grained (CG) bead–spring** framework designed to capture the essential **topology** and **interaction** trends of **latex**-like composites. The architecture highlighted in the paper is **N\(_{30}\)-g-(R\(_3\))\(_6\)/R\(_{10}\)**, where **graft count**, **graft length**, and **rigid fraction** become knobs that alter **stress–strain** behavior under **uniaxial tension**. The authors sweep **strain rate**, **nonbonded interaction strength** among rigid beads, and **composition** to map how **modulus**, **yield**, and post-yield response change, and they compare trends to **experimental** measurements on analogous **latex blends** where such data are available. The work sits squarely in the **polymer mechanics** literature: it seeks interpretable scaling laws from a deliberately simplified **CG** model rather than atomistic chemical fidelity.

## Methods

### Coarse-grained model and code

**Coarse-grained bead–spring** chains represent **NR** and **rigid** inclusions; **Lennard–Jones** interactions between rigid beads use a tunable attraction strength. All simulations are run in **LAMMPS** with the **velocity-Verlet** integrator. Reduced units are used throughout: temperature **T = 1.0**, timestep **Δt = 0.004 τ** during initial diffusion, and **Δt = 0.001 τ** for tensile **NVT** segments (with **τ** the unit time defined in the paper).

**Composition / system size:** the **PCCP** article discusses **N\(_{30}\)-g-(R\(_3\))\(_6\)/R\(_{10}\)** architectures with on the order of **~9000** polymer **beads** after packing in an initial **100 × 100 × 100** (reduced-unit) box before compression to the target **volume fraction**—see **`papers/Others/Wei-2018-Molecular-dynamics-simulation-on-th.pdf`** for exact **bead** inventories per figure.

### Equilibration and tensile **MD**

Chains are first relaxed in **NVT** at large **periodic** box volume with a **soft cosine repulsion** (**A = 20.0**, form eq. (4) in the article) for **10 000** steps to remove overlaps, then the box is compressed to **volume fraction 0.45**. **NPT** equilibration at **P = 0** and **T = 1.0** follows using a **Nosé–Hoover barostat and thermostat** for **5 × 10⁷** timesteps until energy and morphology plateau (see Fig. S2, ESI). **Nonequilibrium** tensile tests then deform the **cubic** cell to a **cuboid** under **NVT** at **T = 1.0** with **constant engineering strain rate** (typically **0.2 τ⁻¹**, comparable to segmental relaxation as stated). Stress follows the **virial** expression (eqs. (5)–(6)); **Poisson’s ratio** is fixed at **0.5** for the in-plane contraction used in their stress definition.

- **System size / bead counts:** **N/A — not restated** in this summary; the **PCCP** article and **ESI** tabulate box sizes and bead totals for each **N₃₀-g-(R₃)₆/R₁₀** variant.

- **Electric field / replica / metadynamics:** **N/A — not used**.

- **Absolute experimental temperature mapping:** **N/A — CG** **T = 1.0** maps to laboratory **K** only through the parametrization discussed in the paper, not reproduced here.
## Findings

The simulations show that **higher strain rate** increases the apparent **elastic modulus** and **yield stress**, consistent with rate-dependent **dissipative** response in polymer networks. **Stronger attraction** between rigid beads and higher **rigid** content both raise **stress** and **modulus**, but the benefit **saturates** at large rigid fractions when the matrix becomes overly brittle or stress localizes. **Graft architecture** matters in a non-monotonic way: increasing the number of **grafts** raises stress at **small strain** by distributing load transfer, while **longer grafts** increase stress more strongly at **large strain** by maintaining connectivity during extension. The grafted architectures outperform **ungrafted** **NR/rigid** blends in the metrics reported, and the authors relate these trends to **experimental** observations on **latex** composites cited in the paper.

## Limitations

**Coarse graining** removes **chemical** detail; absolute **moduli** depend on the chosen **CG** mapping and **LJ** parameters. The study does not address **aging**, **cross-link** polydispersity, or **fatigue** at experimental timescales.

## Related topics

- [[theme-pyrolysis-combustion-organics]]
