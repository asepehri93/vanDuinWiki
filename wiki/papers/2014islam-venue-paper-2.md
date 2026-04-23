---
id: paper:2014islam-venue-paper-2
type: paper
title: "ReaxFF reactive force field simulations on the influence of Teflon on electrolyte decomposition during Li/SWCNT anode discharge in lithium-sulfur batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1149/2.005408jes"
year: 2014
authors:
  - "Islam, Md Mahbubul"
  - "Bryantsev, Vyacheslav S."
  - "van Duin, Adri C. T."
venue: "Journal of The Electrochemical Society"
pdf_sha256: "f8b9540a699a7d9411fcd69a077ad33af8549c9bff91e9c6d68cf599bd34b05c"
pdf_path: "papers/Islam_JES_2014_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014islam-venue-paper-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This ingest uses an author **proof** PDF (`Islam_JES_2014_proof.pdf`) for the same Journal of The Electrochemical Society article as DOI 10.1149/2.005408jes; the **version-of-record** text is mirrored under `paper:2014islam-venue-paper` with a different SHA (`Islam_JES_2014.pdf`). Islam, Bryantsev, and van Duin apply ReaxFF molecular dynamics to the Li/SWCNT composite anode interface with TEGDME electrolyte in lithium–sulfur cells, contrasting bare versus ex situ Teflon-coated scenarios. Lithium-rich interfacial regions promote electrolyte dissociation with ethylene as a prominent gaseous product; discharge exothermicity concentrates heat that accelerates further decomposition. A Teflon layer damps initial heat flow and suppresses lithium-driven electrolyte attack in the modeled sequences described in the abstract. The work targets interfacial degradation modes that limit Li–S cell calendar life when lithium plating occurs on conductive carbon supports.

## Methods

This slug ingests a **proof** PDF for the same **JES** article as **`[[2014islam-venue-paper]]`** (DOI **10.1149/2.005408jes**); protocol detail should be taken from the **version-of-record** PDF when possible.

### Reactive MD system (Li–S anode interface)

- **ReaxFF MD** models **Li/SWCNT** composite anode regions in contact with **TEGDME**-class electrolyte chemistry, contrasting **bare** vs **ex situ Teflon-coated** interface scenarios described in the abstract (**Summary**).

### Thermodynamic state and analysis

- **Ensemble**, **temperature**, **simulation duration**, and **electrode/electrolyte** construction follow the **JES** Methods section; this proof ingest may contain **layout typos**—prefer the **final** PDF for numbers.

### Post-processing

- Trajectories monitor **gaseous products** (e.g., **ethylene** highlighted in the abstract storyline) and **local heating** associated with **exothermic** decomposition pathways (**Summary**).

### Extract coverage

- `extraction_quality: partial` indicates incomplete local text dumps—consult **`[[2014islam-venue-paper]]`** and the **journal** PDF for authoritative tables/figures.

### 1 — MD application (same article as VOR)

- **System size & composition:** **Li/SWCNT** composite anode models with **TEGDME** chemistry as in the **JES** article (**Summary**); **exact atom counts** are **N/A — not re-keyed from this proof PDF in-repo**.
- **Engine / code / timesteps / thermostat / barostat / duration / PBC:** **N/A — not reliably extracted from this proof PDF in-repo**; use **`[[2014islam-venue-paper]]`** + **`papers/Islam_JES_2014.pdf`** for computational settings.
- **Ensemble:** **N/A — NVT/NPT not transcribed from this proof ingest** (see VOR Computational section).
- **Hydrostatic pressure / barostat:** **N/A — pressure control not transcribed from this proof ingest** (see VOR Computational section).
- **Electric field:** **N/A — not indicated** in the abstract-level summary used here.
- **Replica / enhanced sampling:** **N/A — not indicated** in the abstract-level summary used here.

## Findings

The **abstract** (mirrored in **`[[2014islam-venue-paper]]`**) reports **TEGDME** chemistry at **lithium-rich** anode regions with **ethylene** as a prominent **gaseous** product, **exothermic** discharge chemistry that creates **localized heating**, and that an **ex situ Teflon** surface treatment can **damp initial heat flow** and **suppress lithium-driven electrolyte decomposition** relative to **bare** interfaces in the modeled scenarios. **Quantitative** branching, rates, and temperature excursions should be read from the **version-of-record** **PDF** tables/figures, not from this **proof** layout.

## Limitations

Proof PDFs can contain layout artifacts; prefer **`[[2014islam-venue-paper]]`** for citation. Long-timescale solid–electrolyte interphase evolution is outside the reactive MD window.

## Relevance to group

van Duin authorship on Li–S interfacial chemistry and protective coatings.

## Citations and evidence anchors

- J. Electrochem. Soc. 161 (8) E3009–E3014 (2014); DOI `10.1149/2.005408jes`.
- Sibling VOR ingest: [[2014islam-venue-paper]]

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
