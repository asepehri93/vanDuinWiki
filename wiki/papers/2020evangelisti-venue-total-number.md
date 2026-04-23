---
id: paper:2020evangelisti-venue-total-number
type: paper
title: "Development and initial applications of an e-ReaxFF description of Ag nanoclusters (AIP author proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1063/5.0018971"
year: 2020
authors:
  - "Benjamin Evangelisti"
  - "Kristen A. Fichthorn"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "e7895fa11a0bdc20a2d563430542aa418d93d3183f64ac2b360a3cb705533968"
pdf_path: "papers/Evangelisti_JCP_Ag_clusters_eReaxFF_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020evangelisti-venue-total-number -->

## Summary

This wiki row registers an American Institute of Physics author-proof PDF for the Journal of Chemistry Physics article on e-ReaxFF parametrization for silver nanoclusters (DOI `10.1063/5.0018971`). Proof-stage files can contain author queries, provisional pagination, and layout artifacts; for stable figure numbering and final wording, readers should prefer the version-of-record PDF curated on **`[[2020evangelisti-j-chem-phys-development-initial]]`**. Substantively, the publication develops an explicit-electron ReaxFF (e-ReaxFF) parametrization for silver and applies it to small Ag\(_N\) clusters (up to \(N \le 20\) in the work’s scope), comparing two-dimensional versus three-dimensional isomer energetics against quantum-chemistry references, and illustrating dynamics including silver–halide redox and electron-rich plasmon-like behavior in molecular dynamics. The van Duin and Fichthorn collaboration places the work in the group’s lineage of reactive and charge-aware force fields beyond classical ReaxFF for main-group oxides alone.

## Methods

**Provenance:** This slug tracks the **AIP author-proof** PDF; **[[2020evangelisti-j-chem-phys-development-initial]]** is the **canonical** **wiki** **target** for **Methods** **tables**.

**Force-field training (e-ReaxFF):** **QM** references include **DFT** and **CCSD(T)** for **Ag\(_N\)** **isomers**; **e-ReaxFF** adds **explicit** **classical** **electrons** and a **dihedral** **penalty** to capture **2D**/**3D** **competition**; **fit** to **barriers** and **energy** **orderings** as in the **JCP** **article**.

**MD application (condensed from VOR, match [[2020evangelisti-j-chem-phys-development-initial]]):** Molecular dynamics in the standalone ReaxFF code (engine slot); isolated Ag\(_N\) cluster cells with open/non-bulk boundary treatment (boundary slot); on the order of 10–200 Ag atoms per cell in the training sizes cited on the VOR page (system slot). NVT; Nosé–Hoover thermostat; 0.250 fs timestep. Production and equilibration lengths in ps as in the JCP article (duration slot). Thermostated runs including 300 K setpoints in application sections (temperature slot). Barostat: N/A. Hydrostatic pressure: N/A. Electric field: N/A. Enhanced sampling: N/A.

## Findings

Reported conclusions match the curated article page: the e-ReaxFF model tracks low-\(N\) preference for two-dimensional lowest-energy Ag structures and captures the onset of three-dimensional motifs near Ag\(_7\) in the sub-twenty-atom regime, improving on embedded-atom descriptions for planar versus nonplanar competition where cited in the paper. Application sections discuss oxidation-state changes in silver-halide-like environments and electron dynamics in large-scale MD. Quantitative energies, cluster geometries, and figure references should be quoted from the version-of-record note, not from the proof PDF alone. Explicit-electron ReaxFF extends the group’s reactive modeling toolkit into coinage-metal clusters where classical fixed-charge models omit redox flexibility.

## Limitations

Author proofs may differ from the published article in copy editing, figure resolution, and page breaks; **`[[2020evangelisti-j-chem-phys-development-initial]]`** is the canonical wiki target for citations. e-ReaxFF remains an empirical model; excited states and quantitative optical properties require validation beyond the fitted training sets.

## Relevance to group

Provenance duplicate for van Duin-group e-ReaxFF on metallic silver; narrative and MAS anchors live on the VOR page.

## Citations and evidence anchors

- DOI: [10.1063/5.0018971](https://doi.org/10.1063/5.0018971)

## Reader notes (navigation)

- [[2020evangelisti-j-chem-phys-development-initial]]

## Related topics

- [[reaxff-family]]
