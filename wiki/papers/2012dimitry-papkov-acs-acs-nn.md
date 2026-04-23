---
id: paper:2012dimitry-papkov-acs-acs-nn
type: paper
title: "Extraordinary improvement of the graphitic structure of continuous carbon nanofibers templated with double-wall carbon nanotubes"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:graphene-carbon-nano
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
  - keyword:nvt-simulation
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/nn303423x"
year: 2013
authors:
  - "Dimitry Papkov"
  - "Allison M. Beese"
  - "Alexander Goponenko"
  - "Yan Zou"
  - "Mohammad Naraghi"
  - "Horacio D. Espinosa"
  - "Biswajit Saha"
  - "George C. Schatz"
  - "Alexander Moravsky"
  - "Raouf Loutfy"
  - "Sonbinh T. Nguyen"
  - "Yuris Dzenis"
venue: "ACS Nano 7 (1), 126–142 (2013)"
pdf_sha256: "2d6591910b36bd04e7706c9e09e98a10c21dbd963e8f268814e6b521b32c944d"
pdf_path: "papers/ReaxFF_others/Papkov_ACS_Nano_2013_CNT_Nanofiber.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012dimitry-papkov-acs-acs-nn -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Rather than using **carbon nanotubes (CNTs)** as **high-volume-fraction** reinforcements—where **dispersion**, **alignment**, and **stress transfer** often limit gains—this work employs **double-wall nanotubes (DWNTs)** at **~1.2%** loading in **electrospun PAN** precursors as **templates** for **graphitization** during **oxidation** and **carbonization** (**600–1850 °C**). **Structural characterization** shows **large gains in graphitic order** and **orientation**, strongest at **lower carbonization** temperatures relative to **untemplated** controls. **In situ pull-out** tests indicate **good interfacial bonding** between **DWNT bundles** and the **templated carbon matrix**. **Classical MD** of **templated carbonization** supports **oriented graphitic growth** mechanisms consistent with experiment.

## Methods

**Continuous carbon nanofibers** are **electrospun** from **polyacrylonitrile (PAN)** with **1.2% double-wall carbon nanotubes (DWNTs)** (small templating load), then subjected to **oxidative stabilization** and **carbonization** over **600–1850 °C**. **Raman**, **wide-/small-angle X-ray scattering**, and related **structural** metrics quantify **graphitic order** and **orientation** versus **untemplated** controls.

### 1 — MD application (atomistic dynamics)

**ReaxFF molecular dynamics** of **templated carbonization** uses **ReaxFF** valence terms tied to bond order / bond energy relationships for dissociation (as summarized on this page from **`pdf_path`**).

- **Engine / code:** **ReaxFF MD**; **N/A —** MD engine/package not named on the indexed excerpt pages.
- **System size & composition:** **Stabilized PAN fragment** **C₃₂H₁₄N₁₀** (species **B**) with either **B + (5,5) SWNT** (**190 C + 20 H**, H-terminated, **r ≈ 3 Å**, length **22 Å**) or **B + graphene** (**204 C + 40 H**, **22×29 Å**), each with **16 B** molecules aligned along the presumed fiber axis (**21 wt % CNT** or **23 wt % graphene**, higher than experiment to fit periodic cells). **Initial densities** **1.60–1.75 g/cm³** (CNT) or **1.6–1.8 g/cm³** (graphene) at **300 K** (**pdf_path**).
- **Boundaries / periodicity:** **PBC** in all directions.
- **Ensemble:** **NVT** for the **production carbonization** segment.
- **Timestep:** **N/A —** not stated on the indexed excerpt pages.
- **Duration / stages:** **Equilibration** at **300 K** for **60 ps**; **10** structures sampled from **50–60 ps** for annealing runs; **annealing** ramp **10 K/ps** until reactions appear (**2500 K** and above on their short timescales); **production carbonization** **500 ps** at **2500 K** with **N₂**, **H₂**, **HCN**, **NH₃** removed every **50 ps** to mimic volatile loss. Trajectories are analyzed for evolved gases, ring formation/breaking, **sp²** carbon growth, and templating vs pure PAN (**pdf_path**).
- **Thermostat / barostat:** **N/A —** thermostat/barostat algorithm names not recovered from the indexed excerpt pages—verify **`pdf_path`**.
- **Temperature:** **300 K** equilibration; **2500 K** carbonization stage; ramping to **≥2500 K** during annealing (as stated above).
- **Pressure / stress:** **N/A —** not stated for these **NVT** carbonization cells on the indexed excerpt pages.
- **Electric field:** **N/A —** not stated.
- **Replica / enhanced sampling:** **N/A —** not stated.

### 2 — Force-field training

**N/A —** uses **ReaxFF** bond-order dissociation/reactivity concepts as implemented in the authors’ carbonization workflow rather than reporting a new general refit on pp. 1–2.

### 3 — Static QM / DFT-only

**N/A —** not the focus of the MD subsection summarized here.

## Findings

**Outcomes and mechanisms:** At **~1.2 vol %** **DWNT** loading, **templated** fibers show large improvements in **graphitic order** and **orientation**, with the strongest gains at **lower carbonization temperatures** vs **untemplated** controls—interpreted as **global templating** of graphitic structure without high nanotube fractions (abstract-level claims on wiki aligned to **`pdf_path`**).

**Comparisons:** **In situ pull-out** tests are reported as showing **good interfacial bonding** between **DWNT bundles** and the **templated carbon matrix** (wiki summary from **`pdf_path`**).

**Sensitivity and design levers:** **Carbonization temperature** (**600–1850 °C** experimental range in **Summary**) and **templating** vs pure **PAN** are the main comparative axes; the **ReaxFF** section emphasizes high-temperature reactive trajectories with periodic volatile stripping as a modeling lever (wiki + **`pdf_path`**).

**Limitations / outlook:** The wiki **Limitations** section notes **MD** idealization vs real **electrospun** microstructure; the article’s broader caveats should be read in **`pdf_path`**.

**Corpus / KB honesty:** The carbonization MD recipe is summarized from the full article text used to curate this page; pp. 1–2 of `normalized/extracts/2012dimitry-papkov-acs-acs-nn_p1-2.txt` may not contain the full protocol table—verify **`pdf_path`** for authoritative numbers.

## Limitations

- **MD** models are **idealized** relative to **electrospun** fiber microstructure; quantitative property predictions still require experimental validation across batches.

## Relevance to group

**Schatz**-group **MD** appears alongside **nanocarbon** processing—useful cross-reference for **carbon fiber** and **CNT** **interface** literature adjacent to **ReaxFF** combustion/nanocarbon pages.

## Citations and evidence anchors

- DOI: [10.1021/nn303423x](https://doi.org/10.1021/nn303423x)
- Text-aligned pointer: `normalized/extracts/2012dimitry-papkov-acs-acs-nn_p1-2.txt`

## Related topics

- [[graphene-nanocarbon]]
- Carbon nanofibers and graphitic templating
