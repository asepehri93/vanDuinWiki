---
id: paper:2014joshi-venue-rsc-cp
type: paper
title: "Reactive molecular simulations of protonation of water clusters and depletion of acidity in H-ZSM-5 zeolite"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:zeolite-porous
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp02612h"
year: 2014
authors:
  - "Joshi, Kaushik L."
  - "Psofogiannakis, George"
  - "van Duin, Adri C. T."
  - "Raman, Sumathy"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "9cde92b4f14b74a8929595c9a80abb8aa34f0d4a2eae56c25085a2debbdf3221"
pdf_path: "papers/Joshi_PCCP_2014_Zeolite_protons_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014joshi-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **publisher proof** extract. For tables, references, and final pagination, use the **edited article** PDF.

## Summary

This wiki slug registers a **publisher proof PDF** (`papers/Joshi_PCCP_2014_Zeolite_protons_proof.pdf`) for the same Physical Chemistry Chemical Physics article as [[2014joshi-physical-che-reactive-molecular]] (**DOI `10.1039/c4cp02612h`**). Scientifically, the study uses **ReaxFF reactive molecular dynamics** with **refitted Si/Al/O/H** parameters trained against **density functional theory** to improve **water–Brønsted acid site** energetics in **H-ZSM-5 (MFI)**. The authors probe **adsorption**, **self-diffusion**, and **loading-dependent protonation** of water, including formation of **protonated water clusters** at higher water content and rapid **proton hopping** that relocates charge among acid sites—mechanisms framed as **depleting localized acidity** in a loading- and temperature-dependent sense. For authoritative pagination, final figure labels, and any editorial corrections, readers should use the **version-of-record PDF** on the sibling page; this proof ingest exists for corpus provenance and may contain **author-query** banners.

## Methods

This slug registers a **publisher proof** PDF for the same article as **`[[2014joshi-physical-che-reactive-molecular]]`** (**DOI `10.1039/c4cp02612h`**); **Methods text should be cited from the version-of-record PDF** when possible.

### Reactive MD system (H-ZSM-5 + water)

- **ReaxFF RMD** in a **periodic MFI** framework explores **water loading** and **temperature** as control variables for **adsorption**, **diffusion**, and **Brønsted-site** proton chemistry (**Summary**).

### Parameter refit against DFT

- **Si/Al/O/H** parameters are **refit** using **DFT** training data emphasizing **acid-site** energetics and **water–framework** interactions relative to an earlier parameter set (**Summary**).

### What this proof PDF is not

- The proof file may contain **layout queries** and is **not** authoritative for **final** **run lengths**, **cell sizes**, or **analysis** scripts—read **`[[2014joshi-physical-che-reactive-molecular]]`** + **VOR** PDF.

### 1 — MD application (proof ingest; same study as VOR)

- **Protocol:** **ReaxFF reactive molecular dynamics** on **periodic MFI** **H-ZSM-5** with **water loading** and **temperature** as controls (**Summary**); **N/A — engine string/timestep/thermostat law not re-keyed from `papers/Joshi_PCCP_2014_Zeolite_protons_proof.pdf` here** (use **`[[2014joshi-physical-che-reactive-molecular]]`**).
- **System size & composition:** **Zeolite** **supercell** models of **H-ZSM-5** with explicit **water** content as a loading variable (**abstract**-level description mirrored on the VOR page); **exact atom counts** are **N/A — not re-keyed from the proof PDF here**.
- **Boundaries / periodicity:** **Periodic** **MFI** framework (**Summary**); **N/A — full PBC statement not re-keyed from the proof PDF here**.
- **Ensemble:** **N/A — NVT/NPT choice not re-keyed from the proof PDF here** (VOR Methods).
- **Duration / stages:** **Equilibration** and **production** segment lengths are **N/A — not re-keyed from the proof PDF here** (VOR Methods).
- **Barostat / hydrostatic pressure:** **N/A — pressure control not re-keyed from the proof PDF here** (typical zeolite adsorption studies are constant-volume; confirm in VOR PDF).
- **Electric field:** **N/A — not indicated** in the abstract-level summary used here.
- **Replica / enhanced sampling:** **N/A — not indicated** in the abstract-level summary used here.

### 2 — Force-field training (proof ingest)

- **Refit scope:** **Si/Al/O/H ReaxFF** against **DFT** training data emphasizing **acid-site** energetics (**Summary**); **N/A — full QM table reproduction omitted on this proof-ingest page**.

## Findings

The **version-of-record** abstract and curated summary on **`[[2014joshi-physical-che-reactive-molecular]]`** report that the refitted force field yields a **water diffusion coefficient** in **strong agreement with experiment**, that **higher loading** increases the **frequency of water protonation** and supports **larger protonated clusters**, and that clusters remain **short-lived** because **protons and water molecules exchange rapidly** among clusters while **proton-hopping events** move protons between distinct **Brønsted** sites. This proof-ingest page does **not** independently verify those numerical results against the proof text, which is layout-incomplete by nature.

## Limitations

The local **`pdf_path`** is a **proof** with author queries and possible figure placeholder differences relative to the **VOR**. Use **`[[2014joshi-physical-che-reactive-molecular]]`** for stable scholarly citation strings.

For operators automating ingest, note that **proof** PDFs sometimes contain **watermark** lines and **query** sidebars that are not part of the scholarly text; downstream extractors may capture those artifacts, so curated wiki prose should prefer the **final** PDF when available.

## Reader notes (navigation)

Use [[2014joshi-physical-che-reactive-molecular]] (`papers/Joshi_PCCP_2014_Zeolite_protons.pdf`) for the **full article** text and citation strings.

## Citations and evidence anchors

- DOI `10.1039/c4cp02612h` (proof query block; extract).
- [[2014joshi-physical-che-reactive-molecular]] for VOR narrative.

## Related topics

- [[2014joshi-physical-che-reactive-molecular]]
- [[theme-porous-mof-zeolite]]
- [[reaxff-family]]
