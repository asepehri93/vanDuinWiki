---
id: debate:reaxff-vs-mlip-accuracy
type: debate
title: "When to prefer ReaxFF versus machine-learned interatomic potentials"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:ml-atomistic, domain:reaxff-lineage, task:review]
candidate_tags: []
source_refs:
  - paper_id: "paper:2023musaelian-nat-learning-local"
    note: "Equivariant MLIPs; local accuracy vs data cost"
  - paper_id: "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
    note: "Differentiable ReaxFF — hybrid angle"
positions:
  - name: "ReaxFF for broad chemistry"
    summary: "A validated reactive FF can cover diverse bond-breaking events in one MD engine without per-configuration neural evaluation design."
  - name: "MLIPs for targeted accuracy"
    summary: "Neural potentials can match DFT more tightly on a defined configuration manifold if training data are sufficient."
evidence:
  - paper_id: "paper:2023musaelian-nat-learning-local"
    note: "supports MLIP accuracy narrative with data/engineering costs"
  - paper_id: "paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based"
    note: "bridges classical reactive forms with modern autodiff tooling"
---

<!-- id:debate:reaxff-vs-mlip-accuracy -->

!!! abstract "TL;DR"

    **ReaxFF** and **MLIPs** answer different **cost / accuracy / coverage** trade-offs. The corpus includes both **large-scale reactive** studies with ReaxFF and **state-of-the-art ML** papers; this page frames the tension without declaring a single winner.

## Positions

**ReaxFF for broad chemistry:** one **parameter file** (per training effort) can run **long** trajectories across **many** reaction channels if those channels were in the **QM training**.

**MLIPs for targeted accuracy:** when **DFT-quality** energies are needed on a **narrow** phase space, equivariant networks can win—at the price of **data curation** and **out-of-domain** risk.

## Evidence summary

- [[2023musaelian-nat-learning-local]], [[2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based]] — see [[theme-ml-atomistic-potentials]].  
- Broad reactive coverage narrative: [[reaxff-family]], [[2016npjcompumats201511-venue-untitled]].

## Open questions

**Hybrid workflows** (e.g., ML region + FF region) are not uniformly documented—add `methodprotocol` pages when a reproducible recipe exists.

## Key references

See `source_refs` and [[papers/index.md](../papers/index.md)].
