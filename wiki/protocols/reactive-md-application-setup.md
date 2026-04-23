---
id: methodprotocol:reactive-md-application-setup
type: methodprotocol
title: "Reactive MD application setup using published force fields"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs:
  - paper_id: "paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale"
    note: "Large-scale ReaxFF application trajectories at high temperature"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Reactive oxidation trajectory behavior and transport interpretation"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Surface reaction trajectories and catalyst-context setup choices"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Electrolyte-focused validation expectations for reactive trajectories"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    note: "Species tracking and pathway interpretation in reactive electrolyte MD"
  - paper_id: "paper:2021verma-physical-che-reaxff-reactive"
    note: "Defect/water reactive trajectories and environment sensitivity"
  - paper_id: "paper:2022nayir-carbon-190-2-atomic-scale-probing"
    note: "Defect-mediated intercalation application workflow and checks"
aliases:
  - "reactive-md-deployment-checklist"
  - "reaxff-application-setup"
related_ids:
  - "concept:theme-reactive-md-corpus"
  - "forcefield:reaxff-family"
  - "methodprotocol:reaxff-parameterization-workflow"
  - "debate:transferability-reactive-ff"
applies_to:
  - "forcefield:reaxff-family"
evaluates:
  - "trajectory stability under intended thermodynamic conditions"
  - "reaction-network plausibility against paper-scoped expectations"
  - "species and product trends under parameter sweeps"
---

<!-- id:methodprotocol:reactive-md-application-setup -->

!!! abstract "For readers"

    This protocol covers practical setup and use of already-published reactive force fields for production application trajectories. It is for deployment and interpretation, not new parameter fitting; route fitting tasks to [[protocols/reaxff-parameterization-workflow]].

## Summary

This workflow helps operators run reactive MD in a way that is reproducible, scoped to known force-field validity, and auditable before conclusions are reported. The core idea is to front-load sanity checks, enforce explicit validation gates, and only then scale to long trajectories and interpretation.

In this corpus, successful application studies repeatedly pair (i) chemistry/scope declarations, (ii) short pre-production checks for numerical and chemical stability, and (iii) paper-grounded interpretation rules for products, intermediates, and trends. That pattern appears across high-temperature pyrolysis, oxidation/surface chemistry, electrolyte decomposition, and defect-mediated intercalation contexts.

## Inputs and prerequisites

- A published reactive FF parameter file with documented element coverage and known intended chemistry domain (for example, contexts represented in [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]], [[2014zou-acta-materia-molecular-dynamics]], [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]).
- MD engine support for the selected reactive FF and charge equilibration workflow (engine/version and relevant pair style settings recorded in run metadata).
- Initial structures consistent with target phase, density, defect state, and composition; no impossible overlaps or unsupported atom types.
- A reaction/species analysis plan defined before production (what species, bonds, events, and observables are required to claim success).
- A paper-grounded acceptance matrix tying each planned claim to at least one corpus anchor in `source_refs`.

## Procedure

1. **Declare applicability boundary.**  
   Record what chemistry the chosen FF is expected to represent, plus explicit "do not interpret" zones (for example, extreme oxidation state or composition regimes not covered in source studies).
2. **Preflight topology and typing.**  
   Validate atom typing, stoichiometry, boundary conditions, and initial geometry quality; fail fast if unsupported species or unrealistic close contacts appear.
3. **Run micro-sanity trajectories.**  
   Execute short trajectories at target and bracket temperatures to verify stable integration, charge convergence behavior, and absence of immediate unphysical fragmentation/polymerization.
4. **Calibrate control parameters.**  
   Tune timestep and thermostat/barostat coupling for stable yet physically interpretable dynamics; keep settings fixed once accepted for production.
5. **Define observables before scaling.**  
   Lock analysis scripts/criteria for species tracking, bond-event counting, diffusion/reaction proxies, and trajectory quality diagnostics.
6. **Execute staged production.**  
   Use staged runs (equilibration then production windows) with checkpointing and reproducible seeds; log all environment and input hashes.
7. **Apply validation gates after each stage.**  
   Continue only if all validation gates pass (below). If any gate fails, stop, classify failure mode, and revise setup rather than extending runtime.
8. **Interpret with scope discipline.**  
   Report only trends/mechanisms supported by passed gates and corpus-consistent behavior; flag extrapolative claims as hypotheses.

## Validation checks and acceptance criteria

