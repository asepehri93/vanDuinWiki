---
id: paper:2021jwinetrout-venue-paper
type: paper
title: "Implementing Reactivity in Molecular Dynamics Simulations with the Interface Force Field (IFF-R) and Other Harmonic Force Fields"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:classical-ff-specialized
  - domain:methods-software
  - method:reactive-md-generic
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2021
authors:
  - "Jordan J. Winetrout"
  - "Krishan Kanhaiya"
  - "Geeta Sachdeva"
  - "Ravindra Pandey"
  - "Behzad Damirchi"
  - "Adri van Duin"
  - "Gregory Odegard"
  - "Hendrik Heinz"
venue: "Archived preprint / conference manuscript in corpus (IFFR_archived_2021.pdf)"
pdf_sha256: "d79c0ed9a9b94d0cb7943b28a1877fbc576369bb6a75decb4aaab3b9e37dda27"
pdf_path: "papers/IFFR_archived_2021.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2021jwinetrout-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Introduces **IFF-R**, a reactive extension of the Interface Force Field where harmonic bond terms are replaced by **Morse** potentials so bonds can break with prescribed dissociation energies—aiming at fracture and chemistry-aware MD without full ReaxFF expense. The manuscript claims ~50× speed over ReaxFF in their comparisons while retaining IFF-compatible nonreactive properties, and illustrates metals (Fe), ceramics (carbon nanotubes), and polymers (PAN, cellulose Iβ) with parameters anchored to experiment or MP2.

## Methods

Morse-bond reactive scheme on top of IFF; demonstration MD for stress–strain to failure and bond-breaking analytics; parameter recipes for common bond types.

## Findings

Reported agreement for structures, surface energies, moduli, and strengths versus available references in the document; positions IFF-R as a lighter alternative when full bond-order reactive models are unnecessary.

## Limitations

Not a ReaxFF paper—chemistry is constrained to how Morse bond breaking is parameterized; archived venue PDF—verify final bibliographic details if citing externally.

## Relevance to group

van Duin listed among authors; useful contrast case for when reactive FFs differ (IFF-R vs ReaxFF families).

## Citations and evidence anchors

`papers/IFFR_archived_2021.pdf` — abstract and author list.

## Related topics

- [[reaxff-family]]
