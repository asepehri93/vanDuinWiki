---
id: paper:2015hajilar-jmade-90-201-mechanical-failure
type: paper
title: "Mechanical failure mechanisms of hydrated products of tricalcium aluminate: A reactive molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - material:cement-mineral
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.matdes.2015.10.089"
year: 2015
authors:
  - "Shahin Hajilar"
  - "Behrouz Shafei"
venue: "Materials & Design"
pdf_sha256: "f864d69fbf148c77f4161262fab35ba670bbd098c1ea88f9a6addc88d875a3df"
pdf_path: "papers/ReaxFF_others/Hajilar_CaAlOx_MatDesign_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015hajilar-jmade-90-201-mechanical-failure -->

## Summary

**Tricalcium aluminate (C₃A)** hydration chemistry controls several high-impact phases in cement systems, especially **hydrogarnet**, **ettringite**, and **monosulfoaluminate (kuzelite)**. The introduction in this paper frames these phases as mechanically consequential because sulfate availability and phase interconversion can alter volume stability, cracking tendency, and durability. Hajilar and Shafei therefore target atomistic failure behavior of representative crystalline forms of these hydrates using **reactive molecular dynamics** rather than limiting analysis to small-strain elasticity.

The study goal is twofold: (1) generate tensile **stress-strain** curves that separate elastic and post-yield response, and (2) connect macroscopic curve features to **bond-level damage pathways** under large deformation. This is positioned against prior literature that focused more heavily on C-S-H gel, leaving aluminum-rich hydrated phases less characterized under high tensile load. The authors also motivate relevance to broader cement contexts, including calcium sulfoaluminate systems where ettringite and related phases are central.

Within the extract-backed framing, the work is explicitly comparative across phase identity, loading direction, and strain rate. That design allows the paper to ask whether anisotropy and loading-rate sensitivity differ among hydrogarnet, ettringite, and kuzelite, and whether distinct bond-breaking sequences explain those differences. The output is thus both descriptive (curves, moduli, yield/softening behavior) and mechanistic (structural damage evolution under reactive force-field dynamics).

## Methods

### MD application (atomistic dynamics)

**LAMMPS** **ReaxFF** with **QEq** each step and **velocity-Verlet** at **0.25 fs** (*Materials & Design* **90** (2016) 165–176) models **hydrogarnet**, **ettringite**, and **monosulfoaluminate (kuzelite)** in **3D PBC** supercells (**3712 / 2048 / 2544** atoms). After **0 K** minimization, **50 ps NPT** targets **300 K** and **0 atm** gauge. **Uniaxial tensile strain** is applied along **x, y, z** separately with **anisotropic NPT** at **zero lateral pressure** on the transverse axes while recording stress to **50% engineering strain**; four **strain rates** span **0.0005–0.01 ps⁻¹**. Additional tensile-stage thermostat/barostat damping beyond this excerpt: **N/A —** see PDF if full integrator details are needed. **Shock, electric field, replica sampling:** **N/A —** not used.

### Force-field training

**N/A —** applies **ReaxFF** for **Ca–Al–O–S–H** cementitious chemistry (parameter lineage cited in the paper) rather than reporting a new fit.

### Static QM / DFT

**N/A —** not used as the primary engine for the mechanical curves summarized here.

## Findings

Each phase shows distinct **elastic**, **yield**, and **post-yield** behavior that depends on **stretching axis** and **strain rate** in the reported curves. Bond tracking ties **softening** to phase-specific **scission** patterns (e.g., **Ca–O** and **sulfate/aluminate column** roles in **ettringite**, contrasted with prior Liu *et al.* reactive work). Coverage extends **hydrogarnet** and **kuzelite** relative to earlier **ettringite**-focused simulations. **Moduli** and numerical stress–strain values belong in the **PDF**; models omit **paste** microstructure, **pores**, and **interfaces**.

- **Outcomes and mechanisms:** Reactive MD identifies different failure progressions across the three hydrates, with curve nonlinearity linked to evolving local bond topology rather than a single universal rupture motif.
- **Comparisons:** Directional loading (x/y/z) and strain-rate sweeps expose anisotropic and rate-dependent responses that would be hidden in one-direction, one-rate calculations.
- **Sensitivity/design levers:** The paper’s controlled variables are phase identity, tensile axis, and imposed strain rate; all three materially affect where elastic response transitions toward irreversible damage.
- **Corpus honesty:** The local extract establishes study scope and motivation, while detailed numeric tables/plots (e.g., exact strengths/moduli by direction/rate) should be taken from the full `pdf_path` before downstream quantitative reuse.

## Limitations

Models are **single-phase crystals** without **pores**, **interfaces**, or **paste microstructure**; **MD strain rates** far exceed laboratory **quasi-static** tests, so absolute strengths are **illustrative**. The printed issue year is **2016** while the wiki slug retains a **2015** prefix—use **`doi`/`year`** for citation hygiene.

## Reader notes (navigation)

- [[theme-oxides-silica-ceramics]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
