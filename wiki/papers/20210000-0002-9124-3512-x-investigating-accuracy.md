---
id: paper:20210000-0002-9124-3512-x-investigating-accuracy
type: paper
title: "Investigating the Accuracy of Water Models through the Van Hove Correlation Function"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:water-silica-geo
  - method:classical-md
  - method:reaxff
  - method:aimd
  - method:semiempirical-tightbinding
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:aimd
  - keyword:polarizable-ff
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.1c00637"
year: 2021
authors:
  - "Ray A. Matsumoto"
  - "Matthew W. Thompson"
  - "Van Quan Vuong"
  - "Weiwei Zhang"
  - "Yuya Shinohara"
  - "Adri C. T. van Duin"
  - "Paul R. C. Kent"
  - "Stephan Irle"
  - "Takeshi Egami"
  - "Peter T. Cummings"
venue: "J. Chem. Theory Comput."
pdf_sha256: "8a974ca0df05f0d3a9719c4dd35bd0e744945618ce52872756c0761348061f0c"
pdf_path: "papers/Matsumoto_JCTC_vanHove_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20210000-0002-9124-3512-x-investigating-accuracy -->

## Summary

Static pair correlation functions \(g(r)\) capture instantaneous structure, while the **Van Hove function** \(G(\mathbf{r},t)\) (or angularly averaged \(G(r,t)\)) encodes **time-separated** correlations and links molecular trajectories to **inelastic X-ray scattering (IXS)** observables. This *J. Chem. Theory Comput.* study computes \(G(r,t)\) for **neat liquid water** across a wide cost range: **fixed-charge** classical MD, a **polarizable** model, **ReaxFF** reactive MD, **DFTB** MD, and **ab initio** MD. The authors ask how **small** and **short** simulations can be while still yielding **interpretable**, **IXS-consistent** \(G(r,t)\), using published **IXS** data as the reference (not a new experiment in the manuscript). **Adri C. T. van Duin** coauthored, tying the paper to broader **reactive water** and method-benchmarking threads in the corpus.

## Methods

**1 — MD application (atomistic dynamics).** Parallel **neat-liquid** water trajectories are reported for each modeling tier, with program choices and equilibration recipes given in the article and **SI** (e.g. **LAMMPS**/**GROMACS**/**CP2K**/**VASP**-class engines as appropriate). **3D periodic** cubic (or equivalent) **supercells**; **NVT** and/or **NPT** with **Nose–Hoover**- or **Bussi**-style **thermostat** and, where density is relaxed, isotropic **NPT** near **1 bar** **pressure**. **Timestep** is sub-1 fs for classical and ReaxFF water and shorter for **AIMD** (exact values in JCTC tables). **Equilibration** is followed by **multi-ns** production for several classical tracks and shorter windows where **AIMD** cost limits length; the paper explicitly studies convergence of **\(G(r,t)\)** with **system size** and **trajectory length**. **Temperature** is near ambient for the liquid-water **IXS** comparison (see JCTC for setpoints, typically ~300 K class conditions). **Electric field** in bulk neat-water calibration—**N/A**. **Umbrella / metadynamics**—**N/A** unless the **SI** adds a rare-event method. **Shear / shock**—**N/A** in the benchmark as summarized.

**2 — Force-field training.** **N/A** as a new ReaxFF fit: the work **benchmarks** published **ReaxFF** and other water models against **IXS** \(G(r,t)\).

**3 — Static QM / AIMD / DFTB.** **AIMD** uses **DFT** settings in the JCTC text (functional, basis/cutoff, *k*-mesh as listed). **DFTB** parameters follow the DFTB section of the same paper. **N/A** for **GW** or optical properties in the stated scope.

**4 — Experiments (reference data).** **IXS** **\(G(r,t)\)** from the literature (Iwashita *et al.*, cited in the article) provides the experimental reference; the manuscript does not report a new **IXS** campaign.

**5 — Galley.** The repository `pdf_path` is an ACS **galley**; prefer the **version of record** for final tables and page references.

## Findings

**Outcomes and mechanisms:** All tiers show at least **qualitative** agreement with **IXS** \(G(r,t)\) in the authors’ comparison, and some models and observables reach **quantitative** agreement. The work highlights how **sampling** limits (short **AIMD**, small cells) affect **reliability** of **spatiotemporal** **correlation** and **diffusive** dynamics in \(G(r,t)\), not just thermodynamic means.

**Comparisons:** head-to-head **model vs IXS** and **model vs model** for the same probe; **polarizable** and **AIMD** tiers behave differently from fixed-charge classical water in some \(r,t\) windows.

**Sensitivity and design levers:** **System size** and **trajectory duration** shift estimated **\(G(r,t)\)**; the paper’s motivation is to map which approximations fail first when cost forces small/short runs.

**Limitations and outlook:** The abstract frames **aqueous solutions** and **nanoconfinement** as **future** extensions beyond neat bulk water in this report. **ReaxFF** reactivity is not a guarantee of best **\(G(r,t)\)** accuracy versus polarizable or **AIMD** water for every channel.

**Corpus honesty:** The local file is a **galley**; **citable** numerical cutoffs and table rows should be checked against the **VOR** PDF.

## Limitations

Galley PDF in the corpus may differ from the final **JCTC** layout. Classical and reactive **FF** limits on **polarization** and **charge** transfer apply; readers should not infer **optical** or **electronic** spectra from this **structural** benchmark alone.

## Relevance to group

**Van Duin**-authored work situating **ReaxFF** water in a **multi-method** **IXS** validation alongside **AIMD** and **DFTB**, useful for method-choice narratives in the wiki.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.1c00637](https://doi.org/10.1021/acs.jctc.1c00637)

## Related topics

- [[reaxff-family]]

