---
id: paper:2015achtyl-nat-aqueous-proton
type: paper
title: "Aqueous proton transfer across single-layer graphene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:water-silica-geo
  - method:dft-static
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1038/ncomms7539"
year: 2015
authors:
  - "Jennifer L. Achtyl"
  - "Raymond R. Unocic"
  - "Lijun Xu"
  - "Yu Cai"
  - "Muralikrishna Raju"
  - "Weiwei Zhang"
  - "Robert L. Sacci"
  - "Ivan V. Vlassiouk"
  - "Pasquale F. Fulvio"
  - "Panchapakesan Ganesh"
  - "David J. Wesolowski"
  - "Sheng Dai"
  - "Adri C.T. van Duin"
  - "Matthew Neurock"
  - "Franz M. Geiger"
venue: "Nature Communications 6, 6539 (2015)"
pdf_sha256: "e5a780b4bd544becd590d49cc325be4b0d1053e9300186f01df68379d493dd26"
pdf_path: "papers/Achtyl_NatureComm_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015achtyl-nat-aqueous-proton -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Achtyl *et al.* combine **interface-specific second-harmonic generation (SHG)** on **graphene-on-fused-silica** with **atomistic modeling** to argue that **aqueous protons** can traverse **monolayer graphene** reversibly during bulk **pH cycling**, communicating with **silanol acid–base chemistry** beneath the sheet. After arguing against **macroscopic pinhole** transport via SEM and diffusion-order-of-magnitude estimates, they attribute permeation to **rare atomic defects**. **Computer simulations** (the extract’s opening pages do not name the electronic-structure or force-field engine explicitly) report comparatively **low barriers (~0.61–0.75 eV)** for water-mediated **Grotthuss-like** transfer across **hydroxyl-terminated** defect motifs, while **pyrylium-like ether** terminations are predicted to **block** exchange; helium/hydrogen transfer is argued to be disfavored, supporting **proton selectivity**.

## Methods

- **SHG** titration experiments with controlled **ionic strength** and dual-pump pH jumps.
- **SEM** imaging for macroscopic defect inventory.
- **Atomistic simulation** of defect-mediated proton transport (see Methods in the full PDF/SI for the specific Hamiltonian/force field).

## Findings

- SHG responses with graphene present match **bare silica/water** behavior within uncertainty, interpreted as evidence that **interfacial silanol speciation** evolves as if protons reach the buried silica surface.
- Modeling distinguishes **defect motifs** that enable vs suppress proton exchange.


## Limitations

- Rare-defect mechanisms require knowledge of **actual defect populations** in CVD graphene, which can vary by synthesis and transfer.
- Extract is early pages; full simulation setup and statistics live later in the PDF/SI.

## Relevance to group

**Adri C. T. van Duin** is among the co-authors; the work pairs **precision interface spectroscopy** with **atomistic modeling** of defect-mediated proton transport (consult the full article for the simulation model details used beyond the p1–2 extract).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1038/ncomms7539](https://doi.org/10.1038/ncomms7539)

## Related topics

- [[reaxff-family]]