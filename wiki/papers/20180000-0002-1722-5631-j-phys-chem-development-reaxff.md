---
id: paper:20180000-0002-1722-5631-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF reactive force field for NaSiOx/water systems and its application to sodium and proton self-diffusion"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b05852"
year: 2018
authors:
  - "Seung Ho Hahn"
  - "Jessica Rimsza"
  - "Louise Criscenti"
  - "Wei Sun"
  - "Lu Deng"
  - "Jincheng Du"
  - "Tao Liang"
  - "Susan B. Sinnott"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "1a9c05337dd865fde073654a42472ff598931f9a6852c46b7d8f190d50debc52"
pdf_path: "papers/Hahn_NaSiOx_JPCC_2018_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20180000-0002-1722-5631-j-phys-chem-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **J. Phys. Chem. C** article identified by `doi`. **Glass** **composition** and **QM** **functional** choices are in the **Methods/SI**.

## Summary

A **Na/Si/O/H ReaxFF** parametrization is developed for **sodium silicate–water interfaces**, trained on quantum-mechanical data for crystalline NaSiO\(_x\) equations of state, Na\(^+\) migration barriers in silicate structures, hydroxylated silica interacting with Na\(^+\)–water environments, and **[NaOH·\(H_2O\)_n]** cluster dissociation energies. After optimization, the authors validate **crystal and glass structures**, **Na\(^+\)** and **proton** transport in amorphous matrices, and **NaOH dissociation** in bulk water, then relate the results to **glass dissolution** scenarios (interdiffusion, subsurface transport to interfacial vacancies, leaching). **Nuclear waste** **glass** **leaching** and **geochemical** **weathering** both require **reactive** models that allow **Si–O–Na** network **hydrolysis** while capturing **mobile** **Na\(^+\)** and **H\(_3\)O\(^+\)** transport (introduction themes).

## Methods

### Force-field training (ReaxFF, Na–Si–O–H)

