---
id: concept:entrypoint-reactive-md-method-selection
type: concept
title: "Entrypoint: selecting reactive MD methods (ReaxFF, MLIP, hybrid)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:ml-atomistic
  - method:reactive-md-generic
  - method:reaxff
  - method:ml-potential
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "ReaxFF development and application context for ceramic electrolytes"
  - paper_id: "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
    note: "Reactive electrolyte chemistry and Li0/Li+ distinction"
  - paper_id: "paper:2024baksa-adv-elect-ma-strain-fluctuations"
    note: "ML potential-centered atomistic workflow in oxide context"
  - paper_id: "paper:2023musaelian-nat-learning-local"
    note: "MLIP accuracy and data-scope trade-offs"
  - paper_id: "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
    note: "Differentiable ReaxFF as hybrid workflow bridge"
  - paper_id: "paper:2022nayir-carbon-190-2-atomic-scale-probing"
    note: "Reactive MD application in defect-mediated nanocarbon chemistry"
supported_by:
  - "paper:2018shin-physical-che-development-reaxff"
  - "paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation"
  - "paper:2024baksa-adv-elect-ma-strain-fluctuations"
  - "paper:2023musaelian-nat-learning-local"
  - "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
  - "paper:2022nayir-carbon-190-2-atomic-scale-probing"
---

<!-- id:concept:entrypoint-reactive-md-method-selection -->

!!! abstract "Method-selection routing hub"

    Use this page when the first question is "which reactive atomistic method should we use for this problem?" rather than "what did one specific paper show?". It routes between ReaxFF-heavy corpus evidence, emerging MLIP coverage, and practical hybrid paths, while keeping claims tied to curated paper pages.

## Scope and user intent

This entry-point answers method-selection intent for questions such as:

- Should this study start with [[reaxff-family]] or an ML potential route?
- Is the target chemistry broad and exploratory, or narrow and high-accuracy?
- Do we need a single robust workflow now, or a staged hybrid strategy?

It does not replace paper-level protocol details. Final methodological decisions should always be validated against the linked paper notes and domain hubs.

## Start-here pathways

- **If you need broad reactive chemistry coverage quickly:** start with [[theme-reactive-md-corpus]], then branch to [[reaxff-family]] and [[reaxff-parameterization-workflow]].
- **If you need localized high fidelity on a constrained configuration space:** start with [[theme-ml-atomistic-potentials]], then read [[reaxff-vs-mlip-accuracy]] for trade-off framing.
- **If your problem is battery-interface chemistry:** start with [[batteries-interfaces-reaxff]], then check transfer limits in [[transferability-reactive-ff]].
- **If your system is oxide or ceramic dominated:** route through [[theme-oxides-silica-ceramics]] and then select method depth from linked paper pages.
- **If your system is defect-driven 2D growth/intercalation:** start with [[theme-2d-epitaxy-growth]] and representative reactive papers such as [[2022nayir-carbon-190-2-atomic-scale-probing]].

## Decision levers and trade-offs

Method choice in this corpus is usually governed by five levers:

1. **Reaction-space breadth:** ReaxFF-style workflows are more common in corpus pages requiring many bond-breaking channels in one simulation campaign.
2. **Target accuracy regime:** MLIP-centered workflows are stronger when the objective is high local accuracy within a well-specified training manifold.
3. **Training-data burden and maintenance:** ML routes generally require higher upfront curation and tighter domain-of-validity checks.
4. **Transferability risk:** moving across phases or chemistries without retraining is a recurring failure mode (see [[transferability-reactive-ff]]).
5. **Workflow maturity in this KB:** reusable protocol scaffolding is currently strongest for ReaxFF-style parameterization and validation.

## Canonical starting papers

- [[2018shin-physical-che-development-reaxff]]: ReaxFF development + application framing in electrolyte-relevant oxide chemistry.
- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]: reactive electrolyte decomposition and Li speciation behavior.
- [[2022nayir-carbon-190-2-atomic-scale-probing]]: defect-mediated nanocarbon application where reactive trajectories are central.
- [[2024baksa-adv-elect-ma-strain-fluctuations]]: ML-potential-centered oxide case useful for MLIP-first routing.
- [[2023musaelian-nat-learning-local]]: anchor for MLIP accuracy/data trade-off discussions.
- [[2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based]]: bridge paper for differentiable/hybridized reactive workflows.

## Related protocols and debates

- **Protocol backbone:** [[reaxff-parameterization-workflow]].
- **Primary method trade-off debate:** [[reaxff-vs-mlip-accuracy]].
- **Transferability and scope boundaries:** [[transferability-reactive-ff]].
- **Adjacent method hubs:** [[theme-reactive-md-corpus]], [[theme-ml-atomistic-potentials]].
- **Domain-first routing hubs:** [[batteries-interfaces-reaxff]], [[theme-oxides-silica-ceramics]], [[theme-2d-epitaxy-growth]].

## Failure modes and interpretation pitfalls

- Treating one successful paper workflow as universally transferable across phases or chemistries.
- Choosing by model label alone ("MLIP" or "ReaxFF") without checking training scope in the target reaction classes.
- Interpreting sparse corpus coverage as field-wide absence, especially for newer hybrid workflows.
- Comparing outcomes across papers without checking whether timestep, ensemble, or validation criteria differ materially.
- Skipping protocol-level acceptance checks before using trajectory results for design decisions.

??? info "MAS / retrieval"

    **id:** `concept:entrypoint-reactive-md-method-selection`
    **intent:** query-first routing for reactive atomistic method selection (ReaxFF vs MLIP vs hybrid).
    **query synonyms:** "reactive MD method choice", "ReaxFF or MLIP", "hybrid reactive workflow", "transferability before simulation setup".
    **routing policy:** method-first questions start here, then branch to theme/debate/protocol pages and finally to specific paper pages for evidence details.
    **maintenance note:** update `source_refs` and `supported_by` together when adding new method-selection-relevant papers or protocol pages.
