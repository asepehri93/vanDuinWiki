---
id: paper:2018sengul-venue-total-number
type: paper
title: Total Number of pages:7 (author proof, uncorrected)
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reactive-md
- domain:water-silica-geo
- method:reaxff
- method:enhanced-sampling
- scale:atomistic
- task:application
paper_keywords:
- keyword:galley-or-proof-pdf
- keyword:reaxff-application
- keyword:enhanced-sampling
candidate_tags: []
source_refs: []
doi: ''
year: 2018
authors:
- Mert Y. Sengul
- Clive A. Randall
- Adri C. T. van Duin
venue: J. Chem. Phys. (author proof PDF)
pdf_sha256: a0143e0eeb0268a04da39404a20d8ffaf70dcddf39f4dd2c419dac9be5ecb8de
pdf_path: papers/Sengul_aceticacid_water_JCP_2018_proof.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018sengul-venue-total-number -->

## Evidence and attribution

!!! note "Authority of statements"

    This page describes a **non-version-of-record** AIP author proof PDF. For full **Methods**/**Findings**, see **`[[2018sengul-venue-reaxff-molecular]]`**; a later **corrected** proof is **`[[2018sengul-venue-total-number-2]]`**.

!!! abstract "Corpus role"

**Uncorrected AIP proof** with **author query** forms for the **acetic acid–water** **ReaxFF** **JCP** paper; cite **`[[2018sengul-venue-reaxff-molecular]]`** for stable locators.

## Summary

This ingest registers an **AIP uncorrected author proof** PDF (`papers/Sengul_aceticacid_water_JCP_2018_proof.pdf`), not the journal version of record. The file interleaves the manuscript text of *ReaxFF molecular dynamics simulation of intermolecular structure formation in acetic acid–water mixtures at elevated temperatures and pressures* with publisher query forms about figure styling, thermostat language, and glossary entries for software such as **ReaxFF**, **VMD**, and **ADF**. Scientifically, the associated study parametrizes acetic acid and water within **AMS ReaxFF**, uses **metadynamics** to calibrate acid dissociation (\(K_a\)) against reference data, and runs **canonical molecular dynamics** with a **0.25 fs** timestep and **Berendsen** thermostat across ambient to **supercritical** temperature and pressure grids. Structural analysis emphasizes radial distribution functions, hydrogen-bond populations, and clustering trends as a function of acetic acid mole fraction **\(x_{\mathrm{HAc}}\)**. Full methods, finalized figures, and bibliographic cleanup appear on the curated article page **`[[2018sengul-venue-reaxff-molecular]]`**. Maintainer note: proof and alternate PDF roles are catalogued on GitHub: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Methods

Parameter merges, metadynamics window choices, and **1000-molecule** bulk cells with scanned **acetic acid** mole fractions follow the published workflow summarized on **`[[2018sengul-venue-reaxff-molecular]]`** (issue PDF: `papers/Sengul_aceticacid_water_JCP_2018_online.pdf`). This proof duplicate is suitable for tracing editorial queries and hash-level manifest linkage, but operators should cite simulation protocols, thermodynamic state points, and analysis scripts from the **online** article page rather than from the proof pagination. Corrected-proof sibling **`[[2018sengul-venue-total-number-2]]`** may capture intermediate editorial states; the scientific MD definition (ensemble, duration, equilibration) remains aligned with the online entry.

**MD pointers (version-of-record).** For **engine**, **PBC**, **timestep**, **thermostat**, **ensemble**, **temperature**/**pressure** grids, and **metadynamics** calibration details, use **`[[2018sengul-venue-reaxff-molecular]]`**: **ReaxFF molecular dynamics** in **ADF** on **1000-molecule** **periodic** cells (order **\(10^4\)** **atoms** depending on composition), **0.25 fs** integration, **Berendsen** **thermostat**, **NVT** bulk sweeps with **NPT** **metadynamics** for **\(K_a\)**, staged **equilibration**/**production** **nanosecond** segments, and **N/A — electric field** not used. This **proof** path is **not** authoritative for pagination or final copy edits.
## Findings

The chemical narrative matches **`[[2018sengul-venue-reaxff-molecular]]`**: under ambient-like conditions, acid-rich compositions favor cyclic dimers and chain-like hydrogen-bond motifs that water can disrupt; upon approaching supercritical conditions, long-range spatial correlations weaken while short-range first-neighbor structuring can persist over the \(T,P\) sweeps reported. Because this file is a **non-VOR** artifact, quantitative RDF peaks, coordination numbers, and cluster statistics should be quoted from the version-of-record page after cross-checking figure labels.

**Comparisons / sensitivity / limitations.** Treat **`[[2018sengul-venue-reaxff-molecular]]`** as the **experiment**-anchored **comparison** hub for **\(K_a\)** calibration and for **temperature**/**pressure**/**composition** trends; this **proof** PDF may omit final figure labels. **Limitations** of **author proofs** are summarized under **## Limitations** below.
## Limitations

**Author proofs** may lack **final** editorial corrections present in the **issue** PDF; **query forms** are not part of the scientific record.

## Relevance to group

Workflow duplicate for a **van Duin**-co-authored **ReaxFF** **solution** chemistry paper.

## Reader notes (navigation)

- Article page: [[2018sengul-venue-reaxff-molecular]]
- Corrected proof: [[2018sengul-venue-total-number-2]]

## Citations and evidence anchors

- Prefer **`[[2018sengul-venue-reaxff-molecular]]`** for bibliographic completion once DOI is synced from the issue.

## Related topics

- [[reaxff-family]]
