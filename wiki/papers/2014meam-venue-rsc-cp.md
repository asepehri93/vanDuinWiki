---
id: paper:2014meam-venue-rsc-cp
type: paper
title: "An interatomic potential for saturated hydrocarbons based on the modified embedded-atom method"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:classical-ff-specialized
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:eam-potential
  - keyword:reactive-md
  - keyword:qm-training-data
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP00027G"
year: 2014
authors:
  - "S. Nouranian"
  - "M. A. Tschopp"
  - "S. R. Gwaltney"
  - "M. I. Baskes"
  - "M. F. Horstemeyer"
venue: "Phys. Chem. Chem. Phys. 16, 6233–6249 (2014)"
pdf_sha256: "9921b8bbfe16b04ea018ce3d7d1673bf00d5a64b1c741629eb929feb3f56fb50"
pdf_path: "papers/Others/MEAM_hydrocarbons_PCCP_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014meam-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries track the **PCCP** article (`doi`). **MEAM** is distinct from **ReaxFF**; the paper **compares** to **ReaxFF** and **REBO** for hydrocarbon benchmarks.

## Summary

Develops a **modified embedded-atom method (MEAM)** potential for **saturated hydrocarbons** (alkanes), motivated by applications at **hydrocarbon–metal** and **polymer–metal** interfaces where **many-body** metallic models must meet **reactive organic** energetics without mixing incompatible formalisms. The parameterization is fit to a mixed **experimental and first-principles** database spanning **geometries**, **atomization energies**, **diatomics and molecular dimers**, and **high-pressure** **PVT** for **methane**. The authors benchmark **MEAM** against **second-generation REBO** and **ReaxFF** on shared targets to situate accuracy for **saturated** species, explicitly noting **ReaxFF** as a comparator for **reactive** hydrocarbon modeling in the corpus context.

## Methods

Evidence in this section is grounded in **`papers/Others/MEAM_hydrocarbons_PCCP_2014.pdf`** and the indexed abstract/introduction in `normalized/extracts/2014meam-venue-rsc-cp_p1-2.txt` (Phys. Chem. Chem. Phys. 2014, 16, 6233–6249; DOI `10.1039/C4CP00027G`).

### 1 — MD application (atomistic dynamics)

The indexed excerpt centers on **MEAM** development and benchmarks versus **REBO**/**ReaxFF**; it does **not** spell out a single production **molecular dynamics** protocol (engine, **timestep**, **NVT**/**NPT** lengths) in the pages captured here.

- **Engine / code:** **N/A — not stated** in `2014meam-venue-rsc-cp_p1-2.txt` (consult the full **PCCP** article for any explicit **MD** package names).
- **System size & composition:** **Training** references span **alkane** homologs through **n-octane** isomers, diatomics/dimers, and a dense **methane** **PVT** point (density **0.5534 g cm⁻³** in the abstract text)—not a single fixed **supercell** count in the excerpt.
- **Boundaries / periodicity:** **N/A — not stated** in the indexed excerpt (likely **PBC** for bulk **PVT** targets in the paper body).
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A — not stated** in the indexed excerpt for benchmark **MD** details.
- **Temperature:** **0 K** **atomization energies** appear in the **training** list; **high-pressure** **PVT** data for **methane** are also cited as **training** targets (abstract).
- **Pressure:** **PVT** **pressure–volume–temperature** data for dense **methane** are part of the **reference** set (abstract).
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated** in the indexed excerpt.

### 2 — Force-field training

- **Parent FF / elements:** **Modified embedded-atom method (MEAM)** for **saturated hydrocarbons**, positioned as an extension of the **MEAM** formalism traditionally used for **metals** and **metal** compounds (introduction in extract).
- **QM reference:** The abstract states **MEAM** is informed by **density functional theory** alongside **pair potentials** in the parameterization philosophy; **functional**, **basis**, and **k**-mesh specifics for each **training** datum are **N/A — not in the short extract**—read **PCCP** Methods.
- **Training set:** Fit targets listed in the abstract/extract include (1) **n-alkane** bond distances/angles and **0 K atomization energies** through **n-octane** isomers, (2) **H₂**, **CH**, **C₂** diatomic curves, (3) dimer curves for **(H₂)₂**, **(CH₄)₂**, **(C₂H₆)₂**, **(C₃H₈)₂**, and (4) **PVT** for dense **methane** at the quoted density.
- **Optimization:** **Parameterization** by fit to the mixed **experimental** and **first-principles** database (abstract); **optimization** algorithm/software details are **N/A — not in indexed excerpt**.
- **External reference data:** Comparisons to **second-generation REBO** and **ReaxFF** on shared **training** observables; **experimental PVT** for **methane**, **ethane**, **propane**, and **butane** series are discussed as **validation** targets in the abstract narrative.

### 3 — Static QM / DFT-only

**N/A as standalone block** beyond the **DFT-informed** **MEAM** fit statement above; detailed **QM** settings for each **training** item live in the **PCCP** article body/SI.

## Findings

### Outcomes and mechanisms

The abstract states **MEAM** reproduces the listed **experimental** and/or **first-principles** data with accuracy **comparable to or better than REBO or ReaxFF** on those sets, predicts **PVT** for **methane–butane**-class systems **reasonably**, and gives **reasonable** energetics for **C–C** and **C–H** bond-breaking in **saturated** species.

### Comparisons

Head-to-head **benchmarks** against **second-generation REBO** and **ReaxFF** are a core **comparison** axis in the abstract framing.

### Sensitivity and scope levers

The abstract explicitly warns the parameterization **does not** accurately treat **unsaturated** hydrocarbons and should **not** be applied there—an authored **scope** boundary for **olefinic**/**aromatic** chemistry.

### Limitations and corpus honesty

For **interface** or **polymer–metal** use cases, the introduction motivates **MEAM** as a bridge potential, but **transferability** must respect the **saturated** hydrocarbon **training** scope. Quantitative **barriers**, **elastic** data, and any **MD** validation tables should be taken from the **full PDF** rather than this wiki summary alone.

## Limitations

Does **not** accurately treat **unsaturated** hydrocarbons; **MEAM** scope and transferability follow the paper’s caveats. For **interface** or **shock** studies that require **bond rearrangement** beyond **saturated** **alkane** chemistry, readers should compare against **ReaxFF** or other **reactive** models trained for those **reaction** classes rather than extrapolating this **MEAM** set. **Transfer** to **metal** **interfaces** likewise requires explicit **metal** **parameter** **blocks** compatible with the **hydrocarbon** subset published here. **Long** **alkane** **melting** and **interface** **friction** studies should verify **cutoffs** and **neighbor** lists against the **PCCP** implementation notes bundled with the potential release.

## Relevance to group

**Benchmark** context for **reactive hydrocarbon** modeling where corpus work often uses **ReaxFF**; useful cross-method reference.

## Citations and evidence anchors

- https://doi.org/10.1039/C4CP00027G — Abstract and PCCP volume/page as in front matter.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
