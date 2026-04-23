---
id: paper:2022banerjee-venue-manuscript
type: paper
title: "On the Origin of Nonclassical Ripples in Draped Graphene Nanosheets: Implications for Straintronics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - domain:mechanics-tribology
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:reaxff-application
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acsanm.2c02137"
year: 2022
authors:
  - "Riju Banerjee"
  - "Tomotaroh Granzier-Nakajima"
  - "Aditya Lele"
  - "Jessica A. Schulze"
  - "Md Jamil Hossain"
  - "Wenbo Zhu"
  - "Lavish Pabbi"
  - "Malgorzata Kowalik"
  - "Adri C. T. van Duin"
  - "Mauricio Terrones"
  - "E. W. Hudson"
venue: "ACS Appl. Nano Mater."
pdf_sha256: "bd5541a5391f7a04428c9b8ca73dbc29058492b6d1644c578e9cef21b448c0d8"
pdf_path: "papers/Banerjee_Draped_Graphene_ACS_AppNanMat_2022_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022banerjee-venue-manuscript -->

## Summary

!!! note "Corpus PDF note"
    The repository currently registers an ACS Applied Nano Materials **supporting-information** PDF for this `paper_id`. The discussion below follows the article abstract and methods as represented in that ingest; consult the version-of-record article PDF for authoritative pagination. Maintainer catalog (SI-focused ingests): [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

Scanning tunneling microscopy on graphene draped over Cu step edges produces tunable nanoscale ripples. Atomistic simulations reproduce triangular (non-sinusoidal) ripple profiles with a nearly constant apex angle, distinct from classical thin-fabric elasticity. Strain-induced pseudo electric fields create narrow \( \sim 3\,\text{nm} \) p–n–p junctions purely from deformation. The abstract emphasizes that **nanometer-wavelength** ripples violate **continuum fabric** expectations because **in-plane** and **out-of-plane** modes compete, producing a **strain-locked** optimal buckling configuration.

## Methods

!!! note "Corpus note"
    The repository registers the **SI** PDF; figure numbering and the full main-text **STM** protocol follow the **version-of-record** at the DOI.

**1 — MD application (atomistic dynamics).** **Engine / code: LAMMPS** with **ReaxFF**-style **reactive** dynamics to relax **draped** **graphene** over **topography** (see **main article** + **SI** for the exact **parameter** file, **reaxff** spec, and **version**). **System** models represent **CVD graphene** on **copper** draped over **mesoscale** steps/edges, with **height** profiles, **in-plane** strain maps, and **chirality** (armchair vs zigzag) **checks**; atom counts, **supercell** dimensions, and how **PBC** are used for the **drape** appear in the peer-reviewed text. **Ensemble, timestep, and stages:** the summary here follows **NVT**-style equilibration / relaxation to obtain **quasi-static** ripple **shapes**; **thermostat** and **damping** values, full **ps–ns** **segment** lengths, and the **0 K** vs finite-**T** **STM**-matching **protocol** are in the **PDF** (not fully duplicated from the SI alone). **Barostat:** **N/A** for the constant-volume / fixed-cell **drape** **relaxation** as summarized. **Temperature:** **STM**-relevant **temperatures** (including **cryogenic** operation where reported) and any **thermostat** set-points for MD are in the **main Methods**. **Pressure, electric field, enhanced sampling: N/A** in the standard sense of **NPT** production runs, **applied** **E-field** **MD**, or **rare-event** **methods**—**pseudo electric fields** come from post-processing **strain**, not a **static** field in the MD. **Strain and electronics (post-MD / mesoscale):** **Tight-binding**-style or equivalent **treatment** of **Deformation**-induced **pseudoelectric** fields to estimate **\(\sim 3\,\text{nm}\)**-scale **p–n–p** features from the **graphene** **strain** texture is described in the **article** (read those figures in the VOR, not the SI in isolation).

**2 — Force-field training.** **N/A** — the work **uses** a published **ReaxFF** **lineage** for **carbon**-based **draping**; it does not report a new **reoptimization** in this paper.

**3 — Static QM / DFT-only.** **N/A** as a primary new methodology; **ab initio** tools may be cited in passing but the headline comparison is **STM** + **ReaxFF** **drape** **mechanics** + **strain**-based **band** **kinetics**.

**4 — Experiments and imaging.** **STM** of **graphene** on **Cu** with **drape** over **steps**; tip-height **line cuts** and **lateral** **ripples** vs **wavelength**/**amplitude** and **drape** **length** in the **version-of-record**; **figure**-level agreement targets **\(\sim 168{-}170^\circ\)** **apex** angles. Full **tip** **bias** and **temperature** for each **panel** are in the **main** **PDF** (this corpus **SI** may not carry all **main** **figure** labels).

## Findings

**Outcomes and mechanisms.** **Ripple** **profiles** are **triangular** (non-**sinusoidal**), with **bending** concentrated over **a few** **lattice** **constants** at **apices**. The authors argue that **in-plane** vs **out-of-plane** **deformation** **competition** yields a **strain-locked** **buckling** **angle** that is **broadly** **insensitive** to **drape** **geometry**—a **“same angle”** effect at the **nanometer** **scale**—distinct from **continuum** **thin-film** **elastic** **expectations** for long-wavelength **sinusoidal** **ripples**. **ReaxFF**-relaxed **heights** are **compared** to **STM** **shapes** (including **\(\sim 168{-}170^\circ\)** **apices** where the paper **reports** them).

**Comparisons.** **Simulation** is **juxtaposed** with **STM** on the **same** **drape** **morphology**; **pseudogap**-like **consequences** of **local** **strain** are **contrasted** with **continuum** **bending** **laws** for **draped** **membranes** as discussed in the **article**.

**Sensitivity and levers.** The **drape** **wavelength**/**amplitude**, **chirality**, and **drape** **size** (when **swept**) are the key **levers** linking **morphology** to **pseudoelectric** **landscapes**.

**Limitations and corpus honesty.** Citing **\(\sim 3\,\text{nm}\)** **p–n–p** **pseudojunction** **estimates** or **angle** **statistics** from **main** **text**; this wiki’s **SI**-only **pdf_path** is **insufficient** for full **reproduction** of **all** **STM**-match **plots** without the **VOR** **PDF**—see **`## Limitations`** and the maintainer [SI entry](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (local: `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`, section A).
## Limitations

STM samples limited regions; continuum scaling laws are violated only at the nanoscale regime studied here. SI-only PDF in corpus may omit main-text figures. For **retrieval** and **citation**, treat the **DOI** as authoritative for **figure** numbering; when reconciling **STM** line cuts with **simulation** profiles, use the **same** **temperature** and **bias** conditions reported in the **main article** rather than the SI excerpt alone. **Straintronics** readers should link **pseudo** **electric** **fields** to **local** **strain** **gradients** as defined in the **main-text** **figures**, not only the SI panels available in this ingest.

## Relevance to group

Penn State collaboration with van Duin on graphene mechanics and electromechanical coupling.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
