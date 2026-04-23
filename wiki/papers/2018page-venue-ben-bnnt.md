---
id: paper:2018page-venue-ben-bnnt
type: paper
title: 'Supporting Information: Boron Nitride Nucleation Mechanism during Chemical
  Vapour Deposition'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:reactive-md
- material:hexagonal-boron-nitride
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:supporting-information
- keyword:reaxff-application
- keyword:2d-materials
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b05785
year: 2018
authors:
- Ben McLean
- Grant B. Webber
- Alister J. Page
venue: J. Phys. Chem. C (Supporting Information)
pdf_sha256: bb7d536cb81880c6d2b4faba57f64fc27225a7806f4e1b04be762ba9c52c8014
pdf_path: papers/ReaxFF_others/McLean_Page_BN_CVD_JPC_2018_SI.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018page-venue-ben-bnnt -->

This note registers the **supporting information** PDF for the J. Phys. Chem. C article on boron nitride nucleation during boron-oxide CVD (see canonical article page [[2018mclean-j-phys-chem-boron-nitride]]). The SI excerpts in the corpus summarize supplementary figures on water and N2 formation pathways and multilayer BN/O structures from the ReaxFF MD simulations described in the main paper. The SI PDF is the file ingested at `pdf_path`; for scientific conclusions and discussion, treat [[2018mclean-j-phys-chem-boron-nitride]] as the primary citation target.

## Summary

The SI package accompanies McLean, Webber, and Page’s study of BN nucleation during boron-oxide chemical vapor deposition (DOI `10.1021/acs.jpcc.8b05785`). Figures excerpted here illustrate H2O and N2 evolution in selected ReaxFF MD runs at 1100 °C and 1 atm and show example B–O chain motifs that suppress cage closure compared with ammonia-bearing chemistry. The supporting-information scope is explicitly figure-level: it extends the main-text ReaxFF survey of boron–oxygen gas-phase chemistry with time-series populations and proposed elementary sequences referenced by simulation labels (Simulations 1–7 in the captions).

## Methods
This corpus entry ingests the **Supporting Information** PDF for McLean, Webber, and Page (*J. Phys. Chem. C*, DOI **10.1021/acs.jpcc.8b05785**). **Primary scientific narrative and full MD protocols** belong on **`[[2018mclean-j-phys-chem-boron-nitride]]`**.

**1 — MD application (SI figure captions only).** The **SI** captions excerpted locally describe **ReaxFF** gas-phase trajectories at **1100 °C** and **1 atm** tracking **H₂O** (**Simulations 2–3**, **0–10 ns**) and **N₂** (**Simulations 4–7**, **0–10 ns**), plus a **B₁₅O₁₅** chain snapshot from **Simulation 1** within **0–5 ns**. **Ensemble / pressure context:** captions reference **isobaric (1 atm)** **MD** staging at high **temperature**; exact **NVT** vs **NPT** labels, **thermostat**/**barostat** keywords, and **LAMMPS** input decks are **not** duplicated in this **SI-only** corpus slice—copy them from the **main article** + full **SI**. **Engine / code, atom counts, PBC, timestep:** **N/A —** beyond caption windows above; import from **`[[2018mclean-j-phys-chem-boron-nitride]]`** when reproducing runs.

**2 — Force-field training.** **N/A —** parameterization is inherited from the parent **ReaxFF** description in the **main paper**.

**3 — Static QM.** **N/A —** not the purpose of this **SI** file entry.

## Findings
**Outcomes:** caption-level excerpts describe **H₂O** and **N₂** evolution pathways (including **OH** abstraction from **NH₂** and **N–N** formation routes) and show **B–O chain** motifs that **hinder cage closure** relative to **ammonia-driven** pathways in the parent study.

**Comparisons:** interpret only alongside **`[[2018mclean-j-phys-chem-boron-nitride]]`** so **simulation numbering** stays consistent.

**Sensitivity:** **temperature** (**1100 °C**) and **simulation label** (**Simulations 1–7**) organize the SI plots.

**Limitations:** this wiki page is **not** a substitute for the **VOR article**; bond-order cutoffs, thermostats, and feed compositions for each labeled run remain in the **full SI**.

**Corpus honesty:** treat **`pdf_path`** as **non-primary** supporting material per `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md` policy when applicable.

## Limitations

This file is not a substitute for the full article PDF; scientific claims should be verified against the main text and complete SI. The extract contains only figure captions; bond-order cutoffs, thermostats, and initial boron–oxygen feed compositions for each labeled simulation appear in the full SI or main article, not in this short corpus snippet.

## Relevance to group

Provides SI context for a ReaxFF-based BN CVD nucleation study aligned with reactive MD workflows in the group’s corpus.

## Citations and evidence anchors

- Main article: [[2018mclean-j-phys-chem-boron-nitride]] (DOI [10.1021/acs.jpcc.8b05785](https://doi.org/10.1021/acs.jpcc.8b05785))

## Related topics

- [[2018mclean-j-phys-chem-boron-nitride]]
- [[reaxff-family]]

## Reader notes (navigation)

- Canonical article: [[2018mclean-j-phys-chem-boron-nitride]].
