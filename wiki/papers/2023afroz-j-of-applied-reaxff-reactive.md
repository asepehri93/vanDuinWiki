---
id: paper:2023afroz-j-of-applied-reaxff-reactive
type: paper
title: "ReaxFF reactive force field model enables accurate prediction of physiochemical and mechanical properties of crystalline and amorphous shape-memory polyurethane"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:npt-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1002/app.54466"
year: 2023
authors:
  - "Mohammad M. Afroz"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Katie D. Li-Oakey"
venue: "Journal of Applied Polymer Science 140, e54466 (2023)"
pdf_sha256: "ecdb6fa32925566d3ae8370985aa95dc03cd81c1c867b0d6051139976c1a859b"
pdf_path: "papers/Afroz_JAppPol_2023_polyurethane.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023afroz-j-of-applied-reaxff-reactive -->

## Summary

**Shape-memory polyurethanes (SMPUs)** combine **hard (rigid) segments** and **soft segments**; the rigid domains fix the **permanent** shape while **soft** domains absorb **temporary** strain recoverable upon **stimulus**. Afroz et al. focus on a common **rigid segment** chemistry—**4,4′-diphenylmethane diisocyanate (MDI)** with **1,4-butanediol (BDO)**, denoted **MDI–BDO**—and build **crystalline** and **amorphous** atomistic models suitable for **ReaxFF**. They report **equilibrium** molecular dynamics to predict **structural** and **physicochemical** properties, including **simulated XRD and FTIR** fingerprints, and **nonequilibrium** **uniaxial box deformation** to probe **tensile loading** and **stress relaxation** of the **crystalline** rigid domain. The *Journal of Applied Polymer Science* abstract frames the overall goal as showing that a suitable **ReaxFF** model can reproduce **crystalline/amorphous** distinctions in **density** and related observables while also capturing **mechanical** response under the reported loading protocols.

## Methods

### System chemistry and modeling focus

- **Polymer:** **Shape-memory polyurethane**; simulations emphasize the **rigid segment** chemistry **MDI–BDO** (**4,4′-diphenylmethane diisocyanate** + **1,4-butanediol**), which sets **permanent** shape in the **hard/soft** block picture described in the article.

### ReaxFF parameterization and validation (A)

- **ReaxFF** description of **urethane/isocyanate**-containing **rigid** motifs, trained/validated as detailed in *J. Appl. Polym. Sci.* **Methods** (reference **QM** data and targets there).

### Equilibrium molecular dynamics (B)

- **Sampling:** **NVT/NPT**-class equilibration of **crystalline** and **amorphous** **rigid-domain** cells to obtain **density**, **structure**, and **spectroscopic** proxies (**simulated XRD/FTIR** fingerprints per abstract).

### Nonequilibrium mechanical tests (B)

- **Loading:** **Uniaxial box deformation** (tensile) and **stress-relaxation** protocols on **crystalline** rigid-domain models.
- **Software / numerics:** **LAMMPS** with **ReaxFF** as in the article.

### MD application (integrated; extract limits)

**Engine / code:** **LAMMPS** and **ReaxFF**. **System size & composition:** **crystalline** and **amorphous** **MDI–BDO** rigid-domain **supercells**; exact **atom counts** and **stoichiometry** in the version-of-record **Methods**—**N/A in the p1–2 extract only.** **Boundaries:** **3D PBC** bulk models (standard for the reported set). **Ensemble / control:** the abstract states **equilibrium** **molecular dynamics** by controlling mass, **temperature**, and **pressure** or **volume** (NPT- or NVT-style stages implied); **N/A — thermostat type, barostat type/damping, timestep (fs), equilibration/production and deformation durations (ps/ns), strain rate, and setpoint** **K** are **not** in the indexed **p1–2** text—**see full PDF** for protocol tables. **N/A — static external electric field; N/A — umbrella / metadynamics / replica exchange.** **Shear, shock, non-periodic cutoffs, ReaxFF QEq cadence:** **N/A — not in p1–2 extract.**

## Findings

### Shape-memory-relevant mechanics

**Nonequilibrium** runs probe **tensile** response and **stress relaxation** of the **crystalline** rigid domain—behaviors tied to **shape fixity/recovery** emphasized for **soft robotics** applications in the abstract.

### Structure and spectroscopic fingerprints

Simulations contrast **crystalline** vs **amorphous** rigid segments in **structure** and in **XRD/FTIR**-like observables, supporting interpretation alongside the experimental mindset described in the paper.

### Application framing

The authors position **ReaxFF** **loading/unloading** results as a **theoretical** route to **thermomechanical** tuning of **SMPU** **hard blocks** under the stated force field. **Comparisons** to **experiment** for **SMPU** design are framed in the **Introduction**; quantitative agreement is **not** the focus of the abstract alone.

## Limitations

Readers implementing similar workflows should verify **force-field** coverage for **urethane** chemistry under **large** strains and **high** temperatures relevant to **processing**, not only **room-temperature** elastic tests. The study **isolates rigid segments**; **soft segments**, **full polymer** **chain** entanglements, and **device-scale** morphology are outside scope. **ReaxFF** predictions of **mechanical moduli** and **transition temperatures** should be validated against **experiment** for each new chemistry.

**Confidence rationale:** `high`—peer-reviewed primary article with clear abstract-level methods/results.

## Reader notes (navigation)

- [[reaxff-family]]
- [[theme-reactive-md-corpus]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
