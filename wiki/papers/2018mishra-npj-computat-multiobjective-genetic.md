---
id: paper:2018mishra-npj-computat-multiobjective-genetic
type: paper
title: Multiobjective genetic training and uncertainty quantification of reactive
  force fields
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:ml-atomistic
- domain:reaxff-lineage
- domain:reactive-md
- material:tmd
- method:reaxff
- task:parameterization
- scale:atomistic
paper_keywords:
- keyword:reaxff-parameterization
- keyword:qm-training-data
- keyword:aimd
- keyword:gpu-md
- keyword:method-development
candidate_tags: []
source_refs: []
doi: 10.1038/s41524-018-0098-3
year: 2018
authors:
- Ankit Mishra
- Sungwook Hong
- Pankaj Rajak
- Chunyang Sheng
- Ken-ichi Nomura
- Rajiv K. Kalia
- Aiichiro Nakano
- Priya Vashishta
venue: npj Comput. Mater. 2018, 4, 42
pdf_sha256: cae57c5dc11b9e8870ec615e80bf64043bc85ddb58709ec1dea50aa5e44ad11e
pdf_path: papers/ReaxFF_others/Mishra_Hong_NPJ_CompMat_2019_ML_ReaxFF_training.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018mishra-npj-computat-multiobjective-genetic -->

## Summary

Reactive force fields such as **ReaxFF** are widely used to reach nanosecond-to-microsecond reactive trajectories, but parameterization is often posed as a **single-objective** fit to a limited set of quantum references. This **npj Computational Materials** article introduces an **in situ multiobjective genetic algorithm (iMOGA)** that trains ReaxFF models while comparing **reactive MD (RMD)** trajectories to **ab initio MD (QMD)** **on the fly**, maintaining a **Pareto front** over multiple **quantities of interest (QoI)** rather than collapsing everything into one score. The workflow is engineered for **scalability**: coupled **RMD**, **QMD**, and **GA** ranks communicate through **interprocess communication** to avoid disk-bound trajectory exchanges that would bottleneck large-scale optimization. The demonstration application targets **high-temperature sulfidation** of **MoO\(_3\)** by **H\(_2\)S**, a **far-from-equilibrium** process relevant to **MoS\(_2\)** **chemical vapor deposition** chemistry, where trajectory-level agreement is arguably more informative than static energy matching alone.

## Methods

Optimization uses a **multiobjective genetic algorithm** with **nondominated sorting** to retain **Pareto-optimal** ReaxFF parameter sets that jointly address competing QoI targets (rather than averaging errors into a single loss). Training compares **RMD** and **QMD** trajectories generated during optimization, enabling the GA to reward models that reproduce **time-dependent** observables of the reactive environment. The software coupling strategy (detailed in the article) distributes work across ranks and minimizes file I/O overhead. For the **Mo–O–S–H** demonstration, the authors refine parameters appropriate to **H\(_2\)S** reaction with **MoO\(_3\)** **flakes** at **elevated temperature**, with reference QMD settings and RMD integration choices specified in the methods and supplementary materials of the publication.

### MD application (sulfidation demonstration)

**Molecular dynamics** couples **reactive MD** (**ReaxFF**) to **ab initio MD** (**QMD**) **trajectories** inside the optimization loop; the publication and **SI** name the **MD** driver(s) and integration settings (**N/A — LAMMPS vs other engine** not duplicated on this summary page). **System & composition:** **MoO\(_3\)**-derived **flake** supercells exposed to **H\(_2\)S**-relevant **Mo–O–S–H** chemistry (**atom** counts and **stoichiometry** in **Methods**). **PBC:** **three-dimensional periodic** cells for the reactive sulfidation setup. **Ensemble / thermostat / barostat / timestep / duration:** **N/A — NVE/NVT/NPT labels, thermostat type, fs timestep, and equilibration vs production ns** not transcribed here—copy from the **PDF**/**SI** before reproducing runs. **Temperature:** **elevated** **thermal** conditions for high-rate sulfidation (exact **K** in **Methods**). **Pressure:** **N/A — hydrostatic pressure** protocol not summarized in this abstract-level note; confirm whether **NPT** appears in the primary **Methods**. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** beyond **genetic** exploration of force-field parameters.

### Force-field training (iMOGA)

**Parent / scope:** **ReaxFF** for **Mo–O–S–H** updated in situ during **iMOGA**. **QM reference:** **QMD** trajectories supply **DFT**-level **energies** and forces for on-the-fly comparison. **Training set:** reactive **H\(_2\)S** + **MoO\(_3\)** environments emphasizing **trajectory**-level QoI rather than static **energy** points alone. **Optimization:** **multiobjective genetic algorithm** with **Pareto** sorting over competing QoI. **Reference data:** **QMD** benchmarks and published **QM** settings in **Methods**/**SI**.
## Findings

The authors report that **trajectory-level** training can approach **QMD** behavior for the sulfidation process studied, in the sense summarized by their QoI metrics and comparative plots. A central claim is that the **Pareto ensemble** of force-field solutions provides **uncertainty quantification (UQ)** that single-objective fits do not: practitioners can inspect spread across nondominated models when making predictions. For the **MoO\(_3\)** sulfidation case, the work is presented as a proof that **practical** ReaxFF refinement for **CVD-relevant** **reactive** pathways can be carried out with explicit **multiobjective** structure, not only as a post hoc sensitivity check.

**Corpus honesty.** QoI definitions and numerical tolerances are in the **PDF**/**SI**; this summary tracks the **open-access** abstract language only.

## Limitations

Cost remains high even with scalable coupling; **QMD** reference quality, time-step choices, and ReaxFF functional limits still bound **transferability** beyond the training chemistry.

## Relevance to group

Documents a modern **data-driven** ReaxFF optimization paradigm with explicit **UQ**, complementary to manual parabolic training workflows common in hand-tuned ReaxFF development.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/s41524-018-0098-3](https://doi.org/10.1038/s41524-018-0098-3)

## Related topics

- [[reaxff-family]]
