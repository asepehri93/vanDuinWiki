---
id: paper:2016yeon-venue-jp5b09784
type: paper
title: "ReaxFF Molecular Dynamics Simulations of Hydroxylation Kinetics for Amorphous and Nano-Silica Structure, and Its Relations with Atomic Strain Energy"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - method:reaxff
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b09784"
year: 2016
authors:
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "6f15c7d3e39ac8f9fb34da373fdffe68ab4f923215321322845a5a7b143a3e58"
pdf_path: "papers/Yeon_Silica_hydrolysis_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yeon-venue-jp5b09784 -->

## Summary

Reactive molecular dynamics with ReaxFF is used to follow water–silica hydrolysis on nanostructured and amorphous SiO₂, with a ReaxFF parameter refinement starting from the Fogarty et al. (2010) SiO₂–water description so that hydroxylation barriers for strained versus unstrained Si–O motifs better match DFT reference data. The work ties silanol formation to local strain and maps multiple hydroxylation pathways, including routes involving H₃O⁺, with implications for where water-derived chemistry localizes on silica under mechanical stress.

## Methods

**2 — Force-field training (ReaxFF SiO-2015).** **Parent:** **Fogarty *et al.*** **SiO/water** interaction set. **QM reference:** **B3LYP/6-311++G(d,p)** barrier scans for **strained vs unstrained** **Si–O–Si–O** ring **dimers** feeding additional training points; **Si–O** bond/off-diagonal terms, **Si–O–Si**, **O–Si–O**, **O–Si–Si**, and **O–H–O** hydrogen-bond parameters are reoptimized to match the **DFT** curves (**Figure 3**). **Post-fit barriers:** **~31 kcal/mol** (**unstrained dimer**) and **~20 kcal/mol** (**strained dimer**) without **ZPE** corrections (**ZPE < 1 kcal/mol** per the article).

**1 — MD application (ReaxFF).** **Engine / code:** **LAMMPS** molecular dynamics with the **SiO-2015** **ReaxFF** parameter file described above. **Nanowire hydration test:** **108 atoms** (**36 Si + 72 O**) nonperiodic **nanowire** in a **30 × 30 × 30 Å\(^3\)** cell with **200 H\(_2\)O** (**~0.22 kg/dm\(^3\)** water density), **800 ps** **NVT** segments at each **100 K** step from **300 K** to **1500 K** using **Berendsen** thermostat (**100 fs** damping) and **0.1 fs** timestep (**§2.2**). Additional setups (**double-slit amorphous silica**, **strained surface dimers**) extend the same **SiO-2015** model to compare **pathways** vs **temperature** (**§2.3–2.4**). **Barostat:** **N/A —** **NVT** water-vapor boxes. **Pressure control:** **N/A —** not **NPT**; cells are held at the **vapor density** stated for each tutorial box. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**3 — Static QM.** Covered under the **training** block (**B3LYP** dimer scans).

**4 — Reviews.** **N/A —** primary research article.
## Findings

**Barrier agreement.** After **SiO-2015** reoptimization, **ReaxFF** reproduces the **DFT** hydroxylation **barrier ordering** for **strained vs unstrained** **Si–O** dimers with the **~20 / ~31 kcal/mol** targets quoted post-fit (**Figure 3**).

**Strain localization.** **Nanowire** trajectories show **silanol** genesis preferentially at **high-strain edge** sites (**Figures 4–5**), linking **atomic strain energy maps** to **reaction propensity**.

**Pathways and temperature.** The article documents multiple **H\(_3\)O\(^+\)**-mediated sequences (**Figure 6** at **400 K**) plus **direct water dissociation** channels that become more frequent at **>1000 K** (**Figure 8** narrative), and summarizes how the **H-bond network** reorganizes across the **300–1500 K** sampling ladder.

**Amorphous silica.** **Double-slit** **a-SiO\(_2\)** runs mirror the **nanowire** lesson: **silanols** concentrate where **strain** is elevated, with similar **hydronium** involvement (**§2.4–2.5**).

**Tribology link.** The **Discussion** ties **strain-biased hydroxylation** to where **water-derived films** may anchor on **stressed silica** contacts—read that section for caveats on **transferability** to engineering interfaces.

## Limitations

Quantitative barrier values, additional pathway figures, and any SI-only benchmarks should be taken from the **PDF** at `pdf_path` (the indexed extract here is first pages only).

## Relevance to group

Penn State / van Duin-group ReaxFF development and silica–water chemistry relevant to tribology and oxide interfaces.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.5b09784` (J. Phys. Chem. C).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
