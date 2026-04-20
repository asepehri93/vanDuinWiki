---
id: paper:2015aktulga-venue-paper
type: paper
title: "Optimizing the performance of reactive molecular dynamics simulations for multi-core architectures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:software
  - task:method-development
  - scale:atomistic
source_refs: []
doi: null
year: 2015
authors:
  - "Hasan Metin Aktulga"
  - "Chris Knight"
  - "Paul Coffman"
  - "Tzu-Ray Shan"
  - "Wei Jiang"
venue: "MSU / ALCF technical report MSU-CSE-15-16 (PDF in corpus)"
pdf_sha256: "b758618f9cac9decc1e98b4acd3492852bed3bbe071d00597a730c5bc2bf6432"
pdf_path: "papers/Aktulga_MSU-CSE-15-16.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2015aktulga-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Aktulga *et al.* describe **hybrid MPI/OpenMP** optimizations for **LAMMPS/ReaxC**, focusing on accelerating **bonded/nonbonded list builds** and **ReaxFF interaction evaluation** on modern **multi-core** nodes. They also examine **QEq charge equilibration** performance and introduce a **dual-solver** strategy. Benchmarks on **IBM BlueGene/Q (Mira)** report **~1.5–4.5×** speedups for systems from **tens of thousands** to **millions of particles**, with sustained improvements up to **262,144 cores (1,048,576 processes)** and **~91.5%** weak-scaling efficiency quoted for their largest **16.6M-particle** case.

## Methods

- **OpenMP** parallelization of hot loops in **ReaxC** tied to LAMMPS integration.
- **Performance engineering** study on BG/Q including QEq solver variants.

## Findings

- Thread-level parallelism recovers on-node performance lost to **MPI-only** decompositions at moderate core counts.
- Large-scale reactive MD campaigns become more feasible when list builds and QEq are not serial bottlenecks.

## Limitations

- Hardware-specific tuning on **BG/Q** may not transfer directly to contemporary GPU-centric clusters without re-benchmarking.
- Extract is the abstract/introduction chunk; detailed scaling plots require the remainder of the PDF.

## Relevance to group

Although van Duin is not an author, **Tzu-Ray Shan** appears on the author list, linking the report to collaborators closely tied to **ReaxFF** application workloads that motivated throughput improvements.

## Citations and evidence anchors

- No DOI in extract; cite the **PDF path** and institutional report identifier recorded in the manifest.

## Related topics

- [[reaxff-family]]
