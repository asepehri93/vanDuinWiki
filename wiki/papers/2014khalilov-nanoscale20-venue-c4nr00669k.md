---
id: paper:2014khalilov-nanoscale20-venue-c4nr00669k
type: paper
title: "Microscopic mechanisms of vertical graphene and carbon nanotube cap nucleation from hydrocarbon growth precursors"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: "10.1039/c4nr00669k"
year: 2014
authors:
  - "Khalilov, Umedjon"
  - "Bogaerts, Annemie"
  - "Neyts, Erik C."
venue: "Nanoscale"
pdf_sha256: "297c5d03c491cd3a18a86f843abe779321c45e9d284fde429f8f29ea05904732"
pdf_path: "papers/ReaxFF_others/Khalilov-Nanoscale2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014khalilov-nanoscale20-venue-c4nr00669k -->

Reactive MD with time-stamped force-bias Monte Carlo relaxation on a nickel cluster explores how partially dehydrogenated carbon structures evolve toward caps and overlayers that can seed carbon nanotube nucleation from hydrocarbon precursors.

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Reactive MD on metal nanoparticles shows graphitic networks emerging via vertically oriented, incompletely dehydrogenated carbon islands; further dehydrogenation lets these vertical graphenes cap the particle, spreading a carbon overlayer conducive to nanotube nucleation. The work argues that tuning dehydrogenation extent adds a control knob for CNT nucleation beyond prior models that injected pure carbon only (abstract; introduction, extract). The introduction stresses that many earlier growth simulations assumed instantaneous hydrocarbon decomposition and supplied carbon atoms or dimers directly, omitting explicit hydrogen chemistry on curved nanocatalyst particles, whereas this study follows acetylene or benzene impingement on a finite Ni cluster so hydrogen remains part of the elementary pathway.

## Methods

Simulations combine **MD** with **time-stamped force-bias Monte Carlo (tfMC)** relaxation using **ReaxFF** parameters from **Mueller et al.** for **Ni/C/H** chemistry validated against **QM** for **dehydrogenation barriers** and **clustering** benchmarks. **Acetylene** or **benzene** molecules **impinge** on a **Ni\(_{55}\)** cluster while keeping the **number of gas molecules fixed** (new molecules insert when others adsorb). Post-adsorption structures are relaxed with **tfMC** before additional impingement; **pressure** maps to an **impingement flux** via ideal-gas kinetic theory (abstract; computational details opening, extract pages 1–3). The computational-details section states that combined MD/tfMC with ReaxFF was previously demonstrated to yield CNTs with definable chiralities, motivating the same protocol here for hydrocarbon-fed nucleation.

### 1 — MD application + accelerated relaxation (Ni/C/H)

- **Engine / code:** **Molecular dynamics** combined with **time-stamped force-bias Monte Carlo (tfMC)** relaxation using **ReaxFF** (**abstract**; computational-details opening in `normalized/extracts/2014khalilov-nanoscale20-venue-c4nr00669k_p1-2.txt`); **N/A — explicit program name string not on extract p1–3** (confirm in `papers/ReaxFF_others/Khalilov-Nanoscale2014.pdf`).
- **Ensemble:** **N/A — canonical ensemble (NVT/NVE) not stated on indexed extract pages 1–3** (Nanoscale Methods).
- **System size & composition:** **Ni\(_{55}\)** cluster with **acetylene** or **benzene** impingement; **fixed number** of gas molecules with **reinsertion** upon adsorption (**abstract**/extract).
- **Boundaries / periodicity:** **N/A — explicit box/PBC statement not captured on indexed extract pages 1–3** (full **Nanoscale** computational section).
- **Ensemble / timestep / thermostat / barostat / temperature schedules / electric field / umbrella or metadynamics:** **N/A — not stated on indexed extract pages 1–3** (PDF Methods).
- **Duration / stages:** **Impinge → relax (tfMC) → repeat** as described qualitatively in the extract opener; **N/A — quantitative trajectory lengths not on indexed extract p1–3**.
- **Replica / enhanced sampling:** **tfMC** is an **accelerated relaxation** scheme paired with **MD** (**abstract**), distinct from **umbrella/metadynamics**—**N/A — umbrella/metadynamics not indicated**.

### 2 — Force-field training (reference parameterization)

- **Parent FF / elements:** **ReaxFF** parameters from **Mueller et al.** for **Ni/C/H** with **QM** validation benchmarks for **dehydrogenation barriers** and **clustering** as cited in the article (**abstract**/extract).
- **QM reference / optimization / new fits in this paper:** **N/A — this ingest text emphasizes applying an existing parameterization to nucleation mechanics**; confirm whether additional refits are reported in the full PDF.

## Findings

### Outcomes and mechanisms

On **Ni nanocatalysts**, **graphitic networks** emerge through **vertically oriented, incompletely dehydrogenated** carbon islands. Further **dehydrogenation** causes these **vertical graphenes** to **curve** and **cap** the particle, spreading a **carbon overlayer** that supports **nanotube nucleation** (abstract; extract pages 1–3).

### Comparisons and positioning

The authors contrast their **hydrocarbon-fed** pathway (explicit **hydrogen** chemistry) with earlier growth models that **inject pure carbon** only, arguing that **tuning dehydrogenation extent** is an added **control knob** for **CNT nucleation** (abstract; introduction in extract).

### Sensitivity and design levers

**Dehydrogenation extent** and **precursor choice** (**acetylene** vs **benzene**) enter as qualitative **composition**/**coverage** levers in the narrative summarized from the extract; **quantitative** impingement rates map from **pressure** via ideal-gas kinetic theory in the article’s computational-details section (**extract** pointer).

### Limitations and corpus honesty

Industrial **CVD** feeds and **polydisperse** catalysts are simplified versus experiment (**## Limitations**). **Numerical** MD/tfMC settings beyond the extract window should be taken from **`papers/ReaxFF_others/Khalilov-Nanoscale2014.pdf`**, not invented here.

## Limitations

Simplified precursor and catalyst models relative to industrial CVD feeds and polydisperse catalysts.

## Citations and evidence anchors

- DOI `10.1039/c4nr00669k` (extract footer).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

- Prefer **`papers/ReaxFF_others/Khalilov-Nanoscale2014.pdf`** + **`normalized/extracts/`** for numerical settings beyond the abstract/extract window captured here.
