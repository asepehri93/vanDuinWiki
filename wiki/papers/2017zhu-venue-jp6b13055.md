---
id: paper:2017zhu-venue-jp6b13055
type: paper
title: "Enhanced mass transfer in the step-edge-induced oxidation on Cu(100)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - method:dft-static
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:qm-training-data
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b13055"
year: 2017
authors:
  - "Qing Zhu"
  - "Wissam A. Saidi"
  - "Judith C. Yang"
venue: "J. Phys. Chem. C"
pdf_sha256: "319e1df818ba42327696b3893fb139e9e72fdcc801ebb8e8fca2b018d36c75b3"
pdf_path: "papers/ReaxFF_others/Zhu_Cu_oxidation_JPCC_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017zhu-venue-jp6b13055 -->

## Summary

**In situ transmission electron microscopy** shows stepped **Cu(100)** oxidizes to a **flat Cu\(_2\)O film**, unlike the **3D oxide islands** common on flat terraces. **ReaxFF molecular dynamics** with a **DFT-reoptimized Cu/O parameter set** argues that **mass transport from step edges**—driven by uneven **oxygen adatom** populations on **steps** versus **terraces**—feeds the morphology change. The authors analyze **lattice mismatch strain** between **Cu** and **Cu\(_2\)O** and **electrostatic** interactions as triggers, showing **Cu–O cluster** nucleation and **diffusion** accelerate **Cu** flux, especially when **surface vacancies** are present. Together, the study links **TEM**-resolved film shapes to atomistic **oxidation** transport rather than a single solid–solid transformation pathway.

## Methods

**Force-field training (ReaxFF + DFT).** The **Cu/O ReaxFF** description is **reoptimized** against **density functional theory** **energies** and **kinetic barriers** on **Cu** **slabs**, **oxides**, and related **surface** motifs referenced in the abstract, so subsequent large-scale runs retain fidelity to the **DFT** **training** set.

**Molecular dynamics (reactive).** **Molecular dynamics** with the updated **ReaxFF** compares **oxidation** on **stepped** versus **flat Cu(100)** under varying **oxygen coverage** and **temperature**, explicitly tracking **vacancy** defects and **Cu–O cluster** nucleation/**diffusion**. **Periodic** **supercells**, **atom** counts, **timestep** (fs), **thermostat**/**barostat** usage, **NVT**/**NPT** staging, and **equilibration**/**production** **duration** (ps/ns) are specified in **J. Phys. Chem. C** **2017**, **121**, **11251–11260** (`pdf_path`). **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the indexed abstract.

**Static QM / DFT.** **DFT** supplies **adsorption** and **barrier** references used during the **ReaxFF** **fit**/**validation**; it is not the large-scale **oxidation** engine.

**Review scope.** **N/A —** primary **JPCC** article connecting **TEM** motivation to **simulation**.

## Findings

**Outcomes and mechanisms.** **Oxygen adatoms** segregate differently on **step tops** versus **terraces**, enhancing **Cu** detachment from **upper step edges** and net **mass transport** toward **terrace** **oxide** products—consistent with **flat Cu₂O** films on **stepped Cu(100)** and **3D islands** on flatter surfaces in **TEM**.

**Comparisons.** **Simulated** morphology trends are tied to **experimental** **in situ TEM** observations from Zhou et al. cited in the introduction, framing **ReaxFF** as a bridge between atomistic **oxidation** kinetics and mesoscale film shapes.

**Sensitivity / design levers.** **Temperature** elevates **detachment rates** in the **MD** survey, while **surface vacancies** and **Cu–O cluster** mobility accelerate **Cu** flux, acting as explicit **sensitivity** knobs in the **oxidation** narrative.

**Limitations / outlook.** **Electrostatic** and **strain** arguments are qualitative complements to the **MD** statistics; quantitative **barrier** comparisons should be checked against the **PDF** figures.

**Corpus honesty.** This Pittsburgh-led paper is included for **ReaxFF** methodology context; confirm every numeric **barrier** from **`papers/ReaxFF_others/Zhu_Cu_oxidation_JPCC_2017.pdf`** rather than this summary alone.
## Limitations

van Duin is not listed on this Pittsburgh-led paper; it is included as corpus ReaxFF methodology on metal oxidation. Confirm all quantitative barriers and visualizations in the PDF.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.6b13055`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
