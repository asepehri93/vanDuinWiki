---
id: paper:2012jeon-venue-rsc-cp-2
type: paper
title: "Nanoscale oxidation and complex oxide growth on single crystal iron surfaces and external electric field effects"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:oxides-ceramics, domain:alloys-metallurgy, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1039/c2cp43490c"
year: 2013
authors: ["Jeon, Byoungseon", "Van Overmeere, Quentin", "van Duin, Adri C. T.", "Ramanathan, Shriram"]
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "7ef19c15c7329975b7bc6b70f26bffc88538178d5d05dc084d54350b0ba214d2"
pdf_path: "papers/Jeon_PCCP_Iron_Efield_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012jeon-venue-rsc-cp-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This PCCP study uses **ReaxFF reactive MD** to investigate **early-stage oxidation** and **nanoscale oxide growth** on **Fe(100), Fe(110), and Fe(111)** across temperature and with an optional **external electric field (~10 MV/cm)**. At **300 K** over **~1 ns**, oxidation kinetics decreases **(110) > (111) > (100)**; higher temperature accelerates oxidation. The mechanism narrative in the excerpt emphasizes early **oxygen interstitial transport** producing **non-stoichiometric wüstite-like** regions, evolving toward more stoichiometric **wüstite/hematite** character as the film thickens, with increasing **cation outward transport**. Post-growth **relaxation** between **600–1500 K** yields **Arrhenius** estimates for **oxygen diffusion activation energies** ~**0.32, 0.26, 0.28 eV** on (100), (110), (111), respectively. The field **accelerates early oxidation** via interstitial oxygen transport but approaches a **self-limiting thickness**; effects on **activation energy** are described as **minimal** while slightly promoting **cation outward migration**.

Introduction motivation ties iron oxidation to corrosion and passivation across technologies and notes that **electric fields** can appear near surfaces in electrochemical or charged environments, so including **~MV/cm**-class fields alongside thermal oxidation tests probes whether field-assisted transport changes early film growth kinetics on low-index facets.


## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF** is used for **dry oxidation** of **bcc Fe** slabs with **~32 Å** metal thickness, **vacuum** along the surface normal (**z**), and **3D PBC** (**\(a=2.870\) Å** lattice constant stated). **Fe(100)** (**2662 Fe**, **31.57×31.57×31.57 Å³**), **Fe(110)** (**2816 Fe**, **32.47×31.57×32.47 Å³**), and **Fe(111)** (**3120 Fe**, **32.47×35.15×32.31 Å³**) cells are reported (Sec. 3.2, **`pdf_path`**). Substrates are thermalized **10 ps** at the oxidation temperature before **O₂** insertion (Sec. 3.2).

- **Engine / code:** **ReaxFF** **reactive MD**; **N/A —** MD software package not named on the indexed excerpt pages used for this wiki pass.
- **System size & composition:** Stoichiometries and supercells as above; **O₂** supply via a **controlled insertion** protocol (pairs inserted when prior oxygen is consumed; randomized **x/y** placement; initial normal velocities scaled to temperature) (Sec. 3.2, **`pdf_path`**).
- **Boundaries / periodicity:** **Slab + vacuum** with **PBC** (Sec. 3.2).
- **Ensemble:** **NVT** (indexed excerpt + Sec. 4.1 context on **`pdf_path`**).
- **Timestep:** **1 fs** (Sec. 4.1, **`pdf_path`**).
- **Duration / stages:** Oxidation trajectories run to **1 ns** at **300 K** and **900 K** (Sec. 4.1, **`pdf_path`**); additional **600–1500 K** **relaxation** stages are used for **diffusion**/**Arrhenius** extraction (Sec. 4.2–4.3, **`pdf_path`**).
- **Thermostat / barostat:** **N/A —** thermostat/barostat algorithm names are not recovered from the short indexed excerpt pages—verify **`pdf_path`**.
- **Temperature:** **300 K** and **900 K** oxidation; **600–1500 K** for post-growth diffusion analysis ( **`pdf_path`**).
- **Pressure / stress:** **N/A — hydrostatic pressure** / stress control not emphasized in the excerpted protocol summary.
- **Electric field:** **10 MV/cm** along the surface normal at **300 K** (Sec. 4.2), implemented via an additional energy term **\(E_i=\mu q_i r_i\)** and forces **\(-\nabla E_i\)** coupled into **charge equilibration** (Eqs. (6)–(9), **`pdf_path`**).
- **Replica / enhanced sampling:** **N/A —** not indicated in the indexed excerpt.

**Electrostatics / cutoffs:** **ReaxFF** nonbonded cutoff **10 Å** is stated explicitly (Sec. 3.2, **`pdf_path`**).

### 2 — Force-field training

**N/A —** this paper **applies** an **Fe–O** **ReaxFF** parameterization and benchmarks **reference oxide** cells (**wüstite**, **magnetite**, **hematite**) with short **NVT** relaxations (**10 ps**, **1 fs**) at **300** and **900 K** for structural/charge comparisons (**Table 1**, Sec. 3.1, **`pdf_path`**) rather than reporting a new general refit here.

### 3 — Static QM / DFT-only

**N/A —** not the paper’s primary methodology beyond citations/context in the full article.

## Findings

- **Kinetic stages:** **fast** early oxidation (**O** ingress through **interstitial** channels) transitions to **slower** growth / **saturation** after **~300** consumed **O** atoms (transition **~300 ps** at **300 K**, **~100 ps** at **900 K** or with field—Sec. 4–5).
- **Facet ordering (1 ns, thermal oxidation):** more oxide on **(110)/(111)** than **(100)** under the reported conditions; quantitative **%** differences tabulated in Sec. 4.1.
- **Structure/charge:** early films are **non-stoichiometric** **Fe\(_{1-x}\)O**-like by **PDF**/**charge** analysis; **Mott–Cabrera**-style field language used to interpret **field-assisted** early anion motion (Sec. 4.2–5).
- **Diffusion barriers (no field):** **\(E_a \approx 0.32\)**, **0.26**, and **0.28 eV** on **(100)/(110)/(111)** from **600–1500 K** fits (**Fig. 11**).
- **Diffusion barriers (10 MV/cm):** **\(E_a \approx 0.33\)**, **0.24**, and **0.23 eV** on **(100)/(110)/(111)**—**slightly lower** than the **no-field** fits (Sec. 4.2 / Fig. 11 caption).
- **Field vs no-field at 1 ns:** field **accelerates** early uptake but **Fe(100)/(110)** can show **slightly less** total oxide at **1 ns** than **no-field** runs due to **later-stage** **cation** reordering/charge coupling (Sec. 4.2).

## Limitations

- Classical reactive FF uncertainty for **defect-rich oxides** and long-time **phase evolution**; field representation is model-dependent.

## Relevance to group

Strong example of **ReaxFF for metal oxidation** and **electrochemically biased** oxide growth—useful alongside other Fe/Ni aqueous oxidation entries.

## Citations and evidence anchors

- Abstract and Sec. 1–2 opening: kinetics ordering, mechanism narrative, diffusion activation energies, field effects (Phys. Chem. Chem. Phys., 2013, 15, 1821–1830; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
