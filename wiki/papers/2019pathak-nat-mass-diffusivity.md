---
id: paper:2019pathak-nat-mass-diffusivity
type: paper
title: "Mass diffusivity and thermal conductivity estimation of chloride-based salt hydrates for thermo-chemical heat storage: A molecular dynamics study using the reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:validation-experiment
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.ijheatmasstransfer.2019.119090"
year: 2019
authors:
  - "Amar Deep Pathak"
  - "Koen Heijmans"
  - "Silvia Nedea"
  - "Adri C. T. van Duin"
  - "Herbert Zondag"
  - "Camilo Rindt"
  - "David Smeulders"
venue: "Int. J. Heat Mass Transfer"
pdf_sha256: "d4832adab5de5e957fda599e4168bbd20e3ba7de0ec308d7b252ca07deedfb98"
pdf_path: "papers/Pathak_IJHMT_2020_heat_storage.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019pathak-nat-mass-diffusivity -->

## Summary

Thermochemical heat storage in chloride salt hydrates couples dehydration and hydration kinetics to heat and mass transport inside grains and at surfaces. Pathak et al. develop transferable ReaxFF models for MgCl₂ and CaCl₂ hydrates spanning multiple hydration states so that reactive molecular dynamics can estimate water diffusivity and thermal conductivity during cycling. The study targets MgCl₂·nH₂O with n from 1 to 6 together with CaCl₂ hydrate models described in the paper, using the same methodological backbone to compare the two salts on equal footing—motivated by physical mixtures proposed for improved usability in thermal storage systems. The introduction argues that reactor design requires consistent transport coefficients across hydration states encountered during seasonal charging and discharging.

## Methods

**1 — MD application (ReaxFF-MD + SS-NEMD).** *Int. J. Heat Mass Transfer* **149**, **119090** describes **ReaxFF-MD** (reactive force field molecular dynamics) in LAMMPS-class workflows: **H₂O** diffusivity is computed through **MgCl₂·4H₂O** and **MgCl₂·6H₂O** and compared to prior **n = 0–2** work; spatial diffusivity is analyzed from **bulk** toward the **surface** to probe **dehydration**-relevant **surface** vs **bulk** effects. **Steady-state** **non-equilibrium** MD (**SS-NEMD**), using the same reactive model, gives **thermal conductivity** of **MgCl₂·nH₂O** (**n = 0, 1, 2, 4, 6**) and **CaCl₂·2H₂O**; cross-section and length along the heat-flow direction are noted in the article as **size**-sensitive for κ. **Engine:** LAMMPS with ReaxFF (as stated in the work). **System, PBC, unit cells:** hydrate supercells per Methods/SI. **Ensemble, timestep, equilibration, production, SS-NEMD** thermal gradient, **thermostats:** full tables in the PDF+SI; **N/A** to re-list every value here. **Barostat** for any **NPT** segments: as in the article. **Shear, shock, static external E-field, umbrella, metadynamics: N/A** for the reported transport setup unless the SI states otherwise.

**2 — Force-field training (ReaxFF, chloride hydrates).** The paper **proposes** new **transferable** ReaxFFs extending **MgCl₂·nH₂O** to **n = 4, 6** and a new **CaCl₂·nH₂O** model (**n = 0, 2** in the text abstract), with **DFT**/**QM** reference data, training structures, and **ParReaxFF**/**least-squares**-style **optimization** as in *IJHMT*+SI. **Reference** expt/DFT comparisons for **D** and **κ** are part of the validation.

**3 — Static QM / DFT-only** as the sole result of the study. **N/A**; transport comes from RMD/SS-NEMD.

**4 — Review or experiment-only.** **N/A.**
## Findings

### Mechanisms and transport trends

**Water diffusivities** in **MgCl₂·nH₂O** span **~10⁻¹¹–10⁻⁹ m²/s**, **comparable** to **experiment**. **Surface** effects are **minor** for **MgCl₂·6H₂O** dehydration in their treatment but **matter** for other hydrates. **Thermal conductivities** increase with **hydration** (**~0.3–0.9 W/(m·K)** across the **MgCl₂** series); **MgCl₂·6H₂O** shows **strong thermal anisotropy**.

### Mixed salts and durability

**MgCl₂/CaCl₂** blends need not **degrade bulk κ** for the composite but can alter **hydrolysis** chemistry relevant to **durability**—separating **thermal** vs **chemical** design concerns.

### Future workflow (as demonstrated)

**Parameterize hydrates → validate D → add NEMD** without changing the **reactive core**, easing **mixed-salt** extensions.

## Limitations

Reactive FF transferability should be reassessed for interfaces, dopants, and extreme temperature cycles outside training.

## Relevance to group

Extends ReaxFF into chloride hydrate thermochemical storage with van Duin-group parameterization involvement.

## Citations and evidence anchors

- DOI: [10.1016/j.ijheatmasstransfer.2019.119090](https://doi.org/10.1016/j.ijheatmasstransfer.2019.119090)

## Related topics

- [[reaxff-family]]
