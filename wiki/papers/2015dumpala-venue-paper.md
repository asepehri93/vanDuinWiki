---
id: paper:2015dumpala-venue-paper
type: paper
title: "Integrated atomistic chemical imaging and reactive force field molecular dynamic simulations on silicon oxidation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1063/1.4905442"
year: 2015
authors:
  - "Santoshrupa Dumpala"
  - "Scott R. Broderick"
  - "Umedjon Khalilov"
  - "Erik C. Neyts"
  - "Adri C. T. van Duin"
  - "J Provine"
  - "Roger T. Howe"
  - "Krishna Rajan"
venue: "Applied Physics Letters"
pdf_sha256: "e90d08f7f0462f386d84b02c6c05367e073608155b7d73218ff241363c34d0c1"
pdf_path: "papers/Dumpala_SiO_APT_ReaxFF_APL_2015.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2015dumpala-venue-paper -->

## Summary

Silicon microelectronics depend on **thermally grown SiO₂**, but the **Si/SiO₂ interface** is not atomically abrupt: a **suboxide (SiOₓ)** transition region carries gradients in **stoichiometry** and **bonding** that influence transport, reliability, and variability. This *Applied Physics Letters* article couples **atom probe tomography (APT)**—a chemical imaging modality with near-atomic **depth resolution** in favorable cases—with **ReaxFF reactive molecular dynamics** to compare **experimental** and **simulated** evolution of **suboxide** character as **oxidation temperature** changes. The motivating claim is that **integrated** experiment and **atomistic** oxidation modeling can converge on the same trends for **interfacial SiOₓ** fraction and **oxygen ingress**, where simpler continuum oxidation models may wash out chemical detail.

## Methods

### Experiment (APT)

**Si** needles are **thermally oxidized** at **1–4 Torr** at **383 K** and **548 K**. **Laser-assisted APT** (**LEAP 3000 X Si**, **532 nm**, **~10 ps** pulses, **~0.9–1.0 nJ**, **150 kHz**) reconstructs **Si/SiO₂** interfacial chemistry and intermixing.

### MD application (atomistic dynamics)

**Reactive molecular dynamics** with **ReaxFF** (Si/O parameterization attributed to **Buehler *et al.***; extended tables in **SI**, *Appl. Phys. Lett.* **106**, 011602 (2015)) starts from a **Si(100) 2×1** slab cell **21.7 × 21.7 × 27.1 Å³** (**LAMMPS**-style **MD** setup as standard in the cited ReaxFF Si/O literature). **NVT** **Berendsen thermostat** equilibration at **300 K** and **700 K** (**20 ps**, **0.1 ps** damping) precedes **10 ps NVE** relaxation. **3D PBC** applies to the oxidation supercell. **Integrator timestep:** **N/A —** not stated in the short APL paragraph here; see **SI** if a numeric **dt** is required. **NPT stress control:** **N/A —** not reported as a primary knob. Profiles of **suboxide**/**diffusion** are compared to **APT** proximity histograms; the article stresses **qualitative** agreement given **experiment vs nanosecond MD** time-scale mismatch.

### Force-field training

**N/A —** applies an existing **ReaxFF** Si/O parameterization with literature precedent; not a new fit paper.

### Static QM / DFT

**N/A —** DFT is cited comparatively in the surrounding literature discussion, not as an on-the-fly engine in the reported MD.

## Findings

**APT** and **ReaxFF** both show **higher SiOₓ relative to SiO₂** and **broader oxygen ingress** at **548 K** than at **383 K**, in **qualitative** agreement though absolute widths and times differ—i.e., **oxidation** and **intermixing** trends align between **experiment** and simulation despite different accessible **thickness** scales. Proximity histograms highlight **suboxide** in an interfacial **region II**, matching simulation-resolved **mixed-valence** O environments in the figures/text. **Sensitivity** to oxidation **temperature** is therefore captured at the qualitative level the authors claim. **Limitations** include APT reconstruction biases and **MD** timescales far shorter than furnace oxidation; **PDF/SI** remain authoritative for numerical interface widths.

## Limitations

**APT** reconstruction can bias **interface** chemistry; **MD** captures only **short-time** oxidation kinetics, so **absolute** interface widths should be treated as **qualitatively** comparable between experiment and simulation (as the authors discuss).

## Relevance to group

Direct **van Duin**-authored **ReaxFF** interface to **APT**, emphasizing **validation** at **atomic** chemical resolution.

## Related topics

- [[reaxff-family]]
