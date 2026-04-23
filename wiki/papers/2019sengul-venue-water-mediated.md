---
id: paper:2019sengul-venue-water-mediated
type: paper
title: "Water-mediated surface diffusion mechanism enables the Cold Sintering Process: A combined computational and experimental study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - material:oxide
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
source_refs: []
doi: "10.1002/anie.201904738"
year: 2019
authors:
  - "Mert Y. Sengul"
  - "Jing Guo"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Angew. Chem. Int. Ed. (2019)"
pdf_sha256: "04fd49aca69bba9b8ae26e3f7b0826445eaef1e1090ef6a0425b2d2ce51a6ecf"
pdf_path: "papers/Sengul_Angewandte_coldsintering_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019sengul-venue-water-mediated -->

## Summary

Cold sintering processes (CSP) densify ceramics at dramatically lower temperatures than conventional firing by exploiting transient liquid or surface chemistry that accelerates mass transport. This study couples experiments on ZnO with ReaxFF molecular dynamics to argue that water-mediated surface diffusion—not merely passive lubrication—explains reduced activation energies for grain growth observed under CSP conditions. The authors highlight acidic transient chemistry that makes Zn²⁺ surface adsorption kinetically accessible and show that hydroxylation promotes mobile surface species that accelerate diffusion and recrystallization rather than freezing the surface.

## Methods

**Experiments (CSP, ZnO + acetic acid + water).** *Angew. Chem. Int. Ed.* reports cold sintering of ZnO in the ZnO / acetic acid (HAc) / water system, varying HAc concentration (2 m, 4.6 m, and 9 m while the solvent amount is held fixed) and, after identifying the acid level that maximizes grain size (2 m HAc), comparing about 120 °C to about 300 °C processing. Densification, microstructure, and residual species (including grain-boundary acetate-related content at low T per SI) are characterized as in the paper and SI. The CSP stage narrative (solvent wetting, pressure-driven particle rearrangement, diffusive grain-boundary transport, solvent removal) follows the schematic and text in the VOR PDF at `pdf_path`.

**1 — MD application (ReaxFF).** Molecular dynamics with ReaxFF, typically in LAMMPS in this line of work (stated in *Angew.* + SI). ZnO surface and slab models with explicit H₂O and proton- or acid-related species are used to study zinc surface recrystallization and diffusivity under acidic transients, with 3D PBC. Ensemble (NVT or NVE class), timestep (0.1–0.5 fs in comparable Sengul-line runs), Nose–Hoover-class thermostat parameters, and segment lengths are tabulated in the VOR + SI; the wiki does not duplicate every ps/ns. ReaxFF QEq and nonbonded cutoffs appear in the SI. Barostat / NPT: see SI for any preequilibration; N/A for the main surface path if the primary runs are NVT/constant cell (confirm in VOR). Shear, shock, external uniform E-field, umbrella, metadynamics: N/A unless the SI states them.

**2 — Force-field training.** N/A (applies an established ReaxFF for ZnO and aqueous acidic surface chemistry; reparameterization is not the communication’s focus).

**3 — Static QM or DFT-only as sole output.** N/A; outcomes are experimental plus reactive MD.

**4 — Review / non-simulation.** N/A.

## Findings

**Outcomes and mechanisms (CSP + RMD).** The version-of-record text positions accelerated surface diffusion as a key cold-sintering mechanism: under CSP conditions, surface hydroxylation is not a purely passivating “lubricant” layer; the ReaxFF trajectories show orders-of-magnitude faster surface diffusion when hydroxyl/related surface complexes form, and zinc cation surface adsorption/recrystallization is discussed as a rate-limiting step under the explored acidic conditions.

**Comparisons and trends.** The experimental matrix varies HAc at fixed solvent load (2 m, 4.6 m, 9 m) and (after 2 m was used as a favorable case) compares low-T (~120 °C) to ~300 °C sintering: higher acid can lower final density and grain size in the VOR data; at 2 m HAc, the lower-temperature run shows smaller grains/lower densification and residual grain-boundary acetate-related chemistry that the SI links to temperature-limited removal—verify magnitudes in the VOR figures. The paper frames how transient aqueous/acid paths can change which step limits densification and grain growth versus bulk-lattice-only pictures.

**Corpus honesty.** Cite figure numbers and SI panels from the issue PDF; this wiki paraphrases the *Angew.* text and the indexed extract, not a substitute for the full VOR+SI.

## Limitations

Focus on ZnO means transferability to other CSP chemistries requires species-specific validation; ReaxFF cannot capture full electrolyte speciation without parameter testing.

## Corpus notes

If `normalized/papers/2019sengul-venue-water-mediated.json` exists, keep `extraction_quality` synchronized with the wiki after any SI PDF ingest, because cold-sintering papers often relocate extended data after peer review.

Angewandte articles frequently include multimedia; if the corpus ingests supporting videos of densification, reference them in `normalized/papers` metadata rather than embedding large binaries inside wiki markdown.

For educational summaries, emphasize that CSP is not “room-temperature magic” for every ceramic; the chemistry-specific windows emphasized here for ZnO still need independent validation per material system.

## Relevance to group

Strong experiment–simulation pairing with van Duin co-authorship on **reactive sintering** of oxides.

## Citations and evidence anchors

- DOI: [10.1002/anie.201904738](https://doi.org/10.1002/anie.201904738)

## Related topics

- [[reaxff-family]]
