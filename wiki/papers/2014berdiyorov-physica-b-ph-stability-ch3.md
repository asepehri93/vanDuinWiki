---
id: paper:2014berdiyorov-physica-b-ph-stability-ch3
type: paper
title: "Stability of CH₃ molecules trapped on hydrogenated sites of graphene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:dft-static
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1016/j.physb.2014.07.046"
year: 2014
authors:
  - "G. R. Berdiyorov"
  - "M. V. Milošević"
  - "F. M. Peeters"
  - "Adri C. T. van Duin"
venue: "Physica B"
pdf_sha256: "31daa5a56014794361e7919fe2a8e8782fb81f00a7631468bb10d258bb5f1888"
pdf_path: "papers/Berdiyorov_CH3_graphene_PhysicaB_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014berdiyorov-physica-b-ph-stability-ch3 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Transport spectra and energies must be verified in the article.

## Summary

**ReaxFF MD** explores **thermal stability** of **CH₃** on **graphene** when a **nearby** **chemisorbed H** is present vs **pristine** graphene. The abstract reports **stronger pinning** of **CH₃** adjacent to **H** due to differing **adhesion** and **migration** energetics. **DFT** **transmission** calculations for **nanoribbons** show **extra** **localized-state** features in the **CH₃–H** configuration relative to **CH₃** on **pristine** graphene, linking **stability** to **detectable** **electronic** signatures for **sensing** scenarios. The combined **dynamics + transport** workflow targets scenarios where **partial hydrogenation** coexists with **adsorbed radicals** on graphene, a common motif in functionalization and edge chemistry.

## Methods

- **ReaxFF MD:** **200-atom** graphene supercells with **one chemisorbed H** plus **CH₃**, **3D periodic** along the sheet; **conjugate-gradient** relaxation, then **heating to 2500 K** at **20 K/ps** in **NPT** with **Berendsen** controls (**T** damping **0.25 fs**, **P** damping **1 ps**), followed by **500 ps NPT** sampling at each target **T** (**T**/**P** damping **100 fs / 5 ps**), **Δt = 0.25 fs**, **10 velocity ensembles** per temperature.
- **DFT transport:** **NEGF** **transmission** calculations on **graphene nanoribbons** compare **CH₃** on **pristine** sites vs **CH₃–H** complexes (**Section 2**/**3** in the article).
- **Sampling:** Multiple velocity ensembles per target temperature are used so that **thermally activated** hopping statistics are not inferred from a single short trajectory alone.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive MD** with **ReaxFF** as above; integrator package **N/A — not stated** on this wiki page (see `papers/Berdiyorov_CH3_graphene_PhysicaB_2014.pdf`). **System:** **200-atom** graphene supercells with **one** chemisorbed **H** plus **CH₃**, **3D PBC** in-plane. **Boundaries:** periodic supercell with **3D PBC** as described. **Ensemble:** **NPT** with **Berendsen** thermostat (**T** damping **0.25 fs** during ramp; **100 fs** during **500 ps** sampling stages) and barostat (**P** damping **1 ps** ramp, **5 ps** production). **Timestep:** **0.25 fs**. **Duration / stages:** **conjugate-gradient** relaxation; **heat 20 K/ps** to **2500 K**; **500 ps NPT** holds at each sampled **T**; **10** velocity ensembles per **T**. **Temperature:** up to **2500 K** ramp, then staged sampling. **Pressure:** **NPT** with stated **Berendsen** damping (article). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** applies published **ReaxFF** parameters, not a new fit.

**3 — Static QM / DFT-only.** **NEGF** transmission on **nanoribbons** compares **CH₃** on pristine sites versus **CH₃–H** motifs (**article**); **functional / basis** details **N/A — not duplicated** here.

## Findings

- **ReaxFF** tracks **migration vs desorption times** for **CH₃** as a function of **temperature**; with **adjacent H**, **CH₃** remains **bound** to **higher T** than on **pristine** graphene (the paper quotes stability up to **~1300 K** for **isolated CH₃** within **0.5 ns** trajectories, increasing when the **CH₃–H** motif forms).
- **DFT transmission spectra** gain **extra peaks** from **localized states** tied to the **CH₃–H** complex, absent for **CH₃** on **pristine** graphene, supporting a **spectroscopic** handle for **selective detection** scenarios discussed by the authors.
- The authors connect **longer residence** of **CH₃** near **H** to **stronger** interaction motifs that **scatter** carriers differently than bare methyl adsorption, motivating device concepts where **local chemistry** maps to **conductance** fingerprints.
- **Compared to pristine graphene:** **adjacent H** changes **adhesion**/**migration** energetics and **DFT** **transmission** fingerprints (**Summary** / **Findings**).
- **Sensitivity:** **thermal stability** is tracked vs **temperature** and **velocity ensemble** sampling (**Methods**).
- **Limitations / outlook:** **idealized ribbons** omit **substrate** disorder and **experimental** imaging conditions (**## Limitations**).
- **Corpus honesty:** transport **plots** and full **MD** diagnostics are **PDF-grounded** beyond this summary.

## Limitations

- **Idealized** **ribbons** and **coverage**; **experimental** **TEM** contexts in references are not fully reproduced here.

## Relevance to group

**Adri C. T. van Duin** coauthors; couples **ReaxFF** **dynamics** with **DFT** **transport** for **functionalized** **graphene**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.physb.2014.07.046` (`papers/Berdiyorov_CH3_graphene_PhysicaB_2014.pdf`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
