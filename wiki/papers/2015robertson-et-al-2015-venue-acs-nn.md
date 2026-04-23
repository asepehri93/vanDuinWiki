---
id: paper:2015robertson-et-al-2015-venue-acs-nn
type: paper
title: "Atomic structure of graphene subnanometer pores"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - method:semiempirical-tightbinding
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.5b05700"
year: 2015
authors:
  - "Alex W. Robertson"
  - "Gun-Do Lee"
  - "Kuang He"
  - "Chuncheng Gong"
  - "Qu Chen"
  - "Euijoon Yoon"
  - "Angus I. Kirkland"
  - "Jamie H. Warner"
venue: "ACS Nano"
pdf_sha256: "e9167fe36f7bc052ed55aabcb746b88ebfcbb4881e348ac50da4952196275f87"
pdf_path: "papers/Others/robertson-et-al-2015-atomic-structure-of-graphene-subnanometer-pores.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015robertson-et-al-2015-venue-acs-nn -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Nano** (DOI in front matter). This work is **AC-TEM + DFT + supporting tight-binding dynamics**—not a **ReaxFF** study.

## Summary

Sub-nanometer pores in graphene matter for **desalination**, **gas separation**, and **biopolymer translocation**, but their **atomic rim structure** is hard to image before **beam-induced healing** or contamination closes the gap. Robertson *et al.* combine **aberration-corrected TEM** at **80 kV** with **in situ heating (500–800 °C)** to stabilize **open** pores long enough for **picometer-scale** imaging, reporting **non-ideal, disordered** edge configurations rather than pristine **zigzag/armchair** filaments alone. **DFT (VASP, PBE)** relaxes **vacancy** supercells and supports measured **bond lengths**; **tight-binding molecular dynamics** (environment-dependent formulation referenced in the article) explores **ring rearrangement** kinetics along pore edges. Together, the data emphasize **five-membered ring** projections decorating evolving pore perimeters and connect imaging-derived **bond metrics** to relaxed **atomic models**.

## Methods

**Experimental microscopy and sample handling.** **Graphene** is grown by **CVD** on **Cu**, transferred with **PMMA**, and cleaned on **TEM grids** using a **350 °C** bake to remove polymer residues (Methods narrative in the article). **AC-TEM** uses a **JEOL 2200MCO** instrument at **80 kV** with a **monochromator** (energy spread quoted **<300 meV** in the extract) and a **DENS** heating holder. **High temperature (500–800 °C)** suppresses **pore filling** by mobile surface carbon during prolonged imaging. **Flux / dose** estimates and detailed drift/calibration steps are given in **`pdf_path`** and SI.

**Static QM / DFT.** **Functional:** **PBE** **GGA** in **VASP** for **vacancy** and **pore-edge** supercells as described in Methods. **Dispersion:** **vdW** corrections are discussed where **edge adsorbates** matter; the wiki does not assign a universal **DFT-D** label without the SI line—see **`pdf_path`**. **Basis / potentials:** **Plane-wave PAW** expansion at **400 eV** cutoff (article Methods). **k-point / Brillouin sampling:** Γ-centered **(2×2×1) k-mesh** for the **448-atom** graphene supercells summarized on this page. **Structures / properties:** relaxations of **vacancy** and **reconstructed rim** motifs; **multislice image simulation** matched to experimental **intensity profiles** for bond-length extraction (Results).

**Tight-binding MD (supporting kinetics).** **Environment-dependent tight-binding MD** explores **five-membered ring** migration along pore perimeters (code references in the article/SI). **Timestep / duration / thermostat** for TBMD: **not duplicated here**—see **`pdf_path`**.

**MD application (classical ReaxFF/AIMD production):** **N/A** — not a classical reactive MD paper.

**Force-field training:** **N/A**.

## Findings

**Imaging outcomes:** With **heating**, **sub-nm** pores remain **open** long enough for **atomic-resolution** imaging; diameters in one reported range are **~0.5–0.8 nm** alongside **atomic models** in the article’s Figure 1 narrative (extract).

**Edge chemistry and kinetics:** Pores **grow** under the beam by **sequential sputtering**; **undercoordinated** perimeter atoms are removed preferentially, often leaving **five-membered rings** projecting outward. **DFT** + **image simulation** support **reconstructed** **C–C** separations at the rim (e.g., **~169 pm** reconstructed vs **non-reconstructed** contrasts in the Results discussion—exact numbers on `pdf_path`).

**Comparisons / levers:** **Temperature** and **beam exposure** control whether **sub-nm** pores survive versus **self-healing**/**contamination filling**; **80 kV** operation is chosen near the **knock-on** threshold for **sp²** carbon to balance **milling** and **imaging** (Introduction/Results).

## Limitations

The **electron beam** drives chemistry and heating; **PBE** omits some **dispersion** subtleties for certain **edge adsorbate** configurations. **TBMD** approximates **π** electronic structure; highest-accuracy **barriers** may require **DFT NEB** for specific elementary steps. Quantitative **DFT** convergence settings, **TBMD** integration parameters, and figure-level distance metrics should be taken from **`pdf_path`** and SI rather than from this summary alone.

## Relevance to group

**Graphene nanopore** structural science for **separation** and **sensing**—complements **reactive carbon** simulation elsewhere in the corpus but is primarily **microscopy + QM**.

## Citations and evidence anchors

- DOI [10.1021/acsnano.5b05700](https://doi.org/10.1021/acsnano.5b05700).
- `normalized/extracts/2015robertson-et-al-2015-venue-acs-nn_p1-2.txt`.

## MAS / retrieval

Canonical tags emphasize **2D** + **DFT** + **experiment** integration; do **not** add **`method:reaxff`** from this page alone.

## Related topics

- [[graphene-nanocarbon]]
