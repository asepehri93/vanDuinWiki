---
id: paper:2023nadire-nayir-2d-materials-modeling-simulations
type: paper
title: "Modeling and simulations for 2D materials: a ReaxFF perspective"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
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
pdf_sha256: "12c4d1db3981b63c851d4e480b0c9785e182a18588a1d1595a744125911b728f"
pdf_path: "papers/Nayir_2D_materials_ReaxFF_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023nadire-nayir-2d-materials-modeling-simulations -->

## Summary

**2D materials** research routinely couples **experiment** with **simulation** because **edge** and **defect** chemistry can dominate **growth**, **etching**, and **stability**; **ReaxFF** offers a **reactive** **MD** route when **QM** is too costly for **large** systems or **long** timelines. Nayir et al. present an **IOP *2D Materials*** topical review of **ReaxFF** **developments and applications** targeting **2D materials** families including **graphene**, **transition metal dichalcogenides**, **MXenes**, **hexagonal boron nitride**, and **group III–V** sheets, including **heterostructure** examples. The uncorrected proof abstract on file explicitly lists layered and nonlayered two-dimensional systems together with mixed-dimensional van der Waals heterostructures as scope, and it states that the review closes with an outlook on future ReaxFF development needs and large-scale simulation opportunities for guiding experimental discovery. The manuscript organizes **parameterization** strategies (**classical** parabolic optimization versus **machine-learning-assisted** workflows), **simulation modalities** (standard MD, **accelerated sampling**, **force-biased Monte Carlo**), and **material-class** sections before closing with **outlook** on large-scale **ReaxFF** for **2D** discovery. The corpus **`pdf_path`** is **`papers/Nayir_2D_materials_ReaxFF_2023_galley.pdf`**, a **galley/proof** with production queries; a cleaner sibling ingest is **`[[2023nadire-nayir-2d-materials-modeling-simulations-2]]`**.

## Methods

**4 — Review / perspective (*2D Materials*).** The article is a **narrative** **survey** of how **ReaxFF** has been used for **2D** **TMDs**, **MXenes**, **hBN**, **group** **III–V** **sheets**, **nonlayered** **2D** **phases**, and **vdW** **heterostructures**, with **outreach** to **ReaxFF**+**continuum/phase-****field** **coupling** in **CVD/ALD-****themed** **stories** where the **cited** **primary** **work** did so. It does **not** own **one** **simulation** **input** **deck**; **N/A** to **assign** a **single** **timestep/thermostat** **for** the **Manuscript**—**timesteps**, **ensembles**, **QEq** **treatments**, and **rare-****event** **choices** **must** be **imported** **per** **DOI** **(10.1088/2053-1583/acd7fd)** from **the** **primary** **publications** **cited** **in** each **section**.

**ReaxFF** **parameterization** **(review** **only).** The **text** **compares** **conventional** **parabolic** **ReaxFF** **optimization** **to** **ML-****assisted** **parametrization** **in** **the** **literature**; **N/A** **as** a **new** **QM**-**driven** **fit** **by** **Nayir** *et* **al.**—**they** **catalog** **how** **others** **build** **and** **validate** **2D-****relevant** **parameter** **files**.

**MD** **/** **rare-****event** **(review** **only).** The **article** **discusses** **typical** **ReaxFF**+**LAMMPS** **choices**—**0.2–0.25** **fs** **in** **H-**containing** **RMD**, **NVT**/**NPT** **on** **slab** **models**, **and** **metadynamics/parallel-****tempering/force-****biased** **MC** **as** **used** **in** **cited** **work**—**N/A** **at** this **summary** **level** **as** a **repro** **package**; **N/A** **(new** **static** **DFT** **in** **this** **manuscript)**, **N/A** **(E-****field** **RMD** **authored** **as** a **stand-****alone** **case** **study** **in** the **review** **text)**, because **this** **DOI** **is** **synthesis** **+** **outlook**, **not** a **primary** **simulation** **paper**. **Corpus** **role:** this **slug** **registers** the **galley** file **`Nayir_2D_materials_ReaxFF_2023_galley.pdf`**; for **final** **layout** **use** **[[2023nadire-nayir-2d-materials-modeling-simulations-2]]** **or** a **library** **VOR** **PDF**.

**Cited-practice line (not one run).** Reviewed ReaxFF work commonly reports molecular dynamics in LAMMPS with 3D periodic boundary conditions, slab supercells with 10³–10⁴ atoms, 0.2–0.25 fs timestep, NVT or NPT ensembles, Berendsen or Nose–Hoover thermostat damping, 1 bar NPT when cited, ps equilibration, ns production where cited, and temperature from 300 K to >1000 K; **N/A** for a universal electric field recipe in every example.


## Findings

### Parameterization and validation trends (review-level)

Across surveyed literature, **2D** **ReaxFF** studies repeatedly pair **QM** training sets for **edge** and **defect** chemistries with **validation** against **DFT** or **experiment** on **small** cells before **large-scale** production runs. The review highlights **trade-offs** between **classical** **parabolic** optimization and **machine-learning-assisted** fitting when expanding element coverage for **heterostructure** interfaces.

### Sampling and rare events

For **etching**, **growth**, and **oxidation** under **operando**-relevant conditions, the review discusses when authors adopt **metadynamics**, **parallel tempering**, **force-biased Monte Carlo**, or long **MD** segments, noting that **barrier** heights and **nucleation** times remain sensitive to **collective-variable** choices.

### Outlook

The closing sections emphasize **dataset** gaps for **in situ** synthesis pathways and opportunities for **larger** **ReaxFF** campaigns when paired with **experimental** **in situ** probes—claims mirrored on the cleaner sibling page [[2023nadire-nayir-2d-materials-modeling-simulations-2]]. This **duplicate** slug chiefly preserves **PDF hash** provenance for the **`papers/Nayir_2D_materials_ReaxFF_2023_galley.pdf`** ingest.

## Limitations

**IOP** **galley** files sometimes retain **author query** **tags**; if your **OCR** or **extract** pipeline misfires on those pages, prefer **`[[2023nadire-nayir-2d-materials-modeling-simulations-2]]`**. **Galley** PDFs may differ in **figure quality**, **line numbering**, and **copy edits** from the **final** issue PDF. For **citations**, prefer **`[[2023nadire-nayir-2d-materials-modeling-simulations-2]]`** or the **publisher** PDF in your library. [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) covers **proof** duplicates.

**Confidence rationale:** `med`—galley duplicate; comprehensive prose delegated to VOR sibling.

## Citations and evidence anchors

**IOPscience** records **article type**, **submission** dates, and **CC-BY** licensing metadata that help disambiguate **galley** ingests from **final** issue PDFs. DOI: [10.1088/2053-1583/acd7fd](https://doi.org/10.1088/2053-1583/acd7fd).

## Reader notes (navigation)

**2D Materials** **reviews** are **high-traffic** entry points; when refreshing **`source_refs`** on **theme hubs**, ensure this DOI appears where **ReaxFF** **2D** **surveys** are cited as **evidence** for **method** **trends**.

- **Cleaner duplicate:** [[2023nadire-nayir-2d-materials-modeling-simulations-2]]
- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2023nadire-nayir-2d-materials-modeling-simulations-2]]
- [[reaxff-family]]
