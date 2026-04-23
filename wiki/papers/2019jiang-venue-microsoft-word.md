---
id: paper:2019jiang-venue-microsoft-word
type: paper
title: "Interfacial and Electronic Properties of Heterostructures of MXene and Graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - task:application
  - material:graphene-carbon-nano
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:graphene-carbon
source_refs: []
doi: "10.1103/PhysRevB.99.085429"
year: 2019
authors:
  - "Rui Li"
  - "Weiwei Sun"
  - "Cheng Zhan"
  - "Paul R. C. Kent"
  - "De-en Jiang"
venue: "Phys. Rev. B 99, 085429 (2019)"
pdf_sha256: "f8bcb639752ce4b714bc654962e1583b5cc24bcebbd907593ea8eb3648efb1ac"
pdf_path: "papers/Others/Jiang_Kent_PRB_MXene_graphene.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019jiang-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    The repository filename reflects **submission** naming; the article is **plane-wave DFT** of **MXene/graphene** stacks (**not** **ReaxFF**).

## Summary

Stacking two-dimensional crystals creates interfacial dipoles that can move Fermi levels and reshape graphene’s Dirac cones even when the individual sheets are nominally semi-metallic. **Plane-wave DFT** compares **MXene** (**Ti\(_3\)C\(_2\)T\(_2\)**) **/ graphene** **heterostructures** with varied **termination (T)** and **stacking** arrangements, including sandwich geometries with MXene–graphene–MXene and graphene–MXene–graphene layer orders as summarized in the abstract. **Adhesion**, **work-function-driven charge transfer**, and **band shifts** (including **Dirac cone** motion in **monolayer graphene**) depend on **both** **T** and **stack**. The authors report that hydroxyl-terminated MXene couples most strongly to graphene in their survey, with an interaction-strength ordering summarized as OH > O > F for the terminations studied. **Charge** flows **from MXene to graphene** for fully hydroxylated surfaces but reverses for oxygen- and fluorine-terminated cases, producing opposite Dirac-point shifts. **Bilayer graphene** on **MXene** can develop **interlayer** **polarization** and **K-point** **gaps** for certain stackings, attributed to field-like interfacial dipoles rather than bulk insulating behavior in isolated graphene. The repository filename reflects an author list variant; the published **Phys. Rev. B** authorship and DOI in front matter are authoritative for citations.

## Methods

### 1 — MD application (atomistic dynamics)

**N/A** — this is a **static 0 K** first-principles study; there is no production MD, ReaxFF, or finite-temperature ionic sampling.

### 2 — Force-field training

**N/A** — no force-field fit; interatomic interactions enter only through **Kohn–Sham** DFT.

### 3 — Static QM / DFT

**Code:** **VASP** with **PAW** potentials and the **GGA–PBE** exchange–correlation functional. **Dispersion:** **Grimme DFT–D3** with **zero damping** for **vdW** interactions between stacked layers. **Basis / cutoff:** **plane waves** with **500 eV** cutoff. **k-sampling:** **(4×4×1) Monkhorst–Pack** mesh. **Supercells:** **(4×4)** **Ti\(_3\)C\(_2\)T\(_2\)** matched to **(5×5)** **graphene** to limit lattice mismatch; a **15 Å** vacuum separates periodic slabs along **z**. **Structures and pathways:** relaxed **M–G** (`M_G`), **M** with **AA/AB** bilayer graphene, and **G–M–G** / **M–G–M** sandwich stackings (terminations **T =** O, OH, F at **fcc** hollow sites on **Ti\(_3\)C\(_2\)**). **Convergence:** total energy **10\(^{-5}\) eV** and forces **0.02 eV/Å** as stated. **Properties computed:** **adhesive energy** per interfacial area, **Bader** / interfacial **charge transfer**, and **band structures** with **graphene** projection (including **Dirac** point shifts and **K-point** **gaps** in bilayer cases).

## Findings

### Mechanisms (interfacial electrostatics)

**Ti\(_3\)C\(_2\)(OH)\(_2\)** couples **most strongly** to **graphene** (**OH > O > F** trend in the abstract). **Charge transfer direction** flips with **termination**: **MXene → graphene** for **(OH)\(_2\)**, **opposite** for **O** and **F**, moving **Dirac** points accordingly. **Bilayer graphene** under **MXene** can develop **K-point** **gaps** from **interfacial** **dipole** fields.

### Limitations

**0 K** **static** **DFT**; **no** **explicit** **solvent** or **finite-temperature** **ionic** disorder.

## Limitations

**Static 0 K** **DFT**; **no** **finite-temperature** **ionic** **dynamics** or **solvent**.

## Relevance to group

**2D stack** **electronics** reference adjacent to **ReaxFF** **battery** **electrode** materials research.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.99.085429](https://doi.org/10.1103/PhysRevB.99.085429)
- `papers/Others/Jiang_Kent_PRB_MXene_graphene.pdf`

## Reader notes (navigation)

- 2D stacks (DFT, not ReaxFF): [[graphene-nanocarbon]], [[theme-2d-epitaxy-growth]].

## Related topics

- [[graphene-nanocarbon]]
