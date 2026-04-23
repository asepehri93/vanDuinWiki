---
id: paper:2021shi-carbon-173-2-generation-characterization
type: paper
title: "Generation and characterization of an improved carbon fiber model by molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:classical-md
  - method:monte-carlo
  - task:application
paper_keywords:
  - keyword:classical-ff
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2020.11.011"
year: 2021
authors:
  - "Linyuan Shi"
  - "Marina Sessim"
  - "Michael R. Tonks"
  - "Simon R. Phillpot"
venue: "Carbon 173 (2021) 232–244"
pdf_sha256: "2bbaff43777d33832635074e54de0d0e3040790b46c5a9b200ae0094f5b7a190"
pdf_path: "papers/ReaxFF_others/Shi_Tonks_Philpott_Carbon_kMC_MD_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021shi-carbon-173-2-generation-characterization -->

## Summary

**Carbon fiber** properties emerge from **nanoscale** **graphitic** ordering, **cross-linking**, and **porosity**, but building faithful **atomistic** models that span **density**, **texture**, and **mechanical** observables remains nontrivial. This **Carbon** article generates atomistic fiber models by coupling **kinetic Monte Carlo (kMC)** cross-linking with **large-scale molecular dynamics**, producing two families: a **fiber-core** motif representing an interior slice of a thick fiber and a **thin fiber** with explicit surfaces. Initial densities span **1.2–2.0 g/cm\(^3\)**. The authors characterize models using **shape**, **mass density**, **pore-size distributions**, and **hybridization** statistics, then validate against **virtual X-ray diffraction** patterns compared to experimental references. Additional variants remove **graphitic sheets** stochastically along the fiber axis; partial **healing** occurs during equilibration, and **uniaxial tensile** MD yields **Young’s moduli** within experimental spreads reported for carbon fibers. Industrial **carbon fiber** modeling frequently jumps directly to **continuum** or **mesoscale** representations; this work instead asks what **atomistic** texture is minimally required before **modulus** and **diffraction** signatures simultaneously look credible against experiments, which motivates the dual **kMC + MD** construction. The authors thereby aim for models that are falsifiable against **two** independent experimental observables, not just one tuned mechanical number. See the **Carbon** paper for numerical benchmarks.

## Methods

**1 — MD application.** Atomistic **fiber** models are built with **kinetic Monte Carlo** **cross-linking** of **graphitic** layers followed by **LAMMPS** **molecular dynamics** **equilibration** and **mechanical** testing. **Fiber-core** and **thin-fiber** morphologies span **1.2–2.0 g cm⁻³** target **density**; **stochastic** removal of **layers** explores defect variants with partial **healing** during **relaxation**. **MD** uses **PBC** **supercells** with thousands of **atoms** (exact counts in *Carbon*), **NVT** or **NPT** segments as appropriate for **density** control (see article), **thermostat** and **timestep** (**fs**) per **Methods**, and **equilibration** then **production** runs totaling **ns**-scale sampling where reported. **Uniaxial** **strain** **MD** yields **Young’s modulus**; **strain** **rate** and **temperature** (**K**) are specified in the paper. **N/A — external electric field**; **N/A — umbrella** / **metadynamics** in the generation workflow.

**2 — Force field.** **Classical** **empirical** **carbon** **potential** (non-ReaxFF) with fixed **bond** **topology** after **kMC**—suitable for **elastic** and **structural** **property** evaluation without **reactive** bond breaking in the reported tests.

**3 — Static QM. N/A.**

**4 — Experiments (laboratory). N/A** — **virtual** **XRD** is **compared** to **experimental** **diffractograms** from the literature.
## Findings

**Fiber-core** and **thin-fiber** models reproduce the **densities** and **structural signatures** reported in the benchmarks shown. **Virtual XRD** matches experimental profiles in the comparisons presented. **Defective** variants with random layer removals **partially heal** upon relaxation, and predicted **moduli** fall within the **experimental** spread for the models tested—supporting the authors’ claim that the workflow yields **improved** fiber-like models for downstream property studies compared to simpler graphitic constructs. The practical implication for multiscale workflows is that **kMC + MD** can jointly control **pore** statistics and **graphitic** alignment, producing microstructures that are not forced to match a single **ideal crystal** assumption yet still reproduce **XRD** and **modulus** checks used in the carbon fiber literature.

**Comparisons, sensitivity, limitations (corpus).** **Moduli** and **XRD** are **compared** to **experiment**; **density** and **defect** **density** are the main **levers** tuned. Full numerical tables remain in the **version-of-record** **PDF**.

## Limitations

Nanometer-scale models omit full **fiber diameter**, **industrial** processing heterogeneity, and **misorientation** statistics beyond those encoded in the generation rules.

## Relevance to group

Classical **carbon microstructure** generation benchmark in the corpus (non-ReaxFF).

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2020.11.011](https://doi.org/10.1016/j.carbon.2020.11.011)

## Related topics

- [[reaxff-family]] (context only)
