---
id: paper:2014paupitz-venue-rsc-cp
type: paper
title: "Fullerenes generated from porous structures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - material:hexagonal-boron-nitride
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP03529A"
year: 2014
authors:
  - "Ricardo Paupitz"
  - "Chad E. Junkermeier"
  - "Adri C. T. van Duin"
  - "Paulo S. Branicio"
venue: "Phys. Chem. Chem. Phys. 16, 25515–25522 (2014)"
pdf_sha256: "47e0c7eaa57c4c01c6f02dfa8cf5785037abdd744315246b1955ffbf7db6c36a"
pdf_path: "papers/Paupitz_PCCP_2014_Fullerenes_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014paupitz-venue-rsc-cp -->

??? info "PDF variant"
    RSC **author proof** for DOI `10.1039/C4CP03529A`. The corpus `normalized/extracts/2014paupitz-venue-rsc-cp_p1-2.txt` is proof boilerplate. Scientific text and figures appear in the typeset PDF on [[2014paupitz-physical-che-fullerenes-generated]].

## Summary

The file `papers/Paupitz_PCCP_2014_Fullerenes_proof.pdf` is the RSC **author proof** for Phys. Chem. Chem. Phys. DOI `10.1039/C4CP03529A` (Paupitz et al., “Fullerenes generated from porous structures”). The Paupitz et al. PCCP paper investigates giant fullerene-like macromolecules built from porous graphene and biphenylene-carbon motifs, including hexagonal boron nitride analogues, using density functional-based tight-binding methods and reactive molecular dynamics. The automated extract (`normalized/extracts/2014paupitz-venue-rsc-cp_p1-2.txt`) begins with proof boilerplate and editor queries, but it also preserves the **graphical abstract** lead lines: “Structural and electronic properties of macromolecules, which have the architecture of fullerenes, were studied using reactive and density functional-based methods,” attributed to Ricardo Paupitz, Chad E. Junkermeier, Adri C. T. van Duin, and Paulo S. Branicio. The abstract reproduced on the typeset article page states that calculations predict stability up to about 2500 K for selected candidates, reports atomization energies of carbon structures between 0.45 eV per atom and 12.11 eV per atom relative to C₆₀, and gives BN analogues between −0.17 eV per atom and 12.01 eV per atom relative to B₁₂N₁₂, and argues that high porosity may suit gas storage or molecular encapsulation. Readers should use [[2014paupitz-physical-che-fullerenes-generated]] for clean typography, SI links, and continuous article text.

## Methods

DFTB-class and reactive MD protocols for porous fullerene-like carbon and BN architectures appear in the full article (`Phys. Chem. Chem. Phys.`, 2014, 16, 25515–25522). The proof extract on file does not substitute for those sections; it instead instructs authors to e-mail corrections to pccp@rsc.org within 48 hours, to check tabulated material and references carefully, and to note typographic conventions (for example, italic vee versus Greek nu). Consult [[2014paupitz-physical-che-fullerenes-generated]] and the article PDF for annealing schedules, potentials, and analysis. Editor queries recorded in the extract include early citation format with DOI `10.1039/c4cp03529a`, author-name spelling checks, and a cross-reference note about “Hultman” versus “Hulman” in a reference—metadata useful for operators verifying the correct manuscript revision.

### 1 — MD application (atomistic dynamics)

**N/A — reproducible MD protocol** is not recoverable from `normalized/extracts/2014paupitz-venue-rsc-cp_p1-2.txt` (proof boilerplate). Use **`[[2014paupitz-physical-che-fullerenes-generated]]`** for **ReaxFF**/**DFTB** simulation details.

- **Engine / code:** **Molecular dynamics** appears in the graphical-abstract lead lines preserved in the proof extract, but **N/A — software/timestep** not specified here.
- **System size & composition:** **N/A — atom counts / supercell** stoichiometry not stated in the proof boilerplate excerpt (see typeset article PDF on the sibling page).
- **Boundaries / periodicity:** **N/A — PBC** vs isolated **cluster** handling not stated in the proof excerpt; expect standard **3D PBC** for bulk-like cages only after reading the **VOR** **PDF**.
- **Ensemble:** **N/A — NVT**/**NPT**/**NVE** choice not stated in the proof excerpt—confirm on **`[[2014paupitz-physical-che-fullerenes-generated]]`**.
- **Timestep / duration / thermostat / barostat / temperature / pressure / electric field / enhanced sampling:** **N/A — proof-only excerpt** on this slug.

### 2 — Force-field training

**N/A —** not a parameter-file ingest; routing readers to the **typeset** article for training content.

## Findings

### Corpus honesty and sibling routing

Quantitative **atomization energy** ranges, **~2500 K** stability language, and porosity arguments are stated in the **typeset** abstract on **`[[2014paupitz-physical-che-fullerenes-generated]]`**; this **proof** slug should be treated as **manifest**/**PDF-variant** documentation only.

### Mechanisms and comparisons (typeset article)

The **typeset** introduction (summarized on the sibling page) situates **porous graphene** and **biphenylene-carbon** motifs alongside **BN** analogues, noting that geometric similarity between **graphene** and **hBN** does not imply similar **electronic structure**—motivating joint **carbon**/**BN** **fullerene**-like candidates in one study.

## Limitations

Proof PDFs can show editorial queries and differ in layout from the final issue. Prefer the VOR PDF for citation locators.

## Relevance to group

Van Duin co-authored study on porous nanocarbon and BN fullerene analogues with ReaxFF-class modeling.

## Reader notes (navigation)

- [[2014paupitz-physical-che-fullerenes-generated]]
- [[graphene-nanocarbon]]
- [[reaxff-family]]

## Citations and evidence anchors

https://doi.org/10.1039/C4CP03529A
