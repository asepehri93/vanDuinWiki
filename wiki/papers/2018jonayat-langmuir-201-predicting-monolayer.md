---
id: paper:2018jonayat-langmuir-201-predicting-monolayer
type: paper
title: 'Predicting monolayer oxide stability over low-index surfaces of TiO\(_2\) polymorphs using *ab initio* thermodynamics'
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
doi: "10.1021/acs.langmuir.8b02426"
year: 2018
authors:
  - "A. S. M. Jonayat"
  - "Siqi Chen"
  - "Adri C. T. van Duin"
  - "Michael J. Janik"
venue: "Langmuir"
pdf_sha256: "d28ce12a4c45f18e50b46e8e45427b81a12d4754c06d7ba7534f30bfecb83554"
pdf_path: "papers/Jonayat_MetalOxides_DFT_Langmuir_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018jonayat-langmuir-201-predicting-monolayer -->

## Summary

Oxide-on-oxide coatings are pervasive in catalysis and corrosion protection, yet predicting whether a transition-metal dioxide will wet a titania support as a coherent monolayer—and under which polymorph and facet combination—requires balancing surface energies, epitaxial strain, and electronic structure. This *Langmuir* article uses **plane-wave DFT** together with ***ab initio* thermodynamics** to compare **MO\(_2\)** (M = Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn) monolayer configurations on **low-index surfaces** of **anatase**, **brookite**, and **rutile** TiO\(_2\). The study is explicitly framed as a screening exercise: it identifies which oxide coatings are thermodynamically favored as monolayers versus bulk oxide precipitation, and it discusses when **polymorph matching** between film and support and **relative substrate surface energy** emerge as useful qualitative trends. The authors also emphasize that **no single structural or electronic descriptor** explains all computed stabilities across the broad composition space, pointing toward **multivariate** structure–property relationships for future descriptor and machine-learning work.

## Methods

Electronic-structure calculations use **VASP** with the **PBE** GGA, **PAW** pseudopotentials, and **plane-wave** expansions with **Monkhorst–Pack** **k-point** grids (per bulk and slab construction in the article). Calculations are **spin-polarized** where appropriate, and **dipole corrections** are applied for asymmetric slabs. **DFT+U** is applied to **Ti 3d** states with literature-informed **U** values tuned against band gaps and reduction energetics, using **Vosko–Wilk–Nusair** interpolation for the exchange-correlation treatment as stated in the methods. Surface models span **low-index** facets of the three TiO\(_2\) polymorphs; **monolayer** free energies** are evaluated relative to bulk oxide and particle references using the thermodynamic constructions described in the paper (including corrections noted there). Force and energy convergence criteria are set to stringent thresholds (for example **0.05 eV/Å** on forces, with additional criteria in-text). Together, these pieces define a reproducible static-lattice, **0 K** thermodynamic picture of monolayer stability for the MO\(_2\) family on TiO\(_2\).

**Dispersion / other DFT knobs.** **N/A — semi-empirical DFT-D3** (or similar) **dispersion** add-on not called out in this summary; verify in `pdf_path` if **vdW** contributions matter for the **MO\(_2\)** **monolayers**. **Reaction pathways:** **N/A — NEB** not central; the work is **ab initio thermodynamics** over relaxed **slab** **geometries**.

## Findings

**Outcomes.** **Monolayer** **stability** on **anatase**, **brookite**, and **rutile** facets is reported as a function of **M** in **MO\(_2\)**, with **interface** **energies** referenced to bulk **oxide** reservoirs in the **ab initio thermodynamics** construction.

**Comparisons / heuristics.** **Polymorph** alignment between **film** and **support** and **relative substrate surface energy** are useful **screening** rules, yet the authors stress **multifactor** **electronic**/**strain** effects—no single **descriptor** fits the entire dataset.

**Sensitivity.** **Facet** choice and **polymorph** alter predicted **wetting**/**adhesion** rankings at **0 K**; finite-**temperature** and **solvent** effects are deferred (see **Limitations**).

**Limitations and PDF grounding.** **PBE+U** band-gap and **reduction** energetics carry known **uncertainty**; static **0 K** diagrams omit **configurational entropy** and explicit **water** for operando wetting. Tabulated **stabilities** and **phase** boundaries should be read from the **Langmuir** **PDF** (`pdf_path`).
## Limitations

**PBE+U** accuracy limits quantitative oxidation/reduction energetics; **0 K** static models omit configurational entropy, explicit solvation, and finite-temperature vibrational free energy that can matter for wetting at operating conditions.

## Relevance to group

**van Duin-group** coauthored oxide interface thermodynamics that connects cleanly to later **ML descriptor** work (**[[2018jonayat-acs-discovery-descriptors]]**) and related first-principles oxide studies.

## Citations and evidence anchors

- DOI: `10.1021/acs.langmuir.8b02426`.

## Related topics

- [[2018jonayat-acs-discovery-descriptors]]
- [[2018jonayat-physical-che-first-principles-study]]
- [[reaxff-family]]
