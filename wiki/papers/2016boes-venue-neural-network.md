---
id: paper:2016boes-venue-neural-network
type: paper
title: "Neural network and ReaxFF comparison for Au properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:reaxff
  - method:ml-potential
  - domain:alloys-metallurgy
  - task:parameterization
  - task:validation
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:machine-learning-potential
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1002/qua.25115"
year: 2016
authors:
  - "Jacob R. Boes"
  - "Mitchell C. Groenenboom"
  - "John A. Keith"
  - "John R. Kitchin"
venue: "Int. J. Quantum Chem."
pdf_sha256: "ce4ed3bf9519d7e4ee481300438169b498309678456d437c92e50d46f0dd2e27"
pdf_path: "papers/ReaxFF_others/Boes_et_al-2016-International_Journal_of_Quantum_Chemistry.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016boes-venue-neural-network -->

## Summary

Machine-learned interatomic potentials and physics-based reactive force fields are both trained against **Kohn–Sham DFT** data, but they differ in flexibility, data efficiency, and cost per MD step. This *International Journal of Quantum Chemistry* paper uses **gold** as a deliberately simple, **screened** single-component metal to compare **ReaxFF** against **Behler–Parrinello neural-network (BPNN)** potentials across **bulk**, **surface**, **cluster**, and **pathway** (e.g., **NEB**) regimes. The study asks how much training data each model class needs to be reliable, where each breaks down, and what trade-offs appear when the goal is broad coverage of structural chemistry rather than a single narrow application. The overarching motivation is practical: practitioners need guidance on when a compact reactive FF is sufficient versus when a high-capacity regressor is warranted, and what validation splits are meaningful across regimes.

## Methods

### MD application (atomistic dynamics)

This paper is a **potential-energy-surface benchmarking** study: headline data are **static KS-DFT** energies/forces on **bulk**, **surface**, **cluster**, and **NEB** configurations used to train and test **ReaxFF** and **Behler–Parrinello neural networks**, not reported **finite-temperature molecular dynamics** production trajectories.

- **Engine:** **N/A —** no **LAMMPS**/**GROMACS**/**CP2K** **molecular dynamics** trajectories are reported as primary results; **VASP** supplies **DFT** reference forces/energies.
- **System size & boundaries:** training cells vary by task (**bulk EOS**, **surfaces**, **≤126-atom clusters**, **NEB** images); **periodic boundary conditions (PBC)** follow the **VASP** setups described in **Methods**, but there is **not** one fixed **MD** supercell for the whole paper.
- **Ensemble / timestep / thermostat / barostat / duration (production MD):** **N/A —** not in scope because the contribution is **DFT-labeled fitting** rather than **NVT**/**NPT**/**NVE** **MD** sampling.
- **Electric field:** **N/A — not used.** **Replica / enhanced sampling:** **N/A —** training uses **relaxation pathways** and **climbing-image NEB** images, not umbrella sampling or replica-exchange **molecular dynamics**.

### Force-field training (ReaxFF)

- **Parent FF / elements:** **ReaxFF** for **Au** (reactive bond-order formulation as described in the article’s background).
- **QM reference data:** **Kohn–Sham DFT** computed in **VASP** using **PBE-GGA** and **PAW** pseudopotentials; **Monkhorst–Pack** **k** grids at least **14×14×14** for a single Au atom in the primitive ground-state reference; **plane-wave cutoff ≥ 300 eV** targeting **≤5 meV/atom** energy convergence; relaxations to **<0.05 eV Å⁻¹** (Methods section).
- **Training set scope:** **9,972** KS-DFT calculations total (**905** bulk, **1,022** surface, **8,045** cluster), mostly intermediate relaxation images; **896** additional local minima / **NEB** images.
- **Optimization:** **Monte Carlo Force Field optimization (MCFFopt)** in **ADF** for **ReaxFF** parameter searches.
- **Best-fit data count (reported):** A strong **ReaxFF** model trained from **848** points performs well on **bulk/surface** held-out data but remains comparatively weak for **≤126-atom clusters** in their tests; expanding training can **overfit** and **degrade** transfer.

### Force-field training (Behler–Parrinello neural network)

- **Software:** **AMP** (Peterson/Khorshidi) integrated with **ASE** for **BPNN** training; trained-parameter details stored as **JSON** in Supporting Information (as stated in the article).
- **Training set scope:** Example large fit uses **9,734** KS-DFT calculations from the same pool.
- **Performance claim:** **BPNN** matches or exceeds **ReaxFF** across the tested **bulk/surface/cluster** regimes in their benchmarks, with **higher per-step computational cost** in the implementation discussed.

### Static QM / DFT (KS reference generator)

Same **VASP/PBE/PAW** settings as above; **climbing-image NEB** used where transition states are reported (unless otherwise noted in the Methods text).

## Findings

- **ReaxFF vs BPNN trade-off:** **ReaxFF** can reach strong **bulk/surface** accuracy with **far fewer** training points, but is **much weaker** on **small Au clusters (≤126 atoms)** in the reported errors.
- **Overfitting warning:** For **ReaxFF**, **adding more training data** does **not** monotonically improve held-out performance and can **hurt** transfer—an explicit caution about automated reactive fits on heterogeneous datasets.
- **BPNN scaling:** **BPNN** benefits from **large** training coverage and tracks or beats **ReaxFF** across regimes in their tests, at higher MD-step cost in the studied implementation.
- **System choice rationale:** **Au** is used partly because **screened metallic** interactions reduce the role of long-range electrostatic extremes, making the comparison a cleaner probe of **short-ranged PES** modeling between **physical** and **machine-learned** potentials (with the article’s caveat that **polar/ionic** systems add further requirements).

## Limitations

Transfer to oxides, electrolytes, or charged interfaces requires different datasets and validation. Reported timings and cost models depend on NN architecture and software path.

## Relevance to group

Benchmark culture for **ReaxFF** versus **neural** potentials on metals—adjacent to MLIP discussions in reactive MD communities.

## Citations and evidence anchors

- DOI: [10.1002/qua.25115](https://doi.org/10.1002/qua.25115)

## Related topics

- [[reaxff-family]]
