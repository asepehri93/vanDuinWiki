---
id: paper:2024meral-sharkass-j-phys-chem-oxidation-tungsten
type: paper
title: "Oxidation of Tungsten at Room Temperature Irradiated by Oxygen Plasma"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - method:dft-static
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:reactive-md
  - keyword:oxide-surface
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c03664"
year: 2024
authors:
  - "Meral Sharkass"
  - "Swarit Dwivedi"
  - "Yun Kyung Shin"
  - "Martin Nieto-Perez"
  - "Adri C. T. van Duin"
  - "Predrag S. Krstic"
venue: "J. Phys. Chem. C 2024 (ASAP; see DOI for issue/pages)"
pdf_sha256: "f3a65308c6fa6fae6240898cf5ff56bb8d5b3438e57653ebeb38e60b35cb53a1"
pdf_path: "papers/sharkass-et-al-2024-oxidation-of-tungsten-at-room-temperature-irradiated-by-oxygen-plasma.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024meral-sharkass-j-phys-chem-oxidation-tungsten -->

## Summary

A **W–H–O ReaxFF** parametrization is developed with **DFT** references from **ADF** (**molecular** scans) and **VASP** (**PBE** **PAW**, **520 eV**, **DFT-D3**, **Γ-centered 10×10×1** **k**-meshes, **20 Å** vacuum for slabs), including **ZBL** close-range **W–W** and **W–H** pairs and **W–O** training against **bulk**, **surface**, **oxide** **EOS**, and **oligomer** energetics. **LAMMPS** **ReaxFF** simulations prepare **BCC W(001)** slabs (**28×28×84 Å**, **4374 W**), equilibrate to **300 K**, then **cumulatively** deposit **4500** **O** atoms at **1**, **10**, or **30 eV** (below physical **W** sputtering by **O** at **~40 eV** as cited), with **1 fs** timestep, cascade evolution, and **0.5 ps** **Langevin** cooling to **300 K** between impacts. Additional runs probe **O** **reflection** and **chemical sputtering** from **pre-oxidized** surfaces.

## Methods

- **FF training:** Single-parameter search minimizing **QM vs ReaxFF** error; **EEM** charges vs **Mulliken** **PBE**; **W** **BCC** lattice, **defect**, **surface**, **H** interstitial/adsorption data; **WO\(_x\)** **EOS**, **surface energies**, **oxide** molecule **ΔH** ladder (Section 2.1).
- **Surface preparation:** **Steep descent** minimization (**10\(^{-8}\)** force tolerance); **Langevin** heating to **300 K**; **NVE** relaxation; cleave to **2D** periodic **slab**; repeat; **0.5 fs** timestep with **charge equilibration** each step.
- **O irradiation:** **4500** sequential **O** impacts per scenario; impact area **~529 Å\(^2\)** with **5 Å** buffer; interval **3–4 ps** between impacts depending on energy; **3000–4000** steps per impact; post-impact **Langevin** **300 K** cooling **0.5 ps**; reported fluxes **~2.1–2.83×10\(^{32}\)** **O m\(^{-2}\) s\(^{-1}\)**.
- **Analysis:** **Adlayer** thicknesses, **O** depth profiles, **n\(_O\)/n\(_W\)** ratios approaching **WO\(_3\)**-like stoichiometry in upper bins; separate **1000**-impact studies on **low** vs **high** **O** coverage slabs (**A-deps** / **B-deps**).

**1 — MD (O bombardment / cascade + cooling).** **Engine:** **LAMMPS** **ReaxFF**; **1 fs** timestep in **O**-impact stages; **EEM** + **0.5 fs** during equilibration as stated. **System:** **BCC W(001)**, **4374 W** in **~28×28×84 Å**; **O** **cumulative** **4500** impacts, **1 / 10 / 30 eV**; **NVE** during impact, **0.5 ps** **Langevin** to **300 K** between events; **2D PBC** **slab**. **Barostat, NPT, E-field, umbrella, MTD:** **N/A** in the summarized protocol. **2 — W–H–O ReaxFF training** in the first **FF** bullet; **3 — Static QM (ADF + VASP)** in the **summary** lede and **DFT** bullet list.
## Findings

- **Cumulative** **low-energy** **O** impacts build **mixed W–O adlayers** **12–23 Å** thick (depending on **1–30 eV** scenarios) atop **W(001)** before **saturation**, after which additional **O** predominantly **reflects** or ejects **adlayer** species (**Figure 4** trends).
- **Higher impact energy** drives **O** deeper before saturation (**O** extends up to **~5–13 Å** into the metal depending on case), altering **saturation fluence** vs **1 eV** impacts.
- **n\(_O\)/n\(_W\)** profiles show **≥3:1** **O:W** in upper **adlayer** bins, with **B–A–B** interfacial regions nearer **~1.7:1** as described—linking atomistic profiles to **WO\(_x\)**-like oxidation fronts.
- Follow-on **single-impact** studies on **oxidized** slabs quantify **O** **reflection** vs **sputtering** channels that matter for **plasma-facing** **W** under **oxygen** impurity flux. **Sensitivity** to **impact energy** and **O** **coverage** is the main parametric axis in the text above; **J. Phys. Chem. C** **ASAP** **PDF** (issue/pages per DOI) is authoritative.
## Limitations

**Classical** **ReaxFF** cannot capture **electronic** sputtering or full **fusion** **D**/**T** inventories; **300 K** **substrate** cooling between **ps**-scale impacts is a stand-in for experimental **flux**/**time** separation.

## Relevance to group

**van Duin**/**Shin** collaboration on **fusion**-relevant **W** oxidation with **ReaxFF** **plasma**-like **O** bombardment.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c03664](https://doi.org/10.1021/acs.jpcc.4c03664)

## Related topics

- [[reaxff-family]]
