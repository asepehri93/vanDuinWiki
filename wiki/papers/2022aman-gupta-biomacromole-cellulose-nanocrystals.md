---
id: paper:2022aman-gupta-biomacromole-cellulose-nanocrystals
type: paper
title: "Cellulose Nanocrystals: Tensile Strength and Failure Mechanisms Revealed Using Reactive Molecular Dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - domain:mechanics-tribology
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1021/acs.biomac.1c01110"
year: 2022
authors:
  - "Aman Gupta"
  - "Ali Khodayari"
  - "Adri C. T. van Duin"
  - "Ulrich Hirn"
  - "Aart W. Van Vuure"
  - "David Seveno"
venue: "Biomacromolecules"
pdf_sha256: "54248f368359119b1adc308a9af70935e689b1f0f388e70c6f43facef1974809"
pdf_path: "papers/Gupta_acs.biomacro_Cellulose_Tensile_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022aman-gupta-biomacromole-cellulose-nanocrystals -->

## Summary

Crystalline I\(_\beta\) cellulose is modeled as a finite 36-chain cellulose nanocrystal (CNC) with explicit fibril twist using the CHON-2017\_weak ReaxFF parameterization. Uniaxial tensile tests in LAMMPS quantify elastic modulus, ultimate strength, and failure pathways, including strain-rate extrapolation toward laboratory rates. The study targets **nanocellulose** mechanics where **glycosidic** scission competes with **hydrogen-bond** rearrangement during **load**.

## Methods

Structures are built from cellulose I\(_\beta\) crystallography and relaxed with conjugate-gradient minimization, staged heating (1–300 K) in NVT with a Nosé–Hoover thermostat, and an integration timestep of 0.1 fs. Equilibration at 300 K establishes ~1°/nm twist and hydrogen-bond patterns compared against GLYCAM reference data. Tensile loading fixes clamped end groups and applies constant engineering strain rates from 4.301 ns\(^{-1}\) down to 0.05 ns\(^{-1}\); lower effective rates reuse restarts after ~8% strain to limit cost. Bond failure is tracked via ReaxFF bond orders with a 0.3 cutoff. Axial modulus and ultimate properties are extracted from engineering stress–strain curves; a nonlinear model extrapolates ultimate tensile strength and strain toward 1 s\(^{-1}\). **Chiral** twist variants are included to test sensitivity of failure to fibril handedness at the same nominal strain history.

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.
## Findings

The axial elastic modulus at 0.1 ns\(^{-1}\) is reported as 146.1 ± 0.5 GPa, matching prior GLYCAM06 stress–strain behavior for the same degree of polymerization. Ultimate tensile strength and strain decrease with decreasing strain rate in the simulated window; extrapolation yields about 9.2 GPa ultimate strength and 8.5% ultimate strain at 1 s\(^{-1}\), with stated large uncertainty. Failure is dominated by C4–O4 glycosidic bond scission (31 of 36 chains in a representative 0.05 ns\(^{-1}\) test), not hydrogen-bond breaking, although O3H···O5 hydrogen-bond counts drop sharply during loading. Left- and right-hand twists give overlapping stress–strain curves and the same primary bond failure channel. The authors connect this **bond-level** picture to **composite** reinforcement discussions where **CNC** axial properties set upper bounds for **matrix**-embedded fibers.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

ReaxFF inherits carbohydrate crystal parameterization trade-offs (e.g., elongated \(c\)-axis); simulated strain rates remain far above experiment, and defects/solvent are omitted. **Water** and **surface** **hydroxyl** equilibria in real **CNC** suspensions could shift failure statistics relative to these dry crystallite models.

## Relevance to group

Direct ReaxFF/LAMMPS study co-authored by van Duin on nanocellulose mechanics and bond-level failure. The work complements **organics** and **biopolymer** threads in the knowledge base that otherwise emphasize **pyrolysis** or **combustion** hydrocarbons.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.biomac.1c01110

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
