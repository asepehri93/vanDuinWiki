---
id: paper:2022sengul-physical-che-atomistic-level
type: paper
title: "Atomistic level aqueous dissolution dynamics of NASICON-type Li1+xAlxTi2−x(PO4)3 (LATP)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - material:ceramic-electrolyte
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP05360D"
year: 2022
authors:
  - "Mert Y. Sengul"
  - "Arnaud Ndayishimiye"
  - "Wonho Lee"
  - "Joo-Hwan Seo"
  - "Zhongming Fan"
  - "Yun Kyung Shin"
  - "Enrique D. Gomez"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. 24, 4125–4130 (2022)"
pdf_sha256: "865dc85389a4fb64fc2eb2b2f310baa4c6f9d17cb7ed33e8931f1557a32ee62f"
pdf_path: "papers/Sengul_NASICON_PCCP_2022.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2022sengul-physical-che-atomistic-level -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Combined **ReaxFF MD** and **experiment** study of **aqueous dissolution** at the **LATP (NASICON-type Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\)) / water** interface, motivated by **cold sintering** and other **solution-adjacent processing** routes where **incongruent dissolution** complicates densification. Atomistic trajectories support a **sequential** process: rapid **Li leaching**, phosphate-linked rearrangements, and evolution toward **Ti-rich secondary products** as dissolution advances—framed as a template mechanism class for **multicomponent ceramic electrolytes** exposed to water.

## Methods

Experimental cold-sintered **LATP** samples paired with **ReaxFF** simulations of the solid/water interface; iterative comparison between observation and simulation (per article structure).

## Findings

Dissolution is not a simple uniform ion release: **phosphate removal** destabilizes the NASICON framework; **Li** exits early (common to NASICON types); subsequent **polymerization/condensation** chemistry among **AlO\(_x\)** and **PO\(_4\)**-derived species gates rate and triggers **secondary phase** formation; overall picture is **sequential** and strongly pathway-dependent.


## Limitations

Specific surface orientation, pH, and electrochemical bias in real devices extend beyond a single interface model; quantitative dissolution rates require careful calibration to experiment and thermodynamic databases.

## Relevance to group

Direct **ReaxFF + ceramic electrolyte** interface work tied to **PSU materials** collaborations and broader **battery processing** themes in the corpus.

## Citations and evidence anchors

https://doi.org/10.1039/D1CP05360D — Communication (~pp. 1–2) states sequential mechanism and Li/PO\(_4\) arguments.

## Related topics

- [[reaxff-family]]
