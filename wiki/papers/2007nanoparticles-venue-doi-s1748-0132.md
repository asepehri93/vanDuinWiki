---
id: paper:2007nanoparticles-venue-doi-s1748-0132
type: paper
title: "Generating heat with metal nanoparticles"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:review-or-perspective
  - keyword:metallic-systems
  - keyword:validation-experiment
canonical_tags:
  - domain:methods-software
  - material:metal-surface
  - method:continuum-or-mesoscale
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/S1748-0132(07)70017-8"
year: 2007
authors:
  - "Alexander O. Govorov"
  - "Hugh H. Richardson"
venue: "Nano Today 2 (1) (2007)"
pdf_sha256: "669c5ca8a8ee18c7277bfdf3bc6d81b3b79eb8f58862d29a2f17421055c14d95"
pdf_path: "papers/Others/Nanoparticles_heat_generation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2007nanoparticles-venue-doi-s1748-0132 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **review article** identified by `doi` and `pdf_path`. It is **not** a ReaxFF methods note; citations to primary literature are in the PDF.

## Summary

This *Nano Today* review describes photothermal heating with colloidal metal nanoparticles: efficient heat generation under electromagnetic irradiation, strong enhancement under plasmon resonance, and dependence on particle shape and organization. It discusses coupling of optical absorption to heat transfer into a surrounding matrix, practical challenges in measuring local temperature rise at nanoparticle surfaces, and illustrative experimental strategies (for example embedding gold nanoparticles in ice and using melting thresholds to infer surface temperature; complexes of semiconductor and metal nanoparticles linked by thermoresponsive polymers for distance-dependent emission-based thermometry).

## Methods


The article is a conceptual and literature synthesis. It introduces continuum heat-transfer equations for temperature fields \(T(\mathbf{r},t)\) with local mass density \(\rho\), specific heat \(c\), thermal conductivity \(k\), and a source term \(Q\) from optical dissipation, together with constitutive relations linking \(Q\) to the electric field and induced current density as in the review’s Equations (1)–(2). For a single spherical particle in the long-wavelength limit, steady-state temperature profiles and absorbed-power estimates are developed analytically (Equations (3)–(4) in the PDF) and illustrated with model calculations (for example temperature vs distance for an optically driven gold nanoparticle in water in Figure 1).

## Findings

**Metal** nanoparticles convert absorbed radiation into **strong local heating**; **plasmon resonance** can **greatly increase** absorption versus off-resonance illumination. **Metal** nanoparticles have **very low optical quantum yield**, so **total heat release** can often be approximated from the **absorption rate** with simple energy-balance arguments. The article ties localized heating to **phase changes** in matrices (e.g. **ice melting** thresholds), **biomedical** photothermal uses, and **nanoscale thermometry** strategies (e.g. **semiconductor–metal** complexes with **thermoresponsive polymer** spacers and **distance-dependent** optical readout). The review also stresses that **measuring** true **nanoscale temperature** remains experimentally demanding, which motivates indirect probes and modeling bridges between optics and continuum heat transport.

## Limitations

- This is a **review**, not a primary simulation paper; quantitative predictions are attributed to cited studies within the article.
- Not part of the ReaxFF corpus beyond general materials-simulation context.

## Relevance to group

Background reading on **nanoscale energy localization** and optical–thermal coupling; **no direct ReaxFF** content—useful for cross-disciplinary retrieval only.

## Citations and evidence anchors

- DOI: `10.1016/S1748-0132(07)70017-8` (also printed as *Nature Nanotechnology* Vol. 2, 2007 in the extract header).
- PDF: `papers/Others/Nanoparticles_heat_generation.pdf`.

## Related topics

- [[material:metal-surface]]
