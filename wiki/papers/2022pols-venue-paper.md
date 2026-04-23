---
id: paper:2022pols-venue-paper
type: paper
title: "Supporting Information — What happens at surfaces and grain boundaries of halide perovskites (CsPbI3)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - material:widegap-semiconductor
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.2c09239"
year: 2022
authors:
  - "Mike Pols"
  - "Tobias Hilpert"
  - "Ivo A. W. Filot"
  - "Adri C. T. van Duin"
  - "Sofía Calero"
  - "Shuxia Tao"
venue: "ACS Appl. Mater. Interfaces (Supporting Information)"
pdf_sha256: "9e2bd28be80275a40bde00aa82f738ea15564d55a7774ebd9bd582a0097c89e9"
pdf_path: "papers/Pols_ACS_AMI_CsPbI3_2022_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2022pols-venue-paper -->

## Summary

Supporting Information (SI) packages accompany peer-reviewed articles to archive extended data—supercell dimensions, additional figures, convergence tests, supplementary trajectories, and parameter tables—that cannot fit in the main text. This wiki slug registers the **SI PDF** for the ACS Applied Materials & Interfaces article **“What Happens at Surfaces and Grain Boundaries of Halide Perovskites: Insights from Reactive Molecular Dynamics Simulations of CsPbI\(_3\)”** (DOI **`10.1021/acsami.2c09239`**). Per **`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`**, SI-primary ingests are **not** the recommended standalone version-of-record article PDF; scientific conclusions, abstract language, and pagination should be cited from the main article PDF curated as **`[[2022mike-pols-acs-what-happens]]`** (or the sibling galley slug **`[[20220000-0002-1068-9599-x-manuscript]]`** where that row tracks production bytes). The SI nonetheless matters for reproducibility: it typically documents structural models for CsPbI\(_3\) surfaces and grain boundaries, extra ReaxFF validation (energies, radial distribution functions), and additional analyses of iodine connectivity evolution referenced in the main text. Halide perovskite stability is sensitive to moisture, illumination, and temperature; the SI materials help readers separate classical thermal degradation results from photophysical effects absent in ground-state ReaxFF.

## Methods

**Primary Methods** (ReaxFF **Cs–Pb–I**, surface/GB models, production MD): **`[[2022mike-pols-acs-what-happens]]`**. This slug is the **SI PDF** only.

### A — Force field tables

- **Extended** **ReaxFF** parameters, **validation** energies, and **supercell** dimensions: **SI** tables linked from the main article.

### B — Supplementary MD protocols

- Additional **relaxation** tolerances, **RDF** panels, and **trajectory** excerpts: **SI** sections (labels vary—use in-PDF headings).

### C — Quantum chemistry

- Any **DFT** **single-points** or **cluster** benchmarks relegated to **SI**: cite section in **`Pols_ACS_AMI_CsPbI3_2022_SI.pdf`**.

### D — Experiments

- **Experimental** comparison materials remain in the **main** **ACS AMI** article; **SI** may hold extra **microscopy** or **spectroscopy** plots referenced from the main text.

Do not duplicate lengthy **SI** tables in this wiki; cite **DOI** + **SI** section when reproducing simulations.

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

The SI supports—not replaces—the primary conclusions in the main article: relative stability ordering of facets and boundaries, Pb–I connectivity motifs (corner-, edge-, and face-sharing polyhedra), and the role of defects and grain-boundary geometry in thermal degradation pathways. Any quantitative value quoted for publication should appear identically in the main text or figures unless it is explicitly SI-only material; avoid inferring new numerical results from filenames alone. For reproducibility reviews, SI sections often hold the supercell lattice vectors and extra RDF plots that main-text page limits omit.



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

SI-only corpus rows lack the main-text narrative context; classical ReaxFF cannot capture photogenerated carriers or excited-state chemistry without additional models. If the main PDF is updated in a future corpus refresh, synchronize SI page references accordingly.

## Relevance to group

van Duin-group ReaxFF validation materials for halide perovskite interfaces and microstructure.

## Citations and evidence anchors

- DOI: [10.1021/acsami.2c09239](https://doi.org/10.1021/acsami.2c09239) — SI PDF: `papers/Pols_ACS_AMI_CsPbI3_2022_SI.pdf`.

## Reader notes (navigation)

- **Main article:** [[2022mike-pols-acs-what-happens]] (`papers/Pols_ACS_AMI_CsPbI3_2022.pdf`).

## Related topics

- [[2022mike-pols-acs-what-happens]]
- [[reaxff-family]]
