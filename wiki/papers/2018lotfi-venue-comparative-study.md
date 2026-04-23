---
id: paper:2018lotfi-venue-comparative-study
type: paper
title: "A comparative study on the oxidation of two-dimensional Ti3C2 MXene structures in different environments"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/C8TA01468J"
year: 2018
authors:
  - "Roghayyeh Lotfi"
  - "Michael Naguib"
  - "Dundar E. Yilmaz"
  - "Jagjit Nanda"
  - "Adri C. T. van Duin"
venue: "J. Mater. Chem. A"
pdf_sha256: "f326f23a2a7f30201a3bab664287f5da9e86fc15dca79bfff17031c00e24a832"
pdf_path: "papers/Lotfi_Materials_A_2018_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018lotfi-venue-comparative-study -->

## Summary

Two-dimensional **Ti\(_3\)C\(_2\)** MXene is attractive for energy and electronics applications but is famously sensitive to **oxidation** in ambient and processing environments. This **Journal of Materials Chemistry A** article presents a **comparative** experimental and simulation study of **MXene oxidation** under **different environmental** conditions, using **ReaxFF molecular dynamics** to interpret **atomistic** pathways alongside **experimental** characterization of surface chemistry and structure. The scientific goal is to connect **environment-dependent** exposure (gas composition, humidity-related regimes, and related parameters defined in the peer-reviewed text) to **oxidation extent**, **termination** changes, and **defect** evolution at MXene surfaces. This wiki entry’s **`pdf_path`** is an RSC **publisher proof** PDF (workflow pages mixed with article text). For **pagination, final figures, and authoritative numerical values**, prefer the **version-of-record** PDF for the same DOI and the sibling wiki page **`[[2018lotfi-journal-of-m-comparative-study]]`**, which is curated against the non-proof file where available.

## Methods

This **proof** PDF (`papers/Lotfi_Materials_A_2018_proof.pdf`) documents the same study as **`[[2018lotfi-journal-of-m-comparative-study]]`** (VOR `papers/Lotfi_Materials_A_2018.pdf`): paired **experiments** (controlled **gas / humidity** exposure and **surface** characterization) with **ReaxFF reactive MD** of **Ti\(_3\)C\(_2\)** oxidation in **dry air**, **wet air**, and **H\(_2\)O\(_2\)**, including a **vacuum** baseline and a **1000–3000 K** temperature program in the abstract. **MD protocol line items** (code name, supercell sizes, **PBC**, **NVT/NPT** labels, **fs** timestep, **ns** trajectory lengths, thermostat/barostat)—**N/A — not transcribed from this proof path**; copy them from the **version-of-record** Methods after cross-checking pagination. **Electric field:** **N/A — not used** per abstract-level description. **Enhanced sampling:** **N/A — not indicated** in the indexed abstract framing.
## Findings

**Outcomes.** Simulated **oxidation** rates order as **H\(_2\)O\(_2\) > wet air > dry air**; **temperature** increases **Ti** surface segregation and bond-order trends summarized on **`[[2018lotfi-journal-of-m-comparative-study]]`**. **Vacuum** heating trends toward **cubic TiC** with limited bond-order drift aside from **topotactic** rearrangement in the abstract narrative.

**Comparisons.** **XRD/Raman** after **wet vs dry air** heating support the qualitative **simulation** oxidant ordering in the published story—quote numbers from the **VOR** PDF, not this proof file alone.

**Sensitivity / design levers.** **Temperature** sweeps and **environment** matrix are the primary comparative axes in the abstract.

**Limitations / outlook.** Treat **proof** figures and tables as **non-authoritative** for final pagination; prefer **`[[2018lotfi-journal-of-m-comparative-study]]`** for maintenance.

**Corpus honesty.** **Proof PDF** ingest; detailed MD settings and any SI-only protocols live on the **VOR** sibling page and primary article text.
## Limitations

**Proof PDF** formatting can obscure tables and figure quality; **ReaxFF** chemistry is empirical and may not capture all long-timescale oxidation kinetics without calibration.

## Relevance to group

**Group-coauthored** application of **ReaxFF** to **MXene** environmental stability, pairing reactive MD with experimental grounding.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1039/C8TA01468J](https://doi.org/10.1039/C8TA01468J)

## Reader notes (navigation)

- [[2018lotfi-journal-of-m-comparative-study]]

## Related topics

- [[reaxff-family]]
