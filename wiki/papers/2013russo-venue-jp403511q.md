---
id: paper:2013russo-venue-jp403511q
type: paper
title: "Combustion of 1,5-Dinitrobiuret (DNB) in the Presence of Nitric Acid Using ReaxFF Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp403511q"
year: 2013
authors:
  - "Russo, Michael F., Jr."
  - "Bedrov, Dmitry"
  - "Singhai, Shashank"
  - "van Duin, Adri C. T."
venue: "Journal of Physical Chemistry A"
pdf_sha256: "604b4ccd14967c07a850dfd7bdd29d87a1cdf343123b9e62af8da80e53bc3059"
pdf_path: "papers/Russo_DNB_HNO3_JPCA_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013russo-venue-jp403511q -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

ReaxFF reactive MD explores DNB/nitric acid mixtures at 0.5 and 1.0 g/mL to connect atomistic pathways to hypergolic ignition chemistry. Additional QM-driven reparameterization targets DNB dissociation channels and the DCA→DNB formation sequence; certain compositions show a sharp exothermic runaway interpreted as spontaneous ignition (abstract; Introduction; computational methods opening, extract). The Introduction situates **1,5-dinitrobiuret (DNB)** as a **nitrogen-rich** energetic intermediate tied to **ionic-liquid** hypergolic chemistry with **nitric-acid-class** oxidizers, motivating atomistic study of **DNB + HNO\(_3\)** mixtures where experiments are sparse.

## Methods

Grounding: `papers/Russo_DNB_HNO3_JPCA_2013.pdf`; `normalized/extracts/2013russo-venue-jp403511q_p1-2.txt` (abstract + Computational Methods opening).

### 1 — MD application (ReaxFF reactive mixtures + temperature ramps)

- **Engine / code:** **Reactive molecular dynamics** with **ReaxFF**; the article notes the final parameter file can be used with the **standalone ReaxFF code**, **LAMMPS**, or the **ReaxFF module in ADF** (Computational Methods excerpt).
- **System size & composition (mixtures):** **DNB + HNO\(_3\)** mixtures are built at **~0.5 g/mL** (**18 DNB + 18 HNO\(_3\)** in a **2.5 nm × 2.5 nm × 2.5 nm** periodic box) and **~1.0 g/mL** (**37 + 37** in the same box edge length), with additional **off-stoichiometric** examples started in the Methods text (**18 DNB / 180 HNO\(_3\)** with enlarged box side lengths **3.65 nm** and **2.91 nm** as printed in the extract) (Computational Methods excerpt).
- **Boundaries / periodicity:** **Periodic** cubic cells are explicitly described for the mixture preparation excerpt (**periodic box**) (Computational Methods excerpt).
- **Ensemble / thermostat / timestep / duration (mixtures):** After minimization, each mixture system is run for **5 ps** **NVT** equilibration at **500 K** using a **Berendsen** thermostat (**500 fs** damping), followed by **NVE** production at **500 K** with **\(\Delta t = 0.1\) fs**, typically **500 ps** total (some runs extended/shortened depending on reactivity) (`papers/Russo_DNB_HNO3_JPCA_2013.pdf`, Simulation Details).
- **Single-molecule temperature ramps:** **20** simulations with **one DNB** in a **2.5 nm** periodic box, heated with a **Berendsen** thermostat to **4000 K** target, **500 fs** damping, **0.1 fs** timestep; **terminal NO\(_2\)** loss is reported as the dominant first dissociation step in **all 20** runs (Computational Methods excerpt).
- **Barostat:** N/A — **not stated** for these ramp/mixture excerpts beyond constant-volume cubic cells.
- **Temperature:** **4000 K** target in ramp tests; mixture staging temperatures are continued beyond p1–2 in the PDF.
- **Pressure:** N/A — **not a stated hydrostatic control** in the indexed excerpt (density targets are used for mixtures).
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A — **20 independent ramp trajectories** are used as **replicas** for **dominant first-step** statistics, not enhanced sampling in the umbrella/metadynamics sense.

### 2 — Force-field training (ReaxFF extension for DNB / HNO\(_3\) chemistry)

- **Parent FF / elements:** Extends a previously developed **C/H/O/N ReaxFF** database for **hypergolic** systems (Computational Methods excerpt).
- **QM reference:** Additional training/optimization uses **Jaguar** QM with **B3LYP** and **6-311G++\*\*** for reaction energies of **single-DNB** dissociation channels and for the **DCA → DNB** formation sequence (Computational Methods excerpt).
- **Training set / targets:** Adds **reaction energies** (isolated reactant/product energy differences) for **DNB dissociation pathways** and tests the **DNB formation pathway** energetics vs QM (Computational Methods excerpt + abstract motivation).
- **Optimization:** **Training/optimization** language is used in the excerpt; **specific optimizer (GA vs least-squares)** is **not spelled out** on p1–2—see full PDF.
- **Reference data / validation:** Post-training, ReaxFF matches QM for the highlighted DNB reactions typically within **~6 kcal/mol**, with **DCA→DNB** steps mostly within **~8 kcal/mol** except the **final step** called out as a small stability deviation (Computational Methods excerpt).

## Findings

- **Outcomes & mechanisms:** For **single-DNB** ramps at the stated extreme heating, **terminal NO\(_2\)** loss is the dominant **first** dissociation step in **all 20** trajectories (Computational Methods excerpt). For **DNB + HNO\(_3\)** mixtures, the abstract reports that **certain compositions** can show a **very sharp** thermal-energy release interpreted as **spontaneous ignition / hypergolic-like** behavior, with mechanistic discussion in the article body.
- **Comparisons:** QM comparisons are shown for **trained reaction energies** (Figures referenced in excerpt text) and the work positions ReaxFF as reproducing **near-QM** energetics trends at lower cost (Introduction excerpt).
- **Sensitivity / design levers:** **Mixture composition** and **mass density (~0.5 vs ~1.0 g/mL)** are explicit knobs in the abstract/Methods opening; ramp tests probe **temperature-driven** fragmentation.
- **Limitations & outlook:** The excerpt notes the **final DNB-formation step** is slightly less stable vs QM but argues it is unlikely to dominate overall dynamics given large energy releases in earlier steps (Computational Methods excerpt). Atomistic cells are not full **engine-scale** propellant fluid mechanics.
- **Corpus honesty:** Indexed pages include **mixture protocol start** but **truncate** before full **equilibration/production** tables; confirm complete MD staging in `pdf_path` (and compare [[2013russo-venue-research]] galley variant if auditing formatting differences).

## Limitations

Shock/ignition chemistry is extremely sensitive to model and initial geometry; high-temperature ramp protocols are not experimental drop-test conditions.

## Relevance to group

Demonstrates iterative ReaxFF extension for nitrogen-rich energetic/ionic-liquid chemistry led from Penn State MNE.

## Citations and evidence anchors

- J. Phys. Chem. A 2013, 117, 9216–9223; DOI `10.1021/jp403511q` (extract page 2 footer).
- Abstract and force-field development paragraph (extract pages 1–2).

## Related topics

- [[reaxff-family]]
