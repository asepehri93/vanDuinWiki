---
id: paper:2020muraleedharan-venue-paper
type: paper
title: "Understanding the chemistry of cation leaching in illite/water interfacial system using reactive molecular dynamics simulations and hydrothermal experiments"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2019.12.059"
year: 2020
authors:
  - "Murali Gopal Muraleedharan"
  - "Ryan Herz-Thyhsen"
  - "Janet C. Dewey"
  - "John P. Kaszuba"
  - "Adri C. T. van Duin"
venue: "Acta Materialia (Elsevier PDF proof in corpus)"
pdf_sha256: "a1e3d3ba4cf561113986620bf90c9571f0f85f2c7f465e10dd747d8711e252b8"
pdf_path: "papers/Muraleedharan_ActaMater_2020_Cation_Leaching_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020muraleedharan-venue-paper -->

## Summary

This page tracks the **Elsevier page-proof** PDF at `pdf_path`; for figures, pagination, and the same science with the **version-of-record** file, see **`[[2020muraleedharan-acta-materia-understanding-chemistry]]`**. Prose is grounded in the *Acta Materialia* abstract and the short extract in `normalized/extracts/2020muraleedharan-venue-paper_p1-2.txt`.

**Leaching**—release of **cations** from **minerals** to **fluids**—matters for **energy**, **hydrometallurgy**, **agriculture**, and **clay** geochemistry, yet **molecular pathways** remain debated. The work combines **large-scale ReaxFF MD** with **hydrothermal experiments** on **illite** in **water** to dissect **K⁺**, **Al**, and **Si** release. Simulations show **K⁺** exits **earlier** and at **higher concentration** than **network Al/Si**. **Trajectory analysis** describes **protons** from **water** attacking **non-bridging oxygens** in **Al–O–Si** linkages, forming **[Al–O–Si]–H**-like transition states that evolve toward **silanol** formation upon **Al–O** bond cleavage; **protonation** also weakens **interlayer K–O** bonds, driving **K⁺** toward the surface where **KOH** forms and diffuses outward via **proton exchange**. Continued protonation yields **Al(OH)₃** and **Si(OH)₄**-like species that **release** into solution. The authors compare **MD-derived surface kinetics** to **bulk leaching** curves, finding **orders-of-magnitude** gaps without additional **transport** modeling, and relate **structural distortion** to **>20% cumulative cation loss** thresholds.

## Methods

**1 — MD application (atomistic dynamics).** Protocol numbers follow **`[[2020muraleedharan-acta-materia-understanding-chemistry]]`** and the *Acta Materialia* text: **ReaxFF reactive MD** of **illite** with an **aqueous** **interlayer/interface** (slab + water). Integration uses **0.25 fs** timesteps and a **velocity-Verlet** integrator; the dynamics use **NVT** control with a **Berendsen** thermostat (**0.1 ps** damping) as in the published protocol. The models are **three-dimensional** supercells with **periodic boundary conditions** along in-plane directions for the **clay** slab + water stack (standard slab-style setup; any open-boundary details are in the VOR paper). **N/A —** explicit atom counts, production lengths in **ns**, and the MD **program name** are not taken from the short proof **extract** here; confirm in the VOR **PDF** or the sibling page. **N/A — barostat / external pressure** for the **MD** stages as summarized (constant-volume **NVT** style control). **Electric field: N/A —** not used. **Shear / shock: N/A —** not used. **Replica or enhanced sampling: N/A —** not reported. **Experiments (hydrothermal leaching).** Complementary **batch** **hydrothermal** experiments track **K⁺**, **Al**, and **Si** release in solution versus time for comparison to modeled surface reactivity, as described in the article. **Static QM / DFT: N/A —** not a DFT-benchmarking study. **Force-field training: N/A —** application of an existing **ReaxFF** parameterization, not a new fit in this paper. **Provenance of this file:** this slug tracks the **Elsevier page-proof** PDF at `pdf_path` for **manifest** alignment; for **pagination**, **figures**, and final **tables**, use **`[[2020muraleedharan-acta-materia-understanding-chemistry]]`**.

## Findings

**K⁺** **leaches** faster than **Al/Si** **network** dissolution in the **neutral-water** scenarios highlighted. The **multi-step** **protonation** narrative links **interlayer** **K** mobility to **surface** **KOH** **ejection**, while **Al/Si** release follows **hydroxide** cluster formation. **Surface MD rates** do not **collapse** onto **bulk** kinetics without **transport** or **scaling** arguments. **Structural distortion** diagnostics connect **extensive cation loss** to measurable **illite** **deformation** in the model. **Comparisons:** the authors state **MD-derived surface reactivity** does not match **bulk leaching** kinetics without a **transport** or multi-scale model (**orders of magnitude** gap; see abstract and Discussion on the VOR). **Limitations (as written):** **proof PDF**; prefer **`[[2020muraleedharan-acta-materia-understanding-chemistry]]`** for **VOR** locators. **Open direction:** the abstract frames a need to reconcile **surface** reaction kinetics with **reservoir-scale** leaching.

## Limitations

**Proof PDF** may lack final **pagination**; **clay-edge** chemistry complexity exceeds any single **slab** model; **ReaxFF** **geochemistry** parameters carry **uncertainty**. See **`[[2020muraleedharan-acta-materia-understanding-chemistry]]`** for the **authoritative** article page.

## Relevance to group

**van Duin** (corresponding) with **University of Wyoming** **experimental** partners on **clay–water** **reactive MD**; this slug preserves **hash-level provenance** for the **Elsevier proof** PDF while the **scientific narrative** lives on the **VOR** companion page.

## Reader notes (navigation)

- [[2020muraleedharan-acta-materia-understanding-chemistry]]

## Citations and evidence anchors

- DOI `10.1016/j.actamat.2019.12.059` — proof path `papers/Muraleedharan_ActaMater_2020_Cation_Leaching_proof.pdf`; extract `normalized/extracts/2020muraleedharan-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
