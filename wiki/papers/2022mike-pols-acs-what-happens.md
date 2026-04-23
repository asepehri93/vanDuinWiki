---
id: paper:2022mike-pols-acs-what-happens
type: paper
title: "What Happens at Surfaces and Grain Boundaries of Halide Perovskites: Insights from Reactive Molecular Dynamics Simulations of CsPbI3"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:mechanics-tribology
  - material:widegap-semiconductor
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.2c09239"
year: 2022
authors:
  - "Mike Pols"
  - "Tobias Hilpert"
  - "Ivo A. W. Filot"
  - "Adri C. T. van Duin"
  - "Sofía Calero"
  - "Shuxia Tao"
venue: "ACS Appl. Mater. Interfaces 14, 40841–40850 (2022)"
pdf_sha256: "4e0e54fed3c25412da77fa2c0185d06ca01bc4874dafa1d54c8d2bfd154fa7f8"
pdf_path: "papers/Pols_ACS_AMI_CsPbI3_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022mike-pols-acs-what-happens -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** study of **CsPbI\(_3\)** focusing on how **surfaces, surface defects, and grain boundaries** participate in **degradation chemistry** and relative **stability**. The study relate computed **surface stability trends** to experimental prevalence of facets where comparable data exist, and mechanistically track evolution of **PbI\(_x\)**-like local coordination environments via **octahedral connectivity** changes (**corner → edge → face sharing**). **Pb dangling bonds** and **iodine sterics** are highlighted as drivers of degradation reactions; defect engineering can **stabilize** some boundaries by increasing steric hindrance even though clustered defects often accelerate failure.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with the authors’ **CsPbI\(_3\)** **ReaxFF** (prior **ref** **33** in the article) using **dynamical** **bond** **order** for **bond** **making/breaking**.
- **System size & composition:** **Orthorhombic** **CsPbI\(_3\)** **slab** **models** for **(110)**, **(020)**, and **(202)** **faces** with **stoichiometric**, **Pb-poor**, and **Pb-rich** **terminations**; **(110)** **slabs** with **4–10** **octahedral** **layer** **thicknesses** for **phase** **core–shell** **analysis**; **cubic**-phase **Σ** **grain** **boundaries** **3Σ(112)(0.4,0)**, **5Σ(210)(0.4,0)**, **3Σ(111)(0,0)** (see **SI** for **lattice** **vectors** and **build** **recipes**).
- **Boundaries / periodicity:** 3D **PBC** **slabs**; **GB** **cells** as **bicrystals** in the **cubic** **description** in **SI**.
- **Ensemble / barostat / pressure / field / enhanced sampling:** **NVT**-style **constant-**T **thermal** **ramping** and **holds** for the **degradation** **studies**; **N/A** — no **NPT** **stress**-control **focus**; **N/A** — no **external** **electric** **field**; **N/A** — no **metadynamics** (standard **ReaxFF** **MD**).
- **Timestep: N/A** in the **first** **main-text** **pages** **parsed** here; **use** **SI** **section** **1** for **integration** **settings** when **reproducing** (typical **ReaxFF** **0.25** **fs** is **not** **asserted** in the **excerpted** **text**).
- **Temperature / duration:** **Surface** **onset** **scans** from **300** **K** to **700** **K** in **50** **K** **steps**; some **(110)** **surfaces** **run** up to **5** **ns** at **700** **K** in the **narrative**; **degradation** **dynamics** at **600** **K** **illustrated** in **Figures 3**–**4**; **GB** **snapshots** at **600** **K** after **200** **ps** (**Figure** **6**) and **twin** **3Σ(111)** **trajectories** for **2** **ns** without **degradation**; **thermostat** **details** in **SI**.

### 2 — Force-field training (context)

