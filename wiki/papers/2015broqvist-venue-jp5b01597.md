---
id: paper:2015broqvist-venue-jp5b01597
type: paper
title: "ReaxFF force-field for ceria bulk, surfaces, and nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - task:validation
  - material:oxide
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jpcc.5b01597"
year: 2015
authors:
  - "Peter Broqvist"
  - "Jolla Kullgren"
  - "Matthew J. Wolf"
  - "Adri C. T. van Duin"
  - "Kersti Hermansson"
venue: "Journal of Physical Chemistry C 2015, 119, 13598–13609"
pdf_sha256: "f47c87db7068a1d0d403e819f072d9267d392a7103a197374904810083b05744"
pdf_path: "papers/Broqvist_Ceria_JPC_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015broqvist-venue-jp5b01597 -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Broqvist *et al.* introduce a **ReaxFF** parametrization for **CeO\(_2\)** and **CeO\(_{2-x}\)** trained predominantly from **PBE+U** reference data, targeting **oxygen chemistry** in **bulk**, **extended surfaces**, **surface steps**, and **nanoparticles**. Validation claims in the abstract include reproduction of **bulk moduli**, **lattice parameters**, and **surface energies** for stoichiometric systems; **step energies** on **(111)**; **vacancy formation energies** and their **depth dependence** from **(110)** and **(111)** surfaces upon reduction; and **energy orderings** among stoichiometric **tetrahedral, octahedral, and cubic** nanoparticle motifs plus partially reduced **octahedra**. The study position the model as a practical complement to costly **QM dynamics** for **redox** problems on ceria.

## Methods

- **DFT (PBE+U)** training set generation across bulk, surface, step, and nanoparticle configurations.
- **ReaxFF** functional form with EEM-style charges and bond-order energy partitioning (Eq. (1) in the paper).

## Findings

- Emphasis on **oxygen vacancy** energetics and **reduction**-driven reconstructions rather than fixed-charge shell models that cannot change **oxidation state character** dynamically.


## Limitations

- **Ce 4f** physics is only captured empirically; users must validate for each new **surface orientation** or **dopant** scenario beyond the training envelope.
- Strongly correlated electron errors may appear for **non-training** Ce environments.

## Relevance to group

**Adri C. T. van Duin** co-authorship; expands the **ReaxFF oxide/redox** portfolio for **ceria**, widely used in **catalysis** and **energy** materials simulations.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5b01597](https://doi.org/10.1021/acs.jpcc.5b01597)

## Related topics

- [[reaxff-family]]