---
id: paper:2018hegoi-manzano-the-journal-benchmark-reaxff
type: paper
title: "Benchmark of ReaxFF force field for subcritical and supercritical water"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1063/1.5031489"
year: 2018
authors:
  - "Hegoi Manzano"
  - "Weiwei Zhang"
  - "Muralikrishna Raju"
  - "Jorge S. Dolado"
  - "Iñigo López-Arbeloa"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "f113ffcb5702cef4863d4b9715825a31052b7a995042525273dfdcf8664fd0ad"
pdf_path: "papers/Manzano_supercriticalH2O_JCP_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018hegoi-manzano-the-journal-benchmark-reaxff -->

## Summary

**Reactive water** under **subcritical** and **supercritical** conditions underpins **geochemistry**, **combustion**, and **hydrothermal** materials processing. This **benchmark** paper evaluates **ReaxFF** **MD** (**LAMMPS** `reax/c`) against **experiments** for **H₂O** spanning **ambient** through **supercritical** **P–T** windows. Properties examined include **density**, **dipole moment**, **static dielectric constant ε(0)**, **structure factors**, **hydrogen-bond** statistics, **self-diffusivity**, and **proton-transfer** behavior. The study concludes **ReaxFF** matches many **SC water** observables **quantitatively**, while **ε(0)** is only **qualitatively** captured—an explicit caveat for **electrostatic** applications. Because **water** is the **universal** **solvent** in countless **ReaxFF** **oxide** and **electrolyte** simulations, this paper is frequently cited as the **baseline** **sanity check** before mixing **H₂O** with **minerals**, **electrodes**, or **organic** fragments in **large** **reactive** cells. **Operators** should still record which **O/H** **parameter** **file** they combine with **mineral** **databases**, because **cross-term** **training** may **shift** **effective** **pH-like** behavior even when **pure water** looks **reasonable**.

## Methods

**MD application:** Simulations use **LAMMPS** (`reax/c`) with **309** **H₂O** molecules in a **~2.1 nm** cubic **supercell** under **3D periodic boundary conditions (PBC)**. After **energy minimization** and **Gaussian** velocity initialization, trajectories integrate with **Verlet** and **0.2 fs** **timestep** under **NPT** **Nosé–Hoover** **thermostat** and **barostat** control along prescribed **temperature**–**pressure** paths. **~500 ps** aggregate sampling (**~200 ps** **production** after **<10 ps** **equilibration**) with **0.2 ps** trajectory stride is reported, plus additional **proton-transfer** runs with finer output. **State space:** **400–900 K** on **25–100 MPa** isobars plus **293 K, 0.1 MPa** baseline. **N/A — external electric field** or **umbrella sampling** protocols.

**Force-field provenance (not a refit study):** This **J. Chem. Phys.** contribution **benchmarks** an existing **dissociative**, **QEq/EEM**-polarizable **ReaxFF** water description against **experiment**; the **QM training data** and **parameter optimization** that produced the parent **O/H** set are cited from prior **ReaxFF** water publications rather than being regenerated here (**N/A — new GA-based refit** in this manuscript). **Reference data** in this paper are **experimental** **equations of state**, **diffusivities**, **structure factors**, and related observables tabulated for comparison.

## Findings

**Outcomes & mechanisms:** **ReaxFF** tracks **experimental** **density**, **hydrogen-bond** statistics, **diffusivity**, and **proton-transfer** trends for **subcritical** and **supercritical** water across the **state grid** reported in **J. Chem. Phys.** **148**, **234503** (2018).

**Comparisons:** agreement with **experiment** is described as **quantitatively** strong for many observables, while the **static dielectric constant** \(\varepsilon(0)\) is only **qualitatively** reproduced—an explicit limitation for **electrostatic**-sensitive workflows.

**Sensitivity & design levers:** performance depends on the chosen **P–T** path (**temperature** and **pressure** along **isobars**); **proton-transfer** statistics can be **sensitive** to **output cadence** and **timestep** choices, so port rates to other engines only after matching the article/SI settings.

**Limitations / outlook (as authored):** finite **~309-molecule** cells affect **fluctuations**; **global** **O/H** parameters may behave differently when merged with **oxide** or **organic** **cross-terms** in other databases.

**Corpus honesty:** numeric tables and any **SI-only** sensitivity checks should be read from the **PDF** (`pdf_path`) rather than inferred from this wiki summary alone.

## Limitations

**Global** **O/H** parameters are not a **dedicated** water model; **309-molecule** **finite size** affects **fluctuations**; **ε(0)** mismatch may impact **electrolyte** simulations requiring accurate **screening**. **Proton-transfer** statistics are **sensitive** to **timestep** and **thermostat** coupling—compare **SI-level** **settings** before **porting** rates into **other** **codes**. **JCP** **benchmarks** should be **cited** whenever **new** **oxide/water** **cross-terms** are **merged** with this **O/H** **core** to document **compatibility** assumptions. **Keep** **pressure** **units** consistent when comparing **isobars** across **tables**.

## Relevance to group

Foundational **van Duin-group** validation paper for **high-T high-P** **aqueous** **ReaxFF** chemistry cited whenever **supercritical water** appears in **geochemical**, **hydrothermal**, or **combustion** **training** discussions. Treat **ε(0)** caveat as a **hard** limit for **electrolyte** **screening** workflows.

## Citations and evidence anchors

- DOI: `10.1063/1.5031489`; `papers/Manzano_supercriticalH2O_JCP_2018.pdf`; extract `normalized/extracts/2018hegoi-manzano-the-journal-benchmark-reaxff_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
