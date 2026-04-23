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

## Summary

Aktulga *et al.* describe **hybrid MPI/OpenMP** optimizations for **LAMMPS/ReaxC**, focusing on accelerating **bonded/nonbonded list builds** and **ReaxFF interaction evaluation** on modern **multi-core** nodes. They also examine **QEq charge equilibration** performance and introduce a **dual-solver** strategy. Benchmarks on **IBM BlueGene/Q (Mira)** report **~1.5–4.5×** speedups for systems from **tens of thousands** to **millions of particles**, with sustained improvements up to **262,144 cores (1,048,576 processes)** and **~91.5%** weak-scaling efficiency quoted for their largest **16.6M-particle** case.

## Methods

This MSU technical report (**MSU-CSE-15-16**, PDF `papers/Aktulga_MSU-CSE-15-16.pdf`) is a **software / HPC methodology** memo, not a study of a particular material with standalone reactive MD production protocols.

**Reactive MD application (science trajectories).** **N/A —** the document benchmarks performance on representative ReaxFF workloads rather than reporting new chemistry for a specific system; timestep, ensemble, thermostat, and barostat choices for those benchmark cases appear only in the report’s benchmark sections and should be copied from the PDF when needed.

**MD benchmark setups (scalability studies).** The abstract’s scaling study spans **32k–16.6M** **atoms** in **3D periodic** cells run under **NVT** control for throughput measurements on **Mira**. **Boundary conditions:** fully **periodic** bulk **supercells** without explicit free surfaces. **Pressure control:** **N/A —** the technical report excerpt used here does not isolate hydrostatic **pressure** targets separate from the **NVT** integrator configuration; consult later sections of `papers/Aktulga_MSU-CSE-15-16.pdf` for any documented stress-control experiments.

**Force-field training.** **N/A —** not addressed.

**Implementation methods (as authored).** The authors describe **hybrid MPI/OpenMP** extensions to **LAMMPS/ReaxC** (PuReMD heritage) that parallelize bonded/nonbonded list builds and complex ReaxFF interaction evaluation with OpenMP-friendly data layouts. They analyze **QEq** charge-equilibration cost and introduce a **dual-solver** strategy for that subsystem. Performance studies focus on **IBM Blue Gene/Q (“Mira”)**, reporting **~1.5–4.5×** speedups for systems spanning **32k–16.6M** particles relative to their prior implementation, sustained improvements up to **262,144 cores (1,048,576 processes)**, and **~91.5%** weak-scaling efficiency for their largest **16.6M-particle** case (abstract of `papers/Aktulga_MSU-CSE-15-16.pdf`).

## Findings

Thread-assisted **ReaxC-OMP** restores on-node throughput that pure-MPI decomposition leaves on the table at moderate core counts, while QEq algorithmic improvements reduce a historically stiff bottleneck for large reactive runs. Headline comparisons are against the authors’ earlier **LAMMPS/ReaxC** baseline on the same hardware generation, emphasizing weak scaling on BG/Q rather than cross-code competition. Performance numbers are **BG/Q-specific**; transfer to GPU-centric or fat-node clusters requires fresh profiling. The report’s abstract/introduction chunk in `normalized/extracts/2015aktulga-venue-paper_p1-2.txt` omits later figures—use the full PDF for scaling plots.

## Limitations

- Hardware-specific tuning on **BG/Q** may not transfer directly to contemporary GPU-centric clusters without re-benchmarking.
- Extract is the abstract/introduction chunk; detailed scaling plots require the remainder of the PDF.

## Relevance to group

Although van Duin is not an author, **Tzu-Ray Shan** appears on the author list, linking the report to collaborators closely tied to **ReaxFF** application workloads that motivated throughput improvements.

## Citations and evidence anchors

- No DOI in extract; cite the **PDF path** and institutional report identifier recorded in the manifest.

## Related topics

- [[reaxff-family]]
