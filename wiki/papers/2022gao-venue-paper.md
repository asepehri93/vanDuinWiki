---
id: paper:2022gao-venue-paper
type: paper
title: "A reactive molecular dynamics study of bi-modal particle size distribution in binder-jetting additive manufacturing using stainless-steel powders"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:lammps
source_refs: []
doi: ""
year: 2022
authors:
  - "Yawei Gao"
  - "Ana Paula Clares"
  - "Guha Manogharan"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. (publisher proof in corpus)"
pdf_sha256: "a72b48e4df36506c6466e92f54c51ea1e6b3008787eb15fcdc3562bb1a3e412b"
pdf_path: "papers/Gao_PCCP_bimodal_AM_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2022gao-venue-paper -->

## Summary

This wiki entry documents a **publisher proof / galley** PDF (`papers/Gao_PCCP_bimodal_AM_2022_galley.pdf`) associated with a **Physical Chemistry Chemical Physics** study (group authorship includes **Yawei Gao**, **Ana Paula Clares**, **Guha Manogharan**, and **Adri C. T. van Duin**) on **binder-jetting additive manufacturing** of **stainless-steel** powders where **bi-modal particle size distributions** are used as a processing knob. The **graphical abstract** and front matter in the proof establish the headline approach: **reactive molecular dynamics** is used to connect **powder packing** and **interparticle** chemistry to **consolidation** phenomena relevant to **jet-binder** **AM** routes for **metallic** powders. In this workspace the **DOI** field is intentionally left blank pending confirmation against the **final** **issue** metadata; operators should treat numerical **kinetic** and **microstructural** claims as **unknown** until reconciled with the **version-of-record** PDF. The page’s purpose is therefore **manifest transparency**: it records what the corpus stores and what remains **unverified** from **proof** pages alone.

## Methods

From the proof-level description, the study’s intent is to vary **bi-modal** **size** mixtures representative of **industrial** powder feeds and to simulate **reactive** **sintering**/**bonding** events that accompany **binder** interaction and **thermal** processing in **AM**-like scenarios. **ReaxFF-class** simulations (as implied by the **reactive MD** framing and **van Duin** involvement) would typically require explicit statement of **interatomic** parameterization for **Fe/C/O/H** chemistry, **timestep**, **thermostat**, **boundary conditions**, and **system sizes**; these details are **not** stably recoverable from the **partial** **extract** and **galley** layout tracked here. Readers should import **Methods** from the **published PCCP** article and any **supporting information** rather than relying on this proof file for **protocol** reproduction.

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.
## Findings

No **quantitative** **findings** (densification metrics, **stress–strain** outcomes, **sintering** neck growth rates, or temperature windows) should be asserted from the **proof** ingest alone; the **partial** **extraction_quality** flag reflects **publisher** boilerplate and incomplete text capture rather than a curated negative result. Once the **VOR** PDF is linked in the manifest, this page should be updated to **point** to the canonical wiki slug with **full** **Summary/Methods/Findings** prose grounded in the **final** text. Until then, the responsible scientific statement is **provenance-only**: the corpus contains a **galley** path for a **PCCP** **reactive MD** **AM** paper with **van Duin** co-authorship. **Operators** should prioritize locating the **final** **DOI** and **PDF** path in **`papers/`**, then **clone** the **headline** **methods/results** structure from the **published** text onto a **new** **VOR** wiki slug rather than **speculating** **numerical** outcomes from **layout** **fragments**. **Binder-jetting** **microstructures** (**particle** **packing**, **pore** **networks**) can dominate **sintering** **kinetics** even when **ReaxFF** **chemistry** is **correct**, so **multiscale** **continuum** **models** may still be required for **part-scale** **predictions**.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

**Galley/proof PDFs** may differ in **equations**, **tables**, and **author affiliations** from the **journal** version; citations should not use **proof** pagination. The missing **DOI** in front matter signals incomplete **bibliographic** grounding in this repository state—resolve before treating the entry as citation-ready.

## Relevance to group

**ReaxFF**-style reactive simulation of **metal powder** consolidation in an AM context; **van Duin** co-authorship ties to group parameterization practice.

## Citations and evidence anchors

- Prefer the journal version-of-record DOI once confirmed against the published PCCP article.

## Related topics

- [[reaxff-family]]
