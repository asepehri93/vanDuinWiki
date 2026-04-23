---
id: paper:2021hosseinizadeh-nat-few-fs-resolution
type: paper
title: "Few-fs resolution of a photoactive protein traversing a conical intersection"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41586-021-04050-9"
year: 2021
authors:
  - "A. Hosseinizadeh"
  - "N. Breckwoldt"
  - "R. Fung"
  - "R. Sepehr"
  - "M. Schmidt"
  - "P. Schwander"
  - "R. Santra"
  - "A. Ourmazd"
venue: "Nature"
pdf_sha256: "bcb3dc872877dc782e2c66d7a76a02b4f36d20d6c67a7f4630540349c55d2222"
pdf_path: "papers/Others/Hosseinizadeh_et_al-2021-Nature.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021hosseinizadeh-nat-few-fs-resolution -->

## Summary

Hosseinizadeh *et al.* use **serial femtosecond X-ray crystallography** and **machine-learning–assisted** reconstruction to obtain **time-resolved structural** information on **photoactive yellow protein** (PYP) as it **evolves** through a **conical intersection** after **photoexcitation** (*Nature* **598**, 2021; DOI 10.1038/s41586-021-04050-9). The advance is **experimental**: sub-**100 fs** time steps and **near-atomic** spatial resolution for a **thousands-of-atoms** **protein** system, mapping **nuclear** motion to **nonadiabatic** **return** at a **conical** **seam**—peripheral to standard **ReaxFF** (ground-state reactive MD) workflows in this knowledge base but relevant as a **resolution** benchmark for **ultrafast** structure.

## Methods

**Literature scope and protocol (non-MD, non-DFT production in the vanDuinWiki sense).** The *Nature* workflow combines serial femtosecond X-ray crystallography with data-driven reconstruction to extract ultrafast structural trajectories of photoactive yellow protein after optical excitation. In practical terms, the protocol depends on high-temporal-resolution pump-probe timing, careful handling of diffraction snapshots that are sparse/noisy at each delay point, and a machine-learning-assisted inversion/reconstruction layer that turns those snapshots into time-ordered structural coordinates.

The article then interprets those reconstructed geometries with conical-intersection concepts (seam crossing, branching-space-relevant motions) to connect structural evolution with nonadiabatic relaxation. This is why the paper is methodologically important even for a mostly ReaxFF-focused corpus: it provides an experimentally anchored map of ultrafast structural change at a resolution class that many simulation workflows use as an aspirational benchmark.

Blueprint mapping for this wiki:
- MD application block: N/A (no classical production MD protocol reported as the study core).
- Force-field training block: N/A.
- Static QM-only block: partial/interpretive only; the main contribution is experimental reconstruction and analysis rather than a standalone DFT campaign.
- Review/non-simulation framing: applicable; methods should be read directly from the *Nature* Methods + Extended Data sections for full instrument and reconstruction specifics.

**Molecular dynamics / ReaxFF:** **N/A** — not the subject of this publication.

**Force-field training / ReaxFF:** **N/A**.

**Static QM in silico for production MD:** **N/A**; **QM**-level *interpretation* of **photophysics** may be cited in *Nature* in relation to **electronic** structure, but the **contribution** here is **structural** **dynamics** from **experiment** + **reconstruction**.

## Findings

**Outcomes & mechanisms (authored):** The central claim is that the photoactive protein trajectory can be followed with few-fs temporal granularity through the region associated with a conical intersection, giving experimentally informed access to nuclear motions tied to ultrafast internal conversion. The paper frames this as direct structural evidence for dynamics that are often inferred indirectly.

**Comparisons & sensitivity:** The reconstruction is evaluated across time slices and structural coordinates rather than through force-field benchmarking. Sensitivity is therefore tied to data quality, inversion choices, and interpretation of trajectory features in the conical-intersection framework, not to a classical-potential hyperparameter scan.

**Design relevance for this KB:** Even though this is not a ReaxFF paper, it anchors a useful cross-domain message: experimental ultrafast structural datasets can constrain or challenge simulation narratives about excited-state relaxation pathways. In that sense, it is a benchmark-style reference for what "resolved dynamics" can look like when instrumentation and analysis pipelines are pushed aggressively.

**Limitations & outlook (as authored):** Reconstruction quality is model- and data-dependent; uncertainty handling, inversion assumptions, and derived coordinate interpretation remain important caveats. The article's own discussion and Extended Data should be treated as the authority for quantitative confidence intervals and edge cases.

**Corpus / KB honesty:** vanDuinWiki is **ReaxFF**-centric; links from **PYP** work to **[[reaxff-family]]** are **thematic** only unless the reader adds **nonadiabatic** **/ excited-state** **simulation** (surface hopping, TD-DFT MD, *etc.*) consistent with the **phenomenon**. **Definitive** **numbers** from **`pdf_path`** and publisher **ED**.

## Limitations

The wiki page is intentionally high-level and does not substitute for the full *Nature* Methods, Extended Data, and supplemental protocol details (timing calibration, reconstruction settings, and uncertainty analysis). Readers needing exact numerical settings or reproducibility specifics should use the version-of-record publication directly.

Scope limitation for vanDuinWiki users: this entry is adjacent to, not inside, the core ReaxFF workflow family. It should not be cited as evidence for classical force-field parametrization quality, but it can be cited as an experimental reference point for ultrafast structural dynamics and conical-intersection interpretation.

## Relevance to group

Peripheral: experimental and ML-inversion limits on large-molecule **nonadiabatic** **dynamics**, **complementary** to **simulation**-centered **corpus** entries.

## Citations and evidence anchors

*Nature* **598** (2021), DOI [10.1038/s41586-021-04050-9](https://doi.org/10.1038/s41586-021-04050-9) — main text, figures, **Extended Data**.

## Related topics

- [[reaxff-family]]
