---
id: paper:2013zhang-computationa-mixed-pattern-cracking
type: paper
title: "Mixed-pattern cracking in silica during stress corrosion: A reactive molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:water-interfaces
  - keyword:silica-silicate
  - keyword:nvt-simulation
source_refs: []
doi: "10.1016/j.commatsci.2013.09.045"
year: 2013
authors:
  - "Yun-An Zhang"
  - "Junyong Tao"
  - "Xun Chen"
  - "Bin Liu"
venue: "Comput. Mater. Sci."
pdf_sha256: "2cc0f252c4139a91ca048f06c73eb9a85e851952cbb875d9cc99e570c1dcdc68"
pdf_path: "papers/ReaxFF_others/Zhang 2014 _ ReaxFF MD of stress corrosion.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013zhang-computationa-mixed-pattern-cracking -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Crack velocities and strain values are stated in the article; do not treat this page as a substitute for the paper’s tables and figures.

## Summary

**ReaxFF MD** is used to study **stress corrosion cracking (SCC)** of **strained α-quartz** in **liquid water** vs a **dry** reference. Over the **3 ns** trajectory described in the abstract, **no crack growth** is seen for **dry** quartz at **23% strain**, whereas **substantial propagation** appears in **water** at **lower** strains (**17%, 20%, 22%**). Reported **crack speeds** in water decrease with increasing strain in that abstract’s listing, and **crack-tip strain** analysis ties growth to **hydrolysis** of **strained Si–O** bonds at the tip. The work also discusses **mixed** cracking modes combining **stress corrosion** and more **brittle**, stress-driven failure as **load** increases.

## Methods

### Force field (ReaxFF Si/O/H)

- **ReaxFF** follows the **van Duin** reactive force-field formulation with **bond-order**-dependent energetics and **dynamic charge equilibration** appropriate for **Si/O/H** chemistry (introduction/methods excerpt). Parameters for **Si/O/H** are taken from prior **benchmarking** studies on **bulk silica**, **liquid water**, and **silica–water interfaces** cited as **validated** against **QM** and experiment in the article.

### System construction

- **α-quartz** supercell: **14 × 9 × 3** rectangular unit cells built from cells of **~4.91 × 8.50 × 5.42 Å** containing **12 Si** and **6 O** each; an **~12 Å** **notch** seeds a crack-like defect (**Methods** section).
- **Relaxation:** the **notched** sample is equilibrated in the **canonical (NVT) ensemble at 300 K for 50 ps** before loading (extract).

### Wet vs dry setups and loading

- **Wet interface:** a **68 × 37.5 × 15.3 Å** cell contains **1000 H₂O** molecules placed with random positions/orientations at **0.99 g cm⁻³** after **energy minimization** (extract; minimization paragraph continues in the PDF beyond the clipped extract).
- **Dry reference:** simulations without the liquid water region are compared under **23% strain** in the abstract’s dry case.
- **Straining / SCC trajectories:** the abstract highlights **3000 ps** SCC runs with **no growth** for **dry** quartz at **23% strain**, versus **substantial propagation** in **liquid water** at **17%, 20%, and 22% strain**.
- **Timestep, thermostat damping, and nonbond cutoffs** for production SCC runs are **not stated** in the checked-in **`normalized/extracts/2013zhang-computationa-mixed-pattern-cracking_p1-2.txt`** (text ends mid minimization paragraph); consult the **Comput. Mater. Sci.** PDF for integration settings.

**Force-field training:** **N/A —** the work **uses** a validated **Si/O/H ReaxFF** parameterization from prior silica–water literature (as cited in the article); it does not report a **de novo** ReaxFF fit in this paper.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive MD** with **ReaxFF**; integrator package **N/A — not stated** in the p1–2 extract (`papers/ReaxFF_others/Zhang 2014 _ ReaxFF MD of stress corrosion.pdf`). **System:** notched **α-quartz** supercell (**14 × 9 × 3** unit cells of ~**4.91 × 8.50 × 5.42 Å** each, **12 Si** and **6 O** per cell) plus **~12 Å** notch; **wet** cells add **1000 H₂O** in **~68 × 37.5 × 15.3 Å** at **0.99 g cm⁻³** after minimization (Methods / extract). **Boundaries / periodicity:** **3D PBC** bulk with notch and optional water region; exact lattice vectors **PDF-grounded**. **Ensemble:** **NVT** at **300 K** for **50 ps** pre-strain equilibration of the notched solid (extract). **Timestep / thermostat / barostat / duration for production SCC:** **N/A — not in the p1–2 extract** beyond the abstract’s **3 ns** SCC window and strain percents—see article. **Temperature:** **300 K** equilibration; SCC strains **17–23%** as in abstract. **Pressure:** **N/A —** strain-controlled mechanics rather than quoted **NPT** targets here. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used. **Shear / shock:** **N/A —** not the reported protocol in the abstract-level summary.

## Findings

- Over **3 ns**, **no crack growth** appears for **dry** quartz at **23% strain**, whereas **substantial propagation** occurs in **liquid water** at **17%, 20%, and 22% strain**.
- In water, **crack speeds** are reported as **7.1 m/s**, **3.1 m/s**, and **0.57 m/s** at **17%, 20%, and 22% strain**, respectively—**all faster** than the **bulk experimental** crack velocity quoted in the article for comparison.
- **Crack-tip strain maps** and **species analysis** tie growth to **hydrolysis of strained Si–O bonds** at the tip; at **higher applied strain**, the authors describe **mixed-mode** response combining **stress-corrosion** growth with more **brittle**, **stress-driven** fracture.

## Limitations

- **Nanoscale** models and **short** times vs **macroscopic** SCC; **ReaxFF** accuracy for **silica** chemistry under extreme strain must be judged against the paper’s benchmarks.

## Relevance to group

**Stress corrosion** of **silica** is a recurring theme in **oxide** reliability; **ReaxFF** provides an atomistic picture of **water-assisted** bond rupture at **crack tips**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.commatsci.2013.09.045` (`papers/ReaxFF_others/Zhang 2014 _ ReaxFF MD of stress corrosion.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
