---
id: paper:2013afif-venue-paper
type: paper
title: "A reactive force field for zirconium and hafnium di-boride"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, domain:mechanics-tribology, method:reaxff, task:parameterization, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2012.12.038"
year: 2013
authors: ["Gouissema, Afif", "Fan, Wu", "van Duin, Adri C. T.", "Sharma, Pradeep"]
venue: "Computational Materials Science"
pdf_sha256: "59d399dccb15b4ae30ba5837c0941dd352c391e36fa86fb72de1a46c7cefe895"
pdf_path: "papers/Afif_CompMatSci_2013.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013afif-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Zirconium and hafnium diborides are ultra-high-temperature ceramics valued for hypersonic thermal protection, rocket nozzles, and other oxidizing, mechanically demanding environments where metallic bonding in boride frameworks confers refractory strength. The *Computational Materials Science* communication develops ReaxFF parameters for ZrB\(_2\) and HfB\(_2\) so finite-temperature reactive molecular dynamics can treat bond formation, fracture, and oxidation chemistry that nonreactive potentials cannot represent. Introduction-level properties quoted in the PDF include mass densities near 6.09 and 11.09 g cm\(^{-3}\), melting temperatures near 3300 K, and elastic moduli near 450 GPa, motivating atomistic studies of oxidation and creep once a reactive field exists for the boride chemistry space.

## Methods

### Force-field training

**Parent FF / elements:** **ReaxFF** for **ZrB\(_2\)** and **HfB\(_2\)**, using a reduced energy expression (bond, valence, over-coordination, **vdW**, **Coulomb**; torsional terms omitted as a tractability choice in this parameterization) per **§2** of **`pdf_path`**.

**QM reference:** **Quantumwise** (periodic crystal phases) and **Gaussian 09** (geometry optimizations and potential-energy curves for **Zr(BH\(_2\))\(_2\)** and **Hf(BH\(_2\))\(_2\)** clusters) as stated in **§3** (`normalized/extracts/2013afif-venue-paper_p1-2.txt`). **N/A —** DFT functional, basis, and **k**-mesh details beyond the short extract—read **`pdf_path`**.

**Training set:** **QM** energies and charge distributions for **ZrB\(_2\)** / **HfB\(_2\)** crystal inputs (lattice parameters **a = 3.22 Å**, **c = 3.54 Å** for **ZrB\(_2\)**; **a = 3.14 Å**, **c = 3.47 Å** for **HfB\(_2\)** in the extract) plus molecular **BH\(_2\)**-ligand scans.

**Optimization:** Parameters are fit to the **QM training set** following the paper’s staged workflow (**§4** outline in the extract).

**Reference data used:** **QM** cluster and crystal data enter the fit; **MD** comparisons in **§5** are described as validation against **QM** or **experiment** where cited in the article.

### MD application (validation)

**Engine / code:** The article references **molecular dynamics** validation using the fitted potential (**§5**); **VASP** is named for **periodic QM** work in **§3**—confirm which code drives the **MD** validation runs in **`pdf_path`**.

**System size & composition:** **N/A —** supercell sizes and thermodynamic state points for **§5** MD are **not** in the p1–2 extract.

**Boundaries / periodicity:** **Periodic** **ZrB\(_2\)**/**HfB\(_2\)** crystal descriptions appear in the **QM** section; **N/A —** how those map to **MD** validation cells is not excerpted here.

**Ensemble (NVE / NVT / NPT):** **N/A —** not stated in `2013afif-venue-paper_p1-2.txt` for **§5 MD** validation.

**Timestep / duration / thermostat / barostat:** **N/A —** not stated in `2013afif-venue-paper_p1-2.txt`.

**Temperature:** Introduction quotes **melting points around 3300 K** as motivation for high-temperature materials; **N/A —** actual **MD** thermostat temperatures **not** in the excerpt.

**Pressure / stress:** Introduction discusses **pressure-assisted sintering** contexts; **N/A —** explicit **MD** stress/pressure control **not** in the excerpt.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not mentioned.

## Findings

**Outcomes:** The communication reports **self-consistent ReaxFF parameters** for **ZrB\(_2\)** and **HfB\(_2\)**, enabling **reactive** simulations for **metal–boron–oxygen** environments where prior models were lacking (abstract).

**Comparisons:** Fits target **QM** data described in **§3**; broader **EOS**, **defect**, and **oxidation** applications are framed as **follow-on** studies rather than fully expanded here (abstract / outline).

**Sensitivity / levers:** Parameter quality depends on the chosen **QM** training coverage for each boride.

**Limitations:** Short article format; **`extraction_quality: partial`**—tables and **§5** MD benchmarks live in the **PDF**.

**Corpus honesty:** This page does not reproduce numerical **MD** validation metrics; use **`pdf_path`** for **§5** results.

## Limitations

Corpus metadata marks extraction quality as partial, and `confidence: med` reflects reliance on PDF reading for tables and figures—verify numerical fits directly in the journal PDF. Some circulated copies carry watermarking; cite the journal volume for authoritative pagination.

## Relevance to group

Expands **ReaxFF** into **refractory boride** chemistry relevant to extreme-environment materials modeling.

## Citations and evidence anchors

- Title/abstract and Secs. 2–3 overview (Comput. Mater. Sci. 70 (2013) 171–177; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
