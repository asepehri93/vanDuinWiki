---
id: paper:2016yeon-venue-research
type: paper
title: "Effects of water on tribochemical wear of silicon oxide interface: Molecular dynamics study with reactive force field (ReaxFF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.5b04062"
year: 2016
authors:
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Langmuir"
pdf_sha256: "6aa4134fd17775c8e6e41266f6cdb1159f82a0fde5aed255f71614da68ce9292"
pdf_path: "papers/Yeon_Langmuir_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yeon-venue-research -->

## Summary

This wiki slug registers a **proof / galley** PDF (`papers/Yeon_Langmuir_2016_proof.pdf`) for the Langmuir article on **ReaxFF molecular dynamics of tribochemical wear** at hydroxylated silica and oxidized silicon sliding contacts with variable interfacial water coverage. **`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`** lists several proof duplicates; here the **canonical version-of-record PDF** is curated as **`[[2016yeon-venue-la5b04062]]`** (`papers/Yeon_Langmuir_2016.pdf`), with an additional reduced-size variant **`[[2016yeon-venue-la5b04062-2]]`**. The scientific narrative is unchanged across these files: dry or water-lean contacts favor **Si–O–Si bridge-mediated** material transfer between surfaces, **submonolayer** water introduces additional reaction pathways, and a **full water monolayer** can suppress close contact and reduce transfer by separating surfaces. van Duin and Kim co-authorship places the work in the group’s tribochemistry line alongside allyl-alcohol polymerization studies. For MAS retrieval, treat this slug as **provenance metadata** tying a specific SHA-256 to a Langmuir DOI, while routing readers to the VOR page for copy-pasteable article text. Proof PDFs sometimes retain “For peer review only” banners or low-resolution figures even when the science matches the issue PDF.

## Methods

**Provenance.** `pdf_path` registers the **proof / Just Accepted layout** PDF (`papers/Yeon_Langmuir_2016_proof.pdf`). The **methods text** matches the **issue** article summarized on **`[[2016yeon-venue-la5b04062]]`**: **Engine / code:** **LAMMPS**; **ReaxFF** (**Fogarty Si/O/water**); **periodic** **3.19 × 3.19 × 7.0 nm\(^3\)** **slab-on-slab** **a-SiO\(_2\)** vs **oxidized Si(100)**; **ensemble:** **NVT**; **thermostat:** **Nose–Hoover**; **timestep:** **0.25 fs**; **normal load:** **1 GPa**; **shear:** **10 m/s** for **1 ns**; **interfacial water:** **0 / 20 / 50 / 100** molecules; **temperatures:** **300 / 500 / 700 K** variants.

**2 — Force-field training.** **N/A —** literature parametrization.

**3 — Static QM.** **N/A —** not used.

**4 — Replica / enhanced sampling.** **N/A —** not used.

## Findings

**Outcomes / mechanisms.** **`[[2016yeon-venue-la5b04062]]`** reports that **dry** **ReaxFF-MD** sliding produces **dehydroxylation → Si–O–Si bridge** sequences with **substantial atom transfer**, whereas **~monolayer** water **passivates** **Si** with **hydroxyls** and **suppresses** those **bridges** (**abstract**).

**Comparisons.** The **Introduction** links these atomistic trends to **AFM** wear vs **relative humidity**, including **non-monotonic** behavior when **multilayer water** keeps asperities apart.

**Sensitivity / levers.** **Water molecule count** (**20 / 50 / 100**) and **temperature** (**300 / 500 / 700 K**) modulate whether **dissociative** pathways dominate and how much **transfer** occurs during the **1 GPa** load.

**Limitations / outlook.** **Proof** PDFs can carry layout artifacts; quantitative **curves** should be taken from the **typeset** issue PDF or **SI** on the **VOR** slug.

**Corpus honesty.** Cite **figures/tables** from **`[[2016yeon-venue-la5b04062]]`**; **pagination** in this **proof** file may differ.
## Limitations

Proof PDF not ideal for pagination citations; prefer **`[[2016yeon-venue-la5b04062]]`**. ReaxFF cannot capture electronic friction or quantum effects in tribology. For machine-assisted retrieval, prefer linking `paper_id` metadata to the VOR slug so chunk hashes align with the article text consumers actually read. Automated exporters should surface the DOI from the VOR page, not from proof footers. Supporting Information for tribochemistry figures, when present, follows the main article’s supplementary record.

## Relevance to group

Duplicate ingest tracking for van Duin–Kim Langmuir tribochemistry; primary reader page is the VOR slug.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.langmuir.5b04062` (`papers/Yeon_Langmuir_2016_proof.pdf`).

## Related topics

- [[reaxff-family]]
- [[2016yeon-venue-la5b04062]]
