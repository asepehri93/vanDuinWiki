---
id: paper:2021daniela-k-jacquel-n-acs-reactive-force
type: paper
title: "Reactive Force Field-Based Molecular Dynamics Simulations on the Thermal Stability of Trimesic Acid on Graphene: Implications for the Design of Supramolecular Networks"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:nvt-simulation
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1021/acsanm.1c01759"
year: 2021
authors:
  - "Daniela K. Jacquelin"
  - "Federico A. Soria"
  - "Patricia A. Paredes-Olivera"
  - "Eduardo M. Patrito"
venue: "ACS Appl. Nano Mater."
pdf_sha256: "99a76f7e9b785b6c8eacdd2ac242b0928fc8ba58ec0d76fcb7af9e844c67da3f"
pdf_path: "papers/ReaxFF_others/Jacquelin_Patrito_ACS_AppNanMat_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021daniela-k-jacquel-n-acs-reactive-force -->

## Summary

Jacquelin *et al.* use ReaxFF to study how trimesic acid (TMA) self-assembles into several ordered 2D hydrogen-bonded motifs on graphene—honeycomb, filled honeycomb, flower, zigzag, and close-packed—and how those networks evolve with temperature. Simulations combine constant-*NVT* molecular dynamics and force-biased Monte Carlo (fbMC) up to **650 K**, tracking hydrogen-bond counts, OH radial distribution functions, and carboxyl-group torsion as order–disorder indicators. The work argues that honeycomb networks are more thermally robust than the dense zigzag and close-packed arrangements, that extra TMA “guests” in honeycomb pores further stabilize the lattice through host–guest interactions, and that kinetics (not only static energetics) governs when high-coverage close-packed regions reorder toward honeycomb-like packing.

## Methods

### MD application (ReaxFF on graphene)

- **Engine / code:** ReaxFF-based **molecular dynamics** and **force-biased Monte Carlo** as described in *ACS Appl. Nano Mater.*; the article does not restate a specific MD engine name in the indexed front matter—**N/A —** package string (e.g. LAMMPS) if not explicit in the PDF/SI, confirm `pdf_path`.
- **System size & composition:** TMA monolayer polymorphs on a **graphene** support in the named motifs; exact supercell sizes, TMA coverages, and atom counts are given in the article/SI—**N/A —** not duplicated in this note.
- **Boundaries / periodicity:** In-plane **periodic** 2D supercells for the supported monolayer models (standard for graphene/TMA slabs); normal-direction padding as in the paper.
- **Ensemble:** **NVT** MD for the thermal-stability sweeps; fbMC used for the compact **close-packed** case (per the article’s protocol for that segment).
- **Timestep & duration:** Integration settings and run lengths for NVT MD and fbMC stages are in *ACS Appl. Nano Mater.*—**N/A —** not restated here; use `pdf_path`.
- **Thermostat / barostat:** **NVT** thermostating for MD as implemented in the published workflow; **N/A —** explicit thermostat family string if not on the first pages of the PDF. **N/A —** isotropic **NPT** barostat for the monolayer studies unless the paper lists bulk **NPT** equilibration segments.
- **Temperature:** Simulations up to **650 K** (article abstract) to probe melting/reordering; intermediate setpoints and ramps are in the Methods.
- **Pressure, electric field, shear/shock, enhanced sampling:** **N/A —** no static electric field, shock loading, or umbrella/metadynamics in the reported workflow. Long-range and ReaxFF charge equilibration settings—**N/A —** in this short note; see `pdf_path`.

### Force-field training

**N/A —** this is an **application** study: the authors employ a published ReaxFF description for TMA, TMA–TMA, and TMA–graphene interactions and validate it against their QM reference comparators in the article (not a *de novo* open-parameter fit reported as the paper’s main contribution). Copy parameter lineage and any reweighting from `pdf_path`/SI for reproduction.

### Static QM

The paper uses **DFT** (and related) reference data to benchmark ReaxFF against TMA–TMA and TMA–graphene interaction strengths for selected configurations; **functional, basis, and *k*-mesh** details are tabulated in the article—**N/A —** not copied into this summary.

## Findings

- **Stability ordering:** By the melting temperatures and disorder metrics reported (H-bond counts, OH RDFs, carboxyl twisting), the **honeycomb** motif is more thermally stable than high-coverage **zigzag** and **close-packed** networks.
- **Host–guest:** Additional TMA molecules placed in honeycomb **pores** increase stability, consistent with **host–guest** stabilization beyond the empty honeycomb case.
- **Kinetics vs static scores:** The authors show that **energetics alone** do not explain all structural outcomes: **close-packed** regions can be **kinetically** destabilized even when static energy rankings might suggest otherwise, and **MD** captures rapid loss of order in some dense mesophases.
- **Reordering:** For **close-packed** islands, **fbMC** samples a transition toward a **quasi-honeycomb** arrangement, which the paper ties to **stronger dimeric –COOH** hydrogen bonding in honeycomb-like packing versus trimeric motifs in the compact structure.
- **Disorder mechanism:** **Twisting/rotation** of carboxyl groups with temperature disrupts hydrogen bonds and drives network “melting”; partial **desorption** at the onset of disorder is discussed in terms of **intermolecular** vibrational energy transfer.
- **Corpus honesty:** Melting temperatures, RDFs, and H-bond statistics should be quoted from the **version-of-record** PDF/SI; this page does not tabulate those numbers.

## Limitations

ReaxFF remains a semiempirical bond-order model; long-timescale rare events and subtle electronic effects in π-conjugated organics may require higher-level validation. Guest loading and coverage choices in simulation cells may not span all experimental STM solution conditions.

## Citations and evidence anchors

- DOI: [10.1021/acsanm.1c01759](https://doi.org/10.1021/acsanm.1c01759)

## Related topics

- [[reaxff-family]]
- [[graphene-carbon-nano]]
