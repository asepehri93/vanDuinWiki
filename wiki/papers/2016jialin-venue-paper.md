---
id: paper:2016jialin-venue-paper
type: paper
title: "Atomic insight into tribochemical wear mechanism of silicon at the Si/SiO2 interface in aqueous environment"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.apsusc.2016.08.082"
year: 2016
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
  - "Lei Chen"
  - "Linmao Qian"
  - "Yuanzhong Hu"
  - "Xinchun Lu"
venue: "Applied Surface Science"
pdf_sha256: "25f6451965c48fbd140b1419cc72e5db298e3ee9907886dee494a63085fba6bb"
pdf_path: "papers/Jialin_Wen_AppSurfSci_2016_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
paper_keywords:
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:galley-or-proof-pdf
---
<!-- id:paper:2016jialin-venue-paper -->

## Summary

**ReaxFF MD** in **LAMMPS** models **tribochemical wear** of **single-crystal silicon** against **hydroxylated amorphous silica** with an **aqueous interlayer**, focusing on **Si removal pathways** and how **normal pressure** and **water** jointly control **oxidation** versus **mechanical detachment**. The setup mimics **AFM**-like **contact** with a **rigid** **counterbody** and explicit **water** to capture **stress-assisted** **hydrolysis** at **Si/SiO\(_2\)** **junctions** relevant to **chemical mechanical polishing** and **MEMS** reliability. **Weiwei Zhang** and **Adri C. T. van Duin** coauthor the **reactive** modeling line.

## Methods

**LAMMPS** runs use **ReaxFF** for Si/Ge/H and H₂O (parametrization citations [26,27] in the article; SI for additional validation). Separate equilibration builds **H/OH/H₂O-passivated Si(100)** and **hydroxylated silica**, then stacks them with **~300** water molecules in a sandwich geometry (SI figures S3b / S5b). The wear cell is a multilayer slab-on-slab stack with **4.26 nm × 4.26 nm** in-plane periodicity, a rigid bottom Si slab, and a rigid movable top silica counterface to mimic AFM-like contact; normal stress on the top body is stepped at **2.0**, **4.0**, and **6.0 GPa**. Production segments use **NVT** at **300 K**, **Nosé–Hoover** thermostat (**100 fs** damping), **velocity Verlet**, and **Δt = 0.25 fs**, with **OVITO** postprocessing. Out-of-plane cell thickness, full equilibration versus production durations, and electrostatic or QEq update details are not recovered from the short proof excerpt used here—see the *Appl. Surf. Sci.* article PDF. In-plane **PBC** applies to the wear patch; vacuum separates the stack along the interface normal as in the cited SI figures. Wear loading replaces hydrostatic **NPT** control; external electric fields and bias-based enhanced sampling are not used.

**Force-field training.** **N/A** — applies published ReaxFF parametrizations.

**Static QM / DFT.** **N/A** — reactive MD study.

## Findings

The abstract describes two Si removal pathways: (i) breaking stressed Si–O–Si bridges on Si with H attaching to bridging O; (ii) rupturing Si–Si bonds in stressed Si–Si–O–Si chains at the interface—both removing Si via interfacial Si–O–Si bridges. The work is framed against AFM tribology on Si/silica/water where load and water strongly affect wear but experiments lack molecular resolution. Normal load on the silica counter-slab (**2.0–6.0 GPa** in the protocol above) increases Si removal by promoting interfacial Si–O–Si bridge formation; water both oxidizes the Si surface and spaces surfaces to reduce intimate contact. Detailed outlook beyond the abstract belongs in the version-of-record issue; this corpus `pdf_path` is an uncorrected proof—confirm pagination versus *Appl. Surf. Sci.* **390**, 216–223 (2016).

## Limitations

Corpus PDF is an **uncorrected proof**; confirm **pagination** against the **Applied Surface Science** issue. Proof-stage **journal page placeholders** appear in some headers. For **corpus** notes on **proof** PDFs, see [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Relevance to group

**van Duin co-authorship**; **ReaxFF tribochemistry** for **Si/SiO₂/water** stacks relevant to **CMP** and **MEMS** wear discussions.

## Citations and evidence anchors

- DOI: [10.1016/j.apsusc.2016.08.082](https://doi.org/10.1016/j.apsusc.2016.08.082) — *Appl. Surf. Sci.* **390**, 216–223 (2016).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

For **CMP**-relevant **wear** **rates**, combine these **atomistic** **stress** **thresholds** with **continuum** **contact mechanics**; this paper supplies **chemistry-aware** **removal** **pathways**, not **engineering** **wear** **coefficients** measured at **wafer** scale. **Normal** **load** sweeps (**2.0–6.0 GPa**) map to **fixed** **displacement** control on the **rigid** **silica** **plate** as described in **Applied Surface Science**.
