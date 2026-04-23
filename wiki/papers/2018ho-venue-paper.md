---
id: paper:2018ho-venue-paper
type: paper
title: "Development of a ReaxFF Reactive Force Field for NaSiOx/Water Systems and Its Application to Sodium and Proton Self-Diffusion (Supporting Information)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b05852"
year: 2018
authors:
  - "Seung Ho Hahn"
  - "Jessica Rimsza"
  - "Louise Criscenti"
  - "Wei Sun"
  - "Lu Deng"
  - "Jincheng Du"
  - "Tao Liang"
  - "Susan B. Sinnott"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C (Supporting Information PDF in corpus)"
pdf_sha256: "4f729f601bd851419c83d1c153fdb43a83feaefb481b74760abd1973e3fd9c3d"
pdf_path: "papers/Hahn_NaSiOx_JPCC_2018_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2018ho-venue-paper -->

## Summary

The corpus entry points at the **ACS Supporting Information** PDF for the **J. Phys. Chem. C** article **“Development of a ReaxFF Reactive Force Field for NaSiOx/Water Systems…”** The SI documents the **Na/Si/O/H ReaxFF parameter table** and related **supporting computational details** for a parameterization aimed at **sodium silicate–water** chemistry, **Na⁺ transport**, and **proton-related** behavior in **silicate** environments. The **peer-reviewed article** (same author team, including **Adri C. T. van Duin**) is identified by **DOI `10.1021/acs.jpcc.8b05852`**; this wiki page is intentionally **SI-first** because the manifest registers **`papers/Hahn_NaSiOx_JPCC_2018_SI.pdf`**. This role is also recorded in the repository’s non-primary article catalog: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Methods

**SI scope:** The **Supporting Information** **PDF** (`pdf_path`) tabulates the full **Na/Si/O/H ReaxFF** **parameter set** obtained by fitting to **DFT/QM reference energies**, **barriers**, **NaSiOₓ** condensed-phase **structures**, surface–ion–water motifs, and cluster dissociation curves documented in the **main JPCC** article (**DOI** `10.1021/acs.jpcc.8b05852`). **QM reference** levels, **basis** choices, and **k-point** conventions for that fit appear in the primary **Methods** there.

**MD application (delegate to main article):** Production **LAMMPS** **reactive MD** for **Na⁺** and **proton** **diffusion**, dissolution, and validation benchmarks uses **3D PBC** **supercells** whose **atom** counts, **timestep**, **thermostat**/**barostat** choices, **equilibration** vs **production** **durations** (**ps**/**ns**), and target **temperature**/**pressure** are spelled out in the **peer-reviewed** **PDF** on **`[[20180000-0002-1722-5631-j-phys-chem-development-reaxff]]`**—**N/A — reproduce those numbers from this SI page** alone. The main text reports standard **NVT**/**NPT** (and occasional **NVE** segments where noted) **ensembles** for silicate–water cells; confirm the exact stage list in that **PDF**.

**Force-field training (this ingest):** **Optimization** workflow, **training set** composition, and **validation** benchmarks belong to the **main text**; this file preserves the **fitted coefficients** and any SI-only tables.

## Findings

This corpus file’s primary utility is distributing the machine-readable **ReaxFF** coefficients and SI tables for the 2018 **JPCC** study, enabling reproduction of **sodium silicate** and **glass–water** simulations when combined with the **main article** protocols.
- **Comparisons / mechanisms:** Interpretations of **Na⁺**/**proton** **transport** and **reaction** **mechanisms** versus **experiment** appear in the **primary** **paper**; this SI does not restate those **Results** figures.
- **Corpus honesty:** **SI-only** ingest—use **`[[20180000-0002-1722-5631-j-phys-chem-development-reaxff]]`** for integrated **Findings** and for **timestep**/**ensemble** details. **`pdf_path`** here is the **ACS** **Supporting Information** file registered in the manifest.

## Limitations

- **`extraction_quality: partial`** reflects that the **ingested PDF is SI**, not the full article text; readers should use the **main JPCC PDF** for **discussion, figures, and validation** narrative.

## Relevance to group

Core **Na/Si/O/H ReaxFF** dissemination for **silicate dissolution**, **ion interdiffusion**, and related **glass–water** simulations.

## Citations and evidence anchors

- **Main article DOI:** `https://doi.org/10.1021/acs.jpcc.8b05852`.
- **SI file:** `papers/Hahn_NaSiOx_JPCC_2018_SI.pdf` (registered in `raw/MANIFEST.jsonl`).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Main article: [[20180000-0002-1722-5631-j-phys-chem-development-reaxff]]
