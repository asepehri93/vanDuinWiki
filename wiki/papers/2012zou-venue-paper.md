---
id: paper:2012zou-venue-paper
type: paper
title: "Investigation of complex iron surface catalytic chemistry using the ReaxFF reactive force field method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:reactive-md
source_refs: []
doi: "10.1007/s11837-012-0463-5"
year: 2012
authors:
  - "Zou, Chenyu"
  - "van Duin, Adri"
venue: "JOM"
pdf_sha256: "ed89dac2f1280865942e152323d793d29012fc341410f7cc4abab2ef180f5a92"
pdf_path: "papers/Zou_FeCOH_JOM_2012_64_1426.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2012zou-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **JOM** article identified by `doi`, `title`, and `pdf_path`, supplemented by **`normalized/extracts/2012zou-venue-paper_p1-2.txt`**. Detailed simulation tables remain in the **full PDF**.

## Summary

Zou and van Duin report **five ReaxFF reactive molecular dynamics** simulations of **iron**-catalyzed **CO hydrogenation** and **Fischer–Tropsch**-related **surface** chemistry on **Fe(100)** models, focusing on **methanation** and early **hydrocarbon chain initiation**. The abstract frames the work as an atomistic probe of whether **CO** must **dissociate** before hydrogenation or whether pathways through **undissociated CO** (**oxygenate** mechanisms) can explain observed **CH\(_x\)** intermediates, **methane**, and **C–C** coupling. The study explicitly contrasts **carbide** vs **oxygenate** pictures and compares intermediate preferences (**CH**, **CH\(_2\)**, **carbene**-like species) against cited **QM** and **experimental** literature, while acknowledging **ReaxFF** accuracy limits for **Fe/C/O/H** chemistry.

## Methods

### Force-field training

**Parent FF / elements:** **ReaxFF** for **Fe/C/O/H** trained to reproduce an extended **QM** training set covering **heats of formation**, **equations of state**, **binding energies**, and **reaction pathways** (article **§2**; `normalized/extracts/2012zou-venue-paper_p1-2.txt`).

**QM reference, optimization, reference data:** **N/A —** program, functional, basis, **k**-mesh, and optimizer details are **not** in the p1–2 extract; read **`pdf_path`** for computational metadata.

### MD application (atomistic dynamics)

The article reports **five reactive molecular dynamics** simulations addressing **CO hydrogenation** and **hydrocarbon chain initiation** on **Fe(100)** (extract).

**Engine / code:** **N/A —** MD integrator/software **not** named in the indexed excerpt—verify **`pdf_path`**.

**System size & composition:** **N/A —** atom counts and gas-phase stoichiometries per run are **not** restated in the p1–2 extract.

**Boundaries / periodicity:** **N/A —** explicit **PBC** vs open boundary description **not** in the p1–2 extract.

**Ensemble (NVE / NVT / NPT):** **N/A —** not recoverable from `2012zou-venue-paper_p1-2.txt`; consult **`pdf_path`**.

**Timestep / duration / thermostat / barostat / pressure:** **N/A —** not recoverable from the excerpt; consult **`pdf_path`**.

**Temperature:** **Elevated temperatures** are discussed qualitatively in the extract (surface deformation at **elevated temperatures**); **N/A —** explicit thermostat setpoints per run **not** in the excerpt.

**Electric field:** **N/A —** not indicated.

**Replica / enhanced sampling:** **N/A —** not indicated.

**Analysis:** Bond-order-based tracking is used to classify **CH\(_x\)** species and **C–C** coupling events (article; extract).

## Findings

**Outcomes:** In the reported trajectories, **CO hydrogenation** initiates from **undissociated CO** on **Fe(100)** (**oxygenate** picture), producing **surface CH\(_x\)** species, **methane**, and **C–C** coupling without **direct carbide hydrogenation** as the observed dominant channel (extract). **CH** can **dissociate** to surface **C** or **hydrogenate** to **CH\(_2\)**; a highlighted **C–C** coupling case favors **CH + CH\(_2\)** pairing, discussed in relation to **alkenyl / carbene** mechanistic schemes (extract).

**Comparisons:** The authors state overall **qualitative agreement** with selected **experimental** and **QM** literature while flagging **ReaxFF** accuracy limits for **Fe/C/O/H** (extract).

**Sensitivity / levers:** Mechanistic conclusions depend on the **Fe(100)** model, **coverage**, and **temperature** conditions of each of the **five** runs (full article).

**Limitations:** **Partial** extract; **five** trajectories illustrate pathways but do not exhaust **FT** composition or **facet** space.

**Corpus honesty:** p1–2 extract stops early in **COMPUTATIONAL METHODS**; numerical **MD** settings require **`pdf_path`**.

## Limitations

**Partial** extract; **ReaxFF** **Fe** chemistry remains an active development area—validate critical barriers with **QM** when possible. **Fischer–Tropsch** chemistry spans **many** elementary steps; five trajectories illustrate mechanisms but do not exhaust **composition space**.

## Reader notes (navigation)

Link this entry to **iron** **catalysis** hubs cautiously—**Fe(100)** models omit **steps**, **alloys**, and **support** effects that dominate industrial **FT** catalysts.

## Relevance to group

**Adri van Duin** coauthored **heterogeneous catalysis** **ReaxFF** on **iron** surfaces.

## Citations and evidence anchors

- DOI **10.1007/s11837-012-0463-5** — *JOM* **64**(12), 1426ff. (2012).
- Extract: `normalized/extracts/2012zou-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
