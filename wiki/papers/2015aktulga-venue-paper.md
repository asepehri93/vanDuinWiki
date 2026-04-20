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
extraction_quality: "partial"
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

<!-- enrich-from-extract:v2 -->

- Reactive Molecular Dynamics, ReaxFF , LAMMPS-ReaxC-OMP , Multi-core architectures, Hybrid parallelism ! 1 I NTRODUCTION Molecular Dynamics (MD) simulation has become an increasingly important computa- tional tool for a range of scientiﬁc disciplines including, but certainly not limited to, chemistry, biology, and materials science.
- In order to examine the microscopic properties of atomistic systems for many nanoseconds (and possibly microseconds) and distances spanning several nanometers, it is crucial to have a computationally cheap, yet suf- ﬁciently accurate interatomic potential to facilitate the required simulations.
- Instead of resorting to computationally expensive quantum mechanical al- ternatives, which explicitly treat the electronic degrees of freedom and thereby are appropriate to model chemical reactions, one can employ simulation methods that include some degree of variable bond topology (e.g. multistate methods [4], [5]) or force ﬁelds that do not deﬁne a bonding topology.
- ReaxFF is a bond order potential that has been widely used to study chemical re- activity in a wide-range of systems.
- The PuReMD software [10], [11], [12] and the LAMMPS/ReaxC package [13], which is also based on PuReMD, provide efﬁcient, open- source implementations of the ReaxFF model that have been beneﬁcial to large commu- nities of researchers.
- The ability for a large community of researchers to efﬁciently carry out such simulations is becoming even more important as algorithms for the efﬁcient ﬁtting of ReaxFF models are made available [14], [15], [16], [17].
- In this paper, we present hybrid parallel algorithms and their implementation for ReaxFF, where the construction of bonded and nonbonded lists and evaluation of complex interactions are implemented efﬁciently with a suitable choice of data structures and using thread parallelism provided by the OpenMP library.
- Sustained performance improvements have been observed for up to 1,048,576 processes in larger simulations.
- Knight is with the Argonne Leadership Computing Facility, Argonne National Laboratory, Argonne, IL 60439.
- Coffman is with the Argonne Leadership Computing Facility, Argonne National Laboratory, Argonne, IL 60439.


## Findings

- Thread-level parallelism recovers on-node performance lost to **MPI-only** decompositions at moderate core counts.
- Large-scale reactive MD campaigns become more feasible when list builds and QEq are not serial bottlenecks.

### Additional results (article abstract)

- The goal of all such reactive methodologies and force ﬁelds is to model reactive systems at time and length scales that far surpass those currently impractical for exploration with electronic structure methods, but at the same time complementing these more accurate quantum mechanical methods.
- It is thus important to ensure that efﬁcient implementations of a method are available in order to best address challenging scientiﬁc questions and best utilize available computational resources.
- PuReMD and LAMMPS/ReaxC incorporate novel algorithms and data structures to achieve high performance in force computations while retaining a small memory footprint.
- Just like strategies to accurately and efﬁciently model a challenging problem have evolved over time, so too has the translation of algorithms from paper to software matured to make optimal use of high-performance computing (HPC) resources.
- As a result of the physical limitations of the current chip technology, we have witnessed the emergence of multi-core architectures over the past decade.
- Hybrid parallelism (typically in the form of MPI/OpenMP) allows HPC applications to better leverage the increasing on-node parallelism.
- We present detailed performance analysis of the resulting LAMMPS/ReaxC-OMP pack- age on a state-of-the-art multi-core system Mira, an IBM BlueGene/Q supercomputer.
- For system sizes ranging from 32 thousand to 16.6 million particles, speedups in the range of 1.5-4.5× are observed using the new hybrid parallel implementation.


## Limitations

- Hardware-specific tuning on **BG/Q** may not transfer directly to contemporary GPU-centric clusters without re-benchmarking.
- Extract is the abstract/introduction chunk; detailed scaling plots require the remainder of the PDF.

## Relevance to group

Although van Duin is not an author, **Tzu-Ray Shan** appears on the author list, linking the report to collaborators closely tied to **ReaxFF** application workloads that motivated throughput improvements.

## Citations and evidence anchors

- No DOI in extract; cite the **PDF path** and institutional report identifier recorded in the manifest.

## Related topics

- [[reaxff-family]]
