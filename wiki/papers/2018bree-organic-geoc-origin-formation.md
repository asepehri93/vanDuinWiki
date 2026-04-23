---
id: paper:2018bree-organic-geoc-origin-formation
type: paper
title: "Origin, formation and environmental significance of des-A-arborenes in the sediments of an East African crater lake"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.orggeochem.2018.09.001"
year: 2018
authors:
  - "L. G. J. van Bree"
  - "M. M. Islam"
  - "W. I. C. Rijpstra"
  - "D. Verschuren"
  - "A. C. T. van Duin"
  - "J. S. Sinninghe Damsté"
  - "J. W. de Leeuw"
venue: "Organic Geochemistry"
pdf_sha256: "7bbdd1f2619e5483c3d50a4d78e47e0fe6e2041452c3fb3c6f32c1f69cb53611"
pdf_path: "papers/vanBree_OrgGeoChem_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018bree-organic-geoc-origin-formation -->

## Summary

**Pentacyclic triterpenoid** lipids and their **diagenetic** products encode **vegetation**, **fire history**, and **lake** **productivity** signals in **sediment archives**. **Lake Chala** is a **deep** **meromictic** **system** where **organic matter** **preservation** and **bacterial** **reworking** interact with **catchment** **hydrology**, so **biomarker** **interpretations** must **disentangle** **in situ** **production** from **terrigenous** **inputs** using the **multi-proxy** **strategy** laid out in the **paper**. **van Bree** et al. document **des-A-arborene** isomers across a **~25 kyr** **Lake Chala** (**East Africa**) core, integrating **GC–MS**-based **biomarker** identification, **compound-specific** isotopic and **spectroscopic** reasoning, and **molecular mechanics** calculations to test **proposed carbon skeletons** and **ring-contraction** pathways. **Adri C. T. van Duin** participates as a **computational** coauthor, applying **classical** energy models to **steric** feasibility rather than **ReaxFF** reactive dynamics.

## Methods

**Field sampling and laboratory organic geochemistry:** Sediment cores from **Lake Chala** (East African crater lake) are processed on an age model spanning roughly **25 kyr** of lacustrine deposition. The *Organic Geochemistry* **Methods** section gives **solvent extraction**, **fractionation**, and **chromatographic** protocols used to isolate triterpenoid fractions for **GC–MS**.

**Compound identification:** **Des-A-arborene** isomers are assigned from **GC–MS** data with supporting **compound-specific stable carbon isotope** signatures (e.g. des-A-arbor-9(11)-ene averaging about **−32.3‰ ± 1.3‰** in the abstract) and spectroscopic reasoning as cited in the article.

**Molecular mechanics (non-MD):** **Classical molecular mechanics** (force field and search settings in the peer-reviewed **PDF**) ranks steric feasibility of candidate carbon skeletons and ring-contraction hypotheses against mass-spectral constraints. **N/A — atomistic MD production trajectories:** the study does not report **NVE**/**NVT**/**NPT** **LAMMPS** or **GROMACS** production runs for the sediment system; any short relaxations are subordinate to the mechanics ranking workflow described in the journal text.

**Paleolimnological context:** **Holocene** hydroclimate and catchment variability for Lake Chala are synthesized from companion studies referenced in the paper, not from new basin-wide field campaigns introduced only here.

**1 — MD application (atomistic dynamics):** **N/A —** not a reactive or classical MD dynamics study of the lake column.

**2 — Force-field training:** **N/A —** no **ReaxFF** or other reactive force-field refit is reported.

**3 — Static QM / DFT-only:** **N/A —** headline interpretation uses **GC–MS**, isotopes, and molecular mechanics rather than first-principles energy surfaces for the biomarkers.

## Findings

**Mechanism / outcomes:** **Des-A-arborenes** appear at **meaningful abundance** throughout the **~25 kyr** **Lake Chala** record, suggesting **recurring biological** inputs or **diagenetic** routes rather than isolated contamination peaks. **Mechanics** calculations support **plausible** **precursor–product** relationships among **arborene-type** lipids and **des-A** derivatives, narrowing ambiguity where **mass spectra** alone are degenerate.

**Comparisons:** The authors **compared** **GC–MS** assignments, **compound-specific isotope** trends, and **computational** steric screening to prior **lake** **biomarker** interpretations and regional **paleoclimate** archives cited in *Organic Geochemistry*.

**Sensitivity / design levers:** **Abundance** profiles vary with **depth** / age along the core, reflecting changing **catchment** **vegetation**, **fire** history, and **lake** **productivity** proxies discussed in the article.

**Limitations / outlook:** **Microbial** reworking can overprint **original** **vegetation** signatures; the authors stress **multi-proxy** reasoning rather than single-molecule thermometers. **Mechanics** models rank **geometries** but do not supply **barrier**-accurate **reaction kinetics**.

**Corpus honesty:** This page summarizes `pdf_path`; verify ion assignments, **GC–MS** programs, and mechanics settings in the peer-reviewed **PDF** before reuse.

## Limitations

- **Mechanics** models are **not reactive MD**; they support **hypothesis screening** rather than **barrier-precise** reaction kinetics.
- **Biological sources** of related lipids remain **partially uncertain**; interpretations depend on **combined lines of evidence**.

## Relevance to group

Shows **van Duin-group involvement** in **geochemistry-adjacent** organic systems using **classical** computational chemistry tools.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.orggeochem.2018.09.001` (`papers/vanBree_OrgGeoChem_2018.pdf`).

## Related topics

- [[reaxff-family]]
