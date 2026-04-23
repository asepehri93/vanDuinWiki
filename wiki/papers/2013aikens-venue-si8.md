---
id: paper:2013aikens-venue-si8
type: paper
title: "Supporting information: Improved ReaxFF force field parameters for Au–S–C–H systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1021/jp405992m"
year: 2013
authors:
  - "Christine M. Aikens"
venue: "Supporting information (J. Phys. Chem. A)"
pdf_sha256: "a8e38baed5182d62065260259614c237bf33f063aa83954fd5c36f91e3ea8cf0"
pdf_path: "papers/ReaxFF_others/Bae_Aikens_AuSCH_improved_JPCA_2013_SI.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013aikens-venue-si8 -->

## Summary

This corpus entry registers the **Supporting Information (SI)** PDF for **Bae & Aikens**, **J. Phys. Chem. A**, **DOI `10.1021/jp405992m`**, documenting **improved ReaxFF parameters** for **Au–S–C–H** chemistry in **thiolate-protected gold** nanocluster models. The SI is not a substitute for the primary article: it contains **tables** and **figures** comparing **old** versus **nanoparticle-specific** ReaxFF terms, **bond lengths and angles** for selected **Au–thiolate** clusters against **PBE** and earlier ReaxFF parameterizations, **isomer energies**, and **potential energy surfaces** for **S–Au–S** bending in model motifs. Scientific interpretation of why parameters were changed and what accuracy was achieved belongs to **`[[2013bae-j-phys-chem-jp405992m]]`** / **`[[2013bae-venue-jp405992m]]`**.

## Methods

### Corpus role (SI-only)

This file is **Supporting Information** for **Bae & Aikens**, **J. Phys. Chem. A**, **DOI `10.1021/jp405992m`** (`papers/ReaxFF_others/Bae_Aikens_AuSCH_improved_JPCA_2013_SI.pdf`). Scientific interpretation and primary **MD** validation protocols belong on **`[[2013bae-j-phys-chem-jp405992m]]`** / **`[[2013bae-venue-jp405992m]]`**.

### Force-field training (SI disclosure)

**Parent FF / elements:** **ReaxFF** **Au–S–C–H** parameters relative to the prior **Järvi et al.** set; the SI lists adjusted **bond** and **angle** terms (from **Table 1S** onward).

**QM reference / training / optimization:** Tables compare **ReaxFF** metrics to **PBE** references for **Au\(_{25}\)(SCH\(_3\))\(_{18}\)**, **Au\(_{38}\)(SCH\(_3\))\(_{24}\)**, **Au\(_{144}\)(SCH\(_3\))\(_{60}\)** (**multi-hundred-atom thiolate clusters** per table), isomer energies, and **S–Au–S** bending **PES** cuts (**Figures 1S–3S**); the **parameter optimization** / **least-squares** fit narrative is in the **main article**.

**Reference data used:** **PBE** cluster benchmarks and legacy vs **NP-specific** ReaxFF columns in the SI tables.

### MD application

**N/A —** this SI PDF is **tabular/figure supplementary material**; it does not substitute the main text for **production molecular dynamics** settings (**NVE/NVT/NPT** labels, **Δt** in **fs**, **ps/ns** trajectory schedules, **thermostat**/**barostat**, **PBC**, **temperature** setpoints in **K**). Use **`[[2013bae-venue-jp405992m]]`** for **LAMMPS** **NVE** relaxation notes and related validation language.

## Findings

**Outcomes:** The SI shows **which ReaxFF terms change** and how **geometries**, **angles**, and **relative energies** move toward **PBE** for the benchmark **Au–thiolate** clusters listed above.

**Comparisons:** Side-by-side **PBE** vs **original** vs **NP-specific ReaxFF** columns in **Tables 1S+** and **Figures 1S–3S**.

**Sensitivity / levers:** Parameter shifts target **S–Au–S staple** bending and **Au–S** bonding stiffening discussed in the parent article.

**Limitations:** **SI-only** ingest—do not cite this path as the **version-of-record** scientific argument.

**Corpus honesty:** Mechanistic claims about **reactivity** or long **MD** trajectories must be taken from the **main PDF**, not the SI tables alone.

## Limitations

**SI-only** ingest—always pair with the **primary paper**; frontmatter author line may not list all contributors present on the main article byline.

## Reader notes (MAS / retrieval)

Treat as **parameter appendix** for **Au–S** **ReaxFF**; retrieve **`[[2013bae-j-phys-chem-jp405992m]]`** for scientific interpretation and citations to primary spectroscopic claims.

Keep **Table 1S** as the authoritative parameter diff list.

## Relevance to group

Duplicate **SI** path useful for **parameter tables** when calibrating **Au–S** **ReaxFF** simulations in the knowledge base.

## Citations and evidence anchors

- Parent article DOI **10.1021/jp405992m** — see **`[[2013bae-j-phys-chem-jp405992m]]`**.
- PDF: `papers/ReaxFF_others/Bae_Aikens_AuSCH_improved_JPCA_2013_SI.pdf`; extract: `normalized/extracts/2013aikens-venue-si8_p1-2.txt`.

## Related topics

- [[2013bae-j-phys-chem-jp405992m]]
- [[2013bae-venue-jp405992m]]
- [[reaxff-family]]
