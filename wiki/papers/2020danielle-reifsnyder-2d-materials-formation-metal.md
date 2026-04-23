---
id: paper:2020danielle-reifsnyder-2d-materials-formation-metal
type: paper
title: "Formation of metal vacancy arrays in coalesced WS2 monolayer films"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1088/2053-1583/abc905"
year: 2020
authors:
  - "Danielle Reifsnyder Hickey"
  - "Dundar E. Yilmaz"
  - "Mikhail Chubarov"
  - "Saiphaneendra Bachu"
  - "Tanushree H. Choudhury"
  - "Leixin Miao"
  - "Chenhao Qian"
  - "Joan M. Redwing"
  - "Adri C. T. van Duin"
  - "Nasim Alem"
venue: "2D Mater."
pdf_sha256: "7317146d6c7a14a2b718245482b40f7682069f245e7616212293dd312c0e6319"
pdf_path: "papers/Reifsnyder_Hickey_2021_2D_Mater._8_011003_WS2_Al2O3.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020danielle-reifsnyder-2d-materials-formation-metal -->

ADF-STEM shows **linear arrays of W vacancies** in coalesced **CVD** **monolayer** **WS\(_2\)**; the authors connect them to **gas-phase** precursor **access** and **substrate** **catalysis** using **ReaxFF** **MD** of **WS\(_2\)** **edges** on **(0001)** **α-alumina**.

## Summary

Monolayer MOCVD WS\(_2\) often grows as islands that later coalesce. The letter links ADF-STEM line defects to **ReaxFF** MD in which a gas-phase W–S–SH precursor (modeled with **WS\(_2\)(SH)\(_2\)**) approaches **two parallel WS\(_2\)** **growth** **edges** on **(0001)** **α**-**Al\(_2\)O\(_3\)**. The key parameter is the **lateral** **separation** between those edges. For a **1.6 nm** channel, the main-text reaction path (Fig. 2) lets the precursor access the **sapphire** surface, strip **–SH** groups, and exothermically add a **WS\(_2\)** unit; the illustrated trace lists barriers of about **~25** and **~75** kcal mol\(^{-1}\) for the two **–SH** removal steps, and a **net** release of about **~125** kcal mol\(^{-1}\) **overall** (Fig. 2(b), main text). For a **0.2 nm** gap (Fig. 3), access to the catalytic substrate is **blocked** and a barrier **>** 100 kcal mol\(^{-1}\) in step (iii) **disfavors** the decomposition pathway, consistent with W-deficient lines in STEM along tight coalescence junctions. The W/S/H ReaxFF is merged with **Hong**-style Al/O (and related) parameters so the substrate participates in the chemistry, as written in the article.

## Methods

