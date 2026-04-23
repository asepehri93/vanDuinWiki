---
id: paper:2017hong-venue-microsoft-word
type: paper
title: "Supporting Information: Computational Synthesis of MoS2 Layers by RMD (Hong et al., Nano Letters 2017)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - material:tmd
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:supporting-information
  - keyword:2d-materials
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.7b01727"
year: 2017
authors:
  - "Sungwook Hong"
  - "Aravind Krishnamoorthy"
  - "Pankaj Rajak"
  - "Subodh Tiwari"
  - "Masaaki Misawa"
  - "Fuyuki Shimojo"
  - "Rajiv K. Kalia"
  - "Aiichiro Nakano"
  - "Priya Vashishta"
venue: "Nano Letters (Supporting Information PDF)"
pdf_sha256: "9454a2eec9c2429be2b48ca63aea43d350fef2db8e974fcfe7919d9f3f9febb9"
pdf_path: "papers/ReaxFF_others/Hong_MoS2_acs.nanolett_2017_SI.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2017hong-venue-microsoft-word -->

!!! note "Non-primary corpus PDF"

    This `pdf_path` is the **Supporting Information** PDF for Hong et al., *Nano Letters* 2017. The version-of-record letter text and reactive MD results on MoO3 sulfurization are documented under [[2017hong-venue-nl-2017-01727n]] (`papers/ReaxFF_others/Hong_MoS2_acs.nanolett_2017.pdf`). See the maintainer catalog [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) for how SI-first slugs are handled.

## Summary

The SI package documents reoptimization of a Mo/O/S ReaxFF description aimed at gas-phase MoOxSy intermediates and reactions during sulfurization of MoO3 surfaces toward MoS2, using MoO3 surfaces and sulfur-containing gas species in later CVD-style reactive MD. Initial parameters are taken from prior Mo/O and Mo/S ReaxFF work; the authors assemble a quantum training set of small clusters (up to 14 atoms), alpha- and beta-MoO3, and 2H/1T MoS2 crystal references, then refit bond, off-diagonal, and angle terms (including selected Al-O-Mo angles) with a weighted least-squares objective. The SI also records merge of sulfur parameters from Islam et al. and of Al/O parameters for alumina substrate models, with explicit caveats on branch transferability when combining combustion-branch Mo/O/S fits with water-branch Al/O data.

## Methods

**A — Force-field training / fitting:** **Mo/O/S ReaxFF** **reoptimization** via **weighted least squares** / **single-parameter parabolic search** on **QM** vs **ReaxFF** errors. Training includes **charges**, **structures**, **bond dissociation**, **angles**, **cluster cohesive energies**, **MoO\(_3\)** and **MoS\(_2\)** **equations of state**; weights emphasize **small gas-phase** **MoO\(_x\)S\(_y\)** clusters for **early sulfurization**. **Merges:** **S** from **Islam et al.**; **Al/O** for **Al\(_2\)O\(_3\)** substrates—**SI** warns **limited transferability** across branches when **Al/O** not co-refit to **Mo/O/S**.

**B — Molecular dynamics / sampling:** **Supporting Information** focuses on **parameterization**; **large-scale RMD** protocols for **MoO\(_3\)** **sulfurization** are documented on **[[2017hong-venue-nl-2017-01727n]]**.

**C — DFT / static QM:** **Clusters:** **Q-Chem**, **PBE** + **dispersion**, **6-31G\*\*** on **O/S**, **Hay–Watt ECP** on **Mo**, spin scanning. **Periodic:** **VASP** **PAW**, **MoS\(_2\)** **PBE** **400 eV** cutoff; **MoO\(_3\)** **vdW-DF2** **550 eV**; optimizations/**NEB** to **1e-5 eV/atom**, **5e-3 eV/Å** forces (SI).

**D — Review / non-simulation framing:** **SI** methods supplement for **Hong et al.** **Nano Lett.**—see primary letter for **scientific conclusions**.

**MD note.** Large-scale **RMD** production protocols for **MoO\(_3\)** **sulfurization** are documented on **[[2017hong-venue-nl-2017-01727n]]** and its **PDF**, not in this **SI**-first file. **QM training clusters** in this **SI** reach up to **14 atoms**, alongside **bulk** **MoO\(_3\)** and **MoS\(_2\)** **reference cells**. **Ensemble:** **NVT** (**Nosé–Hoover**) for **production RMD** is stated on the **primary letter** page; this **SI** does not re-list those decks. **Timestep / thermostat damping / duration / PBC / barostat / temperature / pressure / electric field / enhanced sampling** for **production RMD:** **N/A —** copy remaining knobs from **`[[2017hong-venue-nl-2017-01727n]]`** rather than this **parameterization** supplement.

## Findings

Mulliken charges from Q-Chem on small Mo/O/S clusters match the ReaxFF charge model closely enough that charge parameters are left unchanged during the bond and angle refit. Cohesive energies for listed clusters (e.g. MoO, MoS, MoO2, MoS2, MoO3, MoS3, MoO2S, MoOS2, and larger Mo2OxSy and Mo3OxSy stoichiometries) show typical errors of a few percent in Table S1, with intentionally higher accuracy for small clusters due to weighting. Bond dissociation and angle distortion data are reproduced at least qualitatively in Figures S3-S4 of the SI. The text stresses that only DFT data generated in this study enter the refit, so numerical agreement with ReaxFF results quoted in earlier references is not guaranteed after reoptimization. Merging Al/O and Mo/O/S lines risks poor bulk or surface descriptions for alumina unless validated, as noted in the SI narrative.

## Limitations

The SI is a methods supplement: reaction pathway and RMD synthesis conclusions belong to the primary letter page. Combined ReaxFF branches may fail outside the validated Mo/O/S and substrate test cases described here.

## Reader notes (navigation)

- [[2017hong-venue-nl-2017-01727n]] (primary Nano Letters article PDF in corpus)
- [[reaxff-family]]
