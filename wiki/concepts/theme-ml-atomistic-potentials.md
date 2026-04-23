---
id: concept:theme-ml-atomistic-potentials
type: concept
title: "Theme: machine learning atomistic potentials (corpus touchpoints)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2024baksa-adv-elect-ma-strain-fluctuations"
    note: "Strain fluctuations + NN potential (perovskite)"
  - paper_id: "paper:2025krstic-venue-paper"
    note: "High-temperature oxide / potential methodology context"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "ReaxFF development (baseline comparison for MLIPs)"
  - paper_id: "paper:2015lloyd-surface-scie-development-reaxff"
    note: "Classical reactive FF development"
supported_by:
  - "paper:2024baksa-adv-elect-ma-strain-fluctuations"
  - "paper:2025krstic-venue-paper"
---

<!-- id:concept:theme-ml-atomistic-potentials -->

!!! abstract "TL;DR"

    This theme hub maps where **machine-learning atomistic potentials (MLIPs)** appear in this corpus and how to navigate them responsibly. The current corpus is still **ReaxFF-heavy**, so this page emphasizes what is actually documented in linked paper pages and where to branch into adjacent debates and protocols.

## Scope (in / out)

**In corpus:** wiki pages in this KB tagged `domain:ml-atomistic`, plus closely related comparison anchors used by those pages.

**Out of scope:** broad ML potential literature that is not represented by a curated paper page in this repository. This is a corpus hub, not a global review.

## How this theme is organized in the corpus

Use this page in three passes:

1. **Locate direct MLIP evidence** in paper pages where NN/ML potentials are explicit.
2. **Contextualize against ReaxFF baselines** to understand why model choice differs by question (reactivity vs data-driven interpolation).
3. **Route to decision pages** (debates, domain hubs, and indexes) when choosing what to read or model next.

## Literature review (this knowledge base)

This synthesis is intentionally corpus-scoped: the KB currently contains fewer MLIP-centered pages than ReaxFF pages, so the strongest evidence comes from targeted use-cases rather than broad methodological coverage.

### Neural network potentials and elastic / thermal properties

[[2024baksa-adv-elect-ma-strain-fluctuations]] is the clearest MLIP-focused entry point in the current oxide subset. Its page grounds how a neural network potential is used for strain-fluctuation elastic analysis in BaZrO3 and what validation context is reported there.

### High-temperature oxides and methodological adjacency

[[2025krstic-venue-paper]] is also tagged `domain:ml-atomistic`. In this hub, treat it as a routing node: consult the paper page directly to determine whether ML potentials are the core method or a supporting element for high-temperature oxide analysis.

### Baselines: ReaxFF development papers as comparison anchors

When comparing MLIPs to reactive classical force fields, use [[2018shin-physical-che-development-reaxff]] and [[2015lloyd-surface-scie-development-reaxff]] as corpus anchors for how ReaxFF development and validation are framed, then connect to [[reaxff-family]] for lineage-level context.

## Analysis and cross-cutting patterns

Two cross-cutting patterns are stable across the currently linked pages:

- **Evidence concentration:** explicit MLIP detail is concentrated in a small number of paper pages, so reliable interpretation depends on reading those pages directly rather than extrapolating from the hub.
- **Model-choice framing:** MLIP entries are most useful in this corpus when interpreted alongside ReaxFF baselines, especially for discussions of transferability, validation burden, and domain-of-applicability boundaries.

## Debates, tensions, and limitations

- **Accuracy vs data and maintenance cost:** route through [[reaxff-vs-mlip-accuracy]] for corpus-linked trade-off framing.
- **Transferability expectations:** use [[transferability-reactive-ff]] for related cautionary logic, noting that page is ReaxFF-centered.
- **Domain overlap with oxide themes:** cross-check with [[theme-ferroelectrics-polar-oxides]] and [[theme-oxides-silica-ceramics]] before making system-level claims.
- **Current limitation:** this hub reflects sparse MLIP coverage in the present corpus; absence here should not be interpreted as absence in the broader field.

## Gaps and open directions (corpus view)

From a corpus-maintenance perspective, major open needs are:

- More paper pages where MLIP training-set construction and validation strategy are first-class narrative elements.
- Better coverage of modern equivariant and graph-based potential families in oxide and reactive settings.
- Clearer protocol-level links from MLIP case studies to reusable decision workflows.

Track growth via [[paper-index-by-domain]] under `domain:ml-atomistic`, then refresh this hub when new grounded pages are added.

## Representative entry points

- **NN potential + elastic properties:** [[2024baksa-adv-elect-ma-strain-fluctuations]].  
- **Tagged ML-atomistic papers:** [[paper-index-by-domain]] (`domain:ml-atomistic`).  
- **ReaxFF baseline and lineage context:** [[reaxff-family]], [[2018shin-physical-che-development-reaxff]], [[2015lloyd-surface-scie-development-reaxff]].
- **Method trade-off framing:** [[reaxff-vs-mlip-accuracy]].

## Methods and limitations

For this corpus, practical reading discipline is:

- Treat each MLIP claim as local to its linked paper page unless multiple corpus sources support the same statement.
- Check training-set scope and validation notes before reusing conclusions across materials or conditions.
- Use ReaxFF pages as comparison context, not as evidence that substitutes for missing MLIP-specific details.

??? info "MAS / retrieval"

    **id:** `concept:theme-ml-atomistic-potentials`
    **routing intent:** entry hub for `domain:ml-atomistic` queries; branch to paper pages first, then to debate and ReaxFF baseline pages for trade-off reasoning.
    **query hooks:** "MLIP oxides", "neural network potential elastic constants", "ReaxFF vs MLIP transferability", "atomistic ML potential validation".
    **maintenance note:** expand `source_refs` and `supported_by` whenever new MLIP-tagged paper pages are added; keep all synthesis statements corpus-scoped.
