---
id: paper:2014senftle-catcom-52-20-determining-situ
type: paper
title: "Determining in situ phases of a nanoparticle catalyst via grand canonical Monte Carlo simulations with the ReaxFF potential"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - method:monte-carlo
  - task:application
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1016/j.catcom.2013.12.001"
year: 2014
authors:
  - "Thomas P. Senftle"
  - "Adri C.T. van Duin"
  - "Michael J. Janik"
venue: "Catalysis Communications 52 (2014) 72–77"
pdf_sha256: "2ffc6cdbbaa6382d53ef97f17ea71ecc10eed9764fb1329221c58dd133c64406"
pdf_path: "papers/Senftle_CatComm2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014senftle-catcom-52-20-determining-situ -->

## One-paragraph summary

Senftle, van Duin, and Janik present a **hybrid grand-canonical Monte Carlo / molecular dynamics (GC-MC/MD)** workflow that uses **ReaxFF** to predict **Pd nanoparticle** structures and **phase stability** as a function of **temperature** and **gas-phase composition**, motivated by the fact that Pd can form **oxide**, **hydride**, and **carbide**-like arrangements under operating environments. The short communication summarizes the ReaxFF formalism for reactive events, cites separately published **Pd/O** and **Pd/H** parameter origins, introduces new **Pd/C/H** training-quality statistics, and highlights two demonstration cases: **oxidation** of a ~3 nm Pd cluster versus O\(_2\) pressure and temperature, and **multi-species GC-MC/MD** exchanging **C and H** with a hydrocarbon/hydrogen reservoir to probe **carbide/hydride** competition.

## Methods

- **ReaxFF** energy expression (bond order, polarizable charge treatment) enabling **RMD** and GC ensembles.
- **GC-MC/MD** in a \((T,V,N_{\mathrm{Pd}},\mu_{\mathrm{res}})\)-style ensemble with stochastic insertion/deletion/displacement of non-Pd atoms, **MD relaxation** after MC moves, and specialized volume accounting to reduce bias (as referenced to prior work).
- Pd/O and Pd/H parameters from earlier publications; Pd/C/H parameters fit to a training set of **adsorption energies** on Pd sites.

## Findings

- The approach is positioned as a practical bridge between costly **DFT/ab initio thermodynamics** and nanoparticle-scale **environment-dependent** catalyst structure prediction.
- Two highlighted applications: **oxygen uptake / oxidation** in a 3 nm Pd cluster across \(P,T\); and **hydrogen/hydrocarbon-ratio** dependent **carbide vs hydride** formation in GC-MC/MD.

## Limitations

- The communication points to **forthcoming publications** for full Pd/C/H training-set disclosure beyond average error statistics quoted in the extract.
- Extract covers early pages; quantitative phase diagrams and convergence details require deeper PDF reading.

## Relevance to group

Co-authored by **Adri C. T. van Duin**; demonstrates **ReaxFF + GC-MC/MD** as a reusable strategy for **in situ catalyst speciation** problems central to catalysis modeling in the lineage.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.catcom.2013.12.001](https://doi.org/10.1016/j.catcom.2013.12.001)

## Related topics

- [[reaxff-family]]
