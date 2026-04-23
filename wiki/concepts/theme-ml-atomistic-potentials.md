---
id: concept:theme-ml-atomistic-potentials
type: concept
title: "Theme: machine learning atomistic potentials (corpus touchpoints)"
updated: "2026-04-21"
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

    This cluster tracks **MLIPs** and **NN potentials** where they appear in the corpus, mainly as **modern comparators** or **elastic-property** workflows for **oxides**. Most KB depth remains **ReaxFF-first**; use [[reaxff-vs-mlip-accuracy]] for the debate framing.

## Scope (in / out)

**In corpus:** papers tagged `domain:ml-atomistic` (currently **sparse** in the KB compared to ReaxFF coverage).

**Out of scope:** generic ML literature without **atomistic** potential content present in a wiki page.

## Literature review (this knowledge base)

This is intentionally **short** because the KB’s **primary** methodological spine is **ReaxFF parameterization and application**. ML content appears where authors **deploy** or **compare** neural potentials.

### Neural network potentials and elastic / thermal properties

[[2024baksa-adv-elect-ma-strain-fluctuations]] documents **strain-fluctuation** elastic constants with a **neural network potential** for **BaZrO₃** (see the paper page for **method** detail and **validation**). This is the KB’s clearest **MLIP application** note in the oxide space at time of writing.

### High-temperature oxides and methodological adjacency

[[2025krstic-venue-paper]] is tagged `domain:ml-atomistic` in the corpus index; read the paper note for whether **ML** is central or **peripheral** to the main result—**the page text is authoritative**.

### Baselines: ReaxFF development papers as comparison anchors

When contrasting **MLIPs** to **reactive classical** models, the KB’s **development** narratives on [[2018shin-physical-che-development-reaxff]], [[2015lloyd-surface-scie-development-reaxff]], and the overview [[reaxff-family]] supply **what ReaxFF optimizes for** (bond-order, training sets, transferability limits).

## Analysis and cross-cutting patterns

The KB’s **ML atomistic** coverage is **thin** relative to ReaxFF; where **NN potentials** appear, **training-set scope** and **validation** details on the paper page are the primary guardrails—avoid hub-level generalization beyond cited notes.

## Gaps and open directions (corpus view)

**Equivariant** and **Allegro-class** workflows are not uniformly represented—track `domain:ml-atomistic` in [[paper-index-by-domain]] and expand this hub as new notes land.

## Debates, tensions, and cross-references

- **Accuracy vs data cost:** [[reaxff-vs-mlip-accuracy]].  
- **Transferability:** [[transferability-reactive-ff]] (ReaxFF-focused but conceptually parallel).  
- **Oxide mechanics / ferroelectrics:** [[theme-ferroelectrics-polar-oxides]], [[theme-oxides-silica-ceramics]].

## Representative entry points

- **NN potential + elastic properties:** [[2024baksa-adv-elect-ma-strain-fluctuations]].  
- **Tagged ML-atomistic papers:** [[paper-index-by-domain]] (`domain:ml-atomistic`).  
- **ReaxFF baseline:** [[reaxff-family]].

## Methods and limitations

**MLIPs** require **careful** domain-of-validity documentation; the KB pages should be read for **training set** scope. **ReaxFF** remains better represented for **reactive** pathways in this corpus.

??? info "MAS / retrieval"

    **id:** `concept:theme-ml-atomistic-potentials`. Expand `source_refs` as new `domain:ml-atomistic` pages are added; keep this hub **honest** about corpus sparsity.
