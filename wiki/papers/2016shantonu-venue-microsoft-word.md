---
id: paper:2016shantonu-venue-microsoft-word
type: paper
title: "Supporting information: QM/experimental vs ReaxFF comparison for CHO-2016 combustion force field training"
updated: "2026-04-20"
confidence: low
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: null
year: 2016
authors:
  - "Chowdhury Ashraf"
  - "Adri C. T. van Duin"
venue: null
pdf_sha256: "5ca1cf271ae520c7566483281e77a7b1f9388235f12ad638bb77bb0c3e97dde2"
pdf_path: "papers/Ashraf_CHO_2017_JPCA_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016shantonu-venue-microsoft-word -->

## Summary

This Supporting Information PDF belongs to the CHO-2016 extension of the ReaxFF combustion parameterization focused on syngas chemistry and oxidation initiation pathways, with the peer-reviewed narrative appearing in the companion *Journal of Physical Chemistry A* article by Chowdhury Ashraf and Adri C. T. van Duin (see **`[[2017ashraf-venue-research]]`** and the version-of-record slug **`[[2017chowdhury-venue-jp6b12429]]`** when citing pagination from the issue PDF). The SI pages tabulate quantum-mechanical reference energies alongside ReaxFF (CHO-2016) reaction energies for a hierarchy of small-molecule reactions, including dehydrogenation steps and bond dissociations involving C=O, C=C, O–O, C–H, H–O, and C–O bonds. The tables are intentionally granular: they expose per-reaction residuals so that parameter changes during the CHO-2016 reoptimization can be audited against the underlying quantum targets rather than summarized only by global error metrics. The purpose is training-set documentation: auditors can verify which energetic targets anchored the reoptimization and where residual errors remain. Frontmatter author strings in the corpus may not match publisher ordering; treat the linked CHO-2016 article as authoritative for authorship and DOI.

## Methods

**1 — MD application.** **N/A —** this PDF is **Supporting Information** of **gas-phase** **QM versus CHO-2016 ReaxFF** reaction **energy tables**; any **condensed-phase** or **production MD** validation protocols live in the companion **J. Phys. Chem. A** article (**`[[2017chowdhury-venue-jp6b12429]]`** and related corpus slugs).

**2 — Force-field training (SI content).** Tables list **QM reference** energies alongside **CHO-2016 ReaxFF** values for **bond dissociations** and **dehydrogenation** motifs spanning **C=O**, **C=C**, **O–O**, **C–H**, **H–O**, and **C–O** classes so **residuals** can be audited reaction-by-reaction. **QM level** (functional, basis, geometry conventions) for each training reaction is defined in the **main article** and referenced here rather than fully re-derived on this page.

**3 — Static QM / DFT.** The SI **is** primarily **QM** documentation for the fit; detailed **Monte Carlo** optimization weights, **liquid**/**interface** benchmarks, and **global** error metrics are **N/A —** not reproduced here—see the **primary** publication.

Production **MD** validation protocols (cells, ensembles, timesteps, run lengths) are **N/A —** not defined in this SI; see the companion **J. Phys. Chem. A** article (**`[[2017chowdhury-venue-jp6b12429]]`** / **`[[2017ashraf-venue-research]]`** per corpus linking). For completeness of **molecular dynamics** indexing on this SI: **LAMMPS**-style **supercell** **PBC** setups, **NVT**/**NPT** staging, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** control, **temperature** (K), **electric field** coupling, and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** here because this file is **QM vs ReaxFF** tables, not trajectory protocols.

## Findings

**Training-set diagnostics.** Side-by-side **QM** and **CHO-2016** rows show where the reactive field **tracks** **QM** **rankings** and **energies** for small-molecule **combustion** motifs and where **large residuals** identify reactions that remained **difficult** to fit during **reoptimization**.

**Scope limits.** These **gas-phase** tables **do not** establish performance for **liquids**, **soot**, or **interfacial** systems; those benchmarks are **N/A —** not in this SI—see **`[[2017chowdhury-venue-jp6b12429]]`**.

Confirm every **number** against **`pdf_path`** and the **version-of-record** companion article; this ingest may lack publisher **DOI** in frontmatter.

## Limitations

SI-only files lack standalone discussion of simulation performance on condensed-phase or interfacial systems; confidence remains low for automated metadata because DOI and venue fields may be incomplete in this ingest stub.

## Relevance to group

The document is a primary transparency artifact for group-led combustion ReaxFF development and should accompany any reproduction of CHO-2016 parameters in LAMMPS decks.

## MAS / retrieval notes

Ingest metadata lacks a DOI in frontmatter—link to the main CHO-2016 *J. Phys. Chem. A* article for bibliographic completion. Automation should treat QM vs ReaxFF energy tables as training-set evidence, not as standalone experimental results. Confidence stays `low` until frontmatter aligns with publisher identifiers and the companion article slug is canonicalized in manifests.

## Citations and evidence anchors

- Companion article: **Ashraf & van Duin**, *J. Phys. Chem. A* **2017**, **CHO-2016** extension (`papers/Ashraf_CHO_2017_JPCA_SI.pdf`).

## Related topics

- [[reaxff-family]]
