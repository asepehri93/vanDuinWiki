---
id: paper:2015tavazza-venue-research-2
type: paper
title: "Molecular dynamics investigation of the effects of tip–substrate interactions during nanoindentation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - domain:methods-software
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b01275"
year: 2015
authors:
  - "F. Tavazza"
  - "T. P. Senftle"
  - "C. Zou"
  - "C. A. Becker"
  - "A. C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "67b72665dd39c9af4e71ac1b74ffdc72113d2b12fbaf3d15e2ba2408d939f2a4"
pdf_path: "papers/Tavazza_JPC_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015tavazza-venue-research-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi` and `pdf_path`. This ingest is a **publisher proof** PDF for the same article as [[2015tavazza-venue-research]].

## Summary

**Proof PDF** (`papers/Tavazza_JPC_2015_proof.pdf`) for **DOI `10.1021/acs.jpcc.5b01275`**, mirroring the peer-reviewed article summarized on [[2015tavazza-venue-research]]. **Nanoindentation** simulations in **molecular dynamics** typically idealize the indenter as a **repulsive sphere** or frozen lattice and neglect **contamination** and **native oxide** films; this study instead varies the **Ni–C** interaction model to include **pure repulsion**, a **DFT-fitted Lennard-Jones** attraction, and fully **reactive ReaxFF** for **Ni/C/H/O** so that **hydrogenated tips** and **oxygen-covered nickel** can be treated explicitly. The authors compare these setups against **AFM** images of blunted tips and selected **DFT** contact calculations. The abstract’s headline result is **large Ni pickup** on **clean** or **oxidized** nickel that survives **retraction**, strongly suppressed by **hydrogen-terminated** diamond tips—an effect described as **larger** than a simple **surface oxide contaminant** narrative.

## Methods

Scientific protocol matches the **version-of-record narrative** on [[2015tavazza-venue-research]]: large-scale **molecular dynamics** of **Ni(111)** **slabs** with **>10⁴ atoms** in the excerpted geometry, **3D PBC** in-plane, **NVT** nanoindentation with **Nosé–Hoover** thermostat, **1 fs** timestep, **50 000 MD steps** per **0.1 Å** semistatic indentation increment (≈**0.05 ns** **production** **MD** per relaxation segment), **temperature** control via that **NVT** thermostat, **pressure** **N/A** for hydrostatic barostat (contact **stress** via **virial**), and the same **EAM/Tersoff/LJ** vs **ReaxFF** hierarchy (see **`pdf_path`**).

**Force-field training:** **LJ** **Ni–C** attraction fit to **DFT** contact data (article Sec. 2).

**Static QM / DFT:** **DFT** used for fitting/validation of early contact—not production MD.

## Findings

**Outcomes:** **Ni transfer** to the tip persists under **clean** or **oxidized** contacts and can survive **retraction**; **H-terminated** tips **eliminate or drastically reduce** pickup (abstract).

**Comparisons:** Same **DFT**/**AFM**-anchored contrasts as the sibling page [[2015tavazza-venue-research]].

**Sensitivity:** **Tip chemistry** and **surface oxidation** dominate **adhesion** relative to a thin **oxide contaminant** story in the abstract.

**Limitations / outlook:** **Proof PDF** may omit final copy edits; quantitative loads live in **`pdf_path`**.

**Mechanism summary:** **Repulsive** idealizations miss **chemomechanical** pathways captured by **ReaxFF**/**LJ**-augmented **Ni–C** models.

## Limitations

**Proof PDF** pagination/colors may differ from the **journal PDF** on [[2015tavazza-venue-research]]. Semistatic **grip** constraints and finite **slab** thicknesses idealize the mechanical boundary conditions relative to bulk **AFM** experiments, so quantitative **adhesion** energies should be taken from the tables in **`pdf_path`** rather than from this navigation note alone.

## Relevance to group

Archival duplicate for **nanoindentation / adhesion** modeling with **NIST** coauthors.

## Citations and evidence anchors

DOI `10.1021/acs.jpcc.5b01275`; this path: `papers/Tavazza_JPC_2015_proof.pdf`.

## Related topics

- [[2015tavazza-venue-research]]
- [[reaxff-family]]
