---
id: paper:2020shin-venue-untitled
type: paper
title: "Development and Applications of the ReaxFF Reactive Force Field for Biological Systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:dft-static
  - keyword:nvt-simulation
  - keyword:reaxff-application
  - keyword:review-or-perspective
candidate_tags: []
source_refs: []
doi: ""
year: 2020
authors:
  - "Yun Kyung Shin"
  - "Chowdhury M. Ashraf"
  - "Adri C. T. van Duin"
venue: "Book chapter (Springer e-proof PDF)"
pdf_sha256: "a0d90567003f7ebd42707f07ca29230cfde53b9b9daf7de4ef0f94dbba376912"
pdf_path: "papers/Shin_Goddard_Chapter_Shin_Ashraf_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020shin-venue-untitled -->

Chapter-style overview of **ReaxFF** applications to **biological and biomolecular** problems, with emphasis on **parameterizations** aimed at **RNA/DNA chemistry**, **Zn–imidazole** protonation, and **peptide-bond hydrolysis** (including **Cu(II)** catalysis), illustrated with **reactive MD** case studies compared to **DFT** where reported.

## Summary

The text surveys how ReaxFF has been used for reactive processes in biochemistry: **phosphodiester cleavage** in RNA versus DNA (distinct mechanisms involving cyclic phosphate intermediates versus hydrolytic attack at phosphorus), **Zn(II)–ligand** energetics and **aqueous Zn–imidazole** dynamics including **pH-dependent protonation**, and **catalyzed vs uncatalyzed peptide hydrolysis** with analysis of **transition-state stabilization** by Cu(II). The overarching goal is to show **validation** against quantum data and the **feasibility of large-scale reactive MD** for enzymatically relevant chemistry.

## Methods

- **Scope:** Book-chapter review of **ReaxFF** for **RNA/DNA** cleavage, **Zn(II)-ligand** and **imidazole** protonation, and **Cu(II)-mediated peptide hydrolysis**, with **DFT** comparisons where cited.
- **QM / static ReaxFF:** **Potential-energy profiles** along **phosphodiester** cleavage paths for **RNA vs DNA** dinucleotides (with **0, 1**, or **liquid** water cases as plotted).
- **Reactive MD example (imidazole protonation):** **NVT** **MD** at **300 K** in a **~20 x 20 x 20 A** cell with **10** neutral **imidazole**, **20 HCl**, and **207 H2O**, replicated to a **3 x 3 x 3 supercell**; **Berendsen** thermostat (**100 fs** relaxation), **time step 0.1 fs**, **600 ps** production to track **imidazolium** formation at low pH.

## Findings

- ReaxFF reproduces a **specific RNA/DNA cleavage picture** from the literature: RNA cleavage via a **3′,5′-cyclic phosphate** intermediate giving **2′-OH,3′-phosphate** and **5′-OH** products; DNA cleavage by **water attack at phosphorus** when the **2′-OH** is absent, yielding **5′-OH** and nucleotide fragments.
- For **Zn(II)–ligand** systems, ReaxFF comparisons to prior **DFT** work cover **dissociation energies** and **proton affinities** across a set of **N-containing ligands** and **imidazole**; reactive MD of **Zn(Im)₂(H₂O)ₙ** in water illustrates **variable coordination numbers** from **dynamic** Zn(II) coordination.
- ReaxFF is argued to capture **pH-dependent imidazole protonation** via **barrier** analysis and **formation of imidazolium** under acidic conditions.
- For **peptide hydrolysis**, ReaxFF **potential energy profiles** along pathways for **Cu(II)-catalyzed** and **uncatalyzed** reactions show **strong TS stabilization** in the catalyzed case and **qualitative agreement** with **DFT**; the text highlights **imidazole** as a **proton shuttle** in **Ser–His–Asp**-type contexts.

## Limitations

The corpus PDF is a **publisher e-proof**; final pagination, figures, and any post-proof corrections follow the **published chapter**. Specific numerical barriers and simulation lengths should be verified against the **final book/chapter** PDF.

## Relevance to group

Direct **van Duin**–authored synthesis connecting **ReaxFF** to **biomolecular** reactivity and MD workflows.

## Citations and evidence anchors

Prefer the **published chapter** DOI or book citation once confirmed in library metadata; the wiki stub did not record a DOI.

## Related topics

- [[reaxff-family]]
