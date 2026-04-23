---
id: paper:2025krstic-venue-paper-2
type: paper
title: "Suitability of the ReaxFF potential for MD modeling of lithium across low and high temperatures"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - material:li-metal-anode
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:metallic-systems
doi: ""
year: 2025
authors:
  - "P. S. Krstic"
  - "S. Dwivedi"
  - "A. C. T. van Duin"
  - "B. E. Koel"
venue: "Phys. Chem. Chem. Phys. (in press as of proof; RSC manuscript d5cp03414k)"
pdf_sha256: "c9ada9585ef849745f0a0118a1009d9f1d415555b602e90c7399537e3a9cc4af"
pdf_path: "papers/Krstic_PCCP_Li_2025_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025krstic-venue-paper-2 -->

## Summary

The repository stores a **Royal Society of Chemistry proof PDF** for a forthcoming *Physical Chemistry Chemical Physics* article (manuscript identifier **d5cp03414k** on the proof cover). The archived text extract **`normalized/extracts/2025krstic-venue-paper-2_p1-2.txt`** contains **publisher proof boilerplate** and the **graphical abstract** wording only; it does **not** include the full article **Introduction**, **Methods**, **Results**, or **Discussion** needed for a complete methods-and-findings summary. The graphical abstract states that **modeling lithium’s atomic-scale behavior** is important for **fusion plasma-facing components** and **lithium-ion batteries**, and that doing so **remains challenging across phase regimes**—motivation language that orients the topic but does not specify simulation protocols, training sets, or numerical benchmarks. This wiki page therefore records **corpus provenance** and **retrieval pointers** rather than a substitute for reading the **version-of-record** article once DOI and final PDF are registered.

## Methods

**No reproducible simulation protocol can be extracted** from the current corpus artifacts. The **proof** PDF is intended for layout checking; the extract does not list **ReaxFF** **parameter** files, **QM** **training** data, **ensemble** choices (**NVE** / **NVT** / **NPT**), **time step** (**fs**), **ps** or **ns** **trajectory** **duration**, **supercell** **atom** counts, **PBC** construction, **thermostat** (e.g. **Berendsen**, **Langevin**, **Nosé–Hoover**), **barostat** targets (**GPa**/**bar**), or **LAMMPS**/**software** version—**N/A** for all of the above in this **wiki** until the **version-of-record** is ingested. **N/A** — external **electric field** protocol in the current extract. **N/A** — **replica** **exchange** and **metadynamics**-class **enhanced** **sampling** in the current extract. Operators should attach the **published** *PCCP* PDF and extend **`normalized/extracts/`** for full text. For related **Li** / **ReaxFF** workflows (distinct DOIs), use [[2025krstic-venue-paper]] and [[2023krstic-sputtering-r-paper]] as **context only**—not as documentation of **this** **manuscript**.

## Findings

Beyond the **graphical abstract** headline reproduced in the proof extract, **no quantitative results** (barriers, diffusion coefficients, sputtering yields, equation of state data, etc.) are available from the corpus text. The proof’s purpose is **layout verification**; scientific findings must be taken from the **peer-reviewed article** after publication. When the **version-of-record** appears, expect the usual *PCCP* structure (abstract, introduction, computational and experimental details as applicable, results, conclusions) and update this page with **section locators** and **verbatim** numerical results **only** as supported by that source. **N/A** in this **proof**-only **extract** for **kinetic** **mechanism** and **sensitivity** to **temperature** in any quantitative sense.
## Limitations

This entry is intentionally **thin on science** because the **primary text** is **not** in the extract. Do **not** infer **ReaxFF** performance for **Li** across **temperature** without the article body. **DOI** assignment should follow the **final** Crossref record; manuscript **d5cp03414k** suggests a candidate DOI pattern **10.1039/D5CP03414K**, which must be **verified** on the publisher site. **`keyword:galley-or-proof-pdf`** flags non-VOR PDFs for retrieval hygiene.

## Corpus artifacts

Treat `papers/Krstic_PCCP_Li_2025_galley.pdf` as a **non-VOR** **proof**; prefer the **published** *PCCP* PDF when available.

## Relevance to group

**Van Duin** **ReaxFF** collaboration on **lithium** in **extreme** and **electrochemical** environments; substantive methodology overlaps should be confirmed against the final paper.

## Citations and evidence anchors

RSC manuscript id **d5cp03414k** appears on the proof cover; assign **`doi`** from the **published** article page when available.

## Reader notes (navigation)

- [[reaxff-family]]
- [[2025krstic-venue-paper]] (different DOI and scientific focus—**Li** oxides/hydroxides **hydrogen** irradiation, JCP **2023**)
- [[2023krstic-sputtering-r-paper]] (**LiH** surfaces, **Front. Phys.**)

## Related topics

- [[reaxff-family]]
