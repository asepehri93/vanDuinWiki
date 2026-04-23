---
id: paper:2017zhang-venue-microsoft-word
type: paper
title: "Supporting information: Second-generation ReaxFF water force field (parameters and citation notes)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - domain:water-silica-geo
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Supporting information (ACS)"
pdf_sha256: "60c4af2bb3a283755b9e9f2af6353beaed839926b12908564c0e194e87ef9ed5"
pdf_path: "papers/Zhang_ReaxFF_water_JPCC_2017_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017zhang-venue-microsoft-word -->

!!! note "Non-primary PDF"

    This ingest is the **supporting information** PDF for the second-generation ReaxFF water model. The standalone article narrative, validation against experiment, and discussion belong under **`[[2017zhang-venue-research]]`**. This file is listed in the maintainer catalog of SI-primary ingests (`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`, section A).

## Summary

Supporting information for “Second-Generation ReaxFF Water Force Field: Improvements in the Description of Water Density and OH-Anion Diffusion” provides **complete ReaxFF parameter tables** for the second-generation (2017) water model, ancillary reference material (including completion of selected bibliography entries as noted in the SI), and any additional numerical inputs required to reproduce simulations reported in the parent **J. Phys. Chem. C** article. The SI does not replace the main paper for scientific interpretation: it is a **machine- and human-readable appendix** for deploying the published parameterization in LAMMPS or compatible codes.

Downstream users typically need three coordinated artifacts: (i) **parameter** blocks for **bond**, **angle**, **torsion**, and **van der Waals** terms as used by the group’s **ReaxFF** implementation; (ii) **charge** **equilibration** settings consistent with the parent publication; and (iii) any **training** or **validation** geometries referenced when auditing the fit. This SI focuses on (i) and supporting bibliography completeness, while **`[[2017zhang-venue-research]]`** carries the narrative validation against **experiment** and **QM**.

## Methods

**Document role.** This **Supporting Information** **PDF** (`papers/Zhang_ReaxFF_water_JPCC_2017_SI.pdf`) archives complete **ReaxFF** parameter blocks for the **second-generation water-2017** model; scientific **protocol** narrative, **validation** metrics, and discussion live in **`[[2017zhang-venue-research]]`**.

**Molecular dynamics (deployment context).** Production **ReaxFF molecular dynamics** benchmarks in the parent article use **LAMMPS**-style inputs with **periodic** bulk-water **supercells** containing thousands of **atoms**, **NVT** (or related **canonical**) **thermostat** control near **300 K**, **femtosecond** integration **timesteps**, and multi-**nanosecond** **production** segments after **equilibration**—exact strings appear in the **J. Phys. Chem. B** **Methods**/**SI** cross-refs rather than in this coefficient listing. **Barostat** usage, if any density-scans employ **NPT**, is likewise documented on the parent page. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** introduced by this **SI** file itself.

**Force-field training (SI tables).** The **SI** tabulates optimized **bond**, **angle**, **torsion**, and **van der Waals** parameters plus **charge equilibration** metadata for **water-2017**, constituting the machine-readable **training** output that accompanies the parent **parameter optimization** narrative.

**Static QM / DFT.** **N/A —** **DFT** **training** details (functional, **basis set**, **k-point** mesh) are summarized on **`[[2017zhang-venue-research]]`**, not duplicated inside every **SI** table.

**Review scope.** **N/A —** **non-primary** **SI** artifact per `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

## Findings

**Outcomes.** The **SI** is the authoritative source for **numerical coefficients** needed to reproduce **water-2017** **ReaxFF** **MD** in **LAMMPS**; it does not independently report new **mechanistic** conclusions.

**Comparisons / validation.** Claims about **density**, **diffusivity**, and **acid/base** **reaction** behavior **versus** **experiment** belong to **`[[2017zhang-venue-research]]`**, which cites the **benchmark** data used during **parameter optimization**.

**Sensitivity / design levers.** Users deploying these tables must still match **cutoffs**, **QEq** refresh policies, and **composition** (**pH**, ionic **concentration**) to the parent **Methods** or risk drifting from published **validation**.

**Limitations / outlook.** Filename artifacts (“Microsoft Word …”) do not change scientific authority—always pair this **PDF** with the **journal DOI** from the parent article for bibliographic **integrity**.

**Corpus honesty.** **SI-only** ingest: treat this slug as **coefficient** storage; cite **`[[2017zhang-venue-research]]`** for prose, figures, and **experimental** agreement statements.
## Limitations

The filename reflects a publisher or author export artifact (“Microsoft Word …”); scientific authority is the **combined** main article + SI. For citations in external documents, prefer the **journal article DOI** from **`[[2017zhang-venue-research]]`**, not this PDF alone.

## Relevance to group

Archives parameters for the group’s ReaxFF aqueous and proton-transfer line used across corrosion, electrochemistry, and electrolyte modeling.

## Citations and evidence anchors

- Parent article: **`[[2017zhang-venue-research]]`** (version-of-record narrative and DOI).
**SI-only.** Deploy water-2017 parameters from this PDF together with `[[2017zhang-venue-research]]` for validation metrics and discussion.

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Curation hygiene.** After substantive edits to this wiki page, Phase 5 chunk identifiers are refreshed by running `python3 scripts/build_chunks.py` from the repository root so `indexes/chunks.jsonl` stays aligned with section headings and body text. The `updated` field in front matter records the last wiki revision date for operator review.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
