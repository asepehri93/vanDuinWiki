---
id: paper:2006chenoweth-venue-microsoft-word
type: paper
title: "ReaxFF potential functions: supporting information (hydrocarbon oxidation manuscript)"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:method-development
  - keyword:charge-equilibration
  - keyword:reactive-md
  - keyword:supporting-information
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:methods-software
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2006
authors:
  - "Kimberly Chenoweth"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Supporting information (manuscript supplement)"
pdf_sha256: "e1579503ae4f486d0b592fdf2698928927f196f509dfe9f6ed95b664f252b935"
pdf_path: "papers/CHO_supplements/ReaxFF_CHO_potential_functions.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2006chenoweth-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below describe the **supporting-information document** identified by `pdf_path`. They are **not** new primary claims by this wiki.

    Equation numbering and full algebraic details are in the **PDF**.

## Summary

This document lists the **general ReaxFF potential-function definitions** accompanying the same hydrocarbon-oxidation manuscript as the CHO parameter file. It states that the current ReaxFF code evaluates **all** energy contributions listed, regardless of system composition, and explains naming: parameters without direct physical meaning are named after the partial energy term in which they appear (e.g., valence-angle parameters), while quantities such as torsional barriers use conventional symbols (V1, V2, V3). The extract covers the **total system energy** decomposition, **bond order** from interatomic distance (sigma, pi, pipi contributions), and **overcoordination** definitions used to correct bond orders—including a lone-pair-aware overcoordination for atoms such as oxygen and nitrogen.

## Methods


The supplement gives the general ReaxFF potential-function definitions in equation form for the same hydrocarbon-oxidation manuscript as the CHO parameter file. It states that the current ReaxFF implementation evaluates every energy contribution listed regardless of system composition, and it explains parameter naming: coefficients without direct physical meaning are named after the partial energy term in which they appear (for example valence-angle parameters), while familiar symbols such as torsional barriers \(V_1\), \(V_2\), \(V_3\) are retained where appropriate. The documented terms include the overall system energy decomposition (Coulomb, van der Waals, bond, hydrogen bond, conjugation, torsion, triple and overcoordination/undercoordination, valence, penalty, lone pair, and bond-order corrections as in Equation (1) of the PDF), bond order from interatomic distance via sigma, pi, and double-pi contributions (Equation (2)), uncorrected overcoordination (Equation (3a)), a lone-pair-aware overcoordination for atoms such as oxygen and nitrogen (Equation (3b)), and the bond-order correction scheme (Equations (4a–f) in the typeset PDF).

### MD application (not reported)

This supplement defines **energy expressions** for use in **molecular dynamics** engines; it does not archive a specific trajectory. **N/A — MD code**; **N/A — atom counts**; **N/A — PBC**; **N/A — NVE/NVT/NPT** run script; **N/A — timestep**; **N/A — trajectory length** (no **ps**/**ns** **production** segment documented here); **N/A — equilibration** MD schedule in this PDF; **N/A — thermostat**; **N/A — barostat**; **N/A — MD temperature**; **N/A — MD pressure**; **N/A — electric field**; **N/A — enhanced sampling**.

### Force-field training (scope boundary)

**Parent FF / elements:** **ReaxFF** functional form paired with the **C/H/O combustion** parameterization line. **QM / DFT training data, reaction sets, optimizer, and validation tables:** **N/A in this PDF**—read the peer-reviewed **hydrocarbon oxidation** article and other CHO supplements for **DFT** reference data and **optimization** details. This file’s role is **documentation of terms** that enter the **parameter fit** performed elsewhere.

## Findings

The supplement defines the **same** general ReaxFF energy decomposition (Equation (1)), **distance-derived** bond orders (Equation (2)), **overcoordination** and **lone-pair-aware** \(\Delta'_{\mathrm{boc}}\) corrections (Equations (3a–b), (4a–f)) used with the CHO combustion parameter file. Bond orders combine \(\sigma\), \(\pi\), and double-\(\pi\) contributions; lone-pair-bearing atoms can rearrange bonding without a full spurious overcoordination penalty. Together with the numeric parameter listing, it specifies the functional form a compatible engine must implement for the parent hydrocarbon-oxidation chemistry. **Limitations / outlook:** **N/A —** no application benchmarks are reported in this methods PDF alone—consult the parent article. **Corpus honesty:** equation text in `normalized/extracts/2006chenoweth-venue-microsoft-word_p1-2.txt` is a fragment; the typeset **`pdf_path`** is authoritative.

## Limitations

- This is **methods documentation** for implementers; validation and application results are in the **main article** and application studies.
- PDF text extraction fragments some equation formatting; the typeset PDF is authoritative.

## Relevance to group

**Adri C. T. van Duin** is a named co-author on the parent manuscript; this supplement documents the **functional form** underlying multiple ReaxFF parameterizations in the group’s toolchain.

## Citations and evidence anchors

- PDF: `papers/CHO_supplements/ReaxFF_CHO_potential_functions.pdf`.
- Extract: `normalized/extracts/2006chenoweth-venue-microsoft-word_p1-2.txt`.

## Related topics

- [[reaxff-family]]
