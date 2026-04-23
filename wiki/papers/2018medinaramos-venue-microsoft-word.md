---
id: paper:2018medinaramos-venue-microsoft-word
type: paper
title: 'Supporting Information: Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte
  Interface under Conditions for CO2 Reduction'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:batteries-electrochemistry
- domain:reaxff-lineage
- method:reaxff
- method:dft-static
- task:software
- scale:atomistic
paper_keywords:
- keyword:supporting-information
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
venue: Chem. Mater. (Supporting Information)
pdf_sha256: deb6cbad92ee2b15afe3c8aad82d67b65733b6d935d24cd748836e231e4f387d
pdf_path: papers/MedinaRamoS_ChemMat_2018_SI.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018medinaramos-venue-microsoft-word -->

## Summary

This Supporting Information file `papers/MedinaRamoS_ChemMat_2018_SI.pdf` expands the *Chemistry of Materials* article DOI `10.1021/acs.chemmater.8b00050` on cathodic corrosion of bismuth in contact with BMIM-type ionic liquid electrolytes under CO₂ electroreduction-relevant conditions (Medina-Ramos et al.). The SI contains supplementary **X-ray reflectivity** cell descriptions, **Bragg** and **layering** analyses, extended **electrochemical** traces, and additional **ReaxFF** and **DFT** comparison plots referenced from the main text. It is the appropriate location for supercell dimensions, convergence settings, and supplementary experimental parameters that could not fit in the primary article PDF. The main text abstract (also excerpted under the proof-ingest slug [[2018medinaramon-venue-research-2]]) quantifies XR reflectivity loss and Bi restructuring during BMIM scans; the SI typically holds the additional curves and fits backing those statements.

## Methods

Readers should follow the SI figure and table index starting at page 1 of the PDF for computational parameters (**ReaxFF** nonbonded settings, **charge equilibration** frequency/cutoffs, **DFT** exchange–correlation choices where quoted) and for experimental **beamline** details duplicated or extended from Methods in the main paper. Interpretation of applied potentials, electron density profiles, and proposed Bi···imidazolium complexes remains in the peer-reviewed article on [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]; the SI supports reproducibility rather than replacing the narrative. When a computational setting appears both briefly in Main Methods and in expanded form in the SI, treat the SI table as the binding reference for replication.

### MD application (SI pointer)

This **Supporting Information** PDF is the authoritative place for expanded **ReaxFF** settings (neighbor lists, **QEq** frequency, cutoffs) and duplicated **molecular dynamics** protocol lines relative to the main text. **Engine / code:** **N/A — MD engine name** appears in the SI computational tables—copy from **`papers/MedinaRamoS_ChemMat_2018_SI.pdf`**. **System & composition:** **Bi(001)** **slab** cells with explicit **ionic-liquid** **atoms** and counterions as tabulated in the SI (full stoichiometry there). **PBC:** **three-dimensional periodic boundary conditions** for the **slab** supercells unless a SI figure caption documents a frozen layer. **Ensemble:** **NVT** sampling for the **ReaxFF** segments is what the main article + SI pair describe—confirm any mixed stages in the SI tables. **Timestep / thermostat / barostat / trajectory length:** **N/A — not duplicated** on this navigation page; use SI + **`[[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]`**. **Temperature:** SI repeats **temperature** setpoints and thermostat coupling referenced from **Methods**—import numerics from the **PDF** rather than this stub. **Pressure:** **N/A — hydrostatic pressure control not used** for the quoted **interface** **MD** summary path. **Electric field in MD:** **N/A — not part** of the SI summary layer here. **Enhanced sampling:** **N/A — not indicated** for these **ReaxFF** runs in the SI description carried on this page.
## Findings

The SI supports the main conclusions about **imidazolium-driven** surface disorder and **bismuth migration** by providing raw and processed datasets; it should not be read as introducing wholly new primary claims absent from the main text. Extended XR and electrochemical plots help separate signal from background for buried bismuth interfaces, which matters because ionic-liquid electrochemistry can produce overlapping features from interfacial layering, bulk electrolyte contributions, and cell-specific artifacts. When citing electron-density oscillations or Bi occupancy metrics, align figure labels with the VOR SI PDF path recorded in manifests rather than assuming numbering matches an intermediate proof bundle. Cross-link users studying AEM-related degradation to the main article’s mechanistic discussion while using this file for **data traces** and **parameter dumps**.

## Limitations

Supporting files may be updated asynchronously from the article HTML; cite the article for scientific assertions and use the SI for reproducibility detail.

## Relevance to group

Repository pointer for ReaxFF and DFT supplementary material tied to van Duin-group electrochemistry collaborations.

Computational sections in the SI often repeat convergence thresholds that main-text Methods summarize briefly; when reproducing ReaxFF interfacial energies, copy the exact charge equilibration frequency and cutoff behavior quoted in the SI tables to avoid drift relative to published numbers.

XR-derived electron-density profiles in the SI should be paired with the electrochemical potential programs listed in the main Methods, because corrosion phenomena are inherently coupled to the applied bias history rather than to a single static snapshot.

## Reader notes (navigation)

- [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Citations and evidence anchors

https://doi.org/10.1021/acs.chemmater.8b00050
