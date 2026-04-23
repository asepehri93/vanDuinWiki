---
id: paper:2013newsome-venue-jp307680t
type: paper
title: "High-Temperature Oxidation of SiC-Based Composite: Rate Constant Calculation from ReaxFF MD Simulations, Part II"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp307680t"
year: 2013
authors:
  - "Newsome, David A."
  - "Sengupta, Debasis"
  - "van Duin, Adri C. T."
venue: "Journal of Physical Chemistry C"
pdf_sha256: "a794e37e8e48bca3182364ad0f9a84af35d75324f2c2fb28c97b1ce290917790"
pdf_path: "papers/Newsome_JPCC_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013newsome-venue-jp307680t -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Part II of a two-part study uses ReaxFF reactive molecular dynamics trajectories to build rate models for thermal protection system (TPS) chemistry: oxidation of silicon carbide by O₂ and H₂O and combustion/pyrolysis of an EPDM polymer model. The work connects atomistic transport and reaction events to Arrhenius parameters for comparison with experiment and with phenomenological multiscale models (abstract and introduction, pages 1–2 of the extract).

## Methods

**1 — MD application:** **Reactive molecular dynamics** uses a **Si/C/H/O** **ReaxFF** parameterization trained to **ab initio** data (**Part I** referenced in the text; **`papers/Newsome_JPCC_2013.pdf`**, **`normalized/extracts/2013newsome-venue-jp307680t_p1-2.txt`**). Trajectories underpin **rate models** for **SiC oxidation** by **O\(_2\)** and **H\(_2\)O** and for **EPDM combustion** vs **pyrolysis** via **Arrhenius** fits. **N/A —** full **LAMMPS** settings (**ensemble**, **timestep**, **thermostat/barostat**, **cell sizes**, **production durations**, **temperature grids**) are not reproduced from the short extract; read **“Details of computational approach”** in the **PDF** for the definitive protocol.

**2 — Force-field training:** **N/A —** **Part I** carries the primary **parameterization/validation** narrative relative to this **Part II** rate-theory focus.

**3 — Static QM / DFT-only:** **N/A —** central method is **ReaxFF MD** plus **phenomenological** **rate** fits (Deal–Grove–style **transport** picture referenced in the abstract/introduction).

**Electric field / enhanced sampling:** **N/A —** not stated in the indexed opening for this **kinetics** extraction workflow.

**System / boundaries / ensemble / pressure (ReaxFF production MD):** **N/A —** **`normalized/extracts/2013newsome-venue-jp307680t_p1-2.txt`** does not restate **slab**/**composite** **atom** counts, **3D periodic** boundary conditions, whether trajectories use **NVT** vs **NPT**, or any **GPa**/**bar** **pressure** targets—see **`papers/Newsome_JPCC_2013.pdf`** **Methods**.

## Findings

**Outcomes and mechanisms:** **O\(_2\)** oxidizes **SiC** more efficiently than **H\(_2\)O** in the simulations; **transport activation barriers** fall roughly in the **40–70 kJ/mol** range for **O\(_2\)** and **125–150 kJ/mol** for **H\(_2\)O**. **Oxidizer** attack builds a **SiO\(_2\)**-rich surface while **O** inserts between **Si–C** bonds and **C** migrates into a **carbonaceous** region (abstract).

**Comparisons:** **EPDM** **combustion** and **pyrolysis** simulations yield activation barriers near **183 kJ/mol** and **213 kJ/mol**, respectively, compared to **experimental** polymer literature near **~100–250 kJ/mol** for both channels (abstract).

**Sensitivity / design levers:** **Temperature** enters through **Arrhenius** extraction across the **MD** trajectory sets; full **temperature/pressure** matrices and **mixture** (**O\(_2\)**, **H\(_2\)O**, **mixtures**) handling appear later in the **PDF** than the indexed opening.

**Limitations and outlook:** **Part II** depends on **Part I** **FF** validation and **trajectory** ensembles; **Arrhenius** extraction from finite **MD** windows can be **sensitive** to **model** and **sampling** choices (see discussion in the article).

**Corpus honesty:** This summary is anchored to **`normalized/extracts/2013newsome-venue-jp307680t_p1-2.txt`** (early pages); quantitative **fits**, **uncertainties**, and **figure**-level mechanisms require the full **J. Phys. Chem. C** article (**DOI `10.1021/jp307680t`**).

## Limitations

Part II depends on Part I force-field validation and trajectory ensembles; Arrhenius extraction from short MD windows can be sensitive to model and sampling. The extract covers early pages only; full temperature/pressure matrices and uncertainty quantification appear later in the PDF. Repository automation maps this stable `paper_id` to `normalized/papers/2013newsome-venue-jp307680t.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

Co-authored with Adri van Duin; demonstrates ReaxFF for aerospace ablation/oxidation chemistry and quantitative kinetics extraction aligned with the group’s reactive MD and parameterization line.

## Citations and evidence anchors

- Abstract and introduction: contribution statement, barrier ranges, EPDM Arrhenius values, J. Phys. Chem. C framing (extract pages 1–2).
- DOI: `10.1021/jp307680t` (footer of extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
