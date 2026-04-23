---
id: paper:2020dulong-venue-paper
type: paper
title: "Optimization of a New Reactive Force Field for Silver-Based Materials (ChemRxiv preprint PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.26434/chemrxiv.12280289.v1"
year: 2020
authors:
  - "Clément Dulong"
  - "Bruno Madebene"
  - "Susanna Monti"
  - "Johannes Richardi"
venue: "ChemRxiv (preprint)"
pdf_sha256: "f43c4d5fd1982512a7b5776c7851cc9344721908f9b03e83148e1db9581d32bd"
pdf_path: "papers/ReaxFF_others/Dulong_Monti_2020_Optimization_of_a_New_Reactive_Force_Field_for_Silver_-_Based_Materials_v1.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2020dulong-venue-paper -->

## Summary

This wiki slug tracks the **ChemRxiv v1** preprint PDF for **AgSCH-ReaxFF**, a **ReaxFF** reparameterization targeting **silver** clusters, slabs, and **thiol/thiolate** chemistry relevant to **self-assembled monolayers** and **metal–organosulfur** interfaces. The work overlaps substantially with the peer-reviewed **J. Chem. Theory Comput.** article [[2020clement-dulong-j-chem-theor-optimization-new]] (**DOI `10.1021/acs.jctc.0c00480`**), which should be treated as the **primary citable** reference for **quantitative** benchmarks and **final** supplementary tables. The preprint narrative describes **Monte Carlo force-field (MCFF)** optimization in **ADF** against **DFT** training sets containing **>120** **QM** structures, followed by validation **MD** in **ADF** and **LAMMPS** with **0.25 fs** timesteps, **Berendsen** thermostats (**5 fs** damping), and **~100 ps** segments for **SAM**-related snapshots (e.g., comparisons near **100 K** in cited figures).

## Methods

Parallel to the **JCTC** article: **MCFF** sampling of **ReaxFF** parameters against an extended **QM** training set (**>120** structures in the ChemRxiv abstract) spanning **silver** clusters/slabs and **silver–thiolate** chemistry. Validation includes **Ag₂₀** **pyramidal** **thiolate** adsorption benchmarks (compared with **gold** analogs in the authors’ discussion) and **SAM**-like **Ag(111)** assemblies. **MD** validation comparing **Ag** vs **Au** **SAM** structural motifs appears in the preprint/SI narrative. Because **`extraction_quality`** is **partial** for this **ChemRxiv** path, operators should prefer the **journal** PDF for exhaustive **parameter** listings and final **benchmark** tables.

**MD validation (as in the linked JCTC page):** ReaxFF molecular dynamics in ADF and LAMMPS; 0.25 fs timestep; Berendsen thermostat (5 fs damping); ~100 ps NVT-style segments for SAM snapshots; PBC supercells. Barostat: N/A for the quoted NVT validation windows. Hydrostatic pressure control: N/A for those NVT windows. Electric field: N/A. Umbrella/metadynamics: N/A.

## Findings

The parameter set improves **average** **cluster** and **slab** energetics vs legacy **Ag** **ReaxFF** descriptions; **Ag\(_{20}\)** **pyramidal** **thiolate** adsorption tracks **gold** benchmarks in the authors’ comparisons. **Low-coordination** **Ag** sites still show **edge-shortening** artifacts, flagged as a known limitation. **Ag(111)** **SAM** simulations do **not** reproduce **Au–S–Au** “staple” motifs seen for **gold**, consistent with differing experimental pictures for **silver** interfaces.

The ChemRxiv abstract also flags a persistent **ReaxFF** limitation: **under-coordinated** **edge** sites can show **shortened** **metal–metal** distances that are not fully captured, so cluster-edge geometries should be interpreted cautiously in downstream applications.

## Limitations

**Preprint** formatting may differ from **JCTC**; residual **low-coordination** errors; anchor **quantitative** claims to the **journal** version when possible. If **`pdf_sha256`** ever diverges between **ChemRxiv** revisions, update **`raw/MANIFEST.jsonl`** in a controlled ingest rather than silent overwrites.

## Reader notes (navigation)

Chunk consumers should prefer **`paper:2020clement-dulong-j-chem-theor-optimization-new`** for **primary** scientific text; this page remains valuable for **preprint** traceability and **SI** filename alignment during corpus migrations.

## Relevance to group

**Provenance** record for **ChemRxiv** blob; canonical benchmarks live under [[2020clement-dulong-j-chem-theor-optimization-new]].

## Citations and evidence anchors

- ChemRxiv: [10.26434/chemrxiv.12280289.v1](https://doi.org/10.26434/chemrxiv.12280289.v1)
- Published: [10.1021/acs.jctc.0c00480](https://doi.org/10.1021/acs.jctc.0c00480) — [[2020clement-dulong-j-chem-theor-optimization-new]]

## Reader notes (navigation)

- [[2020clement-dulong-j-chem-theor-optimization-new]]

## Related topics

- [[reaxff-family]]

## Curator note (2026-04-20)

Prefer **[[2020clement-dulong-j-chem-theor-optimization-new]]** for citable **science**; keep this slug for **ChemRxiv** provenance and version history when needed.

