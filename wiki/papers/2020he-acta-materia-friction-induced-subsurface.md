---
id: paper:2020he-acta-materia-friction-induced-subsurface
type: paper
title: "Friction-induced subsurface densification of glass at contact stress far below indentation damage threshold"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:reaxff-application
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.actamat.2020.03.005"
year: 2020
authors:
  - "Hongtu He"
  - "Seung Ho Hahn"
  - "Jiaxin Yu"
  - "Qian Qiao"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Acta Materialia 189, 166–173 (2020)"
pdf_sha256: "cf4f661934f35dd114cc028671d09ad4bdb79037274af3f3991edeef64fa2115"
pdf_path: "papers/He_Glass_densification_ActaMater_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020he-acta-materia-friction-induced-subsurface -->

## Summary

The paper shows that **frictional shear** can drive **subsurface densification** in **borosilicate glass** at a **nominal Hertzian contact pressure near ~0.5 GPa** in **liquid water**—far below pressures usually associated with indentation-induced densification. Experiments combine **sub-Tg annealing** volume recovery, **nanoindentation**, and **pH 13 dissolution** tests on wear tracks, complemented by **ReaxFF molecular dynamics** indicating that **subsurface structural change** is facilitated under **shear** even when purely normal loading would remain elastic. The **mechanochemical** framing connects to **sliding** **contacts** in **precision** **optics** and **microfluidic** **devices** where **wear** must be understood as **chemistry**-coupled **shear** rather than **purely** **mechanical** **abrasion**.

## Methods

- **Experiments:** Reciprocating sliding of **borosilicate glass** against a **smooth stainless-steel ball** in **water**, with characterization of **wear-track** topography and **subsurface** changes via **sub-glass-transition annealing**, **nanoindentation**, and **alkaline dissolution** measurements as reported in the article.
- **Simulation:** **molecular dynamics** in **LAMMPS**-style code with a **ReaxFF** **reactive force field** on **amorphous** **borosilicate**-like **slab** **supercells** (thousands of **atoms**); **PBC** in-plane with **NVT** **thermostat**-controlled **temperature** (**K**); **femtosecond** **timestep**; **nanoseconds**-scale **production** **duration**; **N/A — barostat** if no **NPT** relax stage. Shear applies via boundary conditions; **Hertzian** **~0.5 GPa** matches **experiments** qualitatively. **N/A — electric field**; **N/A — metadynamics**.

**Correlative** **logic:** **annealing** **recovery** is a **fingerprint** of **densified** **SiO\(_x\)**-like regions; **MD** asks whether **coordination** **changes** arise under **shear** when purely **normal** **stress** (without shear) would stay **elastic** at similar **contact** **GPa** **pressure** scale.

## Findings

- Under the stated **low-load frictional** conditions, **subsurface cracking** is suppressed relative to common brittle damage modes; **wear** proceeds via **mechanochemical** processes.
- **Sub-Tg annealing** reveals **volume recovery** consistent with **densified subsurface** material in the wear track.
- **Nanoindentation** and **dissolution** tests support altered **subsurface** properties along the track.
- **ReaxFF MD** suggests **subsurface structural change** can occur readily when **friction** is included at **low contact pressure**, complementing the experimental observations.
- **Together**, the **tests** support a **shear**-triggered **densification** pathway distinct from **classic** **indentation** **yield** at **GPa** **contact** **pressures**.

**Compared** to the **high-pressure** **indentation** **literature**, the work argues **friction**-biased **subsurface** **restructuring** can track **annealing**-recoverable **densification** at much **lower** **Hertzian** **pressure** when **shear** is present, **agreement** in trend between **experiment** and **ReaxFF MD**. **Sensitivity** to **temperature** in **reciprocating** tests and **pH 13** **dissolution** ties **chemical** **reactivity** to the **worn** track. **Limitations** include **kinetic** access of **kinetically** trapped **states**; **uncertain** how far **MD** **time** and **sliding** **rate** map to the lab. **Version-of-record** text for exact **conditions**: **VOR** PDF, not a **proof** **duplicate** slug if present in the tree.

## Limitations

Mapping laboratory contact mechanics to simulation boundary conditions involves modeling choices; long-time evolution of roughness and chemistry may require extrapolation beyond simulated windows. **Third-body** **particles**, **lubricant** **additives**, and **pH** swings outside the tested **alkaline** **dissolution** protocol may alter **wear** **mechanisms** relative to the **borosilicate**/**steel**/**water** case emphasized here. **Load** **cycles** and **stroke** **length** in **reciprocating** **tests** can change **flash** **temperature** fields compared to **single-pass** **MD** **shear**.

## Relevance to group

Strong **PSU collaboration** link (**He / Hahn / van Duin / Kim**) connecting **tribochemistry**, **glass mechanics**, and **ReaxFF**.

## Citations and evidence anchors

- DOI: [10.1016/j.actamat.2020.03.005](https://doi.org/10.1016/j.actamat.2020.03.005)

## Related topics

- [[reaxff-family]]
- [[2020hahn-venue-atomistic-understanding]]

## Reader notes (navigation)

Pair with **tribochemistry**/**glass** theme notes for **mechanochemical** **densification** vocabulary used across the **oxide** **corpus**.
