---
id: paper:2016harpale-venue-paper
type: paper
title: "Plasma-graphene interaction and its effects on nanoscale patterning"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.93.035416"
year: 2016
authors:
  - "Abhilash Harpale"
  - "Marco Panesi"
  - "Huck Beng Chew"
venue: "Physical Review B"
pdf_sha256: "4aaed5acd190faa7fbe3449febad6d49f7fe9d6a8caedb6601fdb86178bb0b14"
pdf_path: "papers/ReaxFF_others/Harpale_PRB_2016_Plasma-graphene_interaction.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:oxide-surface
  - keyword:dft-static
---
<!-- id:paper:2016harpale-venue-paper -->

## Summary

**Massively parallel reactive MD** with **ReaxFF** models **energetic hydrogen-ion** bombardment of **monolayer graphene** on an **α-quartz SiO₂** substrate to explain how **ion energy** selects among **edge-only etching**, **isotropic basal holes**, and **anisotropic (hexagonal) basal holes** in **hydrogen plasma** processing of graphene. The work is positioned as linking **single-impact** atomistic statistics to **morphology** trends seen when **ions** and **radicals** coexist in real **plasma** tools.

## Methods

- **Code:** **LAMMPS** reactive MD.
- **Potential:** **ReaxFF** for **Si/O/C/H** (bond-order, charge equilibration, vdW/Coulomb terms) with validation against **DFT** references for **H chemisorption barriers** (~**0.47–0.5 eV**), **sp²→sp³** distortions, and bond lengths/angles (values quoted in the paper).
- **Geometry:** **6.8 × 9.8 × 6.1 nm³** periodic cell; **2.1 nm** thick **α-quartz (001)** **O-terminated** substrate; **monolayer graphene** on top with small **in-plane mismatch strain (~0.07%)** for basal studies; separate **nanoribbon** models (**~4.2 nm** / **~5.8 nm** widths stated) for **edge** vs **basal** contributions.
- **Bridging:** MD-derived **edge vs basal** etching channels linked to a **micromechanics** model for **hole growth** at longer scales (ions + radicals synergy, per article).

**Timestep**, **thermostat** (**NVT** relaxation between impacts; damping values), **impact incidence**, and **statistics** over repeated impacts are specified in **`papers/ReaxFF_others/Harpale_PRB_2016_Plasma-graphene_interaction.pdf`** so abstract **ion-energy** windows map to explicit trajectories (**numerical thermostat parameters N/A — not transcribed here**). **Target temperature of the substrate / graphene between impacts (K):** **N/A — not transcribed from the partial extract used here**; read **PRB** §II for relaxation schedules. **Barostat / bulk hydrostatic control:** **N/A — constant-volume PBC** cell for the supported **graphene**/**SiO₂** stack described above (**imposed bulk pressure:** **N/A — not used** in this constant-volume bombardment setup).

## Findings

- Distinct **ion-energy windows** reproduce experimental diversity: **~1 eV** → **edge-limited** etching with **intact basal plane**; **~2 eV** → **isotropic** circular basal holes; **~20–30 eV** → **anisotropic** hexagonal basal holes (ranges stated in abstract and methods discussion).
- **Energetic ions** (and downstream dissociation products) are necessary to explain **basal-plane defect nucleation** and **morphology selection** beyond **H-radical-only** pictures.
- Results motivate **plasma condition tuning** (ion energy distributions) for **controlled graphene nanopatterning**.

**Basal** morphology is **not** universal: shifting the **ion-energy** distribution moves the system among **edge-limited**, **isotropic** basal holes, and **hexagonal** basal holes. **Basal** nucleation requires **higher** impact energies than **edge-limited** chemistry, matching **PRB** comparisons to **plasma** processing trends. **Ion energy** is the dominant simulation lever; reduced **plasma** chemistry and **MD** length scales are caveats (**Limitations**).

## Limitations

- Plasma chemistry is **reduced** to impinging **H species** on a **flat supported graphene** model; **experimental** ion/radical flux ratios vary with reactor conditions.
- **Time/length** scales remain **MD-limited**; continuum/plasma models are **not** resolved atomistically.

**Cross-sections, DFT validation energies, and full protocol tables** belong in the **PRB** PDF at `pdf_path` (and any **SI** cited there).

## Relevance to group

Strong **ReaxFF + LAMMPS** application on **graphene / SiO₂** with explicit **ion energy** as control knob—complements **interface** and **2D materials** threads in the corpus.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.93.035416](https://doi.org/10.1103/PhysRevB.93.035416) — *Phys. Rev. B* **93**, 035416 (2016).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
