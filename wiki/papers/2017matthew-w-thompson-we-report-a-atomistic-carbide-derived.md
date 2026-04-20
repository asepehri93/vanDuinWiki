---
id: paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived
type: paper
title: "An atomistic carbide-derived carbon model generated using ReaxFF-based quenched molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - method:reaxff
  - task:method-development
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: null
year: 2017
authors:
  - "Matthew W. Thompson"
  - "Boris Dyatkin"
  - "Hsiu-Wen Wang"
  - "C. Heath Turner"
  - "Xiahan Sang"
  - "Raymond R. Unocic"
  - "Christopher R. Iacovella"
  - "Yury Gogotsi"
  - "Adri C. T. van Duin"
  - "Peter T. Cummings"
venue: "Carbon (MDPI)"
pdf_sha256: "3bbd9403704262f731450826a68a6d6fea098a44d5276db30166b38d0bd3be17"
pdf_path: "papers/Thompson_C_2017-proof.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The authors introduce **quenched MD** with **ReaxFF** to build **three-dimensional carbide-derived carbon (CDC)** models capturing **heterogeneous porosity** and **short-range graphitic order** beyond idealized **slit pore** geometries. **Radial distribution functions**, **pore size distributions**, and **adsorption** metrics are compared to **experiment**; **post-quench compression** adjusts **pore statistics** toward targets, and **ring statistics** emphasize abundant **non-hexagonal** rings in **CDC** vs conventional **activated carbon** scenarios. **Vanderbilt**/**Drexel**/**ORNL**/**van Duin** collaboration targets **supercapacitor** and **adsorption** modeling needs.

## Methods

- **Reactive force field** **MD** with **quench** schedules emulating **chlorine** **etching**-inspired carbon restructuring (parameterization details in paper).
- **Structural** and **adsorption** validation against **experimental** references cited internally.

<!-- enrich-from-extract:v2 -->

- These materials are heterogenous, non-ideal structures and include several important parameters that govern their performance.
- Therefore, a realistic model of the CDC structure is needed in order to study these systems and their nanoscale and macroscale properties with molecular simulation.
- We report the use of the ReaxFF reactive force ﬁeld in a quenched molecular dynamics routine to generate atomistic CDC models.
- We report a novel atomistic model of carbide-derived carbons (CDCs), which are nanoporous carbons with high speciﬁc surface areas, synthesis-dependent degrees of graphitization, and well-ordered, tunable porosities.
- These properties make CDCs viable substrates in several energy-relevant applications, such as gas storage media, electrochemical capacitors, and catalytic supports.


## Findings

- **CDC** models reproduce key **structural** signatures and respond physically to **compression** refinements.
- **Non-hexagonal** ring content is pronounced, potentially informing **electronic**/**capacitance** differences vs simpler nanoporous carbon models.

### Additional results (article abstract)

- Ring size distributions of this model demonstrate the prevalence of non-hexagonal carbon rings in CDCs.
- The pair distribution function, pore size distribution, and adsorptive properties of this model are reported and corroborated with experimental data.
- Simulations demonstrate that compressing the system after quenching changes the pore size distribution to better match the experimental target.
- These effects may contrast the properties of CDCs against those of activated carbons with similar pore size distributions and explain higher energy densities of CDC-based supercapacitors.


## Limitations

- **DOI** not captured in local manifest metadata—resolve from the **journal issue** when wiring bibliographic automation.

## Relevance to group

**van Duin** contributes **ReaxFF** expertise to **nanoporous carbon** structure generation for **energy** materials.

## Citations and evidence anchors

- Source PDF: `papers/Thompson_C_2017-proof.pdf` (proof; confirm **final** **DOI** via publisher metadata).

## Related topics

- [[reaxff-family]]
