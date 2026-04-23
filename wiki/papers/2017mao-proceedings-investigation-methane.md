---
id: paper:2017mao-proceedings-investigation-methane
type: paper
title: "Investigation of methane oxidation by palladium-based catalyst via ReaxFF Molecular Dynamics simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:combustion
  - keyword:catalysis-surface
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.proci.2016.08.037"
year: 2017
authors:
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K. H. Luo"
venue: "Proceedings of the Combustion Institute"
pdf_sha256: "f552ec853efe4706fa91aa9cf3d81be22cc1fc9ff3b852a7a0973de09db34af6"
pdf_path: "papers/QianMao_CH4_O2_Pd_ProcComb_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mao-proceedings-investigation-methane -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below (**Summary**, **Methods**, **Findings**, etc.) summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For exact numerical values and figures, use the peer-reviewed article at [DOI 10.1016/j.proci.2016.08.037](https://doi.org/10.1016/j.proci.2016.08.037).

## Summary

Methane oxidation over **palladium nanoparticles** is studied with **ReaxFF molecular dynamics** (Pd/C/H/O force field in **LAMMPS**), comparing **bare** metal with **oxygen-coated** surfaces prepared at controlled coverage. Simulations follow **O\(_2\)** and **CH\(_4\)** adsorption and dissociation, **CH\(_4\)/O\(_2\)** mixture reactivity under **temperature-ramp** NVT conditions, and **fixed-temperature** runs from **400–1000 K** used to extract **apparent activation energies** for **CH\(_4\)** dissociation at **~0.3** and **~0.7 ML** oxygen coverage. The authors relate **atomic-level** trajectories to **oxygen blocking** of methane adsorption, **coverage-dependent** methane activation, and **reported** consistency of derived barriers with **DFT** and **experiment**.

## Methods

**A — Force-field training / fitting:** **Pd/C/H/O ReaxFF** in **LAMMPS** from established **combustion**/**catalysis** parametrizations (article cites lineage); **no** new **QM** refit summarized in this proceedings paper.

**B — Molecular dynamics / sampling:** **NVT** reactive MD in a **cubic ~80 Å** cell with **3D periodic boundary conditions** (standard nanoreactor-style setup in the article). **CG** energy minimization, **Δt = 0.25 fs**, **Nosé–Hoover** thermostat (**100 fs** damping), **10⁵** equilibration steps; **~3 nm Pd\(_{935}\)** nanoparticle oxidized at **1500 K** with **O\(_2\)** to **~0.3** and **~0.7 ML** oxygen precoverages; **CH\(_4\)/O\(_2\)** mixture at **~4.85 atm** (e.g. **40 O\(_2\) + 20 CH\(_4\)** molecules in the cited cell). **Temperature ramp** **300 → ~3000 K** at **~1.08 K ps⁻¹** (**10⁷** MD steps) plus **fixed-temperature** windows (**400–1000 K**) for **CH\(_4\)** dissociation kinetics. **VMD** visualization.

**C — DFT / static QM:** **Literature DFT**/**experiment** cited for **barrier** comparison—**not** **ab initio** MD here.

**D — Review / non-simulation framing:** **Proc. Combust. Inst.** **application**—**not** a review.

**Pressure / barostat:** **N/A — NPT** not used for the quoted **NVT** nanoreactor protocol; **no** stated **hydrostatic pressure** control beyond implicit **constant-volume** gas-phase cell.

## Findings

**Adsorption and site blocking:** **O\(_2\)** adsorbs more readily than **CH\(_4\)** on both **bare** and **oxygen-coated** Pd; **preadsorbed O\(_2\)** on oxidized surfaces **blocks** sites available for **CH\(_4\)** adsorption.

**Dissociation and coverage:** At **low temperature**, **adsorptive dissociation** of **CH\(_4\)** is **easier** on **oxygen-coated** nanoparticles than on **bare** Pd. **O\(_2\)** **dissociation** requires **higher temperature** than **O\(_2\)** **adsorption**, unlike the relatively **rapid** **CH\(_4\)** dissociation after adsorption under the conditions explored. **CH\(_4\)** dissociation **rates** increase with **temperature** and depend on **surface oxygen coverage**.

**Activation energies:** From **fixed-temperature** simulations (**400–1000 K**), **apparent** activation energies for **CH\(_4\)** adsorptive dissociation are reported as **3.27** and **2.28 kcal mol\(^{-1}\)** on **0.3** and **0.7 ML** oxygen-coated particles, respectively; the authors state these are **consistent** with **DFT** and **experiments**.

## Limitations

- **ReaxFF** remains an **empirical reactive model**: barriers and pathways are **approximate** relative to **QM** and may depend on **parameterization** and **training-set** scope.
- **Nanoparticle** size (**~3 nm**), **single** morphology, and **idealized** **ML** coverage may not capture all **experimental** **catalyst** **dispersion** and **support** effects.
- **Reactive MD** uses **high** **gas-phase** **pressures** and **temperature ramps** (or **limited** **duration** at fixed \(T\)) to observe chemistry within **accessible** **timescales**—**not** a direct replica of **long** **isothermal** **reactor** **conditions**.

## Relevance to group

**Adri C. T. van Duin** (co-author, **Penn State** Mechanical and Nuclear Engineering) contributes **ReaxFF** methodology context; the work applies the **Pd/C/H/O** **reactive** **framework** to **heterogeneous** **methane** **oxidation** relevant to **combustion** and **catalysis** **modeling**.

## Citations and evidence anchors

- [https://doi.org/10.1016/j.proci.2016.08.037](https://doi.org/10.1016/j.proci.2016.08.037)

## Reader notes (navigation)

- Themes: [[theme-catalysis-surfaces]], [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
