---
id: paper:2015golkaram-materials-di-revealing-graphene
type: paper
title: "Revealing graphene oxide toxicity mechanisms: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reactive-md-generic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:lammps
source_refs: []
doi: "10.1016/j.md.2015.10.001"
year: 2015
authors:
  - "M. Golkaram"
  - "Adri C.T. van Duin"
venue: "Materials Discovery (uncorrected proof; DOI as in bibliography stub)"
pdf_sha256: "7f36b5663a237084bb0ccc31f2b9c2c7b7b485fbf3fda5e449977d981dc19755"
pdf_path: "papers/Golkaram_MD_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015golkaram-materials-di-revealing-graphene -->

## Summary

**Golkaram** and **van Duin** report **ReaxFF-based reactive MD** simulations aimed at **atomistic mechanisms** by which **graphene oxide (GO)** functional groups interact with a **model peptide helix**, interpreted as proxies for biocompatibility/toxicity-relevant chemistry (DOI **10.1016/j.md.2015.10.001**). The study progresses from **isolated functional-group** motifs (**epoxide**, **hydroxyl**, **carboxyl**) to a **combined** GO model, then examines **adhesion**, **secondary-structure disruption**, and **solution acidification** metrics discussed in the article.

## Methods

### MD application (atomistic dynamics)

Simulations use **ReaxFF reactive MD** (article text). A **12-residue α-helix** serves as a compact peptide proxy, with a **mutated sequence** (**A…W → …G** substitution in Methods) to show trends are not sequence-unique. **Graphene** sheets in a **~29.56 Å × 34.16 Å** periodic **supercell** host oxygenated motifs at **C₉₆O₇**, **C₉₆(OH)₇**, **C₉₆(COOH)₇**, and **combined** layouts; explicit **water** plus peptide yields **thousands of atoms** in the largest cells (exact **atom** counts in the **PDF**). Peptides start **~3 Å** from the surface. After **1 K** minimization and equilibration (Methods), production **NVT** runs use **Verlet** integration, **0.1 fs** timestep, **200 ps** segments, and a **Berendsen thermostat** (**100 fs** damping) per the **uncorrected proof** text. **Engine (LAMMPS vs ADF):** **N/A —** not spelled out in the proof excerpt used here; confirm in the **version-of-record** PDF if package identification is required. **External stress loading / hydrostatic pressure:** **N/A —** not part of this constant-volume peptide–GO protocol.

### Force-field training

**N/A —** applies **ReaxFF**; parameter lineage is described via citations in the article rather than as a new parameterization performed in this manuscript.

### Static QM / DFT

**N/A for the main MD trajectories** — the discussion cites **DFT** mainly as supporting context for **H-bond energetics** comparisons where noted in the article.

## Findings

**Epoxide** motifs can promote **water attack** that yields **hydroxyl** pairs on the sheet; the narrative links such chemistry to **ROS-prone** scenarios discussed relative to biophysical **oxidation** literature. **Carboxyl**-rich patches can **acidify** the local environment, **protonate** acidic residues such as **Asp**, and engage **Cys** **thiol** chemistry (including **disulfide-related** disruption) as illustrated in figures. The **combined** GO model discusses **competition or cooperation** between **epoxide** and **carboxyl** groups in **adhesion**, **loss of secondary structure**, and **pH drift** metrics reported in the article. **Sensitivity** to functional-group density is intentionally high to magnify signals—a **limitation** for quantitative dosimetry versus polydisperse **experiment**. **Corpus honesty:** this repo’s **proof PDF** may differ from the final **Materials Discovery** layout; cite the **PDF** for numbers.

## Limitations

The local corpus file is an **uncorrected proof PDF**; prefer the **final *Materials Discovery*** PDF for pagination/wording. Functional-group densities are intentionally **high/exaggerated** to magnify signals, so quantitative dosimetry should not be extrapolated linearly to dilute, polydisperse GO samples without additional modeling.

## Relevance to group

**Adri C. T. van Duin** co-authors a **reactive MD** contribution on **graphene oxide** biointerface chemistry in *Materials Discovery*, consistent with the group’s broader **nanocarbon** and **ReaxFF** application portfolio.

## Citations and evidence anchors

- DOI (from normalized bibliography): [https://doi.org/10.1016/j.md.2015.10.001](https://doi.org/10.1016/j.md.2015.10.001)

## Related topics

- [[reaxff-family]]
