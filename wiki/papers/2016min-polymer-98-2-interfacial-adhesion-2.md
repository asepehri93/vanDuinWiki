---
id: paper:2016min-polymer-98-2-interfacial-adhesion-2
type: paper
title: "Interfacial adhesion behavior of polyimides on silica glass: A molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:polymer-organic
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.polymer.2016.06.017"
year: 2016
authors:
  - "Kyoungmin Min"
venue: "Polymer, 98 (2016) 1-10"
pdf_sha256: "b4bb5318d0b2504eeaf8bf0ca0d19abe5964bed37c60538e56c8219302dcdbde"
pdf_path: "papers/ReaxFF_others/kyonming et.al. 2016 polymer.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016min-polymer-98-2-interfacial-adhesion-2 -->

## Summary

This slug records a **duplicate PDF path** for the *Polymer* (2016) article **DOI [10.1016/j.polymer.2016.06.017](https://doi.org/10.1016/j.polymer.2016.06.017)** on **polyimide** adhesion to **silica glass**, with file `papers/ReaxFF_others/kyonming et.al. 2016 polymer.pdf` (distinct SHA-256 from **`[[2016min-polymer-98-2-interfacial-adhesion]]`** using `Corning_Samsung_polymer_2016.pdf`). The peer-reviewed work investigates adhesion relevant to **flexible display** manufacturing: **steered molecular dynamics (SMD)** with a **reactive force field (ReaxFF)** pulls polyimide films from **SiO₂** glass to obtain **potentials of mean force (PMF)**, **pulling distance**, and **pulling force**, relating response to **coefficient of thermal expansion** and **chain conformation** near the interface. The abstract states that polyimides with **lower thermal expansion** require **greater peak force** but **shorter pull distance** for full detachment; chains **near the interface** dominate the molecular response due to **stronger adhesion** to glass; **bond** and **Coulomb** terms from the interatomic potential dominate deformation energy; and **failure mode** analysis indicates **adhesive failure** as the dominant mechanism across polyimide types considered. Industry co-authors from **Samsung**-affiliated labs and **Corning** situate the motivation in **flexible display** process reliability, where debonding from **carrier glass** must be controlled—this context is developed in the introduction of the full article.

## Methods

**Simulation paradigm.** Same **LAMMPS** **ReaxFF** **SMD** description as **`[[2016min-polymer-98-2-interfacial-adhesion]]`**: **3D periodic** **polyimide–SiO₂ hybrid supercells**, **1 ns** **NVT** relaxation at **300 K**, **1 ns** **NPT** at **300 K**/**1 atm** in **x/y** only, **Nose-Hoover** **thermostat** and **barostat** (**100 fs / 1000 fs** damping), **0.5 fs** **velocity Verlet** integration, then **NVT** **SMD** pulls at **50 m/s** with **100 kcal/mol/Å²** spring constant. **External electric fields** and **umbrella/replica/metadynamics** are **not** used (**N/A**). **Pressure during the pull** is **N/A** (**NVT**).

## Findings

Same abstract-level results as [[2016min-polymer-98-2-interfacial-adhesion]]: lower thermal expansion correlates with higher peak pull force yet shorter pull distance to detach polyimide from silica, and interfacial chains dominate the mechanical response. Multiple polyimide chemistries share one silica substrate under identical SMD settings, with CTE as the main materials knob for PMF, force, and distance trade-offs. Steered-MD path dependence and pull-rate effects are general limitations of Jarzynski/PMF workflows—see the discussion in the registered PDF.

**Corpus note.** Duplicate PDF path (`papers/ReaxFF_others/kyonming et.al. 2016 polymer.pdf`); use the primary slug for figure-quality PMF plots when scans differ.

## Limitations

Two **PDFs** for one **DOI** require operators to track which blob is canonical for figures. **ReaxFF** adhesion numbers are model-dependent. **SMD** pulling speeds and spring constants (given in the article) set the **Jarzynski**/**PMF** interpretation window; reported forces are path-dependent in the usual steered-MD sense and should be compared to experiment only with that caveat.

## Relevance to group

Illustrates **ReaxFF** **SMD** for **organic–oxide** interfaces—adhesion, **display** substrates, and packaging.

## Citations and evidence anchors

- DOI: [10.1016/j.polymer.2016.06.017](https://doi.org/10.1016/j.polymer.2016.06.017)

## Reader notes (navigation)

- Primary PDF path: [[2016min-polymer-98-2-interfacial-adhesion]]

## Related topics

- [[2016min-polymer-98-2-interfacial-adhesion]]
- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
