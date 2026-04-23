---
id: paper:2025krstic-venue-paper
type: paper
title: "Hydrogen irradiation-driven computational surface chemistry of lithium oxide and hydroxide"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:oxides-ceramics
  - material:oxide
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0177460"
year: 2023
authors:
  - "P. S. Krstic"
  - "S. Dwivedi"
  - "E. T. Ostrowski"
  - "S. Abe"
  - "A. Maan"
  - "Adri C. T. van Duin"
  - "B. E. Koel"
venue: "J. Chem. Phys. 159, 244703 (2023)"
pdf_sha256: "dca6fdfc6e299b1cc71f7af10ec95f338f1737aa0226d74736f8205aaa2a1ef9"
pdf_path: "papers/Krstic_JCP_LiOH_2023.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025krstic-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Molecular dynamics** (including **NVE**-style **cascade** segments at stated **K**) study of **H atom impacts** on **crystalline and amorphous Li\(_2\)O / LiOH** surfaces motivated by **fusion** first-wall science where **lithium coatings** manage **hydrogen recycling** and impurity retention. The project uses **DFT-trained ReaxFF + EEM-style polarization** to follow bond-making chemistry as incident **H** stalls in collision cascades and engages resident **Li–O–H** moieties; comparisons reference **DFT relaxation** and **quantum–classical TB dynamics** excerpts in the abstract framing. Take-home: **polarization/explicit charge response** is important for faithful **Li–O–H** reactivity under irradiation, and product distributions depend sharply on **local stoichiometry** and **collisional geometry**. The introduction notes tokamak interest in **low-recycling** regimes where **Li** coatings retain **hydrogen** and reduce edge cooling, motivating **wall** chemistry models that resolve **retention** versus **reflection**.

## Methods

Reactive MD with **ReaxFF** potentials benchmarked against **DFT**; supplementary tight-binding / QM dynamics comparisons (per abstract); surface models spanning ordered vs disordered regions. Incident **H** is followed after **slowing** in a **collision cascade** and **retention** in **amorphous** near-surface **Li\(_2\)O** or **LiOH**, matching the abstract’s emphasis on **bonding** sequences rather than single-bounce scattering only. **Electronegativity equalization** (EEM) coupled to **ReaxFF** is used to capture **polar-covalent** character in **Li–O–H** environments. For **NPT** vs **NVE** **ensemble** choices, **time step** (fs), **ps**-scale **segment** **duration**, **thermostat**/**barostat** settings, and **PBC** **slab** **supercell** **stoichiometry**, the wiki defers to **`papers/Krstic_JCP_LiOH_2023.pdf`** (periodic **supercells** for **Li\(_2\)O** / **LiOH** **surfaces** with **3D** **PBC** as in the **JCP** **setup**; **temperature** **K** and **heating** **ramps** for any **thermostat**ed **stages** are listed there). **N/A** — static **E-field** in the **MD** **cell**; **N/A** — **umbrella** **sampling** / **metadynamics** as primary tools (per abstract emphasis on cascade MD).

## Findings

Chain reactions producing mixed **hydroxide/oxy** species emerge from sequential H uptake; emphasizes **sensitivity** to instantaneous atom positions and Li:O:H ratios in the near-surface region. The abstract stresses that **DFT** **minimizations** and **TB** **dynamics** corroborate the need for **polarization**-aware models for these **Li–O–H** systems, not only **pairwise** **Coulomb** treatments. Experimental touchstones cited in the paper include **H** retention differences between **Li** and **Li\(_2\)O** films and **oxygen** enrichment under high **D** fluence, motivating **multi-step** surface transformation scenarios. New numbers should be taken from the **JCP** **PDF**; **`extraction_quality: partial`** flags thin local **extract**s.

## Limitations

Plasma-facing conditions simplify to **atomic H bombardment**; extrapolation to full edge-plasma spectrum, molecular species, and magnetized transport requires multi-scale coupling not in the MD cell.

## Corpus artifacts

Some corpora register an **AIP eProof / galley** PDF for the same **DOI** (filename pattern `Krstic_JCP_LiOH_2023_galley`). Prefer **`papers/Krstic_JCP_LiOH_2023.pdf`** for **version-of-record** **pagination** and **figures**; proof PDFs are mainly **workflow** artifacts.

## Relevance to group

**Van Duin**-group **ReaxFF** for **extreme Li/H environments** parallels battery SEI work but targets **fusion materials** physics (**PPPL / Princeton** collaborators). Corpus slug `2025krstic-*` is a legacy mismatch; **publication year is 2023** per JCP metadata.

## Citations and evidence anchors

https://doi.org/10.1063/5.0177460 — J. Chem. Phys. **159**, 244703 (published online **28 Dec 2023**); Abstract states physics motivation and polarization emphasis.

## Related topics

- [[reaxff-family]]
- [[2022sengul-physical-che-atomistic-level]]
