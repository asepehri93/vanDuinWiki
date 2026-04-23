---
id: paper:2018jonayat-physical-che-first-principles-study
type: paper
title: 'A first-principles study of stability of surface confined mixed metal oxides with corundum structure (Fe\(_2\)O\(_3\), Cr\(_2\)O\(_3\), V\(_2\)O\(_3\))'
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:catalysis-surfaces
  - method:dft-static
  - task:application
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1039/c8cp00154e"
year: 2018
authors:
  - "A. S. M. Jonayat"
  - "Alan Kramer"
  - "Luca Bignardi"
  - "Paolo Lacovig"
  - "Silvano Lizzit"
  - "Adri C. T. van Duin"
  - "Matthias Batzill"
  - "Michael J. Janik"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "51253e6a40e2f7ff4eaafb92b7d294eb804f1d0ac3344135958ab6b6bef0820a"
pdf_path: "papers/Jonayat_Metaloxide_confined_PCCP_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018jonayat-physical-che-first-principles-study -->

## Summary

Surface-confined mixed oxides with corundum structure appear in oxidation catalysis and corrosion contexts, yet composition segregation and termination stability are difficult to probe experimentally at atomic resolution. This collaboration combines density functional theory with surface-science experiments to evaluate (0001) terminations of Fe₂O₃, Cr₂O₃, and V₂O₃ and Fe substitution in V₂O₃(0001). Plane-wave PAW calculations with Hubbard corrections on localized d states capture transition-metal oxide electronic structure. Thermodynamic analyses using oxygen chemical potentials compare surface-confined configurations to bulk and subsurface exchange scenarios, predicting when Fe enriches at the surface versus subsurface under aggressive temperature and oxygen-potential conditions.

## Methods

DFT uses the **PBE** functional with **Hubbard U** parameters appropriate to **Fe**, **Cr**, and **V** oxides. **Basis set / potentials:** **plane-wave** expansions with **PAW** pseudopotentials (**VASP**-style setup per *PCCP* **Computational Details**). **k-point sampling:** **Monkhorst–Pack** **k-point** meshes specified separately for **bulk** references and **(0001)** **slab** supercells. **Slab models** represent **(0001)** surfaces with **dipole** corrections as needed. **Surface energies** and **segregation energies** enter thermodynamic constructions versus **oxygen chemical potential**. Experimental collaborators provide spectroscopic grounding discussed in the **PCCP** article. Adri van Duin’s role connects reactive modeling expertise to the broader oxide stability question even though the core results here are **DFT**-forward.

Surface-confined mixed oxides are represented as thin corundum-structured films where cation segregation can lower surface energy relative to homogeneous compositions, motivating the oxygen-potential diagrams used to predict stable terminations.

**Dispersion / pathways.** **N/A — Grimme DFT-D** style corrections not highlighted in this summary—confirm in `pdf_path` if needed for weakly bound adsorbates. **NEB / reaction coordinates:** **N/A** as the primary deliverable; the focus is **surface** **energies**, **segregation** **energies**, and **oxygen** **chemical potential** diagrams.

## Findings

**Outcomes.** **Corundum** **(0001)** **terminations** of **Fe\(_2\)O\(_3\)**, **Cr\(_2\)O\(_3\)**, and **V\(_2\)O\(_3\)**, plus **Fe** substitution in **V\(_2\)O\(_3\)(0001)**, are ranked using **DFT** **energies** combined with **μ\(_O\)** diagrams to predict **reduction**-friendly **configurations**.

**Comparisons.** **Surface-science** **spectroscopy**/**microscopy** in the **PCCP** article **benchmark** predicted **terminations** and **reduction** behavior against **experiment**.

**Sensitivity.** **Fe** surface enrichment appears only in aggressive **temperature**/**low μ\(_O\)** windows; **Fe** doping increases **reducible** character relative to endmembers in the model space shown in the figures.

**Limitations and PDF grounding.** **0 K** **DFT** omits **entropy**/**kinetic trapping**; **Hubbard U** shifts absolute **energies**. Quantitative **boundaries** belong to the **PCCP** **PDF** figures (`pdf_path`), not extrapolated here.
## Limitations

0 K DFT with mean-field thermodynamics omits entropic contributions from adsorbates and kinetic trapping; U values influence absolute energies.

## Corpus notes

When cross-walking to ReaxFF simulations of the same oxides, document which surface terminations were fixed in DFT versus allowed to react in MD, because the thermodynamic diagrams here assume static slabs without explicit solvent.

Surface oxygen chemical potentials in the figures should be translated to experimental \(p_{\mathrm{O_2}}, T\) windows using the same thermodynamic conventions the authors document, rather than ad hoc scalings from unrelated catalysis datasets.

## Relevance to group

van Duin-group participation in **oxide catalysis** stability alongside experimental surface-science partners.

## Citations and evidence anchors

- DOI: [10.1039/c8cp00154e](https://doi.org/10.1039/c8cp00154e)

## Related topics

- [[2018jonayat-langmuir-201-predicting-monolayer]]
- [[2018jonayat-acs-discovery-descriptors]]
- [[reaxff-family]]
