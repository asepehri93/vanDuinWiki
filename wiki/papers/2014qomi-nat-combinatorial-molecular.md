---
id: paper:2014qomi-nat-combinatorial-molecular
type: paper
title: "Combinatorial molecular optimization of cement hydrates"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:cement-mineral
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:silica-silicate
  - keyword:validation-experiment
  - keyword:classical-ff
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/ncomms5960"
year: 2014
authors:
  - "M. J. Abdolhosseini Qomi"
  - "K. J. Krakowiak"
  - "M. Bauchy"
  - "K. L. Stewart"
  - "R. Shahsavari"
  - "D. Jagannathan"
  - "D. B. Brommer"
  - "A. Baronnet"
  - "M. J. Buehler"
  - "S. Yip"
  - "F.-J. Ulm"
  - "K. J. Van Vliet"
  - "R. J.-M. Pellenq"
venue: "Nat. Commun. 5, 4960 (2014)"
pdf_sha256: "680b8bf274a82abc6702bea5158cf128c2be0585962813ad4fe223c1ae50f869"
pdf_path: "papers/ReaxFF_others/MIT_team_Cement_Nature_Comm_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014qomi-nat-combinatorial-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **Nature Communications** article (`doi`). This is **cement C–S–H** structure screening with **computational materials** metrics—**not** a ReaxFF paper.

## Summary

This **Nature Communications** article (**DOI** `10.1038/ncomms5960`) presents a **combinatorial** exploration of **calcium–silicate–hydrate (C–S–H)** **atomistic** models—the major binding phase in **Portland cement**—linking **nanoscale structure** to **mechanical** response. The study introduces three **structural descriptors**: the **Ca/Si** ratio and two **medium-range order** correlation metrics quantifying **Si–O** and **Ca–O** environments. It relates **nanoindentation** metrics—**indentation modulus** **M** and **hardness** **H**—to these descriptors, emphasizing the ratio **M/H** as a diagnostic. The **abstract-level** narrative argues that while properties track **C/S**, **joint variation** of all three descriptors exposes an **extremum** in **M/H** reminiscent of **optimal network connectivity** ideas from **glass** rheology, with implications for designing **cement hydrate** **nanomechanics**. By enumerating many **atomistic** realizations, the work makes the **combinatorial** **search** explicit: the point is not a single **ground-truth** **C–S–H** structure, but a **map** of how **medium-range** **order** couples to **mechanical** **fingerprints** accessible through **nanoindentation**-derived observables.

## Methods

### Database construction (atomistic C–S–H realizations)

- The authors generate a **combinatorial library** of **calcium–silicate–hydrate (C–S–H)** atomistic configurations starting from a **crystalline tobermorite**-based molecular model (introduction excerpt), then explore **wide compositional** variation by **chain-cutting** / chemistry manipulations assisted by **empirical reactive potentials** as described in the article (not ReaxFF-specific in the van Duin sense—follow the paper’s force-field naming).

### Structural descriptors (three defect attributes)

1. **Ca/Si ratio** as a compositional index (**point-defect** loading in the silicate network; introduction).
2. Two **medium-range order** metrics based on **Si–O** and **Ca–O** environments, defined via **first sharp diffraction peak**-like correlation distances in partial structure factors (introduction excerpt).

### Mechanical evaluation

- Each library member is assigned **nanoindentation-mapped** **indentation modulus** **M** and **hardness** **H**, and the authors emphasize the ratio **M/H** as a diagnostic (abstract + introduction).

### Validation against experiments

- The study compares model ensembles to **SANS**, **INS**, **solid-state NMR**, **wavelength-dispersive spectroscopy**, **nanoindentation**, and **TEM** datasets from the literature and the authors’ labs (introduction excerpt).

### 3 — Static QM / DFT (supplementary to the atomistic database story)

This contribution is **not** framed as a standalone plane-wave DFT benchmark study on the opening pages. **Functional:** **N/A —** not consolidated in `normalized/extracts/2014qomi-nat-combinatorial-molecular_p1-2.txt` for the screening workflow. **Dispersion:** **N/A —** same excerpt scope. **Basis / k-sampling:** **N/A —** not stated in that excerpt. **Structures / pathways:** the indexed text describes a **tobermorite-derived** molecular starting point and **random chain cutting** (removing charge-neutral SiO\(_2\) groups) to span **C/S** from **1.1 to 2.1**, with **reactivity** handled through **empirical reactive potentials** during editing. **Properties computed for screening:** **indentation modulus** \(M\), **hardness** \(H\), and especially **\(M/H\)** as a mechanical fingerprint tied to the three defect descriptors (abstract + Results opening in the extract).

### 4 — Literature scope / validation (as reported)

The indexed introduction lists **model validation** comparisons against **SANS**, **INS**, **solid-state NMR**, **wavelength-dispersive spectroscopy**, **nanoindentation**, and **TEM** data from the literature and the authors’ own measurements—used to contextualize the **ensemble** of structures before combinatorial screening.

## Findings

**Outcomes and mechanisms.** Structural and mechanical observables **track the Ca/Si (C/S) ratio**, but the authors emphasize that **cross-correlating C/S with two medium-range-order correlation distances** (from Si–O and Ca–O partial structure factors, via the **first sharp diffraction peak** motif familiar from silica glasses) reveals an **extremum in the indentation modulus-to-hardness ratio \(M/H\)**, which they discuss by analogy to **optimum network connectivity** ideas from **glass** rheology (abstract; indexed Results transition).

**Comparisons.** The work positions the simulation database against the experimental techniques listed under **Methods** (indexed introduction), as part of gaining “**system-level properties of the ensemble**” before optimization screening.

**Sensitivity / design levers.** Screening is organized around **three defect attributes** (C/S plus the two correlation distances) and their coupling to **\(M/H\)**; the abstract frames this as a way to search for configurations with **desirable nanoscale mechanical** fingerprints.

**Limitations and outlook (authored framing).** The abstract stresses societal drivers (**concrete’s environmental footprint**) and a **combinatorial** route toward **specific stiffness or strength**; detailed caveats on model uniqueness and disorder appear in the full article and SI beyond the short extract.

**Corpus honesty.** This wiki section is grounded in **`pdf_path`** and **`normalized/extracts/2014qomi-nat-combinatorial-molecular_p1-2.txt`**; numerical tables, supplementary method steps, and any additional QC/DFT cross-checks must be taken from the **full PDF** rather than inferred here.

## Limitations

**C–S–H** **disorder** and **experimental variability** mean atomistic libraries are **idealized**; **descriptor** choices **bias** which structures are explored. This is **not** a **ReaxFF van Duin-group** paper—keep distinct from **reactive MD** cement studies elsewhere. **Nanoindentation-derived** **M/H** maps **local** **mechanics** and may **not** translate linearly to **macroscopic** **strength** without **microstructure** **statistics** reported in the primary study.

## Relevance to group

**Cement / C–S–H** atomistics sits adjacent to **oxide** and **geochemical** materials threads in the broader simulation literature represented here. While **not** a **van Duin ReaxFF** paper, it informs **structure–property** thinking for **silicate**-rich systems that interact with **reactive MD** studies of **hydration** and **interfaces** elsewhere in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1038/ncomms5960 — Nat. Commun. **5**, 4960; `papers/ReaxFF_others/MIT_team_Cement_Nature_Comm_2014.pdf`; extract `normalized/extracts/2014qomi-nat-combinatorial-molecular_p1-2.txt`.

## Related topics

- [[theme-water-silica-geo]]
