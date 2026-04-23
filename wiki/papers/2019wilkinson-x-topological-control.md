---
id: paper:2019wilkinson-x-topological-control
type: paper
title: "Topological control of water reactivity on glass surfaces: evidence of a chemically stable intermediate phase (proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - method:classical-md
  - task:application
  - material:silicate-glass
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:water-interfaces
source_refs: []
doi: "10.1021/acs.jpclett.9b01275"
year: 2019
authors:
  - "Collin J. Wilkinson"
  - "Karan Doss"
  - "Seung Ho Hahn"
  - "Nathan Keilbart"
  - "Arron R. Potter"
  - "Nicholas J. Smith"
  - "Ismaila Dabo"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
  - "John C. Mauro"
venue: "J. Phys. Chem. Lett. (proof PDF)"
pdf_sha256: "95f3e4d53bff3917a554d7e0a42444ded5e0c054306db93f0fc0120619250582"
pdf_path: "papers/Wilkinson_Water_Silica_JPCL_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019wilkinson-x-topological-control -->

## Summary

The research motivation is that **glass** **topology**—variations in **bond** **constraints** across the **network**—should modulate **hydrolysis** propensity at **hydrated** surfaces, with implications for **long-term** **weathering** and **engineering** of **silicate** interfaces. The published letter’s opening experimental protocol section states that bulk sodium silicate glasses were first generated for a nominal 70SiO₂·30Na₂O composition using the Teter potential in a periodic cell sized to match the experimental mass density before surfaces were prepared for subsequent reactive simulations. This file is the **author proof** PDF for the *J. Phys. Chem. Lett.* communication on **topological control of water reactivity** on **sodium silicate glass** surfaces (DOI `10.1021/acs.jpclett.9b01275`). The study combines **melt/quench molecular dynamics** with a **Teter**-type potential to generate **~70 SiO₂·30 Na₂O** glass, **cleaved** surfaces, and **ReaxFF Na/Si/O/H** simulations of **water** interactions mapped against a **rigidity percolation**-style **constraint density** metric. **DFT** checks support key conclusions summarized in the letter. The **version-of-record** PDF used for stable pagination and figures is on **`[[2019wilkinson-j-phys-chem-topological-control]]`** (`papers/Wilkinson_JPCL_2019_water_reactivity_SiO2.pdf`).

## Methods

**Glass formation** uses **LAMMPS** with the **Teter** potential in **PBC** **cells** (see letter) to produce **70 SiO₂·30 Na₂O** **glass** for subsequent **cleaving**; **NVE** **melt**/**NVT** quench and **NPT** **1 atm** **stages** mirror **[[2019wilkinson-j-phys-chem-topological-control]]**, with **thermostat**/**barostat** lines copied from the VOR, not this proof. **ReaxFF** interfacial **molecular** **dynamics** then evaluates **water** **binding** **energies** vs **local** **constraint** **density** on the **exposed** **slab**; **duration** and **loadings** of **H₂O** are in the VOR/SI. **N/A** on this page for exact **fs** **timestep** and **temperature**-resolved **sampling** **lengths** in **ps**/**ns** (target **K** **ranges** for melt/quench are in the **VOR** **Methods**)—**proof** pagination may not match. **Barostat** usage: follow the VOR (post-melt **NPT** at **1 atm**; ReaxFF exposure may be **NVT**). **Electric field:** **N/A**. **Enhanced sampling:** **N/A** unless the **SI** states otherwise.

## Findings

Coupling **continuum** **rigidity theory** intuition with **atomistic** **ReaxFF** maps lets the authors correlate **local** **constraint density** with **energy-resolved** **water** interaction strengths reported in the letter. The authors argue that **surface patches** near **isostatic** rigidity (~**three constraints per atom** in their mapping) exhibit **reduced** water-driven reactivity compared with **under-** or **over-constrained** regions, interpreting the result as evidence for a **topologically stabilized intermediate** surface regime. **Quantitative** thresholds and **figure** panels appear in the **VOR** PDF.

## Limitations

**Environmental** **water** **coverage** and **pH** effects beyond the simulated **vapor–surface** contact are not the focus of the abstract-level summary; consult the **full** letter for scope. **Glass** **topology** metrics depend on **cutoffs** used to define **constraints**; sensitivity analyses in the **SI** (VOR) should be consulted before exporting **quantitative** thresholds into other **silicate** projects. **Proof** PDFs can differ in **pagination**, **line breaks**, and **minor copy** from the **issue** PDF. Use **`[[2019wilkinson-j-phys-chem-topological-control]]`** for external citations.

**Confidence rationale:** `med`—duplicate proof; science on VOR page.

## Reader notes (navigation)

**Glass–water** **ReaxFF** is a recurring **theme** in the group corpus; this letter belongs alongside **wear** and **geochemical** **silicate** notes under **theme hubs** for **oxides** and **water**.

- **Version of record:** [[2019wilkinson-j-phys-chem-topological-control]]
- [[theme-oxides-silica-ceramics]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2019wilkinson-j-phys-chem-topological-control]]
- [[reaxff-family]]
