---
id: paper:2023nadire-nayir-j-phys-chem-modulation-effect
type: paper
title: "Modulation Effect of Substrate Interactions on Nucleation and Growth of MoS2 on Silica"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c01010"
year: 2023
authors:
  - "Nadire Nayir"
  - "Stephen Bartolucci"
  - "Tao Wang"
  - "Chen Chen"
  - "Joshua Maurer"
  - "Joan M. Redwing"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "903a1e7038258f82a5118123f73388320438654b7b9322498c4065088053243b"
pdf_path: "papers/Nayir_MoS2_silica_JPCC_2023_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023nadire-nayir-j-phys-chem-modulation-effect -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *J. Phys. Chem. C* article identified by `doi`, `title`, and `pdf_path`. This slug uses the **online / VOR-class** PDF in the corpus (`Nayir_MoS2_silica_JPCC_2023_online.pdf`).

## Summary

Large-area MoS\(_2\) growth by chemical vapor deposition on insulating SiO\(_2\) supports is sensitive to surface hydroxylation: silanol groups provide reactive anchors for oxide precursors, whereas dehydroxylated silica can be comparatively passive. This study integrates **ReaxFF reactive molecular dynamics**, **density functional theory** benchmarks, and **experimental** CVD trials to show how **substrate hydroxylation** modulates MoO\(_3\) precursor chemistry and subsequent **sulfurization** toward MoS\(_2\). The paper argues that hydroxylated surfaces thermodynamically and kinetically favor reactions that nucleate molybdenum oxide species on the support, enabling growth pathways that remain suppressed on more dehydroxylated silica under comparable feeds. Together, the results frame **surface engineering** (tuning silanol coverage) as a handle on **nucleation density**, **effective growth temperature**, and film continuity for MoS\(_2\) on oxide supports.

The **computational** strand is intentionally **interface-first**: by constructing **oxide** **slabs** with controlled **silanol** **density**, the authors isolate how **precursor** **adsorption** and **reduction** change when the **support** can participate in **acid–base**-like interactions and **Mo–O–Si** coupling, as opposed to treating SiO\(_2\) as an inert scaffold.

## Methods

**Force-field (block 2 — preface).** The JPCC work develops a **trainable** **ReaxFF** for **CVD** of **MoS\(_2\)** from **MoO\(_3\)** and **S\(_2\)** or **H\(_2\)**S (and related steps); **FF** development and **QM** training set details are in the **SI**.

### 1 — MD application (ReaxFF MD with ADF/Amsterdam Modeling Suite)

- **Engine / code:** **ReaxFF** **molecular dynamics** (RMD) with the **ADF/ReaxFF** **simulation** **software** stack cited in the article; **reactive** **snapshots** processed with **OVITO** and **VESTA** (JPCC *Methods*).
- **Time integration / timestep:** **Verlet** (velocity) integration with **0.25 fs** timestep; **PBC** in **all** **three** directions; **NVT** ensemble; **Berendsen** **thermostat** with **100 fs** **damping** (as stated in *J. Phys. Chem. C* for this work).
- **System construction — amorphous silica and hydroxylation (Figure 1 path):** **150** **SiO\(_2\)** “molecules” in a **50 Å** cubic box, heated to **1000 K** at **0.005** **K/ns**, then **1 ns** equilibration; resulting **a-SiO\(_2\)** is further exposed to **200** **H\(_2\)** in a **50 Å** box at **1000 K** for **1 ns** to make **surface** **—OH** and **dehydroxylated** (non-passivated) motifs as in the figures. **N/A** here for every atom count of each subfigure not copied from the same paragraph in the main text.
- **MoO\(_3\)**-only and **chalcogen** exposure:** multiple protocols at **~1000–2000** **K** with **~2.5 ns** **equilibration** segments, **~30** **Å** **boxes** and **50**–**200**-molecule **gas** loads of **MoO\(_3\)**, **S\(_2\)**, **H\(_2\)S** as in §2.2.1; includes **heating** at **0.005** **K/ns** to **1000** **K** + **1 ns** **equilibration** for the **50** **MoO\(_3\)/silica** “silica only” case and two-stage **MoO\(_3\)+S** (or H\(_2\)S) **mixed** **anneals** per the article. **N/A** for every variant not recited in one paragraph—**full** table is in the paper and **SI**.
- **Barostat / pressure / electric field / enhanced sampling:** **NVT**-style gas-phase/oxide handling as described; **N/A** — no **NPT** **or** **barostat** called out in the excerpted **Methods** lines above; **N/A** — no **E-field**; **N/A** — no **metadynamics/umbrella**; **ts**-search for one **H-bonded** path uses **bond** **restraints** in **MD** to reach a DFT product **structure** (§2.2.1, **H-bonded** O–H / **Mo**–O**/**Si**–O** **restraints** as printed).

### 2 — DFT (static, benchmark)

- **Code / setup (non-exhaustive):** **Jaguar**-based (nonperiodic) and periodic examples as in **§2.3**; **B3LYP** (and other settings) in the **JPCC** *Methods*—reproduce **from** the **VOR** **PDF/SI** for **functional**, **basis**, and **k**-sampling, because this wiki only summarizes headlines.

### 3 — Experiment (CVD, §2+)

- **CVD** growth of **MoS\(_2\)** on **treated** **fused** **silica** and **comparative** **substrates** with **O\(_2\)/Ar** and **H\(_2\)**-anneal/oxidation steps—**imaging** links **nucleation** contrast to **Ga⁺-beam**-style **treatments** in **Figure 1**; **N/A** for a full table of **T**, **P**, **flow** **ssccm** here (see article **Experimental** and **SI** for numbers).

**Corpus / KB honesty.** The wiki **paragraphs** above are checked against the *JPCC* **online** PDF; **reactor** and **HRTEM** **conditions** for **all** **panels** are **in** the full article.


## Findings

### Substrate chemistry effect

**Dehydroxylated** silica is comparatively **inert** to **MoO\(_3\)** in emphasized conditions; **hydroxylated** surfaces support **Mo oxide** chemistry and **nucleation**.

### Growth facilitation

**OH** promotes **precursor anchoring** and **sulfurization** toward **MoS\(_2\)**; authors argue **lower effective growth T** vs less reactive supports.

### Experiment–simulation link

**Qualitative** consistency: **microscopy** shows **where** islands form; models rationalize **OH-rich** **MoO\(_x\)** binding—**barriers/coverage** in **primary** text.

## Limitations

ReaxFF for Mo–S–O–Si chemistry inherits training limitations; experiments provide qualitative rather than atom-resolved operando mapping of every intermediate. Long-timescale coalescence and grain-boundary evolution are not fully captured in atomistic runs.

## Relevance to group

2DCC / Penn State collaboration linking **ReaxFF** to **TMD CVD** on oxides with **Joan Redwing**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpcc.3c01010](https://doi.org/10.1021/acs.jpcc.3c01010) (`papers/Nayir_MoS2_silica_JPCC_2023_online.pdf`).

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
- [[2023nayir-venue-manuscript]]
