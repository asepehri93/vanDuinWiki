---
id: paper:2013senftle-venue-paper
type: paper
title: "Development of a ReaxFF potential for Pd/O and application to palladium oxide formation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - material:metal-surface
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4815820"
year: 2013
authors:
  - "Senftle, Thomas P."
  - "Meyer, Randall J."
  - "Janik, Michael J."
  - "van Duin, Adri C. T."
venue: "Journal of Chemical Physics"
pdf_sha256: "186a1dde056640a25d5bdb25272f773f3be8455b86d4e4c73c59dac852da3e9d"
pdf_path: "papers/Senftle_JCP_PdO_2013_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013senftle-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A new Pd/O ReaxFF description is fitted to quantum data for bulk and surface properties, then applied to high-temperature MD of oxide formation on Pd(111), Pd(110), and Pd(100). A hybrid grand canonical Monte Carlo / MD (GC-MC/MD) workflow is introduced to map a theoretical oxidation phase diagram for Pd₉₃₅ clusters from 300–1300 K and very low to 1 atm O₂ pressure, reporting faster subsurface oxygen transport on (110) versus other facets consistent with literature trends (abstract; introduction opening, extract). The motivation ties **Pd** **oxidation** to **catalyst** operation where **oxygen** **uptake** and **oxide** **wetting** on **facets** influence **activity**—motivating **atomistic** models coupled to **open** **O₂** **reservoirs** (introduction themes).

## Methods

Grounding: `papers/Senftle_JCP_PdO_2013_proof.pdf`; `normalized/extracts/2013senftle-venue-paper_p1-2.txt` (AIP author-query cover + abstract/introduction opening).

### 1 — MD application (ReaxFF MD of Pd oxidation + hybrid GC-MC/MD)

- **Engine / code:** **Molecular dynamics** simulations of **oxide formation** using a developed **Pd/O ReaxFF** potential (abstract). **Specific MD software** is **not stated** on the indexed excerpt pages.
- **System / surfaces:** **Pd(111)**, **Pd(110)**, and **Pd(100)** surfaces under **high temperature and pressure** conditions chosen to be **comparable across facets** for comparing **surface → subsurface oxygen transport** (abstract).
- **System size & composition (clusters):** The hybrid **GC-MC/MD** phase-diagram study targets **Pd\(_{935}\)** **clusters** (**935 atoms**) in contact with an **oxygen reservoir** as stated in the abstract (proof PDF text).
- **Hybrid sampling:** A **ReaxFF-based grand canonical Monte Carlo / MD (GC-MC/MD)** approach samples an **open O\(_2\) reservoir** while relaxing structures with **MD**, here applied to map oxidation of **Pd\(_{935}\)** clusters over **300–1300 K** and **\(10^{-14}\)–1 atm** O\(_2\) pressures to obtain a **theoretical oxidation phase diagram** (abstract).
- **Boundaries / periodicity:** N/A — **cell/cluster boundary conditions** details are **not stated** on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** N/A — **not stated** on the indexed excerpt pages (proof pages are mostly abstract/intro).
- **Temperature:** **300–1300 K** window stated for the **GC-MC/MD** diagram study (abstract); **MD oxidation simulations** are described as **high-temperature** without a tighter numeric range on p1–2.
- **Pressure:** **O\(_2\) pressures** **\(10^{-14}\)–1 atm** in the GC-MC/MD diagram study (abstract). N/A for a single **hydrostatic** mechanical pressure target (not the framing on p1–2).
- **Electric field:** N/A.
- **Replica / enhanced sampling:** **GC-MC/MD** is an **open-ensemble** sampling approach distinct from umbrella/replica exchange (abstract).

### 2 — Force-field training (Pd/O ReaxFF)

- **Parent FF / elements:** **ReaxFF** **Pd/O interaction potential** developed within the broader **ReaxFF** reactive force-field framework (abstract).
- **QM reference:** Parameters are fit against an **extensive quantum data set** for **bulk and surface properties** (abstract). **Specific DFT functional/basis/k-mesh tables** are **not stated** on the indexed excerpt pages—see full article Methods in `pdf_path`.
- **Training set / targets:** Includes **bulk Pd oxides**, **O-covered Pd surfaces**, and **Pd–O clusters** as summarized in the abstract’s “quantum data” statement.
- **Optimization:** **Parameter fitting** language is used at abstract level; **optimizer implementation details** are **not stated** on p1–2.
- **Reference data / validation:** Validation is claimed via **agreement with experiment** for **Pd\(_{935}\)** cluster oxidation over the stated **T–P** window and via consistency with **prior experimental surface oxidation trends** discussed in the introduction excerpt (**Pd(110) > Pd(100) > Pd(111)** ordering appears in introduction text).

## Findings

- **Outcomes & mechanisms:** **Oxygen** penetrates to **subsurface** regions **faster on Pd(110)** than on **Pd(111)** and **Pd(100)** under the abstract’s **comparable high-T/P** MD oxidation conditions.
- **Comparisons:** **GC-MC/MD** oxidation of **Pd\(_{935}\)** clusters matches **experiment** well enough across **300–1300 K** and **\(10^{-14}\)–1 atm** O\(_2\) to support both the **Pd/O potential** and the **hybrid method** (abstract).
- **Sensitivity / design levers:** Explicit **temperature** and **oxygen pressure** ranges are the thermodynamic knobs for the **cluster phase diagram** study (abstract).
- **Limitations & outlook:** The corpus PDF is an **AIP proof** with author-query boilerplate; **pagination and section numbering** may differ from the final issue—verify locators against the **published** article when available.
- **Corpus honesty:** `extraction_quality` is **partial** because the extract is dominated by **proof metadata**; quantitative MD settings and move definitions require **`pdf_path`** beyond p1–2.

## Limitations

Proof-stage PDF with author queries; normalized extraction flagged partial despite readable abstract block.

**Sampling:** **GC-MC/MD** **convergence** depends on **attempt** frequencies and **move** mix; check **SI** or **methods** tables for **equilibration** lengths before drawing **quantitative** **phase-boundary** conclusions.

## Relevance to group

van Duin as senior author on ReaxFF parameterization plus hybrid sampling methodology for catalytic metals.

## Citations and evidence anchors

- J. Chem. Phys. 139(4) proof header; DOI `http://dx.doi.org/10.1063/1.4815820` (extract page 2).
- Abstract text block (extract page 1–2).

## Related topics

- [[reaxff-family]]
