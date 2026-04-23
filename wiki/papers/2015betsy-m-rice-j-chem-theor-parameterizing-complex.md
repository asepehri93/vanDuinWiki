---
id: paper:2015betsy-m-rice-j-chem-theor-parameterizing-complex
type: paper
title: "Parameterizing Complex Reactive Force Fields Using Multiple Objective Evolutionary Strategies (MOES): Part 2: Transferability of ReaxFF Models to C-H-N-O Energetic Materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:nve-simulation
  - keyword:energetic-materials
candidate_tags: []
source_refs: []
doi: "10.1021/ct5007899"
year: 2015
authors:
  - "Betsy M. Rice"
  - "James P. Larentzos"
  - "Edward F. C. Byrd"
  - "N. Scott Weingarten"
venue: "J. Chem. Theory Comput."
pdf_sha256: "0739085d444f6e7a5ebd565cb9a87f9be45c0a1f5542a1778aae0cd44c4d189c"
pdf_path: "papers/ReaxFF_others/Rice_MOES_JCTC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015betsy-m-rice-j-chem-theor-parameterizing-complex -->

## Summary

**Part 2** of the authors’ **MOES** series asks whether **Pareto-optimal** **ReaxFF** and **ReaxFF-lg** parameter sets discovered for **RDX** can **transfer** to other **C–H–N–O** **energetic** crystals without hand-tuned **per-compound** refits. **Multiple Objective Evolutionary Strategies (MOES)** searches high-dimensional parameter spaces under **several QM-derived objectives** simultaneously, returning **families** of fits rather than a single weighted optimum. The paper first **optimizes** **RDX**-centric **training** targets, then **screens** candidate parameter sets with **fixed-protocol** **LAMMPS** **molecular dynamics** on **RDX** and on **five** additional **energetic** solids (**HMX**, **PETN**, **TATB**, **nitromethane**, **TATP**) using identical **integration**, **thermostat**, **barostat**, and **stress-control** stages spelled out in the Methods section.

## Methods

**Force-field training (MOES on ReaxFF / ReaxFF-lg).** **Multiple Objective Evolutionary Strategies (MOES)** search high-dimensional ReaxFF parameter spaces under several QM-derived objectives simultaneously, returning **Pareto** families of parameter sets rather than a single weighted optimum for **RDX**-centric training data enumerated in the article (`papers/ReaxFF_others/Rice_MOES_JCTC_2015.pdf`).

**MD application (crystal screening in LAMMPS).** All post-optimization screenings use **LAMMPS** with a uniform **0.25 fs** timestep on **three-dimensional periodic boundary conditions (PBC)** crystal cells for each explosive listed below. The staged protocol tabulated in the Methods section alternates **NVE** and **NVT** blocks (**2.5 ps**, **10,000** steps each), **NPT** blocks (**7.5 ps**, **30,000** steps), and **N\(_s\)T** anisotropic-stress control segments (**25 ps**, **100,000** steps) at **300 K** for **RDX**, **HMX**, **PETN**, **TATB**, **nitromethane**, and **TATP** crystals. Thermostat and barostat damping constants are **0.05 ps** and **0.5 ps**, respectively, as stated in the paper. Supercell dimensions and initial crystal setups are listed in the same tables.

**Static QM / DFT reference data:** QM objectives feeding MOES follow the benchmarks cited in the article (see tables for targets).

**Replica / electric field / AIMD production:** **N/A —** not part of the screening workflow described above.

## Findings

MOES identifies **Pareto-efficient** parameter sets that meet or exceed the baseline **ReaxFF-lg** **crystal-density** and **structural** targets for **RDX** under the screening metrics tabulated in the article. **Two** MOES-derived models **match or outperform** **ReaxFF-lg** across the **six** **energetic** crystals in the **transferability** battery, suggesting that **multi-objective** search can surface **reactive FF** parameters that are **not** narrowly overfit to a **single** explosive. The discussion frames MOES as a practical **global** optimizer for **ReaxFF**-class **bond-order** forms where **manual** weight tuning is fragile, while still warning that **coverage** of **training** chemistries bounds **confidence** outside the **C–H–N–O** set tested here and that loading conditions beyond the fixed-protocol crystal tests require independent validation.

## Limitations

MOES search is expensive; transferability tests cover only the six **C–H–N–O** crystals in the battery. Energetic materials outside the training envelope require refitting or independent validation.

## Relevance to group

Illustrates **evolutionary multi-objective** fitting for **ReaxFF**-class models on **energetic** chemistry—adjacent to broader **reactive FF** practice in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/ct5007899](https://doi.org/10.1021/ct5007899)

## Related topics

- [[reaxff-family]]
