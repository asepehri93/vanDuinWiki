---
id: paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale-2
type: paper
title: "Pyrolysis of a large-scale molecular model for Illinois no. 6 coal using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.jaap.2014.07.011"
year: 2014
authors:
  - "Castro-Marcano, Fidel"
  - "Russo, Michael F., Jr."
  - "van Duin, Adri C. T."
  - "Mathews, Jonathan P."
venue: "Journal of Analytical and Applied Pyrolysis"
pdf_sha256: "4c03f50a358cf49794bdedf63e99766e95e64fe7d52ebfe2941c10b0fe04a45b"
pdf_path: "papers/Castro_JAAP_3246_proofs.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study applies **ReaxFF reactive molecular dynamics** to pyrolyze a **large-scale molecular assembly** of **Illinois No. 6 coal** represented by **728** diverse molecules in a simulation cell exceeding **50,000 atoms**. Pyrolysis is conducted at **2000 K** for **250 ps** and continued until roughly **60%** of **cross-links** have been thermally cleaved, a condition chosen so that chemistry occurs within a tractable simulation time at this elevated temperature. Initiation chemistry is attributed in the abstract to **hydroxyl release**, **dehydrogenation of hydroaromatic** moieties, and **cleavage of heteroatom-containing cross-links**. Reported **volatile** product classes include **hydrogen**, **methyl**, **ethylene**, **acetylene**, **formaldehyde**, **ethynol**, **alkylphenols**, **alkylnaphthalenes**, and **alkylnaphthols**, described as consistent with **experimental** tar and gas signatures. **Molecular-weight distributions** shift toward **lower** molar mass as thermal fragmentation proceeds, and **tar structural motifs** are compared with **literature** data.

## Methods

### Relationship to other ingests

- Same **JAAP** article and scientific protocol as **`[[2014castro-marcano-journal-of-a-pyrolysis-large-scale]]`**, but this `pdf_path` points at an **Elsevier proof** PDF (`papers/Castro_JAAP_3246_proofs.pdf`).

### ReaxFF coal pyrolysis setup

- **ReaxFF** **reactive MD** with the group’s **coal/CHONS** parameterization tracks **bond-order**-based bond formation/scission in the assembled **Illinois No. 6** molecular model (**abstract** on sibling page).

### Thermal schedule and stopping criterion

- **2000 K** for **250 ps**, continued until **~60%** of **cross-links** are disrupted (**abstract**).

### Sulfur-free control

- A **sulfur-free** duplicate model is run under the same schedule to isolate **organic sulfur** chemistry effects (**abstract**).

### Canonical detail

- For **timestep/thermostat** and **analysis** scripts, use the **final JAAP** issue PDF on **`[[2014castro-marcano-journal-of-a-pyrolysis-large-scale]]`** when available—not proof boilerplate alone.

### 1 — MD application (ReaxFF reactive MD)

- **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** per the shared **JAAP** abstract; **specific MD package** is **N/A in the pages 1–2 extract**—confirm in the **final** PDF.
- **System size & composition:** **>50,000 atoms**; **728** diverse **Illinois No. 6** molecules (abstract; extract for sibling slug).
- **Boundaries / periodicity / ensemble / timestep / thermostat / barostat:** **N/A —** not stated in the indexed extract; confirm in the **version-of-record** PDF.
- **Duration / stages:** **250 ps** at **2000 K** until **~60%** of **cross-links** are disrupted **primarily by thermolysis** (abstract).
- **Temperature:** **2000 K** (abstract).
- **Pressure / electric field / enhanced sampling:** **N/A —** not summarized in the abstract excerpt used here.

### 2 — Force-field training

**N/A —** application paper in the abstract framing (parameter provenance in the main text).

### 3 — Static QM

**N/A —** not the primary methodology in the abstract framing summarized here.

## Findings

### 1 — Outcomes and mechanisms

The abstract reports that **heteroatom-linked** cross-links (**sulfurated** and **oxygenated**) thermally degrade more extensively than purely **alkyl** linkages, indicating higher **reactivity** near **heteroatoms**. **Sulfur form** analysis distinguishes **aliphatic sulfur** as more rapidly mobilized than **thiophenic sulfur**, matching qualitative **experimental** expectations. Quantitative **heterocycle** decomposition extents in the abstract include **~57%** for **pyrrolic**, **~47%** for **thiophenic**, and **~29%** for **furanic** five-membered rings in the surveyed structures. Comparing **sulfur-bearing** versus **sulfur-free** trajectories, **aryl/alkyl C–S** bonds are found weaker than corresponding **C–C** bonds, so **C–S** cleavage yields **greater fragmentation** and higher evolution of **inorganic gases** and **tars** when sulfur is present—interpreted as **sulfur** accelerating **pyrolysis kinetics** in this model. The authors position **ReaxFF** plus representative **coal** structures as a practical probe of complex **pyrolysis** chemistry despite known force-field limitations.

### 2 — Comparisons

Qualitative alignment of **volatile/tar** chemistry and **sulfur speciation** trends with **experiment** is stated in the abstract (same scientific text as the issue PDF).

### 3 — Sensitivity

**Sulfur-free** duplicate trajectories isolate **organic sulfur** effects on **gas/tar** generation rates (abstract).

### 4 — Limitations (authored framing)

High **T** and short **ps** window vs laboratory **pyrolysis** timescales; see **## Limitations** for corpus-specific **proof-PDF** caveats.

### 5 — Corpus / KB honesty

This slug’s `pdf_path` is an **Elsevier proof** (`papers/Castro_JAAP_3246_proofs.pdf`). Prefer **`[[2014castro-marcano-journal-of-a-pyrolysis-large-scale]]`** for **version-of-record** bytes and for **Methods** details not carried in short extracts.

## Limitations

The corpus **`pdf_path`** is an **Elsevier proof** (`Castro_JAAP_3246_proofs.pdf`) with **author-query** boilerplate on **page 1**; pagination and figure placement may differ from the final issue. A single **high-temperature**, **short-time** window cannot represent full **reactor** residence-time distributions or **pressure** effects in industrial **pyrolysis**.

## Relevance to group

van Duin and Russo coauthorship on **ReaxFF** for **fossil** **energy** and **coal** **devolatilization** chemistry aligned with group **combustion** and **pyrolysis** modeling.

## Citations and evidence anchors

- “Please cite this article in press as…” DOI `http://dx.doi.org/10.1016/j.jaap.2014.07.011` (extract).
- Structured abstract fields (extract).

## Related topics

- [[reaxff-family]]
