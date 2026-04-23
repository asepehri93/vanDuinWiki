---
id: paper:2017ponce-venue-jp7b04190
type: paper
title: "Analysis of a Li-Ion Nanobattery with Graphite Anode Using Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:classical-ff
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b04190"
year: 2017
authors:
  - "Victor Ponce"
  - "Diego E. Galvez-Aranda"
  - "Jorge M. Seminario"
venue: "J. Phys. Chem. C"
pdf_sha256: "da052a8433cea159f4525c068da5273a717a119dd8963a9bbe54f4565b07672f"
pdf_path: "papers/Others/Ponce_JPCC_battery_nonreactiveFF_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017ponce-venue-jp7b04190 -->

!!! abstract
Classical MD in LAMMPS models a full nanoscale Li-ion cell: B3PW91-parameterized EC/LiPF₆, UFF+LJ mixing, Tersoff graphite, composite cathode/SEI/insulator regions, external electric fields for charging—reports energies, dipoles, drift, conductivity vs field.

## Summary

**Classical MD** with **LAMMPS** models a **Li-ion nanobattery**: **graphite anode**, **LiCoO₂ cathode**, **1.15 M LiPF₆ in ethylene carbonate** electrolyte, **Cu- and Au-like collectors**, **SiOₓ-like insulator**, optional **SEI** (**Li₂CO₃-like** stoichiometry per article). **Packmol** builds electrolyte starting coordinates (**21 ion pairs**, **310 EC** molecules in **1.15 M** cell excerpt). **Force fields:** **CFF93** base with **Gaussian-09 B3PW91/cc-pVTZ**-fitted **bond/angle/dihedral** parameters for **EC** and **LiPF₆**; **UFF** LJ mixing rules with **pair-specific adjustments** to prevent unphysical penetration; **Mulliken/NBO** charges for Coulombics; **Tersoff (Lindsay et al.)** for in-plane graphite plus **LJ** interlayer; cathode/electrode regions parameterized as described in **Tables 1–3**. **Equilibration:** **1 ns at 5 K**, ramp to **293 K in 4 ns**, **10 ns NVT**; charging applies **external electric fields** along the cell (**0.2–1.5 V/Å** range in reported runs, with varying simulated duration). Observables include **energy, temperature, volume, polarization, MSD**, **Li flux to anode**, **conductivity/resistivity** vs field, and **SEI** permeation behavior. The setup is intentionally a **nanoscale testbed** with **large** effective fields relative to macroscopic cells.

## Methods

### 1 — MD application (atomistic dynamics)

**Classical MD** in **LAMMPS** models a **nanoscale Li-ion cell** with **graphite** anode, **LiCoO₂** cathode, **Cu-/Au-like** current collectors, a **SiOₓ-like insulator** region, and **1.15 M** (also **3.36 M**) **LiPF₆** in **ethylene carbonate** electrolyte built with **Packmol** (example stoichiometry in the article: **21 LiPF₆ ion pairs** with **310 EC** molecules for the **1.15 M** cell caption). **Periodic boundary conditions** apply to an initial orthorhombic cell **166.6 × 27.0 × 58.2 Å³** (Fig. 1). Integration uses the **Verlet leapfrog** algorithm. **Equilibration** follows **1 ns at 5 K**, a **4 ns** ramp to **293 K**, then **10 ns NVT** at **293 K** before **charging** trajectories that impose **external electric fields** along the cell axis (field strengths, polarization diagnostics, and segment lengths are tabulated in the article body beyond the indexed p1–2 excerpt).

