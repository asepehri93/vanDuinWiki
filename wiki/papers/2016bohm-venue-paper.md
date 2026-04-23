---
id: paper:2016bohm-venue-paper
type: paper
title: "ReaxFF+ — a new reactive force field method for ionic systems and its application to the hydrolysis of aluminosilicates"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:water-silica-geo
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:charge-equilibration
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b00720"
year: 2016
authors:
  - "Oliver Böhm"
  - "Stephan Pfadenhauer"
  - "Roman Leitsmann"
  - "Philipp Plänitz"
  - "Eduard Schreiner"
  - "Michael Schreiber"
venue: "J. Phys. Chem. C"
pdf_sha256: "73a305e83a8a78b028f4dd6041cef3b32402c88e92c49a024d03cd7744a86c28"
pdf_path: "papers/ReaxFF_others/Bohm_ReaxFF_JPCC_2016.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2016bohm-venue-paper -->

## Summary

**ReaxFF+** extends **ReaxFF** with a modified **charge-equilibration / bond-order** coupling aimed at **ionic liquids and gases**, where standard **QEq-style** treatments can struggle to represent **ionic vs covalent** character of the **same element types** simultaneously. The authors motivate **aluminosilicate hydrolysis** in **acidic/alkaline aqueous** environments, benchmark **cluster and reaction energetics** against **DFT**, and illustrate **ReaxFF+** on **large** reactive **MD** models—including **>20,000-atom** trajectories—using an **efficient MD** implementation. The corpus PDF is a **Just Accepted** *J. Phys. Chem. C* posting; cite the **version-of-record** for pagination-sensitive numbers when available.

## Methods

### MD application (atomistic dynamics)

**Engine / implementation:** reactive **MD** uses **ReaxFF+** in the **Tremolo-X** solver within **Atomistix ToolKit (ATK)** (as stated in the **Molecular dynamics simulations** subsection of **`pdf_path`**), motivated by access to **>20,000 atoms** and **>50 ps** trajectories for hydrolysis-in-solvent models.

**Integration / thermo–barostat:** **Δt = 0.2 fs** is used for time integration (“small enough to account for water molecule vibrations and rotations” in the article). **Nosé–Hoover** **thermostat and barostat** are used for temperature/pressure control (references **35–37** in the article).

**Illustrative aqueous supercell (liquid water benchmark):** a **~6.2 nm** cubic cell with **8000 H₂O** molecules is built on a grid with small random displacements/orientations, **pre-relaxed** with **conjugate gradients**, then cycled through short **NPT** segments (**300 K**, **1 bar**, **200 fs**) repeated with **CG** until a final **NPT** equilibration (**300 K**, **1 bar**, **60 ps**) yields stable averages (pressure, temperature, cell volume, hydrogen-bond energy). The authors report an **equilibrium density ~1378 kg m⁻³**, noting **overdensity** relative to experiment as a known **ReaxFF-family** limitation, while showing **reasonable O–H covalent** and **hydrogen-bond** lengths and **O–O RDF** peak positions vs experiment.

**Hydrolysis MERPs in solvent:** for selected **aluminosilicate hydrolysis** reactions, **minimum-energy paths** are computed with **ReaxFF+** inside a **cavity carved** from the equilibrated water supercell (van-der-Waals surface of the solute), yielding **>24,000 atoms** in **three-dimensional periodic boundary conditions** treated **only** with **ReaxFF+** in the reported large-scale path calculations.

**Electric field:** **N/A — not used** as a controlled external bias in the documented workflows. **Replica / enhanced sampling:** **N/A — not used** beyond standard **NPT** equilibration and **MERPs**.

### Force-field training (ReaxFF+ development)

**ReaxFF+** introduces a revised **charge-equilibrium scheme** combined with the **bond-order** framework so **covalent vs ionic** bonds can be distinguished more consistently for problematic cases in standard **ReaxFF/QEq** (see **Sections II–III**). Training/validation lean on **DFT** reference data (including **cluster ionics**, **water clusters**, and **aluminosilicate reaction energetics**), with **CP2K/Quickstep** **PBE-GGA** **GAPW** setups and **TZVP**-class bases described for the **DFT** portions, and **climbing-image NEB** for paths. The article also describes a **partially automated** parameter-generation workflow aimed at reducing manual **ReaxFF** fitting effort.

### Static QM / DFT

**QM** appears as the **reference generator** for energies/barriers and **NEB** benchmarks used to build and test **ReaxFF+**; it is **not** a separate “application DFT-only” study independent of the force-field development narrative.

## Findings

- **Ionic cluster / water-ion benchmarks:** the authors report that **ReaxFF+** reproduces **qualitatively correct ionic character** for illustrative **Na⁺·(H₂O)ₙ** and **OH⁻·(H₂O)ₙ** clusters (charge localization on **Na** vs **O** of **OH⁻**) and captures key **autoionization**/**deprotonation** charge distributions better than their baseline **ReaxFF** description in the same tests.
- **Energetics vs experiment/QM:** they note **H₂O···H₂O stabilization** is **underestimated** vs a cited experimental value (**-3.9 kcal mol⁻¹** vs **-5.57 kcal mol⁻¹**) but still “reasonably” reproduced for a reactive FF water model, and they emphasize simultaneous accuracy for **both** **Al(OH)₄⁻ → Al(OH)₃ + OH•** and **Al(OH)₄⁻ → Al(OH)₃ + OH⁻** dissociation energetics as a differentiator enabled by the new charge scheme.
- **Liquid-environment hydrolysis:** **Table 4** in the article compares **reaction** and **activation** energies for a representative **aluminosilicate hydrolysis** reaction in **vacuum**, with **Na⁺**, in **liquid water**, and in **water + Na⁺**, showing **ReaxFF+** vs **original ReaxFF** alongside **QM** references; qualitatively, **solvent** can shift **exothermicity** and **barrier ordering** relative to vacuum, and **Na⁺** effects differ between vacuum-like vs fully solvated setups.
- **Corpus honesty:** some PDF pages in this ingest show **stream decompression warnings** in automated text extraction; treat **tabular energies** and **MERP** details as authoritative only when read from a clean **VOR** PDF, and keep **`extraction_quality: partial`** until extracts are regenerated.

## Limitations

The corpus PDF is a **Just Accepted** manuscript (**ACS disclaimer** on the deposited PDF): figures, pagination, and numbers may change at **technical editing**. Prefer the **version-of-record** *J. Phys. Chem. C* PDF for authoritative barriers and elastic/bulk tables, then refresh `pdf_sha256` / `extraction_quality` / `normalized/papers/2016bohm-venue-paper.json` accordingly. **`extraction_quality: partial`** reflects incomplete first-pass text extraction for this slug.

## Relevance to group

Methodological extension of ReaxFF toward geochemistry-relevant silicate reactivity in electrolyte-like environments.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b00720](https://doi.org/10.1021/acs.jpcc.6b00720)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
