---
id: paper:2019mei-venue-paper
type: paper
title: "Effects of water on the mechanical properties of silica glass using molecular dynamics (Elsevier uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2019.07.049"
year: 2019
authors:
  - "Hai Mei"
  - "Yongjian Yang"
  - "Adri C. T. van Duin"
  - "Susan B. Sinnott"
  - "John C. Mauro"
  - "Lisheng Liu"
  - "Zhengyi Fu"
venue: "Acta Materialia (proof PDF)"
pdf_sha256: "4cffcb5e70cc523780d20444f4a70a664ced5eade2b90f7ccac1b4a8219494d1"
pdf_path: "papers/Mei_ActaMat_SiO2_MechanicalProperties_2019_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019mei-venue-paper -->

??? info "PDF variant"
    Elsevier **uncorrected proof**. Full LAMMPS/ReaxFF mechanical-testing narrative is on [[2019mei-acta-materia-effects-water]] with VOR PDF `papers/Mei_ActaMat_SiO2_MechanicalProperties_2019.pdf`.

## Summary

The proof PDF `papers/Mei_ActaMat_SiO2_MechanicalProperties_2019_proof.pdf` corresponds to **Acta Materialia** **178** (2019) 36–44, DOI `10.1016/j.actamat.2019.07.049` (“Effects of water on the mechanical properties of silica glass using molecular dynamics”). The extract begins with Elsevier proofing notices and then lists authors and affiliations (Wuhan University of Technology and Penn State units among them). The **abstract** states that understanding water’s effect on mechanical properties matters broadly for silicate glasses; that **molecular water** can **increase** Young’s modulus at **low** water content while **hydroxyl** has the **opposite** effect; that hydroxyls reduce **strength** and **fracture toughness** by disrupting network connectivity; and that molecular water undermines those properties by driving the silica network into a **strained configuration** even **without external stress**. It further ties water effects to changes in **Si–O bond length** and **Si–O–Si angle**, describes a **stress–strain plateau** under **compact tension** with molecular water as **Si–O bond breaking** followed by **silanol** formation, and notes molecular water **lowers the critical tensile stress** where the plateau appears.

## Methods

This **Elsevier** **uncorrected** **proof** **PDF** does **not** carry the **full** **Simulation** **details** **table** in the **short** **front** **pages** available in the local **extract**; the **version-of-record** **note** is on [[2019mei-acta-materia-effects-water]] with **PDF** `papers/Mei_ActaMat_SiO2_MechanicalProperties_2019.pdf`. In **summary** for **provenance** only: the **work** is **ReaxFF** **MD** in **LAMMPS** with the **Yeon** **Si/O/H** **set**, **0.5 fs** (glass **prep**) / **0.25 fs** (**later** **stages**), **NVT** **anneals** and **mechanical** **tests** on **hydrated** **silica** as in the **VOR** **article**—**copy** **all** **numerical** **MD** **lines** from the **VOR** **page**, **not** from this **proof** **slug** alone. **Specific** **atom** **counts**, **PBC** **edge** **lengths**, and **mechanical** **boundary** **conditions** for each **sample** **ID:** **N/A** on this **proof-ingest** **page**—**see** **VOR** **PDF** **§2**. **Barostat** during **mechanical** **holds:** **N/A** to specify here; follow the **VOR** article if **NPT** stages appear. **Thermostat** (NVT / mechanical coupling): **N/A** on the **proof** **excerpt**—reproduce **NVT** **thermostat** **settings** from [[2019mei-acta-materia-effects-water]] and the final **Acta** **PDF** **Methods**. **External electric field:** **N/A**.
## Findings

Abstract-level findings above are expanded with numerical moduli, toughness metrics, and structural analyses on [[2019mei-acta-materia-effects-water]] and in the final article PDF. The proof extract’s **keywords** line records “Water effect; Silicates; Cracking; Mechanical properties; Molecular dynamics,” which helps operators confirm manuscript identity. Stress–strain plateau behavior tied to Si–O bond breaking and silanol formation is described in the abstract for compact tension with molecular water present, with molecular water additionally lowering the critical tensile stress for the plateau; reproduce those curves from the VOR PDF when citing quantitative stress values. Copyeditor queries visible in the proof header (for example, author order markers Q3/Q4) reflect publisher workflow rather than physical conclusions.

## Limitations

Uncorrected proofs can differ from the XML version in minor wording or figure placement. Cite the DOI and read the VOR PDF for authoritative pagination.

## Relevance to group

Penn State–led collaboration (van Duin, Sinnott, Mauro, Liu) on water in silica mechanics with ReaxFF.

## Reader notes (navigation)

- [[2019mei-acta-materia-effects-water]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1016/j.actamat.2019.07.049](https://doi.org/10.1016/j.actamat.2019.07.049)
