---
id: paper:2025sharkass-venue-paper
type: paper
title: "Retention, sputtering and surface chemistry at tungsten oxide surface facing deuterium plasma"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - material:oxide
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:oxide-surface
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.jnucmat.2025.155622"
year: 2025
authors:
  - "Meral Sharkassa"
  - "Swarit Dwivedi"
  - "Yun Kyung Shin"
  - "Martin Nieto-Perez"
  - "Adri C. T. van Duin"
  - "Predrag S. Krstic"
venue: "Journal of Nuclear Materials"
pdf_sha256: "7218ebe51c43d2d30b0cac63d0998ba2a07ed8e030adb64ea9eaf16e63e5f4a6"
pdf_path: "papers/Sharkass_JNM_Deuterium_2025_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025sharkass-venue-paper -->

## Summary

Reactive molecular dynamics with LAMMPS and a ReaxFF description of tungsten–oxygen–hydrogen chemistry is used to study how deuterium bombardment couples to retention, reflection, sputtering, and surface chemistry on oxidized tungsten surfaces. The oxide structures are continuations of prior work in which tungsten (001) was oxidized by cumulative low-energy oxygen irradiation, yielding complex W–O ad-layers; here, deuterium impact energies from 5 eV to 120 eV are applied at room temperature while varying the effective oxide thickness. The study is motivated by plasma-facing tungsten components in fusion devices, where oxygen impurities lead to surface oxides that can alter fuel recycling and sputtering compared with clean metallic tungsten.

Local corpus PDF text is available only as a short extract plus this galley-style file; detailed numerical protocol values (supercell sizes, timestep, dose, statistics) should be taken from the full article PDF or supporting information when available.

## Methods

- **Engine and model:** LAMMPS molecular dynamics with a ReaxFF parameterization for W–O–H interactions suitable for reactive bombardment of oxidized tungsten.
- **Surface preparation (context from cited prior work in the article):** Oxidized layers on BCC W(001) built by cumulative oxygen irradiation at room temperature, forming W-rich oxide ad-layers (non-stoichiometric WOx motifs between roughly WO2 and WO3-like compositions) with thickness that grows with oxygen impact energy; a thinner, less oxygen-rich subsurface oxide can also form.
- **This study’s irradiation:** Deuterium impacts on these pre-oxidized surfaces over 5–120 eV at room temperature, with analysis of retention, reflection, sputtering, and surface chemistry as a function of impact energy and oxide thickness. **N/A** in this **summary** for **time step** (**fs**), **NVE**-like **collision** **segment** **length** in **ps**, full **slab** **atom** counts, **PBC** construction, **thermostat** details, and **NPT** **barostat** use (see **JNM** **article**/**SI**). **N/A** — external **DC** **electric** **field** in the MD cell; **N/A** — **metadynamics** in the **sampling** sense (not reported in the abstract-level framing used here).

## Findings

- Most reflected deuterium and oxygen sputtered from the surface originates in the oxide ad-layer rather than deep in metallic bulk tungsten.
- Deuterium retention probability is comparatively high at the lowest impact energies in the scanned range, decreases with increasing energy, and trends toward behavior characteristic of metallic tungsten at higher energies.
- The results are discussed relative to metallic tungsten and to selected experimental literature on deuterium interaction with tungsten oxides. **Corpus** **honesty:** the ingested file is a **galley**-style **PDF**; **version-of-record** should be preferred for **dose** and **yield** **tables**.

## Limitations

Galley/proof PDF in the corpus; extraction is partial. Atomistic MD cannot capture all plasma–surface phenomena at experimental fluences without extrapolation; quantitative comparison to experiment depends on the assumed oxide structure and bombardment statistics.

## Relevance to group

Co-authored by Adri C. T. van Duin; extends ReaxFF plasma–surface modeling for high-Z plasma-facing materials with oxygen-contaminated surfaces.

## Citations and evidence anchors

- DOI: [10.1016/j.jnucmat.2025.155622](https://doi.org/10.1016/j.jnucmat.2025.155622)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]

## Reader notes (navigation)

- Corpus registers a **galley/proof** PDF filename; prefer the journal version-of-record PDF when ingested for full methods tables and figures.
