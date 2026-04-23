---
id: paper:2022cnki-venue-paper
type: paper
title: "水蒸气对 CaO 碳酸化过程的影响机制研究 / Study on the Influence Mechanism of Water Vapor on the CaO Carbonation Reaction"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:thermal-decomposition
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: ""
year: 2022
authors:
  - "王娜娜 (Wang Na-Na)"
  - "冯于川 (Feng Yu-Chuan)"
  - "郭欣 (Guo Xin)"
venue: "Journal of Engineering Thermophysics"
pdf_sha256: "ff670fb33913722ad02880b6d12c56ee0d3c9fc4686a8d59eae9096a2d7406b7"
pdf_path: "papers/ReaxFF_others/guoxin_paper_Chinese.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2022cnki-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    The bilingual PDF does not expose a DOI in the corpus extract; confirm bibliographic details from the **version-of-record** when available.

## Summary

Calcium looping processes expose CaO-based sorbents to CO\(_2\) often in humid flue gases, so understanding whether water changes intrinsic reaction kinetics versus transport through a growing carbonate product layer is central to interpreting pilot-scale behavior. The authors state that prior experimental literature disagrees on mechanisms—some work emphasizes possible Ca(OH)\(_2\) pathways, others argue water can promote carbonation even without hydroxide signatures, and still others emphasize reduced diffusion resistance or particle fragmentation—motivating an atomically resolved view of the product layer. Reactive molecular dynamics with a Ca/Al/C/H/O ReaxFF parameterization (developed in collaboration with van Duin and cross-checked against prior oxide and carbonate literature cited in the Chinese/English article) simulates CaO nanoparticle carbonation in CO\(_2\) with explicit water across 400–1000 K, alongside thermogravimetric experiments summarized in the paper. The computational setup described in the journal uses an ~8 nm cubic cell containing an ~3.6 nm CaO nanoparticle, with CO\(_2\) counts chosen so that a distinct product layer forms at the surface (the authors report testing CO\(_2\) loading until roughly three hundred molecules yield a clear layer). Matching a stated 1:1 CO\(_2\):H\(_2\)O gas-phase ratio, simulations integrate NVT dynamics with LAMMPS using Berendsen thermostats as described in §1.2 of the source PDF. The study distinguishes an initial rapid kinetic stage from a later diffusion-limited stage through the product layer.

## Methods

### A — ReaxFF parameterization (Ca/Al/C/H/O)

- **Lineage:** Ca/Al/C/H/O reactive description developed with van Duin-group involvement and checked against prior oxide and carbonate literature cited in the bilingual article (see source for parameter provenance and training targets).
- **Scope:** Bond breaking/formation for CaO carbonation in humid CO\(_2\) atmospheres; not stated in the local extract whether a published `ffield` file identifier matches a separate standalone ReaxFF paper—confirm in the journal text.

### B — Reactive MD (carbonation)

- **Engine / code:** LAMMPS with ReaxFF reactive dynamics (as stated in §1.2 of the source PDF).
- **System:** ~8 nm cubic simulation cell containing an ~3.6 nm CaO nanoparticle; CO\(_2\) loading increased until a distinct product layer forms at the surface (the authors report testing until roughly three hundred CO\(_2\) molecules).
- **Thermodynamic conditions:** Temperatures **400–1000 K**; gas-phase **1:1 CO\(_2\):H\(_2\)O** ratio as reported; **NVT** ensemble with **Berendsen** thermostat per the article.
- **Electrostatics / charge:** ReaxFF charge equilibration as implemented for the Ca/Al/C/H/O field (frequency and cutoffs per standard ReaxFF/LAMMPS usage in the paper).
- **Observables:** CO\(_2\) uptake, carbonate product-layer structure, and ion transport through the layer versus time; staged kinetics (fast vs diffusion-limited) compared to experiment.
- **Not stated in the corpus extract:** Integration timestep, thermostat damping parameters, equilibration protocol, and total trajectory length—take from the peer-reviewed PDF for reproduction.

### C — Quantum chemistry

- Not a primary methodology in this work; ReaxFF is benchmarked against experiment rather than ab initio energy data in the summary available here.

### D — Experiments

- Thermogravimetric and related measurements of CaO carbonation under humid CO\(_2\), summarized in the article for comparison to simulation stages (initial kinetic vs diffusion-limited regimes).

**AGENTS cross-walk.** Subsections A–D map to: **(2) ReaxFF** scope and provenance, **(1) reactive LAMMPS** in **NVT** with a **Berendsen** thermostat and **T = 400–1000 K**, a **1:1** **CO\(_2\):H\(_2\)O** **gas** **ratio** in §1.2 of the **source PDF** (re-read the **bilingual** text to confirm how **H\(_2\)**O **vapor** is implemented—this wiki does not substitute for that line), and **(4) TG** experiments. **Not** in the local extract: **timestep**, **QEq**/**neighbor** **cutoff** **policies**, **PBC** **details**, and **total** **trajectory** **length**—copy from the full **Journal of Engineering Thermophysics** **PDF** for reproduction. **N/A** — static **electric** field, **NPT** **barostat** **(unless** the **VOR** **adds** **NPT** **stages)**, and **umbrella**/**metadynamics** for the **RMD** **as** **summarized** here. **(3) DFT** **N/A** as a new **ab initio** **training** **database** (see **C**).

## Findings

**Outcomes and mechanisms.** The paper argues **H\(_2\)**O **does** **not** much change the **earliest** **fast** **reaction** **regime** but can **accelerate** the **later** **diffusion-limited** **regime** through the **growing** **product** **layer**; the **H\(_2\)**O**-induced** **speed-up** is **larger** at **lower** **T** and **weakens** as **T** **rises** in their **RMD+TG-aligned** **framing** (use the **VOR** **for** **exact** **T**-**trends** and **regime** **names**). **RMD** **rationale** (in the **article**): **faster** **ion** **(and** **CO\(_3^{2-}\)**-**class** **cluster) transport** **in** the **product** **layer** **with** **water** **present**, i.e. **H\(_2\)**O** **targets** the **bottleneck** **stage** more than the **very** **initial** **fast** **surface** **kinetics**.

**Comparisons.** Staged **ReaxFF** **kinetics** vs **TG-derived** **mass-loss** (and **stage** **assignment**) on the **same** **qualitative** **story**—confirm **all** **numbers** in the **VOR**; **`doi`** is **blank** in this repo and **`extraction_quality: partial`**, so this page stays **cautious** on **quantitative** **claims** not **double-checked** in the full **PDF**.
## Limitations

Chinese/English bilingual journal PDF in the corpus complicates automated metadata; force-field transferability to all CaO/CaCO\(_3\) morphologies requires the caveats noted in the ReaxFF development references.

## Relevance to group

Co-developed Ca/Al/C/H/O ReaxFF applied to calcium looping chemistry with van Duin collaboration explicitly cited.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Reader notes (navigation)

- Calcium looping / oxides: [[theme-oxides-silica-ceramics]]; ReaxFF lineage: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