- **N/A** as a **new** **fit** in this **article** — the **paper** **uses** the **parametrization** **from** **ref** **33**; **validation** **tables** in **this** **SI** /**main** **text** **compare** **ReaxFF** to **DFT** **where** **cited** (e.g. **valence** **angles** in **§2.2**).

### 3 — Static QM and experiments

- **DFT:** **Single-point** **or** **cluster** **DFT** **angles** **(148°/180°)** used to **label** **orthorhombic** **vs** **cubic** **character** **(Figure** **2** **caption** **text)**; **not** a **PES** **study** of **reaction** **barriers** here.
- **Experiments (literature):** **XRD** **facet** **prevalence** and **TEM** **degradation** at **GBs** from **cited** **work** for **qualitative** **agreement** with the **simulated** **stability** **trend** — **no** new **lab** **data** in this **MD** **paper**.
## Findings

**Surfaces:** A **stability** **ranking** **(110) > (020) > (202)** for **orthorhombic** **slabs** under **300**–**700** **K** **thermal** **loading** **matches** the **relative** **XRD** **occurrence** **trend** the **authors** **quote**. **Degradation** proceeds by **rearranging** **PbI\(_x\)** **octahedra** **corner** **→** **edge** **→** **face** **sharing**; **Frenkel**-like **I** **defects** **precede** **PbxI\(_y\)** **clustering** and **RDF** **changes** (**e.g.** **Pb**–**Pb** **peaks** at **~4.2** **Å** on **Pb-rich** **(110)** at **600** **K**). **Pb** **dangling** **bonds** and **low** **I** **steric** **hindrance** are **argued** to **promote** **failure**; **Pb-poor** **(110)** can be **very** **stable** (**up** to **700** **K** in the **5** **ns** **case** **described** for that **termination**).

**Grain boundaries:** Some **GBs** **degrade** **(amorphous** **PbxI\(_y\)** **patches** after **hundreds** of **ps**); the **3Σ(111)** **twin** **remains** **intact** over **2** **ns** at **600** **K** because **Cs** **in** **cavities** **sterically** **blocks** **octahedral** **motion** — the **mechanistic** **theme** is **defect/GB** **geometry** **gating** **I** **mobility** and **Pb** **clustering**. **Comparisons** to **laboratory** work are **indirect** **—** the **(110)>(020)>(202)** **trend** **is** said to **agree** with **which** **facets** are **prevalent** in **XRD** **(Methods**+**body**+**citations**+**[37]–[40]**, **in** the **VOR** **PDF**)**. **Temperature** is **a** **major** **sensitivity** **(300**–**700** **K** **scans,** **600** **K** **GBs**+**2** **ns** **/ **5** **ns** **(110)** **holds**)**. **Limitations** **(authors**+**ReaxFF**+**KB):** **Classical** **RMD** **(no** **carriers,** **no** **humidity**+**optics** **in** the **base** **model**)**; **extract**+**VOR**+**[[2022pols-venue-paper]]** **SI** **for** **lattice** **replicas**+**RDFs**+**tolerances.**
## Limitations

Classical reactive model for complex electronic-structure-sensitive photophysical systems; long-time annealing and photogenerated carriers are outside the classical ReaxFF scope unless augmented by higher-level calibration. **Device** **humidity**, **halide** **migration**, and **organic** **cation** **loss** are **multiphysics** concerns that typically require **complementary** **continuum** or **electronic-structure** studies beyond the **inorganic** **surface** focus summarized here. **Grain** **boundary** **structures** in the simulations are **idealized**; **experimental** **films** contain **tilt** **boundaries** and **impurity** **segregation** that can dominate **long-term** **degradation**.

## Relevance to group

Connects the group’s **ReaxFF** expertise to **halide perovskite durability** at **interfaces and microstructure features** that dominate practical thin-film devices.

## Citations and evidence anchors

https://doi.org/10.1021/acsami.2c09239 — Abstract (~p. 1) states mechanistic claims about octahedral sharing and steric control.

## Related topics

- [[reaxff-family]]
