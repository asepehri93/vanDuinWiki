---
id: paper:2014neyts-venue-paper
type: paper
title: "Thermodynamics at the nanoscale: Phase diagrams of nickel–carbon nanoclusters and equilibrium constants for phase transition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - material:alloy-bulk
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/C4NR02354D"
year: 2014
authors:
  - "Yannick Engelmann"
  - "Annemie Bogaerts"
  - "Erik C. Neyts"
venue: "Nanoscale (2014); DOI 10.1039/C4NR02354D"
pdf_sha256: "cb1e8733de71d607e4a6269e4ee35d9e881af4858e88233c22991ecde39286e9"
pdf_path: "papers/ReaxFF_others/Neyts_coworkers_NiC_Lindemann_2014.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014neyts-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    The corpus PDF is a Royal Society of Chemistry **Accepted Manuscript** with placeholder metadata in the header; summaries follow the **abstract block** in the extract. Confirm **volume/pages** from the **final Nanoscale** issue.

## Summary

**Catalytic chemical vapor deposition (CCVD)** of **carbon nanotubes** depends on **Ni–C** catalyst particles that may be **solid**, **molten**, or **partially molten** during growth; inferring the **actual phase** from experiments alone is nontrivial for **nanoscale** clusters. Engelmann, Bogaerts, and Neyts simulate **Ni–C nanoclusters** with **ReaxFF reactive MD**, comparing **icosahedral** and **Wulff** morphologies as model catalyst shapes. They construct **temperature-dependent phase diagrams** using both a **Lindemann index** (Eq. 1 in the manuscript) and **potential energy** traces, then derive **equilibrium constants** and **solid/liquid fractions** during melting so that melting points are less sensitive to a **single arbitrary Lindemann cutoff**—a common pain point in nanoscale melting diagnostics.

## Methods

### Reactive MD model (Ni–C clusters)

- **ReaxFF** simulations include **C–Ni** bonding and **carbon dissolution** into **nickel** as **temperature** increases (**Summary**).

### Morphology comparisons

- **Icosahedral** vs **Wulff** **Ni–C** **nanoclusters** probe how **particle shape** influences **melting** and **phase coexistence** (**Summary**).

### Melting diagnostics

- **Lindemann index** (Eq. 1 in manuscript) and **mean potential energy** vs **temperature** track disordering/melting (**Summary**).

### Thermodynamic post-processing

- Analytic expressions for **equilibrium constants** and **solid/liquid fractions** reduce sensitivity to a **single arbitrary Lindemann cutoff** (**Summary**).

### Ingest note

Corpus PDF is a **Nanoscale Accepted Manuscript** (`papers/ReaxFF_others/Neyts_coworkers_NiC_Lindemann_2014.pdf`); verify **volume/pages** against the **final** issue before citing figure numbers.

### 1 — MD application (atomistic dynamics)

`normalized/extracts/2014neyts-venue-paper_p1-2.txt` is **abstract-level** for this slug; detailed **MD** settings require the **typeset Nanoscale** article.

- **Engine / code:** **ReaxFF** **molecular dynamics** of **Ni–C nanoclusters** (abstract); **N/A — MD package** not in the indexed excerpt.
- **System size & composition:** **N/A — atom counts** not in `p1–2` excerpt (clusters described qualitatively as **icosahedral** vs **Wulff** morphologies in wiki summary).
- **Boundaries / periodicity:** **N/A — not stated** in the indexed excerpt.
- **Ensemble:** **NVT** is the plausible default for isolated **nanocluster** heating scans, but **N/A — explicit ensemble** not confirmed in `p1–2` text—verify in **Nanoscale** **10.1039/C4NR02354D**.
- **Timestep / duration / thermostat / barostat:** **N/A — not stated** in the indexed excerpt.
- **Temperature:** **temperature-dependent** **melting** diagnostics (**Lindemann index**, mean potential energy) are central to the abstract narrative.
- **Pressure:** **N/A — not stated** in the excerpt.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated.**

### 2 — Force-field training

**N/A —** application paper using **ReaxFF** for **Ni–C** **CCVD** **catalyst** modeling rather than a new fit documented on this slug.

## Findings

### Outcomes and mechanisms

The abstract-level summary on file emphasizes **melting**/**phase** behavior of **Ni–C** **nanoclusters** and analytic reductions (**equilibrium constants**, solid/liquid **fractions**) meant to reduce **Lindemann cutoff** arbitrariness when estimating **melting temperatures**.

### Comparisons

Contrasts **icosahedral** vs **Wulff** **morphology** effects on apparent **melting** behavior in the manuscript framing summarized on this page.

### Sensitivity

**Temperature** sweeps and **morphology** choice are the main **sensitivity** knobs discussed at abstract depth.

### Limitations and corpus honesty

**Accepted manuscript** PDF; cluster models omit full **CCVD** reactor **chemistry** and **support** interactions. Cite the **final Nanoscale** **PDF** for authoritative numbers and figure labels.

## Limitations

**Accepted manuscript** PDF; partial extract; cluster models omit full **CCVD** fluid environment.

## Relevance to group

**Ni–C** **ReaxFF** thermodynamics relevant to **catalytic carbon** nanostructure formation—complements **CNT** growth and **fuel** chemistry entries.

## Citations and evidence anchors

- https://doi.org/10.1039/C4NR02354D — Nanoscale article landing page.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
