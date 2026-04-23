---
id: paper:2018sang-nat-situ-atomistic-3
type: paper
title: In situ atomistic insight into the growth mechanisms of single layer 2D transition
  metal carbides
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- domain:reactive-md
- method:reaxff
- method:dft-static
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:galley-or-proof-pdf
- keyword:reaxff-application
- keyword:2d-materials
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1038/s41467-018-04610-0
year: 2018
authors:
- Xiahan Sang
- Yu Xie
- Dundar E. Yilmaz
- Roghayyeh Lotfi
- Mohamed Alhabeb
- Alireza Ostadhossein
- Babak Anasori
- Weiwei Sun
- Xufan Li
- Kai Xiao
- Paul R.C. Kent
- Adri van Duin
- Yury Gogotsi
- Raymond R. Unocic
venue: Nature Communications
pdf_sha256: 1dabf1f43d93ec96915f3f8f5c6fe46d599c628fd20745f8a6f83364cd2394fc
pdf_path: papers/Xiahan_Nature_Comm_MXene_defect_2018_galley.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018sang-nat-situ-atomistic-3 -->

Publisher **galley / uncorrected proof** PDF for the Nature Communications MXene growth article; the science matches [[2018sang-nat-situ-atomistic]].

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi`. For citation-ready text and figures, prefer the **version-of-record** PDFs on [[2018sang-nat-situ-atomistic]] or [[2018sang-nat-situ-atomistic-2]].

## Summary

In situ aberration-corrected STEM with heating shows homoepitaxial growth of hexagonal TiC adlayers on defunctionalized Ti₃C₂ MXene above roughly 500 °C, yielding Ti₄C₃- and Ti₅C₄-like compositions. Density functional theory and ReaxFF hybrid force-biased Monte Carlo and molecular dynamics rationalize adatom diffusion, binding, and step energies for Frank–van der Merwe growth of a single carbide layer. This **galley** ingest slug duplicates the **scientific** narrative on [[2018sang-nat-situ-atomistic]] while recording **PDF** provenance for the **uncorrected proof** file named in `pdf_path`.

## Methods

STEM and electron energy-loss spectroscopy use in situ heating in ultrahigh vacuum (order 10⁻⁹ Torr), annealing Ti₃C₂Tₓ flakes above 500 °C to remove terminators and nucleate TiC islands, with elemental mapping to distinguish carbide adlayers from bare Ti metal. Simulations combine DFT supercell energetics for h-TiC adlayers on Ti₃C₂ with ReaxFF-based hybrid fbMC/MD to capture bond-making and bond-breaking during growth on MXene surfaces.

**Instrument** **settings**, **temperature** **schedules**, **EELS** **acquisition** parameters, and **simulation** **cell**/**sampling** details are given in `papers/Xiahan_Nature_Comm_MXene_defect_2018_galley.pdf` and the **version-of-record** article PDFs cross-linked from [[2018sang-nat-situ-atomistic]].

**Atomistic modeling (DFT + ReaxFF fbMC/MD).** Same protocol family as the **version-of-record** article: **DFT** on **slab/supercell** models of **defunctionalized Ti\(_3\)C\(_2\)** with **h-TiC** adlayers, plus **ReaxFF-based hybrid force-biased Monte Carlo / molecular dynamics (fbMC/MD)** to capture **bond-making/bond-breaking** during **Frank–van der Merwe** growth. **Engine:** **molecular dynamics** with **ReaxFF** in the hybrid **fbMC/MD** workflow (**N/A — specific MD engine name** not in this note’s excerpt). **System:** periodic **supercells** containing the **MXene** template and adlayer (**N/A — atom counts** from article/SI). **PBC:** **three-dimensional periodic** supercells for DFT and coupled fbMC/MD as described in *Nature Communications* **Methods**. **Ensemble / timestep / production length:** **canonical** finite-temperature sampling is used in the published **fbMC/MD** workflow as described in *Nature Communications* **Methods** (**N/A — whether the authors label the segment explicitly as NVT vs another thermostat formulation** should be confirmed from the **PDF/SI** rather than this galley ingest page). **Thermostat / barostat:** **N/A — not stated** in the indexed galley excerpt used here. **Temperature:** **thermal** driving aligned with the microscopy conditions discussed (**~500 °C** with beam assistance; **1000 °C** thermal-only in the abstract narrative). **Pressure (hydrostatic):** **N/A — not used** in the atomistic models summarized here. **Electric field in MD:** **N/A — not used** as a classical MD bias (STEM beam effects are experimental). **Enhanced sampling:** **fbMC/MD** (**Monte Carlo** bond events + **MD**); **N/A — umbrella / metadynamics / replica exchange** not indicated in the indexed text for this work.
## Findings

Homoepitaxial TiC monolayers grow in a Frank–van der Merwe mode with Ti and C supplied from the MXene flake; h-TiC adlayers appear above 500 °C with beam assistance and at 1000 °C thermally. DFT highlights a balance of low adatom diffusion barriers, high h-Ti surface energy, step-edge penalties, and strong h-TiC binding that favors layered growth. EELS supports C-rich adlayer stoichiometry versus bare Ti metal.

The **combined** **STEM**/**theory** storyline emphasizes **layer-by-layer** **carbide** **accretion** on **defunctionalized** **MXene** rather than **metal** **islanding** alone, consistent with the **binding**/**step** **cost** balance summarized in the **DFT** section.

## Limitations

Proof PDFs can differ in wording and figure quality from the journal version. Electron-beam effects couple to thermal driving forces, and reactive force-field kinetics remain approximate versus experiment.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Multiple van Duin group contributors co-author; this slug records ingest provenance for the galley-stage file bytes.

## Citations and evidence anchors

- DOI: [10.1038/s41467-018-04610-0](https://doi.org/10.1038/s41467-018-04610-0)

## Reader notes (navigation)

- Primary curated pages: [[2018sang-nat-situ-atomistic]], [[2018sang-nat-situ-atomistic-2]].

## Related topics

- [[2018sang-nat-situ-atomistic]]
- [[reaxff-family]]
