---
id: paper:2016yeon-venue-la5b04062-2
type: paper
title: "Effects of Water on Tribochemical Wear of Silicon Oxide Interface: Molecular Dynamics (MD) Study with Reactive Force Field (ReaxFF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.5b04062"
year: 2016
authors:
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Langmuir"
pdf_sha256: "51f326fce96bbfcf56b5aee88781b3cadf7228fb859bfb77f6befe0fb07566b7"
pdf_path: "papers/Yeon_Langmuir_2016_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yeon-venue-la5b04062-2 -->

## Summary

ReaxFF molecular dynamics is used to model atomistic processes at a sliding interface between fully hydroxylated amorphous silica and oxidized silicon, with varying **interfacial water** from dry to submonolayer to monolayer-like conditions. The simulations address how water enables or suppresses interfacial mixing, Si–O–Si bridge formation, and atom transfer that accompany tribochemical wear. The study is motivated by MEMS and silica tribology contexts where humidity swings change wear rates without obvious macroscopic lubricant films. **Langmuir** framing ties the **shear**-driven chemistry to **humidity-controlled** **adhesion** and **wear** in **silicon** **oxide** contacts common in **MEMS** reliability studies.

## Methods

This slug points at a **reduced-size PDF** (`papers/Yeon_Langmuir_2016_reduced.pdf`) for the same **Langmuir** article as **`[[2016yeon-venue-la5b04062]]`** (**DOI** `10.1021/acs.langmuir.5b04062`). **Methods** match the **VOR** page: **Engine / code:** **LAMMPS**; **ReaxFF** (**Fogarty Si/O/water**); **3.19 × 3.19 × 7.0 nm\(^3\)** **periodic** cell; **ensemble:** **NVT**; **thermostat:** **Nose–Hoover**; **timestep:** **0.25 fs**; **normal load:** **1 GPa** on the **top rigid** slab; **shear:** **10 m/s** for **1 ns**; **interfacial water:** **0 / 20 / 50 / 100** molecules; **temperatures:** **300 / 500 / 700 K** (**Simulation Methods** in the issue PDF).

**2 — Force-field training.** **N/A —** literature **ReaxFF** parametrization.

**3 — Static QM.** **N/A —** not used.

**4 — Replica / enhanced sampling.** **N/A —** not used.
## Findings

- **Without water**, interfacial mixing begins with **dehydroxylation** followed by **Si–O–Si bridges** linking the two surfaces, with substantial **atom transfer** across the interface during sliding.
- With **submonolayer water**, **water dissociation** opens additional pathways to form Si–O–Si bridges and sustain cross-interface atom transfer.
- When interfacial water is sufficient for a **full monolayer**, **atom transfer is strongly reduced** because interfacial silicon sites are **terminated by hydroxyls** rather than forming as many interfacial Si–O–Si bridge bonds.
- The authors argue the simulations clarify how **humidity and water coverage** modulate **tribochemical wear** of silicon oxide interfaces at the atomistic level.

## Limitations

**Reduced PDF** may omit **SI** figures present in the **full** file; use **`[[2016yeon-venue-la5b04062]]`** for archival completeness. Idealized **planar** contacts omit **asperity** statistics and **third-body** debris relevant to **MEMS** wear maps.

## Relevance to group

Penn State collaboration on ReaxFF for silica tribochemistry and MEMS-relevant interfaces. The humidity-dependent atom-transfer story here is frequently cited alongside later group papers on silica wear, so maintaining consistent terminology around “submonolayer” versus “monolayer-like” coverage helps cross-linking within the wiki graph.

## Citations and evidence anchors

- DOI: [10.1021/acs.langmuir.5b04062](https://doi.org/10.1021/acs.langmuir.5b04062); volume/pages per the issue PDF on **`[[2016yeon-venue-la5b04062]]`**.
- Text-aligned pointers: `normalized/extracts/2016yeon-venue-la5b04062-2_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
