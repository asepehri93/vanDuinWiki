---
id: paper:2016ramirez-gonzalez-venue-paper
type: paper
title: "Supplementary information: Carbon-based tribofilms from friction- and pressure-induced synthesis (Nature 2016)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - method:reaxff
  - material:metal-surface
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:reaxff-application
  - keyword:supporting-information
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1038/nature18948"
year: 2016
authors: []
venue: "Nature 2016 (Supporting Information PDF in corpus)"
pdf_sha256: "87a438d16b9723fa703ccb5b8c5ae2ba0d2e881144281df81481ac6e97e0cfd7"
pdf_path: "papers/ReaxFF_others/Erdemir_Nature2016_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2016ramirez-gonzalez-venue-paper -->

## Summary

This corpus entry registers the **Supporting Information (SI)** PDF associated with the **Nature** article on **carbon-based tribofilms** formed under tribological stress (**DOI `10.1038/nature18948`**). The SI is not a standalone scientific narrative: it expands **experimental** tribology protocols, **materials synthesis** details for coatings, and **computational** workflows that complement the main text. According to the SI table of contents, the package includes magnetron sputtering and characterization of **MoN\(_x\)–Cu** nanocomposite coatings, **ball-on-disk** friction and wear testing in **PAO** oil, electron microscopy of films and tribofilms, and extensive **computational** sections covering **reactive force-field validation**, **ab initio molecular dynamics**, and **reactive MD** analyses of tribochemical bonding on **metal** surfaces. This wiki page exists so the SI PDF remains discoverable and citable within the knowledge base while steering interpretive claims to the **primary article**.

## Methods

This corpus PDF is the **Supporting Information** for the **Nature** article **DOI [10.1038/nature18948](https://doi.org/10.1038/nature18948)** on **carbon-based tribofilms** formed under tribological contact. Per the SI organization, it documents **experimental** materials and testing—**magnetron sputtering** of **MoN\(_x\)–Cu** nanocomposite coatings, **ball-on-disk** friction and wear in **PAO** oil, and **electron microscopy** of films and tribofilms—and **computational** appendices including **ReaxFF** validation, **ab initio molecular dynamics**, and **reactive MD** workflows for **tribochemical** evolution on **metal** surfaces. **Line-item MD/AIMD protocol** (engine, cell sizes and stoichiometry, **PBC**, ensemble, timestep, run lengths, thermostat/barostat, temperature and pressure, shear or tribological driving, electrostatics, and any enhanced sampling) is **N/A —** not transcribed here; it appears in **SI tables and figure captions** in **`pdf_path`**.

**Force-field training.** **N/A —** the SI supports **validation** and **application** of **ReaxFF** in the parent study’s workflow, not a new public fit documented on this page.

**Static QM / DFT.** **QM settings** for AIMD/DFT benchmarks are **N/A —** not tabulated in this wiki note; read the SI and main letter.

**Reviews.** **N/A —** this is **supplementary** material, not a literature review.

**MD protocol indexing (SI):** **Molecular dynamics**, **AIMD**, and **reactive MD** segments in the SI use **LAMMPS** or other engines, **supercell** models with **PBC**, and typically **NVT**/**NPT** staging with stated **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** control, and **temperature** (K) as tabulated in **`pdf_path`**. Line-by-line transcription is **N/A —** on this pointer page. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** workflows are **N/A —** unless the SI explicitly uses them.

## Findings

**Outcomes.** Headline **tribofilm** chemistry, **friction**, and **wear** conclusions belong to the **version-of-record Nature article**; the SI provides **supporting** experimental detail and computational inputs.

Compared to the main letter, the SI foregrounds reproducibility (methods, tables, computational appendices) rather than new headline mechanisms. **Limitations** of using an SI-only ingest include missing publisher-byline metadata in frontmatter. **Future work** belongs to the **Nature** article’s outlook.

## Limitations

**SI-only** ingest: always pair with the **version-of-record article** for conclusions; author list may be incomplete in frontmatter because the SI PDF metadata differs from the article byline.

## Relevance to group

High-impact **tribochemistry** package with **ReaxFF** validation and **reactive MD** workflows on **metal–lubricant** interfaces, relevant to materials mechanics threads in the corpus.

## Citations and evidence anchors

- Article DOI: [10.1038/nature18948](https://doi.org/10.1038/nature18948)

## Related topics

- [[reaxff-family]]
