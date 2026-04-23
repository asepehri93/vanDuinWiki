---
id: paper:2017osti-venue-paper-2
type: paper
title: "Influence of metal ion intercalation on the vibrational dynamics of water confined between MXene layers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:water-silica-geo
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:water-interfaces
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevMaterials.1.065406"
year: 2017
authors:
  - "Naresh C. Osti"
  - "Michael Naguib"
  - "Karthik Ganeshan"
  - "Yun K. Shin"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
  - "Yongqiang Cheng"
  - "Luke L. Daemen"
  - "Yury Gogotsi"
  - "Eugene Mamontov"
  - "Alexander I. Kolesnikov"
venue: "Phys. Rev. Mater."
pdf_sha256: "5ee588bf6fc7ce794a8b7392bccb5ee3ad76f89209eac1c556d7759ad2a956b6"
pdf_path: "papers/Osti_PhysicsMat_2017_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017osti-venue-paper-2 -->

!!! abstract
INS on pristine and Li/Na/K-intercalated Ti₃C₂Tₓ with ReaxFF MD (ADF) on interlayer water: larger ions correlate with more ordered, slower water in experiment and simulation.

## Summary

This slug is a **publisher proof PDF** (`Osti_PhysicsMat_2017_proof.pdf`) for the same **Phys. Rev. Mater.** article curated under **[[2017osti-venue-paper]]** (`papers/Osti_PhysicsMat_2017.pdf`). After the cover letter, the proof contains the full paper on **inelastic neutron scattering** of **water** in **Ti₃C₂Tₓ** with **Li⁺/Na⁺/K⁺ intercalation**, paired with **ReaxFF molecular dynamics** (implementation in **ADF**, ReaxFF citations [27,28] in the article text). The MD section describes **~1776-atom** supercells with **two MXene layers**, energy minimization (**200** steps), **NPT equilibration at 300 K** (**20 ps**) with fixed in-plane lattice parameters, then **NVT** thermalization and **200 ps** production **NVT** with weak thermostat coupling for sampling. INS shows much stronger hydrogen signal for pristine vs ion-intercalated samples; intercalation removes substantial interlayer water and changes **GVDS** of vibrations. MD reproduces **increased ordering** and **reduced mobility** with larger intercalated cations.

## Methods

This slug tracks the **APS publisher proof** PDF (`papers/Osti_PhysicsMat_2017_proof.pdf`); the scientific content matches **[[2017osti-venue-paper]]** (*Phys. Rev. Mater.* **1**, 065406; DOI `10.1103/PhysRevMaterials.1.065406`). The in-repo proof extract `normalized/extracts/2017osti-venue-paper-2_p1-2.txt` is **cover-letter pages only**, so protocol details below follow the **article body bundled in the proof PDF** (same Methods as the VOR) rather than that extract.

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **ReaxFF** molecular dynamics carried out with **ADF (ADF2016)** as stated in the article body on this proof; export pages precede the formatted article in this file.
- **System size & composition:** Supercells of order **~1776 atoms** containing **two Ti\(_3\)C\(_2\)T\(_x\)** layers with intercalated **Li\(^+\)/Na\(^+\)/K\(^+\)** and confined water in the arrangement used for INS comparison.
- **Boundaries / periodicity:** **Three-dimensional periodic** supercells (standard for slab gallery models in the article; confirm facet vectors in the formatted pages).
- **Ensemble:** **NPT** equilibration segment followed by **NVT** production sampling as described in the article body summarized on the sibling VOR note.
- **Timestep:** **N/A here** — explicit fs value is not on the cover-letter extract; read the formatted Methods in the proof PDF or **[[2017osti-venue-paper]]**’s `pdf_path`.
- **Duration / stages:** **Energy minimization** (**200** steps reported in the article body on this proof), **NPT** equilibration at **300 K** for **~20 ps** with **fixed in-plane lattice parameters**, then **~200 ps NVT** production with **weak-coupling** temperature control (values as tabulated in the article).
- **Thermostat:** **Weak-coupling** temperature control during **NVT** production as described in the article body on this proof (exact algorithm label on the formatted Methods pages).
- **Barostat:** **NPT** segment uses anisotropic volume control consistent with fixed in-plane lattice constants as described in the article; confirm barostat label in the formatted Methods.
- **Temperature:** **300 K** for the MD equilibration/production windows quoted above.
- **Pressure:** **N/A** for the **NVT** production segment; **NPT** segment controls stress tensor components as described in the article.
- **Electric field:** **N/A** — not applied in the MD protocol summarized for the INS comparison.
- **Replica / enhanced sampling:** **N/A** — conventional MD stages only.

