---
id: paper:2013sen-venue-paper
type: paper
title: "Oxidation induced softening in Al nanowires"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:lammps
  - keyword:nvt-simulation
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4790181"
year: 2013
authors:
  - "Fatih G. Sen"
  - "Yue Qi"
  - "Adri C. T. van Duin"
  - "Ahmet T. Alpas"
venue: "Applied Physics Letters"
pdf_sha256: "78ddcf75c4f48190a3f54c79a6560311a77e779f51f75e0b503a102c85f8ce7f"
pdf_path: "papers/Sen_ApplPhysLett_2013_Al_wires.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013sen-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

ReaxFF MD probes **elastic tensile response** of **oxidized aluminum nanowires**. A thin amorphous oxide shell shows a low Young’s modulus (about **26 GPa** in the modeling), tied to low mass density and reduced Al–O coordination in the shell. For diameters below ~100 nm, the **effective composite modulus** of oxide-clad wires exhibits a **size trend** described as **“smaller is softer”** in the article, reconciling scattered experimental moduli for nanoscale Al structures.

The introduction notes inconsistent experimental Young’s moduli for metal nanowires and argues that native oxides—often omitted in prior simulations—can dominate mechanics for oxygen-philic metals such as aluminum that oxidize rapidly even under mild exposure, motivating explicit ReaxFF tensile tests on oxidized \(\langle001\rangle\) wires.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

Grounding: `papers/Sen_ApplPhysLett_2013_Al_wires.pdf`; `normalized/extracts/2013sen-venue-paper_p1-2.txt` (AIP metadata + article opening + Methods start).

### 1 — MD application (ReaxFF oxidation + elastic tensile deformation)

- **Engine / code:** **Molecular dynamics** simulations with **ReaxFF** implemented in **LAMMPS** (article text excerpt).
- **System size & composition:** **\(\langle001\rangle\)** **Al nanowires** **~10.2 nm long** with **octagonal** \(\{100\}/\{110\}\) cross-sections at nominal diameters **3.2, 4.0, and 5.6 nm**; wires are oxidized from **Al surrounded by O\(_2\)** until a **stable amorphous oxide shell** forms, then tested by **tensile elastic deformation in vacuum** (article excerpt).
- **Charge dynamics / integration:** **Atomic charges updated every MD time step**; **time step 0.5 fs** (article excerpt).
- **Boundaries / periodicity:** N/A — **explicit PBC vs free surfaces** details for oxidation and tensile legs are **not fully stated** on the indexed excerpt pages (confirm in `pdf_path`).
- **Ensemble:** Oxidation and subsequent tensile testing of the prepared wires are carried out in the **NVT** ensemble (`papers/Sen_ApplPhysLett_2013_Al_wires.pdf`, Methods text around the oxidation/tensile protocol).
- **Thermostat / barostat:** N/A — **thermostat type** beyond **NVT** naming is **not extracted** here; read `pdf_path` for coupling details.
- **Duration / stages:** N/A — **equilibration/production lengths** are **not stated** on the indexed excerpt pages.
- **Temperature:** N/A — **explicit setpoints** for oxidation/tensile stages are **not stated** on the indexed excerpt pages.
- **Pressure:** N/A — tensile testing described as **vacuum** environment for mechanical probing (article excerpt).
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

The excerpt states the **Al/O ReaxFF** is tailored from a prior **Al/O** parameterization and integrated with a **nitramine-related ReaxFF description**, with a **supplied parameter file** (`ffield.reax`) noted as **supplementary** (article excerpt). **QM training functional/basis** for this tailoring is **not stated** on the indexed excerpt pages.

## Findings

- **Outcomes & mechanisms:** The modeled **native oxide shell** is **low density** with **reduced Al–O coordination**, yielding a **low shell Young’s modulus (~26 GPa)** (article excerpt).
- **Comparisons:** The authors connect the model to scattered **experimental** nanoscale **Al** modulus reports and argue **native oxide** effects help explain discrepancies when omitted in prior simulations (article excerpt).
- **Sensitivity / design levers:** **Diameter** (**3.2 / 4.0 / 5.6 nm**) changes the **effective composite Young’s modulus**, producing a **“smaller is softer”** trend for **oxide-covered** wires below **~100 nm** in the article’s statement (article excerpt).
- **Limitations & outlook:** The excerpt emphasizes **elastic** deformation of oxidized wires; **plasticity** and long-time oxidation kinetics are outside the stated scope on these pages.
- **Corpus honesty:** `extraction_quality` is **partial** due to publisher wrapper text in the corpus extract; confirm any additional numerical results in **`pdf_path`**.

## Limitations

Elastic loading only; plasticity, cracking, and long-time oxidation kinetics are outside scope. `extraction_quality` is **partial** due to publisher wrapper text in the corpus extract.

## Relevance to group

Mechanical consequence of **native oxidation** modeled with ReaxFF—useful for nanomechanics and interface-aware property prediction.

## Citations and evidence anchors

- DOI: [10.1063/1.4790181](https://doi.org/10.1063/1.4790181)
- Extract: `normalized/extracts/2013sen-venue-paper_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Aluminum surfaces and thin native oxides
