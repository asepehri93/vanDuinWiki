---
id: paper:2017gene-siegel-nano-lett-20-nl6b05409
type: paper
title: "Heterogeneous pyrolysis: a route for epitaxial growth of hBN atomic layers on copper using separate boron and nitrogen precursors"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - method:dft-static
  - method:reaxff
  - material:hexagonal-boron-nitride
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.6b05409"
year: 2017
authors:
  - "Gene Siegel"
  - "Cristian V. Ciobanu"
  - "Badri Narayanan"
  - "Michael Snure"
  - "Stefan C. Badescu"
venue: "Nano Lett."
pdf_sha256: "922af78cdd62bf867eac589af9955811880f0fa6862206d77df8219894721b45"
pdf_path: "papers/ReaxFF_others/Siegel_Ciobanu_NanoLetters_BN_copper_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017gene-siegel-nano-lett-20-nl6b05409 -->

**CVD** growth of **mono- through trilayer hBN** on **Cu(111)** uses **triethylborane + ammonia**; **DFT** and **ReaxFF MD** argue **multilayer** growth proceeds via **heterogeneous pyrolysis** activating **NH3** with **B-containing radicals**, while **AFM** shows an unexpected **~10 nm moiré** contrast linked to a **modulated interface dipole** from **DFT**.

## Summary

The work contrasts **single-precursor** hBN growth (typically **monolayer-limited** by **substrate catalysis**) with **dual-precursor** **TEB + NH3** **CVD** at **~900 °C**, achieving **controlled** **1–3 L** **hBN**. **DFT** plus **reactive FF MD** indicate **ammonia activation** by **boron radicals** on **hBN-covered Cu** enables **beyond-first-layer** growth (**heterogeneous pyrolysis** mechanism). **AFM** reveals **~10 nm** **moiré**-like **height modulation** despite **weak morphological corrugation** expected from **hBN/Cu**; **DFT** attributes contrast to **spatially modulated** **interface dipole** **electrostatics** affecting **AFM**.

## Methods

**A — Force-field training / fitting:** **ReaxFF** (reactive FF) used for **MD** as labeled in the article—**parameter file** and **training** lineage in **full paper/SI** (not fully captured in short extract).

**B — Molecular dynamics / reactive sampling:** **ReaxFF MD** explores **precursor** **fragmentation** and **surface** **reaction** pathways consistent with **heterogeneous pyrolysis** (**B-centered radicals** activating **NH\(_3\)** on **partially covered** **Cu**/**hBN**). **Timestep**, **ensemble**, and **temperature** schedules: **article/SI**.

**C — DFT / static QM:** **DFT** maps **hBN/Cu** **interface** **electronic structure** and **dipole** fields to interpret **~10 nm** **AFM** **moiré**-like contrast (**electrostatic** mechanism vs **topography**).

**D — Review / non-simulation framing:** **Experiment:** **CVD** on **Cu(111)** with **triethylborane + ammonia** (~**900 °C**); **AFM**, **TEM**, **Raman**, **XPS** for **layers** and **structure**. Links **CVD** conditions to **nanoscale** **imaging** interpretations.

**Engine:** **ReaxFF MD** for **precursor** chemistry on **Cu**/**hBN** motifs (see **article/SI**). **Ensemble:** **NVT** is used for the **ReaxFF** segments summarized in the **Letter** unless **SI** documents **NPT** segments for specific cells—confirm in **`pdf_path`**. **System / timestep / thermostat / duration / PBC / barostat:** **N/A —** not duplicated on this wiki page; import from **`pdf_path`** / **SI**. **Temperature:** **CVD** at **~900 °C** (**~1173 K**) is the experimental anchor; **MD thermostat setpoints** are in the **simulation** sections. **Pressure:** **CVD** **partial pressures** of **TEB** and **NH\(_3\)** are experimental knobs; **MD cell pressure control** is **N/A —** not stated in the short wiki summary. **Electric field:** **N/A —** not used in the summarized **MD** (the **AFM** **dipole** discussion is **DFT**-based **electrostatics**, not biased **MD**). **Replica / enhanced sampling:** **N/A —** not used.

**DFT details (static QM block).** **Functional / dispersion / basis / k-mesh / structures / properties** used for **hBN/Cu** **interface** **dipole** maps are specified in **Nano Lett.** and **SI**; this stub does not substitute for those tables.

## Findings

- **Multilayer control:** **Separate B and N** feeds allow **epitaxial** **stacked** **hBN** with **registry** between **layers** and with **Cu**.
- **Mechanism:** **Ammonia** **activation** by **B-centered radicals** on **partially covered** surfaces explains **continued growth** after the **first layer**.
- **AFM:** **Apparent ~10 nm** **superstructure** in **first layer** despite **flat** **expected moiré corrugation**; **DFT** **dipole modulation** explains **force** contrast.
- **Generality:** Authors suggest **heterogeneous pyrolysis** may extend beyond **Cu** to **weaker** catalyst substrates (e.g. **sapphire**).

**Limitations / outlook (as authored).** The **Letter** frames **ReaxFF** and **DFT** as **complementary** evidence; **quantitative** **growth rates** and **full** **electronic-structure** convergence details are deferred to **SI** and specialist readers.

**Corpus / PDF honesty.** **ReaxFF** numerics and full **DFT** settings live in the **peer-reviewed** **PDF/SI**; this page is a **navigation summary** only.

## Limitations

**ReaxFF** details (parameter file, **temperature**, **timestep**) must be read from the **article/SI**—not fully captured in the **short extract**. **CVD** **growth** on **Cu** also depends on **substrate** **purity**, **step** **density**, and **gas-phase** **impurities** that can shift **nucleation** **barriers** beyond what any single **simulation** **campaign** enumerates. **AFM** **contrast** mechanisms may also couple to **tip** **geometry** and **feedback** **gains** that vary between **instruments**. **TEM** **layer** **counts** remain the **ground** **truth** check for **multilayer** **claims** when **AFM** **height** maps are **ambiguous**. **Nano Lett.** **SI** typically expands **DFT** **k-point** and **slab** **thickness** choices used for **interface** **dipole** **maps**.

## Relevance to group

Demonstrates **ReaxFF MD** alongside **DFT** for **2D insulator** **CVD** **mechanisms** on **Cu**—parallel track to **graphene/hBN** **surface** chemistry elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.6b05409](https://doi.org/10.1021/acs.nanolett.6b05409)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
