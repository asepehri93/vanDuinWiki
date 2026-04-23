---
id: paper:2019ilyin-et-al-2018-fir-nat-first-principles-based
type: paper
title: "First-principles–based reaction kinetics from reactive molecular dynamics simulations: Application to hydrogen peroxide decomposition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:fuel-combustion
  - method:reaxff
  - task:method-development
  - task:validation
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:combustion
  - keyword:method-development
  - keyword:validation-experiment
source_refs: []
doi: "10.1073/pnas.1701383115"
year: 2019
authors:
  - "Daniil V. Ilyin"
  - "William A. Goddard III"
  - "Julius J. Oppenheim"
  - "Tao Cheng"
venue: "Proceedings of the National Academy of Sciences"
pdf_sha256: "0acdd14985c572db0097fde57f022b276d344b5f3252ab8159b6a8826c4787b0"
pdf_path: "papers/ReaxFF_others/ilyin-et-al-2018-first-principles-based-reaction-kinetics-from-reactive-molecular-dynamics-simulations-application-to.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019ilyin-et-al-2018-fir-nat-first-principles-based -->

## Summary

The paper introduces **RMD2Kin** / **ReaxMD2Kin**: extract **dominant reactions** and **temperature-dependent rates** from **condensed-phase ReaxFF RMD**, fit **Eyring** parameters **(\(\Delta H^\ddagger\), \(\Delta S^\ddagger\))** from **ln(k/T) vs 1/T**, then **analytically** propagate **species** trajectories—demonstrated for **hydrogen peroxide** **liquid** decomposition (**1000–2000 K** windows in the main example) with **QM** spot checks on barriers. The opening perspective argues that combustion, CVD, fracking, and related technologies need kinetics tied to **actual intermediates**, but experiments rarely resolve full networks, so practitioners often rely on oversimplified schemes. **QM** is accurate yet too costly for \(\sim\)10 nm and \(\sim\)1 ns averaging, whereas **ReaxFF RMD** is positioned as the workhorse that can be **mined automatically** for mechanisms and rates without hand-built reaction lists.

## Methods

- **Reactive MD:** **ReaxFF** trained to **QM** (prior work) for **H/O** chemistry in **dense HOOH** systems; trajectories long enough to sample **bimolecular** encounters in **liquid** (not dilute gas kinetics).
- **Mechanism mining:** Identify **dominant species** (**HOOH**, **H\(_2\)O**, **O\(_2\)**, **HOO**, **OH**, …) and **seven** **key reactions**; count events per interval → **instantaneous rates** → **k(T)**.
- **Fitting:** **Eyring** analysis yields **\(\Delta H^\ddagger\)** and **\(\Delta S^\ddagger\)**; recomputed **k** feeds **ODE-style** concentration evolution compared against **raw RMD** (**Fig. 1**).
- **QM benchmarks:** Two-body **barrier** scans for select steps (values quoted for reactions **1–7**, including cases with **no** simple **TS** in gas-phase dimer calculations). The authors label the overall pipeline **RMD2Kin** generically and **ReaxMD2Kin** when the reactive model is **QM-fitted ReaxFF**.

**Condensed-phase ReaxFF RMD setup.** **Reactive molecular dynamics** on dense **hydrogen peroxide** systems uses **ReaxFF** trained to **QM** (prior publications) in **three-dimensional periodic** **supercells** sized for **~10 nm** sampling (exact **atom** counts and densities in `pdf_path`). **Ensemble:** **NVT** **thermal** sweeps across **1000–2000 K** as in the **PNAS** article; **timestep** in **fs** and **production**/**equilibration** spans in **ps**/**ns** appear in **Methods**. **Thermostat:** specified there for high-**temperature** **decomposition** kinetics. **Barostat / pressure:** **N/A** — no **NPT** **barostat** or **GPa** targets in the showcased liquid **H₂O₂** **MD**. **External electric field:** **N/A**. **Enhanced sampling:** **N/A** for the **RMD2Kin** extraction trajectories (direct **MD** mining).

## Findings

- The **seven-reaction** **mechanism** reproduces **RMD** species populations across **1000–2000 K** when propagated with **fitted** **Eyring** rates.
- **Negative** **activation entropy** is common; several reactions show **negative** **\(\Delta H^\ddagger\)** when **radical** **TS** lie below separated reactants—highlighting **condensed-phase** effects vs gas-phase intuition.
- **Reaction 7** forms a **short-lived HO–OH** complex that reshapes **OH** availability; **reaction 2** has **multiple** **HOO + HOOH** geometries (productive vs exchanging **H**).
- Supplemental **CFD-scale** discussion (**Landau–Darrieus**) uses **HOOH/OH** **interface** tests without observing sustained **LDI** plumes under sampled conditions. The **ReaxFF** capability list in the article enumerates prior applications from hydrocarbons and nitramines to electrochemical interfaces, framing **HOOH** as a tractable exemplar for the **kinetics-extraction** workflow. The closing discussion positions **ReaxMD2Kin** as a bridge from atomistic trajectories to continuum reactor or engine models once **Eyring** parameters are exported.

## Limitations

Automation for **million-atom**, **hundreds-of-reaction** systems remains future work (manual selection of **dominant** channels in the showcase).

## Relevance to group

Methodological **PNAS** perspective complementary to Penn State **ReaxFF** applications; cites **ReaxFF** ecosystem breadth.

## Citations and evidence anchors

- `papers/ReaxFF_others/ilyin-et-al-2018-first-principles-based-reaction-kinetics-from-reactive-molecular-dynamics-simulations-application-to.pdf`

## Related topics

- [[reaxff-family]]
