---
id: paper:2026mirakhory-venue-paper
type: paper
title: "Dynamics of iodine geminate recombination in supercritical xenon solvent: Caging effect"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1063/5.0302862"
year: 2026
authors:
  - "M. Mirakhory"
  - "A. Majumdar"
  - "M. Ihme"
  - "A. C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "bd04b662332a7fcad59c87ff90f161709f011474c1187b97e709613c0112f9c6"
pdf_path: "papers/Mirakhory_JCP_2026_Xe_I_II.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2026mirakhory-venue-paper -->

## Summary

Reactive molecular dynamics with a ReaxFF parametrization for Xe/I is used to study iodine geminate recombination in supercritical xenon, emphasizing solvent clustering ("caging"), local density enhancement around iodine, and energy transfer to xenon. The work distinguishes primary versus secondary geminate pathways as a function of confinement and controlled dissociation intervals.

## Methods

Primary source: version-of-record PDF at `papers/Mirakhory_JCP_2026_Xe_I_II.pdf` (J. Chem. Phys. 164, 094309 (2026)).

**Force field.** ReaxFF for the Xe/I system from prior work, trained to quantum data including CASSCF(6,8) for I-I, DFT for Xe/Xe, Xe/I, collinear and perpendicular Xe-I2 pairs and I-I-I angles, and CCSD for Xe-Xe; parameters optimized by successive single-parameter search.

**Systems and ensembles.** Main periodic boxes with 10 000 Xe atoms and 250 I atoms (I/Xe = 1:40); additional runs at 1:80 (125 I) and 1:200 (50 I) with fixed Xe density. Energy minimization, then multiple-thermostat NVT at 290 K and pressures from 2 to 200 bar for recombination-rate surveys; local-density and coordination analysis at 290 K and 58.98 bar. Berendsen thermostat: damping 1000 fs on Xe, 1 000 000 fs on I (near-NVE iodine). Timestep 0.25 fs; production 1 ns per run; periodic boundaries; ten independent randomized ensembles averaged where stated.

**Cluster and dissociation protocols.** Smaller 500-Xe cells with manual insertion of dissociated I2 into large Xe clusters. Larger 10 000 Xe / 125 I2 systems: temporary deactivation of the I-I bond dissociation term in ReaxFF for 100, 200, or 300 fs to mimic dissociation, then restoration and 1 ns multiple-thermostat NVT at 290 K and 58.98 bar.

**Limitations stated in the article.** ReaxFF follows ground-state dynamics; electronically excited states of I2 are not explicitly represented, consistent with prior treatments that place fragments on the ground surface before geminate recombination.

**1 — MD application (atomistic dynamics).** As above: LAMMPS ReaxFF **molecular dynamics** in **periodic** **3D** **cells**; **NVT** at **290 K**; **0.25 fs** **time** **step**; **1 ns** **production**; **2–200 bar** state points; **multi-thermostat** **Berendsen**; **N/A** — no **NPT** **barostat** in the main **NVT** **protocol**; **N/A** — no **static** **electric** **field**; **N/A** — no **replica**/**metadynamics**; **1 ns** **(290** **K**, **58.98** **bar)** for **local**-**density** **analyses**; **100–300** **fs** **bond**-**off** **I₂** **splitting** for **pathway** **labeling**.

**2 — Force-field training (application of prior ReaxFF).** As in the **Force field** paragraph.

**3 — Static QM / DFT-only** — **N/A** (QM data only enter the **ReaxFF** training).

**4 — Review** — **N/A.**
## Findings

- Iodine recombination rate is highest near supercritical conditions; lower pressure reduces collisions and yields less stable recombination, while higher pressure slows iodine diffusion and lowers the recombination rate.
- At recombination, local xenon density is at least about 2.5 times the bulk density, with coordination-number analysis supporting xenon clustering around iodine.
- Correlation of xenon cluster energy with recombined iodine supports kinetic-energy transfer from recombination into the solvent, consistent with geminate recombination.
- Iodine pairs confined in xenon clusters (manual insertion or fast dissociation in-cluster) favor primary geminate recombination; longer dissociation intervals let iodine escape the cluster and shift behavior toward secondary geminate recombination.
- Recombination events at 1:40 and 1:80 I/Xe remain spatially isolated from other iodine atoms; local xenon environment at recombination is insensitive to concentration over the range examined.

- **Comparisons / outlook:** **Near**-**critical** **vs** **low**/**high**-**P** **limits**; **ground**-state **ReaxFF** **omits** **excited**-state **I₂** (see `## Limitations`).

## Limitations

Ground-state ReaxFF model; elevated iodine concentrations relative to experiment are used to sample rare recombination events in nanosecond trajectories.

## Relevance to group

Co-authored ReaxFF parametrization and reactive MD study of solvent-mediated recombination and energy transfer (van Duin group, Penn State).

## Citations and evidence anchors

DOI: `10.1063/5.0302862`.

## Related topics

- [[reaxff-family]]
- [[2026mirakhory-venue-paper-2]]
