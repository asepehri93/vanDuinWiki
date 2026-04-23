---
id: paper:2026jeong-venue-manuscript
type: paper
title: "Development of a ReaxFF Reactive Force Field for the Crystallization of van der Waals-Layered Bismuth Selenide"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:2d-layered
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - material:tmd
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5c07042"
year: 2026
authors:
  - "Ga-Un Jeong"
  - "Ryan Morelock"
  - "Soumendu Bagchi"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Panchapakesan Ganesh"
venue: "J. Phys. Chem. C"
pdf_sha256: "de50132381c1d97ce00bf166a059b8862b14861c4cbfb748c8056dab26d79960"
pdf_path: "papers/Jeong_JPCC_BiSe_2026_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026jeong-venue-manuscript -->

## Summary

A **Bi/Se ReaxFF** **parameterization**—trained to **VASP**-**PBE**+**D3** data on **bulk**, **defective**, **cluster**, and **melt-quench amorphous** **structures**—enables **melt-quench** **MD** (**ADF** and **LAMMPS**) that **recrystallize** **amorphous** **Bi₂Se₃** toward **vdW**-**layered** **tetradymite** **order**, with **stacking** and **stoichiometry** sensitive to the **thermal** **schedule**. **DFT** supplies **convex**-hull-consistent **formation** **energies**, **equation-of-state** **scans**, **defect** **energies**, **high-T** **cluster** data, and **melt**-**quenched** **amorphous** **geometries**; **MD** benchmarks **recrystallization** **vs** **cooling** and **annealing** **knobs**.

## Methods

- **DFT training (VASP 6.4.2):** **GGA-PBE** with **Grimme D3 (BJ)**; **520 eV** cutoff; **0.03 eV** Gaussian smearing; **spin-polarized** totals; **Γ-centered** *k*-meshes via **Pymatgen** (**≥2000 / N_atoms** density); **Materials Project** crystals relaxed to **0.0001 eV/atom** and **0.01 eV/Å** forces; **Bader** charges. **EoS** scans (**85–115%** volume) for **rhombohedral Bi₂Se₃**, **rocksalt BiSe**, **vdW Bi₈Se₉**; **defects** via **pymatgen-analysis-defects** (**antisites**, **interstitials**, **~11% Se vacancy** trial) with **fixed lattice**, relaxed ions.
- **ReaxFF optimization:** Start from published **Bi** and **Se** parameter subsets; optimize **Bi–Se** bonds and selected **valence** cross terms via **successive single-parameter parabolic extrapolation**; full table in **SI**.
- **Melt-quench MD:** **ADF** and **LAMMPS**; **135-atom** **trigonal vdW Bi₂Se₃** supercell equilibrated **300 K**, **NPT**, **0.25 fs**, **Berendsen** thermostat (**100 fs**) and barostat (**5000 fs**) for **25 ps** → density **6.83 g/cm³**, box **~12.73 × 12.69 × 30.73 Å**; melt-quench in **NVT**, **0.5 fs**, **0 → 5000 K** at **20 K/ps**, **hold 5000 K / 50 ps**, **cool to 2000 K** at **2 K/ps**, **hold 2000 K / 100 ps**, **quench to 0 K** at **2 K/ps**; **partial RDFs** assess **recrystallized** order.

**1 — MD application (atomistic dynamics).** **LAMMPS**/**ADF** **reactive MD**; **135**-**atom** **supercell** **(Bi₂Se₃)**; **3D** **PBC**; **NPT** **equilibration** then **NVT** **melt**-**quench** **(anneal** **ramp** **stages** above); **Berendsen** **thermostat**/**barostat** on the **NPT** leg; **0.25**/**0.5 fs** **time step**; **~25**–**hundreds** of **ps** per **stage**; **N/A** — no **static electric field**; **N/A** — no **replica**/**metadynamics**; **N/A** — **Hydrostatic** **pressure** in **NPT** is not quoted here in **GPa**; see the **galley** for **1 atm**-equivalent **targets**.

**2 — Force-field training.** **Parent** **ReaxFF** **Bi**+**Se** **parameter** sets; **QM** **VASP 6.4.2** **GGA**-**PBE**+**D3 (BJ)**, **520 eV** **cutoff**, **Pymatgen**-set **k**-mesh, **Bader** **charges**; **training** on **formation** **energies**, **EoS** **(Bi₂Se₃**, **BiSe**, **Bi₈Se₉)**, **defect** **(antisites, interstitials, ~11% Se V trial)**, **melt**-**quenched** **amorphous**; **parabolic** **successive** **one**-**parameter** **ReaxFF** **optimization**; full **table** in **SI**.

**3 — Static QM / DFT-only (training reference, not a standalone DFT “application” paper in isolation from fits).** Covered in the **VASP** list above; **N/A** for extra **NEB**/**AIMD** **production** in this page’s **scope**.

**4 — Review** — **N/A.**
## Findings

- The **ReaxFF** reproduces **DFT convex-hull ordering** (Bi₂Se₃ most stable) and **EoS** trends for key phases; **Bi₂Se₃ heat of formation** is **overstabilized** by **~4.6 kcal/(mol atom)** versus **DFT**, discussed as **acceptable** for **recrystallization** studies by analogy to prior **vdW** fits.
- **Melt-quench** trajectories show **vdW**-**layered** **recovery** whose **stacking**, **stoichiometry**, and **defect** **content** depend on **cooling** **rate**, **anneal** **temperature**, and **hold** **time**; **sensitivity** links **kinetic** **processing** to **tetradymite**-like **order**; **outlook** toward **TI**/**thermoelectric** use is in the main text. **Comparisons:** **ReaxFF** **heat of formation** **over**-**stabilized** by **~4.6** **kcal/(mol atom)** **vs** **DFT** (acceptable for **structural** **kinetics** per the authors’ discussion).

- **Limitation (authored view):** **ReaxFF** at **extreme** **volumes** and **electronic** **topology** of **TI** **physics** are not targets—see `## Limitations`.

## Limitations

Repository PDF is an **ACS galley**; **final pagination** may differ from the **version of record**. **ReaxFF** errors at **extreme volumes** for **Bi₂Se₃** are acknowledged; **electronic topological** properties are **not** targeted by the classical model.

## Relevance to group

**Adri C. T. van Duin** co-leads the **parameterization** with **ORNL** / **Ganesh** group co-authors (**Jeong**, **Bagchi**, **Morelock**, **Nayir**).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5c07042](https://doi.org/10.1021/acs.jpcc.5c07042)

## Related topics

- [[reaxff-family]]
