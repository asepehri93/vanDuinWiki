---
id: paper:2018bejagam-carbon-134-2-nanoparticle-activated
type: paper
title: "Nanoparticle activated and directed assembly of graphene into a nanoscroll"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:reaxff
  - domain:mechanics-tribology
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2018.03.077"
year: 2018
authors:
  - "Karteek K. Bejagam"
  - "Samrendra Singh"
  - "Sanket A. Deshmukh"
venue: "Carbon, 134 (2018) 43–52"
pdf_sha256: "1e150cf71f5ee97b849eda73715c46801575ad668d6dbf69e6fa9f86d99e3d86"
pdf_path: "papers/ReaxFF_others/Bejagam_Carbon_nanoscroll_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018bejagam-carbon-134-2-nanoparticle-activated -->

## Summary

**Reactive molecular dynamics (RMD)** with **ReaxFF** is used to show how **diamond**, **Ni**, **Pt**, and **Au nanoparticles** can **activate**, **guide**, and help **stabilize** **graphene nanoscroll (GNS)** formation from a **free-standing** graphene sheet, including cases where **metal surface atoms reconstruct** during wrapping.

## Methods

Values below are stated in the article PDF (`pdf_path`).

- **Interactions:** **ReaxFF**-based **RMD** in **LAMMPS**; **NVT** at **300 K**; **~5 ns** trajectories; **0.5 fs** timestep; large **300 Å** cubic cell; one end of the graphene sheet **fixed** to mimic clamped edges.
- **Systems:** **Diamond**, **Ni**, **Pt**, and **Au** nanoparticles with **10 Å**, **25 Å**, and **40 Å** diameters on graphene strips of varying width; nanoparticles placed at the **center** or **free edge** to probe initiation pathway.
- **Observables:** **Non-bonded** vs **bonded** contributions, **wrapping/scrolling** pathways, and **energy criteria** for complete scroll formation discussed in the article and SI.
- **System size / composition:** Representative strips such as **32 Å × 230 Å** graphene with **40 Å** nanoparticles (thousands of **atoms** including the metal or diamond cluster; other widths and NP diameters tabulated in the **PDF**).
- **Boundaries / periodicity:** **Three-dimensional periodic boundary conditions** on a **300 Å** cubic cell; one end of the graphene strip **frozen** to mimic a clamped ribbon (**Fig. 1** / text).
- **Thermostat:** **NVT** at **300 K** with thermostat implementation as specified in *Carbon* **Methods** (LAMMPS input details in article / SI).
- **Barostat:** **N/A —** constant-volume **NVT** cells; **no** bulk **NPT** hydrostatic control for the quoted nanoscroll trajectories.
- **Pressure:** **N/A —** no target **hydrostatic pressure**; **vacuum** **RMD** in the published protocol.
- **Electric field:** **N/A —** no applied field in the main **RMD** campaign (contrast with literature cases cited in the Introduction).
- **Enhanced sampling:** **N/A —** direct **~5 ns** **RMD** trajectories without umbrella sampling / metadynamics.

## Findings

- **Mechanism / outcomes:** Certain nanoparticle **sizes** and **placements** initiate **wrapping** or **scrolling** driven first by **graphene–NP** **vdW** interactions; **full** scroll formation and **stabilization** require balanced **graphene–graphene** and **NP–NP** interactions (**abstract**).
- **Comparisons:** **Ni** and **Pt** surfaces **reconstruct** during scrolling versus more inert **Au**, supporting stronger **metal–graphene** coupling in line with prior ordering **Ni > Pt > Au** cited from the literature.
- **Sensitivity:** **Diameter** (**10 / 25 / 40 Å**), **material** (**diamond**, **Ni**, **Pt**, **Au**), and **initial NP position** (center versus free edge) change whether **activation** leads to partial wrap versus a complete **GNS**.
- **Limitations / outlook:** The authors highlight **energy criteria** for completed **GNS** formation and position the study as a design route toward **metal–graphene** hybrids; **experimental** fabrication challenges noted in the Introduction remain outside the **RMD** scope.
- **Corpus honesty:** Protocol numbers (**300 K**, **0.5 fs**, **300 Å** cell, **~5 ns**) are taken from the *Carbon* article text indexed in-repo; cross-check any SI-only extensions against `pdf_path` / SI PDF.

## Limitations

Simulations are **vacuum** **NVT** runs at **300 K** with **fixed** edge constraints and a **large** periodic cell; they omit **solvent**, **substrate roughness**, and **experimental** deposition kinetics. **ReaxFF** accuracy for **noble-metal** **surface reconstruction** and **metal–carbon** binding should be checked when transferring conclusions to specific synthesis routes. Nanoparticle **diameter** and **placement** strongly affect pathway; the study’s conclusions are **demonstrative** rather than exhaustive over all morphologies.

The **energy criteria** for completed **GNS** formation (as discussed in the article) are useful for summarizing when **wrapping** transitions into a **stable** **scroll** versus stalled **partial** wrapping—details belong to the **Results** section and **SI** panels.

## Relevance to group

External **ReaxFF** application paper complementary to Penn State **nanocarbon** and **metal–oxide** interface studies: it highlights how **heterogeneous** **catalyst-like** particles can steer **graphene** **self-assembly** when **non-bonded** and **bonded** terms compete on **nanosecond** trajectories.

## Citations and evidence anchors

- DOI [10.1016/j.carbon.2018.03.077](https://doi.org/10.1016/j.carbon.2018.03.077); *Carbon* **134**, 43–52 (2018).

## Reader notes (navigation)

- Related slug in corpus: [[2018bejagam-venue-paper]]

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
- [[2018bejagam-venue-paper]]
