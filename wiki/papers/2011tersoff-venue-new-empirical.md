---
id: paper:2011tersoff-venue-new-empirical
type: paper
title: "New empirical approach for the structure and energy of covalent systems"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:classical-ff-specialized
  - method:classical-md
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.37.6991"
year: 1988
authors:
  - "J. Tersoff"
venue: "Physical Review B 37, 6991–7005 (1988)"
pdf_sha256: "32789f2dff1b3f231599b28418ed698af5582aac602251fe034537e7a7c910e0"
pdf_path: "papers/Others/Tersoff_PhysRevB.37.6991.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011tersoff-venue-new-empirical -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This paper introduces **empirical interatomic potentials** for **covalent** materials in which **bond order depends on local coordination environment**—weaker bonds when an atom is **over-coordinated**, enabling open structures versus close-packed defaults of pair potentials. A detailed **silicon** potential illustrates the approach: it targets **multiple polymorphs** with **similar cohesive energies**—a known challenge—and reports extensive **tests** of structures, energetics, and suitability for **molecular dynamics**. The discussion is explicit about **limitations** of the early silicon parameterization.

## Methods

### 1 — MD application (atomistic dynamics)

The article motivates potentials that are sufficiently **global** to be used in **molecular-dynamics simulations** of **silicon** beyond small harmonic distortions (abstract/Introduction, `normalized/extracts/2011tersoff-venue-new-empirical_p1-2.txt`).

- **Engine / code:** **Classical molecular dynamics** is explicitly named as a target use case; **N/A —** no MD program is named on the indexed excerpt pages.
- **System size & composition:** **Silicon** is the primary parameterized element in the excerpted introduction; **N/A —** supercell sizes for any illustrative MD are not stated on pp. 1–2.
- **Boundaries / periodicity:** **N/A —** not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat / temperature / pressure:** **N/A —** **NVT**/**NPT**/**NVE** production protocols, timestep sizes, trajectory segment lengths, thermostat/barostat algorithms, bath **temperature** schedules, and **pressure** control are not stated on the indexed excerpt pages.
- **Electric field:** **N/A —** not stated on the indexed excerpt pages.
- **Replica / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

### 2 — Force-field training

- **Parent FF / elements:** A new **empirical bond-order-dependent** potential form for **covalent** systems; the excerpt emphasizes **two-body + bond-order modulation** rather than fixed harmonic expansions about one ground-state geometry (Introduction, extract).
- **QM reference:** **N/A —** the pp. 1–2 excerpt focuses on empirical motivation; any **ab initio** benchmarks used in fitting are not summarized on these pages—verify **`pdf_path`**.
- **Training set / reference data:** The excerpt frames the **silicon** parameterization challenge around **many polymorphs** with **similar cohesive energies** (abstract/Introduction, extract).
- **Optimization:** **N/A —** numerical optimizer / objective-function details are not stated on the indexed excerpt pages—verify **`pdf_path`**.
- **Reference data used:** The excerpt contrasts empirical potentials with **quantum-mechanical calculations** as a competing route for energies/structures, but does not enumerate the paper’s fitted databases on pp. 1–2—verify **`pdf_path`**.

### 3 — Static QM / DFT-only

**N/A —** this is an **empirical potential** methods paper, not a DFT application paper.

## Findings

The **bond-order** construction stabilizes **low-coordination** covalent motifs characteristic of **semiconductors** (e.g., **tetrahedral** silicon) where pairwise models favor dense packing. The fitted **silicon** potential is reported to capture a wide range of **structural and energetic** tests in the paper (with explicit discussion of **limitations** in **Section VI** of the original article), representing a substantial improvement in **transferability** versus earlier empirical silicon models of its era for **MD**-scale simulations.

Historically, this paper is a direct ancestor of **Brenner**-type refinements and later **reactive** frameworks: the key move is to let **effective bond strength** depend on **environment**, not on fixed harmonic springs.

## Limitations

The model remains **empirical** and can fail outside the classes of configurations used in fitting; later **Tersoff** revisions and reactive frameworks such as **ReaxFF** target broader chemistry spaces than this early silicon-focused potential.
- Catalog metadata in `normalized/papers/` misstates the calendar year; this file uses the **journal** year **1988**.

## Relevance to group

Foundational **bond-order empirical potential** preceding **Brenner/ReaxFF** lines that saturate the corpus.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.37.6991](https://doi.org/10.1103/PhysRevB.37.6991)
- Text-aligned pointer: `normalized/extracts/2011tersoff-venue-new-empirical_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Empirical bond-order models (Tersoff, Brenner, ReaxFF lineage)