- **Engine / code:** **LAMMPS** classical MD with **Verlet** integration (*J. Phys. Chem. C* **2017**, **121**, 12959–12971).
- **System size & composition:** **Graphite** (Tersoff + interlayer LJ), **LiCoO₂** cathode block, **EC + LiPF₆** electrolyte, optional **SEI** region modeled with a **Li₂CO₃-like** stoichiometry, and **AX₂-like** insulator spacer—full parameter tables in **Tables 1–3** of the article.
- **Boundaries / periodicity:** **3D PBC** on the nanobattery supercell (Fig. 1b–c).
- **Ensemble:** **NVT** for the **10 ns** **293 K** equilibration segment described in the figure caption; charging stages continue under field-driven dynamics as detailed in **Methodology** (see PDF for thermostat specifics beyond the indexed excerpt).
- **Timestep:** **N/A** — integration **Δt (fs)** is not stated on the indexed p1–2 pages; confirm in the full **Methodology** section.
- **Duration / stages:** **1 ns** at **5 K**, **4 ns** heating ramp to **293 K**, **10 ns NVT** equilibration at **293 K**, followed by **field-on charging** segments of lengths reported with each field strength in the article.
- **Thermostat:** **N/A** — explicit thermostat identity/damping not reproduced from the indexed excerpt; confirm in the PDF.
- **Barostat:** **N/A** — equilibration segment quoted is **NVT** without **NPT** barostat control in the indexed caption.
- **Temperature:** **5 K** start, ramp to **293 K** equilibration target as in Fig. 1 caption.
- **Pressure:** **N/A** — isochoric **NVT** equilibration; no barostat summary on indexed pages.
- **Electric field:** **Static external fields** along the cell axis mimic voltage sources during **charging**; field magnitudes and polarization diagnostics are central observables in the article.
- **Replica / enhanced sampling:** **N/A** — brute-force MD with applied **E-field**.

### 2 — Force-field training / classical parameterization

**Non-reactive** classical potentials: **intramolecular EC** parameters from **Gaussian B3PW91/cc-pVTZ** optimizations (**Table 1** excerpt); **LiPF₆** bonded terms similarly **DFT-fitted**; **LJ cross terms** largely **UFF**-based with **pair-specific adjustments** to avoid unphysical overlap; **Mulliken/NBO-derived** partial charges for Coulombics; **Tersoff (Lindsay et al.)** in-plane **graphite** plus **LJ** interlayer; cathode/current-collector regions use the literature parameterization summarized in **Tables 1–3**. **Not** a ReaxFF reparameterization study.

### 3 — Static QM / DFT-only

**B3PW91/cc-pVTZ** **DFT** supplies **bond/angle/dihedral** reference data for **EC** (and related) intramolecular terms; **not** AIMD production.

## Findings

### Outcomes and mechanisms

Charging under **applied electric fields** drives **Li⁺** migration from **cathode** toward **graphite**, with time traces for **energy, temperature, volume, polarization, MSD**, and **Li flux** reported in the article. **Polarization** of the solvent rises approximately **linearly** with accumulated charge until a **saturation** regime where additional charging stalls because energy input from the external source drops to very low levels—interpreted as the nanobattery reaching an effectively **fully polarized** electrolyte state.

### Comparisons

The authors compare simulated **conductivity / resistivity**, **current density**, and related transport metrics against **available experimental conductivity data** for **EC/LiPF₆** solutions, reporting **qualitative consistency** within the limitations of the classical model.

### Sensitivity / design levers

**Electrolyte concentration** (**1.15 M vs 3.36 M**) and **external field magnitude** modulate **Joule-like heating**, **Li⁺ drift**, and **conductivity**; at high fields the **3.36 M** cell shows **stronger heating** than **1.15 M** under otherwise similar conditions (article discussion).

### Limitations and corpus honesty

Model is **classical and non-reactive**—no bond-making/breaking for **SEI** chemistry beyond the simplified **Li₂CO₃-like** layer used to probe **Li⁺ permeation**. **Field strengths** are **nanoscale testbed magnitudes** and are not direct macroscopic cell voltages. Indexed excerpt covers **early methodology pages**; quantitative tables/figures should be taken from the **DOI-linked PDF** when citing numbers beyond this summary.


## Limitations

Classical non-reactive force fields—no bond-breaking electrolyte decomposition; fields are large compared to laboratory cells (nanoscale testbed). **Charge transfer** beyond fixed **partial** charges and **electrochemical** **polarization** at true **voltages** are not represented at full **QM** fidelity.

## Relevance to group

**Non-ReaxFF** battery MD reference in corpus; contrasts with reactive workflows elsewhere.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.7b04190`

## Related topics

- [[batteries-interfaces-reaxff]]
