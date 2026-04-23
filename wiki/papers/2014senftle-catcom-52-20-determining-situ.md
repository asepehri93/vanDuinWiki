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
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014senftle-catcom-52-20-determining-situ -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Senftle, van Duin, and Janik present a **hybrid grand-canonical Monte Carlo / molecular dynamics (GC-MC/MD)** workflow that uses **ReaxFF** to predict **Pd nanoparticle** structures and **phase stability** as a function of **temperature** and **gas-phase composition**, motivated by the fact that Pd can form **oxide**, **hydride**, and **carbide**-like arrangements under operating environments. The short communication summarizes the ReaxFF formalism for reactive events, cites separately published **Pd/O** and **Pd/H** parameter origins, introduces new **Pd/C/H** training-quality statistics, and highlights two demonstration cases: **oxidation** of a ~3 nm Pd cluster versus O\(_2\) pressure and temperature, and **multi-species GC-MC/MD** exchanging **C and H** with a hydrocarbon/hydrogen reservoir to probe **carbide/hydride** competition.

## Methods

### ReaxFF formalism and parameter lineage

- **ReaxFF** provides **bond-order**-dependent energetics and **polarizable charge** treatment suitable for **reactive MD** and **open** ensembles (communication introduction).
- **Pd/O** and **Pd/H** interaction subsets come from earlier **ReaxFF** publications cited in the article; new **Pd/C/H** terms are fit to a **QM-derived** training set emphasizing **adsorption energies** on **Pd** sites (extract-level summary).

### Grand-canonical hybrid sampling (GC-MC/MD)

- **Hybrid GC-MC/MD** couples **grand-canonical Monte Carlo** moves (insertion/deletion/displacement of **non-Pd** species) with **MD relaxation** segments in a \((T,V,N_{\mathrm{Pd}},\mu_{\mathrm{res}})\)-style framework, including specialized **volume** bookkeeping to reduce bias (references to prior methodological papers in the communication).

### Demonstration cases summarized in the abstract/intro

- **Oxidation:** **O\(_2\)** uptake on a **~3 nm** **Pd** cluster vs **temperature** and **oxygen pressure**.
- **Multi-component reservoir:** **GC-MC/MD** exchanging **C** and **H** with a **hydrocarbon/hydrogen** reservoir to probe competition between **carbide-like** and **hydride-like** nanoparticle states.

### Coverage note

- Full **MC** move sets, **chemical potential** definitions, and **convergence** diagnostics appear in the **Catalysis Communications** PDF beyond the short extract.

### 1 — Grand-canonical sampling + MD segments (GC-MC/MD)

The communication couples **grand-canonical Monte Carlo** moves on **non-Pd** species with **molecular dynamics** relaxation segments—**open ensemble** sampling at specified **\(T,V\)** with reservoir **chemical potentials** (see cited methodological references in the article). **System / composition:** demonstration **oxidation** tracks a **~3 nm** **Pd** cluster with **O\(_2\)** exchange; the multi-species case exchanges **C** and **H** against a **hydrocarbon/hydrogen** reservoir (abstract)—exact **atom** totals per snapshot are **N/A —** confirm in **`pdf_path`**. **Periodic** supercells for the **nanoparticle** models are implied by the GC ensemble setup, but explicit **PBC** vectors are **N/A —** not on the two-page extract. **Temperature and gas-phase pressure:** Case 1 varies **temperature** together with **oxygen pressure** (abstract). **Ensemble:** **NVT**-style **thermal** control is typical for the **MD** segments between **GCMC** moves, but explicit thermostat labels are **N/A —** confirm in **`pdf_path`**. **Timestep (fs) and total ps/ns segment lengths:** **N/A —** not on the indexed extract. **Barostat:** **constant-volume** **\(T,V,N_{\mathrm{Pd}},\mu\)** framing; **NPT** — **N/A —** not highlighted in the abstract-level summary. **Engine:** **N/A —** software name not on indexed pages. **Electric field / enhanced sampling:** **N/A —** not part of the described **GC-MC/MD** workflow.

### 2 — Force-field training

**Pd/O** and **Pd/H** subsets are imported from earlier **ReaxFF** publications; new **Pd/C/H** terms are fit to **QM-derived** **training** statistics quoted in the extract. **Optimization** details and full **reference** **energy** tables are **N/A —** deferred to the forthcoming publications noted in the communication—consult **`pdf_path`**.

## Findings

- The authors position **GC-MC/MD + ReaxFF** as a tractable alternative to exhaustive **ab initio thermodynamics** for **environment-dependent** **nanoparticle** speciation.
- **Case 1:** maps **oxidation** of a **~3 nm** **Pd** cluster across **\(P,T\)** space.
- **Case 2:** explores **hydrogen/hydrocarbon** ratio effects on **carbide vs hydride** competition in **open** ensemble sampling.

**Comparisons / limitations.** Quantitative agreement with **experiment** and any detailed **benchmark** plots are only recoverable from the **full PDF** and cited follow-on papers; this wiki page is **extract**-anchored and should not be treated as a numeric substitute.

## Limitations

- The communication points to **forthcoming publications** for full Pd/C/H training-set disclosure beyond average error statistics quoted in the extract.
- Extract covers early pages; quantitative phase diagrams and convergence details require deeper PDF reading.

## Relevance to group

Co-authored by **Adri C. T. van Duin**; demonstrates **ReaxFF + GC-MC/MD** as a reusable strategy for **in situ catalyst speciation** problems central to catalysis modeling in the lineage.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.catcom.2013.12.001](https://doi.org/10.1016/j.catcom.2013.12.001)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
