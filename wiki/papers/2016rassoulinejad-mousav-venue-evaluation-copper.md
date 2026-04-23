---
id: paper:2016rassoulinejad-mousav-venue-evaluation-copper
type: paper
title: "Evaluation of copper, aluminum, and nickel interatomic potentials on predicting the elastic properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:methods-software
  - method:classical-md
  - task:validation
  - material:alloy-bulk
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4953676"
year: 2016
authors:
  - "Seyed Moein Rassoulinejad-Mousavi"
  - "Yijin Mao"
  - "Yuwen Zhang"
venue: "J. Appl. Phys."
pdf_sha256: "b6ae7c5b4b19a1be8fa68071c41052abdb7bea921532021cceef71d643c49e79"
pdf_path: "papers/Others/NiAl_review.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016rassoulinejad-mousav-venue-evaluation-copper -->

## Summary

This **Journal of Applied Physics** study benchmarks **embedded-atom method (EAM)**-style **interatomic potentials** for **Cu**, **Al**, and **Ni** by computing **single-crystal elastic constants** \(C_{11}\), \(C_{12}\), \(C_{44}\) with **molecular dynamics** at room temperature and converting them to **polycrystalline moduli** via the **Voigt–Reuss–Hill** average. Potentials were taken from **NIST**, **Sandia**, and **LAMMPS** repositories; results are compared to **experimental** elastic data to recommend which parameterization is most reliable for each pure metal and elastic property. The work is **classical non-reactive MD** focused on **mechanical property** prediction rather than **ReaxFF** chemistry.

The motivation is pragmatic: many downstream simulations inherit EAM files packaged for alloys or defect studies without verifying elastic response against experiment for the pure elements.

## Methods

**1 — MD application (classical, non-reactive).** The authors benchmark **embedded-atom method (EAM)** potentials for **fcc Cu**, **Al**, and **Ni** drawn from **NIST**, **Sandia**, and **LAMMPS** online repositories (as stated in the article). **Molecular dynamics** at **room temperature**, described as the most broadly applicable case in their framing, is applied to **cubic single crystals**; small-strain deformation protocols yield the three independent **elastic constants** \(C_{11}\), \(C_{12}\), and \(C_{44}\). **Voigt–Reuss–Hill** averaging converts these to **isotropic polycrystalline** **bulk**, **shear**, and **Young’s** moduli and **Poisson’s ratio** for comparison to **experimental** elastic data tabulated in **J. Appl. Phys.** **Engine**, **supercell** sizes, **deformation** protocol details, **timestep**, **thermostat**, explicit **ensemble** labels, and **equilibration/production** lengths are **N/A —** not restated in the short extract used here; use **`pdf_path`**. **Reactive MD**, **electric fields**, **shear beyond the elastic test**, and **enhanced sampling** are **N/A —** outside the scope of this elastic benchmark.

**2 — Force-field training.** **N/A —** published **EAM** files are **evaluated**, not refit.

**3 — Static QM / DFT.** **N/A —** **DFT** is not the production method for the elastic constants reported here.

Bulk **fcc** supercells use standard **PBC**. **Molecular dynamics** elastic benchmarks at **room temperature** on **single-crystal** cells use potentials distributed through **NIST**, **Sandia**, and **LAMMPS** repositories (as stated in the article); unless quoted in the primary text you have open, **NVT**/**NPT** staging, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** control, and reported hydrostatic **pressure** (if any) are **N/A —** not transcribed from the short extract used here—see **`pdf_path`**. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** not part of this elastic study.

## Findings

**Outcomes.** Tabulated **simulation versus experiment** comparisons show that predicted **elastic moduli** depend strongly on which **literature EAM** is chosen; potentials developed for **alloy** or **compound** fits do not automatically reproduce **pure-element** elastic behavior.

**Design levers.** The side-by-side potential comparison is intended as a **screening** aid before large **atomistic** studies where elastic response sets stress fields.

The registered **`pdf_path`** (`papers/Others/NiAl_review.pdf`) should be reconciled with the **J. Appl. Phys.** record if manifests are audited; numerical error budgets are in the paper’s **tables**.

## Limitations

- **Room-temperature** focus; **temperature** and **size** effects in **nanowires** or **interfaces** may differ from bulk crystal benchmarks.
- The registered **PDF path** in the corpus manifest should be verified against the **JAP** article identity if sources are reconciled.

## Relevance to group

Provides **force-field benchmarking** context adjacent to **reactive** and **metallic** simulation workflows used in broader materials modeling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1063/1.4953676` (`papers/Others/NiAl_review.pdf` per manifest).

## Related topics

- [[reaxff-family]]
