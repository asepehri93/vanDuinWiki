---
id: paper:2018jonayat-venue-rsc-cp
type: paper
title: "A first-principles study of stability of surface confined mixed metal oxides with a corundum structure (Fe2O3, Cr2O3, V2O3)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:oxides-ceramics
  - material:oxide
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:oxide-surface
  - keyword:catalysis-surface
source_refs: []
doi: "10.1039/C8CP00154E"
year: 2018
authors:
  - "A. S. M. Jonayat"
  - "Alan Kramer"
  - "Luca Bignardi"
  - "Paolo Lacovig"
  - "Silvano Lizzit"
  - "Adri C. T. van Duin"
  - "Matthias Batzill"
  - "Michael J. Janik"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "45dffebb6a2b4e1ce48bfe6cb9ecef5336866a14006f717dd9fb441c74d3bf9f"
pdf_path: "papers/Jonayat_PCCP_2018_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018jonayat-venue-rsc-cp -->

## Summary

This **PCCP** study uses **first-principles (DFT)** methods to examine **stability** of **surface-confined mixed oxides** with **corundum-related** structure, focusing on **Fe₂O₃**, **Cr₂O₃**, and **V₂O₃** combinations as **ultrathin films** on a **support** (details in the article). The motivation is that **two-dimensional / surface-confined oxides** can have **chemistry** distinct from bulk-like oxides—relevant to **catalysis** and **surface science** where termination, epitaxial strain, and lateral confinement shift oxide stoichiometry. **Adri C. T. van Duin** is included among coauthors, connecting the work to the group’s broader **oxide interface** interests even though the primary engine here is **DFT**, not **ReaxFF MD**. The ingested file is an **RSC galley/proof** (`c8cp00154e` header). **Surface alloys** and **mixed terminations** are evaluated to show how **local composition** on the **support** can stabilize motifs that would be high-energy in **bulk** **corundum** analogues.

## Methods

- **DFT total-energy** workflows on **surface-confined** **Fe₂O₃**, **Cr₂O₃**, and **V₂O₃** (and mixed) **corundum-structure** films on a **support**, comparing **candidate terminations** and **configurations** (see **Computational Details** and ESI in the version-of-record), including relaxation protocols that map relative energies of mixed versus endmember terminations.
- **Electronic structure:** **DOS**-style analyses in the article connect **stability** trends to **d-band** features where reported.

**Static QM details (version-of-record alignment).** This corpus slug points to an **RSC galley/proof** PDF for the same **PCCP** work as **[[2018jonayat-physical-che-first-principles-study]]** (DOI **10.1039/c8cp00154e**). **Functional:** **PBE** + **Hubbard U** on **Fe**, **Cr**, **V** **3d** states as in the published **Computational Details**. **Basis / code:** **plane-wave** **PAW** **DFT** (VASP-style workflow per article). **k-point sampling:** **Monkhorst–Pack** **k-point** meshes for **slabs** and bulk references. **Structures:** relaxed **corundum** **(0001)** **surface-confined** films and **Fe**-doped **V\(_2\)O\(_3\)** terminations. **Dispersion:** **N/A — explicit DFT-D** correction not summarized here; confirm in the **VOR** **PDF** if applicable. **Pathways:** **N/A — NEB** not the headline method—**surface energies** and **μ\(_O\)** diagrams drive the conclusions.

## Findings

**Outcomes.** **Mixed** **M\(_x\)O\(_y\)** terminations on the **support** can be **thermodynamically** preferred over **bulk-like** **corundum** fragments, shifting **oxidation**/**reduction** motifs at the **interface**.

**Comparisons.** **Experimental** **surface-science** signatures in the article **benchmark** the **DFT** **phase** boundaries for **termination** and **reduction**.

**Sensitivity.** **Oxygen chemical potential** (linked to **T** and **p\(_{\mathrm{O_2}}\)** via the article’s conventions) and **Fe** doping level move predicted **segregation** and **termination** stability.

**Corpus honesty.** Prefer **[[2018jonayat-physical-che-first-principles-study]]** for **VOR** **pagination**; this **galley** `pdf_path` may differ in **page** numbers—cross-check figures before citing locators.
## Limitations

- **DFT functional** and **hubbard / dispersion** choices affect **oxide energetics**; check sensitivity for **quantitative** comparisons.
- **Proof PDF** may differ slightly from the **final typeset** version in **pagination** or minor **typography**.

## Relevance to group

**van Duin** coauthorship on a **DFT-forward oxide stability** paper adjacent to **reactive FF** development for **similar chemistries**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/C8CP00154E` (manuscript id **C8CP00154E** on the proof header; confirm against your library resolver if needed).

## Reader notes (navigation)

- **DFT** oxide stability (not ReaxFF); adjacent catalysis and oxide hub: [[theme-oxides-silica-ceramics]]. Corpus PDF is an **RSC proof**—confirm pagination against the published issue; galley/proof guidance: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section D.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
