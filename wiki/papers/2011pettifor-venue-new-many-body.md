---
id: paper:2011pettifor-venue-new-many-body
type: paper
title: "New many-body potential for the bond order"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:classical-ff-specialized
  - method:semiempirical-tightbinding
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:method-development
  - keyword:eam-potential
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.63.2480"
year: 1989
authors:
  - "D. G. Pettifor"
venue: "Physical Review Letters 63, 2480–2483 (1989)"
pdf_sha256: "9fd89e92850537ba8c8eea2cd58c91bfa7da4b8cc51741e1d881ceface69b486"
pdf_path: "papers/Others/Pettifor_PhysRevLett.63.2480.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011pettifor-venue-new-many-body -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Physical Review Letter** derives an **analytic many-body potential** for the **bond order** in **s-valent** systems so that **local atomic environment** directly modulates **bond strength**. The formulation uses **recursion/Green’s-function** ideas: bond order is expressed via an integral involving **bonding and antibonding** Green’s functions, with **three-** and **four-membered ring** (path) contributions controlling differences between bonding and antibonding recursion coefficients. The work motivates extending **embedded-atom** style models with explicit **three-body** and **four-body** terms tied to bond-order physics, addressing failures of bulk-fitted potentials on **small clusters**.

## Methods


This **Physical Review Letter** derives bond order for **s-valent** systems from a **recursion / tridiagonal Hamiltonian** picture: bond order is an integral over **bonding vs antibonding Green’s functions** written as **continued fractions**, with **three-membered-ring** and **four-membered-ring** path contributions entering at successive recursion levels as differences between bonding and antibonding coefficients. A **Dyson / perturbation** expansion about an **average** reference Green’s function yields an explicit **many-body** bond-order expression involving **response functions** \(Z_{p,n}\) for a reference semi-infinite linear chain; an analytic limiting case uses **zero on-site energies** and **constant hopping** \(b\) with **Fermi energy** fixed by **electron count per atom** \(N\). The formalism is illustrated for how **environment** reduces bond order relative to an isolated dimer and how **cluster topology** (e.g., four-atom clusters) selects among bonding patterns.

## Findings

The Letter provides an **analytic many-body bond-order potential** for **s-valent** systems in which **local atomic environment** directly modulates **bond strength**, addressing failures of **bulk-fitted** potentials on **small clusters**. It demonstrates that **three-** and **four-membered-ring** terms control differences between bonding and antibonding recursion coefficients at low orders, and it discusses reduced **response functions** versus **electrons per atom** (Figure 1 in the Letter). The work positions **bond-order** concepts as a bridge from **tight-binding/recursion** intuition toward **empirical** many-body models used in MD, explicitly citing **Tersoff**-type and **Chelikowsky**-style bond-order constructions as related context.

**Comparisons / outlook.** The discussion contrasts **embedding / second-moment** rationales with the need for explicit **three-body** and **four-body** terms in open **tetrahedral** semiconductors, and cites prior **bond-order fits** to **Si** that successfully span **bulk and cluster** geometries.

**Corpus honesty.** This page is grounded in **`pdf_path`** and `normalized/extracts/2011pettifor-venue-new-many-body_p1-2.txt` (PRL letter text); any extended citations beyond the excerpt require the PDF.

**Outlook.** **However**, the Letter’s explicit scope is **s-valent** toy models and analytic structure; quantitative MD benchmarks are not the subject of these pages.

## Limitations

- s-valent focus; transfer to transition metals or polar systems requires extensions not contained in this short Letter.
- Practical **classical** potentials still require **parametrization** choices when implementing bond-order ideas in MD engines.

## Relevance to group

Historical **bond-order** foundation relevant to **ReaxFF** and **Brenner/Tersoff** lineages used throughout the corpus.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevLett.63.2480](https://doi.org/10.1103/PhysRevLett.63.2480)
- Text-aligned pointer: `normalized/extracts/2011pettifor-venue-new-many-body_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Bond-order and empirical many-body potentials (lineage context)
