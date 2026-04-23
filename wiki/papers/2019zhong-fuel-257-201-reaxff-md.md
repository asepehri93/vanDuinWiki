---
id: paper:2019zhong-fuel-257-201-reaxff-md
type: paper
title: "ReaxFF MD simulations of petroleum coke CO2 gasification examining the S/N removal mechanisms and CO/CO2 reactivity"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:nvt-simulation
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116051"
year: 2019
authors:
  - "Zhong, Qifan"
  - "Zhang, Yu"
  - "Shabnam, Sharmin"
  - "Mao, Qiuyun"
  - "Xiao, Jin"
  - "van Duin, Adri C. T."
  - "Mathews, Jonathan P."
venue: "Fuel"
pdf_sha256: "734e41af2bb56c677bf97a290b629be761ff1806fd466992cf492a2dcefc9c4a"
pdf_path: "papers/Zhong_Fuel_2019_S_N_removal.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019zhong-fuel-257-201-reaxff-md -->


!!! abstract "Scope"

ReaxFF NVT molecular dynamics of CO₂ gasification of a high-sulfur petroleum coke model at 3000 K, tracking sulfur and nitrogen speciation alongside CO/CO₂ reactivity including Boudouard-type chemistry.

## Summary

Petroleum coke used as fuel or gasification feedstock retains sulfur and nitrogen in thermally stable moieties that participate in high-temperature conversion. The article examines removal and transformation pathways for those heteroatoms during CO₂ gasification using reactive force field molecular dynamics, explicitly addressing overlap between slow pyrolysis and gasification kinetics under the chosen hot, short trajectories.

## Methods

**Reactive MD (ReaxFF).** Simulations use the reactive force field formalism cited in the article to follow bond rearrangement in a high-sulfur petroleum coke atomistic model at combustion/gasification-relevant temperature.

**System.** The petcoke structure is the Qingdao high-sulfur model with composition C₁₆₄₈H₇₇₂O₅₉N₂₄S₄₇ (2550 atoms) from prior work, built to capture curvature, stacking, length distribution, and O/N/S functional-group content; the same model was used in related pyrolysis and combustion ReaxFF studies at 2000–4000 K for comparison.

**Integration and conditions.** Runs are **NVT** at **3000 K** for **250 ps**, bracketing conditions where the abstract notes overlap between slower pyrolysis and slower gasification so both contribute to overall behavior. The paper contrasts regimes described as **pyrolytic**, **reducing**, and **oxidizing** with respect to **CO₂** exposure (contribution of petcoke self-pyrolysis, CO₂ oxidation, and CO reduction is evaluated in the Methods narrative).

**Analysis.** Trajectories track **S** and **N** redistribution into gas-phase and condensed fragments and follow **C** oxidation sequences involving **CO** and **CO₂**, including stepwise interpretation of **Boudouard-type** chemistry. **PBC** and 3D periodic supercells are used as in the cited ReaxFF pet-coke work; **N/A —** integration timestep, thermostat name, and QEq/electrostatic update interval not copied from the local PDF to this page (see *Fuel* article and SI). **N/A —** barostat / pressure control: constant-volume NVT; no NPT production stage reported for these runs. **N/A —** static or oscillating electric field. **N/A —** replica exchange, umbrella, or metadynamics; production is standard NVT time evolution.

**Force-field training (block 2).** **N/A** — the paper applies an existing Reaxff CHONS parameterization for high-temperature coke/CO₂ chemistry rather than reporting a new fit in this work.

**Static QM (block 3).** **N/A** — central claims are from ReaxFF MD, not a standalone DFT study.

## Findings

**Sulfur.** The abstract summarizes transformation sequences such as thiophenic S toward **COS**, C₁₋₂S-type fragments toward **CₙOₙS**-class species, further toward **H₂S** and **SO₂** under the modeled oxygen inventory.

**Nitrogen.** Pyrrolic and pyridinic N are reported to evolve through **CON**, **CN**, and **NO**₁₋₂-containing intermediates toward **C**₁₋₂**O**₁₋₂**N**, **COₙN**, and **HNO**₁₋₂-type species and ultimately toward products such as **HCN** and nitrogen oxides depending on local oxygen (0 < n < 5 in the abstract’s shorthand).

**CO/CO₂ reactivity.** ReaxFF captures **Boudouard** chemistry as a two-step picture: one **O** from **CO₂** bonds to a coke **C**, then the **O–C** bond in **CO₂** breaks after **CO** release; the coke **C** that bound **O** is subsequently removed as a second **CO**, matching the abstract’s disassembly of the overall C + CO₂ ⇌ 2CO stoichiometry into atomistic events.

**Interpretation.** The authors argue that such trajectories help relate **feedstock structural diversity** (the “scale challenge”) to **coke consumption** chemistry beyond a single effective Boudouard rate. The KB should treat **S/N removal** and **CO/CO₂** chemistry as **coupled** observables from the same **NVT** runs, not as independent post-processing metrics.

## Limitations

Simulations use a single high-temperature window and short real time; quantitative rates and yields should not be extrapolated to industrial gasifiers without additional validation. The petcoke structural model is necessarily a **single** atomistic realization; compositional diversity in real feedstocks means pathway statistics should be read as **illustrative** rather than exhaustive.

## Relevance to group

Companion study to other Zhong et al. petcoke ReaxFF papers in the corpus, emphasizing CO₂ gasification chemistry rather than hydrogen or ammonia reductants.

## Citations and evidence anchors

- https://doi.org/10.1016/j.fuel.2019.116051

## Related topics

- [[reaxff-family]]
