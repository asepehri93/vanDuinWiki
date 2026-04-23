---
id: paper:2013silica-venue-jp4019525
type: paper
title: "The structure of silica surfaces exposed to atomic oxygen"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:oxide-surface
  - keyword:dft-static
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp4019525"
year: 2013
authors:
  - "Paul Norman"
  - "Thomas E. Schwartzentruber"
  - "Hannah Leverentz"
  - "Sijie Luo"
  - "Rubén Meana-Pañeda"
  - "Yuliya Paukku"
  - "Donald G. Truhlar"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "144c6468ec12f9f455a5cce43c00b01a2c6103fba299a55189119dde4502c924"
pdf_path: "papers/ReaxFF_others/Silica_defect_PaulNorman.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013silica-venue-jp4019525 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

ReaxFF\(_{\mathrm{SiO}}\) **GSI** potentials (Kulkarni et al., parametrized for silica–oxygen gas-surface chemistry) model **quartz** and **amorphous silica** surfaces exposed to **atomic oxygen** using MD with a **flux boundary condition**. Bulk and surface structures align with experimental and prior computational references for these materials. The simulations recover known defect types under vacuum and hot O exposure and predict a **peroxyl** surface defect not seen in earlier MD work but reported experimentally; **DFT** checks the O\(_2\) binding geometry/energy on that site. The discussion ties defect populations to **catalytic O-atom recombination** heating relevant to **thermal protection** applications. The **J. Phys. Chem. C** article emphasizes **high-temperature** **gas-surface** regimes where **atomic** **oxygen** **flux** and **surface** **mobility** jointly set **defect** **inventory**.

## Methods

Grounding: `papers/ReaxFF_others/Silica_defect_PaulNorman.pdf`; `normalized/extracts/2013silica-venue-jp4019525_p1-2.txt` (abstract + introduction opening).

### 1 — MD application (ReaxFF\(_{\mathrm{SiO}}\) GSI + atomic O flux)

- **Engine / code:** **Molecular dynamics (MD)** with the **ReaxFF\(_{\mathrm{SiO}}\) GSI** potential parametrized for **silica–oxygen gas–surface** interactions, citing **Kulkarni et al., J. Phys. Chem. C 2012** (abstract).
- **System size & composition:** Models include **quartz** and **amorphous silica** surfaces exposed to **atomic oxygen** using a **flux boundary condition** (abstract). **Atom counts / slab thicknesses** are **not stated** on the indexed excerpt pages.
- **Boundaries / periodicity:** N/A — **explicit PBC / cell vectors** are **not stated** on the indexed excerpt pages.
- **Ensemble / thermostat / barostat:** Bulk **a-SiO\(_2\)** preparation uses **NVT** heating/cooling and **NPT** relaxation at **300 K**, **1 atm** with a **Nosé–Hoover** thermostat/barostat (**100 fs** damping) as quoted in the article Methods (`papers/ReaxFF_others/Silica_defect_PaulNorman.pdf`, extracted PDF text).
- **Timestep / duration:** N/A — full timestep/production splits for all **atomic-oxygen exposure** segments are **not summarized** on the indexed excerpt pages; read `pdf_path`.
- **Temperature:** Introduction excerpt states focus on **dry silica** exposed to **atomic oxygen** at **1000–1750 K** as **TPS re-entry-relevant** conditions (introduction excerpt).
- **Pressure:** N/A — framed around **low-pressure / high-temperature** re-entry-type environments in the introduction excerpt rather than a single quoted hydrostatic target.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — uses a published **ReaxFF\(_{\mathrm{SiO}}\) GSI** parametrization (**Kulkarni et al. 2012**, cited in abstract) rather than introducing a new fit in this article.

### 3 — Static QM / DFT (spot validation)

**DFT** calculations are used to validate **O\(_2\)** **binding geometry/energy** on a **peroxyl** defect predicted by ReaxFF (abstract). The introduction excerpt notes **DFT direct dynamics** examples with **PBE**, **LDA**, and **PW91** functionals as **literature context** for silica surface reconstruction (introduction excerpt), separate from the headline MD+DFT validation described in the abstract.

## Findings

- **Outcomes & mechanisms:** ReaxFF reproduces **bulk quartz/amorphous silica** and known **surface defect** motifs consistent with **prior MD and experiment**, and predicts a **peroxyl** defect not seen in earlier MD studies but supported by **DFT** for **O\(_2\)** binding (abstract).
- **Comparisons:** Explicit comparisons are made to **experiment** and **prior simulations/measurements** for silica surfaces and defect inventories (abstract; introduction cites multiple experimental reconstruction studies).
- **Sensitivity / design levers:** **Temperature window (1000–1750 K)** and **atomic oxygen exposure** (vs vacuum) are central levers in the introduction framing for TPS-related chemistry (introduction excerpt).
- **Limitations & outlook:** The introduction emphasizes uncertainty in **elementary recombination pathways** despite extensive catalycity measurements (introduction excerpt), motivating the MD+defect inventory approach.
- **Corpus honesty:** Indexed excerpt includes **abstract + long intro** but not the full **MD Methods** tables; read **`pdf_path`** for **flux prescription**, **timestep**, and **run segmentation**.

## Limitations

Force-field scope is Si–O–H gas-surface focused; multicomponent boundary-layer chemistry is not fully represented.

## Relevance to group

Benchmark **silica oxidation / TPS** chemistry using a dedicated ReaxFF\(_\mathrm{SiO}\) line related to broader C/H/O and materials work.

## Citations and evidence anchors

- DOI: [10.1021/jp4019525](https://doi.org/10.1021/jp4019525)
- Extract: `normalized/extracts/2013silica-venue-jp4019525_p1-2.txt`

## Related topics

- [[reaxff-family]]
- High-temperature gas–surface recombination on oxides
