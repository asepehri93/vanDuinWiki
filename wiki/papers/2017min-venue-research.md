---
id: paper:2017min-venue-research
type: paper
title: "Modified Random Sequential Adsorption Model for Understanding Kinetics of Proteins Adsorption at a Liquid–Solid Interface"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:reaxff-application
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.7b00523"
year: 2017
authors:
  - "Hwall Min"
  - "Eugene Freeman"
  - "Weiwei Zhang"
  - "Chowdhury Ashraf"
  - "David Allara"
  - "Adri C. T. van Duin"
  - "Srinivas Tadigadapa"
venue: "Langmuir"
pdf_sha256: "11bb36fa72981b975cd681e5afe45e1e0cf97ef27641244ad20a1c8868c5d5c3"
pdf_path: "papers/Min_Protein_Gold_Langmuir_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017min-venue-research -->

!!! abstract
Microfabricated 83 MHz quartz crystal microbalance tracks HSA adsorption on hydrophobic hexadecanethiol–Au; an interface-depletion RSA model fits kinetics, supported by ReaxFF MD indicating oriented adsorption and slowed interfacial diffusion.

## Summary

Experimentally, **human serum albumin (HSA)** adsorption on a **hydrophobic hexadecanethiolated gold** surface is measured in real time with **83 MHz micromachined quartz crystal resonators**, focusing on asymptotic response and jamming limits under single- and multi-injection protocols. A new **interface-depletion modified RSA** model captures exponentially depleting interfacial concentration. Complementary **ReaxFF reactive MD** uses a **merged Au/S/O/C/H** parameter set (Jarvi *et al.*, Keith *et al.*, Joshi *et al.*, Monti *et al.*, as cited in section 5.2) on a **three-layer Au(111)–hexadecanethiolate–aspartame/water** surrogate for the interfacial environment: **576 Au**, **36** hexadecanethiolates, **18** aspartame molecules, **60** inner-layer waters, plus either **750** waters or **400** waters with **30** dipeptide molecules in the top “bulk” region, in a **34.62 × 29.97 × 140.00 Å³** cell. **ADF** drives **NVT** trajectories at **298.15 K** with a **Berendsen** thermostat (**100 fs** damping) and **Δt = 0.25 fs**, staging **100 ps** surface-only and solution-only equilibrations before a **400 ps** combined run (**last 200 ps** analyzed). Atomic density profiles and MSD analyses support **hydrophobic insertion** into the thiol layer and **slowed interfacial transport**, rationalizing the depletion RSA picture relative to bulk-limited kinetics.

## Methods

**Force-field training / fitting.** The study **does not** report a new ReaxFF refit. Reactive simulations use a **merged ReaxFF** for **Au/S/O/C/H** assembled from published **Au–S–H**, **Au–metal / Au–O–H**, and **protein (Monti *et al.*)** parameter sources as summarized in section 5.2 of the *Langmuir* article.

**MD application (atomistic dynamics).** **Engine / code:** **ADF** (as stated in section 5.2) carries the ReaxFF MD (**N/A — LAMMPS** not claimed in the main-text protocol excerpt used here). **System size & composition:** **Four-layer Au(111)** with **36** **C₁₆H₃₃S–** thiolates (**1 thiol per 4 Au**, **576 Au** total), **18** aspartame (**C₁₂H₁₆N₂O₃**) molecules plus **60** waters in the intermediate region, and a top region of either **750** waters (“pure water” case) or **400** waters **+ 30** dipeptide molecules (“dipeptide solution” case), in a **34.62 × 29.97 × 140.00 Å³** orthorhombic supercell. **Boundaries / periodicity:** **Three-dimensional periodic** supercell for the slab–solution stack (standard for this geometry class). **Stages / duration:** **100 ps** pre-equilibration of the **Au–thiol–peptide** stack, **100 ps** of the **top solution layer alone**, then **400 ps** of the **combined** system with **analysis on the final 200 ps**. **Ensemble:** **NVT** at **298.15 K**. **Timestep:** **0.25 fs**. **Thermostat:** **Berendsen** with **100 fs** damping constant (as reported). **Barostat / pressure control:** **N/A —** **NPT** is **not** used for these production trajectories. **Target temperature:** **298.15 K**. **Hydrostatic pressure / stress control:** **N/A —** not applied beyond the fixed-cell **NVT** setup described. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** direct **MD** only.

**Static QM / DFT.** **N/A —** **DFT** is **not** the engine for the ReaxFF trajectories summarized above (quantum references in the article support parameter provenance, not on-the-fly *ab initio* MD here).

**Review / non-simulation framing.** **83 MHz** micromachined **QCM** measurements of **HSA** on **hexadecanethiolated Au**, plus the **interface-depletion RSA** kinetic model, anchor the experimental narrative alongside the reactive MD surrogate. **Corpus note:** the tracked `pdf_path` is a **proof** PDF; pagination and any publisher tweaks should be checked against the **VOR** sibling **`[[2017hwall-min-langmuir-201-modified-random]]`** when available.

## Findings

**Outcomes & mechanisms.** **QCM** data show both **asymptotic** sensor response and **jamming-limited** coverage for **single-** vs **multi-injection** protocols at matched final bulk concentration. The **interface-depletion RSA** fit captures **exponentially depleted** interfacial protein availability. ReaxFF/ADF trajectories on the **Au–thiol–aspartame–water** stack show **hydrophobic vs hydrophilic** partitioning (atomic density profiles) and **layer-resolved MSDs** consistent with **reduced effective diffusivity** near the interface—supporting the idea that **slow interfacial transport** couples to **surface adsorption rate** to produce the depleted layer invoked in the kinetic model.

**Comparisons.** The **modified RSA** treatment improves agreement with measured kinetics versus **classical RSA** that assumes a well-mixed interfacial reservoir.

**Sensitivity & design levers.** Varying **injection protocol** at fixed final bulk concentration changes how **interfacial depletion** develops, which the model ties to **transport–adsorption coupling** rather than bulk concentration alone.

**Limitations & outlook (as authored).** The atomistic layer uses **aspartame** and **dipeptide**-solution surrogates rather than full **HSA**; **QCM** frequency interpretation may require **viscoelastic** corrections beyond a single kinetic fit (see article discussion).

**Corpus / KB honesty.** Numbers above are taken from the **indexed proof PDF** text in section 5.2; confirm against the **VOR** PDF/SI if any layout or typographic ambiguities remain after corpus swaps.

## Limitations

Proof PDF; atomistic models simplify full protein complexity—interpret as mechanistic support rather than quantitative fit to every experimental concentration. **QCM** **frequency** shifts can also couple to **viscoelastic** **film** properties not fully resolved by a single **RSA**-like **kinetic** fit without **rheological** **calibration**. **ReaxFF** snapshots of **peptide** segments should be interpreted as **qualitative** **orientation** trends because **full-length** **HSA** **conformations** can reorganize on **long** **experimental** **timescales**. **Langmuir** **SI** sections may contain additional **simulation** **cells** and **analysis** scripts not summarized on this page.

## Relevance to group

Adri C. T. van Duin is a co-author; ReaxFF links surface chemistry to measurable kinetics.

## Citations and evidence anchors

- DOI: `10.1021/acs.langmuir.7b00523`

## Related topics

- [[reaxff-family]]
- [[water-silica-geo]]

## Reader notes (navigation)

- Corpus PDF is a **proof** (`*_proof.pdf`).
