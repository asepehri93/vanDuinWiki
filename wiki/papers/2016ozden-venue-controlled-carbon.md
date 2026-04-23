---
id: paper:2016ozden-venue-controlled-carbon
type: paper
title: "Controlled 3D carbon nanotube structures by plasma welding"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:validation-experiment
  - keyword:classical-ff
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1002/admi.201500755"
year: 2016
authors:
  - "Sehmus Ozden"
  - "Gustavo Brunetto"
  - "N. S. Karthiselva"
  - "Douglas S. Galvão"
  - "Ajit Roy"
  - "Srinivasa R. Bakshi"
  - "Chandra S. Tiwary"
  - "Pulickel M. Ajayan"
venue: "Adv. Mater. Interfaces 2016, 3, 1500755"
pdf_sha256: "da3d7ec06ad03feef659e3477c8a0e3de7a26218bf9c0aced5dad64e9ea754a6"
pdf_path: "papers/ReaxFF_others/Ozden_et_al-2016-Advanced_Materials_Interfaces.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016ozden-venue-controlled-carbon -->

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

This Advanced Materials Interfaces communication reports bulk three-dimensional architectures built from multi-walled carbon nanotube powders consolidated by spark plasma sintering, a method that applies pulsed direct current and uniaxial pressure simultaneously to achieve rapid densification through joule heating, plastic deformation, and localized spark or plasma effects. The authors position the work against a diverse prior literature in which SPS of nanocarbons has produced outcomes ranging from retention of tubular morphology through partial conversion to graphene-like networks to extreme cases such as diamond formation under intense temperature and pressure. The present study emphasizes systematic variation of processing temperature and hold time within a window the authors argue had not been explored in the same structured way for bulk interconnected CNT solids, coupled with detailed Raman spectroscopy and electron microscopy of the starting powder and processed blocks. Complementary molecular dynamics simulations of nanotube welding at contacts are presented to support a microscopic picture of interconnection.

## Methods

**Experiments (SPS).** Multi-walled carbon nanotube powder is consolidated by **spark plasma sintering (SPS)** at **1000**, **1200**, and **1400 °C** with hold times **5**, **15**, and **30 min**, producing different compaction levels. During sintering, the authors report an **uniaxial pressure of 50 MPa** applied at **peak temperatures** (experimental protocol per the article). **Visual inspection** shows **compact blocks** without **macroscopic voids or cracks** for the illustrated conditions. **Raman** spectroscopy and **SEM/TEM** characterize starting powder and processed blocks; **Supporting Information** holds additional micrographs and spectra.

**Atomistic simulations (MD).** Reactive MD uses **ReaxFF** via the **Reax/c** implementation in **LAMMPS** to mimic localized **Joule-like heating** between neighboring tubes: kinetic energy is injected as a **non-translational “heat”** flux into a **10 Å** source region at one tube extremity, scanning fluxes from **0.0** up to **5.4 kcal mol\(^{-1}\) fs\(^{-1}\)** in the protocol description (individual figure panels quote intermediate values such as **1.0**, **4.1**, **4.3**, and **5.4 kcal mol\(^{-1}\) fs\(^{-1}\)**). Energy is deposited over **20 ps**; a **10 Å** **Nosé–Hoover**-thermostatted **heat drain** at the opposite extremity dissipates heat to emulate bundle dissipation paths. The MD section compares simulated junction morphologies and temperatures (including **~800 K** and **~1200 K** regimes in the published examples) to **HRTEM** of welded tips. **N/A — integration timestep** — not stated in the main communication text extracted here (check Supporting Information if reproducing inputs). **N/A — barostat-driven bulk pressure control for the welding cells** — the welding study is a localized heating/drain protocol rather than the macroscopic **50 MPa** SPS boundary value. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not reported for these welding trajectories.

**Force-field training.** **N/A —** the article applies literature **ReaxFF** parameters for carbon chemistry rather than reporting a new fit.

**Static QM.** **N/A —** DFT-level training of ReaxFF parameters is referenced generically, but the paper is not a standalone static-QM materials study.

## Findings

The introduction synthesizes literature results showing strong temperature- and pressure-dependent microstructure and property evolution for SPS-compacted CNT and graphene nanoplatelet systems, including mechanical properties and thermal conductivity trends that can be dominated by tube–tube interfacial resistance when tubular character survives. For the authors’ own 1000–1400 °C processing series, they correlate processing conditions with interconnected three-dimensional morphology and with spectroscopic signatures that distinguish structural damage from bonding between tubes. The molecular dynamics component is used to interpret inter-tube welding at contacts in the consolidated architectures; numerical performance metrics appear in the article’s figures and tables. The communication is experimental and computational process science rather than a ReaxFF methods benchmark, but it provides context for how extreme consolidation routes modify nanocarbon connectivity relevant to materials modeling elsewhere in the corpus.

The introduction frames joining strategies for three-dimensional nanocarbon networks in terms of covalent interconnections versus weaker van der Waals or π–π contacts, and it highlights prior demonstrations of metallic or ceramic additives and catalyst-assisted growth as alternative routes, situating SPS as a scalable consolidation approach where joule heating and spark-plasma effects can bond tubes across a wide temperature–pressure landscape.

## Limitations

The welding MD is a stylized two-tube heating experiment, not a direct atomistic replica of full **SPS** pressure–temperature cycles. Quantitative mechanical and transport properties of bulk blocks should be taken from the experimental figures/tables and SI rather than inferred from the illustrative simulations alone.

## Relevance to group

Experimental nanocarbon processing context adjacent to MD studies of carbon materials; not a ReaxFF methods paper.

## Citations and evidence anchors

- DOI: [10.1002/admi.201500755](https://doi.org/10.1002/admi.201500755)
- Text-aligned pointers: `normalized/extracts/2016ozden-venue-controlled-carbon_p1-2.txt`

## Reader notes (navigation)

- Carbon processing context: [[graphene-nanocarbon]], [[theme-2d-epitaxy-growth]]; contrast with reactive MD benchmarks such as [[2016tomas-carbon-109-2-graphitization-amorphous]].

## Related topics

- [[graphene-nanocarbon]]
