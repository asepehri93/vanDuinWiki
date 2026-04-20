---
id: paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based
type: paper
title: "JAX-ReaxFF: A Gradient-Based Framework for Fast Optimization of Reactive Force Fields"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:methods-software
  - domain:ml-atomistic
  - method:reaxff
  - task:method-development
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.2c00363"
year: 2022
authors:
  - "Mehmet Cagri Kaymak"
  - "Ali Rahnamoun"
  - "Kurt A. O’Hearn"
  - "Adri C. T. van Duin"
  - "Kenneth M. Merz Jr."
  - "Hasan Metin Aktulga"
venue: "J. Chem. Theory Comput. 18, 5181–5194 (2022)"
pdf_sha256: "b88485f0e074898eed5df2acca339046a27e660593fe7cfdae585048954813e9"
pdf_path: "papers/Kaymak_JAX_JCTC_2022.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based -->

## One-paragraph summary

**JAX-ReaxFF** replaces slow, heavily stochastic ReaxFF parameter searches (genetic algorithms / Monte Carlo style workflows that can require millions of error evaluations) with **differentiable loss landscapes**: gradients of the training objective are computed via **JAX**, enabling **local optimizers** launched from **multiple initial guesses** in high-dimensional parameter space. The implementation targets **CPU/GPU/TPU** execution and reports dramatic wall-clock reductions for complex fits—positioned as enabling rapid iteration when both **training data** and **functional forms** must be refined jointly. The paper also frames the stack as a **sandbox** to explore ReaxFF functional customization guided by fast, gradient-based search.

## Methods

Derivation/implementation of differentiable ReaxFF error metrics; JAX-based autodiff; multi-start local optimization; benchmarking vs traditional genetic/Monte Carlo fitting approaches; hardware portability discussion (JAX ecosystem).

## Findings

Gradient-driven optimization plus accelerators reduces representative optimization runtimes from **days to minutes** in cases highlighted; multi-start strategy mitigates nonconvexity; framework supports exploratory modifications to the reactive FF formulation when paired with rapid re-optimization.

## Limitations

Quality still depends on **training set curation** and physics of the ReaxFF model class; global optimality is not guaranteed—multi-start mitigates but does not remove ruggedness of parameter spaces.

## Relevance to group

Core **infrastructure** paper for **PSU/MSU collaborators** on **accelerated ReaxFF development**, directly supporting the group’s large parameterization agenda.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jctc.2c00363 — Abstract (~p. 1) states goals and performance claims; later sections document methodology and benchmarks.

## Related topics

- [[reaxff-family]]
- [[2021itai-leven-j-chem-theor-recent-advances]]
