---
id: paper:2013poovathingal-venue-jp3125999
type: paper
title: "Large scale computational chemistry modeling of the oxidation of highly oriented pyrolytic graphite"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:validation-experiment
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1021/jp3125999"
year: 2013
authors:
  - "Savio Poovathingal"
  - "Thomas E. Schwartzentruber"
  - "Sriram Goverapet Srinivasan"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "d5001a1a80e1f1424d4c21704a7ec9fa07f6882ce6adbf959f540819e2a84430"
pdf_path: "papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013poovathingal-venue-jp3125999 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

Large-scale reactive MD studies the oxidation of highly oriented pyrolytic graphite (HOPG) by a hyperthermal (5 eV) atomic oxygen beam, using a C/H/O ReaxFF parametrization with additional checks against ab initio energies relevant to oxidation. Multilayer graphene models undergo many sequential O-atom impacts; simulations show an oxygen-covered precursor state followed by carbon removal that forms wide, shallow etch pits consistent with experiment. Product rankings match experiments: O\(_2\) (via recombination) most abundant, then CO\(_2\), with CO least abundant. Recombination occurs across the surface, while net carbon removal is localized near pit edges. Small-model defect studies and pit trajectories give dominant activation energies of about 0.30, 0.52, and 0.67 eV for pathways leading to O\(_2\), CO\(_2\), and CO, respectively.

## Methods

Grounding: `papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013.pdf`; `normalized/extracts/2013poovathingal-venue-jp3125999_p1-2.txt` (abstract + introduction excerpt).

### 1 — MD application (large-scale reactive bombardment)

- **Engine / code:** **Large-scale molecular dynamics** simulations using the **ReaxFF** reactive classical **force field** (abstract); **specific MD package** is **not named** on the indexed excerpt pages—confirm in the full PDF.
- **System size & composition:** **HOPG** is modeled as **multilayer graphene** with **etch-pit formation/evolution** driven by **many sequential atomic oxygen collisions** on an enlarged surface versus prior small-cell work (abstract; introduction excerpt).
- **Boundaries / periodicity:** **Three-dimensional periodic boundary conditions** are implied for extended **graphene sheet** models in this MD setting; **exact cell vectors and vacuum gaps** are **not stated** in the indexed excerpt.
- **Ensemble:** N/A — **NVE/NVT/NPT** choice and **thermostatting model for the beam/surface** are **not stated** in the indexed excerpt.
- **Timestep:** N/A — **integration timestep (fs)** is **not stated** in the indexed excerpt.
- **Duration / stages:** The protocol is framed as **longer-time / larger-area** sequential-impact MD than prior small graphene studies (introduction excerpt); **explicit ps/ns production lengths** are **not stated** on p1–2.
- **Thermostat / barostat:** N/A — **not stated** in the indexed excerpt.
- **Temperature:** Experimental motivation cites **high-temperature gas** contexts (e.g., reactor examples in the introduction excerpt); **simulation temperature(s)** for the reported HOPG runs are **not stated** on p1–2.
- **Pressure:** N/A — **not stated** in the indexed excerpt (beam energy is specified instead of bulk pressure control).
- **Beam / shock-like loading:** **Hyperthermal atomic oxygen** impacts at **5 eV** are simulated to match cited **molecular-beam** experiments (abstract).
- **Electric field:** N/A — **not used** in the abstract/intro framing.
- **Replica / enhanced sampling:** N/A — **not stated**.

### 2 — Force-field training

N/A — this publication is an **application/validation** study of an existing **C/H/O ReaxFF** parametrization; the abstract states **additional evidence** that the parametrization **reproduces ab initio-derived energies** relevant to HOPG oxidation (details/SI: full PDF).

## Findings

- **Outcomes & mechanisms:** MD predicts an **oxygen coverage precursor** followed by **wide, shallow etch pits**; **carbon removal** occurs **near etch-pit edges**, while **O\(_2\)** forms via **recombination** more broadly on the sheet (abstract).
- **Comparisons:** Reported **product ranking** matches experiment: **O\(_2\)** (most abundant), then **CO\(_2\)**, with **CO** least abundant (abstract). The abstract also emphasizes **qualitative and quantitative agreement** with experiment overall.
- **Sensitivity / design levers:** Dominant pathway **activation energies** extracted from **isolated defect models** plus **etch-pit trajectory analysis** are reported as **~0.30 eV (O\(_2\))**, **~0.52 eV (CO\(_2\))**, and **~0.67 eV (CO)** (abstract).
- **Limitations & outlook:** The introduction motivates extending beyond **ideal HOPG** to **more complex microstructures** and flux environments encountered in **TPS** and related engineering settings (introduction excerpt); quantitative transfer requires matching **beam spread**, **surface defects**, and **multicomponent** chemistry as treated in the full article.
- **Corpus honesty:** Indexed text is **early-journal pages** only; **integrator settings, cell sizes, run lengths, and thermostat details** must be read from **`pdf_path`** (and SI) for reproduction.

## Limitations

- Beam conditions and idealized crystallinity may omit real TPS microstructure, defects, and mixed gas chemistry.
- Activation energies are extracted from the model chemistry as simulated; experimental interpretation may differ in detail.

## Relevance to group

Demonstrates **large-scale ReaxFF** for **carbon oxidation** relevant to thermal protection and high-temperature gas–surface chemistry.

## Citations and evidence anchors

- DOI: [10.1021/jp3125999](https://doi.org/10.1021/jp3125999)
- Extract: `normalized/extracts/2013poovathingal-venue-jp3125999_p1-2.txt`

## Reader notes (navigation)

- Galley duplicate ingest: [[2013poovathingal-venue-research]]

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
