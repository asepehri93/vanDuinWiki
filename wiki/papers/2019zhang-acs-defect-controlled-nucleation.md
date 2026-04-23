---
id: paper:2019zhang-acs-defect-controlled-nucleation
type: paper
title: "Defect-Controlled Nucleation and Orientation of WSe2 on hBN: A Route to Single-Crystal Epitaxial Monolayers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - material:hexagonal-boron-nitride
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.8b09230"
year: 2019
authors:
  - "Zhang, Xiaotian"
  - "Zhang, Fu"
  - "Wang, Yuanxi"
  - "Schulman, Daniel S."
  - "Zhang, Tianyi"
  - "Bansal, Anushka"
  - "Alem, Nasim"
  - "Das, Saptarshi"
  - "Crespi, Vincent H."
  - "Terrones, Mauricio"
  - "Redwing, Joan M."
venue: "ACS Nano"
pdf_sha256: "1601271aa4eb87997dd241d33e207858d8e701f1f6d0266e49aefe36dbc39cff"
pdf_path: "papers/Others/Zhang_Zhang_Wang_BN_WSe2_acsnano_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019zhang-acs-defect-controlled-nucleation -->

!!! abstract "Scope"

Experimental epitaxy of monolayer WSe₂ on hexagonal boron nitride with high in-plane orientation yield, supported by first-principles modeling and microscopy, linking hBN defects to nucleation preference.

## Summary

The work reports a chemical vapor deposition route in which tungsten diselenide islands nucleate and grow epitaxially on hexagonal boron nitride with preferred orientation exceeding roughly ninety percent, reducing inversion domain boundary density upon coalescence relative to growth on sapphire under comparable conditions. Complementary transmission electron microscopy, optical probes, and device measurements support a mechanism in which hBN surface defects—not only bulk thermodynamics—control nucleation density and orientation. First-principles calculations and growth-condition studies align with single-atom vacancy motifs on hBN trapping tungsten and lowering the formation energy for a dominant rotational domain.

## Methods

Monolayer WSe₂ was grown on hBN using powder-vapor-transport–style chemical vapor deposition with systematic variation of growth conditions and substrate pretreatment designed to tune defect populations on hBN. Transmission electron microscopy characterized domain orientation and boundary content; low-temperature photoluminescence and back-gated field-effect transistor measurements compared films on hBN versus sapphire. **Static QM / DFT (defect energetics).** The article uses **first-principles** **DFT** calculations to compare **defect**-related **nucleation** **formation** **energies**/**binding** **energies** and **in-plane** **orientation** **preferences** for **W**/**Se** on **hBN** **defects**; **N/A** on this page for the full **VASP**/**QE** **input** deck—copy **functional** (**PBE**/**GGA** or as stated), **dispersion** (**van der Waals**/**DFT-D3** if used), **PAW**/**plane-wave** **cutoffs** (**basis**), and **Monkhorst**–**Pack** **k**-**point** **meshes** (or **Γ**-**only** if used) for **Brillouin** **sampling**, plus **relaxed** **geometries**/**reaction** **pathway**-style **local** **minima** from the *ACS Nano* **Methods**/**SI**. **Properties** **computed** include **energy** **differences** and **trends** in **favor** of a **dominant** **rotational** **domain**; **N/A** for **NEB** **curves** unless the **SI** **states** so. **Replica / metadynamics / umbrella:** **N/A** for the **defect** **NEB** **sweep** in the **abstract**-level **summary** if the **manuscript** is **defect** **stability**-centric without **rare-event** **method** **names**.

## Findings

The study reports strongly preferred WSe₂ orientation on hBN (stated as over ninety-five percent in the abstract) and a reduced density of inversion domain boundaries after island coalescence compared to sapphire-grown films under similar conditions. Optical and transport characterization indicate improved properties on hBN relative to sapphire for the compared growth windows. The combined microscopy, growth, and modeling evidence supports defect-assisted nucleation on hBN—particularly single-atom vacancies that localize tungsten and break in-plane symmetry—rather than orientation selection dominated by equilibrium thermodynamics alone. Fully coalesced monolayer films on hBN are demonstrated with processing choices that emphasize controlled nucleation and extended lateral growth time.

## Limitations

The page summarizes claims at the level of the article abstract and introduction; quantitative growth-parameter tables, full DFT setup details, and statistical distributions of domain orientation should be taken from the primary PDF and supporting information when needed for retrieval.

## Relevance to group

Connects two-dimensional synthesis and defect engineering themes relevant to heterostructure modeling and interface-controlled growth discussed elsewhere in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1021/acsnano.8b09230

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
