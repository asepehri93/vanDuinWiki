---
id: paper:2020rajabpour-carbon-174-2-low-temperature-carbonization
type: paper
title: "Low-temperature carbonization of polyacrylonitrile/graphene carbon fibers: a combined ReaxFF molecular dynamics and experimental study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - material:graphene-carbon-nano
  - material:polymer-organic
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
  - keyword:polymer
  - keyword:validation-experiment
  - keyword:berendsen-thermostat
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2020.12.038"
year: 2020
authors:
  - "Siavash Rajabpour"
  - "Qian Mao"
  - "Zan Gao"
  - "Mahdi Khajeh Talkhoncheh"
  - "Jiadeng Zhu"
  - "Yosyp Schwab"
  - "Malgorzata Kowalik"
  - "Xiaodong Li"
  - "Adri C. T. van Duin"
venue: "Carbon"
pdf_sha256: "5326738f97a573e7f68b2007debc319c7fa423523939450a44fcb26d65a0e6fd"
pdf_path: "papers/Rajabpour_Carbon_2021_lowT_carbonization.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020rajabpour-carbon-174-2-low-temperature-carbonization -->

## Summary

**ReaxFF MD** of oxidized **polyacrylonitrile (PAN)** with **graphene** explores catalytic **edge and N/O** chemistry during **accelerated-temperature** trajectories; **experiments** compare **PAN** vs **PAN/graphene** carbon fibers carbonized at **1250 °C** vs **1500 °C**. The simulation narrative emphasizes **graphene edges** and **heteroatom** groups as nucleation seeds that accelerate alignment of carbon rings and graphitic growth sequences. Experiments report large **tensile strength** and **Young’s modulus** gains for graphene-containing fibers carbonized at **1250 °C** relative to neat PAN fibers carbonized at **1500 °C**, framing energy/cost benefits of lower-temperature processing enabled by graphene. The **process** message is **not** merely “add graphene,” but **use** **graphene** to **catalyze** **graphitization** chemistry so **lower furnace** temperatures achieve **superior** **mechanical** properties than **higher-T** **neat** **PAN** routes.

## Methods

- **ReaxFF MD:** Oxidized PAN models with graphene inclusions (see article for system construction); **NVT** equilibration **60 ps** at **300 K**; **five** snapshots from the last **5 ps** (1 ps spacing) are heated to **2200, 2500, or 2800 K** at **10 K/ps**, then held **1 ns** at each target temperature to sample high-temperature chemistry on MD timescales.
- **Integrator:** **0.25 fs** timestep (validated vs **0.10 fs** at **2800 K** in SI); **Berendsen** thermostat with **100 fs** damping (as stated).
- **Experiments:** Carbonization of PAN and PAN/graphene fibers with mechanical testing (values in abstract).

**MD application (ReaxFF).** The *Carbon* paper uses **ReaxFF-based reactive MD** in **3D** **PBC** supercells of **oxidized** **PAN** with **graphene** inclusions (full **stoichiometry** in `pdf_path`). The protocol summarized here: **NVT** equilibration **60 ps** at **300 K**; **five** snapshots from the last **5 ps**; heating **10 K/ps** to **2200, 2500, or 2800 K**; **1 ns** holds at each **target** **temperature**; **0.25 fs** timesteps (cross-checked vs **0.10 fs** at **2800 K** in **SI**); **Berendsen** thermostat, **100 fs** damping. **Barostat: N/A —** **NVT** **stages** as written. **Pressure: N/A —** not a **barostat** **study** in the **MD** protocol quoted. **Electric field: N/A —** not used. **Umbrella / metadynamics / replica exchange: N/A —** not used.

## Findings

- MD mechanism narrative: **graphene edges** plus **N/O** functionality act as **catalytic seeds** promoting ring alignment and graphitic cluster formation relative to oxidized PAN alone.
- Experiments: **PAN/graphene** fibers at **1250 °C** show **~91%** higher strength (**632 → 1207 MPa**) and **~101%** higher modulus (**88 → 177 GPa**) compared to **PAN-only** at **1500 °C** (abstract values).
- The **2200–2800 K** **MD** windows are **acceleration** **strategies**; the paper uses them for **qualitative** **reaction** **pathways**, not as direct **furnace** **timelines**.

**Corpus / versions:** the **uncorrected-proof** PDF is tracked as **`[[2020rajabpour-venue-paper]]`**; this page uses the **VOR** `pdf_path` **above** for table-ready **mechanics** **numbers** when they **diverge**.

## Limitations

Simulations use elevated temperatures to accelerate chemistry vs furnace protocols; quantitative one-to-one mapping to factory carbonization schedules requires caution. **Fiber** **mechanics** also depend on **misalignment**, **voids**, and **surface** **defects** not represented in **atomistic** **reaction** **pathways**; treat **experimental** **modulus** and **strength** as **structure**-sensitive **metrics** even when **chemistry** trends align. **Graphene** **loading** fractions and **dispersion** **quality** in **precursor** **fibers** can shift **effective** **catalysis** relative to **ideal** **MD** **geometries**.

## Relevance to group

Penn State chemical/mechanical engineering co-authorship with van Duin; UVA mechanical testing collaboration.

## Reader notes (navigation)

- [[2020rajabpour-venue-paper]] (Elsevier proof PDF duplicate). Maintainer catalog: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (proof/galley duplicate handling).
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
