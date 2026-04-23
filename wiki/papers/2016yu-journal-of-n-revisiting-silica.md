---
id: paper:2016yu-journal-of-n-revisiting-silica
type: paper
title: "Revisiting silica with ReaxFF: Towards improved predictions of glass structure and properties via reactive molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - method:classical-md
  - material:silicate-glass
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1016/j.jnoncrysol.2016.03.026"
year: 2016
authors:
  - "Yingtian Yu"
  - "Bu Wang"
  - "Mengyi Wang"
  - "Gaurav Sant"
  - "Mathieu Bauchy"
venue: "J. Non-Cryst. Solids"
pdf_sha256: "6c6958008e5744fa7819f8060a6eef3ce5b0549e105deb216658d1bfb091fbf0"
pdf_path: "papers/ReaxFF_others/reaxff_bauchy.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016yu-journal-of-n-revisiting-silica -->

## Summary

The authors compare **ReaxFF** and a **conventional classical potential** for a model **silica glass**, assessing how well each reproduces structural disorder and selected bulk properties. The focus is whether reactive potentials can match or exceed classical descriptions for glassy silicates while remaining affordable relative to ab initio methods, including implications for later surface reactivity studies. The abstract notes that applicability of reactive potentials to glasses “remains poorly understood,” motivating a side-by-side assessment because many ReaxFF fits target crystalline oxides even though glasses are formed by quenching liquids and therefore demand accurate liquid and supercooled-liquid behavior.

## Methods

**MD application (LAMMPS).** Glassy **SiO₂** is built along **two parallel routes** in **§2.2** (`papers/ReaxFF_others/reaxff_bauchy.pdf`): **user-reaxc ReaxFF** and a **modified BKS** potential with **5.5 Å** van der Waals and **10.0 Å** Coulomb cutoffs. Each route starts from **4536 atoms** in a **cubic** cell with **3D PBC**, melted **4000 K for 100 ps**, then cooled **4000 K → 300 K** at **1 K/ps** under **NPT** at **zero pressure**, followed by **1 ns** at **300 K** to relax the glass. A **hybrid** path quenches with **BKS** only, then runs **1 ns** at **300 K** with **ReaxFF** without manual reconnectivity edits. **Supercooled-liquid** analysis (**§3.5**) uses equilibrated **liquid** trajectories above **T_g** for **MSD** and **oxygen self-diffusion**. Integration **timestep** and explicit **thermostat/barostat** damping values are **not** in the indexed **p1–2** extract—take them from **`pdf_path`** before reproducing inputs. **Electric fields** and **replica / enhanced sampling** are **not** part of the quench protocol described in the excerpt.

**Force-field training:** **N/A —** the paper **benchmarks** published **ReaxFF** and **BKS** parameterizations; it does **not** report a new fit.

**Static QM / DFT:** **N/A —** no standalone DFT production study; **QM** appears through the **ReaxFF** training literature cited in **§2.1**.

## Findings

**ReaxFF** matches **neutron S(Q)**—including the **FSDP** window—better than **BKS**, indicating more realistic **short- and medium-range disorder** in the modeled glass. **Young’s** and **shear moduli** from **ReaxFF** track **experiment** far more closely than **BKS**; **hybrid** glasses inherit **BKS-like** medium-range errors and degraded moduli, so the **hybrid** route is a poor compromise. **Oxygen self-diffusion** in the **supercooled liquid** follows **Arrhenius** trends, with **ReaxFF** activation behavior closer to **experimental** extrapolations than **BKS**. Under identical quench schedules, **ReaxFF** therefore outperforms **BKS** on both **structure** and the **bulk properties** highlighted in the article, while **BKS** remains computationally cheaper. The **1 K/ps** cooling rate is far above laboratory quenches; sensitivity to thermal history follows the glass-MD literature and limits direct mapping to experiment.

## Limitations

**Cooling rates** (**1 K/ps**) are far above laboratory quenches. **Timestep** and thermostat damping values are not recovered from the short extract used when drafting this page—confirm against **`pdf_path`** for exact reproducibility.

## Relevance to group

Benchmark-style silica-glass study using ReaxFF in the broader PARISlab/ReaxFF silica literature context (UCLA-led).

## Citations and evidence anchors

- DOI: `10.1016/j.jnoncrysol.2016.03.026`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]

## Reader notes (navigation)

