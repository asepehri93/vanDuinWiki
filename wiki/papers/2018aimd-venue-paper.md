---
id: paper:2018aimd-venue-paper
type: paper
title: "Ab initio molecular dynamics simulation of tribochemical reactions involving phosphorus additives at sliding iron interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - method:aimd
  - task:application
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:tribology
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.3390/lubricants6020031"
year: 2018
authors:
  - "Sophie Loehlé"
  - "Maria Clelia Righi"
venue: "Lubricants"
pdf_sha256: "aa6a721591228d2861405b5de2d4c0d0b227ca08648b52ef6e7647ebf4873b46"
pdf_path: "papers/Others/AIMD_lubricants-06-00031-v2.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2018aimd-venue-paper -->

!!! note "Corpus note"

    This open-access article is **ab initio molecular dynamics** tribochemistry on **iron** with an **organophosphorus** extreme-pressure additive. It is **not** a van Duin-group **ReaxFF** study; it is included as **boundary-lubrication** and **QM dynamics** context adjacent to reactive classical simulations in the corpus.

## Summary

The authors investigate **tribochemical activation** of an **organophosphorus** lubricant additive at **steel-on-steel**-like **iron** sliding interfaces using **fully ab initio molecular dynamics**. The central question is how **mechanical stress** and **interfacial confinement** alter the timescales and pathways for **molecular dissociation** compared with expectations based on **gas-phase** or **static** barrier estimates. The simulations follow the additive in contact with **Fe** surfaces under **boundary lubrication** pressures, tracking **bond-breaking** events that are consistent with formation of **iron phosphide**-rich tribofilm chemistry as discussed in the tribology literature. The study emphasizes **real-time** chemistry under load, relating observed **activation times** to **stress-biased** reaction coordinates rather than treating the interface as a passive heat bath. This framing connects directly to debates in tribology about when **Arrhenius-like** pictures remain predictive for reactions that are mechanically driven.

## Methods

### AIMD setup (read from `pdf_path`)

The article reports **ab initio molecular dynamics** (**CP2K**/**VASP**-class engines are common in tribochemistry literature—**confirm program name in the PDF**) for **Fe** **sliding** interfaces with an **organophosphorus** additive. Because **`extraction_quality`** is **partial**, the following **slot coverage** uses explicit **N/A** where this wiki cannot transcribe unpublished table cells:

- **Engine / code:** **AIMD** / **first-principles MD** as named in *Lubricants* **Methods** (open-access **`papers/Others/AIMD_lubricants-06-00031-v2.pdf`**).
- **System size & composition:** **Fe** **slab**/**interface** **supercells** with the additive in the tribological contact region—**atom** counts in **PDF** tables.
- **Boundaries / periodicity:** **3D PBC** supercells with in-plane shear/slide boundary conditions as defined for tribology AIMD (see **PDF**).
- **Ensemble:** **NVT** or mixed **NVE**/thermostatted segments for load/stress protocols—**N/A here to guess** without the full **Methods** paragraph transcribed locally.
- **Timestep:** Sub-**1 fs** **timestep** typical of AIMD; **exact fs** value **not stated** in the partial corpus extract—take from **PDF**.
- **Duration:** **Production** segments on the **picosecond** scale (order of **10–100 ps** typical for AIMD tribochemistry, but **N/A** to quote precisely without the article table).
- **Thermostat:** **Nose–Hoover**/**Langevin**-class choices as printed—**N/A** to specify damping constants here without **PDF** access in this pass.
- **Barostat:** **N/A — hydrostatic NPT barostat** not assumed; tribo cells often use fixed cell + mechanical loading—confirm in **PDF**.
- **Temperature:** **K** setpoints for thermal control of the interface as listed.
- **Pressure / stress:** **Stress**/**load** control along the sliding direction in lieu of isotropic **pressure**—see **PDF** for **GPa**/**bar**-equivalent contact **pressure** when reported.
- **Electric field:** **N/A — electric field** not applied.
- **Enhanced sampling:** **N/A — umbrella / metadynamics** not indicated in the abstract-level summary.

## Findings

The **AIMD** trajectories capture **dissociation** of the **organophosphorus** species at the **sliding** interface under pressure, supporting a **tribochemical** route toward **iron phosphide** formation rather than requiring a purely thermal mechanism in the gas phase. The authors report that **mechanical stress** materially changes **activation times** relative to what would be expected from **barrier-based** estimates that ignore **stress bias** and **interfacial electronic polarization**. The discussion ties simulated timescales across **loads** to the **dissociation barrier** framework, highlighting where **stress-assisted** chemistry accelerates or channels particular pathways. These conclusions are qualitative-to-semiquantitative in the abstract-level summary used here; precise numbers belong to the **peer-reviewed PDF**.


## Limitations

**Partial** text extraction in the corpus limits operator confidence in secondary details; readers should confirm **all numerical parameters** and **statistical sampling** from **`papers/Others/AIMD_lubricants-06-00031-v2.pdf`**. **AIMD** reach is intrinsically shorter in time and smaller in space than **ReaxFF** reactive MD, so direct quantitative comparison to classical reactive simulations requires care.

## Relevance to group

Provides a **QM MD** benchmark for **stress-assisted** reactions at **metal** interfaces, useful when interpreting **ReaxFF** tribochemistry studies at larger scales.

## Citations and evidence anchors

- DOI: `10.3390/lubricants6020031` (open access).

## Related topics

- [[reaxff-family]]
