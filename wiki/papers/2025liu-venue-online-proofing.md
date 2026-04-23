---
id: paper:2025liu-venue-online-proofing
type: paper
title: "Polarization switching on the open surfaces of the wurtzite ferroelectric nitrides: ferroelectric subsystems and electrochemical reactivity"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - material:widegap-semiconductor
  - method:classical-md
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:galley-or-proof-pdf
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1002/adma.202511001"
year: 2025
authors:
  - "Yongtao Liu"
  - "Anton V. Ievlev"
  - "Eugene A. Eliseev"
  - "Ali Mohammadi Dinani"
  - "Alireza Sepehrinezhad"
  - "Ubaidullah S. Hassan"
  - "Drew Behrendt"
  - "Nana Sun"
  - "Kazuki Okamoto"
  - "Hiroshi Funakubo"
  - "Andrew M. Rappe"
  - "Adri C. T. van Duin"
  - "Anna N. Morozovska"
  - "Sergei Kalinin"
venue: "Advanced Materials (Wiley)"
pdf_sha256: "1265939bdf72c37ba1b10797ba92e96b78f99905ecf2fa9db96d41a6ac256bf4"
pdf_path: "papers/Liu_Dinani_Sepehrinezhad_AlN_switching_AdvMat_2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025liu-venue-online-proofing -->

!!! abstract

Piezoresponse force microscopy (PFM) and spectroscopy on wurtzite ferroelectric nitrides resolve polarization switching, electromechanical response, and surface deformation during first-order reversal curves; complementary ReaxFF MD on AlN with applied electric fields and DFT adsorption energies address how surface adsorbates and hydroxyl chemistry couple to switching.

## Summary

The study addresses polarization switching in binary ferroelectric nitrides (e.g., AlScN-type systems in the graphical abstract), where reversal ties to **N- versus M-terminated** surface polarity and electrochemical coupling. **Multidimensional high-resolution PFM** (including band-excitation PFM workflows) maps domains, switching, and topography under varying DC pulse magnitude and duration. **ReaxFF molecular dynamics** of **AlN** thin films under external electric fields probes water dissociation, hydroxyl chemisorption versus molecular water physisorption, and field-driven desorption; **first-principles calculations** (details in Supporting Information) report adsorption energies for water and hydroxyl on Al- versus N-terminated surfaces.

## Methods

### Experiments (PFM)

- **Platform:** Automated / high-throughput PFM workflows on a band-excitation (BE) PFM platform: DC pulses of varying magnitude and duration nucleate or grow domains, followed by BE PFM imaging of amplitude and phase; topography was recorded in parallel.
- **Protocols:** First-order reversal curve (FORC) measurements capture evolution of ferroelectric domains, electromechanical response, and surface deformation during bias ramps; vacuum PFM measurements are noted for part of the work (author roles in the proof).
- **Sample context:** Wurtzite nitride thin films (e.g., **AlScN** in the graphical abstract text); film growth and basic structural/ferroelectric characterization by collaborators (see author list).

### Atomistic modeling

- **ReaxFF MD:** **LAMMPS** **Molecular** **dynamics** with the **ReaxFF** **potential** for **AlN** **thin** **films** at a fixed **isothermal** **temperature** in **K** (thermostat and **K**-value in **SI**) under **applied** **electric** **fields** (full **ReaxFF** **development** in **Supporting Information**). Polarization sign conventions: **P > 0** toward the free **Al-terminated** surface; **P < 0** toward the substrate (**N-terminated**). **MD** emphasizes **Al-terminated** **surfaces** as a **low**-**field** **screening** **model**.
- **DFT:** First-principles adsorption energies for H₂O and OH on Al- and N-terminated surfaces support interpretation (values stated in the main text include approximately **−1.50 eV** and **−0.46 eV** for most favorable H₂O adsorption on Al- vs N-terminated surfaces, and about **−2.43 eV** for OH on the Al-terminated surface in the reported comparison).

**N/A** on this **wiki** page: **molecular dynamics** **code** (e.g. **LAMMPS** version), **NVE**/**NVT**/**NPT** label, **time step** (**fs**), **ps**-scale **trajectory** length, full **slab** **atom** list, **thermostat**/**barostat** settings, and **hydrostatic** **pressure** in **GPa**/**bar** (see **SI**). **PBC** **in-plane** **periodic** **AlN** **thin-film** **cells** for **ReaxFF** (details in **SI**). The study reports **reactive** **ReaxFF** **MD** of **AlN** films under **applied** **electric** **field**; **N/A** in this short summary for **replica** **exchange**-style **rare**-event **sampling**.

## Findings

- **PFM:** FORC measurements resolve multiple switching stages (partial switching, nested domains, back-switching, complete switching under the probe) consistent with complex domain topology (“shark-teeth” / fringing-ridge behavior) discussed in the text.
- **Subsystems:** Evidence supports **two weakly coupled ferroelectric subsystems** and **bias-induced electrochemical reactivity** at surfaces.
- **ReaxFF / DFT:** MD shows **hydroxyl groups** from water dissociation **chemisorb** on AlN while **molecular water remains physisorbed**; increasing electric field can **strip hydroxyls**, leaving a cleaner surface for switching. DFT adsorption energies support stronger binding on **Al-terminated** vs **N-terminated** surfaces in the reported comparisons. The **Wiley** **author proof** `pdf_path` may differ from the final **VOR** **PDF**; confirm **field** and **kinetic** **numbers** in the **published** issue.

## Limitations

The corpus PDF is a **Wiley author proof** (online proofing overlay); final pagination and copyediting may differ from the version of record. Full numerical protocols appear in **Supporting Information**, not in the local PDF alone.

## Relevance to group

**Adri C. T. van Duin** is credited with **ReaxFF training**; co-authors performed **ReaxFF simulations** and **DFT** alongside ORNL-led PFM.

## Citations and evidence anchors

- DOI: `10.1002/adma.202511001` — *Advanced Materials* (galley PDF in corpus).

## Related topics

- [[reaxff-family]]
