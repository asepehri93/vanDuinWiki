---
id: paper:2010two-phase-thermodyna-venue-paper
type: paper
title: "Two-phase thermodynamic model for efficient and accurate absolute entropy of water from molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:method-development
  - keyword:water-interfaces
  - keyword:classical-md
  - keyword:nvt-simulation
  - keyword:validation-experiment
canonical_tags:
  - domain:water-silica-geo
  - domain:methods-software
  - method:classical-md
  - task:method-development
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp103120q"
year: 2010
authors:
  - "Shiang-Tai Lin"
  - "Prabal K. Maiti"
  - "William A. Goddard III"
venue: "Journal of Physical Chemistry B 114 (24), 8191–8198 (2010)"
pdf_sha256: "cf1559baa73ba9ea1b7389a4257eceaad6bf10a4e2dfa20944328d869bda8fb3"
pdf_path: "papers/Others/two-phase-thermodynamic-model-for-efficient-and-accurate-absolute-entropy-of-water-from-molecular-dynamics-simulations.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2010two-phase-thermodyna-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Thermodynamic claims follow the paper **abstract** and introduction. Water models enumerated there include **F3C, SPC, SPC/E, TIP3P, TIP4P-Ew**.

## Summary

The authors extend the **two-phase thermodynamic (2PT)** model—originally for monatomic fluids—to **molecular systems** by treating rotational density of states analogously to translational modes (gas-like vs hindered solid-like partitions). From MD trajectories, **density of states** are obtained from **velocity autocorrelation** spectra; a **fluidicity parameter** partitions diffusive vs nondiffusive contributions so that **quantum statistics** can be applied without the **infinite-entropy** pathology of misapplied harmonic formulas for diffusive modes. The abstract reports validation for several **water models** at ambient conditions, entropy along the **vapor–liquid coexistence curve** from the **triple point** to the **critical point**, and **converged liquid entropy** in **tens of picoseconds** of simulation.

## Methods


The **two-phase thermodynamic (2PT)** model **post-processes** classical **molecular dynamics** trajectories of **molecular fluids**. **Density of states (DoS)** for **translation**, **rotation**, and **intramolecular vibration** are obtained from **Fourier transforms** of the corresponding **velocity autocorrelation functions**. A **fluidicity parameter** \(f\) (inferred from the same MD trajectory/state information) partitions **translational** and **rotational** modes into a **diffusive, gas-like** part (the abstract quotes **\(3Nf\)** diffusive translational modes in the stated formulation) and a **nondiffusive, solid-like** part. **Quantum statistics** are applied to the **solid-like** partition, while **hard-sphere / rigid-rotor** statistics treat the **gas-like** partition—this split is motivated to avoid the **infinite-entropy pathology** that comes from applying harmonic formulas blindly when the DoS has **finite zero-frequency** weight associated with **diffusion**.

**1 — MD application (underlying simulations).** The abstract validates 2PT on several **rigid/semi-rigid water models** (**F3C**, **SPC**, **SPC/E**, **TIP3P**, **TIP4P-Ew**) and along the **vapor–liquid coexistence curve** from the **triple point** to the **critical point**. **N/A —** MD **program**, **ensemble**, **timestep**, **thermostat/barostat**, **system sizes**, and **PBC** details are **not stated** in `normalized/extracts/2010two-phase-thermodyna-venue-paper_p1-2.txt`—consult **`pdf_path`** for the production MD protocols feeding 2PT.

**2 — Force-field training.** **N/A —** not applicable; 2PT is a **trajectory analysis** layer atop a given classical model.

**3 — Static QM / DFT.** **N/A —** not the central method in the abstracted description.

**Checklist closure (indexed pages).** **System / composition:** **water** (**H\(_2\)O**) **molecular** fluids and rigid/semi-rigid **SPC**/**TIP3P**/**TIP4P-Ew**/**F3C**/**SPC/E** models (abstract). **Atom** counts per box: **N/A —** not stated on pp. 1–2. **Ensemble:** **N/A — NVT**/**NPT**/**NVE** for the underlying MD feeding 2PT is not stated in the excerpt. **Duration / stages:** abstract notes **tens of picoseconds** for converged **liquid** entropy extraction (**ps**/**ns** context). **Temperature:** **ambient** liquid water benchmarks imply **~298 K** class conditions as in typical literature comparisons, but **N/A — explicit thermostat setpoint** lines are not excerpted here. **Pressure:** vapor–liquid coexistence implies **pressure** along the coexistence curve is part of the validation target, but **N/A — explicit barostat** protocol is not on pp. 1–2.

## Findings

**Limiting correctness.** 2PT is stated to reproduce **exact** thermodynamic behavior in the **nondiffusive solid** limit (**\(f\to 0\)**) and the **ideal-gas** diffusive limit (**\(f\to 1\)**).

**Water benchmarks (abstract).** For **ambient liquid water**, entropies from 2PT agree with **literature** results for **F3C**, **SPC**, **SPC/E**, **TIP3P**, and **TIP4P-Ew**. Along **liquid–vapor coexistence** from **triple point** to **critical point**, **liquid** and **vapor** entropies match **reference** data in the authors’ tests.

**Sampling efficiency.** The abstract reports **converged liquid entropy** from **tens of picoseconds** of MD when combined with 2PT analysis—positioning 2PT as **efficient** for **absolute entropy** extraction from short trajectories **given adequate underlying MD**.

**Limitations / outlook.** **N/A —** detailed author limitations and uncertainty budgets are **not excerpted** on pp. 1–2; read the discussion in **`pdf_path`**.

**Corpus honesty.** Grounding here is **`pdf_path`** plus `normalized/extracts/2010two-phase-thermodyna-venue-paper_p1-2.txt`; numerical tables beyond the abstract require the PDF.

## Limitations

2PT accuracy depends on trajectory length, force-field quality, and the quantum corrections employed; it is a post-processing layer atop any classical MD engine, not a ReaxFF-specific method.

## Relevance to group

Thermodynamic analysis tool adjacent to **MD workflows** used alongside **ReaxFF** for aqueous interfaces and solvation studies.

## Citations and evidence anchors

- DOI: `10.1021/jp103120q`.
- PDF: `papers/Others/two-phase-thermodynamic-model-for-efficient-and-accurate-absolute-entropy-of-water-from-molecular-dynamics-simulations.pdf`.
- Extract: `normalized/extracts/2010two-phase-thermodyna-venue-paper_p1-2.txt`.

## Related topics

- [[theme-water-silica-geo]]
- [[themes-index]]
