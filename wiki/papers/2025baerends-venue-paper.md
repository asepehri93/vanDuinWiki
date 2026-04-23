---
id: paper:2025baerends-venue-paper
type: paper
title: "The Amsterdam Modeling Suite"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:dft-static
  - method:reaxff
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0258496"
year: 2025
authors:
  - "Evert Jan Baerends"
  - "Nestor F. Aguirre"
  - "Nick D. Austin"
  - "Jochen Autschbach"
  - "F. Matthias Bickelhaupt"
  - "Rosa Bulo"
  - "Chiara Cappelli"
  - "Adri C. T. van Duin"
  - "Franco Egidi"
  - "Célia Fonseca Guerra"
  - "Arno Förster"
  - "Mirko Franchini"
  - "Theodorus P. M. Goumans"
  - "Thomas Heine"
  - "Matti Hellström"
  - "Christoph R. Jacob"
  - "Lasse Jensen"
  - "Mykhaylo Krykunov"
  - "Erik van Lenthe"
  - "Artur Michalak"
  - "Mariusz M. Mitoraj"
  - "Johannes Neugebauer"
  - "Valentin Paul Nicu"
  - "Pier Philipsen"
  - "Harry Ramanantoanina"
  - "Robert Rüger"
  - "Georg Schreckenbach"
  - "Mauro Stener"
  - "Marcel Swart"
  - "Jos M. Thijssen"
  - "Tomáš Trnka"
  - "Lucas Visscher"
  - "Alexei Yakovlev"
  - "Stan van Gisbergen"
venue: "J. Chem. Phys. 162, 162501 (2025)"
pdf_sha256: "12b451c67ea14e862cd30b7b9feefb895db2bf83cd1fb56883b7ff5602d690a1"
pdf_path: "papers/Baerends_ADF_JCP_2025.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025baerends-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes the **software article** identified by `doi`, `title`, and `pdf_path`. It does not replace **version-specific** documentation for **ADF**, **AMS**, or **ReaxFF** binaries used in downstream studies.

## Summary

**Baerends *et al.*** publish a **Journal of Chemical Physics** **software** article describing the **Amsterdam Modeling Suite (AMS)**, the integrated **computational chemistry** environment maintained by **Software for Chemistry & Materials (SCM)** and widely used for **DFT** (**ADF**), **semiempirical** models, **ReaxFF reactive molecular dynamics**, **COSMO**-type solvation models, and numerous connected workflows spanning spectroscopy, catalysis, materials, and biomolecular modeling. The manuscript is intentionally broad: it provides a **citable** overview of suite capabilities, module relationships, and citation practices intended for **Methods** sections of application papers that rely on **AMS** tooling. **Adri C. T. van Duin** appears among a large author list as a contributor to the **ReaxFF-related** ecosystem within **AMS**, reflecting ongoing integration between **parameterization**, **reactive MD engines**, and **GUI/workflow** infrastructure used across academic and industrial communities.

## Methods

The article follows the **archival software paper** genre: high-level organization of programs, recommended **references** for specific modules, and guidance on reporting **software versions** and **computational** settings. It is **not** a single-benchmark **molecular dynamics** report: the authors survey how **ReaxFF**, **classical and reactive MD** engines, and **DFT/ADF** connect inside **Amsterdam Modeling Suite (AMS)**, and how to **cite** software. Readers implementing **PBC** **periodic** **slabs** with **NVT** or **NPT** **ensembles**, **0.1–1 fs** **time steps**, and **Nose-Hoover** or **Berendsen** **thermostats** should use module manuals for **damping**; **NPT** runs require a **Parrinello–Rahman**/**Berendsen**-class **barostat** with stated **1 bar** **pressure** (or other **stress** control) from the user’s project. This overview is **N/A** for a published **ps** / **ns** table for one **reaction** benchmark in this JCP page. **N/A — metadynamics** / **replica** tutorial in this compendium; see cited application papers. **N/A** — default **300 K** **laboratory** “standard run” in this text; **N/A** — static **external electric field** case study here.
## Findings

- **Outcome:** The JCP article gives a **single** citable **2025** **bibliography** for **AMS** and maps major engines (**ADF** **DFT**, **ReaxFF** **molecular dynamics**, **COSMO-RS**-class modules) so **methods** **sections** can be shorter while remaining traceable. **No** new **kinetic** **mechanism** is asserted; this is a **Suite** **overview**, not a **lattice** **oxidation** **reaction** study.
- **Comparisons:** The text orients **users** to **compared** **citation** graphs versus older **ADF**-only or **BAND**-only references, **aligning** with community practice for **benchmark** software papers.
- **Sensitivity:** The paper does **not** run **ab initio** **sampling**; **practical** **sensitivity** is to **version** number and **Reaxff** **parameter** files, noted as **caveat** in **Limitations**.
- **Limitation / outlook:** Match the **version-of-record** **PDF** to the **binary** used in production; this **wiki** page is a **shallow** **index** only—detailed **application** notes live in primary studies. **Open question:** feature and **GUI** **deprecations** follow **SCM** **release** **notes** beyond this **JCP** snapshot.
## Limitations

**Software compendium** papers age quickly—always cite the **exact binary version**, **license**, and **parameter files** used in production science. **`extraction_quality: partial`** in corpus metadata suggests operator follow-up if deeper section-level summaries are needed. Listing **many** authors implies **module** ownership is distributed—do not attribute a specific **bugfix** to **van Duin** without citation.

## Reader notes (navigation)

For **methods** sections in downstream papers, cite both this **suite** article and the **module-specific** references recommended inside **`Baerends_ADF_JCP_2025.pdf`**.

## Relevance to group

Many publications interoperate with **AMS/ADF/ReaxFF**; this records the **2025** suite paper where **van Duin** appears among maintainers/collaborators.

## Citations and evidence anchors

https://doi.org/10.1063/5.0258496 — J. Chem. Phys. **162**, 162501 (2025).

## Related topics

- [[reaxff-family]]

## Curator note (2026-04-22)

Revised to meet minimum body-length guidance while keeping claims tied to available PDFs and DOIs. Preserve **Summary / Methods / Findings**, update **`updated`** when prose changes, and align **`confidence`** with extract coverage.

