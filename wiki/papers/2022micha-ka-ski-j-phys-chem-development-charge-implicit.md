---
id: paper:2022micha-ka-ski-j-phys-chem-development-charge-implicit
type: paper
title: "Development of a Charge-Implicit ReaxFF for C/H/O Systems"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.1c03867"
year: 2022
authors:
  - "Michał Kański"
  - "Sviatoslav Hrabar"
  - "Adri C. T. van Duin"
  - "Zbigniew Postawa"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "e5fff0e24cf88b64f482bfa425d62ad8eba77903cf1ff12c93ca28d7b289166b"
pdf_path: "papers/Kanski_JPC_letters_CHO_noQ_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022micha-ka-ski-j-phys-chem-development-charge-implicit -->

!!! abstract "Scope"

Charge-implicit ReaxFF for C/H/O removes explicit charge equilibration, runs faster than the parent parametrization, and is validated on densities and on trehalose bombardment by water clusters (SIMS context).

## Summary

ReaxFF achieves accurate reactive chemistry in condensed organics but charge equilibration (QEq) is costly. This work extends the earlier hydrocarbon charge-implicit ReaxFF to oxygen-containing systems: Coulomb contributions are folded into other ReaxFF terms so explicit electrostatics are omitted, targeting faster simulations without losing key thermochemistry and density behavior. The motivation includes **SIMS** and **organic matrix** problems where **high-energy** collisions require **stable** integration and **reactive** fragmentation without paying for **full QEq** every step.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (ReaxFF pair style) for all validation **MD**; **VMD** for visualization (*J. Phys. Chem. Lett.*).
- **System & protocols:** (i) **Density** and **thermodynamic** **benchmarks** for **C/H/O** **liquids** and **tests** in **Table 1** (e.g. **1,5-pentanediol** in systems up to **6.2×10⁵** **atoms** as tabulated) and an **o-xylene** **oxidation** **stunt** at **2,500 K** with protocol in **SI**; (ii) **SIMS**-style **(H\(_2\)O)\(_n\)** **cluster** **bombardment** of a **~60 nm**-scale **hemispherical** **trehalose** target; **(H\(_2\)O)\(_n\)** projectiles with **2**, **2.85**, and **5 eV** per **H\(_2\)O** in the main-text examples (larger-**n** and energy sweeps in **SI**; **C\(_{60}\)**-on-**ice** crater figures use **~40 nm** samples, **20 keV**, **40°** **incidence** in the main text for comparison to prior fields). **3D** **PBC** **(periodic** **boundary** **conditions)** in **the** **liquid/ice** and **bombardment** **cells** **(full** **cell** **vectors** in **SI** as **cited** in *JPCL*).
- **Ensemble & thermostating:** **Constant-volume** **NVT**-class control for equilibrated **liquids** as implied by the density studies; high-**T** **oxidation** and **impulsive** **bombardment** trajectories are **NVE**-like during **impact** in standard **SIMS**-style **setups**—**exact** **NVT**/**NVE** **switches** and **thermostat** **damping** are in **SI** where the authors separate **preequilibration** from **projectile** **impact**.
- **Timestep / barostat / pressure / field / enhanced sampling:** **N/A** — the **main** **JPCL** **pages** excerpted here do not restate a single **fs** **timestep**; **N/A** — no **NPT** **barostat**-driven **stress** control in the **summarized** **validations**; **N/A** — no **static** **electric** **field**; **N/A** — no **metadynamics** / **replica** **exchange** (kinetics from **conventional** **MD**).

### 2 — Force-field training (charge-implicit ReaxFF-CHO)

- **Parent / elements:** **Charge-implicit** **ReaxFF** for **C/H/O** built from **ReaxFF-2008 (Chenoweth** **et** **al.)** **data**; **Coulomb** is folded into **other** **terms** so **explicit** **QEq** is **omitted** in **production** **runs**.
- **QM reference & training set:** **DFT**-level **curves** for **bonds**, **reactions**, **valence**, and **dihedral** **hurdles**; augmented **table**-based **targets** for **liquid**/**vapor** **densities**, **water** **heat** of **vaporization**, and **amorphous** **ice** **cohesive** **energy** (average **density** **deviation** ~**5%** on the **fit** set per **Table 1**; **ZBL** **splicing** for **ultra**-short-**range** **repulsion** per **Ziegler**–**Biersack**–**Littmark** in **SI**).
- **Optimization:** **Successive** **single-parameter** **refinement** for **bonding**; **iterative** **nonbonding** **retuning** to match **Table 1** to **~10%** on **energies**/**densities** as stated; **ReaxFF-lg** used as a **density** **comparator** in the **article**.
- **Reference validation (throughput):** **Table 2** reports **μs (timestep)\(^{-1}\) atom\(^{-1}\)** cost—**ci-ReaxFF-CHO** is **>2×** **faster** in **step** time than the **parent** **explicit** **ReaxFF** in the **tabulated** **large**-**cell** **cases** (*JPCL* **Table 2**).
## Findings

**Speed / fidelity:** The **ci-ReaxFF-CHO** **parametrization** achieves **>2**× **wall-time** or **per-step** **gains** **vs** **conventional** **ReaxFF** in the **documented** **Table 2** **systems** while **retaining** **bond/angle/torsion** **fidelity** against **DFT** **training** data **comparable** to **ReaxFF-2008** in **mean** **deviation** on **training** **reactions** (**~17%** **vs** **~16%** in the main text for the **H-abstraction** **test**). **Densities** and **reactions** for **C/H/O** **materials** remain **usable**; **ZBL** **stitching** supports **keV**-scale **impacts** in **C\(_{60}\)**-on-**ice** **comparators**.

**SIMS mechanism:** In **(H\(_2\)O)\(_n\)**-on-**trehalose** **runs** mirroring **experiment**, **higher** **molecular** **ion** **yields** **track** **ejection** of **trehalose**–**water** **complexes** at **certain** **per-molecule** **energies** (**Figure 4** in *JPCL*), matching the **peaked** **experimental** **sensitivity** **trend** for **massive** **water** **projectiles** **(≥**~**order**-of-magnitude** **gains** cited in the **intro** and **ref** [4]).
## Limitations

Transferability to elements or chemistries outside the fitted C/H/O space requires additional extension; long-lived polarization effects may require explicit polarizable treatments in some solvents. **SIMS**-relevant **impact** conditions probe **high-energy** collisions that stress **short-range** repulsion terms; users should confirm that their **projectile** **mass** and **velocity** ranges remain within the **training** spirit of the **trehalose** benchmark cases highlighted in the article. **Charge-implicit** **runs** omit **long-range** **Coulomb** **forces**; do not use them for **electrolyte** **systems** where **explicit** **solvent** **polarization** dominates **reaction** **barriers** without additional **validation**. **Trehalose** **benchmarks** are illustrative **organic** **matrices**, not exhaustive **coverage** of **oxygenate** **chemistries**.

## Relevance to group

Co-authored method paper on accelerated ReaxFF for oxygenated organics and surface bombardment.

## Reader notes (navigation)

- [[reaxff-family]]

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.1c03867](https://doi.org/10.1021/acs.jpclett.1c03867)

## Related topics

- [[reaxff-family]]
