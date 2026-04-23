---
id: paper:2026mirakhory-j-chem-phys-dynamics-iodine
type: paper
title: "Dynamics of iodine geminate recombination in supercritical xenon solvent: Caging effect"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1063/5.0302862"
year: 2026
authors:
  - "M. Mirakhory"
  - "A. Majumdar"
  - "M. Ihme"
  - "A. C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "9a87a01ad3d04f342726b5ba21f81d669799e40cfe19615dab883c34b2f6c62f"
pdf_path: "papers/Mirakhory_XeI_II_JCP_2026_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026mirakhory-j-chem-phys-dynamics-iodine -->

## Summary

The work extends **Xe/I ReaxFF** training (*J. Chem. Phys.* **2025**, **162**, 194309) to **I₂** **geminate recombination** in **supercritical xenon**, emphasizing **caging**: local **Xe** **density** at recombination exceeds **bulk** by at least **~2.5×**, **coordination-number** analysis shows **clustered** solvent, and **energy** correlation between **Xe** and **recombining I** supports **kinetic-energy transfer** to the solvent. **NVT** **surveys** at **290 K** and **2–200 bar** (through **isochoric** **tuning** of the **sc** state) find **recombination** **rate** maximized **near the critical** region, with **low P** and **high P** both reducing rates (diffusion-limited or cage-limited I motion).

## Methods

- **Force field:** **Xe/I ReaxFF** from prior work—fit to **CASSCF(6,8)** **I–I**, **DFT** **Xe/Xe**, **Xe/I**, **colinear / perpendicular Xe/I₂**, **I–I–I** data, and **CCSD** **Xe–Xe**, with **single-parameter** optimization against QM energies.
- **Primary production systems:** **10,000 Xe** + **250 I** atoms (**I:Xe = 1:40** default); **energy minimization**; **multi-thermostat NVT** at **290 K** across **pressures** (**2–200 bar**) with **Berendsen** damping **1000 fs** (**Xe**) vs **1,000,000 fs** (**I**, near-**NVE**); **periodic** boundaries; **Δt = 0.25 fs**; **1 ns** trajectories; **10** independent seeds averaged.
- **Concentration checks:** additional **1:80** and **1:200** **I:Xe** ratios (**125** and **50 I**, respectively) to test **event independence** (minimum **I–I** separations to non-recombining atoms **> bond cutoff**).
- **Geminate protocols:** (**i**) **500-Xe** cells with **manual** **I₂** placement inside the **largest Xe clusters** after **1 ns** **290 K / 58.98 bar** equilibration; (**ii**) **12,500-atom** cells (**10,000 Xe**, **125 I₂**) with **temporary ReaxFF I–I bond dissociation energy** set to **zero** for **100–300 fs** bursts to initiate **dissociation**, then restored for **1 ns** **multi-thermostat NVT**—varying **dissociation interval** moves outcomes between **primary** and **secondary geminate** regimes.

**1 — MD application (atomistic dynamics).** LAMMPS ReaxFF **molecular dynamics** in **periodic** **3D** **cells** (**10,000 Xe** + **250 I** at 1:40, plus 1:80/1:200); **NVT** at **290 K**; **0.25 fs** **time step**; **1 ns** **production** **(10** **independent** **replicates**); **multi-thermostat** **Berendsen** (damping **1000 fs** on **Xe** vs **1,000,000 fs** on **I** for near-**NVE** I behavior); **2–200 bar** **thermodynamic** **pressure** for **isochoric** state points (**NVT**; **N/A** — no **NPT** **Parrinello**/**Berendsen** **barostat** in the main protocol as stated). **N/A** — no **static external electric field**; **N/A** — no **replica**/**metadynamics**/**umbrella** sampling. See bullets above for **1 ns** **(290** **K**, **58.98** **bar)** **cluster**-equilibration and **100–300 fs** **I–I** bond-off “**dissociation**” **bursts**.

**2 — Force-field training (prior ReaxFF line, used here in application).** **Xe**/**I** **ReaxFF** trained to **CASSCF(6,8)**, **DFT**, and **CCSD** **reference** data; **single**-**parameter** **optimization** to **QM** **energies**.

**3 — Static QM / DFT-only (outside ReaxFF training).** **N/A** in this work’s application section (QM serves the **ReaxFF** only).

**4 — Review** — **N/A.**
## Findings

- **Recombination rate vs pressure** peaks **near supercritical** conditions on the **reduced phase diagram**; **low-pressure** runs show **unstable** transient “recombinations” and **non-geminate** encounters; **high-pressure** **Xe** cages **hinder** **I diffusion**, lowering rates.
- **Local Xe density** around recombination **≥ ~2.5×** the **global** value; **coordination** metrics and **energy pairing** between **cluster Xe** and **I** support **cage-accelerated geminate** kinetics and **vibrational energy** flow to the **solvent**.
- **Concentration study:** recombination events remain **spatially isolated** (**Fig. 1**); **mechanism** and **average Xe coordination (~3.7)** at recombination are **insensitive** to **I** loading between **1:40** and **1:80** (1:200 **undersampled** but **consistent** qualitatively).

- **Corpus honesty / outlook:** **Excited**-state **I₂** **chemistry** is out of scope for **ground**-state **ReaxFF**; see `## Limitations` and the main text.

## Limitations

The PDF is an **accepted manuscript** notice (**AIP**); **copyedited VOR** may differ. **ReaxFF** follows **ground-state** chemistry; **excited-state** **I₂** photophysics is **explicitly excluded** (discussion cites **rapid collisional deactivation** rationale). **Elevated I concentration** vs experiment trades **sampling** for **rarity** of events.

## Relevance to group

**A. C. T. van Duin** (Penn State) co-authors; builds on the group’s **Xe/I ReaxFF** line with **Stanford** collaborators (**Majumdar**, **Ihme**).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1063/5.0302862](https://doi.org/10.1063/5.0302862)

## Related topics

- [[reaxff-family]]
