---
id: paper:2014raju-venue-nl404533k-2
type: paper
title: "Mechanisms of oriented attachment of TiO2 nanocrystals in vacuum and humid environments: reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/nl404533k"
year: 2014
authors:
  - "Muralikrishna Raju"
  - "Adri C. T. van Duin"
  - "Kristen A. Fichthorn"
venue: "Nano Letters"
pdf_sha256: "b5b203156be521f5a4568a1ae176f46827bcb164037c792774b0a0d8280b9956"
pdf_path: "papers/Raju_Nano_Letters_2014_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014raju-venue-nl404533k-2 -->

!!! abstract "Alternate corpus PDF for the Nano Letters letter on ReaxFF MD of anatase TiO2 aggregation in vacuum vs humid environments (same scientific content as the proof-ingest sibling)."

## Summary

This page registers a **second ingested PDF** for the **same** **Nano Letters** article (DOI **10.1021/nl404533k**) on **TiO\(_2\)** **nanocrystal** **aggregation** and **oriented attachment (OA)** studied with **ReaxFF MD**. Maintainer mapping of **duplicate** PDF paths: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md). The substantive scientific summary matches **`[[2014raju-venue-nl-2013-04533k]]`**: **vacuum** versus **humid** pathways, **hydrogen-bond-mediated** **particle** **reorientation** under **humid** conditions, and emphasis on **surfaces** that **dissociate water** more readily as **OA**-favorable facets. The letter argues **humidity** switches **aggregation** from **kinetic** **trapping** in **misaligned** **dimers** toward **thermodynamically** preferred **aligned** interfaces.

## Methods

### Corpus / extract provenance

- Local PDF: `papers/Raju_Nano_Letters_2014_reduced.pdf`; extract: `normalized/extracts/2014raju-venue-nl404533k-2_p1-2.txt` (overlaps sibling extract `2014raju-venue-nl404533k_p1-2.txt` for the same letter).

### Computational protocol (canonical reference)

- Full **ReaxFF MD** settings for **Ti/O/H** chemistry in **ADF**, **Wulff** vs asymmetric **anatase** **nanocrystals**, **eight-particle** supercells (**125 × 325 × 125 Å**), **NVT** at **573 K** for **1.0–2.0 ns**, **~15 000–18 000 atoms**, and **vacuum** vs **humid** comparisons are documented on **`[[2014raju-venue-nl-2013-04533k]]`**—this slug duplicates bytes only.

### Operator guidance

- Prefer **`[[2014raju-venue-nl-2013-04533k]]`** for stable **pagination** and **figure** references; keep this slug for **manifest** **SHA-256** provenance.

### 1 — MD application (duplicate PDF record)

The scientific protocol matches **`[[2014raju-venue-nl404533k]]`**: **ReaxFF** **molecular dynamics** in **ADF** on **eight** **Wulff** **anatase** nanocrystals (**125 × 325 × 125 Å** cell, **≥ 30 Å** initial separation), **NVT** at **573 K**, **1.0–2.0 ns** trajectories, **~15 000–18 000 atoms** typical, **vacuum** vs **humid** environments. **Timestep / thermostat / explicit PBC paragraph:** **N/A —** not repeated from the indexed extract on this duplicate page—see **`[[2014raju-venue-nl404533k]]`**. **Barostat / NPT pressure control:** **N/A —** **NVT** excerpt only. **Electric field / enhanced sampling:** **N/A —** not used in the letter’s aggregation study.

### 2 — Force-field training

**N/A —** same **Kim *et al.*** **Ti/O/H** application as siblings.

## Findings

**Vacuum** trajectories merge along the **approach direction** into **polycrystalline** agglomerates **without oriented attachment (OA)**, consistent with cited prior work. **Humid** environments enable **reorientation** and **OA** into **single** or **twinned** crystals through **dynamic hydrogen-bond networks** between **surface hydroxyls** and **oxygens**. **OA** is reported **most favorable** on facets with the highest **water-dissociation** propensity—linking **surface chemistry** to pathway selection. The authors state **agreement with experiment** and argue for a **critical solvent** role in **aqueous oxide** **nanoparticle aggregation** generally.

**Sensitivity / corpus view.** **Temperature** is fixed at **573 K** in the excerpted protocol to echo hydrothermal experiments; **humidity** level is the main environmental lever contrasted with **vacuum**. **Limitations** on finite nanocrystal size and accessible **simulation time** remain as on the primary pages.

**Corpus honesty.** This slug tracks **`papers/Raju_Nano_Letters_2014_reduced.pdf`**; use **`[[2014raju-venue-nl404533k]]`** for **version-of-record** pagination when possible.

## Limitations

Maintained as a **duplicate blob record**; prefer a single **authoritative PDF** for **figure** extraction consistency and **pagination**.

## Relevance to group

Same as the primary Raju et al. entry; kept for **manifest completeness** and local PDF provenance.

## Reader notes (navigation)

- Primary sibling: [[2014raju-venue-nl-2013-04533k]].

When building **retrieval** **chunks**, prefer **`[[2014raju-venue-nl-2013-04533k]]`** for stable **Nano Letters** **pagination**; retain this slug so **manifest** **SHA-256** rows and **local** **PDF** filenames stay **traceable** for **reproducibility** audits. **Humidity** levels and **water** **counts** in **simulation** cells follow the **Nano Letters** methods; do not infer **RH** **values** from filenames alone. **Eight-particle** **supercell** dimensions and **573 K** **NVT** **duration** ranges are stated in the letter and should be copied exactly when **re-running** **aggregation** **benchmarks** reported in the **Nano Letters** study.

## Citations and evidence anchors

- DOI: [10.1021/nl404533k](https://doi.org/10.1021/nl404533k)
