---
id: paper:2026dryzhakov-advanced-mat-revealing-defect
type: paper
title: "Revealing the Defect-Driven Ferroelectric Mechanisms of Aluminum Nitride"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:neb
  - keyword:validation-experiment
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1002/adma.202520258"
year: 2026
authors:
  - "Bogdan Dryzhakov"
  - "Chloe Skidmore"
  - "Drew Behrendt"
  - "Sebastian Calderon V"
  - "Leonard C. Jacques"
  - "Erdem Ozdemir"
  - "John Hayden"
  - "Ian Mercer"
  - "Ali Mohammadi Dinani"
  - "Ilia Ivanov"
  - "John Lasseter"
  - "Bernadeta Srijanto"
  - "Alireza Sepehrinezhad"
  - "Ga Un Jeong"
  - "Betul Akkopru Akgun"
  - "Andrew M. Rappe"
  - "Adri C. T. van Duin"
  - "Susan Trolier-McKinstry"
  - "Elizabeth C. Dickey"
  - "Steven J. Randolph"
  - "Jon-Paul Maria"
  - "Kyle P. Kelley"
venue: "Advanced Materials"
pdf_sha256: "d7995f7d4086ef38f0c15d08294d81f2d827ee5bf00bfd6185e877627cfff9f4"
pdf_path: "papers/Dryzhakov_Dinani_Sepehrinezhad_Jeong_AlN_defect_AdvMat_2026.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026dryzhakov-advanced-mat-revealing-defect -->

## Summary

**Helium-ion** direct-write irradiation introduces **point defects** that **tune ferroelectric response** in **w-AlN** and **Al₀.₉₂B₀.₀₈N**, measured by **piezoresponse** and **dielectric** methods. The article combines **focused He⁺ / helium-ion microscopy** patterning, **band-excitation PFM / BEPS**, **dielectric modulus** and **Rayleigh** analysis, and **SRIM**-motivated **collision** estimates with **atomistic modeling**: **ReaxFF** simulations of **He irradiation**, **relaxation**, and **sinusoidal electric-field polarization cycling**, plus **DFT nudged elastic band** calculations for **vacancy** and **defect-complex** pathways in **wurtzite AlN**.

## Methods

- **Experiment:** **RF-sputtered** **AlN** and **boron-alloyed AlN** films; **He-ion** irradiation across **dose** ranges (including **~500–10,000 ions nm⁻²** on **µm-scale** capacitors); **HIM** **nanoscale** patterning (**~0.5 nm** probe; **~1000 ions nm⁻²** on **30 nm** films in one figure series); **BEPS / PFM** **d₃₃,eff** and **nonlinearity** metrics; **dielectric spectroscopy** (e.g., **tan δ**, **Rayleigh** slopes); **second-harmonic BEPS** for thermal/nonlinear checks; **KAI** / **Avrami** analysis of switching (**n ≈ 1** nucleation-limited behavior under irradiation in the reported conditions).
- **ReaxFF MD:** **Helium bombardment** of a **pristine AlN** crystal with **eight He atoms** at **3.5 keV** kinetic energy; **equilibration**; **sinusoidal electric field** applied to **pristine vs damaged** cells to compare **polarization switching** energetics (**Fig. 4** reports **500**-frame bombardment, **100**-frame equilibration, **1550**-frame switching trajectories in the figure caption).
- **DFT NEB:** **Vacancy-type** models (**V_N**, **(V_Al–O_N)** complex, etc.) for **barriers** along **polar** switching paths; **barrier reductions** quoted vs **perfect** AlN in **small-cell** DFT (**full k-point / functional details in Supporting Information**).

**1 — MD application (atomistic dynamics).** LAMMPS ReaxFF **molecular dynamics** on a **pristine wurtzite** **AlN** **periodic 3D PBC** **supercell**; **He** **bombardment** at **3.5 keV** with **eight** **He** atoms; **Fig. 4** reports **500**-frame, **100**-frame, and **1550**-frame **segments**; **fs** **time** **step** values are in the **PDF**, not restated here. **sinusoidal** **electric** **field** drives **polarization** **switching**. **N/A** — **NPT** **barostat**; **N/A** — **replica**/**metadynamics**; **N/A** — **hydrostatic** **GPa** **pressure** control for the quoted **NVT** **field-cycling** unless the **VOR** adds an **NPT** leg. **Thermostat** details for **He** **damage**—see **SI**.

**2 — Force-field training** — **N/A** (uses a published **Al**/**N** **ReaxFF** line; this work is **application**-focused).

**3 — Static QM / DFT (NEB).** **NEB** on **vacancy**/**complex** **pathways** in **w-AlN**; **functional**/**k**-mesh in **SI**; **barrier** **property** for **polar** **reversal** **mechanism** **comparison** **vs** **defect**-free **AlN**.

**4 — Review** — **N/A.**
## Findings

- **Ion irradiation** induces **ferroelectric-like switching** in **as-grown** **pristine AlN** and **strengthens** response in **Al₀.₉₂B₀.₀₈N**, with **dose-dependent** **coercive field** reduction (e.g., **~41%** coercive-field reduction cited for **alloyed** films at high dose relative to structural tuning by **boron alone** in the discussion).
- **BEPS** on **irradiated capacitors** reports large (**~10×**) **apparent electromechanical enhancement** with dose, alongside **increased loss** and **AC conduction**; **activation energy ~1 eV** **modulus** signature attributed to **irradiation-induced V_N**-related conduction.
- **ReaxFF** shows **line defects** after **He damage** and **lower** **switching** **barriers** (**~48%** for the first two **averaged** **switches** **vs** **pristine** in the text). **DFT**-**NEB** shows **barriers** drop with **vacancies** and **(V_Al–O_N)**, enabling **columnar** **reversal** **vs** **homogeneous** **switching** in **perfect** cells; **trends** **qualitatively** **align** **across** **PFM/BEPS**, **ReaxFF**, and **NEB** (see `## Limitations` for small-cell caveats).

- **Dose**/**coercive**-**field** and **d₃₃,eff** **sensitivity** are **dose**-tuned in the **alloyed** and **pristine** **stacks** as in the main text; **outlook** toward **extrinsic** **clamping** is noted in `## Limitations`.

## Limitations

**DFT** cells are **small** versus experimental **polycrystalline** films; **ReaxFF** **Al/N** chemistry is **approximate** for **quantitative** **barrier** matching. **Extrinsic** contributions (electrodes, **clamping**, **damage** chemistry beyond **point defects**) affect **PFM** amplitudes. Full **DFT** settings and larger **SI** lives in **Wiley Supporting Information**.

## Relevance to group

**Adri C. T. van Duin** and **Ga Un Jeong** (Penn State) co-author the **ReaxFF** contribution; **ORNL**-led **HIM** / **thin-film** collaboration with **PSU**, **CMU**, **Penn**, and others.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1002/adma.202520258](https://doi.org/10.1002/adma.202520258)

## Related topics

- [[reaxff-family]]
- [[theme-ferroelectrics-polar-oxides]]
