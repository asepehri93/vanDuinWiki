---
id: debate:transferability-reactive-ff
type: debate
title: "Transferability of reactive force fields across phases and chemistries"
updated: "2026-04-23"
confidence: med
canonical_tags: [domain:reaxff-lineage, task:review, scale:atomistic]
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Summary; Methods; Findings"
    note: "LATP-focused ReaxFF development and composition-dependent conductivity behavior in solid electrolyte context"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Summary; Methods; Findings"
    note: "Organic carbonate electrolyte extension with Li+/Li0 distinction and chemistry-specific reactive pathways"
positions:
  - name: "Strong locality"
    summary: "A ReaxFF fit is reliable only for element combinations and coordination environments represented in its training set."
  - name: "Pragmatic reuse"
    summary: "Teams often reuse published sets as starting points and re-fit subsets when moving to adjacent chemistries."
evidence:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Methods; Findings"
    note: "Supports both positions: targeted LATP fit performs within that domain, while conductivity remains sensitive to composition and sampled structural realization"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Summary; Methods; Findings"
    note: "Supports need for chemistry-specific extension from solid-state domains to liquid carbonate electrolyte reactions"
---

<!-- id:debate:transferability-reactive-ff -->

!!! abstract "TL;DR"

    In this corpus, reactive force-field transferability is not a binary property. Evidence supports a conservative view (transfer is local to trained chemistries and environments) and a practical workflow view (published parameter sets can be reused as starting points when extension and revalidation are explicit).

## Position statements

- **Position A - Strong locality:** ReaxFF parameterizations are trustworthy mainly inside the chemistry and configuration space represented in their training and validation sets; moving across phase or reaction class without retraining is high-risk.
- **Position B - Pragmatic reuse with extension:** Existing parameterizations are often useful starting points, but reliable transfer requires explicit extension and revalidation for the new domain.

## Evidence by position

- **Evidence for Position A (strong locality):** `paper:2018shin-physical-che-development-reaxff` reports composition-sensitive conductivity behavior within LATP, including differences across structural realizations. Even inside one materials family, transport outcomes depend on the represented local environment, which argues against assuming broad transferability.
- **Evidence for Position B (pragmatic reuse with extension):** `paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation` extends reactive modeling to organic carbonate electrolyte chemistry by adding targeted training data and a Li+/Li0 treatment. This supports reuse as a workflow pattern, but only with domain-specific augmentation.
- **Shared empirical pattern across both papers:** each study is fit-for-purpose in its own scope (ceramic solid electrolyte versus liquid carbonate electrolyte chemistry), and both imply that "same method family" does not by itself guarantee cross-domain fidelity.

## Scope conditions and applicability

- **Likely valid scope for Position A:** transferring between different phases (crystalline ceramic to liquid organic) or different dominant reaction channels without retraining.
- **Likely valid scope for Position B:** adjacent chemistries where prior parameterization work is available and the new use case includes explicit retraining targets plus validation checks.
- **Corpus boundary:** this debate is grounded in two battery-related papers and should not be interpreted as a universal statement for all ReaxFF parameterizations in all domains.

## Shared ground

- Both positions agree that transferability must be evidenced, not assumed.
- Both positions agree that validation metrics tied to the new target task are required before claiming predictive use.
- Both positions agree that publication-specific scope statements should guide reuse decisions.

## What evidence would resolve this

- Side-by-side cross-domain tests using one parameter set without retraining versus with retraining, evaluated on the same held-out observables.
- Standardized transferability benchmark suites spanning phase changes (solid electrolyte structures to liquid electrolytes) and reaction-class changes (transport-dominant to decomposition-dominant regimes).
- Clear failure diagnostics in paper pages (which observables fail first under transfer, and under what composition/temperature windows).

## Practical implications for modeling choices

- For this corpus, treat each ReaxFF parameter set as domain-scoped by default.
- When reusing an existing set, document what is inherited, what is re-fit, and what new validation targets are added.
- Route method selection through [[reaxff-family]] and related protocol pages, and tie confidence on downstream synthesis pages to explicit evidence coverage.
