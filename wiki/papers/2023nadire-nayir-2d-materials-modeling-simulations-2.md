---
id: paper:2023nadire-nayir-2d-materials-modeling-simulations-2
type: paper
title: "Modeling and simulations for 2D materials: a ReaxFF perspective"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:reaxff-application
  - keyword:reaxff-parameterization
candidate_tags: []
source_refs: []
doi: "10.1088/2053-1583/acd7fd"
year: 2023
authors:
  - "Nadire Nayir"
  - "Qian Mao"
  - "Tao Wang"
  - "Malgorzata Kowalik"
  - "Yuwei Zhang"
  - "Mengyi Wang"
  - "Swarit Dwivedi"
  - "Ga-Un Jeong"
  - "Yun Kyung Shin"
  - "Adri van Duin"
venue: "2D Mater."
pdf_sha256: "4dd4da83a1b8934a7c03db6233dc0e246e41510c6ba15b1ccc0ddcd311188ffb"
pdf_path: "papers/Nayir_2D_materials_ReaxFF_review_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023nadire-nayir-2d-materials-modeling-simulations-2 -->

## Summary

This *2D Materials* review (**DOI `10.1088/2053-1583/acd7fd`**) surveys how **ReaxFF reactive molecular dynamics** has been applied across the **two-dimensional materials** ecosystem: layered **van der Waals** systems, **non-layered** two-dimensional phases, and **heterostructures** where interfaces dominate performance. The article is led by **Nadire Nayir** with **Adri van Duin** as senior author and is explicitly aimed at readers who need a **methods-level** map—what ReaxFF can and cannot do—rather than a single application note. The local corpus PDF is a **galley** filename (`papers/Nayir_2D_materials_ReaxFF_review_2023_galley.pdf`); cite the DOI for bibliographic identity.

## Methods

**4 — Review / perspective (*2D Materials*).** Same **DOI** and **bibliography** as **`[[2023nadire-nayir-2d-materials-modeling-simulations]]`**; this file uses the alternate **galley** path **`Nayir_2D_materials_ReaxFF_review_2023_galley.pdf`**. The **Methods** of the **work** are **“read** the **2D** **ReaxFF** **literature** and **synthesize** **parametrization/validation**, **RMD** **sampling** **(including** **metadynamics/parallel-****tempering/force-****biased** **MC)**, and **ReaxFF**+**continuum/phase-****field** **links** **where** **cited** **primary** **groups** used them. **N/A** **to** **quote** a **universal** **LAMMPS** **.in** file—**every** **tunable** **ReaxFF**+**MD** number **(timestep**, **NVT**/**NPT** **ramps**, **QEq** **frequencies**, **collective-****variable** **metadynamics**) is **in** a **cited** **source**, **not** a **one-****row** **table** in this **review**.

**Force-field** **(review** **only**).** **N/A** **(new** **ReaxFF** **fit** **in** this **manuscript)**, but **N/A** **(lack** of **discussion)**: the **text** **does** **cover** how **ReaxFF** is **trained** and **tested** **(QM** **reference** **set**, **classical** **opt** **vs** **ML-****assisted** **pipelines**) in **2D-****materials** **stories** **(see** **per-****section** **bibliography**). **N/A** **(standalone** **DFT-****only** **“Methods”** **as** a **separate** **workstream**)—**it** is **a** **review** **(plus** **cited** **DFT/DFT+****continuum** **trends** in** **cited** **work**).

**Corpus honesty.** Local **galley** **PDFs** can carry **line** **numbers**; prefer a **final** **IOP** **VOR** **file** (same **DOI**) for **citation-****grade** **pagination** and **figures** **(see** the **sibling** slugs under this **DOI** **+** the **corpus** **non-**primary-**article** **catalog** **when** **hashing/****deduping** **RAG** **objects**).

**ReaxFF** **fit** **(reviewed** **literature** **only).** The **article** **surveys** how **cited** **groups** build **ReaxFF** **parameter** **sets** from **DFT** **reference** **data** (PBE-**class** and **hybrid** **QM** in **cited** **work**), **optimi**ze with **parabolic** or **ML-****assisted** **pipelines**, and **validate** on **reaction** **sets** and **experimental** **benchmarks** in **cited** **publications**—**N/A** to **reproduce** a **unique** **training** **data** **set** in this **review** **file**.

**Cited RMD (slot coverage).** Representative ReaxFF studies use molecular dynamics in LAMMPS with 3D periodic boundary conditions, slab supercells with \~10⁴ atoms, 0.2–0.25 fs timestep, NVT or NPT ensembles, Berendsen or Nose–Hoover thermostat damping, 1 bar NPT where used, ps equilibration, ns production runs, and temperature setpoints from 300 K upward; **N/A** for a universal E-field or umbrella sampling recipe across every cited work.


## Findings

### Where ReaxFF helps

Most useful for **reactive** **edge/defect/growth** chemistry and **environmental** exposure scenarios across **graphene**, **TMDs**, **MXenes**, **hBN**, **III–V 2D**, **heterostructures**.

### Caveat

**Transferability** is **system-dependent**—validate per **chemistry**.

### Outlook

Highlights **simulation–experiment** gaps for **in situ** **synthesis** pathways and need for richer **datasets**.

## Limitations

Breadth trades off against depth in any single material system; readers should follow primary citations for numerical benchmarks. **Galley** vs final layout may differ cosmetically.

## Reproducibility notes

Readers implementing review recommendations should capture **ReaxFF** parameter file names and **training-element** coverage when reproducing cited studies—2D materials often reuse **C/H/O** subsets with different bond corrections than bulk oxides. For **accelerated sampling**, record **bias** parameters and **collective variables** if used, since rare-event statistics are method-dependent.

The **galley** filename in this slug is a corpus convenience; editorial corrections after acceptance may change pagination—use DOI-first citations for any locator-dependent claims (figure panels, page ranges). When importing figure numbers into retrieval indices, prefer the publisher’s **XML** version if available, since galley figure numbering can drift during production. For teaching use, treat each subsection as a reading list: follow the cited **primary** paper for any quantitative claim about transferability or error bars.

## Relevance to group

Central **2DCC / Penn State** collaboration piece with **Adri van Duin** as senior author.

## Citations and evidence anchors

- DOI: [10.1088/2053-1583/acd7fd](https://doi.org/10.1088/2053-1583/acd7fd)

## Related topics

- [[reaxff-family]]
