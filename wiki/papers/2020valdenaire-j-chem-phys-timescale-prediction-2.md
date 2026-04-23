---
id: paper:2020valdenaire-j-chem-phys-timescale-prediction-2
type: paper
title: "Timescale prediction of complex multi-barrier pathways using flux sampling molecular dynamics and 1D kinetic integration: Application to cellulose dehydration"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:enhanced-sampling
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:galley-or-proof-pdf
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:reaxff-application
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1063/1.5126391"
year: 2020
authors:
  - "Pierre-Louis Valdenaire"
  - "Roland J. M. Pellenq"
  - "Franz J. Ulm"
  - "Adri C. T. van Duin"
  - "Jean-Marc Leyssale"
venue: "J. Chem. Phys. 152, 024123 (2020)"
pdf_sha256: "a23855f18634e0ab899a7dbe2e091de965e3cf75f85c96d469ef64d52c9bf1e2"
pdf_path: "papers/Valdennaire_JCP_2020_cellulose_dehydration.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020valdenaire-j-chem-phys-timescale-prediction-2 -->

Second corpus PDF for the same *J. Chem. Phys.* article ([DOI 10.1063/1.5126391](https://doi.org/10.1063/1.5126391)) as [[2020valdenaire-j-chem-phys-timescale-prediction]], registered under the alternate on-disk filename spelling **Valdennaire**. Scientific content matches the primary wiki page; this note exists so manifest and hash provenance stay explicit.

## Summary

The publication develops **flux sampling** along a one-dimensional reaction coordinate and **one-dimensional kinetic integration** to extrapolate rare-event kinetics for **ReaxFF** reactive MD of **crystalline cellulose** dehydration and decomposition at **1500–1900 K**, comparing volatile product distributions to **replica-exchange** benchmarks and discussing **Arrhenius** parameters and breakdown when the order parameter is inadequate at lower temperature. This wiki **duplicate-PDF** slug is for **provenance** only: **methods**, **findings**, and **limitations** are curated on [[2020valdenaire-j-chem-phys-timescale-prediction]].

## Methods

**1 — MD and rare-event protocol.** As on the VOR page: **LAMMPS**; **2013** **C–C** **Reaxff**; **I-β** **cellulose** **supercell** with **PBC**; **atom** count and **lattice** **vectors** in the **VOR** **article**; **NPT** **~2.5** **GPa**; **0.1** **fs** time step; **flux** **sampling** with **10** **ps** **MD** **segments**; **temperatures** **1500–1900** **K** in **100** **K** steps. **N/A** — re-deriving the full method narrative here: use **`[[2020valdenaire-j-chem-phys-timescale-prediction]]`** and its **PDF** for **pagination** and **thermostat/barostat** **labels**.

**2 — Force-field training.** **N/A** — not a separate refit; same published **Reaxff** as the article.

**3 — Static QM.** **N/A**.

**4 — Review.** **N/A**

## Findings

**Outcomes.** The **flux-sampling** protocol reaches longer effective times than **brute-force** **MD** for the pathway class under study. Main products (**H₂O**, **CO**, **CO₂**) line up with **replica-exchange** data where **decomposition** completes. An **Arrhenius** form gives **Eₐ** **≈** **93** **kcal** **mol⁻¹** and **k₀** **≈** **9** **×** **10¹⁹** **s⁻¹**; at **low** **T** the **kinetics** can **diverge** from a single **line** if the **order** **parameter** is **poor**—as developed on the **primary** page. **N/A** for **new** **science** via this file path alone.

**Comparisons, sensitivity, limitations, corpus honesty.** Identical in substance to [[2020valdenaire-j-chem-phys-timescale-prediction]]; this entry documents **byte**-level **duplicate** **storage** and **spelling** in **`pdf_path`**.

## Limitations

Duplicate PDFs differ only by **filename** in the corpus; replacing one file without the other can cause **hash** and manifest drift—keep one path canonical for operational sync. Use the **VOR** slug for the canonical protocol narrative and **## Limitations** of the work itself.

## Relevance to group

**Adri C. T. van Duin** co-authorship; same contribution record as the primary slug.

## Citations and evidence anchors

- DOI: [10.1063/1.5126391](https://doi.org/10.1063/1.5126391)

## Reader notes (navigation)

- **Primary curation (full methods, limitations, and thermodynamic/flux details):** [[2020valdenaire-j-chem-phys-timescale-prediction]]
- **Thematic context:** [[theme-pyrolysis-combustion-organics]], [[reaxff-family]]

## Related topics

- [[2020valdenaire-j-chem-phys-timescale-prediction]]
- [[reaxff-family]]
