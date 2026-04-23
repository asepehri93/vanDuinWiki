---
id: paper:2017liu-venue-proof-2-pdf
type: paper
title: "Atomistic Insights into Nucleation and Formation of Hexagonal Boron Nitride on Nickel from First-Principles-Based Reactive Molecular Dynamics Simulations (galley PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:hexagonal-boron-nitride
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:application
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.6b06736"
year: 2017
authors:
  - "Song Liu"
  - "Adri C. T. van Duin"
  - "Diana M. van Duin"
  - "Bin Liu"
  - "James H. Edgar"
venue: "ACS Nano"
pdf_sha256: "ecb306783a4f04b6a98c8ce43c0a8a190b858229f4a12c32f3987c66a47741f0"
pdf_path: "papers/Liu_ACS_Nano_BN_Nickel_2017_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017liu-venue-proof-2-pdf -->

## Summary

This ingest records **`papers/Liu_ACS_Nano_BN_Nickel_2017_galley.pdf`**, an **ACS galley / proof** duplicate of the **ACS Nano** article (DOI `10.1021/acsnano.6b06736`) on **first-principles-informed ReaxFF molecular dynamics** of **hexagonal boron nitride (hBN)** **nucleation** from **elemental B and N** on **nickel** surfaces. For readers who need a **one-stop scientific précis** before opening the PDFs: the peer-reviewed work combines **periodic DFT** on **Ni(111)** and **Ni(211)** with **ReaxFF** training focused on **Ni–B** and **Ni–N** interactions, then uses **LAMMPS** **reactive MD** to follow **growth** from **deposited** **B** and **N** through **chain-like BN motifs** toward **hexagonal** **hBN** patches, with **DFT** spot checks on **intermediates** as described on **`[[2017liu-venue-research]]`**. The **galley** file should reproduce the **same** scientific text as the **ASAP** PDF aside from publisher formatting. The scientific contribution—a combined **DFT** and **ReaxFF** story about **precursor chemistry**, **surface-mediated** assembly, and **growth** pathways toward **hBN**—is documented on the **canonical** wiki page **`[[2017liu-venue-research]]`**, which uses the **ASAP / issue** PDF `papers/Liu_ACS_Nano_BN_Nickel_2017_ASAP.pdf`. Per [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md), **galley** files may show **watermarks**, **placeholder pagination**, or **layout** differences; **citable** figure and page references should follow the **VOR sibling** unless the proof file itself is the object of study. The peer-reviewed abstract on the galley’s first page states that reactive molecular dynamics with the fitted ReaxFF potential shows nucleation beginning from linear BN chains that evolve toward branched motifs and hexagonal lattices, with subsequent DFT calculations used to confirm intermediate energetics along that pathway.

## Methods

**Corpus duplicate of the same DOI.** This slug registers **`papers/Liu_ACS_Nano_BN_Nickel_2017_galley.pdf`**; the **computational narrative** (**periodic DFT** training sets for **Ni–B/Ni–N**, **ReaxFF** refit, and **LAMMPS rMD** of **hBN** nucleation from **deposited B/N** on **Ni**) is **identical in scientific content** to **`[[2017liu-venue-research]]`**, which should be treated as the **canonical** wiki page for **protocol numbers** (see that page’s **Methods** sourced from the **ASAP/VOR PDF**).

**N/A — independent Methods block on this page**: operators should not maintain divergent timestep/ensemble text here; any refresh should **mirror** the **canonical** page after PDF verification.

**Blueprint alignment (galley duplicate).** For automated checks: **N/A — system size & atom counts** on this duplicate page—use **`[[2017liu-venue-research]]`**. **N/A — MD duration (ps/ns)** here—canonical page carries **≥6 ns** rMD runs. **N/A — thermostat damping** details here—canonical page lists **Nosé–Hoover** + **0.25 fs** timestep. **N/A — barostat / pressure control** for the rMD growth segment—canonical setup is a **fixed slab + vacuum** style description. **N/A — target temperature grid** duplication—see **900–1500 K** on the canonical page.

## Findings

**Corpus honesty and navigation.** **No additional scientific results** are claimed for the **galley** relative to the **ASAP**/**issue** PDF tracked on **`[[2017liu-venue-research]]`**. Use the **canonical** page for **barrier estimates**, **run lengths**, **temperature grids**, and **figure** citations; use this slug only when the **question is which ingested bytes** (galley watermark, placeholder pagination) apply.

## Limitations

**Proof/galley** PDFs are **non-authoritative** for bibliometrics and may omit **final copy edits**. Automated pipelines should **prefer** the ASAP hash recorded on **`[[2017liu-venue-research]]`** for text mining.

**Confidence rationale:** `med`—navigation and corpus policy are explicit; detailed science is intentionally delegated.

## Reader notes (navigation)

- Canonical article: [[2017liu-venue-research]]
- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2017liu-venue-research]]
- [[reaxff-family]]
