---
id: paper:2008palaria-venue-paper
type: paper
title: "Structures and energetics of silicon nanotubes from molecular dynamics and density functional theory"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:qm-training-data
  - keyword:enhanced-sampling
canonical_tags:
  - domain:methods-software
  - material:widegap-semiconductor
  - method:dft-static
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.78.205315"
year: 2008
authors:
  - "Amritanshu Palaria"
  - "Gerhard Klimeck"
  - "Alejandro Strachan"
venue: "Physical Review B 78, 205315 (2008)"
pdf_sha256: "3c853e0904e59f5ca23e7a0ca1ade47962d78fcc7c8fd00fa2b907a97811d831"
pdf_path: "papers/ReaxFF_others/Palaria_Klimeck_Strachan_PRB2008_Structures and energetics of silicon nanotubes from molecular dynamics and density functional theory.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2008palaria-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Numeric ranges for cohesive energies and Young’s moduli are taken from the **abstract** as printed (eV and GPa).

## Summary

The authors combine **ReaxFF molecular dynamics** (annealing with cyclic mechanical loading) with **DFT GGA** relaxation (SEQQUEST; cross-checks with ABINIT noted) to predict **low-energy hollow Si nanotube** structures near **~1 nm** outer diameter. The abstract reports similar cohesive energies for the four most stable tubes (**0.638–0.697 eV/atom above bulk Si**) but **widely varying Young’s moduli** (**72–123 GPa**). The workflow uses ReaxFF to explore configuration space, then DFT to refine low-lying candidates.

## Methods


The workflow couples **ReaxFF molecular dynamics** for global exploration with **density-functional theory** for local refinement. Trial single-walled silicon nanotubes are built from stacked pentagonal or hexagonal rings (5, 6, 10, 11, or 12 rows) to vary periodicity. Annealing uses ReaxFF MD with **cyclic compressive/expansive loading** at **300 K** and **600 K**; for each initial topology and temperature the authors apply three strain-amplitude ranges (\(-37.50\%\) to \(-12.50\%\), \(-25.00\%\) to \(-8.30\%\), and \(-20.87\%\) to \(-4.17\%\)) and three strain rates (0.04167, 0.41667, and 0.83333% ps\(^{-1}\)), yielding trajectory lengths from about **0.2 to 2.7 ns** depending on case—explicitly noted as beyond practical **ab initio MD** reach for this search. **N/A —** MD **integration package**, **timestep**, **thermostat/barostat algorithm**, and **full PBC/stress-control statement** are not recovered from `normalized/extracts/2008palaria-venue-paper_p1-2.txt` (verify `pdf_path`).

**DFT refinement (static QM).** Promising ReaxFF structures are relaxed with **DFT-GGA** using **SEQQUEST** (local orbital basis, norm-conserving pseudopotentials) with **two \(k\)-points** along the tube axis; selected structures are cross-checked with **ABINIT** using a **12 hartree** plane-wave cutoff, **Troullier–Martins** norm-conserving pseudopotentials, and the same \(k\)-point sampling.

**2 — Force-field training.** ReaxFF is used as a **published, QM-trained reactive potential** for Si (including bond breaking); **N/A —** this excerpt does not restate the original ReaxFF parametrization protocol for Si—see the ReaxFF Si primary literature cited in the article.

**Checklist closure (indexed pages).** **System / composition:** **Si** nanotube trial **structures** with variable ring-row **stoichiometry** / periodicity as described above (**atom** counts for each case: verify **`pdf_path`** tables). **Ensemble:** **N/A — NVT**/**NPT**/**NVE** not stated for the ReaxFF annealing MD in the short extract. **Pressure / stress:** cyclic **strain** ranges are specified, but **N/A — hydrostatic pressure** target for MD is not stated on pp. 1–2.

## Findings

**Outcomes.** The search finds **hollow**, **low-symmetry** Si nanotubes with external diameters near **~1 nm** that are reported as the **most stable small-diameter** structures in their survey, with properties **very different from bulk** Si in the abstract’s framing.

**Comparisons and mechanical spread.** The **four** most stable tubes reported share similar **cohesive energies** (**0.638–0.697 eV/atom** above **bulk Si**) but **disparate Young’s moduli** (**72–123 GPa**), showing that **elastic stiffness** can vary strongly even when **relative stability** is similar.

**Context vs prior proposals.** The introduction contrasts this **MD+DFT** construction route with earlier **intuition-based** Si nanotube proposals that can sit **high in energy**—the computational approach is presented as a way to avoid guessing metastable topologies.

**Corpus honesty.** `extraction_quality` is **partial**; elastic tensors, additional figures, and any extended discussion beyond the indexed pages live in the **Phys. Rev. B** PDF at `pdf_path`.

## Limitations

`extraction_quality` is **partial**; rely on **Phys. Rev. B** for final numbers and figures.
- DFT kinetics and electronic properties are outside the core structural/energetic/elastic focus stated in the abstract.

## Relevance to group

Demonstrates **ReaxFF + DFT** hybrid workflow for **covalent nanostructures**—methodologically adjacent to reactive nanocarbon/silicon studies in the broader corpus.

## Citations and evidence anchors

- DOI: `10.1103/PhysRevB.78.205315`.
- PDF path as in manifest (filename contains full title).
- Extract: `normalized/extracts/2008palaria-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
