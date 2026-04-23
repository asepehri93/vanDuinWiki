---
id: paper:2020hahn-venue-paper
type: paper
title: "Atomistic understanding of surface wear process of sodium silicate glass in dry versus humid environments (publisher proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1111/jace.17008"
year: 2020
authors:
  - "Seung Ho Hahn"
  - "Hongshen Liu"
  - "Seong H. Kim"
  - "Adri C. T. van Duin"
venue: "J. Am. Ceram. Soc. (proof/galley duplicate in corpus)"
pdf_sha256: "3b9524d72324a1366f5f1ca834c75c5f31bc286827be4cb760d729147c4c1dc2"
pdf_path: "papers/Hahn_Surface_Wear_JACerS_2020_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020hahn-venue-paper -->

## Summary

This slug registers **`papers/Hahn_Surface_Wear_JACerS_2020_galley.pdf`**, a **publisher proof / galley** for the *Journal of the American Ceramic Society* article on **ReaxFF molecular dynamics** of **mechanochemical wear** at **sodium silicate glass** / **silica** interfaces in **dry** versus **humid** sliding. The peer-reviewed study (DOI `10.1111/jace.17008`) uses **large-scale** **LAMMPS** simulations with a **Na/Si/O/H** **ReaxFF** description to follow **bond formation and rupture** at **asperity–counterface** contacts, focusing on how **interfacial bridging** species and **alkali-assisted hydrolysis** couple **mechanical load** to **chemical** rearrangement. **`[[2020hahn-venue-atomistic-understanding]]`** lists **timestep**, **temperature**, **normal load**, **shear velocity**, **humidity** realization, and **analysis** metrics needed to reproduce the simulations. The peer-reviewed **version of record** for DOI **`10.1111/jace.17008`** is curated on **`[[2020hahn-venue-atomistic-understanding]]`** with the clean journal PDF path. The scientific story concerns how **interfacial bridging bonds** and **sodium-assisted hydrolysis** change when **water** is present at the sliding interface, altering **wear** morphology and **subsurface** coupling relative to **dry** contact.

## Methods

**MD application (align with VOR).** The study uses **molecular dynamics** in **LAMMPS** with **ReaxFF** on **amorphous** **Na–Si–O** / **silica** **slab** **supercells**; **PBC** in the sliding plane; **NVT**-style **thermostat** and **femtosecond** **timestep**; **ns**-scale **production** windows under shear; **K**-range **temperature** as reported. **N/A — electric field**; **N/A — NPT** **barostat** unless a relax stage uses **NPT**—**N/A** for **GPa** **pressure** if sliding is **NVT**; full tables on **`[[2020hahn-venue-atomistic-understanding]]`**.

## Findings

The narrative on the VOR page ties **dry** sliding to stronger **subsurface** **Si–O–Si** **bridging** across the interface—raising **wear particle** formation and **cohesive** coupling—whereas **interfacial water** can **passivate** or **hydrolyze** bridging pathways, shifting failure toward **near-surface** chemistry and altering **friction** signatures discussed in the paper. The article abstract reproduced in this proof extract attributes severe dry wear to formation of interfacial Si_substrate–O–Si_counter_surface bridges that transmit shear stress into the subsurface, and it states that interfacial water reduces formation of those bridging bonds while leachable sodium ions participate in hydrolytic surface chemistry. Aligned with the **VOR article**, the work argues that **humid** conditions suppress certain **interfacial bridging** interactions that promote **subsurface** mechanical coupling in **dry** wear, while **Na⁺** participates in **hydrolytic** chemistry that reshapes the **glassy** surface. **Quantitative** friction/wear metrics and **snapshots** are cited from the **final** paper, not from this proof duplicate.

## Limitations

When reconciling **simulation** snapshots with **experimental** tribology literature on **glass** wear, remember that **MD** uses **idealized** **crystalline/amorphous** blocks and **high shear rates** compared with **macroscopic** tests; quantitative **wear rates** therefore serve as **trends**, not direct **engineering** predictions, unless validated against the **same** length/time scales. **Proof** PDFs can retain **layout queries** and are **non-authoritative** for pagination. Use **`[[2020hahn-venue-atomistic-understanding]]`** for **bibliography** and **figure** numbers in external manuscripts.

**Confidence rationale:** `med`—duplicate galley; canonical science on sibling page.

## Reader notes (navigation)

- Canonical article: [[2020hahn-venue-atomistic-understanding]]
- [[theme-oxides-silica-ceramics]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2020hahn-venue-atomistic-understanding]]
- [[reaxff-family]]
