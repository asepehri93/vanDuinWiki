---
id: paper:2013singh-venue-paper
type: paper
title: "Thermal properties of fluorinated graphene"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:galley-or-proof-pdf
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.87.104114"
year: 2013
authors:
  - "Sandeep Kumar Singh"
  - "S. Goverapet Srinivasan"
  - "M. Neek-Amal"
  - "S. Costamagna"
  - "Adri C. T. van Duin"
  - "F. M. Peeters"
venue: "Physical Review B"
pdf_sha256: "3ccdd8f1ca81c1f0c0a5ce151b14d2d20d3fd14c7d1c591d9ac56b5dbc287041"
pdf_path: "papers/Singh_Srinivasan_etal_PRB_Fluorographene_2013_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013singh-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. The corpus PDF is an **APS proof**; pagination may differ from the journal issue.

## Summary

Large-scale **ReaxFF** MD explores **thermomechanical** behavior of **fluorinated graphene (FG)** with parameters fit to carbon–fluorine cluster QM data. Compared to pristine graphene, FG shows **suppressed thermal rippling**: height fluctuations and \(H(q)\) correlations indicate an **unrippled** sheet across sizes and temperatures studied. Effective **Young’s moduli** from uniaxial strain are about **273 N/m (armchair)** and **250 N/m (zigzag)** for the model flake—contrasting with graphene, graphane, and BN trends discussed in the paper. The study positions **fluorination** as a **chemical knob** on **out-of-plane** fluctuations distinct from **hydrogenation**, relevant to **thermal management** and **mechanical** design of **2D** heterostructures.

## Methods

Grounding: `papers/Singh_Srinivasan_etal_PRB_Fluorographene_2013_proof.pdf`; `normalized/extracts/2013singh-venue-paper_p1-2.txt` (Phys. Rev. B abstract text).

### 1 — MD application (large-scale ReaxFF MD of fluorographene)

- **Engine / code:** **Molecular dynamics** simulations are performed with **LAMMPS** using the authors’ **ReaxFF** parametrization for fluorographene (`papers/Singh_Srinivasan_etal_PRB_Fluorographene_2013_proof.pdf`, Methods text; abstract also references MD).
- **System size & composition:** Studies **fluorinated graphene (FG)** and compares to **graphene**, **graphane**, and **BN** sheets in the abstract’s comparative framing; **explicit atom counts** are **not stated** in the indexed excerpt.
- **Observables / deformation protocol:** MD evaluates **thermal rippling** via **mean-square height fluctuations** and **height–height correlation function \(H(q)\)** across **system sizes** and **temperatures**, and computes **effective Young’s moduli** under **uniaxial strain** along **armchair** and **zigzag** for a **flake** model (abstract).
- **Boundaries / periodicity:** N/A — **PBC vs free-standing flake boundary conditions** are **not stated** in the indexed excerpt.
- **Ensemble:** Rippling sweeps use the **NPT** ensemble at **\(P=0\)** with a **Nosé–Hoover** thermostat, varying **temperature** from **10 K to 900 K** for a representative **N = 17280 atoms** fully fluorinated unit cell (`papers/Singh_Srinivasan_etal_PRB_Fluorographene_2013_proof.pdf`, Sec. III.A excerpt).
- **Timestep / duration:** N/A — **timestep and segment lengths** for all mechanical tests are **not copied** here; read `pdf_path` for full simulation tables.
- **Temperature:** **Temperature** is explicitly invoked as a swept variable for rippling analysis (abstract), but **numeric K values** are **not listed** on the indexed excerpt page.
- **Pressure:** N/A — **not stated** in the indexed excerpt beyond **mechanical strain** for modulus extraction.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training (FG-focused ReaxFF extension)

- **Parent FF / elements:** **ReaxFF** reactive potential form used for **carbon/fluorine/hydrogen** chemistry in this fluorographene study (abstract).
- **QM reference:** Parameters are **optimized to reproduce key quantum mechanical properties** of **carbon–fluorine cluster systems** (abstract). **Specific DFT program/functional/basis** are **not stated** in the indexed excerpt—see `pdf_path` Methods.
- **Training set / targets:** **Carbon–fluorine clusters** relevant to **FG** chemistry (abstract); detailed training list is **not in** `normalized/extracts/2013singh-venue-paper_p1-2.txt`.
- **Optimization:** **Parameter optimization** for ReaxFF is stated at abstract level; **optimizer details** are **not stated** in the indexed excerpt.
- **Reference data / validation:** Post-optimization observables are evaluated by **MD** against comparative reference sheets (**graphene**, **graphane**, **BN**) in the abstract’s comparative framing.

## Findings

- **Outcomes & mechanisms:** FG is described as an **unrippled** system relative to graphene: **mean-square height fluctuations** and **\(H(q)\)** across sizes/temperatures indicate **suppressed thermal rippling** compared to graphene (abstract).
- **Comparisons:** Compares FG behavior against **graphene**, **graphane**, and **BN** for rippling and mechanics in the abstract’s narrative.
- **Sensitivity / design levers:** **System size** and **temperature** are explicit axes for rippling metrics; **strain direction** (**armchair vs zigzag**) is explicit for **Young’s modulus** extraction (abstract).
- **Limitations & outlook:** N/A — author limitations are **not present** in the indexed abstract-only excerpt.
- **Corpus honesty:** Corpus PDF is an **APS proof**; **`normalized/extracts/2013singh-venue-paper_p1-2.txt`** is **abstract-only**—full Methods/tables must be read from **`pdf_path`** (and the **journal version** for stable pagination).

## Limitations

Proof PDF; finite flakes and force-field limits bound quantitative transfer to experimental samples. **Periodic** **in-plane** **boundary** conditions and **finite** **flake** **sizes** influence **rippling** **statistics**; experimental **supported** **films** may show additional **substrate** **coupling** not represented in the idealized **free-standing** **models** emphasized in the article. **Fluorine** **coverage** **homogeneity** in **samples** may differ from **ideal** **lattices**; treat **modulus** **anisotropy** as **model**-dependent until compared to **nanoindentation** on **uniform** **samples**. **Thermal** **conductivity** predictions would require **additional** **phonon** **analysis** beyond the **fluctuation** metrics summarized here.

## Relevance to group

Shows ReaxFF treatment of **halogenated graphene** with van Duin-group parametrization alongside collaborators.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.87.104114](https://doi.org/10.1103/PhysRevB.87.104114)
- Extract: `normalized/extracts/2013singh-venue-paper_p1-2.txt`
- **Corpus catalog (APS proof PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) — confirm pagination against the **journal** issue when available.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
