---
id: paper:2018aral-physical-che-oxyhydroxide-metallic
type: paper
title: "Oxyhydroxide of metallic nanowires in a molecular H2O and H2O2 environment and their effects on mechanical properties"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C8CP02422G"
year: 2018
authors:
  - "Gurcan Aral"
  - "Md Mahbubul Islam"
  - "Yun-Jiang Wang"
  - "Shigenobu Ogata"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "95ddbda87a3e52094e92b1bedd1f666880d37664092ea9784fe80c7e154f49b8"
pdf_path: "papers/Aral_PCCP_FeO_OH_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018aral-physical-che-oxyhydroxide-metallic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF reactive MD** simulates **oxidation** of **iron nanowires** in **molecular H\(_2\)O** and **H\(_2\)O\(_2\)**, forming **iron oxide** and **oxyhydroxide** shells whose **microstructure** depends on the **oxidizing environment** (**mild** **hydrolytic** oxidation versus **stronger** **peroxide**-driven pathways). The work then connects these **oxide shells** to **tensile** **mechanical response**: **pre-oxidation** introduces **defect-prone regions** near the **metal–oxide interface**, lowering **yield stress** and **Young’s modulus** compared to cleaner wires, with **H\(_2\)O\(_2\)** oxidation producing especially **detrimental** **mechanical weakening** in the models studied. **Deformation twinning** remains the dominant **plasticity** mechanism in **Fe**, but it **onsets earlier** in **oxidized** wires because **shell** **heterogeneity** concentrates **stress**. **Adri C. T. van Duin** is a coauthor.

## Methods

### Force-field lineage (ReaxFF, Fe/O/H)

Simulations use the **ReaxFF** reactive potential for **Fe/O/H** chemistry as parameterized in the **Aryanpour** *et al.* line cited in §2.1 of the article, enabling variable **atomic charges** (electrostatic energy minimized each MD step in the implementation described there).

### MD application — aqueous oxidation of Fe nanowires

**Engine / code.** Reactive MD is run in **LAMMPS** with the **ReaxFF** implementation referenced in §2.

**System size and composition.** The authors build **BCC** iron nanowires (NWs) with lattice constant **\(a = 2.86\) Å** inside an **orthogonal** simulation box of **\((50\times 50\times 50)\,a\)**, i.e. **\(\approx 14.315\) nm** per side. The initial cylindrical **Fe** NW is **\(\sim 5.0\) nm** in diameter and **\(\sim 14.3\) nm** long (**24 050 Fe atoms**), oriented along **[001]** and centered in the cell. **Oxidation** benchmarks place **1334 H\(_2\)O** molecules or **1000 H\(_2\)O\(_2\)** molecules in the vacuum region **\(\sim 6\) Å** from the NW surface (Fig. 1 in the paper).

**Boundaries / periodicity.** **Oxidation** trajectories use **periodic boundary conditions** in **all three** directions. **Tensile** runs apply **PBC** along the **loading ([001])** direction to mimic an infinitely long NW while suppressing artificial free-end effects, as stated in §2.

**Ensemble.** **Oxidation** simulations are performed in the **NVT** ensemble at **300 K** with a **Nose–Hoover** thermostat. **Mechanical deformation** after energy minimization (conjugate gradient) begins with a **Nose–Hoover NPT** equilibration at **300 K** with **zero pressure in the \(z\)** direction to relax residual stresses, then continues in **NVT** at **300 K** for the tensile stage.

**Timestep.** Equations of motion are integrated with a **velocity-Verlet** scheme using **\(\Delta t = 0.25\) fs**.

**Duration / stages.** **H\(_2\)O** oxidation runs **0.4 ns**; **H\(_2\)O\(_2\)** oxidation runs **1.1 ns** (the paper reports differing consumption of O/H atoms to build the oxide shells). **Tensile** deformation extends **1.5 ns** total while straining up to **15%** of the initial box length.

