---
id: paper:2016cui-physical-che-lithium-ion
type: paper
title: "Lithium ion solvation by ethylene carbonates in lithium-ion battery electrolytes, revisited by density functional theory with the hybrid solvation model and free energy correction in solution"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1039/C6CP01667G"
year: 2016
authors:
  - "Wei Cui"
  - "Yves Lansac"
  - "Hochun Lee"
  - "Seung-Tae Hong"
  - "Yun Hee Jang"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "221b8a897417b6dc4f24600b2dcc0faa6a0288b80d1b75c233cb6afb7eb14405"
pdf_path: "papers/Others/Cui_Lansac_YunHee_PCCP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016cui-physical-che-lithium-ion -->

## Summary

Ion conductivity in lithium-ion batteries depends on how Li⁺ is solvated by carbonate solvents; ethylene carbonate (EC) is a high-dielectric component of typical electrolytes. Cui *et al.* revisit the first-shell solvation number of Li⁺(EC)\(_n\) using **DFT** combined with a **hybrid solvation model**: an explicit Li⁺(EC)\(_n\) cluster sits inside a continuum representing bulk EC, augmented by a gas-to-solution standard-state correction, Monte Carlo sampling of initial structures, and a Gibbs free-energy correction based on a free-volume treatment for EC solution (as laid out in the PCCP *Assumptions, corrections and calculation details* section). The abstract reports the most probable solvation number **\(n = 4\)** and a solvation free energy of about **\(-91.3\)** kcal mol⁻¹ under that protocol, and describes **desolvation toward \(n \approx 2\)** upon reduction near anodes.

## Methods

**Static QM / DFT (primary):** Geometries and standard-state Gibbs energetics for **Li⁺(EC)\(_n\)** with **\(n = 1\)–\(6\)** use **B3LYP** with a **Gaussian-type basis set** **6-31G(d,p)** in **Jaguar** (v8.5). Each species is assigned **\(\Delta G^\circ_\mathrm{EC} = \Delta G^\circ_\mathrm{g} + \Delta G^\circ_\mathrm{solv}\)**; **\(\Delta G^\circ_\mathrm{solv}\)** uses a **Poisson–Boltzmann continuum** for bulk **EC** with a **\(\varepsilon_\mathrm{solute} = 1\)** cavity inside the high-dielectric medium. The protocol layers (1) a **hybrid** explicit first shell in implicit bulk **EC**, (2) a **gas-to-solution** standard-state correction, (3) **Monte Carlo** sampling of cluster **geometries**, and (4) a **free-volume** Gibbs correction for **EC** solution when comparing **\(\Delta\Delta G^\circ_\mathrm{b}\)** across **\(n\)**. **Periodic k-mesh / Brillouin sampling:** **N/A — isolated molecular clusters**, not periodic solids. **Dispersion correction (DFT-D):** **N/A — not stated on the excerpt used here.** **Properties computed:** **Gibbs free energy** differences (**\(\Delta G^\circ\)**, **\(\Delta\Delta G^\circ_\mathrm{b}\)**) vs **\(n\)**, inferred **first-shell solvation number** (**\(n = 4\)** dominant) and **desolvation toward \(n \approx 2\)** upon reduction, as reported in the abstract (numeric anchor **\(\Delta G_\mathrm{solv} \approx -91.3\)** kcal mol⁻¹ in the abstract text).

**MD application (atomistic dynamics):** **N/A — not used**; solvation structure is treated with **static DFT** plus statistical corrections, not finite-temperature explicit-solvent MD.

**Force-field training:** **N/A — not a force-field parameterization study.**

## Findings

Hybrid solvation recovers \(n = 4\) as the dominant first-shell coordination for Li⁺ in EC and thermodynamic trends consistent with simpler models, while allowing analysis of desolvation sequences relevant to intercalation and solid–electrolyte interphase formation. Reduction-driven desolvation toward smaller \(n\) is captured as stated in the abstract, linking gas-phase cluster data to electrode-relevant states.

The abstract’s numerical anchor (\(\Delta G_\mathrm{solv} \approx -91.3\) kcal mol⁻¹ for the primary solvation environment reported there) is explicitly tied to the hybrid thermodynamic cycle, giving readers a quantitative check when comparing to implicit-only continuum models that may shift absolute solvation energies. Desolvation toward \(n \rightarrow 2\) is framed as the relevant partially stripped species approaching reducing anodes, consistent with two-electron reduction channels discussed in the electrochemical context of the paper.

## Limitations

Static cluster models omit finite concentration, ion pairing with anions, and dynamic exchange timescales present in electrolytes; implicit outer solvation depends on cavity parametrization.

## Relevance to group

Electrolyte solvation physics adjacent to battery interface and reactive MD studies of SEI chemistry in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/C6CP01667G](https://doi.org/10.1039/C6CP01667G)

## Related topics

- [[batteries-interfaces-reaxff]]
