---
id: paper:2018zhong-journal-of-a-sulfur-removal
type: paper
title: "Sulfur removal from petroleum coke during high-temperature pyrolysis. Analysis from TG-MS data and ReaxFF simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.jaap.2018.03.007"
year: 2018
authors:
  - "Qifan Zhong"
  - "Qiuyun Mao"
  - "Jin Xiao"
  - "Adri C. T. van Duin"
  - "Jonathan P. Mathews"
venue: "J. Anal. Appl. Pyrolysis"
pdf_sha256: "199ace13e1bce743988e34fad7d85b2f1903300ec85f6669fcc63c5eac7f8992"
pdf_path: "papers/Zhong_PetCoke_JAAP_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018zhong-journal-of-a-sulfur-removal -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

**Thermogravimetry–mass spectrometry (TG-MS)** on **petroleum coke** samples quantifies **sulfur rejection** versus **temperature**, **particle size**, and **source**, showing that **high temperature (≳1673 K)** drives large **desulfurization** extents (often **~80%**) for fine fractions, with **more variable** behavior for **large particles** in some feeds. **ReaxFF MD** on a **macromolecular coke** model with **thiophene-like** sulfur probes **atomistic** elimination pathways at **3000–4000 K** in **NVT** runs, rationalizing **volatile sulfur** species (e.g. **SO₂**, **CS₂**, **COS**) observed or inferred from **experiment**. **Adri C. T. van Duin** and **Jonathan P. Mathews** are Penn State coauthors with **Zhong** and collaborators in China.

## Methods

- **TG-MS** pyrolysis of **multiple petcoke** cuts and **provenances** under controlled **heating** programs.
- **ReaxFF** simulations of **S-containing** carbonaceous models at **very high temperature** to accelerate **C–S** chemistry within **short** trajectories.

## Findings

- **Gas evolution** features include **H₂O** (low-T), **volatiles**, then **CO₂/H₂**, **CO/SO₂** at higher **T**, and trace **CS₂**; **COS/H₂S** are **absent or below detection** under the reported conditions.
- **ReaxFF** trajectories suggest a **multi-step** **S removal** sequence from **thiophenic** sulfur toward **small** **S-bearing** intermediates and ultimately **SO₂** / **CS₂**-class products, consistent with the **TG-MS** picture.

## Limitations

- **ReaxFF** temperatures are **far above** industrial **calcination** to access **reactions** in **nanoseconds**; **mechanistic** insight is **qualitative** for **absolute yields**.
- **Petcoke** structural **heterogeneity** means any **single** **macromolecular** model is **illustrative**, not **sample-specific**.

## Relevance to group

Companion **JAAP** study to **`paper:2018qifan-combustion-a-reaxff-simulations`** on **petcoke desulfurization**, with **van Duin** / **Mathews** **reactive MD** involvement.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.jaap.2018.03.007` (`papers/Zhong_PetCoke_JAAP_2018.pdf`).

## Related topics

- [[reaxff-family]]
