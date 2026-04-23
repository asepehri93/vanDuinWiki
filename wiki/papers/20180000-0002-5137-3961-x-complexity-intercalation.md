---
id: paper:20180000-0002-5137-3961-x-complexity-intercalation
type: paper
title: "Complexity of Intercalation in MXenes: Destabilization of Urea by Two-Dimensional Titanium Carbide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.8b05913"
year: 2018
authors:
  - "Steven H. Overbury"
  - "Alexander I. Kolesnikov"
  - "Gilbert M. Brown"
  - "Zhiyong Zhang"
  - "Gokul S. Nair"
  - "Robert L. Sacci"
  - "Roghayyeh Lotfi"
  - "Adri C. T. van Duin"
  - "Michael Naguib"
venue: "J. Am. Chem. Soc."
pdf_sha256: "5c684258b036f1d88a0b0bc2c32e44101fda2cbf3c251b761911259a052ad66a"
pdf_path: "papers/Overbury_JACS_2018_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20180000-0002-5137-3961-x-complexity-intercalation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Journal of the American Chemical Society** study probes **urea intercalation** in **Ti₃C₂Tₓ MXene** using **inelastic neutron scattering (INS)**, **infrared spectroscopy**, and **ReaxFF reactive molecular dynamics**. Experiments indicate that urea is not stable as intact intercalant under intercalation-relevant conditions: **decomposition** leads to species such as **ammonium** in the gallery, with **CO₂** evolution detectable spectroscopically. **ReaxFF MD** supplies **atomistic reaction pathways and energetics** consistent with the experimental picture, with implications for how **small-molecule intercalants** behave in **layered carbide MXenes** used in **energy storage** and related applications. The corpus PDF here is an **ACS author proof** variant of the same article also archived as `papers/Overbury_JACS_2018.pdf` (`paper:2018overbury-j-am-chem-so-complexity-intercalation`).

Framing in the article stresses that **MXene** galleries are reactive **nanoreactors**: assumed **guest** molecules may **hydrolyze** or **decompose** rather than persist as neat intercalants, so spectroscopy plus reactive MD is needed to interpret **interlayer** chemistry beyond static **XRD** gallery heights.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

### Experiments (INS / IR)

- **Samples:** **Ti\(_3\)C\(_2\)T\(_z\)** **MXene** prepared by **HF** **MAX-phase** etching and workup as referenced; **urea**-related **intercalation**/**soaking** conditions and **control** experiments appear in **§2 Experimental and computational methods** of the **JACS** article (local **proof** PDF: `papers/Overbury_JACS_2018_proof.pdf`).
- **INS:** **inelastic neutron scattering** to probe **vibrational** signatures of **intercalated** species versus **reference** **urea**/**ammonium** materials (assignment strategy in the paper).
- **IR:** **infrared** detection of **CO\(_2\)** **evolution** and related **gas-phase** products tied to **decomposition** under intercalation-relevant conditions.

### ReaxFF reactive molecular dynamics

- **Purpose:** provide **atomistic** **reaction pathways** and **relative energetics** for **guest–MXene** chemistry complementing **spectroscopy** (abstract).
- **Engine / potential:** **ReaxFF** **MD** (parameter lineage for **Ti/C/O/H** and organic **C/N/O/H** blocks as described in **Methods**/**SI**—confirm **termination** (**T\(_z\) = −OH/−F/=O**) handling against the experimental samples).
- **System construction, ensemble, timestep, duration:** follow the **Computational** subsection of the published article; **interlayer** **spacing** and **surface** **termination** strongly affect outcomes (see **Limitations**).

### Static QM

- **Not stated in the indexed excerpt** whether every channel has standalone **DFT** benchmarks; **ReaxFF** supplies the primary **atomistic** **reaction** picture paired with **experiment** in the abstract.

### MD protocol (computational subsection of *JACS*)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ReaxFF** (per **Experimental and computational methods**).
- **System size & composition:** **Ti\(_3\)C\(_2\)T\(_z\)** **slab**/interlayer models with explicit **urea**-derived **guest** species; **atom** counts and gallery spacings in **Methods**/SI.
- **Boundaries / periodicity:** **In-plane PBC** with vacuum or explicit gallery geometry as defined in the article (treat as **periodic** supercells for the interlayer stack).
- **Ensemble:** **NVT** production trajectories typical for gallery chemistry benchmarks unless **NPT** stress control is documented—confirm in **PDF**.
- **Timestep / duration:** Femtosecond **timestep** and **nanosecond**-scale segments as tabulated for equilibration and **production** sampling.
- **Thermostat:** **Nose–Hoover** or **Langevin**-class **thermostat** parameters as listed (see **SI** if split from main text).
- **Barostat:** **N/A — hydrostatic barostat** for gallery models run at fixed **interlayer** spacing unless the article applies **NPT** relaxation—verify locally.
- **Temperature:** **K** setpoints for reactive **MD** sweeps in **Methods**.
- **Pressure:** **N/A — bulk** **hydrostatic pressure** targets not central to the gallery chemistry models unless **NPT** appears in **SI**; confirm in **PDF**.

## Findings

### Outcomes and mechanisms

**Urea** under **intercalation**-relevant conditions **decomposes** rather than persisting intact in the **MXene** gallery; **INS** supports **ammonium**-like **intercalated** species after transformation. **IR** detects **CO\(_2\)** evolution consistent with **decomposition**/**oxidation** channels. **ReaxFF** **MD** gives **atomistic** **reaction** pathways and **relative energetics** aligned with the **spectroscopy**.

### Comparisons

**INS**/**IR** are compared to **reference** **urea**/**ammonium** materials; **simulation** results are interpreted alongside those **experimental** fingerprints rather than as standalone proof.

### Sensitivity

**Termination** (**T\(_z\)**) and **interlayer** **spacing** strongly affect **reactivity**—**temperature** and **soaking** history from **experiments** must match the modeled surface chemistry.

### Limitations and outlook

**Proof** PDF ingest; confirm figure numbering on **VOR**. **ReaxFF** accuracy for new **C–N** bond-making should be cross-checked with **QM** where quantitative **barriers** matter (**future work** per article spirit).

### Corpus honesty

This summary uses the **DOI** abstract plus local **`pdf_path`**; full numerical settings live in the peer-reviewed **PDF**/**SI**.


## Limitations

- **MXene termination** (mix of −OH, −F, oxo groups) sensitively affects chemistry; models must match the **synthetic history** of the sample.
- **ReaxFF** conclusions should be read alongside **QM benchmarks** for any **new bond-making/breaking** channels emphasized quantitatively.

## Relevance to group

**Adri C. T. van Duin** is a coauthor; the work is a flagship example of **ReaxFF** paired with **neutron and optical spectroscopy** on **MXene intercalation chemistry**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jacs.8b05913` (see first pages of `papers/Overbury_JACS_2018_proof.pdf`).

## Related topics

- [[reaxff-family]]
