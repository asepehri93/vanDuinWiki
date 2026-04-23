---
id: paper:2019zhang-carbon-159-2-converting-pbo
type: paper
title: "Converting PBO fibers into carbon fibers by ultrafast carbonization"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - material:polymer-organic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2019.12.067"
year: 2019
authors:
  - "Zhang, Liwen"
  - "Kowalik, Małgorzata"
  - "Gao, Zan"
  - "Ashraf, Chowdhury M."
  - "Rajabpour, Siavash"
  - "Bumgardner, Clifton"
  - "Schwab, Yosyp"
  - "Damirchi, Behzad"
  - "Zhu, Jiadeng"
  - "Akbarian, Dooman"
  - "Klett, James W."
  - "van Duin, Adri C. T."
  - "Li, Xiaodong"
venue: "Carbon"
pdf_sha256: "f21143b13cc611d2002a495e9796767f099827e7f4ff18cb6e36e63f47a56be4"
pdf_path: "papers/Zhang_Liwen_Carbon_PBO_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019zhang-carbon-159-2-converting-pbo -->

!!! abstract "Scope"

Ultrafast-heating carbonization of poly(p-phenylene-2,6-benzobisoxazole) (PBO) fibers to carbon fibers, paired with ReaxFF reactive molecular dynamics to interpret heating-rate effects on gas evolution and carbon-ring organization.

## Summary

The study demonstrates direct carbonization of PBO precursor fibers into carbon fibers using rapid heating and cooling, targeting cost reduction relative to conventional polyacrylonitrile routes that require separate stabilization. Experimental campaigns vary carbonization temperature, heating rate, cooling rate, and dwell time, reporting mechanical property trends including high tensile strength and Young’s modulus at a relatively low peak temperature when ultrafast thermal profiles are used. Reactive molecular dynamics with the ReaxFF formalism examines how heating rate alters early-stage pyrolysis chemistry, emphasizing relationships between oxygen-bearing gas release and the development of aligned six-membered carbon rings as precursors to graphitic order.

## Methods

Experiments carbonized PBO fibers under controlled thermal programs; gas evolution during conversion was analyzed to connect volatile release to microstructure and mechanical performance. Complementary **ReaxFF** **reactive** **molecular** **dynamics** in **LAMMPS** study **PBO**-segment **oligomer**/**fiber**-style **supercells** (atom **counts** and **periodic** **PBC** **cell** in *Carbon* **Method**) under **ramped** **temperature** **programs** for **pyrolysis**/**carbonization** with **explicit** **variation** of **heating** **rate** to probe **differential** **gas** **release** (for example **CO**, **H₂O**, **H₂**, with lesser **CO₂** and **N₂**) and **clustering** of **all-carbon** **six-membered** **rings**, building on the group’s **prior** **PBO** **ReaxFF** **line** (cited in the *Carbon* text). The manuscript links **simulation** **trends** to **ultrafast** **experimental** **heating** that **suppresses** **O-containing** **gas** **release** relative to **slower** **ramps** (as stated in the **abstract** **thread**).

**MD protocol (ReaxFF).** **Engine** **is** **LAMMPS** (as in the **2019** **PBO** **ReaxFF** **reference** in the *Carbon* **text**); **simulation** **cell** is **3D** **PBC** with **PBO** **strands** at **roughly** **0.1–0.3** **g/cm³** **initial** **density** (see **main** text); **timestep**/**thermostat** and **ramp** **durations** (**ps**–**ns**) are **N/A** on this one-page **summary**—**Section** **2** and **SI**. **Barostat / NPT production:** **N/A** unless the **carbonization** **MD** uses **constant** **pressure**; default assumption is **constant-volume** **heating** of the **polymer** **cell** (confirm in PDF). **Electric field:** **N/A**. **Umbrella / metadynamics / replica:** **N/A**—the **ReaxFF** work is **direct** **ramped** **MD** on **PBO** **models**, not a **rare-event** **enhanced** **sampling** **study** in the sense of **metadynamics**.

## Findings

Ultrafast heating and cooling produced PBO-derived carbon fibers with reported breakthrough tensile strength and Young’s modulus at a peak carbonization temperature near 1000 °C, highlighting heating rate—and cooling rate—as decisive processing levers alongside temperature and dwell time. Reactive simulations indicate that faster heating can suppress oxygen-containing gas release during early carbonization, promoting alignment of all-carbon rings and more favorable microstructural development consistent with improved mechanical response. The combined results frame heating-rate control as a practical knob for PBO-derived carbon fiber quality beyond traditional emphasis on peak temperature alone.

The paper thereby links **process window** (ramp shape) to **atomistic** fragmentation pathways, which is the sense in which ReaxFF adds interpretive value beyond **post-mortem** microstructure alone.

## Limitations

Atomistic models capture finite segments and time windows of pyrolysis; quantitative agreement with continuum fiber experiments requires careful interpretation of temperature definitions, sample sizes, and ReaxFF limitations for condensed-phase pyrolysis chemistry.

## Relevance to group

Direct van Duin-group ReaxFF application to polymer carbonization and carbon-fiber manufacturing, aligned with other precursor pyrolysis studies in the knowledge base.

## Citations and evidence anchors

- https://doi.org/10.1016/j.carbon.2019.12.067

## Related topics

- [[reaxff-family]]
