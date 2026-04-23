---
id: paper:2014hatzelletal-venue-es5043782
type: paper
title: "Effect of strong acid functional groups on electrode rise potential in capacitive mixing by double layer expansion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/es5043782"
year: 2014
authors:
  - "Hatzell, Marta C."
  - "Raju, Muralikrishna"
  - "Watson, Valerie J."
  - "Stack, Andrew G."
  - "van Duin, Adri C. T."
  - "Logan, Bruce E."
venue: "Environmental Science & Technology"
pdf_sha256: "aa45c8bf97532946cd2e1e42745b98291d68be2f6db4ffdb2773ef8f54e2b3d9"
pdf_path: "papers/Hatzelletal_ES&T_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014hatzelletal-venue-es5043782 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Experiments on five activated carbons link strong-acid group concentration to electrode “rise potential” during capacitive mixing by double-layer expansion (CDLE) in dilute electrolyte. Nitric acid oxidation shifts rise potential and boosts whole-cell voltage. Atomistic MD and metadynamics connect the trend to EDL structure: pristine-like graphene surfaces expand the diffuse layer in low-concentration solution (positive rise), whereas oxidized graphene-oxide-like surfaces compress it (negative rise), mechanistically coupling functional chemistry to salinity-gradient energy harvesting (abstract; introduction, extract pages 1–2). **CDLE** devices harvest **energy** from **salinity** swings by **charging** **electrodes** in **concentrated** brine then **discharging** in **freshwater**; **rise potential** is a **figure of merit** for how **electrode** **chemistry** shifts **interfacial** **potential** during the **dilution** half-cycle.

## Methods

### Experiments (macro electrochemistry)

- **Materials:** **Potentiometric titrations** and **CDLE-style rise/fall** measurements on **five activated carbons** spanning **strong-acid** surface loadings from **~0.05 to ~0.36 mmol g⁻¹** (abstract); **HNO₃ oxidation** of **YP50** provides a paired **before/after** functionalization case (details in the article).

### ReaxFF molecular dynamics / EDL sampling (atomistic)

- **Surfaces:** **Pristine graphene (PG)** models **low** strong-acid coverage, while **graphene oxide (GO)**-like structures (from **Bagri *et al.***, cited in the article) model **high** coverage (**SI Figure S11** in the publication). In-plane slab footprints are **~43.35 Å × 40.04 Å** with a **~16 Å** solution gap as stated in the Methods narrative.
- **Electrolyte:** **KCl(aq)** solutions at **~2.4 M (“HC”)** and **~0.9 M (“LC”)** after ion removal are used to bracket the **CDLE** experiment’s **high- vs low-concentration** half-cycles. **Cross-interaction** parameters follow **Rahaman *et al.*** for **C/H/O** (graphene–water) and **Cl/O/H** (chloride–water) subsets described in the paper.
- **Integration:** **NPT**, **Δt = 0.25 fs**, **Berendsen** thermostat (**100 fs** damping) and barostat (**500 fs** damping); energy minimization to **0.25 kcal mol⁻¹ Å⁻¹** force norm; **50 ps** equilibration at **300 K**; **HC EDL** statistics from **50 ps** production at **300 K**; **LC EDL** from **100 ps** total (**50 ps** equilibration + **50 ps** production) per the article’s simulation schedule.
- **Enhanced sampling:** **Well-tempered metadynamics** via **PLUMED 1.3** coupled to **LAMMPS** (collective variables summarized in **SI**).

### Coverage note

- Full **experimental** titration protocols and **SI** tables for **functional group** assignments should be taken from the **ES&T** PDF; the checked-in text extract may truncate figure captions.

### Integrated MD checklist (maps to article narrative above)

- **Engine / code:** **LAMMPS** with **PLUMED 1.3** for **well-tempered metadynamics** (Methods above).
- **System / PBC:** **PG** vs **GO**-like slabs in **~43.35 Å × 40.04 Å** footprints with **~16 Å** solution gap (Methods).
- **Ensemble:** **NPT** with **Δt = 0.25 fs**, **Berendsen** thermostat (**100 fs** damping) and barostat (**500 fs** damping) as stated.
- **Stages:** minimization to **0.25 kcal mol⁻¹ Å⁻¹** max force; **50 ps** equilibration at **300 K**; **HC** **EDL** statistics from **50 ps** production; **LC** from **100 ps** total (**50 ps** equilibration + **50 ps** production).
- **Temperature:** **300 K** for the summarized **MD** windows.
- **Pressure:** controlled via **NPT** barostat settings above (Methods).
- **Electric field (applied):** **N/A —** not part of the summarized **EDL** setup.
- **Enhanced sampling:** **well-tempered metadynamics** (**PLUMED**) as stated.

## Findings

### 1 — Outcomes and mechanisms

- Across carbons, **electrode rise potential in LC** correlates with **strong-acid group concentration** at **P = 10⁻⁵**; **low-acid** electrodes show **positive** rises (e.g., **59 ± 4 mV** at **~0.05 mmol g⁻¹**), whereas **high-acid** carbons trend **negative** (e.g., **−31 ± 5 mV** at **~0.36 mmol g⁻¹**).
- **Nitric acid oxidation** of **YP50** shifts **rise potential** from **46 ± 2 mV** to **−6 ± 0.5 mV** and yields a **whole-cell** mixing potential of **53 ± 1.7 mV**, about **4.4×** the **12 ± 1 mV** obtained with **symmetric** electrodes in their comparison.
- **ReaxFF MD + metadynamics** link **PG** surfaces to **EDL expansion** in **LC** (positive-rise trend) and **GO** surfaces to **EDL compression** (negative-rise trend), matching the **functional-group** narrative of the experiments.

### 2 — Comparisons

- **Experiments** on **five activated carbons** plus **HNO₃** **before/after** **YP50**; **atomistic** models interpret **PG** vs **GO**-like surfaces (**SI Figure S11** cited in the article).

### 3 — Sensitivity

- **Strong-acid** site loading from **~0.05 to ~0.36 mmol g⁻¹** correlates with **rise potential** trends (abstract).

### 4 — Limitations / outlook

- Model surfaces coarse-grain **carbon** heterogeneity; see **## Limitations**.

### 5 — Corpus / KB honesty

- Full **experimental** protocols and **metadynamics** collective variables are in **`pdf_path`** and **SI**; extract may truncate captions.

## Limitations

Carbon structural heterogeneity is coarse-grained into model surfaces; CDLE cycle simplifications noted in broader CDLE literature referenced in intro.

## Relevance to group

Raju and van Duin contribute atomistic interpretation tying interfacial chemistry to electrochemical device metrics.

**Retrieval note:** pair this paper with other **CDLE**/**capacitive mixing** entries in the corpus when benchmarking **salinity-gradient** **energy** claims, because **rise potential** depends on **both** **macroscopic** **flow** and **nanoscale** **EDL** **structure**.

## Citations and evidence anchors

- Environ. Sci. Technol. 2014, 48, 14041–14048; DOI `10.1021/es5043782` (extract page 2 footer).
- Abstract statistics (extract page 1).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
