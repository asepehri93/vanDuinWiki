---
id: concept:theme-ml-atomistic-potentials
type: concept
title: "Theme: machine-learned interatomic potentials and hybrid workflows"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:methods-software
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2023musaelian-nat-learning-local"
    note: "Learning local equivariant representations; MLIP"
  - paper_id: "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
    note: "JAX differentiable ReaxFF"
  - paper_id: "paper:2016npjcompumats201511-venue-untitled"
    note: "NPJ Computational Materials survey / ML context"
supported_by:
  - "paper:2023musaelian-nat-learning-local"
  - "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
  - "paper:2016npjcompumats201511-venue-untitled"
---

<!-- id:concept:theme-ml-atomistic-potentials -->

!!! abstract "TL;DR"

    This cluster collects **neural and differentiable** approaches that sit **alongside classical ReaxFF**: **Allegro**-style equivariant models, **JAX**-based **automatic differentiation** for reactive FF, and **survey** material on **computational materials** workflows. It answers “where does the KB discuss **MLIPs**?” without conflating them with a single ReaxFF parameter file.

## Scope

**In:** papers whose primary contribution is **ML interatomic potentials**, **differentiable simulation stacks**, or **data infrastructure** for atomistic ML—when present in `wiki/papers/`.

**Relation to ReaxFF:** many papers **compare** or **hybridize** with reactive FF; see [[reaxff-family]] for the classical line.

## Representative papers

- **Equivariant / local learning:** [[2023musaelian-nat-learning-local]] — **ML1** gold.  
- **JAX + ReaxFF gradients:** [[2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based]] — **ML1** gold.  
- **NPJ / ecosystem:** [[2016npjcompumats201511-venue-untitled]] — **ML1** and **X1** cross-refs.  
- **Additional ML / data papers:** [[2023li-venue-paper]].

## Methods and limitations

**Data efficiency** and **out-of-distribution** chemistry remain central limitations; papers typically disclose **training sets** and **error metrics** relative to **DFT**. Reactive **long-time** kinetics are not always targeted.

## Related

- [[reaxff-vs-mlip-accuracy]]  
- [[reaxff-family]]  

??? info "Maintainers"

    Keep aligned with frozen eval **ML1**; update `source_refs` when new ML papers are ingested.
