---
id: paper:2016npjcompumats201511-venue-untitled
type: paper
title: "The ReaxFF reactive force-field: development, applications, and future directions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:review
  - domain:methods-software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1038/npjcompumats.2015.11"
year: 2016
authors:
  - "Thomas P. Senftle"
  - "Sungwook Hong"
  - "Md Mahbubul Islam"
  - "Sudhir B. Kylasa"
  - "Yuanxia Zheng"
  - "Yun Kyung Shin"
  - "Chad Junkermeier"
  - "Roman Engel-Herbert"
  - "Michael J. Janik"
  - "Hasan Metin Aktulga"
  - "Toon Verstraelen"
  - "Ananth Grama"
  - "Adri C. T. van Duin"
venue: "npj Comput. Mater."
pdf_sha256: "11c70284ea984b327048cb49e17b1eed5ce41582e579a3178c5b13092226076d"
pdf_path: "papers/NPJCOMPUMATS201511.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016npjcompumats201511-venue-untitled -->

Community review of the ReaxFF reactive force field: formalism, parameterization culture, software ecosystem, and cross-domain applications led by van Duin and collaborators.

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This *npj Computational Materials* article (DOI `10.1038/npjcompumats.2015.11`) is the widely cited community overview of ReaxFF co-led by van Duin with a large multi-institution author list: it synthesizes the reactive force-field formalism (bond-order-dependent valence and penalties, nonbonded terms, variable charge treatments), QM-driven parameterization practice, software and HPC coupling, and representative application domains from catalysis through degradation, combustion-related chemistry, and electrochemical interfaces. Some corpus ingests of `papers/NPJCOMPUMATS201511.pdf` carry noisy text extraction; cite the publisher **PDF/HTML** for clean section numbering, figures, and SI pointers.

## Methods

As a **review**, the manuscript’s “methods” are bibliographic and pedagogical: milestones in ReaxFF development, the bond-order energy expression and charge models (including QEq-style treatments), workflows for training against QM data, validation culture, and software coupling to community MD engines such as LAMMPS where the article discusses them. It does not center on one new production MD trajectory, one new public parameter release, or one new static QM benchmark as primary authored data—worked examples point to cited primary papers for timesteps, ensembles, system sizes, and training details.

## Findings

The review explains how bond-order reactive models enable large-scale reactive MD, surveys application domains and recurring successes in complex materials chemistry, and records limitations around subset transferability and accuracy versus QM or experiment for selected barriers and energies. Outlook material in the published text discusses trends such as tighter QM coupling in fitting, faster integrators and hardware-aware implementations, and extensions like eReaxFF for explicit carriers; quantitative statements should be taken from the publisher version-of-record and its references, not from the query-form PDF text sometimes ingested for this slug.

## Limitations

High-level synthesis: any specific element subset or application still requires the cited primary parameterization and validation papers. The corpus copy tied to this slug may be a pre-layout or query-heavy PDF; prefer the publisher version-of-record for pagination and figures.

## Relevance to group

Flagship **outreach and onboarding** document for the **ReaxFF ecosystem** directly tied to **Penn State leadership**.

## Citations and evidence anchors

- Canonical article **DOI:** `10.1038/npjcompumats.2015.11`; ingested bytes at `papers/NPJCOMPUMATS201511.pdf` (SHA-256 in frontmatter).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

Prefer publisher HTML/PDF for clean pagination when citing sections.
