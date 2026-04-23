---
id: paper:2024talkhoncheh-venue-manuscript
type: paper
title: "Development of the ReaxFF Reactive Force Field for Li/Mn/O Battery Technology with Application to Design a Self-Healing Cathode Electrolyte Interphase"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c07242"
year: 2024
authors:
  - "Mahdi Khajeh Talkhoncheh"
  - "Hamed Ghods"
  - "Mahsa Doosthosseini"
  - "Jeffrey Silberberg"
  - "Iacovos Kyprianou"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "b3f3dbdc0d19dc2edbc24d1de2b0cb66006339acf9fdd8ecee758ade54535aa4"
pdf_path: "papers/Talkhoncheh_MnO_PF_LiF_battery_JPC_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024talkhoncheh-venue-manuscript -->

!!! abstract "Scope"
    **ReaxFF** for **Li/Mn/O** battery chemistry is developed and applied to **cathode–electrolyte interphase (CEI)** formation on **LiMn₂O₄**, focusing on a **self-healing** design with an **ionic liquid–derived additive** (PYR₁₃⁺).

## Summary

The work targets **lithium manganese oxide (LMO, LiMn₂O₄)** cathodes, especially in **high-reliability** contexts such as **implantable devices**, where **capacity fade** and **interfacial chemistry** (SEI/CEI) affect safety. The authors motivate **CEI** (cathode electrolyte interphase) formation as less understood than **SEI** at the anode, and propose attaching an **ion pair** to the cathode surface to promote a **self-healing CEI** that **seals cracks**: bound cations limit cathode–electrolyte attack, while anions migrate to damaged regions and **decompose preferentially** relative to bulk electrolyte, reducing **electrolyte loss** and **active-material loss**. **ReaxFF molecular dynamics**, trained to **ab initio reaction energies and barriers**, is used to study CEI formation under **experimentally inspired** electrolyte compositions without fully *ab initio* cost.

## Methods

- **ReaxFF training:** The **abstract** states **ReaxFF** is **trained against ab initio reaction energies and barriers** for **Li/Mn/O** chemistry relevant to **LiMn₂O₄** cathodes and **CEI** products; full **QM** program, **functional**, and **training-set** tables are in the article and **Supporting Information** (not in the short `normalized/extracts/2024talkhoncheh-venue-manuscript_p1-2.txt` front matter).
- **ReaxFF MD (CEI):** Simulations target **CEI** formation on **LMO** with electrolyte chemistry involving **PYR₁₃⁺** cations and **FSI⁻** anions (abstract). **System size**, **surface termination**, **electrolyte** composition, **ensemble**, **timestep**, **thermostat**, and **run length** are **not stated in the checked-in extract**—read **`pdf_path`** (or version-of-record) for the computational protocol.

**1 — MD application (ReaxFF on LiMn₂O₄).** **Engine:** **ReaxFF** **LAMMPS**-class **molecular** **dynamics** (as in *Computational Methods*). **System, PBC, slab termination, and electrolyte** composition: **N/A in this page summary** — the **p1–2** extract is **front matter**; pull **cell** size, **atom** counts, **NVT**/**NPT** choice, **fs** **timestep**, **K**-scale **isothermal** **T** (e.g. **~300** **K** for room-temperature interface MD is typical—**confirm** the **K**-listed **T** in **`pdf_path`**), and **ps**/**ns** **duration** from **`pdf_path`**. **Barostat / stress / E-field (external), replica methods:** **N/A** in the **abstract**-level summary on this page unless the full text adds them.

**2 — Force-field training.** **Abstract** states **ReaxFF** is **trained to ab initio reaction energies and barriers** for **Li/Mn/O** chemistry; **SI** and §2+ carry **DFT** code, level, and **training** **structures** (**N/A** to duplicate here on the stub).

**3 — Static QM** — the **ab initio** set underpins **ReaxFF**; standalone **DFT** **results** sections are part of the same **article** (**full PDF**).
## Findings

**CEI and additive (abstract).** **Simulations** in the **abstract** support **stronger**, **more** **stable** **cathode**-**side** **interphases** on **LMO** when **PYR₁₃⁺** is an **electrolyte** **additive**, a **higher** **Li⁺** **transference** in those **electrolytes**, and a role for **FSI⁻** vs **PYR₁₃⁺** **interactions** in the trend. This is framed as a **kinetic/thermodynamic** story about **reaction** at the **LMO**/**electrolyte** **interface**; **mechanism**-level **atomistic** **detail** (e.g. **catalytic** **steps** on **specific** **facets**) requires the **Results** in **`pdf_path`**.

**Comparisons to literature and outlook.** The **introduction** situates the work next to **Mn** **dissolution**/**impedance** and **cathode**-side **decomposition**; **open** **questions** about long **cycling** and full **reaction** **networks** remain **larger** than the **reactive** **ReaxFF** **window** can **resolve** in one **manuscript**—as **typical** in **FF**-based **interface** **studies**.

**Corpus honesty** — **galley** **`pdf_path`**; use **VOR** for final **pagination**.
## Limitations

The local corpus PDF is a **galley** (`…_galley.pdf`). CEI chemistry is complex; ReaxFF models require **validation** against experiment and QM for each new composition. Simulation time scales remain **short** relative to battery aging.

## Relevance to group

**Adri C. T. van Duin** is corresponding author; the paper extends the group’s **ReaxFF** work into **Li-ion cathode interfaces** and **medical-device battery** narratives.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.3c07242](https://doi.org/10.1021/acs.jpcc.3c07242)

## Reader notes (navigation)

Use the full **PDF** at `pdf_path` for **Computational methods** tables not present in the short extract. Theme retrieval: [[paper-index-by-domain]].

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
