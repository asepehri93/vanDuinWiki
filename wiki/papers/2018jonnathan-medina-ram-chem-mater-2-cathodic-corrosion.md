---
id: paper:2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion
type: paper
title: "Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte Interface under Conditions for CO2 Reduction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.8b00050"
year: 2018
authors:
  - "Jonnathan Medina-Ramos"
  - "Weiwei Zhang"
  - "Kichul Yoon"
  - "Peng Bai"
  - "Ashwin Chemburkar"
  - "Wenjie Tang"
  - "Abderrahman Atifi"
  - "Sang Soo Lee"
  - "Timothy T. Fister"
  - "Brian J. Ingram"
  - "Joel Rosenthal"
  - "Matthew Neurock"
  - "Adri C. T. van Duin"
  - "Paul Fenter"
venue: "Chem. Mater."
pdf_sha256: "2f06941fb0d800186e940881ae40a5df8ef3a28444c7a9db780b319793bfec71"
pdf_path: "papers/MedinaRamon_ChemMat_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The paper investigates **cathodic corrosion** of **bismuth** in contact with an **ionic-liquid electrolyte** under **CO₂ electroreduction**–relevant **potentials**, combining **ReaxFF molecular dynamics** and **DFT** to connect **interfacial disorder**, **charge state**, and **metal migration** into the **electric double layer**. **ReaxFF** is used to capture **large-scale ionic rearrangements** and **surface roughening** at **negative bias**, while **DFT** supports **local bonding** interpretations (e.g., **Bi migration** motifs). **Adri C. T. van Duin** is among the coauthors bridging **reactive MD** with **electrocatalysis-focused** collaborators.

## Methods

- **ReaxFF MD** of **Bi(001)** slabs with **ionic liquid** components under **cathodic** conditions (as defined in the article).
- **DFT** calculations for **complementary** energetics and **bonding** analysis.

## Findings

- **Increasingly negative** surface charge correlates with **greater surface disorder** in **ReaxFF** trajectories.
- **Bi migration** from the **metal surface** is predicted to intensify under the **cathodic** scenarios studied, consistent with a **corrosion** picture rather than a perfectly **passive** interface.

## Limitations

- **Electrochemical potential control** in **classical reactive MD** is approximate; compare **DFT** and **experiment** where quoted in the paper.
- **Ionic liquid force-field** fidelity for **long-time** dynamics may require **validation** on **subset processes**.

## Relevance to group

Demonstrates **ReaxFF** applied to **electrified interfaces** with **ionic liquids**, a recurring theme in **electrochemistry + reactive MD**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.chemmater.8b00050` (`papers/MedinaRamon_ChemMat_2018.pdf`).

## Related topics

- [[reaxff-family]]
