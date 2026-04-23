---
id: paper:2017reddivari-venue-fep-17032-rs
type: paper
title: "Chemical composition and formation mechanisms in the cathode-electrolyte interface layer of lithium manganese oxide batteries from reactive force field (ReaxFF) based molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:perovskite-oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1007/s11708-017-0500-8"
year: 2017
authors:
  - "Sahithya Reddivari"
  - "Christian Lastoskie"
  - "Ruofei Wu"
  - "Junliang Zhang"
venue: "Frontiers of Engineering in China / Higher Education Press (2017)"
pdf_sha256: "00b5249d803e876da38c8357a853d32c0d58721a0ba3aca2eac38616d37559ee"
pdf_path: "papers/ReaxFF_others/Reddivari_MnOx_ReaxFF_EC_front_energy_2017_v11_p365.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017reddivari-venue-fep-17032-rs -->

## Summary

Lithium manganese oxide spinel cathodes power many lithium-ion cells, but interfacial degradation—electrolyte oxidation, transition-metal dissolution, and cathode–electrolyte interphase (CEI) growth—limits calendar and cycle life in high-voltage operation. This Frontiers of Engineering in China article applies ReaxFF-based reactive molecular dynamics to LiMn\(_2\)O\(_4\) surfaces in contact with electrolyte-relevant molecular environments, focusing on how solvent oxidation and acid-driven chemistry produce CEI species and how manganese mobility couples to surface hydroxylation. The work positions itself as bridging atomistic detail with experimentally reported CEI compounds, comparing simulation outputs to spectroscopic identifications of carbonates, esters, and inorganic fluorides in realistic cells. Spinel cathodes operate at high voltage versus graphite anodes; interfacial electrolyte oxidation is therefore expected even before transition-metal dissolution accelerates fade.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF-based reactive MD** probes **LiMn\(_2\)O\(_4\)** **cathode surfaces** in contact with **organic carbonate-type** solvent fragments and **HF**-containing environments to capture **cathode–electrolyte interphase (CEI)** formation chemistry (*Frontiers of Engineering in China* / Higher Education Press, DOI in front matter). The indexed extract `normalized/extracts/2017reddivari-venue-fep-17032-rs_p1-2.txt` states the scientific goal and chemistry classes but **not** the numerical MD table—pull **ensemble, Δt, thermostat, run length, and supercell sizes** from **`pdf_path`**.

- **Engine / code:** **ReaxFF MD** (reactive bond-order dynamics as implemented in the article’s software stack—see PDF).
- **System size & composition:** **LiMn\(_2\)O\(_4\)** surface cells interfaced to **electrolyte-relevant** organics and **HF** as described in the article; explicit **atom counts** are **N/A** in the indexed excerpt.
- **Boundaries / periodicity:** **N/A** — **PBC** details not stated in the indexed excerpt.
- **Ensemble:** **N/A** — **NVE/NVT/NPT** not stated in the indexed excerpt.
- **Timestep:** **N/A** — **Δt (fs)** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — equilibration vs production **ps/ns** not stated in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt.
- **Barostat:** **N/A** — **NPT** usage not stated in the indexed excerpt.
- **Temperature:** **N/A** — target **K** not stated in the indexed excerpt.
- **Pressure:** **N/A** — stress control not stated in the indexed excerpt.
- **Electric field:** **N/A** — **galvanostatic** cell operation is **not** simulated as a continuum **voltage** profile here; focus is **chemical** reactivity at the **oxide–electrolyte** contact.
- **Replica / enhanced sampling:** **N/A** — direct **ReaxFF** trajectories.

### 2 — Force-field training

**N/A as a new publication fit** — the article **applies** a **ReaxFF** parameterization for **Li–Mn–O / organics / fluorine** chemistry from the cited **ReaxFF** development literature (see bibliography in PDF).

### 3 — Static QM / DFT-only

**N/A** — **QM** is not the **production trajectory** engine for the reported **CEI** MD.

## Findings

### Outcomes and mechanisms

**ReaxFF MD** trajectories show **CEI**-like layers built from **oxidized solvent** products (**aldehydes, esters, alcohols, polycarbonates, organic radicals**) coexisting with **surface hydroxyl** species that couple to **exposed Mn** centers—linking **electrolyte oxidation** to **Mn dissolution** pathways emphasized in the abstract.

### Comparisons

Predicted **organic + inorganic** products—including **Mn–F** motifs promoted by **HF**—are stated to agree with **experimentally identified CEI** compounds summarized from the **Li-ion** literature.

### Sensitivity / design levers

**HF presence** toggles **fluoride** formation versus purely **organic** oxidation routes; **surface hydroxylation** mediates how **Mn²⁺** participates in **interfacial** reactions.

### Limitations and corpus honesty

**Empirical reactive models** can **misrank** rare **barriers**; accessible **nanosecond** trajectories emphasize **early-stage CEI** chemistry rather than **hundred-cycle** thickening. Minimalist **solvent/salt** choices omit full commercial **electrolyte** complexity—treat the scheme as **mechanistic** guidance anchored to **`pdf_path`**, not a turnkey **full-cell** model.

## Limitations

Empirical reactive models may misrank rare reaction barriers; accessible simulation times capture early-stage interphase formation rather than thickening over hundreds of cycles. Organic electrolyte compositions in commercial cells contain multiple solvents and salts not all represented in minimalist models.

## Relevance to group

Battery cathode ReaxFF narrative aligned with [[batteries-interfaces-reaxff]] themes.

## Citations and evidence anchors

- DOI: [10.1007/s11708-017-0500-8](https://doi.org/10.1007/s11708-017-0500-8)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
