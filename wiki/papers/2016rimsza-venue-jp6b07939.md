---
id: paper:2016rimsza-venue-jp6b07939
type: paper
title: "Water interactions with nanoporous silica: Comparison of ReaxFF and ab initio based molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - method:aimd
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b07939"
year: 2016
authors:
  - "J. M. Rimsza"
  - "Jejoon Yeon"
  - "A. C. T. van Duin"
  - "Jincheng Du"
venue: "J. Phys. Chem. C"
pdf_sha256: "d3170c8e85355d7001264f6cc194620e9920ad3ca974f3d482096e052e1d931a"
pdf_path: "papers/Rimsza_JPC_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016rimsza-venue-jp6b07939 -->

## Summary

Rimsza *et al.* compare **ReaxFF** and **ab initio molecular dynamics (AIMD)** for **water** interacting with **nanoporous silica**, focusing on how well classical **reactive MD** reproduces **QM**-level structure, **reaction** barriers, and **transport** trends in **confined** **Si/O/H** environments. Two **Si/O/H ReaxFF** parametrizations—associated with **Yeon *et al.*** and **Fogarty *et al.*** in the article’s framing—are evaluated against **AIMD** references on **high-defect**, **strained** silica motifs where **water dissociation**, **hydroxylation**, and **small-ring** defect chemistry are sensitive tests of the classical model. **Adri C. T. van Duin** is a coauthor, linking the paper to the group’s long-running **silica–water** **ReaxFF** development lineage and to **geochemical**/**materials** applications where **nanopores** alter **H-bond** networks and **reaction** kinetics.

## Methods

**1 — MD application (ReaxFF and AIMD).** The study compares **ReaxFF** and **DFT-based ab initio molecular dynamics (AIMD)** for **water** in **nanoporous silica** models that expose **high-defect**, **strained** **Si/O/H** environments. **Reactive classical MD** uses two literature **Si/O/H** parameterizations—the **Yeon *et al.*** set (*J. Phys. Chem. C* **2016**) and the **Fogarty *et al.*** set (*J. Chem. Phys.* **2010**)—on the same classes of structures simulated at the **AIMD** level. Observables include **local Si–O–Si and Si–OH** speciation, **water dissociation** propensity, pathways and energetics for **two-membered (2-ring) siloxane** defect removal, **hydroxylation** kinetics, and **H** versus **O** **diffusion** under **nanoconfinement**. **Engine**, **system sizes** (atom counts), **PBC**, **ensemble**, **timestep**, **thermostat/barostat**, **temperature and pressure**, **run lengths**, **electrostatics**, and **QEq** usage are **N/A —** not transcribed on this wiki page; read **`pdf_path`** and any SI. **Electric fields** and **enhanced sampling** beyond conventional **MD/AIMD** are **N/A —** not highlighted in the short abstract-level material used for this note.

**2 — Force-field training.** **N/A —** the paper **benchmarks** published **ReaxFF** parameterizations rather than publishing a full new fit as its main contribution.

**3 — Static QM / DFT.** **AIMD** on comparable **nanoporous silica** motifs supplies the **QM** reference for structures, barriers where reported, and diffusion trends; detailed **DFT** functional, basis, and **k**-sampling choices are **N/A —** not duplicated here—see the article.

Both **ReaxFF** and **AIMD** use **PBC** supercells with explicit **Si/O/H** stoichiometry as in the published models. **Molecular dynamics** protocol tables in **`pdf_path`** should list the engine (e.g. **LAMMPS** for **ReaxFF**), **supercell** atom counts, **NVT**/**NPT** staging, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** control, and target **temperature** (K). Those numerical fields are **N/A —** not transcribed on this page unless they appear above. Shear, **electric field** driving, and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** not highlighted in the abstract-level excerpt used here unless the full text introduces them.

## Findings

**Outcomes and mechanisms.** Competing **reaction pathways** and **intermediate** geometries affect **2-ring** defect removal and **hydroxylation** rates, so **defect-rich** nanoporous silica is a strong discriminator between **ReaxFF** parametrizations. **Nanoconfinement** lowers **water diffusion** relative to bulk-like water. **Hydrogen** diffuses roughly **10–30%** faster than **oxygen** in the nanoconfined regime discussed in the abstract, consistent with **H-hopping** contributions emphasized in the article.

**Comparisons.** For the **high-defect** **Si/O/H** benchmark suite in the paper, the **Yeon *et al.*** **ReaxFF** parametrization tracks **AIMD** more closely than the **Fogarty *et al.*** set on the observables highlighted in the abstract (mechanisms, hydroxylation, defect populations, activation energies where quoted).

**Sensitivity and limitations.** Results are **parametrization-dependent**; **AIMD** itself depends on **DFT** approximations. Quantitative values should be taken from **J. Phys. Chem. C** figures and tables rather than this summary.

## Limitations

**Parametrization dependence** implies residual uncertainty for **complex amorphous** **silica** and **high-pH** chemistry outside the training scope. **AIMD** references themselves depend on **DFT** choices; treat disagreements as **triangulation** opportunities rather than automatic **ReaxFF** failure.

## Reader notes (navigation)

This benchmark is frequently cited next to **geochemistry** theme pages; keep **`task:validation`** prominent in frontmatter so **application** papers do not drown out **method** comparisons in retrieval.

## Relevance to group

Direct **ReaxFF** validation work for **silica–water** interfaces with **van Duin** authorship.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.6b07939` (`papers/Rimsza_JPC_2016.pdf`).

## Related topics

- [[reaxff-family]]
