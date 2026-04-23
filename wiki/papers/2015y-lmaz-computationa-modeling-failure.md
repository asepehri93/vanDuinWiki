---
id: paper:2015y-lmaz-computationa-modeling-failure
type: paper
title: "Modeling failure mechanisms of poly(p-phenylene terephthalamide) fiber using reactive potentials"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - method:reactive-md-generic
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:reactive-md
  - keyword:classical-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2015.07.010"
year: 2015
authors:
  - "Dündar E. Yılmaz"
venue: "Computational Materials Science"
pdf_sha256: "2aec0628127de042fbc55f7a20a4bbc58f81d81b865497d559cbed7b66a238bd"
pdf_path: "papers/ReaxFF_others/1-s2.0-S0927025615004206-main-4.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015y-lmaz-computationa-modeling-failure -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the article identified by `doi` and `pdf_path`. **Reactive potentials** are used as stated in the abstract; confirm **which** **FF** in the **Methods** section of the PDF.

## Summary

**Reactive MD** with **bond-order**-style **potentials** studies **tensile failure** of **PPTA** (**Kevlar-class**) in **amorphous** and **crystalline** morphologies with **vacancy** **defects**. **Modulus** estimates (**~6.7 GPa** **amorphous**; **~350 GPa** **defect-free crystal**) and **defect** sensitivity (**5% N vacancy** drops modulus to **~197 GPa** in the abstract’s example) are combined with **histograms** of **bonds/angles** vs **strain** to localize **failure** at **amide**/**phenyl** **C–N** regions under **extreme** **tension**. The introduction stresses **aramid** use in **ballistic** fabrics where **fiber failure** absorbs **projectile** energy, motivating **atomistic** models that allow **bond breaking** beyond fixed-bond **classical** schemes (introduction, extract).

## Methods

**LAMMPS** runs use the **Strachan et al.** **ReaxFF** set for **PPTA**-relevant **C/H/O/N** (`papers/ReaxFF_others/1-s2.0-S0927025615004206-main-4.pdf`, §2.1–2.3). Models include **amorphous** packings from an **in-house** builder (several molecular weights) and **crystalline PPTA** with **C** or **N vacancies** (§2.2), all in **3D periodic supercells** with explicit **atom** positions for polymer and defects. After **300 → 600 K** over **10 ps**, **10 ps** hold at **600 K**, and cool to **300 K** over **10 ps**, quasi-static **tensile** loading applies **1%** **z**-strain steps with **10 ps** relaxations at **σ_xx = σ_yy = 0** while **L_z** is fixed, to **30%** engineering strain; histograms every **100** MD steps (§2.3). **NVT** with a **Nosé–Hoover**-style thermostat is used (PDF OCR spells “Noose-Hover”). **Timestep:** **N/A —** not recovered unambiguously from the indexed §2.3 text—confirm in the journal PDF. No global barostat; in-plane normal stresses are relaxed to zero by the protocol rather than hydrostatic pressure control. No electric field or enhanced sampling.

**Force-field choice:** **NWChem B3LYP/6-31G** bond stretches for six **PPTA-relevant** motifs are compared to ReaxFF scans to justify using the existing Strachan parametrization (§2.1); the paper does **not** report a new ReaxFF optimization campaign.

**Static QM / DFT:** **NWChem B3LYP/6-31G** scans serve **QA** for the reactive potential, not production AIMD.

## Findings

Tension is borne mainly by **bond stretching** in **amide–phenyl** linkages before **ultimate rupture** localizes at **C–N** under large strain—**mechanistic** localization consistent with reactive bond order (abstract, §3). **Histograms** of bond lengths, angles, and phenyl metrics versus **strain** show where response nonlinearizes (§2.3, §3). The abstract quotes **~6.7 GPa** (amorphous), **~350 GPa** (defect-free crystal), and **~197 GPa** with **5% N vacancies**, plus a **rule-of-mixtures**-style blend for effective “fiber” moduli. **Vacancy type** and **concentration** are the main **sensitivity** levers on stiffness and failure progression. **Limitations**: idealized **bulk-like** cells omit spun-fiber **skin–core** texture noted in the Introduction. **Corpus honesty**: this is an external **Comput. Mater. Sci.** study (not van Duin-group); **comparisons** to experiment are only as far as the article’s abstract and discussion take them—use the **PDF** for numerical tables.

## Limitations

- **Idealized** **microstructures** may omit **spun-fiber** **texture** and **skin-core** gradients.
- **Reactive FF** **quality** depends on the **specific** **parameterization** used (see PDF).

- **Strain-rate** and **system size** in **MD** differ from **fiber** **draw** experiments; treat **modulus** and **failure** trends as **qualitative** indicators unless mapped with **careful** **scaling** analysis (discussion caveat in polymer mechanics literature).

## Relevance to group

**Polymer** **mechanics** with **reactive MD** parallels **group** interests in **large-strain** **failure** of **organic** **solids**.

## Citations and evidence anchors

- **DOI:** `10.1016/j.commatsci.2015.07.010` — `papers/ReaxFF_others/1-s2.0-S0927025615004206-main-4.pdf`.

## Related topics

- [[reaxff-family]]
