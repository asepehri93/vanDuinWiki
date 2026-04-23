---
id: paper:2022nayir-carbon-190-2-atomic-scale-probing-2
type: paper
title: "Atomic-scale probing of defect-assisted Ga intercalation through graphene using ReaxFF molecular dynamics simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2022.01.005"
year: 2022
authors:
  - "Nadire Nayir"
  - "Mert Y. Sengul"
  - "Anna L. Costine"
  - "Petra Reinke"
  - "Siavash Rajabpour"
  - "Anushka Bansal"
  - "Azimkhan Kozhakhmetov"
  - "Joshua Robinson"
  - "Joan M. Redwing"
  - "Adri van Duin"
venue: "Carbon"
pdf_sha256: "fabc90e97aad0eda8f2dd2dbefa55cc98b556a59802c5db8f7984b53bc7812fe"
pdf_path: "papers/Nayir_Ga_graphene_galley_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022nayir-carbon-190-2-atomic-scale-probing-2 -->

This ingest uses an **Elsevier galley/proof-style PDF** for the same Carbon article (DOI [10.1016/j.carbon.2022.01.005](https://doi.org/10.1016/j.carbon.2022.01.005)); prefer **`[[2022nayir-carbon-190-2-atomic-scale-probing]]`** for the primary file naming in this repo when both exist.



!!! abstract "Scope"

Joint experiment and ReaxFF MD on Ga and TMGa on graphene with controlled vacancies, linking defect size to intercalation barriers and TMGa-assisted defect healing.

## Summary

Epitaxial 2D non-layered metals often rely on precursors such as trimethylgallium (TMGa) and metallic Ga interacting with graphene supports. Raman, XPS, and STM/STS experiments map defect distributions; ReaxFF molecular dynamics connects defect size and topology to adsorption, reaction temperatures, and intercalation pathways for Ga and TMGa. The study is framed around **2DCC**-style integration of **Ga-based** precursors with **CVD graphene** on **Cu**, where **defect-assisted** mass transport competes with **precursor decomposition** and **carbon healing** chemistry.

## Methods

**Canonical article page:** **`[[2022nayir-carbon-190-2-atomic-scale-probing]]`** (Elsevier version-of-record PDF). This slug is a **galley**/**duplicate** path in the corpus.

### A — Experiments

- **Raman**, **XPS**, **STM/STS** vs **defect** density—full protocols on VOR page.

### B — ReaxFF MD

- **Ga** / **TMGa** on **graphene** with **vacancy** motifs from **monovacancy** to **multivacancy** (**5–8–5**, etc.); **adsorption**, **barriers**, **passivation**—identical scientific content summarized on **`[[2022nayir-carbon-190-2-atomic-scale-probing]]`**.

### C — Quantum chemistry

- Supplementary **QM** benchmarks if any appear in the article—use VOR/SI.

### D — Provenance

- Use VOR for pagination and final figure labels when citing.

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

Defects strongly modulate Ga and TMGa adsorption and lower the temperature needed for Ga deposition. Multivacancy defects reduce the kinetic barrier to Ga intercalation through graphene, whereas migration through a single vacancy or 5–8–5 defects remains kinetically hindered. TMGa exposure can heal defects by passivating carbon dangling bonds with hydrocarbon and organometallic fragments, consistent with reduced Raman D:G ratio and STM images after Ga intercalation. Together, the results emphasize defect engineering as a handle for 2D metal integration.



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

ReaxFF models approximate electronic structure of graphene defects and organometallic chemistry; quantitative barriers should be read from the paper’s convergence tests. Experimental **Raman** and **STM** observables integrate over **ensemble** defect distributions, whereas simulations sample **idealized** defect motifs; mapping between them requires the **statistics** and **coverage** conditions stated in the main text.

## Relevance to group

Group-led collaboration on 2DCC graphene processing with ReaxFF interpretation.

## Reader notes (navigation)

- [[reaxff-family]]
- Sibling PDF: [[2022nayir-carbon-190-2-atomic-scale-probing]]
- **Corpus catalog (Elsevier galley duplicate):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) — prefer the sibling slug’s **`pdf_path`** when both exist locally for **VOR** pagination.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2022.01.005](https://doi.org/10.1016/j.carbon.2022.01.005)

## Related topics

- [[reaxff-family]]
