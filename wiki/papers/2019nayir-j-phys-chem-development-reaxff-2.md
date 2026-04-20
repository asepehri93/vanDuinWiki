---
id: paper:2019nayir-j-phys-chem-development-reaxff-2
type: paper
title: "Development of the ReaxFF Reactive Force Field for Inherent Point Defects in the Si/Silica System"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:silicate-glass
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.9b01481"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "J. Phys. Chem. A 123:4303-4313 (2019)"
pdf_sha256: "e83be92a076307cb250a2862abfbcfc690943f4398b88fd38eab3318eec84ad8"
pdf_path: "papers/Nayir_JPC_C_SiOx_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019nayir-j-phys-chem-development-reaxff-2 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Si/O/H ReaxFF parameters are redeveloped to treat O interstitials and migration in bulk Si and oxidation chemistry at a-SiO2/Si interfaces, emphasizing point-defect behavior omitted by earlier fits. The new “ReaxFFpresent” reproduces the bond-centered hopping pathway for O in Si with a barrier near 65 kcal/mol, closer to experiment/DFT than prior SiOH(2010) behavior that spuriously allowed deep O diffusion at 300 K. Annealing simulations of prepared a-SiO2 on Si recover expected interfacial O transport relative to literature, including fixing the low-temperature spurious diffusion issue.

## Methods

Large QM-guided training for Si/O/H; construction of amorphous silica at experimental density; high-temperature MD for O diffusion and a-SiO2/Si annealing; comparison to prior ReaxFF SiOH(2010).

## Findings

O migration in bulk Si follows BC–BC hops in the (110) plane with a split-like saddle, initiation of significant diffusion above roughly 1400 K in their analysis, and temperature-dependent diffusion coefficients in broad agreement with experiment. a-SiO2 density matches experiment closely.

## Limitations

Focus on Si/SiO2 defect and interface phenomena; parameters are not automatically transferable to unrelated chemistries (e.g., alkali-containing silicates) without testing.

## Relevance to group

Foundational ReaxFF for silicon oxidation—central to much group and field work on gate stacks and silica.

## Citations and evidence anchors

`papers/Nayir_JPC_C_SiOx_2019.pdf` — abstract (barrier, pathway, fix of unphysical low-T diffusion). https://doi.org/10.1021/acs.jpca.9b01481

Supporting information PDF: [[2019nayir-venue-paper]].

## Related topics

- [[2019nayir-venue-paper]]
- [[reaxff-family]]
