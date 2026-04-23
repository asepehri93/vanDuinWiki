---
id: paper:2017jejoon-yeon-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF force field for Cu/S/C/H and reactive MD simulations of methyl thiolate decomposition on Cu(100)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.7b06976"
year: 2017
authors:
  - "Jejoon Yeon"
  - "Heather L. Adams"
  - "Chad E. Junkermeier"
  - "Adri C. T. van Duin"
  - "Wilfred T. Tysoe"
  - "Ashlie Martini"
venue: "J. Phys. Chem. B"
pdf_sha256: "f8a35a32ee421caa2984debab920e39166a271254889a2d8bdec735468e7e84c"
pdf_path: "papers/Yeon_CuSCH_JPCB_2017.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:tribology
  - keyword:catalysis-surface
  - keyword:metallic-systems
---

<!-- id:paper:2017jejoon-yeon-j-phys-chem-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This Journal of Physical Chemistry B article develops a new ReaxFF parameterization for Cu/S/C/H chemistry to study methyl thiolate decomposition on Cu(100). The scientific motivation comes from surface-science experiments in which sliding on a methyl thiolate-covered copper surface in ultrahigh vacuum at room temperature accelerates decomposition, producing small gas-phase hydrocarbons and leaving sulfur on the surface, a process argued to be mechanochemical rather than thermally dominated under the stated mild sliding conditions. To enable atomistic simulation of these pathways, the authors fit ReaxFF parameters using density functional theory data for bulk copper sulfide phases, bond dissociation and angle bending involving Cu–S–C motifs, binding energies of SCH\(_3\), CH\(_3\), and S on copper, and potential energy curves for methyl thiolate decomposition on Cu(100). The collaboration spans UC Merced, UW–Milwaukee, Penn State (van Duin), and surface-science and tribology expertise (Tysoe; Martini).

## Methods

**A — Force-field training / fitting:** **ReaxFF** parameters optimized against **DFT** for **Cu/S/C/H**: **EOS** of **CuS**, **CuS\(_2\)**, **Cu\(_2\)S**; **Cu–S** dissociation; **Cu–S–C** angles; **adsorption** of **SCH\(_3\)**, **CH\(_3\)**, **S**; **methyl thiolate** decomposition paths on **Cu(100)**. **Software:** standalone **ReaxFF** fitter + **LAMMPS** for validation MD (per article/SI).

**B — Molecular dynamics / sampling:** **Reactive MD** of **adsorbed methyl thiolate** on **Cu(100)** at **elevated T** to compare **pathways**/**products** with **UHV** experiments. **Rare-event**/**Bell-type** mechanochemical context in text—numerical **timestep**, **ensemble**, **duration** in **SI**.

**C — DFT / static QM:** **Training** **QM** for **bulk sulfides**, **surfaces**, and **reaction** **PES** slices—functional/basis per **Methods** (see paper).

**D — Review / non-simulation framing:** **Primary** **JPCB** parameterization + **application**—not a literature review.

**Engine:** **LAMMPS** **ReaxFF** validation MD for **methyl thiolate** on **Cu(100)**. **System:** **Cu(100)** **slab** with **adsorbed** **CH\(_3\)S–** / decomposition products; **atom counts** and **supercell** repeats are in **article/SI**. **Ensemble:** **NVT** for the **elevated-temperature** **reactive MD** validation trajectories (confirm **NVE** segments, if any, in **SI**). **Timestep / thermostat / duration / PBC / barostat:** **N/A —** numerical inputs are **not** duplicated on this wiki page—copy from **`pdf_path`**. **Temperature:** **elevated T** (exact setpoints in **SI**). **Pressure:** **N/A —** **UHV**-style chemistry is discussed experimentally, but **MD** **barostat** targets are **not** summarized here. **Electric field:** **N/A —** not used in the summarized **MD** (mechanochemistry is contextual). **Replica / enhanced sampling:** **N/A —** not used.

## Findings

The reactive simulations identify C–S bond scission as the initiation step for methyl thiolate decomposition, consistent with the experimental picture emphasized in the abstract. After scission, methyl species diffuse on the surface and combine to desorb ethane, again matching experimental observations summarized in the article. The work is presented as a demonstration that the newly fitted ReaxFF potential can capture the methyl thiolate decomposition chemistry on Cu(100) sufficiently well to support further studies of mechanochemistry at copper–organosulfur interfaces.

The introduction further contrasts thermally driven extreme-pressure lubricant chemistry at very high interfacial temperatures with mild sliding conditions where tribofilm formation can be mechanochemically accelerated without appreciable temperature rise, using dialkyl disulfide chemistry on copper in ultrahigh vacuum as the experimental anchor for the methyl thiolate family. That framing motivates reactive MD not only as a barrier-fitting exercise but as a route toward molecular interpretations of parameters such as activation length in stress-biased rate models, while acknowledging oversimplifications of collinear force assumptions.

## Limitations

- Scope centers on **Cu(100)** **methyl thiolate** family chemistry; broader **additive** chemistry requires further validation.

## Relevance to group

Shows **van Duin** **ReaxFF** deployment for **organosulfur** **Cu** interfaces linking **surface science** and **tribochemistry**.

## Citations and evidence anchors

- **DOI:** [10.1021/acs.jpcb.7b06976](https://doi.org/10.1021/acs.jpcb.7b06976) (`papers/Yeon_CuSCH_JPCB_2017.pdf`).
- Text-aligned pointers: `normalized/extracts/2017jejoon-yeon-j-phys-chem-development-reaxff_p1-2.txt`

## Reader notes (navigation)

- Cu/S organosulfur tribochemistry alongside [[2016yeon-venue-la5b04062]]; [[reaxff-family]].

## Related topics

- [[reaxff-family]]
