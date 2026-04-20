---
id: paper:2013russo-venue-jp403511q
type: paper
title: "Combustion of 1,5-Dinitrobiuret (DNB) in the Presence of Nitric Acid Using ReaxFF Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp403511q"
year: 2013
authors:
  - "Russo, Michael F., Jr."
  - "Bedrov, Dmitry"
  - "Singhai, Shashank"
  - "van Duin, Adri C. T."
venue: "Journal of Physical Chemistry A"
pdf_sha256: "604b4ccd14967c07a850dfd7bdd29d87a1cdf343123b9e62af8da80e53bc3059"
pdf_path: "papers/Russo_DNB_HNO3_JPCA_2013.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2013russo-venue-jp403511q -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

ReaxFF reactive MD explores DNB/nitric acid mixtures at 0.5 and 1.0 g/mL to connect atomistic pathways to hypergolic ignition chemistry. Additional QM-driven reparameterization targets DNB dissociation channels and the DCA→DNB formation sequence; certain compositions show a sharp exothermic runaway interpreted as spontaneous ignition (abstract; Introduction; computational methods opening, extract).

## Methods

Extensions to an existing C/H/O/N hypergolic ReaxFF database with new training on Jaguar B3LYP/6-311G** reaction energies for DNB fragmentations and intermediate formation. Temperature-ramp tests on single DNB molecules up to 4000 K; mixture boxes with 18/18 and 37/37 molecules at two densities, plus fuel-rich variants sketched in methods (extract pages 1–2).

## Findings

After training, ReaxFF matches QM reaction energies within several kcal/mol for most DNB steps; terminal NO₂ loss dominates high-temperature single-molecule decomposition. Mixture simulations motivate composition-dependent “sharp” energy release associated with hypergolic behavior (abstract; methods excerpt).


## Limitations

Shock/ignition chemistry is extremely sensitive to model and initial geometry; high-temperature ramp protocols are not experimental drop-test conditions.

## Relevance to group

Demonstrates iterative ReaxFF extension for nitrogen-rich energetic/ionic-liquid chemistry led from Penn State MNE.

## Citations and evidence anchors

- J. Phys. Chem. A 2013, 117, 9216–9223; DOI `10.1021/jp403511q` (extract page 2 footer).
- Abstract and force-field development paragraph (extract pages 1–2).

## Related topics

- [[reaxff-family]]
