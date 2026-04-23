---
id: paper:2014chakraborty-combustion-a-do-nanoenergetic
type: paper
title: "Do nanoenergetic particles remain nano-sized during combustion?"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:energetic-materials
  - keyword:lammps
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.combustflame.2013.10.017"
year: 2014
authors:
  - "Purnendu Chakraborty"
  - "Michael R. Zachariah"
venue: "Combust. Flame"
pdf_sha256: "47045d0bda42fdf77db7f1f99f2ae3b4bd25580528896467098ed24f2b67ea96"
pdf_path: "papers/ReaxFF_others/Chakraborthy_Zachariah_Alumina_CombFlame_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014chakraborty-combustion-a-do-nanoenergetic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Barrier and temperature values must be verified in the article.

## Summary

**Reactive MD** (parameterization described in the paper) follows **oxide-coated Al nanoparticle** **doublets** to address why **burning times** of **nanoparticle** **aggregates** can show **sublinear** scaling with **particle size** in experiments. The abstract argues the **native alumina shell** **softens** when **Al cations** **penetrate** from the **molten core**, lowering **effective melting** behavior vs **bulk alumina**; **interfacial electric fields** assist **cation** injection upon heating. **Surface tension** then drives **sintering** on times **comparable** to **reaction** times, so **aggregates** may **coarsen** before **oxidation** completes—challenging naive **“nano”** length scales inferred from **primary particle** sizes alone.

## Methods

### 1 — MD application (ReaxFF reactive MD)

- **Engine / code:** **LAMMPS** with **ReaxFF** for **Al/Al₂O₃**; **Verlet** integration (**Simulation details** in the article; `pdf_path`).
- **System size & composition:** **Oxide-coated Al** **doublets** (simplest aggregate). **8 nm** particles (**~2.5 nm** **Al** core, **~1.5 nm** **oxide** shell) and **16 nm** particles (**~12 nm** core, **~2 nm** shell, **~2×10⁵ atoms**).
- **Boundaries / periodicity:** **Doublet** with **image particle** separated by **~2–3 Å**; full **PBC** details **N/A here**—confirm in **Combust. Flame** PDF.
- **Ensemble:** **N/A —** not spelled out in this wiki summary; confirm constant-volume vs pressure in the manuscript.
- **Timestep:** **Δt = 1.0 fs** (article **Simulation details**).
- **Duration / stages:** **Pseudo-equilibration** at **500 K** after **300 K** relaxation; **~1 ns** at **500 K** for the smaller particle before assembly; **heating ramp ~10¹³–10¹⁴ K/s** from **500 K** toward **≤2000 K** (kept **below bulk alumina melting ~2400 K**) on **nanosecond** timescales (article as summarized here).
- **Thermostat:** **Velocity rescaling** whenever **|T − T_target| > 10 K** (article **Simulation details**).
- **Barostat / pressure:** **N/A —** not stated in the summarized protocol bullets; confirm if **NPT** appears in the PDF.
- **Temperature:** **300 K** relaxation, **500 K** equilibration, then **rapid heating** toward **≤2000 K** as above.
- **Electric field (externally applied):** **N/A —** no applied bias in the summarized setup; the abstract discusses **self-consistent interfacial fields** at the **core–shell** boundary (see **## Findings**).
- **Replica / enhanced sampling:** **N/A —** not used in the protocol summarized here.

### 2 — Force-field training

**N/A —** uses a published **Al/Al₂O₃** **ReaxFF** description (parameter lineage in the article).

### 3 — Static QM

**N/A —** not the primary methodology in the summarized simulation workflow.

## Findings

### 1 — Outcomes and mechanisms

- **Molten Al** drives **Al cations** into the **native shell**, forming a **sub-oxide** that **softens/melts** at **temperatures below** **bulk Al₂O₃ melting**, distinct from **bulk alumina** mechanics.
- A **strong interfacial electric field** assists **cation injection** as the **core** heats, accelerating **shell disordering**.
- **Surface tension** can **fuse adjacent particles** on times **comparable** to **oxidation** timescales, so **aggregates** may **coarsen** before **oxidation** completes—challenging the assumption that **primary nanoparticle size** sets the **effective** **reactive length scale** during **burning** (abstract; `normalized/extracts/2014chakraborty-combustion-a-do-nanoenergetic_p1-2.txt`).

### 2 — Comparisons

- The study is motivated by **experimental** burning-time **scaling** anomalies for **nano-Al** aggregates versus simple power-law expectations (introduction framing in the article).

### 3 — Sensitivity

- **Particle size** (**8 nm** vs **16 nm** constructs) and **heating rate** are part of the simulation design described in the article’s **Simulation details**.

### 4 — Limitations (authored / model)

- **Idealized doublet** geometry vs **polydisperse** powders and **gas-phase** transport—see **## Limitations**.

### 5 — Corpus / KB honesty

- Quantitative **barriers**, **rates**, and **field** strengths should be verified in **`pdf_path`**; this page does not replace the **peer-reviewed** **Combust. Flame** text.

## Limitations

- **Idealized** **doublet** geometry; **real** **powders** have **polydispersity** and **gas-phase** **transport**.

## Relevance to group

**Reactive MD** (**ReaxFF-class**) **combustion** narrative for **metal** **nanoparticles**, adjacent to **energetic materials** interests.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.combustflame.2013.10.017` (`papers/ReaxFF_others/Chakraborthy_Zachariah_Alumina_CombFlame_2014.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
