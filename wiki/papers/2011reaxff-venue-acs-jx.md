---
id: paper:2011reaxff-venue-acs-jx
type: paper
title: "ReaxFF-lg: Correction of the ReaxFF reactive force field for London dispersion, with applications to the equations of state for energetic materials"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, domain:organics-polymers-pyrolysis, method:reaxff, task:parameterization, task:validation]
candidate_tags: []
source_refs: []
doi: "10.1021/jp201599t"
year: 2011
authors: ["Liu, Lianchi", "Liu, Yi", "Zybin, Sergey V.", "Sun, Huai", "Goddard, William A., III"]
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "0579728040a35c9179732c67cd3d3db782f39103bc70c15f2f132a22ccb26cfd"
pdf_path: "papers/ReaxFF_others/ReaxFF_lg.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011reaxff-venue-acs-jx -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The paper introduces **ReaxFF-lg**, adding a **low-gradient (lg) long-range dispersion** correction on top of standard ReaxFF so that **molecular crystal densities** are not systematically too low—addressing the known limitation that practical DFT training data for solids underbinds **London dispersion**, which propagates into ReaxFF’s **Morse-like vdW** terms when those terms were not trained for long-range attraction. Parameters are fit using **low-temperature crystal structures** for benchmarks including **graphite, polyethylene, CO₂(s), N₂(s)**, and energetic crystals (**RDX, PETN, TATB, NM**). The abstract reports the average volume error dropping from **18.5% to 4.2%** for those systems, and highlights improved **α–γ RDX** transition pressure/volume compared to experiment.

## Methods

### 1 — MD application (atomistic dynamics)

The article’s primary deliverable is a **dispersion-corrected reactive force field** and **crystal equation-of-state** validation rather than a standalone production-trajectory study on pp. 1–2 of `normalized/extracts/2011reaxff-venue-acs-jx_p1-2.txt`.

- **Engine / code:** **Reactive molecular dynamics (ReaxFF-RD)** is discussed as a major motivation/use-case for accurate crystal densities (Introduction); **N/A —** a specific MD integrator/package for the EOS validation runs is not named on the indexed excerpt pages.
- **System size & composition:** Benchmark **molecular crystals** and **energetic crystals** named in the abstract: **graphite, polyethylene, CO₂(s), N₂(s), RDX, PETN, TATB, NM** (indexed excerpt).
- **Boundaries / periodicity:** **Molecular crystals** imply **three-dimensional periodic** models for EOS work; **N/A —** explicit supercell sizes are not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** schedules, timestep sizes, trajectory segment lengths, and thermostat/barostat algorithms are not stated on the indexed excerpt pages for the EOS validation protocol (the excerpt focuses on energy definitions and fitting inputs).
- **Temperature:** **Room temperature** comparisons are stated for EOS vs experiment in Sec. 2 opening (extract).
- **Pressure / stress:** **Pressure–volume** / **phase transition** language appears for **RDX** (**α–γ**) in the abstract; **N/A —** full stress-control protocol details are not on the indexed excerpt pages.
- **Electric field:** **N/A —** not indicated in the indexed excerpt.
- **Replica / enhanced sampling:** **N/A —** not indicated in the indexed excerpt.

### 2 — Force-field training

- **Parent FF / elements:** **ReaxFF** with the standard valence + **vdW + Coulomb** partition in Eq. (2.2) of the article (extract).
- **QM reference / training philosophy:** The introduction states prior **ReaxFF** development used **consistent QM** training, commonly **B3LYP-flavor DFT** with **6-31G\*\*** for molecular training data, and notes systematic **London dispersion** underbinding for **molecular solids** at practical DFT levels (Introduction, extract).
- **Training set / targets:** **Low-temperature crystal structures** for **graphite (P63mc), polyethylene (Pnam), CO₂ (Pa3), N₂ (Pa3)** are used to determine **lg** parameters for “ordinary organic” motifs; **densities** and **heats of sublimation** enter the training discussion; parameters are then extended/refined for **RDX, PETN, TATB, NM** (Sec. 2, extract).
- **Functional form / optimization variables:** **ReaxFF-lg** defines \(E_{\text{Reax-lg}}=E_{\text{Reax}}+E_{\text{lg}}\) with \(E_{\text{lg}}\) as a pairwise long-range correction built from **\(r_{ij}^{-6}\)**-like terms using **\(R_{e,ij}\)** and **\(C_{\text{lg},ij}\)** (Eqs. (2.1)–(2.3), extract). **Geometric combination rules** apply unless off-diagonals are explicitly listed; **\(d=1.0\)** is used; **\(R_e\)** is taken from **UFF** vdW radii and **only \(C_{\text{lg}}\)** is fitted (extract).
- **Reference data used for validation:** After fitting, the authors report **equations of state** compared to **experiment at room temperature** (Sec. 2 opening + abstract, extract).

## Findings

**Outcomes and mechanisms:** **ReaxFF-lg** reduces the average **equilibrium volume** error for the listed benchmark systems from **18.5% to 4.2%** (abstract, extract). The **lg** correction is designed to add **long-range London dispersion** while leaving short-range **valence** interactions largely intact (Introduction + Eq. (2.3) discussion, extract).

**Comparisons:** The abstract highlights **crystal structures** and **equations of state** in **good agreement** with **experiment** after correction, and gives a concrete **RDX** **α–γ** transition benchmark (**~4.8 GPa** and **~2.18 g/cm³** from **ReaxFF-lg** vs **~3.9 GPa** and **~2.21 g/cm³** experimentally in the abstract wording, extract).

**Sensitivity and design levers:** The correction is parameterized from **low-temperature** reference crystals and then applied to **energetic** chemistries; the **α–γ RDX** case shows sensitivity of **transition pressure/density** to the dispersion treatment (abstract, extract).

**Limitations and outlook (authored tone):** The introduction frames the underlying issue as **DFT-for-solids** dispersion errors propagating into **ReaxFF** training when **vdW** terms were not trained for long-range attraction; **ReaxFF-lg** is proposed as a pragmatic extension (Introduction, extract).

**Corpus / KB honesty:** Numeric transition values above follow the **abstract** on the indexed excerpt pages; full tables, weighting schemes, and any additional validation cases require **`pdf_path`** beyond pp. 1–2.


## Limitations

- Adds complexity and parameters; users must ensure **ReaxFF-lg** is consistently applied when comparing to older ReaxFF datasets.
- Coverage is tied to the training chemistry set; extension to new elements/environments needs explicit validation.

## Relevance to group

Core **method lineage** paper for **dispersion-corrected ReaxFF** used in condensed-phase organics and **energetic materials** simulations.

## Citations and evidence anchors

- Abstract and Sec. 2: ReaxFF-lg definition, motivation, benchmark systems (J. Phys. Chem. A 2011, 115, 11016–11022; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
