---
id: paper:2014cysteine-venue-la5014973
type: paper
title: "Cysteine on TiO₂(110): A theoretical study by reactive dynamics and photoemission spectra simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - material:oxide
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:dft-static
  - keyword:water-interfaces
  - keyword:berendsen-thermostat
  - keyword:nvt-simulation
source_refs: []
doi: "10.1021/la5014973"
year: 2014
authors:
  - "Cui Li"
  - "Susanna Monti"
  - "Hans Ågren"
  - "Vincenzo Carravetta"
venue: "Langmuir"
pdf_sha256: "15df8c41bbb3e968e666a6c8589a410d6260c4cfdd1d5ebac6f730bab3db735f"
pdf_path: "papers/ReaxFF_others/Cysteine_TiO2_Monti_et_al_Langmuir_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014cysteine-venue-la5014973 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Spectral assignments and binding motifs must be verified in the article.

## Summary

**Classical all-atom reactive MD (ReaxFF)** explores **cysteine** adsorption on **perfect and defective rutile TiO₂(110)**, paired with **simulated O 1s, N 1s, S 2p XPS** for **lowest-energy** structures. The abstract emphasizes **multipoint** **anchoring** involving **carboxylate**, **amine**, and **thiol** moieties, **enhanced proton-transfer** reactivity near the surface, and **coexistence** of **multiple** **cysteine** **forms** in the modeled **adsorbate**. The authors argue **reactive FF dynamics plus spectroscopy simulation** is a practical route to **bioinorganic** **TiO₂** interfaces.

## Methods

### 1 — MD application (ReaxFF in ADF)

- **Surfaces / setup:** **Rutile TiO₂(110)** **perfect** and **defective** slabs (**five layers**, in-plane **~37 × 35 Å**), simulation box height **~75 Å**, **PBC** in all directions. **50-cysteine** droplets (three protonation forms) are placed **~7 Å** above the surface (“nanodroplet” protocol).
- **ReaxFF MD (ADF):** **RMD** with **ReaxFF** as implemented in **ADF**; slabs and droplets are **equilibrated separately** (**10 → 300 K** over **~25 ps**), combined, then run at **300 K** (**NVT**, **Berendsen** thermostat **τ = 0.1 ps**, **Verlet** integration, **Δt = 0.25 fs**, frames every **0.5 ps**). After **~10 ps** contact is established; **production** totals **~1 ns** with clustering analysis on **900–1000 ps** windows (**g_cluster**).
- **Barostat / pressure control:** **N/A —** **NVT** at **300 K**; no **NPT** segment summarized here.
- **Replica / enhanced sampling:** **N/A —** standard **MD** sampling with clustering post-processing (**g_cluster**).
- **Spectroscopy simulation:** **ΔSCF** core-level **O 1s**, **N 1s**, **S 2p** binding energies (**DALTON**, **AhlrichsVTZ**) on **cluster** models cut from low-energy adsorbate geometries (**5 Å** slab-atom cutoff around the ionization site), convoluted (**1 eV** FWHM Gaussians) for comparison to **XPS**.

### 2 — Force-field training (this publication)

**N/A —** applies an established **ReaxFF** description within **ADF** for **RMD**; any **reparameterization** history belongs to the parent **ReaxFF** publications cited in the article.

### 3 — Static QM (XPS simulation)

Covered under **Spectroscopy simulation** above (**ΔSCF** core-level shifts on **cluster** cuts).

## Findings

### 1 — Outcomes and mechanisms

- **Adsorption** is **multipoint**, involving **carboxylate**, **amine**, and **thiol** moieties; **proton-transfer** reactivity is **enhanced** at the **oxide** interface versus gas-phase references in their analysis.
- Multiple **cysteine protonation/-binding** states **coexist** on the surface, consistent with the **broadened experimental XPS** fingerprints discussed in the paper.
- **Defects** shift **binding preferences** and **spectral signatures** relative to the **perfect (110)** terrace, underscoring **microstructure sensitivity** for **bio–TiO₂** interfaces.

### 2 — Comparisons

- **Simulated XPS** is compared to **experimental** line shapes discussed in the paper (see **Langmuir** PDF).

### 3 — Sensitivity

- **Perfect vs defective TiO₂(110)** and coexistence of multiple **protonation** states (abstract-level framing).

### 4 — Limitations / outlook

- **Force-field** scope for **S–O** chemistry on **titania**; approximations in **XPS** simulation (**## Limitations**).

### 5 — Corpus / KB honesty

- Definitive **cluster** choices and **spectral** parameters live in **`pdf_path`** and SI, not this summary alone.

## Limitations

- **Force-field** **accuracy** for **S–O** **chemistry** on **titania**; **XPS** **simulation** approximations as detailed in the methods.

## Relevance to group

**Bio–oxide** **ReaxFF** **interface** study parallel to **biomaterial** and **electrochemistry** themes; **no** Penn State coauthors in the author list shown.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/la5014973` (`papers/ReaxFF_others/Cysteine_TiO2_Monti_et_al_Langmuir_2014.pdf`).

## Reader notes (navigation)

For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
