---
id: paper:2025jiwoo-choi-inorg-chem-0-copper-selenides
type: paper
title: "Copper Selenides via Anion Exchange versus Direct Growth – The Role of Diorganyl Diselenides"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:dft-static
  - keyword:qm-training-data
doi: "10.1021/acs.inorgchem.5c04328"
year: 2025
authors:
  - "Jiwoo Choi"
  - "Benjamin A. Schmidt"
  - "Mykhailo Boleychuk"
  - "Kiran Bedi"
  - "Emily Sandoval-Arteaga"
  - "Kezia N. Almonte"
  - "Quentin M. Boussard"
  - "J. Kenneth Krebs"
  - "Malgorzata Kowalik"
  - "Adri van Duin"
  - "Katherine E. Plass"
venue: "Inorg. Chem. (2025)"
pdf_sha256: "3bdd703182e9a987646391413ec295a212c9b9e8003124dd1a6fc942d1f37502"
pdf_path: "papers/Choi_Kowalik_Plass_Organic_selenide_InorgChem_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025jiwoo-choi-inorg-chem-0-copper-selenides -->

## Summary

Postsynthetic anion exchange is a versatile way to transform nanoparticle composition and can reach nanostructures that are difficult to access by direct growth alone. Earlier work implicated long-chain dialkyl diselenides in driving Se\(^{2-}\) exchange on Cu\(_{2-x}\)S, but mechanistic detail was sparse. Choi et al. systematically compare diphenyl, didodecyl, and dibenzyl diselenides as drivers of selenium anion exchange that creates metastable copper sulfur–selenide alloys, and they contrast those reactivity trends with direct synthesis of copper selenide nanoparticles. Dialkyl diselenides are the only precursors in this study that induce anion exchange. Thermal decomposition measurements are paired with ReaxFF molecular dynamics trained against DFT data for organoselenium bond cleavage and hydrogen selenide elimination, illustrating how inexpensive atomistic screening can rationalize precursor choice before exhaustive laboratory iteration.

## Methods

Experiments compare three commercially available diselenides with distinct relative C–Se bond strengths yet safer handling than strongly malodorous alternatives, enabling direct comparison with prior literature on phase-selective metal chalcogenide growth (`papers/Choi_Kowalik_Plass_Organic_selenide_InorgChem_2025.pdf`). Thermal analyses map fragmentation temperatures and decomposition channels feeding the mechanistic discussion in the main text. ReaxFF trajectories use the DFT-fitted parameter set documented in the article to survey H\(_2\)Se release pathways and intermediate geometries on copper chalcogenide models, emphasizing why dialkyl precursors can populate exchange-compatible elimination coordinates while other diselenides favor direct condensation routes toward selenide phases. **Force-field training** is summarized in the article: **DFT** (and related **QM**) **reference** data, **training** **reaction** and **conformer** **targets**, and **optimization** of **ReaxFF** **parameters** to match those references—see the **Inorg. Chem.** text for program, **basis** **set**, and **weighting** detail. **Reactive** **Molecular** **dynamics** **production** (typically **LAMMPS**-class engines in this group’s workflow; confirm software string in the **article**). **N/A** in this **summary** for **hydrostatic** **NPT** **barostat** and **GPa**/**bar** **pressure** targets in the **gas**-**phase** **ReaxFF** **screens** (often **NVT**-like or **NVE** **segment**s); see **PCCP**/**SI**-level **pressure** if reported. For **MD** **application**: **N/A** on this page for **time step**, **NVE**/**NVT** label, **ns**-scale **trajectory** length, and **thermostat**/**barostat** settings (confirm in **PDF**/**SI**); **PBC** **periodic** **supercells** for **copper** **chalcogenide** **slab**/**cluster** **models** as in the **Inorg. Chem.** **simulation** section. **N/A** — external **electric field**; **N/A** — **replica** **exchange** / **metadynamics** in the sense of rare-event **enhanced sampling** (not stated for these screening runs).

## Findings

The abstract frames mechanistic orthogonality between anion exchange and direct growth toward metastable copper chalcogenide compositions. Dialkyl diselenides uniquely promote exchange on Cu\(_x\)S because they release H\(_2\)Se, which the authors argue is critical for delivering Se\(^{2-}\) into the particle; other diselenides examined here steer chemistry toward direct growth channels without comparable exchange. ReaxFF results support the H\(_2\)Se-mediated picture by resolving low-lying elimination coordinates whose ordering matches experimental precursor rankings. The authors position ReaxFF as a practical design tool for diorganyl diselenide precursors in nanoparticle synthesis, including identification of dialkyl diselenides as a new class of selenium exchange reagents informed by initial H\(_2\)Se-release screening. **Comparisons** in the main text and **SI** to **DFT** and **experiment** should be cited from the **PDF** for **exact** **barriers** and **TGA** traces.

## Limitations

Copy quantitative barrier heights, decomposition temperatures, particle sizes, ligand environments, and Supporting Information tables from the peer-reviewed PDF; this summary does not duplicate those datasets.

## Relevance to group

**Van Duin** / **Kowalik**-linked **ReaxFF** for **nanoparticle synthesis** mechanisms complements **chalcogenide** materials work in the corpus.

## Citations and evidence anchors

https://doi.org/10.1021/acs.inorgchem.5c04328 — *Inorg. Chem.* (2025).

## Reader notes (navigation)

- [[reaxff-family]]
- Cross-link to other chalcogenide anion-exchange papers in the corpus when building comparative synthesis bibliographies.

## Related topics

- [[reaxff-family]]
