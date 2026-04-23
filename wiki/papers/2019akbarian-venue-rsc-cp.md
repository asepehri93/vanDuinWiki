---
id: paper:2019akbarian-venue-rsc-cp
type: paper
title: 'Understanding the influence of defects and surface chemistry on ferroelectric
  switching: a ReaxFF investigation of BaTiO3 (publisher proof PDF)'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:ferroelectrics-polar
- domain:reactive-md
- method:reaxff
- task:application
- material:perovskite-oxide
paper_keywords:
- keyword:reaxff-application
- keyword:oxide-surface
- keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: 10.1039/C9CP02955A
year: 2019
authors:
- Dooman Akbarian
- Dundar E. Yilmaz
- Ye Cao
- P. Ganesh
- Ismaila Dabo
- Jason Munro
- Renee Van Ginhoven
- Adri C. T. van Duin
venue: Phys. Chem. Chem. Phys. (proof PDF in corpus)
pdf_sha256: 6285bd6b86169731849325f8a0490c59753d2653a211b17964c88e960cc8e278
pdf_path: papers/Akbarian_PCCP_BaTiO3_2019_proof.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2019akbarian-venue-rsc-cp -->

## Summary

This wiki slug points at an RSC *Phys. Chem. Chem. Phys.* **publisher proof** PDF (`Akbarian_PCCP_BaTiO3_2019_proof.pdf`) for the same article as DOI [10.1039/C9CP02955A](https://doi.org/10.1039/C9CP02955A). The peer-reviewed work develops an extensible atomistic ReaxFF for BaTiO₃ that captures field- and temperature-driven ferroelectric hysteresis together with effects of surface chemistry and bulk oxygen vacancies. Simulations are connected to experimental themes discussed in the paper, including a critical thickness near **4.8 nm** below which ferroelectricity is suppressed, reductions in polarization and Curie temperature when vacancies migrate and cluster, and domain-wall interactions with surfaces that alter switching pathways—see the **version-of-record** page `[[2019akbarian-physical-che-understanding-influence]]` for authoritative wording and pagination. Maintainers should treat this slug as a duplicate stream for bibliographic provenance, not as the canonical text for quotations. Duplicate PDFs are common in publisher workflows; this entry documents one such stream explicitly.

## Methods

This slug is **bibliographic provenance** for an RSC **publisher proof** PDF (`papers/Akbarian_PCCP_BaTiO3_2019_proof.pdf`) of the same article as DOI `10.1039/C9CP02955A`. For **tabulated simulation settings** (integrator, timestep, thermostat/barostat, supercell sizes, field ramps, production lengths), treat the **version-of-record** article PDF and Methods/SI as authoritative; proof exports can reorder pages and should not be the only source for copy/paste input decks.

**MD application (ReaxFF, BaTiO₃ ferroelectrics).** The peer-reviewed study uses **ReaxFF** reactive MD to treat **field- and temperature-driven polarization switching** in **BaTiO₃**, including **bulk oxygen vacancies** and **surface** chemistry effects discussed in the article (see **`[[2019akbarian-physical-che-understanding-influence]]`** for the corpus “reading copy”). **Engine / code:** **N/A — not extracted** from the proof PDF text layer on this curation pass; confirm any explicit code naming on the VOR page/PDF. **System size & composition:** **N/A — not re-tabulated** from this proof stream; supercell stoichiometry and atom counts are on the VOR **Methods**/**SI**. **Boundaries / periodicity:** the published ferroelectric supercells use **3D periodic boundary conditions (PBC)** as usual for bulk polar switching; any slab-like variants or fixed layers—**N/A to quote here**—are specified on the VOR article. **Ensemble:** constant-temperature **MD** (**NVT**-class integration is typical for the reported ramps; confirm label and thermostat on the VOR page). **Timestep, duration/stages, barostat, pressure, electric field, enhanced sampling:** **N/A — not re-tabulated here**; import integrator timestep, equilibration/production spans, and field protocols from the VOR **Methods**/**SI** rather than this proof PDF.

**Force-field training.** The article develops an extensible **BaTiO₃**-focused **ReaxFF** parameterization tied to **QM training** benchmarks and experimental anchors summarized on **`[[2019akbarian-physical-che-understanding-influence]]`**. **N/A — training tables and optimizer call-outs** are not duplicated on this proof-ingest page.

**Static QM.** **N/A — not the dominant Methods block** for this publication relative to the reactive MD ferroelectric study; any static **DFT** references should be followed from the VOR article’s training/validation discussion.
## Findings

Mechanistic conclusions about vacancy–domain-wall–surface coupling and switching behavior are summarized on the primary wiki page cited above; this proof ingest should not be used when page-level citation to the final article is required. Substantive scientific findings are not duplicated here in full to avoid divergence from the VOR wording; use the sibling page for thesis-quality citations. Automated ingest pipelines should map both SHA variants to the same DOI to prevent duplicate bibliographic entries in downstream indices. For scientific substance, the reader should rely on `[[2019akbarian-physical-che-understanding-influence]]` for figure-quality reproduction of polarization–field loops, vacancy formation energies, and surface termination comparisons, because those quantitative panels may render differently in proof exports. The proof PDF remains valuable for provenance audits showing what the group ingested on a particular date even after the VOR file replaces it in workflows. External readers discovering this slug first should follow the sibling page for polar–field hysteresis plots and vacancy migration narratives.

## Limitations

Proof PDFs can differ subtly from the version of record; prefer `papers/Akbarian_PCCP_BaTiO3_2019.pdf` via the sibling slug for stable corpus reference.

## Relevance to group

Perovskite ferroelectrics with ReaxFF; van Duin-group co-authorship documented on the primary note.

## Citations and evidence anchors

- DOI: [10.1039/C9CP02955A](https://doi.org/10.1039/C9CP02955A)

## Reader notes (navigation)

- Primary article page: [[2019akbarian-physical-che-understanding-influence]]  
- Theme: [[theme-ferroelectrics-polar-oxides]], [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[2019akbarian-physical-che-understanding-influence]]