**1 — MD application (ReaxFF growth edges).** **Engine:** ReaxFF molecular dynamics (main text; full thermostat/timestep/integrator **details** in **Supplementary** **Information** (not retyped here). **System (atoms, supercell):** **WS\(_2\)** **armchair** and **zigzag** **edge** **pairs** (both **in** the **text/SI** **figures**) on **c**-axis **(0001) α**-**Al\(_2\)O\(_3\)**; **W/S/H** **ReaxFF** (trained **in** the **W/S/H** line **cited** **(Ostadhossein,** **Yilmaz**-**line** **MoS\(_2\)**-style, **2D** **Mater.)** is **merged** with **ReaxFF** **Al/O**/**C**/**H** (Hong) **so** the **sapphire** **+** **WS\(_2\)** **reactive** **interface** is **treated** **(main** **text** **paragraph).** **Bound** **/** **PBC:** **3D** **PBC** **(standard** **slab**-**in**-**box** for **imaged** **supercells**; **lateral** **dimensions** **+** **gap** **geometry** in **Figs. 2**–**3**). **Reaction** **promotion:** **Targeted** **bond** **restraints** (four in the **1.6** **nm** **illustration**: **S**-**W** (precursor)–**W** (edge) **+** **S(–SH)**-**to**-**Al** on **(0001)**; **rationale** in the **narrative**) **accelerate** **bond**-**formation**; **restraint** **energy** **is** **excluded** from **“barrier”** **analysis** (as **stated**). **Wide**-**channel** run **(≈1.6** **nm)**: path **(i)–(iv)** **(precursor** **to** **substrate** **(ii–iii)**, then **row** **growth (iv)**, **Figs. 2** **a**–**b)**, with **largest** **cited** **hurdle** on **second** **–SH** **removal** **(≈75** **kcal** **mol\(^{-1}\)**, **figure**). **Narrow**-**channel (0.2** **nm)**: high **(>** **100** **kcal** **mol\(^{-1}\))** **barrier** in **(iii)**, **incomplete** **WS\(_2\)** **row** **incorporation** **(Figs. 3a–b)**, paralleling **W**-**deficiency** **arrays** in **STEM**. **Temperature (thermostat / target K in MD and CVD):** N/A in this short note; see the **2D** **Mater.** **article** and **SI** for **CVD** (K) and any **NVT** setpoints. **Barostat:** **N/A** in the **restraint**-**driven** **kinetic** **sampling** as **excerpted;** **pressure: N/A**; **isotropic** **hydrostatic** **(NPT)** is **not** a **stated** **end**-**to**-**end** **protocol** **in** the **excerpted** **main** **text. **Electric** **field: N/A**. **Replica/umbrella/metadynamics: N/A**; **restraints** (not metadynamics) are used. **Cumulative** **ps** and **0.25** **fs**-type **control** (if any): **N/A** — see **Supplementary** **Information**; **MOCVD** **(W(CO)\(_6\)**, **H\(_2\)S**, **H\(_2\)**) is **laboratory** **context** **(Methods**-level **chemistry)**, not **a** full **reactor** **ReaxFF** run.

**2 — DFT/MD in this work.** The **kinetic** **arguments** use **ReaxFF** **reaction** **energies** **(main** **text)**, not **VASP**-style **DFT** **PES** in this **letter;** **N/A** — **standalone** **ab** **initio** **(DFT) production** in **the** **2D** **Mater. methods** is **not** a **separate** **“block”** **(check** **SI** **if** they **cite** **comparative** **DFT)`.

**3 — Force-field** **reparameterization: N/A** (uses **published** **W/S/** **and** **merged** **oxide** **sets**).

**Microscopy (experiment).** **ADF-STEM** **(and** **TEM/STEM**-**class** **imaging) on** monolayer **CVD** **WS\(_2\)**; **W**-**deficiency** **line** and **cluster** **morphologies** **(Figs. 1,** **4)**, with **CVD** **(MOCVD) growth** on **(0001)** **sapphire** (article/SI for growth parameters).

## Findings

- **Imaging:** long **W-vacancy** line defects and a minority of **scattered** vacancies; **cluster**-rich arrays also occur (Fig. 4), consistent with **kinetic** and **morphological** coalescence variability, not a single **equilibrium** point-defect picture.
- **ReaxFF, wide (≈1.6 nm) channel:** the **(i)–(iv)** path in **Fig. 2** is **exothermic** by **~125** kcal **mol**\(^{-1}\) in the main-text trace, with **(iii) ≈ 75** kcal **mol**\(^{-1}\) as the largest barrier (second –SH removal) and **(i) ≈ 25** kcal **mol**\(^{-1}\) for the first –SH removal (Discussion).
- **Narrow** **(0.2** **nm)** **gap:** a **(>** 100) kcal **mol**\(^{-1}\) barrier in the third step and **incomplete** precursor **decomposition** to a **WS\(_2\)** **row**-**adding** unit is argued to kinetically yield **W**-**deficient** line formation during **late** coalescence (Fig. 3, tied to the STEM “continuous array” case).
- **Comparisons:** the paper contrasts **catalysis** of **–SH** **loss** on **sapphire** (accessible in **wide** gaps) with **H**-**abstraction** off a **facing** **edge** in **tight** gaps, explaining the **sensitivity** of **defect** type to **edge**–**edge** **separation** and **substrate** **access** (armchair and zigzag edges treated, with zigzag in SI).

**Corpus honesty:** package-level ReaxFF control (timestep, thermostat) is not transcribed to this page; use the local PDF and SI for barrier curve digitization and figure numbering.

## Limitations

**ReaxFF** accuracy for **TMD–oxide** interfaces is finite; **gas-phase** precursor chemistry and **reactor** flow are simplified in MD.

## Relevance to group

**van Duin-group** collaboration on **2D TMD defects** with **ReaxFF** growth modeling tied to **electron microscopy**.

## Citations and evidence anchors

- DOI: [10.1088/2053-1583/abc905](https://doi.org/10.1088/2053-1583/abc905)

## Related topics

- [[reaxff-family]]
