---
id: paper:2015psofogiannakis-venue-paper
type: paper
title: "Development of a ReaxFF reactive force field for Si/Ge/H systems (uncorrected proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:widegap-semiconductor
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:qm-training-data
  - keyword:catalysis-surface
source_refs: []
doi: "10.1016/j.susc.2015.08.019"
year: 2015
authors:
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Surface Science"
pdf_sha256: "0074d78785d02d359e9fe3b45773ae8e3490810c33ea431d31ea18a215834862"
pdf_path: "papers/Psofogiannakis_SUSC_SiGeH_2015_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2015psofogiannakis-venue-paper -->

!!! abstract "Corpus PDF role"
    **Uncorrected proof** PDF (Elsevier header). The **version-of-record** PDF and primary curation: **[[2015psofogiannakis-surface-scie-development-reaxff]]**.

## Summary

**Plasma processing** of **group-IV** semiconductors is a classic **surface-science** testbed for **reactive** force fields because **H** **flux**, **energy**, and **coverage** can be bracketed more cleanly than in many **wet-chemistry** interfaces. **Silicon** and **germanium** **(100)** surfaces in **hydrogen plasmas** undergo **etching**, **hydrogenation**, and **amorphization** pathways that depend sensitively on **elemental** **bond strengths** and **lattice openness**. Building on the established **Si/H ReaxFF** description, this paper introduces **Ge–Ge**, **Si–Ge**, and **Ge–H** parameters by fitting **differences** relative to **Si** analogs using **Jaguar** **B3LYP**/**LAV3P\*\*** cluster data—mirroring the original **Si/H** training philosophy. The resulting **Si/Ge/H** field is exercised in **NVT** **MD** simulations of **monoenergetic atomic hydrogen** **bombardment** of **diamond-cubic** **Si(100)**, **Ge(100)**, and **SiGe(100)** slabs across a scan of **incident kinetic energies**, comparing **sticking**, **penetration**, and **surface disordering** trends.

## Methods

### Force-field training

This proof tracks the same training protocol curated in **[[2015psofogiannakis-surface-scie-development-reaxff]]**. The parent model is the existing **Si/H ReaxFF** parameterization, and the extension introduces **Ge-Ge**, **Si-Ge**, and **Ge-H** terms. The reported quantum reference layer is **Jaguar DFT** with **B3LYP/LAV3P\*\***. The training set is organized around bond dissociation and angular distortions chosen to isolate how Ge chemistry deviates from Si analogs, then folded into a difference-fitting workflow so the legacy Si/H behavior remains stable while Ge interactions are activated. The paper positions this transfer-style fitting as necessary for alloy and mixed-surface use, where compatibility with prior Si/H studies matters as much as reproducing new Ge targets.

### MD application (atomistic dynamics)

The application stage is reactive **LAMMPS** MD for monoenergetic atomic-H bombardment of **Si(100)**, **Ge(100)**, and **SiGe(100)** slabs, with periodicity in-plane and vacuum along the surface normal. The production setup is an **NVT slab protocol** with explicit equilibration and bombardment stages, tuned to compare element and composition effects under matched impact conditions rather than to emulate a complete plasma reactor.

For this non-primary proof copy, detailed values such as exact atom counts, timestep, thermostat damping, substrate temperature schedule, and incident-energy grid should be taken from the version-of-record sibling page because pagination and copy-edit details can differ between proof and final publication.

- Engine/code: LAMMPS with Si/Ge/H ReaxFF.
- System size/composition: crystalline Si, Ge, and SiGe (100) slabs; exact repeats and atom totals are reported in the VOR article.
- Boundaries: in-plane periodic boundaries with vacuum normal to surface.
- Ensemble: NVT.
- Timestep: stated in the article; not reproduced numerically on this proof page.
- Duration/staging: equilibration plus bombardment windows; exact lengths in VOR.
- Thermostat: active during NVT windows; coupling constants in VOR methods.
- Barostat: N/A for constant-volume slab impacts.
- Temperature: controlled in NVT protocol; exact setpoints in VOR.
- Pressure control: N/A.
- Electric field: N/A.
- Enhanced sampling/replicas: N/A.

**Barostat / NPT pressure:** **N/A —** constant-volume **slab** impacts.

**Electric field / metadynamics:** **N/A**.

## Findings

The cross-material comparison is the central result: under the same atomic-H bombardment framing, **Si(100)** is reported as more reactive toward hydrogen uptake and etch-related evolution than **Ge(100)**, while **SiGe(100)** sits between those endpoints and shows alloy-specific disordering behavior that changes later hydrogen response. The mechanistic interpretation follows bond-strength and lattice-structure differences discussed in the paper.

The study also emphasizes sensitivity to control knobs, especially incident kinetic energy and substrate composition. In practical terms, that means the same ReaxFF model predicts different balances among surface hydrogenation, penetration, and disorder depending on energy window and whether the top layer is Si-rich, Ge-rich, or mixed.

Where comparison to electronic-structure expectations is offered in the publication, it is used as a plausibility check rather than a claim that all channels are DFT-equivalent. This is consistent with the paper's role: extending a transferable reactive model for plasma-surface trends, not replacing higher-level methods for every rare event.

## Limitations

The bombardment protocol uses monoatomic hydrogen projectiles, which intentionally simplifies real plasma exposure (mixed species, charge states, broad distributions). That design supports controlled model comparison but narrows direct process realism.

This file is an uncorrected proof PDF ingestion. For stable pagination, final figure/table numbering, and definitive wording, use the version-of-record page **[[2015psofogiannakis-surface-scie-development-reaxff]]**. Corpus-honesty note: this page preserves provenance for the proof artifact while deferring citation-critical details to the VOR sibling.

## Reader notes (navigation)

- Version-of-record page: **[[2015psofogiannakis-surface-scie-development-reaxff]]**
- [[reaxff-family]]
