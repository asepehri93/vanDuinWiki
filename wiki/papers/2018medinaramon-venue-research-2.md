---
id: paper:2018medinaramon-venue-research-2
type: paper
title: Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte Interface under
  Conditions for CO2 Reduction
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:batteries-electrochemistry
- domain:catalysis-surfaces
- domain:reaxff-lineage
- material:metal-surface
- method:dft-static
- method:reaxff
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:galley-or-proof-pdf
- keyword:batteries-interfaces
- keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: 10.1021/acs.chemmater.8b00050
year: 2018
authors:
- Jonnathan Medina-Ramos
- Weiwei Zhang
- Kichul Yoon
- Peng Bai
- Ashwin Chemburkar
- Wenjie Tang
- Abderrahman Atifi
- Sang Soo Lee
- Timothy T. Fister
- Brian J. Ingram
- Joel Rosenthal
- Matthew Neurock
- Adri C. T. van Duin
- Paul Fenter
venue: Chem. Mater.
pdf_sha256: a6fb4b3e3e7f5549270cf2f4b8c0c5249d570227dcd450fe49d627c5271e61d8
pdf_path: papers/MedinaRamon_ChemMat_2018_proof.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018medinaramon-venue-research-2 -->

??? info "PDF variant"
    ACS **proof** PDF. Canonical curation with VOR `pdf_path` is on [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]] (`papers/MedinaRamon_ChemMat_2018.pdf`).

## Summary

This entry registers the ACS **proof** PDF `papers/MedinaRamon_ChemMat_2018_proof.pdf` for *Chemistry of Materials* DOI `10.1021/acs.chemmater.8b00050`, “Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte Interface under Conditions for CO₂ Reduction.” The extract (`normalized/extracts/2018medinaramon-venue-research-2_p1-2.txt`) contains the article **abstract** and the start of the **Introduction**, establishing the combined experimental and computational scope: in situ X-ray reflectivity on Bi(001) films that initially contain a native Bi₂O₃ layer reduced to Bi⁰ during cyclic voltammetry in acetonitrile with BMIM⁺ electrolytes; loss of roughly 60% of the Bi(001) Bragg reflectivity during a potential sweep between about −1.5 and −1.9 V versus Ag/AgCl attributed to roughly 4–10% thinning and roughly 40% decrease in lateral domain size, largely reversible on the anodic scan; and repeated cycling enhancing thinning and roughening, suggesting partial dissolution under negative polarization. The abstract states that molecular dynamics with **ReaxFF** and **DFT** calculations indicate stronger binding of imidazolium cations than tetrabutylammonium (TBA⁺) as the potential and surface charge become more negative, that ReaxFF predicts greater disorder for negatively charged Bi(001) with imidazolium and substantial Bi migration from the surface, and that DFT shows Bi···[Im]⁺ complexes favoring dissolution from step edges between about −1.65 and −1.95 V while desorption from a flat terrace requires about −2.25 V. The scientific narrative, figure references, and full Methods are maintained on [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]] because the proof file can differ subtly in layout from the journal PDF.

## Methods

The proof extract continues into the **Experimental** section opener, listing BMIM triflate (≥98%) from Sigma-Aldrich used as received and solutions prepared in acetonitrile at **100 mM**, with comparison experiments using TBA-based electrolytes (for example TBAPF₆ and TBAOTf sources named in the text layer). Experimental XR electrochemical cells, potential programs, and surface-sensitive fitting procedures appear in the main article. ReaxFF simulations use a Bi/ionic-liquid parameterization developed in the study to explore binding and restructuring at the electrified interface, while DFT calculations address cluster or complex energetics referenced in the text. Full computational details—supercell sizes, charge models, thermostat choices, and convergence settings—should be read from [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]] rather than inferred from this duplicate proof path alone.

### MD application (proof-ingest note)

**ReaxFF molecular dynamics** on **Bi(001)** with **imidazolium** vs **TBA⁺** motifs parallels the main article narrative. **Engine / code:** **N/A — MD engine** not restated on this duplicate proof page—confirm alongside **LAMMPS**/**other** notes on **`[[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]`**. **Ensemble:** **NVT**-class sampling for the interfacial **ReaxFF** segments per the **VOR** Methods summary on the sibling page. **Timestep / duration / thermostat / barostat:** **N/A — not transcribed** from this proof PDF—use the **VOR** Methods. **PBC:** **slab** models implied by the **Bi(001)** focus (**exact padding/freeze** in **PDF**). **Temperature / pressure / electric field / enhanced sampling:** **N/A — MD-stage details** not duplicated here beyond what appears in the abstract on the sibling VOR page.
## Findings

The peer-reviewed article ties imidazolium-related surface disorder and bismuth migration to cathodic corrosion under the investigated potentials; the proof extract’s abstract already quantifies XR reflectivity loss, thinning, and domain-size trends during BMIM scans and contrasts behavior with TBA-based electrolytes where the dramatic restructuring was not observed. The Introduction reproduced in the extract recounts prior in situ XR on Bi thin films during CO₂ reduction and frames the present work as coordinated XR, RRDE, ReaxFF, and potential-dependent DFT to explain atomic-level restructuring. Because this slug duplicates the science under a proof `pdf_path`, automated PDF-to-text pipelines may reorder captions relative to the final issue; when quoting layer electron densities or Bi occupancy metrics, anchor numbers to the VOR PDF or to tables in [[2018medinaramos-venue-microsoft-word]] rather than to this proof file.

## Limitations

Proof PDFs may not match final figure numbering. Prefer the non-proof PDF for long-term maintenance.

## Relevance to group

Multi-institution collaboration including van Duin (ReaxFF) and Argonne beamline science for electrified interfaces.

When diffing this proof against the VOR PDF, pay attention to author affiliations and compound labels that ACS sometimes reformats during production; those cosmetic edits do not change the core electrochemistry but can break naive string-based extract alignment in automation scripts.

## Reader notes (navigation)

- [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Citations and evidence anchors

https://doi.org/10.1021/acs.chemmater.8b00050
