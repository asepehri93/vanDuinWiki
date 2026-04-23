---
id: paper:2023kritikos-venue-paper-2
type: paper
title: "Atomistic insight into the effects of electrostatic fields on hydrocarbon reaction kinetics (AIP author proof PDF)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:combustion
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/5.0134785"
year: 2023
authors:
  - "Efstratios M. Kritikos"
  - "Aditya Lele"
  - "Adri C. T. van Duin"
  - "Andrea Giusti"
venue: "J. Chem. Phys. (author proof / query PDF in corpus)"
pdf_sha256: "6d5f451fd98b8f360a429b986cf3b5bc6ac68fc23c76786fd1c6a1fbcddb4716"
pdf_path: "papers/Kritikos_efield_combustion_JCP_2023_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023kritikos-venue-paper-2 -->

!!! abstract "Corpus role"

**AIP author proof / query** PDF for the same **J. Chem. Phys.** article as **`[[2023kritikos-venue-paper]]`**; use that page for stable Methods, Findings, and citation locators.

## Summary

This ingest records an **AIP author proof / query** PDF for **Kritikos, Lele, van Duin, and Giusti**, *J. Chem. Phys.*, on **electrostatically biased** **hydrocarbon oxidation** and **combustion** (DOI **10.1063/5.0134785**). The science investigates how **external electric fields** couple to **ReaxFF** **charge equilibration**, **reaction barriers**, and **macroscopic** **n-dodecane + O₂** trajectories—topics summarized authoritatively on **`[[2023kritikos-venue-paper]]`** using the **version-of-record** PDF. This duplicate page exists because proof PDFs are common in the corpus and must remain traceable without confusing **page** citations.

## Methods

### Corpus role (galley / author proof)

Duplicate **AIP** proof PDF for **DOI** `10.1063/5.0134785`; **pagination** and **figure** labels may be **non-final**.

### Protocol pointer

Science layers (**DFT** charge benchmarks, **ReaxFF CHO-2016**, **NEB**, **bimolecular** collisions, **n-dodecane/O\(_2\)** **E-field** cells) are summarized on **`[[2023kritikos-venue-paper]]`**—use that page for **ensemble**, **dimensions**, and **field strengths**.

For retrieval convenience (mirroring the **VOR** summary): the article cross-checks **ReaxFF QEq** **polarization** under **fields** against **DFT**, uses **NEB** to quantify **barrier** shifts for selected **oxidation** vs **pyrolysis** steps, probes **bimolecular** collisions to separate **Lorentz** vs **Coulomb** contributions, and finally runs **large** **n-dodecane/O\(_2\)** cells to see how **fields** partition energy among **translation**, **rotation**, and **vibration** during **combustion**-like chemistry.

### 4 — Duplicate / proof PDF (no standalone protocol on this slug)

**N/A** — do **not** use this **AIP** **proof** file for **final** **pagination** or for **reproducing** full **MD** **enumerations**; all **engine**, **system**, **ensemble**, **E-field** **magnitudes**, and **DFT** **settings** **belong** on **`[[2023kritikos-venue-paper]]`**.

### Bridge to version-of-record **MD** keywords (for retrieval; see VOR for numbers)

**LAMMPS** + **ReaxFF CHO-2016** on **PBC** **supercells** with **0.25** **fs**-order **timesteps** and **NVT**/**NVE**-class **stages** over **ps**–**ns** for **gaseous** **n-dodecane**/**O\(_2\)**; **Hydrostatic** **pressure** in **bar**-scale **targets** is **N/A** for the **dilute**-gas **combustion** **examples** highlighted in the **abstract**, whereas **Nose–Hoover**/**Berendsen**-style **thermostats** appear in the **full** **article**; **E-field** magnitudes in **V** m\(^{-1}\) are **not** reprinted on this **proof** page.

## Findings

Mirror **`[[2023kritikos-venue-paper]]`** for substantive results; **do not** cite **page numbers** from this **proof** in external manuscripts.

**Retrieval:** keep this slug for **hash** provenance; deduplicate **chunks** with the **VOR** page by **DOI**.

**Chunk builders:** when both **proof** and **VOR** PDFs exist for **10.1063/5.0134785**, align **section** **anchors** and **page** **locators** with **`[[2023kritikos-venue-paper]]`** so **MAS** consumers do not ingest **pagination** from **non-final** **AIP** **proof** files.

For **science** **content**—**QEq** **vs** **DFT** **field** **polarization**, **NEB** **reaction** **barriers** under **electrostatic** **bias**, **Lorentz**-related **collisions**, and **combustion**-scale **temperature**/**pressure**-like **driving** forces in **dodecane**/**O\(_2\)** **flames**—treat the **version-of-record** **PDF** (see **`[[2023kritikos-venue-paper]]`**) as **authoritative**; this **proof** is only for **provenance** and can carry **uncertain** **pagination**. **Open** **question** routing: use the **JCP** **Discussion** and **outlook** there rather than this **wiki** for **post-publication** **kinetics** **uncertainties** **compared** to **experiment** or **laminar** **flame** **data**.

## Limitations

**Proof** PDFs carry **publisher queries**, provisional pagination, and sometimes **placeholder** metadata—**do not** cite this file’s page numbers as final. Prefer **`[[2023kritikos-venue-paper]]`**.

## Reader notes (navigation)

If automated pipelines ingest both **proof** and **VOR** PDFs for one DOI, keep **`pdf_sha256`** rows distinct and point wiki prose to the **published** slug for **Methods** details and **SI** references. **Field strengths** and **system sizes** reported in the **VOR** are the only defensible basis for comparing this work to **plasma** or **spark** experiments.

## Relevance to group

Duplicate **galley** registration for the **van Duin**/**Lele**/**Giusti** **field-coupled combustion** **JCP** article.

## Citations and evidence anchors

- DOI: [10.1063/5.0134785](https://doi.org/10.1063/5.0134785)

## Reader notes (navigation)

- Version of record: [[2023kritikos-venue-paper]]

## Related topics

- [[2023kritikos-venue-paper]]
- [[reaxff-family]]
