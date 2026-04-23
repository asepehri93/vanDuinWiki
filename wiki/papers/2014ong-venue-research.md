---
id: paper:2014ong-venue-research
type: paper
title: "Lithium ion solvation and diffusion in bulk organic electrolytes from first-principles and classical reactive molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:aimd
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:galley-or-proof-pdf
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/jp508184f"
year: 2015
authors:
  - "Mitchell T. Ong"
  - "Osvalds Verners"
  - "Erik W. Draeger"
  - "Adri C. T. van Duin"
  - "Vincenzo Lordi"
  - "John E. Pask"
venue: "J. Phys. Chem. B 119 (4), 1535–1545 (2015)"
pdf_sha256: "9b819669b8064e558f9cb99583f4b94f7f5feb24010fb09ce7fbaeef7a79fd4a"
pdf_path: "papers/Ong_JPCB_IL_DFT_ReaxFF_2014_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014ong-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **J. Phys. Chem. B** article (`doi`). The corpus file is an **author proof** dated **2014**; publication is **2015**—front matter matches the **journal**.

## Summary

**First-principles MD** of **Li⁺** and **PF₆⁻** in bulk **ethylene carbonate (EC)**, **ethyl methyl carbonate (EMC)**, and **EC/EMC** mixtures with **LiPF₆**. **Li⁺** coordinates to **carbonyl** and/or **ether oxygens** (and sometimes **PF₆⁻**) with a broadly **tetrahedral** first shell whose composition depends on **solvent**. **Diffusion coefficients** are larger in **EMC** than **EC**, correlating with **weaker Li⁺ solvation**; **PF₆⁻** diffuses faster with a **looser** solvation shell. The work is paired in the title with **classical reactive MD** analysis in the full paper (see Methods therein). Together, the **AIMD** and **ReaxFF** strands aim to connect **atomistic** solvation structure to **continuum-relevant** transport trends for **carbonate** electrolytes.

## Methods

### First-principles MD (bulk carbonate electrolytes)

- **FPMD/DFT** simulations treat **LiPF₆** dissolved in bulk **ethylene carbonate (EC)**, **ethyl methyl carbonate (EMC)**, and **EC/EMC** mixtures to resolve **Li⁺** and **PF₆⁻** solvation and **diffusion** statistics (**Summary**; **LLNL–Penn State** collaboration).

### Classical reactive MD (paired in the article title)

- The manuscript’s **classical reactive MD** strand uses **ReaxFF** (details in **JPCB** Methods) to reach larger systems/longer times than **AIMD**, with explicit comparison targets enumerated in the article (**Summary**).

### Proof vs version-of-record

- Local `pdf_path` is an **ACS author proof**; publication metadata in front matter reflects **J. Phys. Chem. B** **119**, **1535–1545** (**2015**). Prefer the **VOR** PDF for **pagination** and **figure** labels.

### Extract anchor

Abstract-level pointers: `normalized/extracts/2014ong-venue-research_p1-2.txt` plus **`papers/Ong_JPCB_IL_DFT_ReaxFF_2014_proof.pdf`** (ACS author proof; published article **J. Phys. Chem. B** **119**, **1535–1545**, **2015**).

### 1 — MD application (atomistic dynamics)

- **First-principles MD:** **DFT-based** (**FPMD**) trajectories treat bulk **LiPF₆** in **EC**, **EMC**, and **EC/EMC** mixtures (**Summary**; full kinetics in **JPCB**).
- **Classical reactive MD:** **ReaxFF** strand paired in the title for larger systems/longer times than **AIMD** (**Summary**); **N/A — integrator, timestep, thermostat, equilibration/production ns**, and thermostat labels not reproduced here—read the **Methods** section of the **published** **PDF**.
- **Engine / code:** **N/A — software** not named in the short wiki summary layer.
- **System size & composition:** **N/A — atom totals** not copied into this page from the proof/extract.
- **Boundaries / periodicity:** Bulk **liquid** electrolyte cells imply **PBC** in standard practice, but **N/A — explicit boundary wording** not checked on this slug—confirm in **JPCB**.
- **Ensemble:** **NVT**/**NPT** choices for **AIMD** vs **ReaxFF** segments are **N/A — not stated** on this page; see article.
- **Temperature:** **30 °C** appears in the wiki’s abstract-derived discussion of **experimental diffusion** ranges used for context (extract-backed summary on file).
- **Pressure:** **N/A — not emphasized** in the indexed abstract layer summarized here.
- **Electric field:** **N/A — not stated** in the excerpted discussion used here.
- **Replica / enhanced sampling:** **N/A — not stated** here.

### 2 — Force-field training

**N/A —** this page is an **application** note; any **ReaxFF** **parameter** updates belong to the **JPCB** **Methods**/**SI**, not this summary.

### 3 — Static QM / DFT-only (**AIMD** block)

**Functional**, **dispersion**, **basis**, **k**-sampling, and **production** lengths for **FPMD** are defined in **J. Phys. Chem. B** **119**, **1535–1545**—**N/A — not duplicated** on this wiki stub.

## Findings

### Outcomes and mechanisms

**Li⁺** coordinates through **carbonyl** and/or **ether oxygens** (sometimes **PF₆⁻** participates), with a broadly **tetrahedral** first shell whose composition depends on **solvent** (abstract).

### Comparisons

**Li⁺ diffusion coefficients** are **slightly larger in EMC than EC**, correlating with **weaker Li⁺ solvation**; **PF₆⁻** diffuses faster with a **weakly bound, poorly defined** first shell (abstract). Experimental **diffusion** ranges cited for context include order **~(1–8)×10⁻⁶ cm² s⁻¹** for **Li⁺** at **30 °C** and **~(1.5–4.5)×10⁻⁶ cm² s⁻¹** for mixed **EC/EMC** depending on salt concentration (discussion text present in the corpus extract file referenced above).

### Sensitivity and outlook

Solvent identity (**EC** vs **EMC** vs mixtures) modulates **solvation** strength and inferred **transport** trends in the abstract framing; the manuscript positions these results as input to **parameterizing**/**validating** larger-scale **reactive** models.

### Corpus honesty

Local **`pdf_path`** is an **ACS author proof**; cite **pagination**/**figures** from the **version-of-record** **JPCB** **PDF** when possible ([[2014ong-venue-research]] maintainer note links **NON_PRIMARY_ARTICLE_PAPER_SLUGS.md**).

## Limitations

Bulk liquid focus (not full **SEI** chemistry); proof PDF; DFT/FF costs limit duration and system composition sweep.

## Relevance to group

Core **LLNL–Penn State** **electrolyte** collaboration including **van Duin**; central to **battery electrolyte** narrative in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1021/jp508184f — J. Phys. Chem. B **119**, 1535–1545 (2015).

## Reader notes (navigation)

- Corpus **`pdf_path`** is an ACS **author proof**; the published article is **J. Phys. Chem. B** **119**, **1535–1545** (**2015**). Maintainer catalog: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (section **D**, `2014ong-venue-research`).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