**Thermostat.** **Nose–Hoover** thermostats control **300 K** during **NVT** oxidation and **NVT** tensile loading; **NPT** equilibration before tension likewise uses **Nose–Hoover** coupling as described in §2.

**Barostat.** **Nose–Hoover NPT** is used only for the **pre-tensile stress-relaxation** step (**\(T = 300\) K**, **\(P_z = 0\)**). **Oxidation** and **tension** segments are **NVT** at fixed cell volume aside from the controlled **uniaxial strain** increments.

**Temperature.** **300 K** for oxidation, equilibration, and mechanical tests.

**Pressure / stress.** **Hydrostatic pressure control** is **not** applied during **NVT** oxidation. **NPT** equilibration targets **\(P_z = 0\)** in the normal direction. **Tensile** loading applies a **constant engineering strain rate** of **\(0.01\%\,\mathrm{ps}^{-1}\)** (**\(10^8\,\mathrm{s}^{-1}\)**) along **[001]**.

**Electric field.** **N/A —** no applied **electric field** or bias in the published protocol.

**Replica / enhanced sampling.** **N/A —** direct **ReaxFF MD** without **umbrella sampling**, **metadynamics**, or **bond boost**.

### Analysis

The authors track **oxide/oxyhydroxide** phases (**Fe\(_x\)O\(_y\)H\(_z\)**), **shell** microstructure, **coordination**/**density** metrics, and **virial stress–strain** responses (Table 1).

## Findings

### Outcomes and mechanisms

**Oxidation** in **molecular H\(_2\)O** versus **H\(_2\)O\(_2\)** produces **different iron oxide and oxyhydroxide** microstructures on the NW surface. **Pre-oxidation** increases **defect-prone** regions near the **metal–oxide** interface, so **plasticity** initiates at **lower stress/strain** than in **pristine** wires. **Deformation twinning** remains the **dominant** plastic mechanism for all NWs, but **twins appear earlier** under load for **oxidized** systems.

### Comparisons

Table 1 quotes **linear yield strains** and **yield stresses** of **6.0%, 4.9%, 4.8%** and **6.8, 5.6, 4.3 GPa** for **pristine**, **H\(_2\)O-oxidized**, and **H\(_2\)O\(_2\)-oxidized** NWs, respectively—**H\(_2\)O\(_2\)** gives the **largest** **softening** relative to **pristine** **Fe**.

### Sensitivity and design levers

**Oxidizer chemistry** (**H\(_2\)O** vs **H\(_2\)O\(_2\)**) and the resulting **local defect** population strongly couple to **yield** and **stiffness** at fixed **\(T = 300\) K** loading conditions.

### Limitations and outlook (as authored)

The study emphasizes **nanosecond** **oxidation** windows and **model** **NW** geometries; **quantitative** transfer to **long-time corrosion** or **alloys** should follow the article’s discussion of **ReaxFF** scope.

### Corpus honesty

Protocol numbers above are taken from **`papers/Aral_PCCP_FeO_OH_2018.pdf`** §2; if pagination differs in another print, use the **DOI** version for locators.


## Limitations

**Nanowire diameter**, **strain rate**, and **temperature** in **MD** influence **quantitative moduli**; compare to **experiment** where available. **ReaxFF** **Fe/O/H** parameter scope should be verified when extending to **alloys**, **aqueous** **electrolytes**, or **long-time** **corrosion** kinetics beyond the **nanosecond** **oxidation** **windows** modeled here.

## Relevance to group

Demonstrates **group ReaxFF** practice on **reactive metal oxidation** coupled to **nanomechanics**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/C8CP02422G` (see `papers/Aral_PCCP_FeO_OH_2018.pdf`).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

Compare **H\(_2\)O** versus **H\(_2\)O\(_2\)** **oxidation** outcomes here with other **Fe** **nanowire** **ReaxFF** entries in the corpus when building **retrieval** **clusters** around **aqueous** **corrosion** plus **mechanical** **loading**.
