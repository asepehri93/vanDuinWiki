---
id: methodprotocol:battery-interface-reactivity-workflow
type: methodprotocol
title: "Battery interface reactivity workflow (ReaxFF with DFT-grounded checks)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    section: "Summary; Methods; Findings"
    note: "LATP case for DFT-trained ReaxFF and conductivity-oriented validation in solid electrolyte context"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    section: "Summary; Methods; Findings"
    note: "Carbonate electrolyte decomposition, Li+/Li0 separation, and DFT-referenced reaction energetics"
  - paper_id: "paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism"
    section: "Summary; Methods; Findings"
    note: "Experiment-coupled interface degradation interpretation for Si/SEI systems"
aliases:
  - "battery interface reactive md workflow"
  - "electrolyte interface reactivity protocol"
related_ids:
  - "concept:batteries-interfaces-reaxff"
  - "methodprotocol:reaxff-parameterization-workflow"
  - "debate:transferability-reactive-ff"
  - "debate:reaxff-vs-mlip-accuracy"
applies_to:
  - "concept:batteries-interfaces-reaxff"
  - "forcefield:reaxff-family"
evaluates:
  - "reaction-barrier-consistency-vs-dft"
  - "solvation-structure-consistency"
  - "interface-morphology-trend-consistency"
---

<!-- id:methodprotocol:battery-interface-reactivity-workflow -->

!!! abstract "For readers"

    This protocol is an execution checklist for battery interface reactivity studies that use ReaxFF as the production model while keeping key decisions anchored to DFT-derived references and corpus-grounded validation patterns. It is designed for electrolyte decomposition, interphase chemistry, and interface morphology questions where transferability limits must be made explicit.

## Summary

This workflow stages battery-interface modeling into four gates: scope definition, DFT-anchored reference selection, reactive production simulation, and acceptance testing against chemistry-aware observables. In this corpus, the central pattern is to use DFT to constrain training or benchmark targets, then evaluate whether ReaxFF recovers the right qualitative and semi-quantitative trends for the specific interface regime (solid electrolyte transport, liquid-electrolyte decomposition, or coupled interface degradation). The protocol treats cross-domain transfer as a hypothesis that must be tested, not assumed.

## Inputs and prerequisites

- A defined interface question with boundaries (for example, LATP transport window, carbonate reduction near Li, or Si/SEI delithiation-driven morphology change).
- A parameter set and element scope that already include the target chemistry or can be explicitly extended.
- Reference dataset plan from DFT and/or published DFT-backed quantities relevant to the target mechanisms (barriers, solvation energetics, structural trends).
- Simulation engine support for reactive MD and the selected workflow controls (ensemble, timestep, sampling windows, and any reduction-state handling strategy).
- A validation matrix that distinguishes primary claims (must pass) from exploratory claims (may be provisional).

## Procedure

1. Define the intended inference boundary before setup.
   - State what this campaign will claim (for example, pathway plausibility, trend direction, or rank ordering) and what it will not claim (absolute lifetime predictions, universal transferability).
   - Classify target regime as solid-electrolyte transport, liquid-electrolyte decomposition, or mixed interface degradation.

2. Map chemistry coverage to parameter scope.
   - List required elements, charge-state behavior expectations, and key reactive motifs.
   - If a required motif is outside prior training scope, mark as extension-required before production runs.

3. Build DFT-grounded acceptance targets.
   - Select a compact set of reference quantities directly tied to the intended claim: representative reaction barriers, solvation motifs, formation or structural energies, and local coordination trends.
   - Record comparison tolerance as trend-level, rank-level, or value-level to avoid post-hoc metric drift.

4. Configure initial reactive simulations for stability and realism.
   - Run short sanity trajectories to detect unphysical bond cascades, charge pathologies, or unstable thermodynamic behavior.
   - Verify that the selected ensemble, timestep, and temperature window support the targeted interface process.

5. Execute mechanism-focused production sampling.
   - For decomposition studies, capture state transitions and local environment descriptors that affect barriers (for example, coordination-dependent behavior).
   - For solid-interface transport studies, include composition or structural realizations needed to test trend sensitivity.
   - For degradation studies, track morphology-linked descriptors that can be compared against experimental narratives when available.

6. Perform ReaxFF-vs-DFT and cross-evidence checks.
   - Compare targeted ReaxFF observables against the selected DFT-grounded references.
   - Where available, check consistency with independent experiment-linked trends (for example, conductivity order, morphology directionality, or interphase behavior).
   - Escalate any contradiction from "minor mismatch" to "model-scope failure" when it changes mechanistic conclusions.

7. Publish scope-qualified conclusions.
   - Separate robust findings from hypothesis-level observations.
   - Document transfer boundaries and unresolved failure points in the same page/report as the results.

## Validation checks and acceptance criteria

- DFT-consistency check passes for the pre-declared reference set at the chosen tolerance level (trend, ranking, or value).
- No persistent unphysical reaction channel dominates production trajectories in the target window.
- Claimed mechanism is supported by at least two independent evidence dimensions (for example, reactive trajectory behavior plus DFT benchmark trend, or trajectory trend plus experiment-coupled observation).
- Sensitivity analysis across key setup levers (composition, local solvation state, or cycle stage) does not invert the headline conclusion unless explicitly reported.
- Final claim language is scoped to the validated chemistry and phase window.

## Failure modes and mitigations

- Missing chemistry in training scope -> add targeted DFT references and re-fit or restrict claim scope to observed-valid regions.
- Over-interpreting decomposition pathways from short or unstable trajectories -> add staged equilibration, replicate trajectories, and environment-conditioned analysis.
- Treating one successful regime as proof of broad transferability -> require explicit out-of-domain holdout checks before reuse.
- Confusing pathway discovery with predictive ranking -> separate plausibility claims from rate/selectivity claims unless validated against stronger references.
- Ignoring interface morphology evidence in degradation studies -> include experiment-linked descriptors when corpus anchors provide them.

## Variants and when to choose them

- Solid electrolyte transport variant: use when the objective is composition- and disorder-sensitive ion-transport trends in ceramic frameworks.
- Liquid electrolyte decomposition variant: use when Li speciation and local solvation structure control reduction/decomposition pathways.
- Coupled experiment-simulation degradation variant: use when interface morphology evolution is central and microscopy or analogous observations are available.
- Method-escalation variant (ReaxFF -> higher-fidelity refinement): use when key acceptance checks fail but trajectory-level mechanism hypotheses remain valuable for narrowing a DFT follow-up set.

## Outputs and downstream links

- A scoped protocol record containing setup decisions, declared acceptance criteria, and pass/fail outcomes.
- Mechanism notes tagged by confidence tier (robust, provisional, rejected) with explicit transfer boundaries.
- A validation table mapping each major claim to its DFT and/or experiment-linked evidence anchor.
- Suggested follow-up routes:
  - [[batteries-interfaces-reaxff]]
  - [[reaxff-parameterization-workflow]]
  - [[transferability-reactive-ff]]
  - [[reaxff-vs-mlip-accuracy]]

## Evidence anchors

- [[2018shin-physical-che-development-reaxff]] (`paper:2018shin-physical-che-development-reaxff`) for DFT-trained ReaxFF in LATP and composition-sensitive validation logic.
- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] (`paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation`) for electrolyte decomposition workflow decisions tied to DFT references and Li-speciation-aware chemistry.
- [[2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism]] (`paper:2025carl-erik-l-foss-j-phys-chem-revisiting-mechanism`) for interface degradation interpretation with experiment-coupled reactive modeling constraints.
