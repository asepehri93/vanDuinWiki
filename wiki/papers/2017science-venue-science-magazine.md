---
id: paper:2017science-venue-science-magazine
type: paper
title: "A conundrum for density functional theory"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:review-or-perspective
candidate_tags: []
source_refs: []
doi: "10.1126/science.aal3442"
year: 2017
authors:
  - "Sharon Hammes-Schiffer"
venue: "Science 355 (6320), 28–29 (2017)"
pdf_sha256: "d27e30e85307577d375882d25c5d56e7d5101a4c9bbf70ef1d5f41dfa8ecd2d1"
pdf_path: "papers/Others/Hammes-Schiffer - 2017 - A conundrum for density functional theory.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017science-venue-science-magazine -->

Hammes-Schiffer’s Science perspective discusses how modern density functionals can lower energy errors while degrading electron densities relative to exact references, with implications for what DFT-based training data actually encodes.

## Summary

This **Science** perspective comments on Medvedev *et al.* (same issue) showing that **recent density functionals** can improve **energies** while **electron densities** move away from exact references—a tension with textbook expectations from Jacob’s ladder. The piece discusses when density errors matter for chemistry versus when **energies and structures** remain the practical focus. Readers pairing this perspective with force-field development should treat it as a caution about single-objective fitting: improving total energies alone does not guarantee improved charge densities or related observables used in electrostatic or polarizable models.

## Methods

This page is a **Science Perspective** (`task:review`). **Methods** therefore means **literature scope** and **argument structure**, not a single reproducible simulation pipeline.

Hammes-Schiffer situates **modern density-functional approximations** on **Jacob’s ladder**, recounting how historically both **total energies** and **electron densities** tended to improve together until roughly **2000**, then contrasts that history with **Medvedev *et al.*** in the same issue (**[[2017medvedev-venue-science-journals]]**; DOI `10.1126/science.aah5975`), who show that many **highly parameterized functionals** continue to lower **energy errors** while **densities** can move **away** from exact references. The perspective explains **why** this is permissible in principle—the **exact functional** yields the **exact energy** only at the **exact density**, so improved energies evaluated at **approximate densities** need not imply uniformly improved **density-driven observables**—and discusses when **density-sensitive** chemistry (vs **valence-region energetics**) should dominate functional choice.

**MD / sampling studies:** **Not applicable** as new work here—the text cites the broader **MD / Monte Carlo** ecosystem only as context for how practitioners consume **DFT** data.

**Force-field training:** **Not applicable**—the focus is **XC functional** development philosophy, not classical **FF** fitting.

**New DFT benchmarks:** **None** are introduced beyond commentary on the paired **Science** research article; for numerical **density**/**energy** comparisons, follow **Medvedev *et al.*** and its **SI** rather than this perspective alone.

## Findings

Historically, climbing **Jacob’s ladder** improved **both** energies and densities until roughly 2000; afterward many **highly parameterized** functionals continue to lower energy errors while **densities can worsen**. Possible explanations include fitting to energies and geometries without weighting **density-sensitive observables**. The exact functional must reproduce the **exact energy only for the exact density**, not for approximate densities—so improved energies on imperfect densities need not imply a better approximation to the universal functional. The commentary notes that for many chemical questions, **valence-region behavior** and **relative energies** dominate practical conclusions, so the import of density degradation depends on **where** errors accumulate (e.g., near nuclei versus chemically active regions). The perspective therefore recommends judging functional quality against the observables relevant to a specific modeling task rather than a single energy metric.

## Limitations

Perspective format: it does not introduce new computational benchmarks beyond discussing the paired research article.

## Relevance to group

Frames **DFT quality** debates that underpin **QM training data** for force fields (ReaxFF, MLIPs) and cautions against assuming monotonic improvement of all properties when a single score (energy) is optimized.

## Citations and evidence anchors

- DOI: [10.1126/science.aal3442](https://doi.org/10.1126/science.aal3442)
- Companion analysis: Medvedev *et al.*, *Science* **355**, 49–52 (2017), DOI [10.1126/science.aah5975](https://doi.org/10.1126/science.aah5975).

## Related topics

- [[reaxff-family]]
- QM benchmarks and force-field training-data quality

## Reader notes (navigation)

- Pairs with **[[2017medvedev-venue-science-journals]]** for the quantitative **DFT density** analysis referenced throughout the perspective.
