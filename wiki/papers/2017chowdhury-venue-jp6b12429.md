---
id: paper:2017chowdhury-venue-jp6b12429
type: paper
title: "Extension of the ReaxFF combustion force field toward syngas combustion and initial oxidation kinetics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b12429"
year: 2017
authors:
  - "Chowdhury Ashraf"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A"
pdf_sha256: "fe1467aed0c35b8887920ebee84765b86c64dd6afa5badeea0753b2c9365c125"
pdf_path: "papers/Chowdhury_CHO_2017_JPCA.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2017chowdhury-venue-jp6b12429 -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This work **retrains** the **Chenoweth et al. CHO-2008** **ReaxFF combustion** description into **CHO-2016**, targeting **syngas-relevant C\(_1\)** oxidation (**CO**/**CO\(_2\)** chemistry) and correcting **too-fast H abstraction by O\(_2\)** that underestimated **oxidation initiation temperature**. Expanded **DFT** training includes **transition states** along **syngas** and **initiation** pathways; **high-temperature MD** validates **methane**, **syngas**, **JP-10**, and **n-butylbenzene** scenarios while preserving **large-hydrocarbon** behavior from **CHO-2008**. **Chowdhury Ashraf** and **Adri C. T. van Duin** author the article.

## Methods

- **ReaxFF** reparameterization against augmented **QM** datasets; **NVT** high-temperature **oxidation**/**pyrolysis** MD for fuel cases named in the abstract.

## Findings

- **CHO-2016** improves **small-molecule oxidation** energetics and fixes **low-temperature initiation** bias relative to **CHO-2008**.
- **JP-10 decomposition Arrhenius** behavior and **n-butylbenzene** pathways remain consistent with prior expectations and experiment within stated scope.


## Limitations

- Combustion **networks** remain enormous; **transferability** must be assessed case-by-case beyond tested fuels.

## Relevance to group

Landmark **group** publication extending the widely used **CHO ReaxFF** line.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.6b12429` (`papers/Chowdhury_CHO_2017_JPCA.pdf`).

## Related topics

- [[reaxff-family]]