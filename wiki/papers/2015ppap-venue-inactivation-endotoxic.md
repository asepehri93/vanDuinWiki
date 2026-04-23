---
id: paper:2015ppap-venue-inactivation-endotoxic
type: paper
title: "Inactivation of the endotoxic biomolecule lipid A by oxygen plasma species: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1002/ppap.201400064"
year: 2015
authors:
  - "Maksudbek Yusupov"
  - "Erik C. Neyts"
  - "Christof C. Verlackt"
  - "Umedjon Khalilov"
  - "Adri C. T. van Duin"
  - "Annemie Bogaerts"
venue: "Plasma Processes and Polymers 2015, 12, 162–171"
pdf_sha256: "f0e09561531dd7a348592a5469855314c62f4062b0e79705004477cfecbdef59"
pdf_path: "papers/PPaP_2015_Yusupov-Lipid A.PDF"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015ppap-venue-inactivation-endotoxic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Yusupov *et al.* perform **ReaxFF reactive MD** to study impacts of **oxygen plasma-derived species** (**OH**, **HO\(_2\)**, **H\(_2\)O\(_2\)**) on **lipid A**, the endotoxic anchor of *E. coli* lipopolysaccharide. The abstract claims these species can **destroy lipid A** and thereby **reduce toxic activity**, with **distinct bond-breaking mechanisms** for **HO\(_2\)**/**H\(_2\)O\(_2\)** versus **OH** impacts, and states qualitative agreement with experimental observations cited in the introduction framing. The introduction surveys **cold atmospheric plasma (CAP)** sterilization motivations and summarizes prior experimental work on **LPS/lipid A** modifications by plasma-generated **radicals** and **VUV**.

## Methods

**Reactive molecular dynamics** with **ReaxFF** studies impacts of **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** on a **truncated *E. coli* lipid A** model in which oligosaccharide tails are replaced by **methyl** caps (*Plasma Process. Polym.* computational section). **System composition** follows their capped **headgroup + acyl chain** construct (explicit **atoms** for the reactive core with **H** atoms selectively **frozen** on the methyl caps as in Fig. 1). The **simulation box** is about **50 × 70 × 40 Å³**; **periodic boundaries are not used** on any face because a semi-infinite surface is not targeted—instead, selected **methyl-site hydrogens** are **spatially fixed** to preserve the experimental lipid A geometry. **Equilibration:** **500 ps** canonical (**NVT**) dynamics at **300 K** with a **Bussi** thermostat (**100 fs** coupling constant). **Integrator:** **0.25 fs** timestep for both thermalization and impact segments. **Production impacts:** each of **100 independent runs** per species places **ten** incident particles with **random** positions (**≥ ~10 Å** from the lipid and from each other) and **room-temperature** kinetic energies; trajectories continue **500 ps** under **NVT** (authors state this duration suffices to break at least one **critical** bond in the cases they highlight). **Barostat / NPT:** **N/A**. **Applied electric fields / metadynamics:** **N/A**. **MD engine:** **N/A —** the **PDF** text checked for this page does not name the dynamics **code** (only **ReaxFF** is specified).

## Findings

**Mechanisms / damage pathways.** The **abstract** reports that **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** can **oxidatively cleave** and **fragment** the modeled **lipid A**, lowering modeled **toxicity** proxies; **HO\(_2\)**/**H\(_2\)O\(_2\)** versus **OH** follow **distinct bond-breaking sequences** (e.g., **H-abstraction** events involving **ether oxygens** versus other **headgroup** attacks detailed in **Results**).

**Comparisons.** The authors state **good agreement** between these **ReaxFF** trajectories and **experimental** plasma-exposure observations they cite for **LPS**/**lipid A** chemistry—positioning the simulations as mechanistic cartoons rather than a clinical dose model.

**Sensitivity / statistics.** **Statistics:** **100 runs** per impinging species with **ten** particles each quantify how often **critical** **C–O**, **C–N**, or **C–C** bonds rupture within **500 ps** at **300 K** **NVT**; **temperature** is fixed to **room** conditions during impacts, so **thermal** activation differences between species enter mainly through initial **radical** identity rather than bath ramps.

**Limitations / outlook.** The study acknowledges but does not fully resolve **plasma** complexity (**many** **ROS**/**RNS** omitted); **future work** in their framing would extend species coverage and membrane embedding.

**Corpus honesty.** Bond inventories and representative **reaction** sequences should be checked against the **PDF** figures/tables for exact **atom** labels—this page summarizes the **peer-reviewed** text only.

## Limitations

Biological complexity (full **LPS** assemblies, membrane heterogeneity, realistic **plasma** composition) is reduced to a **truncated lipid A** model with **gas-phase-like** ROS impacts; translating bond-loss statistics to **endotoxicity** or clinical **CAP** outcomes still requires experiment and multiscale modeling beyond this **ReaxFF** study.

## Relevance to group

**Adri C. T. van Duin** co-authorship connects the work to **ReaxFF** extensions toward **plasma–biomolecule** interactions pursued with Antwerp **PLASMANT** collaborators.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1002/ppap.201400064](https://doi.org/10.1002/ppap.201400064)

## Related topics

- [[reaxff-family]]
