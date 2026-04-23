---
id: paper:2017wen-venue-research
type: paper
title: "Surface Orientation and Temperature Effects on the Interaction of Silicon with Water (galley PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:water-interfaces
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b11310"
year: 2017
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Xinchun Lu"
venue: "The Journal of Physical Chemistry A (2017)"
pdf_sha256: "69410ed54bbdc68d27fdbbca466733608916844b0d9b95677cf7d1fddbc72af5"
pdf_path: "papers/Wen_Silicon_water_JPC_2017_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017wen-venue-research -->

## Summary

This wiki page tracks a **galley / proof-style** PDF for the Journal of Physical Chemistry A article on ReaxFF molecular dynamics of water interacting with crystalline silicon surfaces (**DOI `10.1021/acs.jpca.6b11310`**). Galley files can differ from the version of record in pagination, figure quality, and minor copy edits; for stable section locators and final figures, use **`[[2017wen-venue-jp6b11310]]`**, which points to the non-galley article PDF in this corpus. Scientifically, the study compares water interaction with Si(100), Si(110), and Si(111) at 300 K and 500 K, addressing molecular versus dissociative adsorption, hydrogen versus hydroxyl termination patterns, and oxidation reactions relevant to wet oxidation, chemical mechanical polishing, and MEMS processing. The work is a foundational silicon–water ReaxFF reference with van Duin co-authorship and links forward to CMP-focused simulations on related chemistries. Facet-dependent reactivity is a recurring theme in semiconductor aqueous processing; this article supplies orientation-resolved baseline chemistry before abrasive particles enter the model.

## Methods

**Molecular dynamics (reactive).** This ingest (`papers/Wen_Silicon_water_JPC_2017_galley.pdf`) is a **galley / proof** duplicate of the same **J. Phys. Chem. A** study as **`[[2017wen-venue-jp6b11310]]`**: **ReaxFF molecular dynamics** exposes **Si(100), (110), and (111)** slabs to explicit **water** films at **300 K** and **500 K** inside **periodic** supercells so **adsorption**, **dissociation**, and **oxidation** can be facet-resolved. **Atom** counts, slab thicknesses, **timestep** (fs), **thermostat**/**barostat** settings, **NVT**/**NPT** labels, and **equilibration**/**production** **duration** (ps/ns) match the **version-of-record** article and must be copied from the canonical **PDF** rather than this **galley** pagination.

**Force-field fitting.** **N/A —** identical published **Si/O/H ReaxFF** consumption as the canonical page; no new fit is reported here.

**Static QM / DFT.** **N/A —** production trajectories are ReaxFF **MD**; literature **DFT** is cited only for qualitative context in the article.

**Review scope.** **N/A —** duplicate **PDF** artifact; prefer **`[[2017wen-venue-jp6b11310]]`** for stable figure numbering.

## Findings

**Outcomes and mechanisms.** **Molecular water** dominates on **(100)/(110)** facets, while **dissociative adsorption** dominates on **(111)**; **Si(100)** trends **H-rich**, **Si(111)** **OH-rich**, and **hydroxyl insertion** builds **Si–O–Si** **oxidation** products. **Temperature** ramps from **300 K** to **500 K** increase dissociation and **oxidation** across facets, as summarized in the abstract shared with the VOR file.

**Comparisons.** The article relates simulated terminations to **experimental** surface probes cited internally; quantitative RDFs or population plots should be read from **`[[2017wen-venue-jp6b11310]]`**, not inferred from this **galley** **PDF** alone.

**Sensitivity / design levers.** **Facet** choice and **thermal** setpoint are the explicit comparative axes controlling **coverage** of **H**, **OH**, and molecular **H₂O**.

**Limitations / outlook.** **Galley** formatting may differ from the final XML layout; rare reactive events may be undersampled in finite-length **MD**.

**Corpus honesty.** This slug exists for manifest fidelity to alternate bytes; scientific locators should cite **`[[2017wen-venue-jp6b11310]]`** unless you deliberately need the **duplicate PDF** note.

## Limitations

Proof PDFs may not match final journal formatting. Finite simulation cells and nanosecond-scale trajectories limit sampling of rare reactive events; ReaxFF parameters inherit training-set biases.

## Relevance to group

Duplicate ingest path for a core van Duin-group silicon–water ReaxFF study; **`[[2017wen-venue-jp6b11310]]`** is the reader-facing primary entry.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.6b11310](https://doi.org/10.1021/acs.jpca.6b11310) — galley: `papers/Wen_Silicon_water_JPC_2017_galley.pdf`.

## Reader notes (navigation)

- **Canonical article page:** [[2017wen-venue-jp6b11310]] (`papers/Wen_Silicon_water_JPC_2017.pdf`).

## Related topics

- [[2017wen-venue-jp6b11310]]
- [[reaxff-family]]
