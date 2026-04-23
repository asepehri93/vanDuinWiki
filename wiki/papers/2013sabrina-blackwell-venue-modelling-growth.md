---
id: paper:2013sabrina-blackwell-venue-modelling-growth
type: paper
title: "Modelling the growth of ZnO thin films by PVD methods and the effects of post-annealing"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:classical-ff
  - keyword:monte-carlo-sampling
  - keyword:oxide-surface
canonical_tags:
  - domain:oxides-ceramics
  - method:classical-md
  - method:monte-carlo
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1088/0953-8984/25/13/135002"
year: 2013
authors:
  - "Sabrina Blackwell"
  - "Roger Smith"
  - "Steven D. Kenny"
  - "John M. Walls"
  - "Carlos F. Sanz-Navarro"
venue: "Journal of Physics: Condensed Matter"
pdf_sha256: "f71b466a6691aaf66b906eacb2513fc88c3b5ce44f52a64828a7709fa5a45249"
pdf_path: "papers/ReaxFF_others/Blackwell_Smith_SanzNavarro_etal_JoP_CondMat_ZnOgrowth_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013sabrina-blackwell-venue-modelling-growth -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. This study uses **on-the-fly kinetic Monte Carlo with MD**, not ReaxFF.

## Summary

Combined molecular dynamics and **on-the-fly kinetic Monte Carlo (otf-KMC)** simulate magnetron sputter and evaporation deposition of Zn\(_x\)O\(_y\) species onto an O-terminated ZnO (000\(\bar{1}\)) wurtzite substrate, including post-anneal steps. Sputtering yields denser, more crystalline films than evaporation due to higher impact energies; evaporation shows more stacking faults. Annealing at 770 K does not fully heal faults; 920 K can recrystallize some films to wurtzite, though zinc-blende regions may persist. Deposition-flux stoichiometry strongly affects quality: evaporation is best with stoichiometric ZnO-cluster flux; sputtering improves slightly with an O-rich flux; single-species-dominated fluxes sputter/reflect more O, producing up to ~18% O deficiency, extra faults, and phase boundaries.

## Methods

Grounding: `papers/ReaxFF_others/Blackwell_Smith_SanzNavarro_etal_JoP_CondMat_ZnOgrowth_2013.pdf`; `normalized/extracts/2013sabrina-blackwell-venue-modelling-growth_p1-2.txt` (IOP wrapper + abstract).

### 1 — MD application (PVD growth modeling: MD + on-the-fly KMC)

- **Engine / code:** **Molecular dynamics (MD)** combined with **on-the-fly kinetic Monte Carlo (otf-KMC)** (abstract).
- **System size & composition:** **Zn\(_x\)O\(_y\)** deposition onto an **O-terminated ZnO (000\(\bar{1}\)) wurtzite** surface (abstract). **Atom counts** are **not stated** in the indexed excerpt.
- **Process knobs:** Vary **substrate bias**, **distribution of deposition species**, and **annealing temperature** (abstract).
- **Boundaries / periodicity:** N/A — **not stated** in the indexed excerpt.
- **Ensemble:** **MD** relaxation between depositions uses **canonical** (fixed-temperature) control via a **Berendsen** thermostat attached to the **non-frozen** layers while the **bottom layer** remains **fixed** (`pdf_path`, Methods: “During the MD stage…”).
- **Timestep / duration:** **MD** segments run up to **~10 ps** per deposition/relaxation cycle as described in the same Methods paragraph (`pdf_path`).
- **Thermostat:** **Berendsen** thermostat on the **next two layers** above the fixed base (`pdf_path`).
- **Barostat:** N/A — growth **MD** segments are not described as **NPT** in the quoted deposition-relaxation paragraph (`pdf_path`).
- **Temperature:** Post-annealing at **770 K** and **920 K** (abstract).
- **Pressure / electric field:** N/A — **not stated** in the indexed excerpt.
- **Replica / enhanced sampling:** N/A — **not stated** beyond **otf-KMC** itself.

### 2 — Force-field training

N/A — **not a ReaxFF parametrization** study (see Evidence note: **MD + otf-KMC** workflow).

## Findings

- **Outcomes & mechanisms:** **Sputtering** yields **denser, more crystalline** films than **evaporation** due to **higher deposition energy**; **evaporation** shows **more stacking faults** (abstract).
- **Comparisons:** Direct **process-to-microstructure** comparison between **sputtering-like** and **evaporation-like** modes in the abstract narrative.
- **Sensitivity / design levers:** **Annealing temperature** (**770 K** vs **920 K**) controls whether **faults persist** vs **wurtzite recrystallization**; **920 K** can still leave **zinc-blende** regions. **Deposition-species distribution** is a strong lever: **stoichiometric ZnO clusters** are best for **evaporation**, while **slightly O-rich** distributions are best for **sputtering**; predominantly **single-species** deposition increases **O sputtering/reflection**, producing up to **~18% O deficiency** and more **faults/phase boundaries** (abstract).
- **Limitations & outlook:** Abstract frames the approach as revealing **mechanisms** and **optimum conditions** hints for **crystalline layer formation** (abstract).
- **Corpus honesty:** Indexed excerpt is **abstract-only**; reproducibility details live in **`pdf_path`** Methods.

## Limitations

Force-field and KMC move assumptions bound accuracy; experimental disorder and grain boundaries are only partially represented. The indexed extract is short; use `pdf_path` for complete simulation and validation details.

## Relevance to group

Corpus **oxide thin-film growth** reference (non-ReaxFF) useful next to reactive simulations of oxidation and ceramics.

## Citations and evidence anchors

- DOI: [10.1088/0953-8984/25/13/135002](https://doi.org/10.1088/0953-8984/25/13/135002)
- Extract: `normalized/extracts/2013sabrina-blackwell-venue-modelling-growth_p1-2.txt`

## Related topics

- Zinc oxide surfaces and PVD microstructure
- [[reaxff-family]] (context only; method differs)
