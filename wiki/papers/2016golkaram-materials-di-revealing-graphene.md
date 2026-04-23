---
id: paper:2016golkaram-materials-di-revealing-graphene
type: paper
title: "Revealing graphene oxide toxicity mechanisms: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.md.2015.10.001"
year: 2015
authors:
  - "M. Golkaram"
  - "Adri C. T. van Duin"
venue: "Mater. Discov."
pdf_sha256: "da50f2c92e47de28e96ee2f4a638f96be75f72b64311c866e2bf346586ec53ef"
pdf_path: "papers/Golkaram_MD_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016golkaram-materials-di-revealing-graphene -->

## Summary

**Graphene oxide (GO)** is widely used in biotechnology because its oxygen **functional groups** increase hydrophilicity, but cytotoxicity mechanisms remain debated experimentally. Golkaram and van Duin report **ReaxFF-based reactive molecular dynamics** of **GO** interacting with **peptide** models in **explicit water**, isolating **epoxide (–O–)**, **hydroxyl (–OH)**, and **carboxyl (–COOH)** motifs before combining them. The abstract frames the study as the authors’ **first atomistic-scale** examination of **GO toxicity chemistry**, emphasizing **bond-level** pathways (e.g. **reactive oxygen species**, **pH** shifts, **adhesion**) rather than a single scalar dose metric.

## Methods

**MD application (ReaxFF):** The authors build **separate systems** for each major **GO** functionalization (**epoxide**, **hydroxyl**, **carboxyl**) interacting with **peptide** segments in **explicit water**, then a **combined** model containing all groups (*Mater. Discov.* §2). **Reactive MD** with **ReaxFF** resolves **bond-making/breaking** at the **GO–peptide** interface on **fs**–**ps** timescales inside **3D PBC** supercells. **Ensemble:** **N/A — not stated on the indexed extract** (typical aqueous biomolecular segments use **NVT**-class control; confirm in PDF). **Barostat / bulk hydrostatic pressure:** **N/A — not the focus** of the interface chemistry models summarized from the abstract. **Timestep, thermostat type/damping, target temperature, total production time, and water/peptide stoichiometry:** **N/A — not transcribed from the short extract**; read **`papers/Golkaram_MD_2016.pdf`**.

**Force-field training:** **N/A — uses a published CHON ReaxFF** referenced in the article (headline is application, not refit).

**Static QM / DFT:** **N/A — not the primary method** in the summarized framing.

## Findings

The abstract states that **different chemical reactions** between **GO** and **peptides** can produce **reactive oxidative species** (**ROS**), drive **acidic or basic pH** conditions, and promote **cell-surface adhesion** (wording as printed in *Mater. Discov.*). It further reports **strong hydrogen bonding** together with stable **π–π stacking** between **GO** and peptide aromatics, with **stacking** implicated in **disruption of polypeptide secondary structure**. The **Methods** section (indexed text) adds that **epoxide** and **carboxyl** groups can **catalyze thiol (–CSH) deprotonation** and **aldehyde → carboxyl** conversion in the presence of **ROS**, whereas **hydroxyl** groups are tied primarily to **secondary-structure denaturation** and, through **H-bonds** to hydrophilic side chains, to **enhanced adhesion** (as discussed relative to prior experimental reports cited there). **Quantitative** rates, populations, and time-resolved product statistics are **figure-specific** and should be read from **`papers/Golkaram_MD_2016.pdf`**, not extrapolated from this note.

## Limitations

The study reduces biological complexity to **GO + peptide + water** supercells rather than full **membrane** or **cell** models; the abstract explicitly notes that **computational limitations** hinder larger **GO–protein** systems that would capture **tertiary** structure and **allosteric** effects. **GO** polydispersity and **in vivo corona** chemistry are not fully represented.

## Relevance to group

**Penn State / van Duin**-authored **ReaxFF** application extending reactive workflows to **nanomaterial–biointerface** questions.

## Citations and evidence anchors

- Journal header in `papers/Golkaram_MD_2016.pdf` lists *Materials Discovery* **1 (2015) 54–62**; **DOI:** [10.1016/j.md.2015.10.001](https://doi.org/10.1016/j.md.2015.10.001).

## Related topics

- [[reaxff-family]]
