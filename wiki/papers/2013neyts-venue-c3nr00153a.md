---
id: paper:2013neyts-venue-c3nr00153a
type: paper
title: "Formation of single layer graphene on nickel under far-from-equilibrium high flux conditions"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - material:graphene-carbon-nano
  - material:metal-surface
  - method:reaxff
  - method:monte-carlo
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1039/c3nr00153a"
year: 2013
authors:
  - "Neyts, Erik C."
  - "van Duin, Adri C. T."
  - "Bogaerts, Annemie"
venue: "Nanoscale"
pdf_sha256: "5af3f1bcafc215281a3807638ae203441d0f584f9fbe91552ab92e9540005bbb"
pdf_path: "papers/Neyts_Nanoscale_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013neyts-venue-c3nr00153a -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Hybrid reactive MD with uniform acceptance force-bias Monte Carlo (MD/UFMC) is used to study graphene formation on ultrathin Ni(100) under high effective precursor flux. The study argue that under these strongly driven conditions a combined deposition–segregation pathway can yield near-continuous graphene-like films by 900 K and above, complementing literature focused on equilibrium segregation (abstract; introduction, extract pages 1–2).

## Methods

**1 — MD application (hybrid MD / UFMC):** The study uses **state-of-the-art hybrid MD** with **uniform acceptance force-bias Monte Carlo (UFMC)** together with the same **ReaxFF** **Ni/C** chemistry line as prior **Ni(111)** graphene growth work (**Meng et al.**, cited in-text). Growth is simulated on **Ni(100)** rather than the more stable **Ni(111)** facet because, on **poly-Ni** substrates, literature cited in the article argues that **(100)** becomes abundant after **graphene synthesis** alongside **(110)** and **(111)** directions, and **Ni(100)** is less closely packed than **Ni(111)** (`papers/Neyts_Nanoscale_2013.pdf`; **`normalized/extracts/2013neyts-venue-c3nr00153a_p1-2.txt`**). The manuscript contrasts **unrealistically high precursor flux** accessible in pure **MD** with **UFMC-modulated** sampling.

**MD numerics not in p1–2 extract:** **N/A —** **timestep**, **supercell atom** totals, **periodic** (**PBC**) details, whether hybrid segments use **NVE**, **NVT**, or **NPT**, **picosecond**/**nanosecond** **production duration**, **thermostat**/**barostat** damping, **target pressure**, **temperature** set points beyond the abstract’s **900 K** mention, and **electric field** are not quoted from the indexed excerpt; read **Nanoscale** **Methods** (**`papers/Neyts_Nanoscale_2013.pdf`**) for authoritative settings.

**Replica / enhanced sampling:** **UFMC** is an **accelerated** **Monte Carlo** augmentation of **MD** (not umbrella/metadynamics); details of **move classes** and **acceptance** bias belong in the **PDF**.

**2 — Force-field training:** **N/A —** **ReaxFF** is **inherited** from prior **Ni/C** growth parametrizations as cited.

**3 — Static QM / DFT-only:** **N/A —** primary tool is **hybrid reactive MD/UFMC** for growth under driven flux.

## Findings

**Outcomes and mechanisms:** **Simulations** predict **nearly continuous graphene** layers at **900 K** and above under the modeled **high-flux** conditions. The **introduction** ties **carbon solubility** in **Ni** (**~2.7 at%** at the **eutectic** **1600 K**, **~0.9 at%** near **900 K**) and much higher **subsurface** solubility (up to **~25%**, **Ni\(_3\)C**-related literature in the text) to why **segregation** routes often yield **multilayer** graphene experimentally, and discusses strategies to **limit bulk dissolution** (e.g., **thinner Ni films**, rapid **saturation** of near-surface layers before **bulk diffusion**) to favor **single-layer** formation.

**Comparisons:** The **Ni(100)** choice and **solubility** arguments are framed against **experimental** **segregation** literature and prior **simulation** work on **Ni(111)** (citations in **`papers/Neyts_Nanoscale_2013.pdf`**).

**Sensitivity / design levers:** **Temperature** (**≥ ~900 K** in the abstract-level prediction), **effective precursor flux** (**MD** vs **UFMC**), and **Ni film thickness / saturation kinetics** appear as levers in the indexed discussion.

**Limitations and outlook:** **UFMC** does not map one-to-one to a single **physical time** scale; modeled **fluxes** can remain above typical **CVD** experiments (**introduction** themes).

**Corpus honesty:** Ground claims in **`normalized/extracts/2013neyts-venue-c3nr00153a_p1-2.txt`**; fragmented lines in the legacy extract dump are **not** quoted verbatim as standalone evidence.

## Limitations

UFMC lacks a strict physical time scale; fluxes remain above typical CVD experiments. Defectivity and comparison to Ni(111) growth remain active caveats in the narrative (introduction, extract pages 1–2).

## Relevance to group

Adri van Duin as coauthor links the ReaxFF Ni/C chemistry used in metal-catalyzed carbon growth studies across the corpus.

## Citations and evidence anchors

- Abstract: mechanism statement and 900 K result.
- Introduction: MD/UFMC rationale, Ni(100) choice, flux discussion (extract pages 1–2).
- DOI: `10.1039/c3nr00153a` (extract footer).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
