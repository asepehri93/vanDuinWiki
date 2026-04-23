---
id: paper:2018jonayat-acs-discovery-descriptors
type: paper
title: "Discovery of descriptors for stable monolayer oxide coatings through machine learning"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - domain:catalysis-surfaces
  - method:dft-static
  - task:method-development
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:dft-static
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1021/acsaem.8b01261"
year: 2018
authors:
  - "A. S. M. Jonayat"
  - "Adri C. T. van Duin"
  - "Michael J. Janik"
venue: "ACS Appl. Energy Mater."
pdf_sha256: "be189a19ac74a0fdfe5bfaf7fdff844d3a109d1fdc6fa6142b20399a4515aeb4"
pdf_path: "papers/Jonayat_MetalOxides_ML_ACS_AEM_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018jonayat-acs-discovery-descriptors -->

## Summary

Screening monolayer oxide coatings on oxide supports with exhaustive density functional theory is expensive, yet simple linear models may suffice if informative descriptors can be identified. Jonayat, van Duin, and Janik train supervised LASSO regression models that map DFT-computed monolayer oxide stabilities for coating/support pairs onto physically interpretable features drawn from tabulated ionic, electronic, and surface properties. They separately treat stoichiometric and nonstoichiometric monolayer oxides to reflect different defect chemistries important in catalysis. The motivation ties to supported catalyst design where monolayer oxides can stabilize interfaces but where brute-force DFT across composition grids is prohibitive. The article’s machine-learning layer is deliberately sparse and interpretable rather than a black-box neural network, aiding experimental guidance.

## Methods

Training labels come from DFT (PBE family with Hubbard corrections where noted in companion work) evaluations of monolayer adhesion or stability relative to bulk references across transition-metal oxide coatings on oxide supports; exact dataset scope appears in the article and Supporting Information. Input features include substrate surface energies, ionic/atomic radii, ionization potentials, and parent oxide stability metrics as enumerated in the feature table. LASSO regression selects sparse descriptor sets with cross-validation protocols defined in the SI. Feature scaling and colinearity checks matter because tabulated radii and energies can correlate. Reproducibility requires the same DFT settings, dataset splits, LASSO hyperparameters, and random seeds documented in DOI 10.1021/acsaem.8b01261.

**Static QM / DFT details.** **Functional / Hubbard:** **PBE**-family **DFT** with **DFT+U** on localized **d** states where noted for transition-metal **oxides** (exact **U** values and **XC** treatment in **Methods**/**SI**). **Dispersion:** **N/A — explicit DFT-D3 / pairwise vdW correction** not highlighted in this wiki summary; confirm whether the publication applies a **vdW** correction in `pdf_path`. **Basis / potentials:** **plane-wave** expansion with **PAW** **pseudopotentials** as in companion oxide-screening work from the same series. **k sampling:** **Monkhorst–Pack** **k-point** meshes sized per **slab** / **bulk** calculation in the article. **Structures:** relaxed **oxide** **surfaces** and **monolayer** configurations for **coating/support** pairs; **N/A — NEB transition-state pathways** as the primary object—the study targets **adhesion/stability** **energies** rather than reaction barriers. **Properties:** **formation**/**adhesion**-type **energies** feeding **LASSO** labels plus tabulated **electronic**/**ionic** descriptors.

## Findings

**Outcomes.** For **stoichiometric** mixed **oxides**, **LASSO** selects **substrate** **surface** **energy**, **orbital radii**, and **ionization** **energies** as dominant descriptors of **monolayer** stability. For **nonstoichiometric** films, **parent** **oxide** **stability** and **oxidation-state mismatch** between **coating** and **support** dominate.

**Comparisons.** Sparse linear models **benchmark** against brute-force **DFT** screening costs while staying interpretable versus black-box **ML**.

**Sensitivity / practice levers.** **Oxidation state** metadata and explicit **stoichiometry** tags materially change which descriptors survive **LASSO**—mixing regimes collapses interpretability even if error improves marginally.

**Limitations and PDF grounding.** **DFT+U** errors on correlated **oxides** and narrow **training** chemistry imply **extrapolation** risk; coefficients are **not** portable if the **functional**/**U** recipe changes. Numeric **dataset** sizes, **cross-validation** splits, and **bootstrap** uncertainty should be taken from the **ACS Appl. Energy Mater.** **PDF**/SI (`pdf_path`).
## Limitations

DFT errors on strongly correlated oxides and limited coverage of synthesis environments mean extrapolation risk outside the training chemistry.

## Relevance to group

van Duin-group coauthorship on descriptor learning for oxide interfaces—complements ReaxFF applications by targeting DFT screening.

## Citations and evidence anchors

- DOI: `10.1021/acsaem.8b01261`.

## Related topics

- [[2018jonayat-langmuir-201-predicting-monolayer]]
- [[2018jonayat-physical-che-first-principles-study]]
- [[reaxff-family]]