- **Gate 1 - Numerical stability:** no runaway temperature/pressure behavior beyond expected fluctuations for the chosen ensemble, and no persistent integration instability across replicate seeds.
- **Gate 2 - Charge-equilibration health:** charge solution converges reliably with no repeated solver failures; large oscillatory charge artifacts trigger rejection.
- **Gate 3 - Chemical plausibility baseline:** early-time chemistry is qualitatively consistent with expected regime from relevant corpus papers (for example, no dominant impossible products in the first analysis window).
- **Gate 4 - Replicate consistency:** key trend directions (major species evolution, relative pathway ranking, or interfacial reactivity ordering) are stable across independent replicas.
- **Gate 5 - Sensitivity sanity:** modest perturbations (temperature window, timestep sanity adjustment, initial velocity seed) do not invert central conclusions.
- **Gate 6 - Claim-to-evidence traceability:** every reported mechanistic statement is tied to observable definitions and at least one source-backed comparator from `source_refs`.

A run is **accepted for interpretation** only when all six gates pass and all deviations are documented.

## Failure modes and mitigations

- **Unphysical early chemistry (explosive decomposition or inert deadlock):** reduce timestep, re-check initial geometry/typing, and verify chemistry lies inside known FF scope before retrying.
- **Charge solver instability or extreme charge swings:** tighten solver tolerances if available, inspect problematic local motifs, and test whether artifacts persist across minimized/pre-equilibrated starting states.
- **Replica divergence dominated by rare events with no stable trend:** increase replica count and report distributional outcomes rather than a single exemplar trajectory.
- **Product network dominated by species absent from paper-grounded expectations:** pause interpretation; treat as potential out-of-domain behavior unless independently validated by higher-level evidence.
- **Boundary/finite-size artifacts (surface systems, defects, confined phases):** test larger cells or alternative boundary setups before assigning mechanism-level conclusions.
- **Over-interpretation of accelerated/high-T trajectories:** explicitly separate "pathway accessibility under simulated conditions" from real-world rate claims unless validated against external evidence.

## Variants and when to choose them

- **Bulk pyrolysis / combustion variant:** prioritize high-temperature stability gates, robust species-network extraction, and multiple-seed statistics (aligned with corpus use cases like [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] and [[2018jain-j-phys-chem-understanding-combustion]]).
- **Surface reaction / oxidation variant:** include slab-specific boundary checks, adsorption-state initialization controls, and depth-resolved reaction/transport diagnostics (as in [[2014zou-acta-materia-molecular-dynamics]], [[2015broqvist-venue-jp5b01597]]).
- **Electrolyte/interface variant:** emphasize ion speciation accounting and solvent-fragment bookkeeping with strict replicate comparison (see [[2018shin-physical-che-development-reaxff]], [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]).
- **Defect-mediated 2D/materials variant:** require defect-state provenance, local environment sensitivity tests, and mechanism claims tied to defect class (see [[2021verma-physical-che-reaxff-reactive]], [[2022nayir-carbon-190-2-atomic-scale-probing]]).

## Outputs and downstream links

- Reproducible simulation package: input decks, FF file identity, runtime metadata, random seeds, and checkpoint lineage.
- Validation dossier documenting pass/fail status for each gate, plus mitigation notes for any failed attempts.
- Analysis bundle: species/bond-event outputs, trend summaries, and uncertainty/replicate spread metrics.
- Interpretation notes mapped to evidence anchors for use in paper pages, theme hubs, and debate pages.
- Recommended downstream pages:
  - [[theme-reactive-md-corpus]]
  - [[reaxff-family]]
  - [[transferability-reactive-ff]]
  - [[protocols/reaxff-parameterization-workflow]]

## Evidence anchors

- [[2014castro-marcano-journal-of-a-pyrolysis-large-scale]] - large-scale reactive trajectory deployment in high-temperature organic chemistry.
- [[2014zou-acta-materia-molecular-dynamics]] - reactive oxidation and transport interpretation constraints in a materials context.
- [[2015broqvist-venue-jp5b01597]] - catalytic/surface reaction application framing for reactive trajectories.
- [[2018shin-physical-che-development-reaxff]] - electrolyte-focused setup and validation expectations for reactive applications.
- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]] - practical species-tracking and interpretation boundaries in electrolyte decomposition studies.
- [[2021verma-physical-che-reaxff-reactive]] - defect and environment sensitivity issues in reactive 2D/water trajectories.
- [[2022nayir-carbon-190-2-atomic-scale-probing]] - defect-mediated intercalation application workflow with mechanism-scope caveats.
