---
id: paper:2019wen-j-phys-chem-atomistic-insights
type: paper
title: "Atomistic insights into Cu chemical mechanical polishing mechanism in aqueous hydrogen peroxide and glycine: ReaxFF reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - material:metal-surface
  - material:oxide
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:tribology
  - keyword:water-interfaces
source_refs: []
doi: "10.1021/ACS.JPCC.9B08466"
year: 2019
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Diana M. van Duin"
  - "Yuanzhong Hu"
  - "Xinchun Lu"
venue: "J. Phys. Chem. C (2019), 123, 26467-26474"
pdf_sha256: "742e9dd1ca3c5587384c37bee900e70830d1080b98d803f136499c9d819dc169"
pdf_path: "papers/Wen_JPCB_2019_Cu_polishing.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019wen-j-phys-chem-atomistic-insights -->

!!! abstract "Scope"

    **ReaxFF MD** of a **Cu / aqueous H₂O–H₂O₂–glycine / hydroxylated SiO₂ abrasive** stack models **CMP**-like **shear** under high **normal load**, emphasizing **slurry chemistry** and **Cu removal** pathways.

## Summary

Wen *et al.* simulate **chemical mechanical polishing (CMP)**-relevant chemistry at a **copper** surface contacted by a **hydroxylated silica** abrasive and an **aqueous** mixture of **water**, **hydrogen peroxide**, and **glycine**. The goal is atomistic clarity on how **oxidation**, **proton transfer**, and **mechanochemical** shear combine to enable **material removal** in **Cu** **CMP**, where industrial slurries are far more complex but share the same **oxidant + complexing agent + abrasive** motifs. The **ReaxFF** model spans **Cu**, **Si/O/H** abrasive chemistry, and **organic** **glycine** fragments, with development context and **DFT** checks (including **NEB** references for key **water** steps) summarized in the article. **Adri C. T. van Duin** and **Diana M. van Duin** appear among authors, tying the publication to the group’s **tribochemistry** and **oxide–metal** interface expertise.

## Methods

### ReaxFF model lineage (A)

**ReaxFF** spans **Cu**, **Si/O/H** abrasive chemistry, and **organic** **glycine**/oxidant chemistry with **DFT**/**NEB** support cited in **JPCC** for key steps (see article).

### Mechanochemical CMP protocol (B)

**System** (**Fig. 1**): **Cu(111)** slab (**4369 Cu**), **hydroxylated SiO₂** abrasive (**1296 Si**, **2708 O**, **232 H**), slurry **200 H₂O**, **10 H₂O₂**, **5 glycine** in **~6.34 × 5.90 × 4.50 nm**; **periodic xy**; bottom **Cu** layers **frozen**, **silica** tool **rigid**/**movable**. **Load** to **~6.0 GPa** normal pressure on abrasive, **25 ps** equilibration, then **shear** **40 m/s** (**0.4 Å/ps**) for **300 ps** along **x**. **LAMMPS**, **NVT**, **300 K**, **Nose–Hoover** (**100 fs** thermostat damping), **Δt = 0.25 fs**; **Ovito** visualization.

### Static QM (C)

**DFT/NEB** references support specific **barrier** claims—not a standalone static study.

**Barostat / hydrostatic pressure:** **N/A** — production shear uses **NVT** at **300 K** with **~6.0 GPa** **normal** **load** on the abrasive (mechanical **stress** in the interfacial stack) rather than **NPT** fluid **pressure** control. **Electric field:** **N/A** — not used. **Replica / enhanced sampling:** **N/A** — not reported for this **CMP** shear study.

## Findings

### Mechanisms (removal pathways)

**H₂O** **chemisorbs**; **H₂O₂** **dissociates** toward **Cu–OH**-rich surfaces. **Silanol** groups mediate **proton-transfer** coupling **abrasive** to **slurry**. Under **shear**, **Cu removal** proceeds via **glycine-**, **OH-**, and **Cu–O–Si bridge** channels (**§3.2+**)—**oxidation + ligand-assisted lift-off** vs pure **abrasion**.

**Glycine** **carboxylate**/**amine** **interactions** with **Cu** **oxides** compete with **peroxide-driven** **oxidation**, so **removal** is not a single **mechanical** **scrape** but a **coupled** **ligand**/**oxide**/**abrasive** sequence consistent with **industrial** **CMP** slurry design heuristics.

### Limitations / outlook

Single-asperity, high **load/speed** idealization; industrial **slurry** complexity (**pH**, **inhibitors**, **particles**) not fully captured. **Sensitivity** in the modeled **stack** is to **normal load** (**~6.0 GPa**), **shear speed** (**40 m/s**), and **reagent** counts (**H₂O**/**H₂O₂**/**glycine**) as in **Fig. 1**; broader **process** **maps** in the **PDF** add nuance. **Corpus honesty:** use the **JPCC** **PDF** for **table**-level **repro** detail.

## Limitations

A **single** asperity and **high** load/speed are idealizations; industrial **slurries** include **particles**, **inhibitors**, and **pH** buffers not modeled here.

## Relevance to group

Detailed **ReaxFF CMP** case study with explicit **mechanochemical** pathways (van Duin / consulting-affiliation context in the publication).

## Citations and evidence anchors

DOI: [10.1021/acs.jpcc.9b08466](https://doi.org/10.1021/acs.jpcc.9b08466)

## Related topics

- [[reaxff-family]]
