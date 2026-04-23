---
id: paper:2013poovathingal-venue-research
type: paper
title: "Large scale computational chemistry modeling of the oxidation of highly oriented pyrolytic graphite (galley PDF)"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp3125999"
year: 2013
authors:
  - "Savio Poovathingal"
  - "Thomas E. Schwartzentruber"
  - "Sriram Goverapet Srinivasan"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "8f4477153f07e618a6da3735935fd8c933dbc5da2072718f3c611455de3bdcc9"
pdf_path: "papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013poovathingal-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    This note registers a **galley/proof PDF** for the same JPCA article summarized on [[2013poovathingal-venue-jp3125999]]. Scientific content should be taken from the **version-of-record** page unless you explicitly need this file’s line breaks or figures.

## Summary

Same study as [[2013poovathingal-venue-jp3125999]]: ReaxFF molecular dynamics of hyperthermal atomic oxygen (5 eV) oxidizing HOPG, predicting etch-pit evolution, product distributions (O\(_2\) > CO\(_2\) > CO), and pathway activation energies (about 0.30 / 0.52 / 0.67 eV for O\(_2\), CO\(_2\), CO channels in the analysis presented). This wiki entry tracks the **galley** PDF bytes ingested in the corpus; narrative **science** should match the **version-of-record** page, while this file remains useful for **provenance** when comparing **figure** placement or **pagination** against proofs.

## Methods

This slug tracks the **galley/proof** bytes at `papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013_galley.pdf`. The **scientific protocol** is the same article as [[2013poovathingal-venue-jp3125999]]; use that page’s **`pdf_path`** for **pagination-stable** Methods tables and figures when possible.

### 1 — MD application (same study; galley PDF provenance)

- **Engine / code:** **Large-scale molecular dynamics** with **ReaxFF** implemented in **LAMMPS** (same article Methods as [[2013poovathingal-venue-jp3125999]]; read `papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013.pdf` when galley `pdf_path` text is hard to extract reliably).
- **System size & composition:** **HOPG** is modeled as a **bulk hexagonal graphite slab** with **ABAB stacking**, a **frozen bottom layer**, **Langevin**-controlled **substrate layers** to mimic bulk dissipation, and an **oxygen atom** beam initialized **15 Å** above the surface with **5 eV** normal kinetic energy for sequential impacts (VOR Methods). Isolated small models in the same article discuss defect energetics on the order of **100–3000 atoms** (VOR PDF text).
- **Boundaries / periodicity:** **Three-dimensional periodic boundary conditions** in **LAMMPS** supercells as described in the VOR Methods (paired PDF).
- **Ensemble:** The **1 ps** high-energy **O-atom collision** integrations use **velocity-Verlet** with **0.25 fs** timesteps and explicitly checked **energy conservation** in the Methods text (paired PDF), i.e., effectively **microcanonical** dynamics for those collision legs, while selected **substrate layers** use **Langevin** thermostatting to represent bulk coupling (paired PDF).
- **Timestep:** **0.25 fs** with **velocity-Verlet** integration (VOR Methods).
- **Duration / stages:** The Methods describe **1 ps** integration for initial high-energy collisions under low-pressure experimental separation assumptions, with longer **sequential-collision** campaigns described later in the article (paired PDF).
- **Thermostat:** **Langevin** thermostat on selected **substrate layers** (paired PDF figure/methods caption as referenced in the article).
- **Barostat:** N/A — not the primary control mode for the quoted collision protocol (paired PDF).
- **Temperature:** Large-scale sequential-collision runs sample **surface temperatures** of **300, 600, 1000, and 1500 K** (broader than the **298–573 K** experimental window, which the authors note is too narrow for MD statistics) (`papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013.pdf`, Results discussion excerpt).
- **Pressure:** N/A — beam-energy-controlled oxidation scenario (abstract framing).
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — **application/validation** of **C/H/O ReaxFF** with **QM benchmark checks** as summarized in the shared abstract (see [[2013poovathingal-venue-jp3125999]]).

## Findings

- **Outcomes & mechanisms:** Same abstract-level results as [[2013poovathingal-venue-jp3125999]]: **oxygen precursor**, **etch pits**, **edge-localized carbon removal**, **O\(_2\) > CO\(_2\) > CO** product ranking, and pathway **E_a** values **~0.30 / 0.52 / 0.67 eV** for the dominant channels discussed there.
- **Comparisons:** **Versus molecular-beam experiments** and **ab initio-derived energetics checks** as in the shared article narrative.
- **Sensitivity / design levers:** **Beam energy (5 eV)** and **sequential-impact** large-cell protocol are the main knobs highlighted in the abstract/intro shared across PDF variants.
- **Limitations & outlook:** **Galley/proof** formatting can differ in **line breaks/figure placement**; for citation-ready locators and SI pointers, prefer **version-of-record** ingest [[2013poovathingal-venue-jp3125999]].
- **Corpus honesty:** This wiki entry is intentionally **duplicate PDF provenance**; do not treat this file as an independent scientific source beyond what matches the **VOR** page.

## Limitations

Proof/galley formatting; prefer the non-galley PDF for citation-ready pagination when available. **Hyperthermal** **atomic** **oxygen** **beams** in experiment can include **energy** **spread** and **angular** **distributions** that differ from the **idealized** **single-energy** **impacts** used for **comparability** in the MD protocol. **Surface** **contaminants** and **multilayer** **graphene** **wrinkles** in **HOPG** samples can steer **oxidation** **localization** compared to **ideal** **basal** **planes**. **Etch-pit** **morphologies** in **experiment** should be compared using the **same** **length** **scales** and **time** **windows** reported for **MD** **analysis** in the **version-of-record** article.

## Relevance to group

Duplicate ingest for archival provenance; **primary narrative** lives with [[2013poovathingal-venue-jp3125999]].

## Citations and evidence anchors

- DOI: [10.1021/jp3125999](https://doi.org/10.1021/jp3125999)
- Extract: `normalized/extracts/2013poovathingal-venue-research_p1-2.txt`

## Related topics

- [[2013poovathingal-venue-jp3125999]]
- [[reaxff-family]]
