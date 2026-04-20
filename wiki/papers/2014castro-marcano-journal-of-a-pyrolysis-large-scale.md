---
id: paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale
type: paper
title: "Pyrolysis of a large-scale molecular model for Illinois no. 6 coal using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.jaap.2014.07.011"
year: 2014
authors:
  - "Fidel Castro-Marcano"
  - "Michael F. Russo Jr."
  - "Adri C. T. van Duin"
  - "Jonathan P. Mathews"
venue: "Journal of Analytical and Applied Pyrolysis 109 (2014) 79–89"
pdf_sha256: "bfcc61364bbeb8c3fd66c2504a560a29c305dae5ea4842ff988aa838fef56eaa"
pdf_path: "papers/Castro_JAAP_3246_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses large-scale MD to run high-temperature (2000 K) ReaxFF MD on a **>50,000 atom** molecular structural model of Illinois No. 6 coal—728 molecule diversity—over 250 ps to accelerate bond-breaking chemistry. Roughly 60% of cross-links break primarily by thermolysis in the simulation window, enabling analysis of devolatilization and structural transformation pathways for a complex organic geopolymer model relevant to utilization and emissions chemistry.

## Methods

- **Reactive MD:** ReaxFF for coal-like hydrocarbon/heteroatom chemistry at high T.
- **Model:** Large discrete molecular assembly representing coal macromolecular structure (prior construction by the Mathews group workflow).

## Findings

- Demonstrates feasibility of large-scale reactive pyrolysis with explicit molecular complexity beyond small-molecule benchmarks.
- Provides chemically detailed trajectories of cross-link scission and early product formation under extreme heating.

## Limitations

- Short simulated time vs laboratory heating rates; temperatures are elevated to access reactions within nanoseconds.
- Model fidelity depends on the underlying structural model and force-field transferability for sulfur/nitrogen/oxygen moieties present in coal.

## Relevance to group

Flagship **large-system ReaxFF pyrolysis** study tying geochemical/energy engineering (EMS Energy Institute) to reactive MD capabilities.

## Citations and evidence anchors

- DOI: [10.1016/j.jaap.2014.07.011](https://doi.org/10.1016/j.jaap.2014.07.011)
- Abstract: `normalized/extracts/2014castro-marcano-journal-of-a-pyrolysis-large-scale_p1-2.txt`

## Reader notes (navigation)

- **Cluster:** [[theme-pyrolysis-combustion-organics]]; cross-link to [[graphene-nanocarbon]] for sp² carbon themes.  
- **Frozen eval:** PYR1 gold in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
- Coal devolatilization and reactive MD at mesoscale atom counts
- ReaxFF for complex CHONS organics
