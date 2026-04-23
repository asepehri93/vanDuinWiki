---
id: paper:2011si-vgomzi-metalclust-venue-paper
type: paper
title: "Supporting information: Au anion clusters (BIOGRF structures for Gomzi metal-cluster study)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-application
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: null
year: 2012
authors:
  - "Vjeran Gomzi"
venue: "Supporting information (Journal of Computational and Theoretical Nanoscience 9, 2012; related article doi:10.1166/jctn.2012.2041)"
pdf_sha256: "ceded8a8d38314c66bd6b830553b0ee00173a8ccca7d47c640d5ae4defa40669"
pdf_path: "papers/ReaxFF_others/SI-VGomzi-MetalClusters-JCTN.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2011si-vgomzi-metalclust-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This PDF is **supporting information** to V. Gomzi’s **Journal of Computational and Theoretical Nanoscience** article on **metal cluster** formation with **ReaxFF** (see companion wiki page **`paper:201215-33-29-tex-output-2-ctn03-2041`**). The extract on file consists largely of **BIOGRF 200** records listing **coordinates**, **connectivity**, and **energies (kcal)** for small **gold** species, including an **[Au]⁻** anion example and successive **Au\(_N\)** cluster segments—i.e., machine-readable **structures** backing tabulated SI rather than standalone narrative science.

## Methods

### 4 — Supporting information (non-article narrative)

This **`pdf_path`** is **supporting information** for V. Gomzi’s **JCTN** metal-cluster **ReaxFF** article ([[201215-33-29-tex-output-2-ctn03-2041]]; DOI **10.1166/jctn.2012.2041**). The indexed text in `normalized/extracts/2011si-vgomzi-metalclust-venue-paper_p1-2.txt` is dominated by machine-readable **BIOGRF 200** records: **`HETATM`** coordinates, **`CONECT`** connectivity, and a labeled **`ENERGY`** in **kcal** (`UNIT ENERGY kcal`), including an **[Au]⁻** example and successive **Au\(_N\)** segments (extract).

### 1 — MD application (atomistic dynamics)

This SI PDF does **not** define a standalone **molecular dynamics** protocol; it is a **structure/energy listing** companion to the primary article.

- **Engine / code:** **N/A — molecular dynamics** engine/package is **not identified** in this SI file; see **`paper:201215-33-29-tex-output-2-ctn03-2041`**.
- **System size & composition:** **Au** cluster segments appear as **BIOGRF** entries with explicit **atoms**/coordinates in the extract; **N/A —** the SI does not restate a single consolidated simulation supercell stoichiometry for dynamical runs.
- **Boundaries / periodicity:** **N/A —** **PBC** vs free-cluster boundary choices are **not stated** in the SI listing (see primary article **`pdf_path`**).
- **Ensemble:** **N/A —** **NVT**/**NPT**/**NVE** labels are **not stated** in the SI listing.
- **Timestep:** **N/A —** **fs**-scale timestep is **not stated** in the SI listing.
- **Duration / stages:** **N/A —** **production run** timing in **ps**/**ns** is **not stated** in the SI listing.
- **Thermostat:** **N/A —** thermostat method/damping is **not stated** in the SI listing.
- **Barostat:** **N/A —** **NPT** barostat usage is **not stated** (and **NVT** is not documented here either).
- **Temperature:** **N/A —** **temperature** control is **not stated** in the SI listing.
- **Pressure / stress:** **N/A —** **pressure** control is **not stated** in the SI listing.
- **Electric field:** **N/A —** **electric field** bias is **not stated** in the SI listing.
- **Replica / enhanced sampling:** **N/A —** **metadynamics**/**umbrella**/**replica exchange** are **not stated** in the SI listing.

### 2 — Force-field training

**N/A —** parameter fitting details are not contained in this SI structural dump.

### 3 — Static QM / DFT-only

**N/A —** not applicable as a standalone QM study PDF.

## Findings

**Corpus / KB honesty (primary):** This SI file does **not** present independent scientific conclusions in prose form; it archives **structures** and printed **total energies** for **Au** cluster segments. Any statements about accuracy vs **DFT**/experiment, convergence criteria, and the **ReaxFF** growth protocol should be taken from **`paper:201215-33-29-tex-output-2-ctn03-2041`** and its **`pdf_path`**.

**Comparisons / mechanisms / sensitivity:** **N/A —** not asserted here beyond numeric entries in the **BIOGRF** listings visible in the extract.

**Limitations:** Treat this slug as **provenance** for SI tables/structures, not as a substitute for the primary paper’s **Methods**/**Findings**.

## Limitations

- **SI-only** corpus artifact; read the **main JCTN paper** for motivation, protocols, and comparisons to DFT/experiment.

## Relevance to group

**Provenance record** for **ReaxFF metal-cluster** SI tied to the Gomzi **JCTN** study; keep linked to the primary article slug for retrieval.

## Citations and evidence anchors

- Parent article (same work): [10.1166/jctn.2012.2041](https://doi.org/10.1166/jctn.2012.2041) — see `wiki/papers/201215-33-29-tex-output-2-ctn03-2041.md`
- Extract pointer: `normalized/extracts/2011si-vgomzi-metalclust-venue-paper_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[201215-33-29-tex-output-2-ctn03-2041]] (paired primary article page)
