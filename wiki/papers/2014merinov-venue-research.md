---
id: paper:2014merinov-venue-research
type: paper
title: "ReaxFF reactive force-field modeling of the triple-phase boundary in a solid oxide fuel cell"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:oxide
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/jz501891y"
year: 2014
authors:
  - "Boris V. Merinov"
  - "Jonathan E. Mueller"
  - "Adri C. T. van Duin"
  - "Qi An"
  - "William A. Goddard, III"
venue: "J. Phys. Chem. Lett. 5, 4039–4043 (2014)"
pdf_sha256: "cba44f4a7e5a26a1abf788b1928ded3ec7149bc41d9c17681a2146bafb46e9c8"
pdf_path: "papers/Merinov_JPC_Letters_YSZ_Ni_interface_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014merinov-venue-research -->

## Evidence and attribution

!!! note "Maintainer note"

    Maintainer catalog (SI/galley/proof PDF roles): https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md

!!! note "Authority of statements"

    Summaries follow the **J. Phys. Chem. Lett.** letter abstract in the corpus extract. The registered PDF is an **author proof**; verify pagination against the **published issue** via `doi`.

## Summary

**ReaxFF** for **Ni/YSZ** is built by merging existing **YSZ** and **Ni/C/H** descriptions. **Reactive MD** explores **H₂** and **C₄H₁₀** feeds at **Ni/YSZ** **triple-phase boundary (TPB)** conditions (**1250 K** and **2000 K** in the abstract). Simulations report **Ni surface amorphization**, **interfacial delamination**, and **coking**, aligned with experimental observations, and propose a **butane conversion mechanism** at the **Ni/YSZ** interface related to **pyrolysis-like** steps with product sets consistent with experiment.

## Methods

Grounding: **`papers/Merinov_JPC_Letters_YSZ_Ni_interface_proof.pdf`** (author proof; verify pagination against the published **J. Phys. Chem. Lett.** issue) and `normalized/extracts/2014merinov-venue-research_p1-2.txt`.

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **ReaxFF reactive molecular dynamics (RMD)** as stated in the letter extract; **N/A — MD software package name** not stated in the indexed excerpt (often **LAMMPS** in ReaxFF studies—confirm in the **PDF**/**SI**).
- **System size & composition (TPB examples):** **H₂/Ni/YSZ** cell excerpted as **240 Ni, 16 Y, 48 Zr, 148 O** with **YSZ** at **~14 mol % Y₂O₃** [(Y₂O₃)(ZrO₂)₆] and **125 H₂** molecules; **C₄H₁₀/Ni/YSZ** case uses **20** butane molecules (extract).
- **Boundaries / periodicity:** **Periodic** **TPB** model (“Figure 1 shows the periodic system…”, extract).
- **Ensemble:** **NPT** equilibration at the target **temperature**, then **NVT** production **MD** on the **TPB** systems (extract).
- **Timestep:** **N/A — not stated** in `2014merinov-venue-research_p1-2.txt`.
- **Duration / stages:** **~150 ps** at **1250 K** for the **H₂** case (many reactions observed in that window); **~2 ns** at **2000 K** for the **butane** case (extract).
- **Thermostat:** **N/A — not stated** in the indexed excerpt.
- **Barostat:** **NPT** used during equilibration (extract); **N/A — barostat type/parameters** beyond **NPT** label not in excerpt.
- **Temperature:** **1250 K** (**H₂/Ni/YSZ**, near typical SOFC operation) and **2000 K** (**C₄H₁₀/Ni/YSZ**, elevated to accelerate sampling—authors caution when extrapolating to lower **temperature**, extract).
- **Pressure:** **N/A — explicit pressure targets** not quoted in the indexed excerpt beyond **NPT** equilibration mention.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated** in the indexed excerpt.

### 2 — Force-field training (Ni/YSZ ReaxFF assembly)

- **Parent FF / elements:** Combine published **YSZ** and **Ni/C/H** ReaxFF descriptions; define missing angular terms (e.g., **Ni–O–Zr**) from **combination rules**; ignore **Ni–Zr** and **Ni–Y** bonded interactions; **Ni/Y** and **Ni/Zr** nonbonded parameters from **combination rules** (extract; see **Supporting Information** pointer in letter).

## Findings

### Outcomes and mechanisms

The abstract and extract report **Ni** surface **amorphization**, **interfacial delamination** (**decohesion**), and **coking**, phenomena said to align with **experiment**. For **butane**, the authors derive a **conversion** **mechanism** at the **Ni/YSZ** **interface** with **pyrolysis-like** steps and **simulated products** matching **experiment** in their framing.

### Comparisons

The letter positions **ReaxFF** against prior **QM** validation for **YSZ** (oxygen-ion diffusion) and **Ni**/**hydrocarbon** chemistry blocks, and compares **simulation** outputs to **experimental** observations for **TPB** degradation motifs (abstract/extract).

### Sensitivity and design levers

**Temperature** is used as an explicit lever: **2000 K** accelerates sampling versus **1250 K** operating-relevant conditions; the extract notes care when mapping high-**T** observations to lower-**T** devices.

### Limitations and corpus honesty

Registered **`pdf_path`** is an **author proof**; cite **figure** labels and numbers from the **version-of-record** **PDF** when possible. **Mechanistic** detail beyond the abstract/extract should be checked against the **full letter** and **SI**.

## Limitations

Proof PDF; **high-T** reactive simulations are **force-field dependent**; extrapolation to full **SOFC** stacks requires continuum and microstructural factors not in the letter.

## Relevance to group

**van Duin** coauthored **Caltech MSC** SOFC interface study—core **oxide / Ni / hydrocarbon** reactive chemistry corpus entry.

## Citations and evidence anchors

- https://doi.org/10.1021/jz501891y — J. Phys. Chem. Lett. **5**, 4039–4043 (2014).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
