---
id: paper:2013huang-venue-paper-4
type: paper
title: "Reactive adsorption of ammonia and ammonia/water on CuBTC metal-organic framework: A ReaxFF molecular dynamics simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:zeolite-porous
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1063/1.4774332"
year: 2013
authors:
  - "Liangliang Huang"
  - "Teresa Bandosz"
  - "Kaushik L. Joshi"
  - "Adri C. T. van Duin"
  - "Keith E. Gubbins"
venue: "The Journal of Chemical Physics"
pdf_sha256: "f1e622236c903442b8bac73d9c2ccee333f6d1f47315b676f89b4c9e4ed0f723"
pdf_path: "papers/Huang_Joshi_MOF_JCPSA6_138_3_034102_1.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013huang-venue-paper-4 -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed article** identified by `doi`, `title`, and `pdf_path` in the front matter. For exact numbers and figures, use the published paper and `normalized/extracts/2013huang-venue-paper-4_p1-2.txt`.

## Summary

ReaxFF molecular dynamics is used to study **reactive adsorption of NH\(_3\)** on **dehydrated CuBTC (HKUST-1)**, including temperature- and concentration-dependent framework stability and **NH\(_3\)/H\(_2\)O** mixtures. The work emphasizes chemisorption at **Cu** sites, partial framework response to ammonia, and a **critical NH\(_3\) loading** (about **one NH\(_3\) per Cu**) beyond which collapse behavior changes, with **water** moderating ammonia uptake and stabilizing the framework under some conditions.

## Methods

**ReaxFF** reactive MD (**RMD**) used a parameter set that **merges prior Cu/O/H work with the published glycine ReaxFF** (shared O/H functions; non-bonded C/Cu from combination rules), **retrained** so the combined field describes **CuBTC** and its interaction with **NH\(_3\)** and **H\(_2\)O** (parameter tables in supporting information of the article). The **dehydrated CuBTC** model starts from the **hydrated** crystal geometry with coordinated waters removed. Adsorbates were placed in **channels and tetrahedral pockets** with a **3.0 Å** minimum separation to avoid overlaps.

Simulations used a **1×1×1** periodic cell of dehydrated CuBTC (**Cu\(_{48}\)C\(_{288}\)O\(_{192}\)H\(_{96}\)**), i.e. on the order of **10³ atoms** in the framework **supercell**, plus the reported numbers of **NH\(_3\)** and/or **H\(_2\)O** **adsorbate** **atoms**. Calculations were run in the **NPT** ensemble with a **Verlet** integrator, **time step 0.25 fs**, **Berendsen** thermostat and barostat (**damping 100 fs** and **2500 fs**, respectively), and trajectories stored every **50 fs**; **equilibration** and **production** segment lengths in **ps**/**ns** are given in the article’s protocol tables (**`papers/Huang_Joshi_MOF_JCPSA6_138_3_034102_1.pdf`**).

**Water stability** scans covered **301–389 K** with **12–196 H\(_2\)O** molecules (**0.25–4.0** equivalents per Cu site, following a prior NMR study cited in the paper). **NH\(_3\)** loading followed experimental uptake at **301 K, 318 K, and 348 K** (**120, 88, and 63 NH\(_3\)**, respectively, in the **1×1×1** cell). **NH\(_3\)/H\(_2\)O** mixtures included **24/120**, **48/120**, and **96/120** **H\(_2\)O/NH\(_3\)** ratios (among the cases reported).


## Findings

At **moderate temperature**, dehydrated CuBTC tolerates water up to about **4 H\(_2\)O per Cu** without loss of **hydrostatic stability**, whereas at **550 K** collapse can occur even at **1 H\(_2\)O per Cu**. **NH\(_3\)** in channels and micropores **chemisorbs at Cu** rather than pairing as **NH\(_3\) dimers**. **Equimolar Cu\(_2\)(NH\(_2\))\(_4\)** and **(NH\(_4\))\(_3\)BTC**-like motifs appear at **348 K**, described as **consistent with prior experiments**. **Partial framework collapse** upon NH\(_3\) adsorption can occur while **Cu–Cu dimer** motifs remain stable under the conditions sampled. The work identifies a **critical NH\(_3\)** loading of about **one NH\(_3\) per Cu**: depending on whether the NH\(_3\) concentration is **below or above** this threshold, the dehydrated framework can remain stable to **378 K** or **collapse at 250 K**, respectively. For **H\(_2\)O/NH\(_3\)** mixtures, water **does not** show strong direct interaction with **Cu** in the same sense as ammonia, but it **suppresses chemisorbed NH\(_3\)** and **stabilizes** the framework to some extent.

## Limitations

ReaxFF accuracy depends on the Cu/MOF and amine parameterization; long-time equilibria and polydisperse experimental samples may require larger cells and longer runs than reported.

## Reader notes (navigation)

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]] (peripheral; MOF focus)
