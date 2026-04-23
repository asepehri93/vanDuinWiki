---
id: paper:2013meng-venue-paper
type: paper
title: "Defect healing of chemical vapor deposition graphene growth by metal substrate step"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - method:classical-md
  - material:graphene-carbon-nano
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:classical-ff
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:metallic-systems
  - keyword:catalysis-surface
source_refs: []
doi: "10.1021/jp312802e"
year: 2013
authors:
  - "Lijuan Meng"
  - "Zilu Wang"
  - "Jian Jiang"
  - "Yonghong Yang"
  - "Jinlan Wang"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "409e2812e1f3bed3782331d7cfe520c6e7df22ec96370f26a0d0530cfc3c55ab"
pdf_path: "papers/Others/Meng_JPCC_DefectHealing_CVD.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2013meng-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. The corpus extract is **“Just Accepted”** text with partial OCR noise.

## Summary

This Journal of Physical Chemistry C article investigates how carbon structures evolve during graphene nucleation on nickel surfaces, with explicit attention to the role of substrate steps versus flat terraces. The work combines classical molecular dynamics with density functional theory calculations to compare kinetic pathways when carbon species interact with stepped Ni surfaces and with terrace regions. A central distinction in the abstract is between cases where no substrate nickel atom is removed and cases where defects involve nickel atoms that have been pulled out of the surface. In the latter situation, the manuscript reports that step sites assist efficient healing of the associated carbon-related defects, whereas comparable healing is comparatively difficult on terraces alone. The authors attribute this contrast to a substantially lower healing barrier at steps for defects tied to pulled-out nickel, and they interpret the result as evidence that steps can be beneficial for synthesizing higher-quality graphene in chemical vapor deposition on nickel.

## Methods

The peer-reviewed study uses **classical molecular dynamics** to follow **carbon structure evolution** and **graphene nucleation** on **nickel**, with complementary **density functional theory** calculations as stated in the **Just Accepted** abstract (`papers/Others/Meng_JPCC_DefectHealing_CVD.pdf`; `normalized/extracts/2013meng-venue-paper_p1-2.txt`). The modeling contrasts **step** surfaces with **flat terrace** regions, including scenarios with defects tied to a **pulled-out** surface **Ni** atom.

**1 — MD application (numerical protocol):** **N/A —** the corpus extract is **abstract-only**; do **not** infer **LAMMPS**/**GROMACS**-class **engine**, **supercell** **atom** counts, **periodic** boundaries, **NVE**/**NVT**/**NPT** **ensemble**, **fs** **timestep**, **picosecond**/**nanosecond** **duration**, **thermostat**, **barostat**, **temperature**/**pressure** schedules, **electric fields**, or **enhanced sampling** from this wiki page—read the **version-of-record** **J. Phys. Chem. C** article (**DOI `10.1021/jp312802e`**) for the full **MD** protocol.

**2 — Force-field training:** **N/A —** not a reactive force-field parameterization paper.

**3 — Static QM / DFT:** **DFT** is reported as complementary to **MD** for the same **Ni surface / carbon** problem; **functional**, **basis**, **k-sampling**, and **structures/pathways** belong in the article’s **Methods** section, not in this abstract-limited note.

## Findings

When no nickel atom is pulled out of the surface, the abstract states that the evolution mechanism for carbon structures on the step surface matches that on the flat terrace. When defects involve pulled-out nickel atoms, by contrast, those defects can be healed efficiently with assistance from step atoms, while healing is comparatively difficult on the terrace. Relative to the terrace, the step is reported to lower the healing barrier for the defect class associated with the pulled-out nickel atom, leading to comparatively fast healing. The authors summarize these observations as demonstrating that the presence of steps can help synthesize better graphene for CVD growth on a nickel substrate, at least in the defect channels emphasized in their abstract-level description.

**Corpus honesty:** Because the available corpus extract is essentially the **Just Accepted** **abstract**, this wiki page does **not** restate **barrier heights**, **reaction coordinates**, or **convergence** details that appear only in the full **PDF**. Treat the **step vs terrace** distinction and the **pulled-out Ni** defect class as **abstract-level** claims; consult **`papers/Others/Meng_JPCC_DefectHealing_CVD.pdf`** for figures and quantitative **MD/DFT** comparisons.

## Limitations

Classical FF may miss some electronic effects at the metal–graphene interface; “Just Accepted” text may differ slightly from the final layout.

## Citations and evidence anchors

- DOI: [10.1021/jp312802e](https://doi.org/10.1021/jp312802e)

## Reader notes (navigation)

- CVD graphene growth: [[graphene-nanocarbon]], [[theme-2d-epitaxy-growth]]; DFT + classical MD (not ReaxFF).

## Related topics

- [[graphene-nanocarbon]]