The work extends the **ReaxFF** bond-order framework to **Na/Si/O/H** for **sodium silicate–water** chemistry. **Parent** models build on prior **Si/O/H** and glass–water ReaxFF lines cited in the article. **QM reference data** come from **DFT** calculations used to fit **equations of state** of **NaSiO\(_x\)** crystals, **Na\(^+\)** migration **barriers** in silicate hosts, **hydroxylated silica** interacting with **Na\(^+\)**–**water** clusters, and **[NaOH·(H\(_2\)O)\(_n\)]** dissociation energies (**\(n=1\)–\(6\)**) as summarized in the abstract. **Optimization** refits bonded, **vdW**, and **Coulomb/QEq**-related terms until those training targets are matched; full functional/basis/**k**-mesh tables are in **Methods** and **Supporting Information** on the version-of-record PDF.

### MD application — glass preparation, ion transport, and aqueous NaOH

**Engine / code.** **Reactive molecular dynamics** with **ReaxFF** is implemented in **LAMMPS** using a **velocity-Verlet** integrator at **\(\Delta t = 0.25\ \mathrm{fs}\)**. **Berendsen** thermostats (**100 fs** damping) are used for **NVT** segments, while **NPT** segments employ a **Berendsen barostat** (**5 ps** damping) as summarized in the computational overview.

**System size and composition.** **Na\(_2\)Si\(_2\)O\(_5\)** benchmarks use a **\(1\times2\times2\)** supercell (**144 atoms**). **Na\(^+\)/H\(^+\)** interdiffusion starts from the same amorphous framework with **three Na\(^+\)** ions replaced by **protons**. **NaOH(aq)** kinetics use **10 NaOH** plus **782 H\(_2\)O** in a **\(28.86\ \text{Å})^3** cubic cell (**§2.4.3**).

**Boundaries / periodicity.** **Three-dimensional periodic boundary conditions** apply to all bulk **crystal**, **glass**, and **electrolyte** cells in **§2.4**.

**Ensemble.** **NPT** appears for **1 K** crystal relaxation, **melt–quench** with **0 GPa** internal pressure, and **300 K** density stabilization of glasses; **NVT** follows for additional **300 K** relaxation. **Na\(^+\)** self-diffusion uses **200 ps NPT** equilibration per temperature, then **100 ps NVE** production. **Na\(^+\)/H\(^+\)** interdiffusion uses **NVT** at **800 K** followed by **100 ps** sampling. **NaOH** dissociation uses **NVT** at **300 K** for **100 ps**.

**Timestep.** **0.25 fs** for the protocols quoted above.

**Duration / stages.** **Glass** construction: **melt at 4000 K (NVT)**, **cool at 10 K/ps** under **0 GPa NPT** to **300 K**, then **0.5 ns NPT** until density plateaus, plus **0.5 ns NVT** at **300 K** (**§2.4.1**). **Na\(^+\)** diffusion: **200 ps NPT** equilibration then **100 ps NVE** trajectories across **300–900 K** (**§2.4.2**). **Interdiffusion:** **NVT** equilibration at **800 K**, then **100 ps** production (**§2.4.2**). **NaOH(aq):** **100 ps NVT** at **300 K** with bond-order **0.3** species analyses every **50 MD steps** (**§2.4.3**).

**Thermostat / barostat.** **Berendsen** thermostat (**100 fs** damping) for **NVT**; **Berendsen** barostat (**5 ps** damping) whenever **NPT** is active.

**Temperature.** **Glass** workflow spans **1 K**, **4000 K**, and **300 K**; **Na\(^+\)** diffusivity sweeps **300–900 K**; **interdiffusion** at **800 K**; **NaOH** benchmark at **300 K**.

**Pressure.** **NPT** segments target **0 GPa** hydrostatic conditions for **melt–quench** and **density** equilibration; **NVE** production fixes volume after **NPT** preconditioning.

**Electric field.** **N/A —** no applied **electric field**.

**Replica / enhanced sampling.** **N/A —** direct **MD** without **metadynamics**, **umbrella sampling**, or **bond boost**.

## Findings

### Outcomes and mechanisms

After optimization, **ReaxFF** reproduces **QM equations of state** for the **NaSiO\(_x\)** crystals examined and ranks **Na\(^+\)** vacancy migration pathways with the same **low-energy** ordering as **DFT** (**Fig. 2**). **Melt–quenched Na\(_2\)Si\(_2\)O\(_5\)** glasses remain stable under the subsequent **NPT/NVT** protocol, enabling **Na\(^+\)** self-diffusivity extraction across **300–900 K** and **Na\(^+\)/H\(^+\)** interdiffusion studies in **proton-substituted** glasses. **NaOH** dissociation in bulk **water** proceeds on the **100 ps** **NVT** window analyzed with a **0.3** bond-order criterion. Together, these validations motivate **dissolution** narratives involving **Na\(^+\)–proton interdiffusion**, **subsurface Na\(^+\)** transport toward **interfacial vacancies**, and **post-leach** ion–water chemistry.

### Comparisons

**Crystal/glass** structural metrics and **barrier** trends are compared to **DFT** training data; broader **leaching** implications are discussed relative to **experimental** silicate–water literature cited in the introduction.

### Sensitivity and design levers

**Quench rate** (**10 K/ps**), **temperature** (**300–900 K** diffusion sweep, **800 K** interdiffusion), and **stoichiometry** of the **Na\(^+\)/H\(^+\)** substitution control the observed **transport** and **speciation** kinetics.

### Limitations and outlook (as authored)

**Nanosecond** sampling and **bulk** benchmark cells bound direct extrapolation to **field** **leaching** times; the discussion highlights future **interface**-explicit models.

### Corpus honesty

Numerical protocol details above are summarized from **`papers/Hahn_NaSiOx_JPCC_2018_online.pdf`** §2.4; cite the **SI** parameter file for authoritative **ReaxFF** coefficients.


## Limitations

**Glass** **structure** **realism** depends on **melt–quench** **protocol** and **composition**; **transport** **coefficients** should be **spot-checked** against **independent** **QM** or **experiment** when extrapolating to **long** **leach** times.

## Relevance to group

Sandia + Penn State collaboration with van Duin on geochemical glass dissolution and reactive MD at silicate–water interfaces.

## Reader notes (navigation)

Proof duplicate: [[20180000-0002-1722-5631-x-development-reaxff]].

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.8b05852`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
