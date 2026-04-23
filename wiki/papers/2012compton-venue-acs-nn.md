---
id: paper:2012compton-venue-acs-nn
type: paper
title: "Tuning the mechanical properties of graphene oxide paper and its associated polymer nanocomposites by controlling cooperative intersheet hydrogen bonding"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/nn202928w"
year: 2012
authors:
  - "Owen C. Compton"
  - "Steven W. Cranford"
  - "Karl W. Putz"
  - "Zhi An"
  - "L. Catherine Brinson"
  - "Markus J. Buehler"
  - "SonBinh T. Nguyen"
venue: "ACS Nano 6 (3), 2008–2019 (2012)"
pdf_sha256: "ca898e68cf60551ab85c88e9130a2b3a8d9fe1cdd192dc0e899c952ded95715b"
pdf_path: "papers/ReaxFF_others/Compton_Buehler_ACSNano_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012compton-venue-acs-nn -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Graphene oxide (GO) paper** is a **lamellar** assembly whose **mechanical** properties depend strongly on **hydration**: **intercalated water** participates in **hydrogen-bonding networks** between **oxygenated** basal planes and edges. Joint **experiment** and **ReaxFF MD** show that **~5 wt % water** optimizes **cooperative** H-bonding that **stiffens** the paper versus drier or oversaturated galleries; **PVA** in the gallery further **increases cooperativity** (biomaterial-like) and **raises stiffness** for **nanocomposite** films. **DMF** (acceptor-only) yields lower modulus/strength than water at comparable intercalation, underscoring the role of **donor/acceptor** matching in **stress transfer**.

## Methods

### 1 — MD application (atomistic dynamics)

The work pairs **experiments** on **GO paper** and **PVA–GO nanocomposites** with **ReaxFF molecular dynamics** of **lamellar GO** models containing gallery **water** and/or **PVA** to interpret **hydrogen-bond cooperativity** and **stress transfer** (`pdf_path`; `normalized/extracts/2012compton-venue-acs-nn_p1-2.txt`).

- **Engine / code:** **ReaxFF molecular dynamics** (indexed excerpt title/abstract region); **N/A —** MD engine/package not named on pp. 1–2.
- **System size & composition:** **Lamellar GO** with controlled gallery contents (**water** vs **DMF** in experiments; **water/PVA** in simulations as summarized in wiki abstract); **N/A —** atom counts/supercells not on pp. 1–2 extract.
- **Boundaries / periodicity:** **N/A —** not stated on pp. 1–2 extract (lamellar models imply in-plane **PBC** is plausible but not asserted on excerpt pages).
- **Ensemble / timestep / duration / thermostat / barostat / temperature:** **N/A —** **NVT**/**NPT**/**NVE** labels, timestep sizes, **production run** lengths, thermostat/barostat algorithms, and bath **temperature** schedules are not stated on pp. 1–2 extract.
- **Pressure / stress:** Experiments report mechanical **modulus/strength** trends; simulations are motivated to connect **deformation** to **H-bond network** rearrangements (**stress** language appears in the scientific goal statement on the wiki page grounded in the abstract—verify **`pdf_path`** for deformation mode).
- **Electric field:** **N/A —** not stated on pp. 1–2 extract.
- **Replica / enhanced sampling:** **N/A —** not stated on pp. 1–2 extract.

### 2 — Force-field training

**N/A —** uses **ReaxFF** as an interaction model for **GO**/**PVA**/**water** chemistry/mechanics rather than reporting a new parameterization on pp. 1–2.

### 3 — Static QM / DFT-only

**N/A —** not the paper’s headline methodology on pp. 1–2 (beyond any citations in full article).

## Findings

**Outcomes and mechanisms:** **~5 wt % intercalated water** is associated with especially strong **cooperative hydrogen bonding** between **oxygenated** basal planes and edges in **GO paper**, and **DMF** (acceptor-only) yields **lower modulus/strength** than **water** at comparable intercalation—highlighting **donor/acceptor matching** in gallery **H-bond networks** (opening pages/extract on file).

**Comparisons:** The abstract/excerpt emphasizes joint **experimental** + **ReaxFF** interpretation of how gallery contents tune mechanics.

**Sensitivity and design levers:** **Water content** in the gallery is the central lever for **modulus** in **pristine GO paper**; for **PVA–GO**, **stiffness** can **increase with dehydration** down to about **~7 wt % residual water** after annealing, and the abstract framing on the wiki notes **no simple optimum** like pristine GO paper (wiki summary aligned to **`pdf_path`**).

**Limitations / outlook:** **N/A —** detailed limitations discussion is not excerpted on pp. 1–2; consult **`pdf_path`** Discussion.

**Corpus / KB honesty:** Numeric moduli/strength ranges quoted in **Summary**/**Findings** here come from the article’s opening context on the indexed excerpt pages; verify tables/figures in **`pdf_path`** before citing as definitive benchmarks outside this KB page.

## Limitations

- **ReaxFF** captures **classical** chemistry of **GO** functional groups but not full **quantum** electronic structure of edges.
- Laboratory **kinetics** of drying and **defect** distributions can shift real films from ideal models.

## Relevance to group

**ReaxFF** **mechanics** of **GO assemblies** from **MIT/Northwestern** collaboration—pairs with **oxide** and **nanocarbon** themes in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/nn202928w](https://doi.org/10.1021/nn202928w)
- Text-aligned pointer: `normalized/extracts/2012compton-venue-acs-nn_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- Graphene oxide paper and nanocomposites
