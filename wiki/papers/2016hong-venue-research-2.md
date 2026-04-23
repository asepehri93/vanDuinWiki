---
id: paper:2016hong-venue-research-2
type: paper
title: "Atomistic-scale analysis of carbon coating and its effect on the oxidation of aluminum nanoparticles by ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b00786"
year: 2016
authors:
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "d9e0eb2b3222077eec1630eb4c9227bc458449923f83f4dc7d1a5f91b3a8150d"
pdf_path: "papers/Hong_AlCOx_JPCC_2016_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:combustion
  - keyword:galley-or-proof-pdf
---
<!-- id:paper:2016hong-venue-research-2 -->

## Summary

This page documents the reduced-resolution duplicate PDF for the same 2016 JPCC study on carbon-coated aluminum nanoparticles and oxidation (`10.1021/acs.jpcc.6b00786`). The study itself develops a ReaxFF description for Al/C interactions (within an Al/C/H/O reactive chemistry scope), then uses reactive MD to connect three linked questions: how hydrocarbon precursors bind/react on Al nanoparticle surfaces, how carbon coatings grow under repeated exposure cycles, and how those coatings influence subsequent oxidation behavior.

From the abstract and first pages in `normalized/extracts/2016hong-venue-research-2_p1-2.txt`, the central claim is that the new ReaxFF reproduces key Al/C interaction trends from QM and captures qualitative pathways seen experimentally for coating and oxidation. The reported mechanistic picture includes hydrogen transfer from hydrocarbons to available Al sites during coating growth, often without C-C scission in the highlighted ethylene scenario, precursor-dependent coating buildup, and temperature-sensitive oxidation behavior where coatings suppress low-temperature reactivity but can be removed at elevated temperature, exposing Al and accelerating oxidation.

The introduction frames why this matters for energetic materials. Aluminum nanoparticles are highly energetic but can lose effective energy density when thick oxide layers form before intended combustion; coating strategies are therefore explored as passivation and performance-control tools. The paper cites prior coating/oxidation experiments as context and uses ReaxFF MD as an atomistic bridge between measured trends and reaction-level interpretations.

Corpus honesty is critical for this slug: `wiki/papers/2016hong-venue-research-2.md` corresponds to `papers/Hong_AlCOx_JPCC_2016_reduced.pdf`, a reduced-byte duplicate. The core science matches `[[2016hong-venue-research]]`, but this file role is archive/portability oriented. For figure-level precision (small annotations, exact axis readouts, publication pagination), users should cite the proof/VOR-oriented sibling page.

## Methods

**1 - MD application (reactive dynamics).**
- **Engine / code:** ReaxFF molecular dynamics is run with the ADF implementation in this publication line.
- **System size and composition:** Coating runs use an aluminum nanoparticle model (864 Al atoms) plus hydrocarbon feed molecules; oxidation runs add O2 around coated particles.
- **Boundaries / periodicity:** Coating setup is reported in a finite box (45 x 45 x 45 A^3) and oxidation in a larger box (60 x 60 x 60 A^3), consistent with gas-solid reactive sampling rather than periodic bulk condensed phases.
- **Ensemble:** NVT.
- **Timestep:** 0.1 fs.
- **Duration / stages:** Coating cycles include hot-gas exposure then cooling; oxidation trajectories are reported to 150 ps in the summarized protocol.
- **Thermostat:** Berendsen thermostat with 100 fs damping (as captured on the canonical sibling page from the same article).
- **Barostat:** N/A - no NPT stage is reported in the summarized protocol.
- **Temperature:** Coating and oxidation scenarios span ambient and high-temperature conditions; oxidation comparison emphasizes 300 K versus 3000 K.
- **Pressure:** N/A as controlled variable in the summarized NVT setup.
- **Electric field:** N/A - not used.
- **Replica / enhanced sampling:** N/A - not reported.

