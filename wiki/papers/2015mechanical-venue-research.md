---
id: paper:2015mechanical-venue-research
type: paper
title: "Mechanical properties and defect sensitivity of diamond nanothreads"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:reaxff
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1021/nl5041012"
year: 2015
authors:
  - "Ruth E. Roman"
  - "Kenny Kwan"
  - "Steven W. Cranford"
venue: "Nano Letters"
pdf_sha256: "14199e5e0cff882ad8ec4bdbd4480e78fb0c65244e21c43c167bb8dba837604a"
pdf_path: "papers/ReaxFF_others/Mechanical Properties and	Defect Sensitivity of Diamond Nanothreads.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015mechanical-venue-research -->

## Summary

Diamond nanothreads are ultrathin, hydrogenated sp\(^3\)-bonded carbon strands proposed as high-strength one-dimensional materials. This Nano Letters article uses ReaxFF reactive molecular dynamics to predict axial stiffness, strength, strain to failure, bending rigidity, and specific tenacity for model nanothread structures that include Stone–Wales defects, comparing performance to carbon nanotubes and graphene benchmarks cited in the paper. The wiki documents the same peer-reviewed article as **`[[2015roman-venue-nl5041012]]`** under an alternate local PDF filename and SHA-256 hash; treat both slugs as one publication for bibliographic purposes. The study emphasizes how topological defects modulate mechanical response under steered molecular dynamics loading, leveraging ReaxFF’s ability to capture bond rupture and rehybridization events beyond harmonic elastic treatments. Nanothread synthesis remains challenging; simulation therefore supplies property targets that guide experimentalists comparing measured moduli to ideal model strands.

## Methods

### MD application (atomistic dynamics)

The study uses **ReaxFF**-based **atomistic molecular dynamics** on hydrogen-terminated, sp\(^3\)-bonded **diamond nanothread** models built from linked diamondoid motifs with embedded **Stone–Wales** defects (the abstract notes 1–4 defect variants for structural comparison). **Equilibration / sampling:** a **~1 ns** trajectory at **300 K** on an **~8 nm** thread segment is used to compute a **radial distribution function** \(g(r)\) as a structural check. **Mechanical loading:** **quasi-static** cycles of incremental axial strain with energy minimization and **dynamic steered MD (SMD)** along the thread axis probe stiffness, peak stress/strain, and defect-density sensitivity; **virial stress** (and an equivalent 1D force metric) is used for tensile response. **Bending rigidity** is obtained from an **energy-minimization / molecular mechanics** protocol described in the **Supporting Information**. **Boundaries:** **periodic boundary conditions (PBC)** enclose the isolated **nanothread** models as in *Nano Lett.* / **SI**. **Ensemble / temperature / duration:** the abstract reports a **~1 ns** segment at **300 K** for RDF **equilibration**; the article/SI specify whether this segment is **NVT** (canonical) or otherwise and give **production** lengths for **SMD** pulls. **Timestep (fs)** and **thermostat** coupling for the steered segments are specified in the **Supporting Information** (main **Nano Lett.** letter text checked in corpus PDF does not repeat every numerical control). **Barostat / NPT pressure control:** **N/A** for the summarized constant-volume thread tests. **Electric field / umbrella or metadynamics:** **N/A**. **MD engine:** **N/A —** the **Nano Lett.** PDF examined for this page does **not** name the simulation package (implementation details are deferred to **SI**).

### Force-field training

**N/A —** the publication **applies** an existing **ReaxFF** parametrization for carbon/hydrogen chemistry (cited to prior ReaxFF carbon developments) rather than reporting a new fit in this letter.

### Static QM

**N/A —** not the primary methodology; benchmarking is against ReaxFF energy consistency with graphane reference and mechanical test protocols.

## Findings

The paper reports a Young’s modulus near **850 GPa**, peak strength near **26.4 nN** (the letter also quotes a virial **stress at failure** near **134.3 GPa** using their cross-section convention), failure strain near **14.9%**, bending rigidity near **5.35×10⁻²⁸ N·m²**, and specific tenacity near **4.1×10⁷ N·m/kg**, exceeding nanotube and graphene comparisons in their table. **Stone–Wales** defect count (**1–4** variants explored) systematically modulates strength, stiffness, and extensibility under steered loading; adding a defect raises the thread potential energy by about **12 kcal/mol** per the letter. These numbers are **ReaxFF** model outputs and should be cited with that caveat when comparing to experiment. The nanothread models build on hydrogen-terminated sp\(^3\) carbon motifs with Stone–Wales defects as controlled imperfections, isolating how topological defects modulate ultra-high mechanical performance predicted for ideal strands.

## Limitations

ReaxFF accuracy for strained sp\(^3\) carbon depends on the parameterization; loading rates in MD exceed experimental strain rates. Real synthesis produces polydisperse threads unlike ideal periodic models. Steered MD pulls may not map one-to-one to nanoindentation or AFM bending tests without additional calibration. Temperature control in experiment can anneal defects that MD treats as frozen topology.

## Relevance to group

Reactive carbon mechanics benchmark for nanothread allotropes in the corpus.

## Citations and evidence anchors

DOI `10.1021/nl5041012`.

## Related topics

- [[reaxff-family]]
- [[2015roman-venue-nl5041012]]
