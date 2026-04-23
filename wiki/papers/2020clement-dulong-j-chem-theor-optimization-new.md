---
id: paper:2020clement-dulong-j-chem-theor-optimization-new
type: paper
title: "Optimization of a New Reactive Force Field for Silver-Based Materials"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - task:parameterization
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:metallic-systems
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.0c00480"
year: 2020
authors:
  - "Clément Dulong"
  - "Bruno Madebene"
  - "Susanna Monti"
  - "Johannes Richardi"
venue: "J. Chem. Theory Comput."
pdf_sha256: "5b30d7746726329b88fc3cfdbd0ac0fb2d60579d6e876b1cd396f4b2baee8205"
pdf_path: "papers/ReaxFF_others/Dulong_AgS_JCTC_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020clement-dulong-j-chem-theor-optimization-new -->

A **ReaxFF** reparameterization for **Ag** and **Ag–thiolate** systems using **>120 QM structures**, **MCFF** optimization in **ADF**, and validation MD in **ADF/LAMMPS** against prior Au/S thiolate literature behavior.

## Summary

The authors introduce **AgSCH-ReaxFF**, fit with Monte Carlo force-field (**MCFF**) sampling to DFT training data on silver clusters, slabs, and thiolate adsorption. The new parameter set improves average geometries and energetics versus earlier Ag/Au ReaxFF descriptions for many benchmarks, while acknowledging limits at highly under-coordinated edge sites. MD snapshots compare **Au vs Ag** thiolate SAMs, including staple motifs on gold but not on silver under their silver model. The parameterization targets **organosulfur** chemistry at **Ag** interfaces relevant to **SERS**, **self-assembled monolayers**, and **nanoparticle** coatings where prior **Au-centric** ReaxFF descriptions are a common starting point but **Ag-specific** bonding errors accumulate.

## Methods

- **Training data:** Diverse **Ag** clusters (sizes and isomers), **bulk/surface** slabs, and **thiol/thiolate** reactions; QM references primarily **DFT** as described (functionals/basis sets in article and SI).
- **Optimization:** **MCFF** implementation in **ADF** to adjust selected ReaxFF parameters against the training set.
- **MD validation:** Production runs with **ADF** and **LAMMPS** ReaxFF modules; **timestep 0.25 fs**, **Berendsen** thermostat (**5 fs** damping), total **~100 ps** segments as reported; **NVT** heating/cooling protocols for SAM studies (e.g., snapshots near **100 K** for comparison figures). **PBC** for **slab** and **SAM** supercells; **barostat: N/A** in the **NVT** **validation** **windows** described here; **pressure: N/A** for those **constant-volume** **NVT** runs. **Electric field: N/A**; **umbrella / metadynamics: N/A**.

## Findings

- New parameters better reproduce **average** cluster and slab energetics vs older Ag ReaxFF and track **Ag\(_{20}\)** pyramid **thiolate** adsorption comparably to gold benchmarks.
- **Edge-shortening** artifacts for under-coordinated Ag atoms remain imperfect—an intrinsic limitation noted by the authors.
- **SAM simulations** on **Ag(111)** do **not** show **Au–S–Au staple** motifs that appear in gold SAMs with prior parameterizations—consistent with differing experimental pictures for Ag.
- The article positions **MCFF** optimization as a practical route to large **training-set** fits while flagging **residual** errors where **coordination** is extremely low—an important caveat for **nanocluster** applications.

## Limitations

Residual errors for low-coordination geometries; thiolate chemistry extrapolated beyond training chemistries should be revalidated. **SAM** comparisons to **gold** **staple** motifs are **qualitative** **structural** contrasts; quantitative **free energies** of **disorder** and **domain** boundaries on **Ag(111)** may require longer sampling than the **~100 ps** illustrative segments quoted in the article. **MCFF** **fits** can be sensitive to **weighting** of **cluster** versus **surface** **targets**; reproduce **optimization** **settings** from the **primary** **text** before **porting** **parameters** into new **workflows**.

## Relevance to group

Core **ReaxFF parameterization** reference for **Ag** and **organosulfur/metal interfaces**, relevant to catalysis and nanocarbon/metal hybrid contexts.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.0c00480](https://doi.org/10.1021/acs.jctc.0c00480)

## Related topics

- [[reaxff-family]]