**2 - Force-field training (ReaxFF parameterization).**
- **Parent FF / elements:** ReaxFF was extended for Al/C interactions within Al/C/H/O chemistry.
- **QM reference:** Periodic QM references are generated with VASP using GGA-PBE and PAW; nonperiodic references use Jaguar with B3LYP/6-311G, as described in the article computational-details section.
- **Training set:** Includes adsorption/reactivity energetics on Al(111), cluster geometries, bond/angle distortions, and barrier benchmarks linked to coating-relevant chemistry.
- **Optimization:** Sequential refinement of relevant ReaxFF terms, with selected pathway checks against DFT/NEB references.
- **Reference data used:** Additional validation against QM targets and experimental oxidation/coating trends cited in the paper.

**3 - Static QM / DFT-only block (as supporting layer).**
- **Functional:** PBE for periodic calculations; B3LYP for cluster calculations.
- **Dispersion:** N/A in the extract-level summary.
- **Basis / cutoff:** Plane-wave cutoff around 400 eV for periodic calculations; 6-311G basis for Jaguar cluster work.
- **k-sampling:** Reported in full methods on the canonical page/article; not fully reproduced here.
- **Structures/pathways:** Al(111) adsorption and coating-related reaction-pathway energetics.
- **Properties computed:** Interaction energies, barriers, and geometrical targets used for fitting and validation.

**File-role note:** this markdown tracks the reduced-byte PDF variant. The scientific protocol is the same study as `[[2016hong-venue-research]]`; differences are archival (PDF raster/quality), not chemistry.

## Findings

The article reports that the fitted ReaxFF reproduces key Al/C interaction behavior from the QM references and then yields a coherent atomistic narrative for coating growth and oxidation response. During hydrocarbon exposure, coating growth proceeds through surface reactions where hydrogen transfer to reactive Al sites is prominent in the highlighted ethylene case, while extensive C-C backbone cleavage is not the dominant early mechanism in that scenario. Across precursor choices, the carbon deposition extent differs systematically, producing a precursor-dependent C/Al trend and coating-thickness ordering.

For oxidation behavior, the paper's MD results support a temperature-gated interpretation: carbon-coated particles are less reactive under low-temperature conditions, but at elevated temperature the coating can be removed/consumed, which increases access of oxygen to the Al core and leads to more vigorous oxidation chemistry. This aligns with the introduction's cited experimental context that organic/carbon coatings may protect against premature oxidation but can still participate in high-temperature energy release.

The study's broader contribution is therefore not just a new parameter file, but a linked methodology: DFT-guided reactive force-field fitting plus reactive MD scenarios that connect coating chemistry to oxidation consequences in a unified model. For knowledge-base use, this paper is a useful bridge between force-field parameterization (`task:parameterization`) and application-style reactive MD interpretation for energetic nanoparticle systems.

Corpus-honesty findings for this duplicate slug:
- This file tracks a reduced-resolution PDF; it should not be the preferred citation source for fine-grained figure metrology or precise page anchoring.
- The scientific conclusions should be treated as shared with the canonical sibling page, not as an independent second experiment.
- Where quantitative values differ between local copies due to rendering or readability, the proof/VOR copy should take precedence for downstream extraction and quoting.

## Limitations

**Reduced-resolution** figures vs other corpus PDFs; cite the **journal version-of-record** for pagination. Short **oxidative** windows use **accelerated O₂ density** (qualitative kinetics). Operators comparing PDF duplicates should still verify that figure panels needed for quantitative barrier readouts are taken from a full-resolution ACS export rather than this reduced rasterization.

## Relevance to group

**van Duin** co-authorship on **ReaxFF** for **Al combustion** nanoparticles with explicit **coating** chemistry; this entry tracks **alternate bytes** only.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b00786](https://doi.org/10.1021/acs.jpcc.6b00786) — `papers/Hong_AlCOx_JPCC_2016_reduced.pdf`.

## Reader notes (navigation)

- **Primary curated page:** [[2016hong-venue-research]] (ACS proof PDF); this slug is the **reduced-file** duplicate (`papers/Hong_AlCOx_JPCC_2016_reduced.pdf`). Operator catalog of PDF roles: `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

## Related topics

- [[2016hong-venue-research]]
- [[reaxff-family]]
