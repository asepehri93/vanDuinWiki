---
id: paper:2019khalilov-carbon-153-2-catalyzed-growth-2
type: paper
title: "Catalyzed growth of encapsulated carbyne"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
candidate_tags: []
paper_keywords:
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:metallic-systems
source_refs: []
doi: "10.1016/j.carbon.2019.06.110"
year: 2019
authors:
  - "Umedjon Khalilov"
  - "Charlotte Vets"
  - "Erik C. Neyts"
venue: "Carbon"
pdf_sha256: "a94849e74fd7455a72c4261af10a41c2152c9832872f2c29d55b4adb1fe75f44"
pdf_path: "papers/ReaxFF_others/Umedjon_Ni_catalysis_CNT_growth_Carbon_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019khalilov-carbon-153-2-catalyzed-growth-2 -->

!!! note "Corpus PDF role"
    Second registered **PDF bytes** for the *Carbon* **2019** article on **Ni-catalyzed** **endohedral carbyne** inside a **double-walled nanotube** (same DOI). Narrative alignment: **[[2019khalilov-carbon-153-2-catalyzed-growth]]** (alternate path).

## Summary

Endohedral **carbyne**—a one-dimensional carbon chain—inside carbon nanotubes is a long-standing target in **nanocarbon** synthesis, but **atomistic** mechanisms of **catalytic** chain growth under **hydrocarbon** feedstock remain difficult to probe experimentally at the **insertion** step. This work combines **ReaxFF** reactive molecular dynamics (parameters from **Zou et al.**) with **DFT** (**VASP**, **GGA-RPBE**, **PAW** pseudopotentials) to study **nickel** clusters hosted inside a **(5,5)@(10,10)** **double-walled** tube. **C\(_2\)**, **C\(_2\)H**, and **C\(_2\)H\(_2\)** species are injected as **feedstock** at **500 K** versus **1700 K** effective **flux** conditions (controlled by insertion interval). The study emphasizes **sticking** and **adsorption energetics** as a function of **hydrogen content**, **Ni** facet geometry (**step-like** versus flatter **(111)**-like regions), and how **ReaxFF** and **DFT** agree on **trends** even when **absolute** binding strengths differ.

## Methods

Narrative matches the **version-of-record** curation on **[[2019khalilov-carbon-153-2-catalyzed-growth]]** (same **DOI** and **science**; alternate **PDF** **bytes** here).

### 1 — MD application (RMD, ReaxFF)

**ReaxFF** (parameters of **Zou** *et al.*) in a **(5,5)@(10,10)** **DWNT** with **PBC** along the **axis**; **Ni** in the **inner** tube (**d\(_\mathrm{in}\)≈0.70 nm**, **d\(_\mathrm{out}\)≈1.39 nm**). **NpT** preequilibration (**Berendsen**), then **NVT** with **Bussi**; **C\(_2\)/**C\(_2\)H/**C\(_2\)H\(_2\)** **insertion** every **25 ps** (**1700 K**) or **250 ps** (**500 K**). **Timestep (fs):** **N/A** in the **Methods** text of the **indexed** **PDF**—use **[[2019khalilov-carbon-153-2-catalyzed-growth]]** or **SI** for **reproducibility**. **Barostat in production / pressure in NVT:** **N/A** for **NVT** **stages** as **written**. **Electric field / enhanced sampling:** **N/A**.

### 2 — Force-field training

**N/A** — **published** **ReaxFF** **parameters** (**Zou** *et al.*), not a **new** **fit** in this **article**.

### 3 — Static QM (VASP, NEB)

**VASP** **RPBE**+**PAW**, **400 eV**, **Γ (1×1×1)**, **~20×20 Å** **in-plane** **supercells**; **PBE+TS** **negligible** in **author** **tests**; **NEB** for **dimer** **nucleation** with **~0.1–0.3 eV** **barriers** as **reported**.
## Findings

**Sticking** and **adsorption energies** **anti-correlate** with **H/C** ratio in the feedstock family: hydrogen-rich species behave differently from bare **C\(_2\)** in both **ReaxFF** and **DFT**, preserving qualitative ordering across methods. **Step-like** **Ni** facets promote **C–H** cleavage pathways compared with **flatter** facets, shaping whether **dimerization** or **dehydrogenation** dominates early chemistry. **DFT** consistently reports **stronger** absolute **binding** than **ReaxFF**, but **relative** trends (which site binds more strongly, which feedstock sticks more readily) remain aligned between models. **Ni-terminated** carbon chains allow **hydrogen** to modulate **electronic** response, linking **hydrocarbon identity** to whether **C–C** polymerization or **C–H** scission is favored on **curved** **Ni** surfaces inside the confining **nanotube** (see **version-of-record** text on **[[2019khalilov-carbon-153-2-catalyzed-growth]]** for **table** / **figure** locators).
## Limitations

**ReaxFF** and **DFT** **adsorption** energies can differ by roughly **two-fold** in magnitude for some configurations; the paper focuses on **mechanistic** **trends** and **barrier** order-of-magnitude estimates rather than quantitative agreement with experiment for **long** **carbyne** **stability** or **growth** rates.

## Reader notes (navigation)

- Alternate PDF / primary curation: **[[2019khalilov-carbon-153-2-catalyzed-growth]]**
- [[reaxff-family]]
