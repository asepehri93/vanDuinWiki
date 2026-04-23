---
id: paper:2013monti-venue-rsc-cp
type: paper
title: "Exploring the conformational and reactive dynamics of biomolecules in solution using an extended version of the glycine reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - material:polymer-organic
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:method-development
source_refs: []
doi: "10.1039/c3cp51931g"
year: 2013
authors:
  - "Susanna Monti"
  - "Alessandro Corozzi"
  - "Peter Fristrup"
  - "Kaushik L. Joshi"
  - "Yun Kyung Shin"
  - "Peter Oelschläger"
  - "Adri C. T. van Duin"
  - "Vincenzo Barone"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "7c8f4b462d2d30b306759cf5df6c4cc222942c79e5a3adc047e049affea8f24b"
pdf_path: "papers/Monti_ReaxFF_Peptides_galley_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013monti-venue-rsc-cp -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **PCCP** article (**DOI `10.1039/c3cp51931g`**). The corpus PDF is a **publisher proof** (queries/banner text in `normalized/extracts/2013monti-venue-rsc-cp_p1-2.txt`); confirm **final** title/figures against the **published** issue.

## Summary

Monti *et al.* describe an **extended ReaxFF** parameterization aimed at **peptide** and **protein** **solution** chemistry, building outward from a **glycine-centered** reactive model toward coverage of **all amino acids** and selected **short peptides** (*Phys. Chem. Chem. Phys.*, DOI `10.1039/c3cp51931g`; the ingested corpus PDF is a **publisher proof**, so **pagination** should be verified against the **final** **issue**). The author list includes **van Duin**-group contributors alongside **Barone**-group collaborators, reflecting a joint **QM** training and **validation** effort. The scientific goal is **reactive molecular dynamics** in **explicit water** where **proton transfer**, **hydrolysis**, and **backbone** **bond-making/breaking** events matter—phenomena that **fixed-bond** protein force fields coupled to **non-dissociating** water models cannot represent faithfully.

## Methods

**2 — Force-field training:** The parameterization expands the training corpus by adding **>500** additional **QM**-characterized systems (abstract accounting) spanning **amino-acid fragments**, **peptide motifs**, and **pharmaceutically** relevant **reaction** classes referenced in the text. **Optimization** follows the **ReaxFF** **weighted least-squares** philosophy, targeting **conformational energies**, **reaction barriers**, and **spectroscopic** benchmarks where available. **QM reference** details (**functionals**, **basis sets**, **k-sampling**, **cluster vs continuum solvation**) are specified in the article and SI rather than duplicated here (`papers/Monti_ReaxFF_Peptides_galley_2013.pdf`; **`normalized/extracts/2013monti-venue-rsc-cp_p1-2.txt`**).

**1 — MD application (validation trajectories):** **Validation** includes **~500 ps** **ReaxFF MD** segments compared against **classical non-reactive** simulations and **experimental** observables for **capped amino acids**, **peptides**, and **small proteins** (abstract). **Ensemble:** **N/A —** whether each **~500 ps** segment uses **NVT**, **NPT**, or **NVE** is **not** resolved from the galley excerpt alone—use **PCCP** **Methods**/SI (**DOI `10.1039/c3cp51931g`**). **Engine / system / PBC / timestep / thermostat / barostat / temperature / pressure / electric field / enhanced sampling:** **N/A —** **supercell** **atom** counts for each **explicit-water** biomolecular benchmark, **PBC** details, **fs** **timestep**, **thermostat**/**barostat** settings, **temperature**/**pressure** schedules, **electric fields**, and **enhanced sampling** are not taken from **`normalized/extracts/2013monti-venue-rsc-cp_p1-2.txt`** without quoting unpublished tables; **`papers/Monti_ReaxFF_Peptides_galley_2013.pdf`** + published issue are authoritative.

**3 — Static QM / DFT-only:** **N/A —** **QM** enters as **training/validation** data for **ReaxFF**, not as standalone production **AIMD** for peptide folding in this paper’s abstract-level summary.

## Findings

**Outcomes and mechanisms:** The expanded **ReaxFF** description reproduces **reference conformations** and **kinetic trends** for the **benchmark** cases highlighted in the abstract, supporting **explicit-solvent** studies where **protonation** and **reactive events** couple to **conformational sampling** (hydrolysis, **proton transfer**, backbone **bond-making/breaking**).

**Comparisons:** Validation is framed against **QM** references and **experimental** observables for **capped amino acids**, **peptides**, and **small proteins**, and against **non-reactive classical** baselines for selected observables (abstract-level summary).

**Sensitivity / design levers:** Practical use depends on **benchmark coverage** (which **chemotypes** were in the **>500**-system training expansion), **solvent model**, and **temperature**—details in the **PCCP** text rather than this note.

**Limitations and outlook:** **Transferability** must be revalidated for **new chemotypes** outside the training corpus; **computational cost** and **parameter maintenance** are higher than for **fixed-bond** protein models optimized for **structure refinement**.

**Corpus honesty:** Ingested **`pdf_path`** is a **publisher proof**; confirm **tables**, **coefficient blocks**, and **pagination** against the **final** **PCCP** issue. **`normalized/extracts/2013monti-venue-rsc-cp_p1-2.txt`** may still carry **query/banner** text from the proof stage.

## Limitations

See **Findings** paragraph above for author-stated **limitations**; this heading exists for **AGENTS** section navigation parity.

## Reader notes (navigation)

- [[reaxff-family]]
