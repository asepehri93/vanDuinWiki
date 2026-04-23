---
id: paper:2007administrator-venue-microsoft-word
type: paper
title: "Additional QM vs. ReaxFF comparison for CHO training set (supporting information)"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:supporting-information
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2007
authors:
  - "Kimberly Chenoweth"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Supporting information (manuscript supplement)"
pdf_sha256: "02d4e9365abe70d58a857af3c157e9dc21ec14d8ac6231841d5b792e83225d04"
pdf_path: "papers/CHO_supplements/ReaxFF_CHO_additional_training_results.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2007administrator-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **supporting table** in the PDF identified by `pdf_path`. **Numerical agreement** should be verified against the **table in the PDF**; the extract is a partial mirror.

## Summary

This supplement tabulates **additional comparisons of quantum-mechanical and ReaxFF reaction energetics** used in the ReaxFF training set for “A ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation” (Chenoweth, van Duin, Goddard). The extract includes rows grouped by reaction class (e.g., dehydrogenation, C=O bond dissociation, C=C bond dissociation, O–O bond dissociation, C–H dissociation) with paired ReaxFF and QM values as printed in Table 1.

## Methods


Supporting Table 1 lists reaction energetics side by side from ReaxFF and quantum mechanics for reactions included in the ReaxFF training set for hydrocarbon oxidation. Rows are grouped by reaction class in the PDF (dehydrogenation, C=O bond dissociation, C=C bond dissociation, O–O bond dissociation, and C–H dissociation). Energies are reported as printed in the table (same units as in the manuscript—typically kcal mol\(^{-1}\) in the parent CHO ReaxFF work). This supplement is a data table for parameterization QA; interpretation of weighting, objective function, and overall fit quality appears in the main article.

### MD application (not reported)

This supplement is a **QM vs ReaxFF** energetics table, not an MD trajectory appendix. **N/A — molecular dynamics engine** (no trajectories here); **N/A — atom counts**; **N/A — PBC**; **N/A — NVE/NVT/NPT**; **N/A — timestep**; **N/A — trajectory length** (no **ps**/**ns** **production** runs in this table); **N/A — equilibration** trajectories; **N/A — thermostat**; **N/A — barostat**; **N/A — MD temperature**; **N/A — MD pressure**; **N/A — electric field**; **N/A — enhanced sampling**.

### Force-field training (what the table encodes)

**Parent FF / elements:** **ReaxFF** **C/H/O** combustion training-set reactions for the Chenoweth–van Duin–Goddard oxidation manuscript. **QM reference:** **QM** column entries paired with **ReaxFF** for each reaction (programs/functionals documented in the **parent paper**, not reprinted on this table page). **Training set / reference data:** grouped **reaction energies** for **dehydrogenation**, **C=O** / **C=C** cleavage, **O–O** cleavage, and **C–H** families as printed. **Optimization:** **N/A — optimizer weights** in this PDF fragment—see the main text. **Reference data used:** side-by-side **QM** and **ReaxFF** values for **validation** of the fit. Grounding: `papers/CHO_supplements/ReaxFF_CHO_additional_training_results.pdf`, `normalized/extracts/2007administrator-venue-microsoft-word_p1-2.txt`.

## Findings

Table 1 lists side-by-side **ReaxFF** and **QM** reaction energetics (kcal mol\(^{-1}\) in the manuscript convention) for reactions in the CHO training set, grouped by class (dehydrogenation, C=O and C=C dissociation, O–O cleavage, C–H and other bond-breaking families, plus additional rows). Examples in the extract include dehydrogenation entries such as **\(-149.7\)** (ReaxFF) vs **\(-150.2\)** (QM) and **\(-47.2\)** vs **\(-21.0\)**, C=O dissociation rows such as **\(175.7\)** vs **\(180.5\)**, and peroxide-related rows with larger gaps such as **\(142.0\)** vs **\(91.6\)**. The SI also plots ReaxFF vs QM for selected **C–C** and **C=O** distance scans and angle distortions (Figures 1–2 in the PDF). Overall fit quality and weighting are discussed in the **peer-reviewed parent paper**, not in this table alone.

## Limitations

- Interpretation of individual discrepancies belongs to the **main paper**; this page is a locator for the SI table.
- Filename/metadata “System Administrator” in legacy records is **not** treated as authorship; author list follows the stated manuscript attribution in the supplement text.

## Relevance to group

**Adri C. T. van Duin** is a named co-author on the parent hydrocarbon-oxidation ReaxFF work; this table is direct **training-data documentation** for that parameterization line.

## Citations and evidence anchors

- PDF: `papers/CHO_supplements/ReaxFF_CHO_additional_training_results.pdf`.
- Extract: `normalized/extracts/2007administrator-venue-microsoft-word_p1-2.txt`.

## Related topics

- [[reaxff-family]]
