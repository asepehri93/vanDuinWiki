---
id: paper:2018selcuk-venue-paper
type: paper
title: 'Supporting Information: Structural evolution of titanium dioxide during reduction
  in high-pressure hydrogen'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:oxides-ceramics
- method:reaxff
- method:dft-static
- task:validation
- scale:atomistic
paper_keywords:
- keyword:supporting-information
- keyword:reaxff-application
- keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: 10.1038/s41563-018-0135-0
year: 2018
authors:
- Sencer Selcuk
- Xunhua Zhao
- Annabella Selloni
venue: Nature Materials (Supporting Information)
pdf_sha256: 6a58b4d1ccf4fd20b0da3e1cdaf16f6caac8f0029f83b294550894b989a964d1
pdf_path: papers/ReaxFF_others/Selcuk_Selloni_NatureMaterials_2018_TiO2_H2_SI.pdf
extraction_quality: partial
group_affiliation: false
---
<!-- id:paper:2018selcuk-venue-paper -->

## Summary

This wiki entry registers the **Supporting Information** PDF (`papers/ReaxFF_others/Selcuk_Selloni_NatureMaterials_2018_TiO2_H2_SI.pdf`) for Selcuk, Zhao, and Selloni, *Nature Materials* **DOI `10.1038/s41563-018-0135-0`**. The parent article investigates **structural evolution of titanium dioxide during reduction in high-pressure hydrogen** using multiscale modeling that includes **ReaxFF reactive MD**; the SI package is not a standalone research article but provides **validation** material that underpins the reactive simulations. Corpus extracts emphasize **ReaxFF versus DFT/DFT+U** comparisons for **hydrogen diffusion** on **anatase** surfaces—illustrative potential-energy profiles for **surface-to-subsurface** hopping appear in supplementary figures referenced from the main text.

## Methods

Per the SI structure, validation follows pathways and coordinate definitions consistent with the main article and prior **DFT** literature on **TiO₂** surfaces: **ReaxFF** energy profiles are compared against **DFT** and **DFT+U** references along representative **H migration** coordinates on selected **anatase** facets. These static profiles complement the **nanosecond-scale** reactive trajectories reported in the primary publication by demonstrating that the force field recovers key barrier shapes needed for qualitative transferability in **H₂** reduction simulations.

**Linked production MD (parent article).** For the **reactive molecular dynamics** used in the peer-reviewed study, see **[[2018selcuk-nat-structural-evolution]]**: **LAMMPS** **ReaxFF** simulations on **anatase** **slabs**/**nanoparticles** in **high-pressure H\(_2\)** (e.g. **800 K**, **200 bar**, **NPT**-style **stress** control with **Nosé–Hoover** **thermostat**/**barostat**, **0.1 fs** **timestep**, **~1 ns** (**nanosecond**) **production** segments as reported there). **PBC:** **three-dimensional periodic** supercells. **Electric field / enhanced sampling:** **N/A — not used** in the protocol description excerpted for this SI landing page.

**SI-only limitations on this file.** The corpus extract for this **Supporting Information** PDF is thin (Fig. S1 header + caption); **N/A — full supercell stoichiometries, k-mesh settings, and additional facet benchmarks** must be read from the complete **SI** **PDF** and the main article.
## Findings

The excerpted SI material supports **qualitative alignment** between **ReaxFF** and higher-level electronic-structure calculations along the illustrated **H** diffusion coordinates, strengthening the case that the reactive MD captures the correct **hopping** hierarchy for the modeled reduction context. Full numerical barriers, convergence settings, and additional facet comparisons must be read from the **complete SI PDF** and the **main article**; this wiki page should not be treated as a substitute for those tables.

## Limitations

The corpus **`extraction_quality`** is **partial**; figures beyond the excerpt may contain additional benchmarks. Always use **`[[2018selcuk-nat-structural-evolution]]`** for the peer-reviewed narrative and citation strings.

## Reproducibility notes

When using SI energy profiles to justify production ReaxFF runs, archive the **DFT functional**, **hubbard U** choices (if any), and **k-point** settings used for the reference curves, because **DFT+U** sensitivity can shift barrier heights independently of ReaxFF quality. For **H** diffusion on **anatase**, pathway labels should match the facet and hopping coordinate definitions in the SI figures to avoid mixing distinct surface sites.

Because this corpus extract is **partial**, operators should not assume the SI contains only the single profile excerpted here: additional **facets**, **coverages**, or **convergence** studies may exist later in the PDF and should be consulted before claiming “full” validation coverage. If SI figures include **multiple** hopping pathways, ensure the production MD uses the same **rate-limiting** step identified by the lowest barrier in the benchmark set.

## Relevance to group

Documents benchmark-quality comparisons underpinning ReaxFF application to TiO2 hydrogenation.

## Citations and evidence anchors

- Main article: [[2018selcuk-nat-structural-evolution]] (DOI [10.1038/s41563-018-0135-0](https://doi.org/10.1038/s41563-018-0135-0))

## Related topics

- [[2018selcuk-nat-structural-evolution]]
- [[reaxff-family]]
