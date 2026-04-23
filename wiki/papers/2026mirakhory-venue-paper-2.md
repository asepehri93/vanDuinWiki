---
id: paper:2026mirakhory-venue-paper-2
type: paper
title: "Dynamics of iodine geminate recombination in supercritical xenon solvent: Caging effect (AIP proof PDF)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
source_refs: []
doi: "10.1063/5.0302862"
year: 2026
authors:
  - "M. Mirakhory"
  - "A. Majumdar"
  - "M. Ihme"
  - "A. C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "c3a6aa4df221979a9f416493f3f6253d06814420dca745d03471cd029b0ab190"
pdf_path: "papers/Mirakhory_JCP_2026_Xe_I_II_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2026mirakhory-venue-paper-2 -->

??? info "Why confidence is med"
    The local **extract** is almost entirely AIP proofing instructions and author queries (`normalized/extracts/2026mirakhory-venue-paper-2_p1-2.txt`). Full **Methods** and **Findings** prose is taken from the sibling VOR page [[2026mirakhory-venue-paper]], which reads `papers/Mirakhory_JCP_2026_Xe_I_II.pdf`.

## Summary

This corpus slug registers the AIP **layout proof** PDF `papers/Mirakhory_JCP_2026_Xe_I_II_galley.pdf` for the Journal of Chemical Physics article at DOI `10.1063/5.0302862` on iodine geminate recombination in supercritical xenon studied with ReaxFF molecular dynamics. The automated extract (`normalized/extracts/2026mirakhory-venue-paper-2_p1-2.txt`) is dominated by AIP **eProof** instructions and an **AUTHOR QUERY FORM** for Journal article number JCP25-AR-03845, not the full article narrative. The proof text asks authors to verify title spelling, affiliations, funding, and ORCID entries, and lists numbered queries (for example, clarifying what “following sections” refers to in a sentence about solvent pressure, consolidating duplicate references 23 and 33, supplying a volume number for reference 56, and confirming funder U.S. Department of Energy award DE-SC0022222). Scientific content—including ReaxFF Xe/I parametrization philosophy, large xenon cells, thermostat choices, production segments, and quantitative findings—is curated on [[2026mirakhory-venue-paper]] because that page is tied to the readable article PDF `papers/Mirakhory_JCP_2026_Xe_I_II.pdf`.

## Methods

This **eProof** ingests AIP **author queries** in the local extract, not a clean **Methods** table. The LAMMPS ReaxFF **molecular dynamics** protocol in the paper uses **NVT** at **290 K** (with **2–200 bar**-labeled supercritical state points in fixed-volume **cells** on the order of **~10,000** **atoms** and **0.25 fs** **time step** in the version-of-record narrative), **periodic** **boundaries**, **1 ns** **trajectories**, **multi-thermostat** **Berendsen** coupling, and a **1 ns** **(290** **K**, **58.98** **bar)** equilibration window for the large-cluster and bond-off dissociation experiments described on **[[2026mirakhory-venue-paper]]**—treat that page as the scientific source of truth; **N/A** — this proof PDF is not a substitute. **N/A** — no **NPT** **Parrinello**/**Rahman** (or other) **barostat** in the NVT **production** plan as read from the VOR. **N/A** — no **static electric field**; **N/A** — no **replica**/**metadynamics**/**umbrella** sampling. **2 — Force-field training:** the **ReaxFF** **Xe**/**I** **CASSCF**/**DFT**/**CCSD** training story is on the VOR page; **N/A** to extract protocol from this eProof. **3 — Static QM (standalone):** **N/A.** **4 — Review** — **N/A.**

## Findings

- **I₂** **geminate** **recombination** in **sc** **Xe**—including **caging** (**~2.5×** local **vs** **bulk** **density**), **energy** **transfer** into the **cluster** **coordination** shell, and **pressure**/**concentration** **sensitivity**—is summarized on **[[2026mirakhory-venue-paper]]**; **comparisons** to **low**-**P** and **high**-**P** **limits** are in that note, not the **eProof** file.
- The **AIP eProof** is **corpus** **metadata** (bibliography cleanup, **ORCID** **checks**, duplicate references); it does **not** add **kinetic** **data** to the KB. **Caveat** — **eProof** may **mismatch** **pagination** and **typography** **vs** the VOR; see `## Limitations`.

## Limitations

Proof PDFs can differ in pagination from the published article. This slug duplicates content under a non-VOR file hash; always cite the DOI and prefer the VOR PDF for figures.

## Relevance to group

Co-authored ReaxFF study from the van Duin group on solvent-mediated recombination and energy transfer.

## Reader notes (navigation)

- [[2026mirakhory-venue-paper]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: `10.1063/5.0302862`.
