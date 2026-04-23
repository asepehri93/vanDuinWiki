---
id: paper:2014hantal-molecular-ph-atomic-scale-modelling
type: paper
title: "Atomic-scale modelling of elastic and failure properties of clays"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - method:reaxff
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:classical-ff
  - keyword:tribology
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1080/00268976.2014.897393"
year: 2014
authors:
  - "Hantal, György"
  - "Brochard, Laurent"
  - "Laubie, Hadrien"
  - "Ebrahimi, Davoud"
  - "Pellenq, Roland J.-M."
  - "Ulm, Franz-Josef"
  - "Coasne, Benoit"
venue: "Molecular Physics"
pdf_sha256: "12f12f2f9d848fdb22344baadd46b980b79ea8528d445638e196c2afcaa2fa7d"
pdf_path: "papers/ReaxFF_others/Hantal_Clay_ReaxFF_MolPhys_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014hantal-molecular-ph-atomic-scale-modelling -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

**Elastic moduli** of **illite** clay are compared using **ReaxFF** versus **ClayFF**, while **failure** under **tensile** and **shear** loading is studied primarily with **ReaxFF** (with **some ClayFF** cross-checks noted in the abstract). The work targets **layered silicate** **mechanics** relevant to **shale** and **clay** **aggregate** behavior, where **interlayer** **weakness** often controls **macroscopic** **toughness**. **Mode I** opening **normal** to **basal** planes shows **low** **fracture resistance** with **decohesion** in the **interlayer gallery**; **mode II** **shear** yields **interlayer** **stick–slip** without **through-thickness** **crack** **propagation**. **Weak** **non-covalent** cohesion between **T–O–T** sheets explains **low** **mode I** **toughness** and **easy** **layer** **sliding** under **shear** (abstract; extract).

## Methods

### Interatomic models

- **ClayFF:** **fixed-charge** clay force field used as a **baseline** for **elastic** property calculations on **illite** (**abstract**).
- **ReaxFF:** **bond-order** reactive model used for both **elastic** comparisons and **bond-breaking** during **failure** simulations (**abstract**).

### Elastic property calculations

- **Elastic moduli** of **illite** are computed with **both** **ReaxFF** and **ClayFF** to contrast **stiffness** predictions between reactive and non-reactive descriptions (**abstract**).

### Failure simulations (mode I vs mode II)

- **Mode I:** **tensile opening** normal to **basal** planes for a **crack-like** discontinuity **parallel** to **clay layers** (**abstract**).
- **Mode II:** **in-plane shear** loading on the same **layer-parallel** crack geometry (**abstract**).
- **ReaxFF** captures **fracture** and **sliding** pathways; **ClayFF** cross-checks appear where noted in the article for cases that do not require bond rearrangement.

### Protocol details

- **System sizes**, **loading rates**, **boundary conditions**, and **thermostats** are specified in **Molecular Physics** Methods; the short **`_p1–2` extract** carries abstract-level wording only.

### 1 — MD application (illite elastic + failure)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ClayFF** (elastic) and **ReaxFF** (failure pathways) as reported in **Mol. Phys.** (confirm version notes in **`pdf_path`**).
- **System / composition:** **Illite** clay models as described in **Mol. Phys.** (abstract).
- **Loading:** **Mode I** tensile opening normal to **basal** planes; **Mode II** in-plane shear on a **layer-parallel** crack-like geometry (abstract).
- **Boundaries / periodicity:** **3D PBC** supercells for layered **clay** simulations (**standard** for these **slab** models—confirm cell sizes in **`pdf_path`**).
- **Ensemble:** **NVT** **molecular dynamics** is typical for these **clay** deformation benchmarks unless the article specifies **NPT** segments—**N/A in this wiki summary** to quote the exact thermostat/ensemble string without reopening the PDF.
- **Timestep / thermostat / barostat / duration:** **N/A in the indexed extract**—confirm **Δt**, thermostat, **ps**/**ns** staging, and any **NPT** usage in **`pdf_path`**.
- **Temperature:** **temperature** set points for the **failure** runs are defined in **Mol. Phys.** Methods (**N/A in this wiki summary** to quote numerically).
- **Pressure / stress control:** **N/A — hydrostatic pressure** targets are **not** stated in the abstract excerpt; confirm whether **anisotropic stress** control appears for **mode I/II** loading in the PDF.
- **Electric field / metadynamics:** **N/A —** not part of the abstract-level description.

### 2 — Force-field training

**N/A —** compares **published ClayFF** and **ReaxFF** models rather than reporting a new parameterization in the abstract framing.

### 3 — Static QM

**N/A —** not a DFT-centric study in the abstract summary used here.

## Findings

### 1 — Outcomes and mechanisms

A **crack parallel to clay layers** subjected to **tension normal to the crack** shows **low fracture resistance**; **yield and fracture** proceed by **decohesion in the interlayer gallery** rather than **intra-layer** **Si–O** rupture. Under **shear**, failure is **stick–slip sliding between layers** without **crack propagation** as **lamellae** ride over one another. The **low mode I toughness** and **mode II interlayer sliding** follow from **weak non-covalent cohesion** between layers. The authors frame these **atomistic** trends as a **microscopic baseline** toward **polycrystalline** clay/shale failure models where **texture** and **pore fluid** will modify **effective** **toughness**.

### 2 — Comparisons

- **ReaxFF** vs **ClayFF** for **elastic moduli** of **illite**; **ReaxFF** primary for **bond-breaking** during **failure** (abstract).

### 3 — Sensitivity

- **Mode I vs mode II** loading highlights different **failure** modes (abstract).

### 4 — Limitations / outlook

- Idealized **illite** microstructures; **fluid** and **texture** effects deferred (**## Limitations**).

### 5 — Corpus / KB honesty

- **Modulus** numbers and **stress–strain** details must be taken from **`pdf_path`**, not the short extract alone.

## Limitations

Idealized **illite** microstructure; **polycrystalline** texture and **fluid** effects at **reservoir** scale are explicitly deferred in the abstract-level framing. **Pore** **pressure** and **ionic strength** in **clay** **galleries** are not represented in the **dry** **mechanics** benchmarks summarized here.

## Citations and evidence anchors

- DOI `10.1080/00268976.2014.897393` (Taylor & Francis landing link; extract header).
- Abstract (extract page 2).

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geo]]

## Reader notes (navigation)

When comparing **ReaxFF** to **ClayFF** here, treat **ClayFF** as a **fixed-charge** **baseline** for **elastic** properties and **ReaxFF** as the **reactive** model needed for **bond** **rupture** during **failure** simulations; **quantitative** **modulus** agreement between the two should be interpreted cautiously outside the **illite** **structures** tested.