### 2 — Force-field training

**N/A as a new fit** — the publication **employs** a published **ReaxFF** parametrization for MXene–water–ion interactions (cited training literature in the article).

### 3 — Static QM / DFT-only

**N/A** — INS is the primary experimental observable; QM is not the production spectroscopy engine.

### 4 — INS experiment (mirrors VOR page)

**SEQUOIA** measurements with **E\(_i\) = 50, 160, 250, 600 meV** and **VISION** baselines for water / 2 M hydroxide solutions; HF-derived Ti\(_3\)C\(_2\)T\(_x\) processed with **2 M LiOH/NaOH/KOH** intercalation, **XRD**, and **110 °C (4 h) vacuum** drying, plus the **150 °C** hydrogen-removal step for pristine material (Sec. II.A text shared with **[[2017osti-venue-paper]]**).

## Findings

### Outcomes and mechanisms

**INS** shows interlayer water with **bulk-like disorder** for **pristine** Ti\(_3\)C\(_2\)T\(_x\)**,** but **much less** confined water and **more ordered** hydrogen-bond environments after **alkali intercalation**, with ordering that **increases with cation size** in the article’s analysis.

### Comparisons

**ReaxFF MD** reproduces the trend of **reduced mobility** and **stronger spatial interference** among water molecules as intercalated **alkali size** grows, consistent with the **INS**-derived picture and with earlier **quasielastic** discussion of **K\(^+\)**-intercalated MXenes.

### Sensitivity / design levers

Ion identity (**Li vs Na vs K**) and post-synthesis **drying/anneal** history strongly modulate how much water remains in the gallery—both must stay consistent between INS specimens and simulation cells.

### Limitations, outlook, and corpus honesty

Prefer **[[2017osti-venue-paper]]** for automation keyed to the **VOR** blob hash; this **proof** PDF adds **workflow/cover** pages that can shift pagination. Operators should cite **DOI + journal pagination** from the formatted article, not the proof letterhead, when archiving simulation metadata. Full spectral interpretation and any author-stated caveats belong to the formatted **Phys. Rev. Mater.** text inside this PDF bundle.


## Limitations

Proof PDF adds **workflow pages**; prefer **[[2017osti-venue-paper]]** for stable file naming in automation. **INS** instrument **resolution** and **multiple** **incident** **energy** settings influence how **G(E)** features map onto **MD** **spectral** comparisons; use the article’s **figure** captions when aligning **simulation** **timestep** and **sampling** windows to **neutron** data. Keep **hydration** **history** and **intercalation** **routes** synchronized between **experiment** and **simulation** when comparing **ion-size** trends.

## Relevance to group

**Adri C. T. van Duin** and **Alireza Ostadhossein** co-authorship; neutron + ReaxFF pairing for **MXene** electrolyte confinement.

## Citations and evidence anchors

- DOI: `10.1103/PhysRevMaterials.1.065406`

## Related topics

- [[2017osti-venue-paper]]
- [[reaxff-family]]

## Reader notes (navigation)

- **VOR-focused page:** [[2017osti-venue-paper]].
- **Corpus catalog (publisher proof PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) — treat this slug as **proof/workflow** packaging when automating citations; prefer **`2017osti-venue-paper`** for stable pagination when both PDFs exist locally.
