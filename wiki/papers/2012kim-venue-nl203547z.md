---
id: paper:2012kim-venue-nl203547z
type: paper
title: "Ripping graphene: Preferred directions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/nl203547z"
year: 2012
authors:
  - "Kwanpyo Kim"
  - "Vasilii I. Artyukhov"
  - "William Regan"
  - "Yuanyue Liu"
  - "M. F. Crommie"
  - "Boris I. Yakobson"
  - "A. Zettl"
venue: "Nano Letters 12, 293–297 (2012)"
pdf_sha256: "44c8eb1e14063a13ad905d3dc566b73ed5c0a886569393e9d0be3753b0ee750f"
pdf_path: "papers/ReaxFF_others/Kim_Jacobson_RippingGraphenePreferred_Directions_NanoLetters_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012kim-venue-nl203547z -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Mechanical tears** in **suspended monolayer graphene** are imaged by **TEM** with **crystallographic** indexing via **electron diffraction**. **Torn edges** are predominantly **straight** along **armchair** or **zigzag** directions, with **30°** kinks (and multiples). **Theory** (including **simulations** accounting for **edge electronic** structure) attributes **preferred directions** to a **nonmonotonic** **edge energy** vs **misorientation**—not to generic isotropic fracture. **Electron-beam** irradiation can **propagate** tears rapidly (up to ~**1 µm/s** at low flux in reported conditions) while preserving **crystallographic** alignment. Near **grain boundaries**, tears may **cross** boundaries rather than follow them, informing **failure** of **polycrystalline** graphene.

## Methods

### Experimental microscopy (tearing morphology)

**Sample fabrication:** **Monolayer graphene** grown by **CVD** on **polycrystalline Cu**, transferred to **TEM** grids, and imaged as **suspended** membranes (Supporting Information referenced for preparation details).

**Mechanical tearing:** tears arise from **mechanical stress** during transfer and wet etching/drying; edges are tracked in **TEM** images.

**Crystallographic assignment:** **Electron diffraction** near tear regions (rotation-calibrated patterns) assigns **armchair** vs **zigzag** registry for straight tear segments.

**Electron-beam-driven propagation:** the study documents **TEM** **e-beam** stimulation of tear growth at **100 keV** imaging conditions, with reported propagation speeds up to **~1 µm/s** at low dosages (**~0.01 A/cm²**), while noting a **~86 keV** knock-on threshold context for pristine graphene.

### Static QM / DFT and atomistic theory (preferred directions)

**Functional:** **N/A —** specific **DFT** exchange–correlation functional not recovered from `normalized/extracts/2012kim-venue-nl203547z_p1-2.txt`; verify **`pdf_path`**.

**Dispersion:** **N/A —** **vdW** / **DFT-D** treatment not recovered from the indexed excerpt; verify **`pdf_path`**.

**Basis set:** **N/A —** localized or plane-wave **basis set** choices for the graphene edge electronic-structure models are not recovered from the indexed excerpt; verify **`pdf_path`**.

**k-sampling:** **N/A —** k-point / k-mesh sampling for periodic edge models is not recovered from the indexed excerpt; verify **`pdf_path`**.

**Structures / pathways:** **TEM**-resolved tear geometries (straight segments, **30°** kinks, behavior near **grain boundaries**) supply the structural constraints compared against theory; atomistic models in the paper treat **graphene edge** energetics and tearing direction preferences (see **`pdf_path`** for full model hierarchy).

**Properties computed:** **Edge energies** as a function of **misorientation** (nonmonotonic dependence invoked in the abstract to rationalize preferred tearing directions), plus comparisons to the **experimental** tearing catalog.

### MD application (atomistic dynamics)

**N/A —** this work’s primary evidence is **TEM** plus **electronic-structure / atomistic theory**; any cited **molecular dynamics** literature appears as background in the introduction rather than as new production **MD** in this article (see **`pdf_path`**).

## Findings

**Outcomes / mechanisms:** **Mechanically induced** tears in **suspended monolayer graphene** produce **straight** edges over long distances, predominantly aligned along **armchair** or **zigzag** directions, with **30°** (or multiple-of-**30°**) kinks consistent with **hexagonal** symmetry. **Electron-beam**-stimulated tear growth can propagate quickly—up to **~1 µm/s** at low reported flux (**~0.01 A/cm²**)—while preserving registry; imaging uses **100 keV** electrons with discussion of **knock-on** thresholds near **~86 keV** for pristine graphene.

**Comparisons:** **Theoretical simulations** that include **edge electronic structure** are reported to reproduce the observed **preferred armchair/zigzag tearing** and occasional kinks, linking morphology to **nonmonotonic edge energy vs misorientation** rather than isotropic fracture alone.

**Sensitivity / design levers:** **Electron dose** and **accelerating voltage** influence whether tears propagate under irradiation; **crystallographic orientation** (from diffraction) is the primary structural lever discussed for tear alignment.

**Limitations / outlook (as authored tone in abstract/intro):** **TEM** imaging couples **mechanics** with **irradiation** effects; separating intrinsic mechanical tearing from **e-beam** chemistry requires care (see discussion in **`pdf_path`**).

**Corpus / KB honesty:** This page is grounded in **`pdf_path`** and `normalized/extracts/2012kim-venue-nl203547z_p1-2.txt` (pages **1–2** of the extract); quantitative **DFT** settings, additional statistics, and figures should be taken from the **peer-reviewed PDF** / **Supporting Information**, not inferred here.

For readers comparing to **simulated tearing**, the paper’s lesson is that **crystallographic registry** matters alongside **stress distribution**: tears **route** along directions consistent with **anisotropic edge energetics** rather than arbitrary **Griffith** paths.

## Limitations

- **TEM** **e-beam** can **drive** chemistry and **cutting**; separating **pure mechanics** from **radiolysis** requires care.
- **Suspended** samples differ from **substrate-supported** tearing in devices.

## Relevance to group

Complements **ReaxFF tearing** studies (e.g., **Huang et al., PRB 2012**) with **experimental** **crystallographic** tearing data and **continuum/DFT** edge energetics.

## Citations and evidence anchors

- DOI: [10.1021/nl203547z](https://doi.org/10.1021/nl203547z)
- Text-aligned pointer: `normalized/extracts/2012kim-venue-nl203547z_p1-2.txt`

## Related topics

- [[graphene-nanocarbon]]
- [[2011huang-venue-paper]]
- Graphene fracture and edge anisotropy
