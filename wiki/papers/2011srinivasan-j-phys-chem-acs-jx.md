---
id: paper:2011srinivasan-j-phys-chem-acs-jx
type: paper
title: "Molecular-dynamics-based study of the collisions of hyperthermal atomic oxygen with graphene using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:nve-simulation
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/jp207179x"
year: 2011
authors:
  - "Sriram Goverapet Srinivasan"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry A 115, 13269–13280 (2011)"
pdf_sha256: "cb248ff13b5cfd5202afba0f6b056764d595191904cb918537dfc43f74780c5d"
pdf_path: "papers/Srinivasan_JPC_2011_Hyperthermal_O_graphene.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2011srinivasan-j-phys-chem-acs-jx -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Low-Earth-orbit (LEO)** atomic oxygen impacts carbonaceous thermal-protection materials at effective mean energies around **~5 eV** and high flux. This study uses **ReaxFF MD** to simulate **hyperthermal atomic oxygen** colliding with **graphene**, extending prior tight-binding direct dynamics work by **Paci et al.** Benchmark **5 eV** impacts on **small** pristine and **single-vacancy** **epoxidized** sheets recover qualitative event statistics comparable to Paci et al., with **O\(_2\)** removal dominated by an **Eley–Rideal**-type pathway. Larger **expanded** sheets show **high steady-state oxygen coverage** (more than **one O per three surface C** in the abstract’s statement), **diagonal buckling** under impact, and **trampoline-like** dynamics that increase **inelastic scattering** counts relative to the smaller system. **Bilayer AB** stacks are compared: breakup involves **epoxidation**, **interlayer bonding** and **AB→AA** conversion, **defect growth** in the top layer, then **bottom-layer erosion**—a **sequential layer-by-layer** picture.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF reactive molecular dynamics** studies **hyperthermal atomic oxygen** colliding with **graphene** in a **LEO**-motivated setting: the introduction cites a mean collision energy of **~5 eV** and an estimated flux of **~10¹⁵ O atoms cm⁻² s⁻¹** from the **O** number density and **~8 km/s** orbital speed (`normalized/extracts/2011srinivasan-j-phys-chem-acs-jx_p1-2.txt`).

- **Engine / code:** **Reactive MD** using **ReaxFF** (abstract + title); **N/A —** MD engine/package name not stated on the indexed excerpt pages.
- **System size & composition:** Benchmark **5 eV** impacts on **24-atom** **epoxidized** pristine graphene and a **single-vacancy** epoxidized sheet following **Paci et al. (J. Phys. Chem. A 2009)**; subsequent work extends to a **25-times-expanded** pristine monolayer and studies **pristine-sheet breakup** and **AB-stacked bilayer** impacts (abstract, extract).
- **Boundaries / periodicity:** **N/A —** explicit **PBC** vs free-surface details are not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** labels, timestep sizes, trajectory segment lengths, and thermostat/barostat algorithms are not stated on the indexed excerpt pages (the excerpt is abstract + introduction through benchmark description).
- **Temperature:** **493 K** appears in the introduction’s discussion of experimental **HOPG** temperature effects on erosion morphology (extract); simulation thermostat temperatures for the MD campaigns are **N/A —** not stated on the indexed excerpt pages.
- **Pressure / stress:** **N/A —** not stated on the indexed excerpt pages.
- **Electric field:** **N/A —** not stated on the indexed excerpt pages.
- **Replica / enhanced sampling:** **N/A —** not indicated in the indexed excerpt.

### 2 — Force-field training

**N/A —** this is a **ReaxFF application** paper, not a parameterization study.

### 3 — Static QM / DFT-only

**N/A —** not the paper’s primary methodology beyond referencing prior **DFT-TB direct dynamics** literature for context (Introduction, extract).

## Findings

For the **Paci et al.**-style benchmarks, **O₂** removal occurs predominantly via an **Eley–Rideal**-type pathway, with event counts described as **qualitatively consistent** with the prior tight-binding direct-dynamics study. On the **expanded** monolayer, steady-state **oxygen coverage** exceeds **one O per three surface C atoms**, impacts drive **diagonal buckling**, and **trampoline-like** motion increases **inelastic scattering** counts relative to the small system; **O₂** removal on the large sheet remains **strictly** via the **Eley–Rideal** mechanism as summarized in the abstract. **Bilayer AB** stacks fail in stages reported as **epoxidation**, **interlayer bonding** with **AB→AA** conversion, **defect growth** in the top layer, then **bottom-layer erosion**, i.e., a **sequential layer-by-layer** process.

## Limitations

- Classical reactive FF cannot match **full quantum** accuracy for every channel; coverage numbers and thresholds are simulation- and protocol-dependent.
- LEO environment includes **UV**, **ions**, and **molecular O\(_2\)** not all modeled simultaneously here.

## Relevance to group

Core **van Duin-group** **ReaxFF** application to **oxidative erosion** of **graphene/carbon** in **aerospace**-relevant conditions.

## Citations and evidence anchors

- DOI: [10.1021/jp207179x](https://doi.org/10.1021/jp207179x)
- Text-aligned pointer: `normalized/extracts/2011srinivasan-j-phys-chem-acs-jx_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- Atomic oxygen and carbon ablation (LEO materials)
