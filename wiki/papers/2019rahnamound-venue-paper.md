---
id: paper:2019rahnamound-venue-paper
type: paper
title: "Chemical dynamics characteristics of Kapton polyimide damaged by electron beam irradiation (uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:ereaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:polymer
source_refs: []
doi: "10.1016/j.polymer.2019.05.035"
year: 2019
authors:
  - "Ali Rahnamoun"
  - "Daniel P. Engelhart"
  - "Sunita Humagain"
  - "Hilmar Koerner"
  - "Elena Plis"
  - "W. Joshua Kennedy"
  - "Russell Cooper"
  - "Steven G. Greenbaum"
  - "Ryan Hoffmann"
  - "Adri C. T. van Duin"
venue: "Polymer (uncorrected proof, 2019)"
pdf_sha256: "ab265afc0964f85d0759d29bc22c2b20d19047f245bfa52309612b102f94915d"
pdf_path: "papers/Rahnamound_Kaption_eBeam_Polymer2019_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019rahnamound-venue-paper -->

??? info "PDF variant"
    **Uncorrected proof**. Curated VOR summary: [[2019rahnamoun-polymer-176-chemical-dynamics]].

## Summary

The uncorrected proof corresponds to the Polymer article DOI `10.1016/j.polymer.2019.05.035` on Kapton (PMDA–ODA polyimide) degradation under electron irradiation, combining polarizable ReaxFF reactive molecular dynamics with Fourier-transform infrared spectroscopy, electron paramagnetic resonance, nuclear magnetic resonance, wide- and small-angle X-ray scattering, and dynamic mechanical analysis. The abstract in the proof describes approximating the electron beam as a dense column of negatively charged particles inserted at random positions in the polymer matrix, switching each beam on for 2 fs so that Coulomb interactions transfer an average energy of 21 eV per electron trajectory during the simulation window. It states that experimental samples are aged in vacuum with a 90 keV electron beam whose penetration depth exceeds the film thickness, and that after beam segments the authors run 0.5 ns of microcanonical MD to capture structural relaxation.

## Methods

**Document role.** This file is the **uncorrected proof** PDF for the *Polymer* article; full simulation tables, the complete beam protocol, and all characterization parameters are in **`[[2019rahnamoun-polymer-176-chemical-dynamics]]`** and the version-of-record **PDF** at the same **DOI**.

**1 — MD application (polarizable eReaxFF, electron-beam model).** **Molecular dynamics** uses the **ReaxFF program** as in the VOR Methods. The **abstract** (also in the local proof extract) approximates the beam as a **dense column of negatively charged particles** inserted at **random positions** in the **Kapton (PMDA–ODA)** matrix; each beam is **on for 2 fs**, with **Coulomb**-mediated transfer of **~21 eV** per **electron trajectory**; **NVE** for **0.5 ns** after the beam **sequence** captures post-exposure **relaxation** (as stated in the proof). The **VOR** Methods give the **eReaxFF** line, the **20-chain** Kapton model (**C₁₅₄H₇₂O₃₅N₁₄** per chain, 7 repeat units, H-terminated), **0.1 fs** integration where stated, and the **NVT** equilibration **~300 K** (with thermostat type) before **NVE** beam segments. **3D** **PBC** apply to the **polyimide** slab. **Barostat** / **NPT** production: **N/A** for the **NVE**-**dominant** damage stages after equilibration. **Pressure** control: **N/A** in the **NVE** stages. **Shear, shock, external uniform E-field, umbrella / metadynamics: N/A**—energy enters via **local** **Coulomb** **deposition** from the dummy **beam** model, not a **continuum** **E-field** fix in the **FF** sense.

**2 — Experiments.** **90 keV** **e**-**beam** aging in **vacuum**; penetration depth **>** film thickness. **FTIR, EPR, ¹³C** **MAS** **NMR, WAXD, SAXS, DMA** on **pristine** vs **irradiated** films—**full** **dose** **rates** and **sampling** in the **VOR**.

**3 — Force-field training.** **N/A** (uses a **published** **polarizable** **eReaxFF** / **ReaxFF** line for this polymer; **de novo** **fit** is **not** the **main** result).

**4 — Static DFT as sole outcome.** **N/A.**
## Findings

**Corpus honesty.** The **proof** **abstract** claims **agreement** between **trajectory**-**level** **chemistry** and **FTIR** / **EPR** / **NMR** / **WAXD** / **SAXS** / **DMA**, and refers to **slab** **temperature** and **mechanical** **evolution** under **exposure**; **dose**–**response** **curves** and **tables** must be read from the **final** **Polymer** **PDF** on **`[[2019rahnamoun-polymer-176-chemical-dynamics]]`**, not from **proof** **pagination** alone. **Intro** **motivation** ( **space** **materials**; **e**-**beam** **vs** **heavy**-**ion** **literature** ) is **framing** in the **manuscript**—**verify** **wording** on the **VOR** if **citing** **verbatim**.

**Comparisons / limitations.** For **qualitative** **regimes** ( **imide** **damage**, **cross**-**linking** vs **cleavage** ), use the **VOR** **page**; this **proof** **slug** is for **provenance** of this **PDF** **hash** only.

## Limitations

Uncorrected proofs may differ slightly from the journal version. Use the VOR page for stable pagination and any publisher corrections.

## Relevance to group

Van Duin-group contribution linking polarizable ReaxFF to radiation damage of aerospace polyimides with multi-technique validation.

The beam-on/off protocol described in the abstract (2 fs excitation segments, 10 fs NVE spacing, 0.5 ns post-beam NVE) is unusual compared with standard ReaxFF production runs; reproducers should copy segment counts and durations verbatim from the VOR Methods section rather than improvising continuous-beam approximations.

## Reader notes (navigation)

- [[2019rahnamoun-polymer-176-chemical-dynamics]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1016/j.polymer.2019.05.035](https://doi.org/10.1016/j.polymer.2019.05.035)
