---
id: paper:2022momeni-venue-paper
type: paper
title: "Supporting Information — A computational framework for guiding the MOCVD-growth of wafer-scale 2D materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:continuum-or-mesoscale
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:supporting-information
  - keyword:2d-materials
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-022-00936-y"
year: 2022
authors:
  - "Kasra Momeni"
  - "Yanzhou Ji"
  - "Nadire Nayir"
  - "Nuruzzaman Sakib"
  - "Haoyue Zhu"
  - "Shiddartha Paul"
  - "Tanushree H. Choudhury"
  - "Sara Neshani"
  - "Adri C. T. van Duin"
  - "Joan M. Redwing"
  - "Long-Qing Chen"
venue: "npj Computational Materials (Supporting Information)"
pdf_sha256: "bcf9c11ccd76d412666f4690b5d2a77d573781885e689b8049b79a01f0b12698"
pdf_path: "papers/Momeni_MOCVD_2D_npjCompMat_2022_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2022momeni-venue-paper -->

## Summary

This file is the **Supporting Information (SI)** PDF for the **npj Computational Materials** article **DOI [10.1038/s41524-022-00936-y](https://doi.org/10.1038/s41524-022-00936-y)** on the **CPM** multiscale framework for **MOCVD** growth of **wafer-scale 2D materials**, curated in full on **`[[2022momeni-npj-computat-computational-framework]]`**. The SI documents supplementary **methods** that complement the main text: **MOCVD** reactor **geometry** (Supplementary Figure 1), coupling of **macroscale** **Navier–Stokes** and **heat/mass transport** to **mesoscale** **phase-field** island growth and **nanoscale** **reactive MD** (including **ReaxFF** chemistry for **WSe₂**). The abstract of the main paper positions **CPM** as linking **CFD**, **phase-field**, and **MD** to interpret **precursor** delivery, **substrate rotation**, and **morphology** for **WSe₂** growth against **2DCC** experiments. The SI explicitly states that **WSe₂** films were grown in the **2DCC-MIP** facility at **Penn State**, grounding the modeled **furnace** geometry and boundary data in an experimentally characterized reactor rather than a generic schematic alone.

## Methods

**Macroscale (SI text):** The model solves **Navier–Stokes** with **pressure** and **buoyancy** (equation (1) in the SI), **continuity** (equation (2)), and **species transport** with **convection–diffusion** (equations (3)–(4)) for precursor concentrations **cᵢ**, diffusivities **Dᵢ**, and source terms **Rᵢ**. **Heat transfer** couples **convection** and **conduction** (equations (5)–(6)) with mixture properties; **boundary conditions** are tabulated in **Table 1** in the SI, with carrier-gas properties in **Supplementary Figure 3**.

**Mesoscale:** **Phase-field** treatment of **orientation-dependent** **edge energies**, **deposition rate**, **edge diffusion**, and **temperature** effects on **coverage** and **morphology** (as referenced in the SI introduction).

**Nanoscale:** **Reactive MD** with **ReaxFF**-based **precursor–surface** reaction chemistry for **WSe₂** (full precursor list and thermal protocol in article + SI).

This wiki page does not replace the SI equations; it points retrieval consumers to **`Momeni_MOCVD_2D_npjCompMat_2022_SI.pdf`** for **reproducibility** details.

<!-- blueprint-slots:v1 -->

### MD application — blueprint checklist (indexed text)

Use **`N/A`** where this **PDF role** or **short extract** does not restate a quantity; prefer linked **version-of-record** pages for definitive values.

- **Engine / code:** **LAMMPS** is the usual **reactive MD** engine when **ReaxFF** appears in this corpus; **N/A — additional engines** if not stated on this page.
- **System size & composition:** **Atom** counts / **stoichiometry** / **supercell** sizing are **N/A — not stated in the indexed extract** unless quoted above.
- **Boundaries / periodicity:** **Periodic boundary conditions (PBC)** are typical for slab/bulk models; **N/A — frozen layers / walls** if not stated here.
- **Ensemble:** **NVT** is typical for constant-volume production unless **NPT** is explicitly cited elsewhere for this entry.
- **Timestep:** **timestep** on the order of **0.25 fs** is common for **ReaxFF**; **N/A — exact fs** if not stated in the indexed text.
- **Duration / stages:** **Equilibration** and **production** lengths in **ps**/**ns** are **N/A — not stated** on this stub.
- **Thermostat:** **Nose–Hoover** / **Berendsen** / **Langevin** controls are **N/A — damping/time constant not stated** in the indexed pages.
- **Barostat:** **NVT** entries imply **N/A — barostat / hydrostatic pressure control** unless **NPT** is documented on the canonical article page.
- **Temperature:** **Temperature** setpoints (e.g., **300 K**) are **N/A — not restated** when this file is **SI/proof-only**.
- **Pressure:** **N/A — pressure / stress tensor** targets are **not stated** for this PDF role.
- **Electric field:** **N/A — external electric field / bias** not invoked on this page.
- **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not stated for the workflows summarized here.


## Findings

Scientific conclusions about **uniformity**, **coverage**, and **precursor** profiles are stated on **`[[2022momeni-npj-computat-computational-framework]]`**; the SI provides **numerical** **preamble** (mesh, BC tables, equation forms) that supports those claims. **Figure** and **table** references in publications should prefer the **version-of-record** article for citation stability.



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

**SI-only** ingest—no standalone article narrative here. **Reactive MD** segments remain **expensive**; **continuum** and **phase-field** parameters need **recalibration** per material stack. **Buoyancy** and **low precursor concentration** assumptions in the **gas** model should be checked against the **experimental** **carrier-gas** flow and **dilution** stated in the main text when porting **CPM** to other **MOCVD** chambers.

## Relevance to group

**Adri C. T. van Duin** co-authorship; **ReaxFF** embedded in a **multiscale** pipeline with **2DCC** **MOCVD** experiments.

## Citations and evidence anchors

- DOI: [10.1038/s41524-022-00936-y](https://doi.org/10.1038/s41524-022-00936-y)

## Reader notes (navigation)

- Main article: [[2022momeni-npj-computat-computational-framework]]

## Related topics

- [[2022momeni-npj-computat-computational-framework]]
- [[reaxff-family]]
