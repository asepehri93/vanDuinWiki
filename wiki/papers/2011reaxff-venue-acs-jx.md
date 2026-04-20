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

- **Energy partition:** \(E_{\text{Reax-lg}} = E_{\text{Reax}} + E_{\text{lg}}\), with \(E_{\text{lg}}\) as pairwise **\(1/r^6\)**-like corrections built to minimally perturb valence distances.
- **Fitting:** Dispersion coefficients with **UFF-based equilibrium vdW radii** as described; training on experimental crystal structures and sublimation-related targets.

<!-- enrich-from-extract:v2 -->

- In this work, we report dispersion corrections for ReaxFF, based on this low-gradient model (ReaxFF-lg), for the energetic materials RDX, PETN, TATB, and NM plus graphite, polyethylene, solid carbon dioxide, and solid N 2, using the low temperature crystal structures to determine the lg correction parameters.
- Here we consider densities and heats of sublimation of these materials in the training sets.
- Then the ﬁtted parameters are extended to energetic materials and reﬁned to obtain the ﬁnal parameters.
- METHOD AND COMPUTATIONAL DETAILS In ReaxFF-lg, the total energy of the system can be expressed as EReax-lg ¼ EReax þ Elg ð2.1Þ where EReax is the energy evaluated from the previous ReaxFF force ﬁeld: EReax ¼ Ebond þ Elp þ Eover þ Eunder þ Eval þ Epen þ Ecoa þ Etors þ Econj þ EH-bond þ EvdW þ ECoulomb ð2.2Þ and Elg is the long-range-correction terms using the low-gradient model: Elg ¼/C0 ∑ N ij, i<j Clg, ij rij6 þ dReij6 ð2.3Þ Here rij is the distance between atom i and atom j, Reij is the equilibrium vdW distance between atoms i and j, and Clg,ij is the dispersion energy correction parameter.
- For each atomic pair ij, we use the geometric combination rules for both Reij and Clg,ij, unless the o ﬀ-diagonal parameters are listed speci ﬁcally for a particular pair.
- Low temperature crystal structures of graphite ( P63mc),19 polyethylene (PE, Pnam),20 carbon dioxide ( Pa3),21 and solid nitrogen22 (Pa3) were selected to determine the dispersion correction parameters for ordinary organic materials.


## Findings

- Substantially improved **equilibrium volumes** and **equations of state** for selected molecular crystals and energetic materials after lg correction.
- Detailed validation example for **RDX** phase transition pressure/density compared to experiment (per abstract).

### Additional results (article abstract)

- To validate the ReaxFF- lg method, we calculated the equations of state of these materials and compared the results with results from experiments at room temperature. 2.
- Here d is a scaling factor, but we set d = 1.0 since we found no need for scaling in this work.
- Re is taken as the vdW radii in the Universal force ﬁeld (UFF)18 (convenient since these values are de ﬁned in UFF up to element 103, Lr), as shown in Table 1, and only the Clg parameters are ﬁtted.
- Graphite and polyethylene are prototypes for determining the dispersion corrections for C/C0 C, C/C0 H, H/C0 H and were used previously for studying or testing the vdW interactions.23,24 Carbon dioxide and solid nitrogen are molecular c


## Limitations

- Adds complexity and parameters; users must ensure **ReaxFF-lg** is consistently applied when comparing to older ReaxFF datasets.
- Coverage is tied to the training chemistry set; extension to new elements/environments needs explicit validation.

## Relevance to group

Core **method lineage** paper for **dispersion-corrected ReaxFF** used in condensed-phase organics and **energetic materials** simulations.

## Citations and evidence anchors

- Abstract and Sec. 2: ReaxFF-lg definition, motivation, benchmark systems (J. Phys. Chem. A 2011, 115, 11016–11022; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
