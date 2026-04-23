---
id: concept:theme-ferroelectrics-polar-oxides
type: concept
title: "Theme: ferroelectrics and polar perovskite oxides (corpus)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2024baksa-adv-elect-ma-strain-fluctuations"
    note: "BaZrO3 elastic constants and strain-fluctuation workflow with a neural network potential."
  - paper_id: "paper:2023roshan-venue-paper"
    note: "Perovskite and high-temperature oxide mechanics context in the corpus."
  - paper_id: "paper:2025krstic-venue-paper"
    note: "Additional high-temperature oxide behavior and transferability context."
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Reactive electrolyte and oxide chemistry overlap relevant to adjacent polar-oxide questions."
supported_by:
  - "paper:2024baksa-adv-elect-ma-strain-fluctuations"
  - "paper:2023roshan-venue-paper"
  - "paper:2025krstic-venue-paper"
  - "paper:2018shin-physical-che-development-reaxff"
---

<!-- id:concept:theme-ferroelectrics-polar-oxides -->

!!! abstract "TL;DR"

    This corpus theme tracks polar perovskites and related functional oxides where atomistic simulations are used to interpret elastic, thermal, and defect-linked behavior. The center of gravity is ABO3-like systems and electromechanical interpretation, while oxide chemistry links are intentionally cross-referenced to adjacent hubs.

## Scope (in / out)

In scope for this hub are corpus pages on BaZrO3 elasticity, perovskite high-temperature mechanics, and nearby oxide studies that are explicitly tagged `domain:ferroelectrics-polar`.

Out of scope are silica-first and non-perovskite ceramic narratives unless a paper page explicitly establishes a bridge that is documented through linked theme pages.

## How this theme is organized in the corpus

The current corpus separates this theme into three practical lanes: elasticity-focused atomistics for BaZrO3, broader perovskite or high-temperature oxide mechanics pages, and adjacent electrolyte-interface chemistry where polar-oxide environments matter but bulk ferroelectric switching is not the primary target.

## Literature review (this knowledge base)

This section is a corpus-scoped synthesis rather than a complete field review. Detailed equations, simulation controls, and article-level evidence are retained on each linked `[[paper-slug]]` page.

### Elastic properties and strain fluctuations

[[2024baksa-adv-elect-ma-strain-fluctuations]] is the clearest corpus anchor for strain-fluctuation evaluation of elastic constants in BaZrO3 using a neural network potential. Within this hub, it is the main evidence pathway connecting polar-oxide mechanics to [[theme-ml-atomistic-potentials]].

### High-temperature mechanics and perovskite oxides

[[2023roshan-venue-paper]] and [[2025krstic-venue-paper]] provide the corpus backbone for high-temperature perovskite and oxide mechanics. These pages are most useful for clarifying whether a result is interpreted through ferroelectric ordering physics or through more general mechanical and thermal response.

### Electrolytes and polar oxide chemistry (adjacent)

[[2018shin-physical-che-development-reaxff]] contributes adjacent evidence where reactive electrolyte chemistry intersects oxide environments. In this hub, that paper functions as a boundary case tied to [[batteries-interfaces-reaxff]] rather than as direct evidence for bulk ferroelectric switching behavior.

## Analysis and cross-cutting patterns

Across these pages, one recurring pattern is methodological heterogeneity: elasticity-oriented analysis can leverage ML potentials, while neighboring perovskite and oxide studies may rely on classical or multiscale formulations. As a result, cross-paper comparisons should be framed as conditional and should only claim overlap that is explicitly supported in each source page.

## Debates, tensions, and limitations

A practical tension in this corpus is how confidently anharmonic and soft-mode behavior can be compared across model families, especially when one page uses a neural network potential and another uses a different force-field lineage or simulation stack. A second limitation is topical balance: the current corpus appears richer for mechanics and thermal response than for domain-wall-resolved switching pathways, so retrieval answers should avoid implying complete coverage of ferroelectric switching mechanisms.

This theme also inherits a scope boundary from adjacent hubs. Oxide-reactivity and interface chemistry can be scientifically relevant here, but those questions are often better resolved through [[theme-oxides-silica-ceramics]] or battery-interface pages unless the polar-oxide linkage is directly discussed in the cited paper notes.

## Gaps and open directions (corpus view)

From a corpus-management perspective, the largest gap is thin direct coverage of atomistic switching pathways and domain-wall kinetics relative to elasticity and high-temperature mechanics. A useful next direction is to ingest or elevate papers that explicitly connect polarization switching observables to the same material classes already represented in the mechanics-focused subset.

## Methods and limitations

Method interpretation should remain conservative when moving between pages. Elastic workflows based on small cells or near-harmonic assumptions may underrepresent soft-mode behavior near phase transitions, and cross-method agreement should not be assumed without explicit validation in the underlying paper note.

For polarization-linked interpretation, atomistic observables and continuum ferroelectric quantities are not always directly interchangeable. Retrieval and synthesis should therefore state which quantity each paper actually reports and avoid overextending conclusions across incompatible definitions.

## Representative entry points

Readers starting with elasticity and ML-enabled atomistics should begin at [[2024baksa-adv-elect-ma-strain-fluctuations]]. For broader perovskite and high-temperature mechanics context, [[2023roshan-venue-paper]] and [[2025krstic-venue-paper]] are the primary corpus entry points. For discovery across this tag family, the domain index at [[paper-index-by-domain]] under `domain:ferroelectrics-polar` remains the best navigation spine.

??? info "MAS / retrieval"

    **id:** `concept:theme-ferroelectrics-polar-oxides`. When new perovskite papers are ingested, tag `domain:ferroelectrics-polar` and add a bullet here if the theme narrative should cite them.
