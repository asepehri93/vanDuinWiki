---
id: paper:2014ganesh-venue-binding-diffusion
type: paper
title: "Binding and diffusion of lithium in graphite: quantum Monte Carlo benchmarks and validation of van der Waals density functional methods"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - method:dft-static
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:graphene-carbon
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/ct500617z"
year: 2014
authors:
  - "Ganesh, Panchapakesan"
  - "Kim, Jeongnim"
  - "Park, Changwon"
  - "Yoon, Mina"
  - "Reboredo, Fernando A."
  - "Kent, Paul R. C."
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "50869aa77602992671331c937beec82ce27304a9c008fd3a07a5354348ea22d7"
pdf_path: "papers/Others/Ganesh et al. - 2014 - Binding and Diffusion of Lithium in Graphite Quan.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014ganesh-venue-binding-diffusion -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Diffusion quantum Monte Carlo (DMC) benchmarks for Li adsorption and diffusion in AA-stacked graphite are compared to several van der Waals–aware DFT approximations. AA graphite is used as a controlled stacking to locate dilute Li sites; QMC lattice constants for pure AA graphite match experiment. Many vdW-corrected DFT recipes that work for AB graphite are shown to struggle for AA graphite; among those tested, vdW-DF2 scores best overall for AA graphite plus Li binding and diffusion, though binding-energy errors remain. Charge-aware vdW corrections (e.g., TS-vdW) are motivated over fixed empirical dispersion when charge transfer matters (abstract; introduction, extract).

## Methods

### 1 — MD application

**N/A —** this work is **DMC** and **DFT** benchmarking of **Li** in **graphite**, not production **classical** or **ReaxFF MD**.

### 2 — Force-field training

**N/A —** not applicable.

### 3 — Static QM / QMC (Li in AA graphite)

- **QMC (DMC):** **Diffusion Monte Carlo** benchmarks **adsorption** and **diffusion** of **dilute Li** in **AA-stacked graphite** (symmetry-determined sites; abstract; `normalized/extracts/2014ganesh-venue-binding-diffusion_p1-2.txt`).
- **Supercells:** smaller cell—**two** graphene layers of **50 C** each with optional **single Li** (\(x=0.06\) in Li\(_x\)C\(_6\)); larger “doubled” cell—**200 C** with **two Li** at the same concentration; **binding** from the **larger** cell and **diffusion barriers** from the smaller (extract).
- **Geometry protocol:** **in-plane C–C** fixed at experimental **1.421 Å**; **interlayer separation** scanned to probe **vdW** treatment (extract).
- **DFT / functional family:** comparisons include **vdW-DF**, **vdW-DF2**, **DFT-D2**, and **Hirshfeld-partitioned TS-vdW**-style charge-aware corrections (abstract; introduction, extract).
- **Dispersion:** central question is how **vdW** is treated across these families (abstract).
- **Basis / k-mesh / pathway details:** full plane-wave settings, **Brillouin-zone k-mesh** choices, and barrier definitions are given in **JCTC** Methods in **`pdf_path`** (not duplicated from the short extract).

## Findings

### 1 — Outcomes and mechanisms

**DMC** lattice constants for pure AA graphite **agree with experiment**. AA-stacked graphite is shown to **challenge many vdW-inclusive DFT recipes** even when those recipes work for conventional **AB** graphite. Across AA graphite and **Li binding and diffusion**, **vdW-DF2** achieves the **highest overall DFT accuracy** in their comparison, **though binding-energy errors remain**. **Empirical dispersion (DFT-D) approaches are unreliable** unless **local charge transfer** is accounted for (motivating **Hirshfeld-weighted** schemes such as **TS-vdW**). Overall, accurate Li–graphite modeling requires **simultaneous** treatment of **charge transfer** and **dispersion**, favoring **self-consistent** vdW-inclusive functionals (abstract; extract pages 1–2).

### 2 — Comparisons

- **DMC** vs several **vdW-inclusive DFT** recipes; **DFT** rankings vs **QMC** references (abstract).

### 3 — Sensitivity

- **Interlayer separation** scans couple **Li** energetics to **graphite** **vdW** treatment (extract).

### 4 — Limitations / outlook

- **AA stacking** is a computational construct vs ground-state **AB** graphite (**## Limitations**).

### 5 — Corpus / KB honesty

- Detailed **barrier** numbers and **DFT** settings must be read from **`pdf_path`**; this page tracks abstract-level claims only.

## Limitations

AA stacking is a computational convenience versus ground-state AB graphite; DMC and DFT comparisons inherit respective cost and functional biases as discussed in the paper.

## Citations and evidence anchors

- DOI `10.1021/ct500617z` (article footer in extract).
- Abstract (extract page 1).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
