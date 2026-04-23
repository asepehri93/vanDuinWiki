---
id: paper:2021gao-computationa-molecular-dynamics-2
type: paper
title: "Molecular dynamics study of melting, diffusion, and sintering of cementite chromia core-shell particles"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - material:alloy-bulk
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:supporting-information
  - keyword:lammps
source_refs: []
doi: "10.1016/j.commatsci.2021.110721"
year: 2021
authors:
  - "Yawei Gao, Ana Paula Clares Pastrana, Guha Manogharan, Adri C.T. van Duin"
venue: "Comput. Mater. Sci. 199 (2021) 110721 (reduced PDF variant in corpus)"
pdf_sha256: "ea85109cb4e62c4e84de41ec78043628bee7a54f947c622719759ba55ad2f74d"
pdf_path: "papers/Gao_CompSciMat_2021_Cementite_Chromia_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021gao-computationa-molecular-dynamics-2 -->

This corpus slug registers a **reduced-size PDF** of the cementite–chromia ReaxFF additive-manufacturing study; the peer-reviewed science is the same as on [[2021gao-computationa-molecular-dynamics]].

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and the **primary** article PDF on [[2021gao-computationa-molecular-dynamics]]. This file may omit figures or layout present in the full PDF.

## Summary

ReaxFF MD in LAMMPS models hydrated Fe\(_3\)C with a Cr\(_2\)O\(_3\) shell versus bare Fe\(_3\)C, following Section 2 of the article: validation of the existing Shin *et al.* C/H/O/Fe/Cr parameter set for Fe\(_3\)C (lattice, EOS, surfaces, moduli), then NVT production runs (0.25 fs, Berendsen thermostat with 100 fs damping) for melting (1000–2600 K, 200 ps per step), diffusion (900 K and 2000 K in 200 Å cells), and two-particle sintering (900 K and 2000 K, 0.5 ns) with QEq-style charge updates every step. Full tabulated protocols and figures: [[2021gao-computationa-molecular-dynamics]].

## Methods

### 1 — MD application (atomistic dynamics)

**Same as the version-of-record entry:** LAMMPS + ReaxFF; NVT; 0.25 fs timestep; Berendsen thermostat (100 fs damping); 200 Å cubic cells for large-cell tasks; **periodic boundary conditions** on the cubic supercells; 900 K and 2000 K for solid/liquid comparisons; 1000–2600 K melting scan; 0.5 ns sintering segments; charges updated every step. **Barostat / hydrostatic pressure control:** N/A — no barostat; **N/A — pressure** not fixed (constant-volume NVT only). **Electric field / enhanced sampling:** N/A. **Engine:** LAMMPS. For atom counts, heating schedule, and restraint-based cohesive energy, use the primary PDF on [[2021gao-computationa-molecular-dynamics]]—this reduced binary may clip pagination.

### 2 — Force-field training

**N/A —** no new ReaxFF fit in this work. The authors use the published C/H/O/Fe/Cr ReaxFF from Shin *et al.* and validate Fe\(_3\)C and related properties against DFT and experiment in Section 2.1 of the article (see primary page for itemization).

### 3 — Static QM / DFT (validation)

Auxiliary BAND/DFT and literature DFT comparisons in Section 2.1 to justify using the existing ReaxFF for Fe\(_3\)C; not a DFT production study. Details on [[2021gao-computationa-molecular-dynamics]].

### 4 — Review / non-simulation

N/A.

## Findings

**Outcomes:** Shell does not change the reported melting point vs same-size bare Fe\(_3\)C; oxygen ingress; core-initiated vs surface-initiated melting; four-stage liquid sintering vs three stages in solid 900 K runs within the simulated time. **Comparisons:** core–shell vs pure particle; DFT/ experiment only in pre-MD validation. **Sensitivity / levers:** temperature (solid vs liquid, heating ramp). **Corpus:** numerical detail and figure alignment should be taken from **`papers/Gao_CompSciMat_2021_Cementite_Chromia.pdf`**; this page tracks the reduced PDF only.

## Limitations

The reduced PDF may omit figures or pagination. Prefer the full VOR file when both exist. ReaxFF and finite system size caveats as on the primary article page.

## Relevance to group

Adri C. T. van Duin is senior author; duplicate manifest row for the same group AM powder study.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2021.110721](https://doi.org/10.1016/j.commatsci.2021.110721)

## Reader notes (navigation)

- Version-of-record narrative and full PDF: [[2021gao-computationa-molecular-dynamics]].

These sections summarize what the checked-in extraction and abstracts support where quoted above; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[2021gao-computationa-molecular-dynamics]]
- [[reaxff-family]]
