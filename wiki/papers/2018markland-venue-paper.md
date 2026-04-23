---
id: paper:2018markland-venue-paper
type: paper
title: "Nuclear quantum effects enter the mainstream"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:pimd
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:aimd
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/s41570-017-0109"
year: 2018
authors:
  - "Thomas E. Markland"
  - "Michele Ceriotti"
venue: "Nat. Rev. Chem."
pdf_sha256: "490e17b2507b979af5651405386d4a0b8b5b845e26def826e4622c9d3dabc2e7"
pdf_path: "papers/Others/Markland_PIMD_2018_review.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2018markland-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Nature Reviews Chemistry* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Classical molecular dynamics treats nuclei as point masses moving on a Born–Oppenheimer potential energy surface, which is computationally attractive but can fail when zero-point energy, tunneling, or quantized vibrational structure materially affects structure, spectroscopy, or rates. This review explains why nuclear quantum effects (NQEs) have moved from niche corrections to a mainstream concern in condensed-phase chemistry and materials modeling. It surveys conceptual limitations of the classical-nuclei picture, introduces path-integral and ring-polymer perspectives for incorporating NQEs in simulation, and discusses practical algorithms, cost trade-offs, and when empirical potentials that implicitly fold quantum behavior into parameters at one thermodynamic state can obscure the physical origin of isotope effects and other NQE-sensitive observables.

The review also stresses that **zero-point energy** for stiff **X–H** stretches can exceed **thermal** energy near **ambient** conditions, so **hydrogen-bonded** networks, **proton** transport, and **enzyme** active sites are not “quantum only at cryogenic temperatures.” That observation reframes when practitioners should budget for **path-integral molecular dynamics (PIMD)** or related estimators instead of assuming classical sampling is always sufficient for **light** atoms.

## Methods

The article is a **review**, not a single computational benchmark. Its structure typically progresses from (i) physical motivation and examples where NQEs matter even near ambient conditions, (ii) path-integral and related formulations that treat nuclear motion beyond Newtonian dynamics on a fixed electronic surface, (iii) discussion of approximate schemes, software ecosystems, and scaling with system size and timestep, and (iv) commentary on interpreting experiments and force fields when light atoms (especially hydrogen) or low temperatures amplify quantum–classical differences. Readers should use the published sections and citations for equation-level detail and for links to primary methodological papers.

**Ring-polymer picture.** In practice, many implementations map **quantum** **Boltzmann** sampling of nuclei onto **classical** dynamics of **beads** in an extended phase space, which explains the connection between **PIMD** cost and **number of beads** required for convergence at a target temperature. The review discusses how **open-path** versus **closed-path** estimators relate to **kinetic** versus **structural** properties.

## Findings

The review argues that NQEs can change structures, reaction rates, and isotope effects in hydrogen-bonded and proton-transfer systems where zero-point energy is comparable to or larger than relevant thermal energy scales for key modes. It cautions that classical force fields fitted to reproduce experimental data at one condition may absorb NQEs into effective parameters, which complicates transferability and physical interpretation. Path-integral molecular dynamics and related techniques are presented as practical routes to treat NQEs more explicitly when the problem demands it, balanced against computational cost.

**Implication for empirical models.** When **isotope effects** are **zero** in a classical simulation by construction, any agreement with measured **H/D** or **T** fractionation must be questioned: either the observable is insensitive, or the model has **implicitly** baked **quantum-like** shifts into its parameters. The review uses that tension to motivate **explicit** **NQE** methods rather than over-interpreting classical fits.

## Limitations

This is **not** a ReaxFF application note; connections to the van DuinWiki corpus are **pedagogical** (when to consider PIMD or path-integral checks alongside classical or reactive MD). `extraction_quality` remains partial in profiling metadata; cite the **Nat. Rev. Chem.** PDF for authoritative section numbering.

## Relevance to group

Background for judging when classical ReaxFF or classical MD may need nuclear quantization checks for light atoms, low temperatures, or isotope-specific experiments.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/s41570-017-0109](https://doi.org/10.1038/s41570-017-0109) (`papers/Others/Markland_PIMD_2018_review.pdf`).

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Curation hygiene.** After substantive edits to this wiki page, Phase 5 chunk identifiers are refreshed by running `python3 scripts/build_chunks.py` from the repository root so `indexes/chunks.jsonl` stays aligned with section headings and body text. The `updated` field in front matter records the last wiki revision date for operator review.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
