---
id: paper:2017cunha-venue-paper
type: paper
title: "Raman spectroscopy revealing noble gas adsorption on single-walled carbon nanotube bundles"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.11.017"
year: 2017
authors:
  - "Renato Cunha"
  - "Ricardo Paupitz"
  - "Kichul Yoon"
  - "Adri C. T. van Duin"
  - "Paulo T. Araujo"
  - "Mauricio Terrones"
venue: "Carbon"
pdf_sha256: "eb76096047283c2495c2eb29d3440a854bf0b304cd4158d1b4bc9817486e5600"
pdf_path: "papers/Cunha_Carbon_2017_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017cunha-venue-paper -->

## Summary

This page tracks an **uncorrected proof** PDF (`papers/Cunha_Carbon_2017_proof.pdf`) for a *Carbon* article investigating **argon** and **xenon** adsorption on **single-walled carbon nanotube (SWCNT) bundles** using **low-temperature Raman spectroscopy** combined with **ReaxFF-based modeling**. Bundles deposited on **transmission electron microscopy grids** are exposed to noble gases at **20 K**, where condensed adsorbates populate **external groove sites** (the interstitial channels between tubes in a bundle) and outer bundle surfaces. The abstract reports **substantial blueshifts** of the **radial breathing mode (RBM)**, **G-band**, and **G′/2D** features, interpreted as a **solidified adsorbate shell** that applies an effective **hydrostatic pressure** to the nanotube lattice, mechanically coupling to the measured phonons. The authors highlight that **Ar** and **Xe** produce **almost the same frequency shifts**, arguing that the bundle–gas interactions are **nearly identical** in strength within the experimental resolution, consistent with physisorption-dominated noble-gas probes.

## Methods

Same **experimental + ReaxFF** design as the **version-of-record** article (**DOI 10.1016/j.carbon.2017.11.017**): **Raman** on **SWCNT bundles** with **Ar/Xe** at **20 K**, plus **ReaxFF** modeling of **adsorption-site** occupancy and **mechanical coupling** to **phonon** shifts. **This repo `pdf_path`** points to an **uncorrected proof**—use **[[2017cunha-carbon-127-2-raman-spectroscopy]]** for the **journal-layout** PDF when reconciling numbers.

**MD protocol details** (**code**, **ensemble**, **timestep**, **thermostat/barostat**, **duration**, **supercell** definitions) match the **VOR** *Carbon* **Methods**; they are **not transcribed** from the indexed proof excerpt on this duplicate-route page.

**MD blueprint honesty (proof route).** **Reactive molecular dynamics** with **ReaxFF** on **PBC** **bundle** models mirrors the **VOR**. **LAMMPS** is the usual **MD engine**—confirm in the **journal PDF**. **NVT**/**NPT**/**NVE**, **timestep**, **thermostat**, **barostat**/**pressure**, and **equilibration**/**production** times (**ps**/**ns**) are **N/A** from the proof excerpt—copy from **[[2017cunha-carbon-127-2-raman-spectroscopy]]**’s **Methods** source.

## Findings

**Blueshifts** of **RBM/G/2D** upon **noble-gas** condensation; **Ar** and **Xe** give **nearly identical** shift patterns, consistent with **physisorption**-dominated coupling. **Interpretation:** shifts reflect **mechanical** loading from a **solidified adsorbate shell** more than **strong electronic doping** (supported by **linewidth/intensity** behavior in the manuscript). Treat this slug as a **duplicate PDF route**; detailed **simulation–experiment** comparisons live in the **final** *Carbon* **PDF**. **Comparisons:** experimental **Raman** trends for **Ar** vs **Xe** are the primary comparator; modeling supports **physisorption** interpretations. **Sensitivity:** **temperature** (**20 K** dosing) controls adsorption state. **Limitations:** **proof** PDF may omit final figure quality; see **## Limitations**.

## Limitations

**Proof** PDF (`extraction_quality: partial`): **pagination**, metadata, and figures may differ from the **VOR**; prefer **[[2017cunha-carbon-127-2-raman-spectroscopy]]** for curation-backed numbers.

## Relevance to group

Alternate **manifest** entry for **van Duin**/**Terrones**-adjacent **nanotube** **adsorption** work.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.carbon.2017.11.017` (`papers/Cunha_Carbon_2017_proof.pdf`).

## Related topics

- [[reaxff-family]]
