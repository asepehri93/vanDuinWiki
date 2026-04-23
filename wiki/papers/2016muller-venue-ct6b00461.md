---
id: paper:2016muller-venue-ct6b00461
type: paper
title: "REAXFF reactive force field for disulfide mechanochemistry, fitted to multireference ab initio data"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00461"
year: 2016
authors:
  - "Julian Müller"
  - "Bernd Hartke"
venue: "J. Chem. Theory Comput. 2016, 12, 3913-3925"
pdf_sha256: "2839d4ce2e7b7e50cb12a6164fbb7b4fe24f3a887bc5ca866884e0808d432d38"
pdf_path: "papers/ReaxFF_others/Muller_Hartke_JCTC_disulfide_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016muller-venue-ct6b00461 -->

!!! note "Authority of statements"

    Prose summarizes *J. Chem. Theory Comput.* **2016**, **12**, **3913–3925** (DOI **10.1021/acs.jctc.6b00461**).

## Summary

Müller and Hartke reparametrize ReaxFF for disulfide mechanochemistry using multireference *ab initio* reference data. The motivation is single-molecule AFM-style pulling: routine single-reference DFT is a weak match for S–S bond breaking under load, and ab initio MD cannot reach millisecond-scale traces. They fit with a nondeterministic global evolutionary algorithm, then illustrate the field with exploratory ReaxFF trajectories on large multifunctional mechanophores (DSM-C and DSM-PEG in the article) where disulfides are intentional weak links—sizes and solvent/handle motifs that are impractical for first-principles dynamics.

## Methods

**Force-field training.** The work refits ReaxFF for mechanochemical disulfide chemistry in designed organomechanophores (Figure 1: DSM-C for conducting/solution AFM scenarios; DSM-PEG with polyethylene glycol handles), separate from earlier protein disulfide studies that relied on DFT-only training data. QM references combine multireference *ab initio* energy surfaces along stretch and bond-breaking paths with single-determinant HF/DFT comparisons where single-reference models fail (section 3.1). The training set covers those disulfide pathways plus additional geometries in the Supporting Information. Optimization uses the authors’ evolutionary-algorithm global search, motivated by their estimate that roughly **80 ± 20** parameters per atom must be matched to reliable reference energies for a usable reactive field. Validation is tied to those multireference surfaces and to literature context on ReaxFF practice for related chemistry.

**MD application.** Exploratory trajectories use **LAMMPS** with the authors’ newly fitted **ReaxFF** parametrization for the targeted C/H/O/S mechanophores (the article contrasts its error against legacy **LAMMPS** CHOS parametrizations such as Singh *et al.* and Mattsson *et al.* when discussing starting points for optimization). Systems include multifunctional mechanophores in **vacuo** and in a **toluene** solvent box with **periodic boundary conditions**; peripheral anchor atoms mimic attachment to a surface and AFM tip. Integration uses a **0.5 fs** time step at **300 K** in the **NVT** ensemble with a **Berendsen thermostat** (damping factor **100** in the paper’s units). The authors seed random velocities per trajectory to avoid redundant phase-space sampling. Illustrative pulling segments reach **25 ps** in one quoted comparison to AFM timescales, and rupture scouting runs search for events within **50 ps** windows when ramping end forces. **N/A — barostat / hydrostatic pressure control** — not used for these constant-volume gallery simulations. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not reported for these exploratory runs.

**Static QM.** Multireference and DFT/HF calculations generate the training surfaces; they are not presented as a standalone dynamics substitute for AFM time scales.
## Findings

The fitted ReaxFF is reported to track multireference energetics along disulfide mechanochemical pathways and to allow reactive MD of large mechanophores with disulfide breaking points. The exploratory trajectories are framed as narrowing part of the time-scale gap between AFM experiments and atomistic simulation when bond-order MD remains affordable for solvent-bearing constructs. Compared with common practice, the article stresses that training on **multireference** surfaces—not only routine **DFT**—matters for quantitative S–S rupture under load. Mechanophore design is a sensitivity lever: conducting **DSM-C** versus **PEG**-functionalized **DSM-PEG** motifs are proposed so that force-extension traces isolate disulfide events from competing pathways. The discussion flags transferability limits—each new reaction class still needs its own reference set and optimization cycle—and notes that agreement with a given AFM trace will still depend on laboratory spring constants, loading rates, and solvent chemistry.

## Limitations

Parameter fits are specific to the chosen disulfide mechanochemistry targets; extending to other reaction classes requires new training data and optimization cycles. Quantitative agreement with a given AFM experiment still depends on instrument spring constants, loading rates, solvent environment, and anchor chemistry that are not universal across laboratories.

## Relevance to group

The article shows a **QM**-reference upgrade path—**multireference** training targets—for **ReaxFF** in **mechanochemistry**, adjacent to broader **reactive** **FF** development practice in **polymer** **pulling** and **sonochemistry** communities that already use **bond-order** models. It is a useful citation when arguing that **high-quality** **reference** data, not only **system size**, gates **accuracy** for **S–S** **rupture** under **load** in **van Duin**-style **ReaxFF** workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.6b00461](https://doi.org/10.1021/acs.jctc.6b00461) — *J. Chem. Theory Comput.* **12**, **3913–3925** (2016); **Supporting Information** documents additional **training** **geometries** referenced in the main text.

## Related topics

- [[reaxff-family]]
