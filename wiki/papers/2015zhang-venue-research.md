---
id: paper:2015zhang-venue-research
type: paper
title: "ReaxFF reactive molecular dynamics simulation of functionalized poly(phenylene oxide) anion exchange membranes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - domain:reactive-md
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b07271"
year: 2015
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "0d7b3c7d04989cf9d1e216989fb0e63e5e05d6fb3cb9f1d3ce06ed8df074aacb"
pdf_path: "papers/Zhang_Anion_Exchange_proof_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015zhang-venue-research -->


## Summary

Reactive molecular dynamics with ReaxFF is used to compare three functionalized poly(phenylene oxide) (PPO) anion exchange membranes—PPO–trimethylamine (PPO–TMA), PPO–dimethylbutylamine (PPO–DMBA), and PPO–dimethyloctylamine (PPO–DMOA)—at two hydration levels (λ = 8.3 and 20.8, where λ is the ratio of water molecules to quaternary ammonium groups). The work connects membrane microstructure, hydroxide transport, and alkaline degradation behavior relevant to anion exchange membrane fuel cells. **Reactive** treatment is emphasized because **OH⁻** transport in alkaline membranes often involves **proton hopping** networks that fixed-charge **classical** models may misrepresent when bonds rearrange. The comparison across headgroups and hydration levels is framed explicitly for AEMFC durability trade-offs, not as a full device-scale transport model.

## Methods

### MD application (atomistic dynamics)

Reactive MD uses **ReaxFF** so O–H bond formation and cleavage needed for **Grotthuss-type** OH⁻ transport can occur alongside vehicular motion; the authors motivate this choice against fixed-charge classical models that omit hopping (see Introduction in `pdf_path`).

- **Engine / code:** **ADF 2012** is used to run the reported ReaxFF MD (Simulation Details in the article).
- **System size and composition:** Each hydrated membrane contains **three** PPO chains (degree of polymerization **8** per chain, ends capped with H), **24** quaternary ammonium centers with **24** OH⁻, and either **200** or **500** H₂O to reach **λ = 8.3** or **20.8** (water molecules per cation). Total atom counts are **1419 / 2319** (PPO–TMA), **1635 / 2535** (PPO–DMBA), and **1923 / 2823** (PPO–DMOA) for the low/high hydration pairs, respectively (Table 1 in the article).
- **Boundaries / periodicity:** **Three-dimensional periodic** cell for the condensed-phase membrane models (standard for bulk hydrated polymer MD).
- **Ensemble and stages:** Initial amorphous packing via **Monte Carlo** at low density → minimization → compression toward **~1.00 g cm⁻³** at **300 K**; **four** annealing cycles (expand volume **50%** over **25 ps** while heating **300 → 600 K**; **100 ps NVT** at **600 K** on the expanded cell; compress back to **1.00 g cm⁻³** while cooling to **300 K**), with **24 H₂O** temporarily replacing OH⁻ during anneal to limit backbone damage; restore **24 OH⁻** and minimize; **100 ps NPT** at **300 K** for density equilibration; **350 ps NVT** production with structural/transport statistics taken from the **last 120 ps**.
- **Timestep:** **0.25 fs**.
- **Duration:** Production **NVT** segment **350 ps** (analysis window **120 ps** as above); anneal + **NPT** equilibration stages as listed.
- **Thermostat:** **Berendsen** temperature control with coupling time **100 fs** (Simulation Details).
- **Barostat:** After restoring **OH⁻** and minimization, a **100 ps NPT** segment equilibrates the cell to the **final density** (Table 1). The manuscript labels this as **NPT** density equilibration; **if a specific barostat implementation is required for reproduction**, confirm the thermostat/barostat pairing in the formatted *J. Phys. Chem. C* text of **`pdf_path`** (the proof PDF text layer does not isolate a distinct barostat name from the **NPT** line alone).
- **Temperature:** **300 K** for the reported transport/degradation analysis; anneal peaks at **600 K** as part of equilibration.
- **Pressure:** **Isotropic NPT** at **300 K** for **100 ps** is used to relax the cell to the reported **equilibrated densities** (Table 1); the article’s Simulation Details emphasize **Berendsen** temperature coupling (**100 fs**) for the subsequent **350 ps NVT** production segment.
- **Electric field:** **N/A — not used.**
- **Replica / enhanced sampling:** **N/A — not used.**
- **Electrostatics / charge dynamics:** ReaxFF **EEM-style** variable charges updated through the force-field formulation as implemented in ADF for these runs (see article ReaxFF background).

### Force-field training

**N/A — not a ReaxFF parameterization paper.** The study **applies** an established ReaxFF description suitable for OH⁻/water-containing polymer chemistry; QM training details for building that parameter set belong to the original ReaxFF references cited in the article, not to this application manuscript.

### Static QM / DFT

**N/A — no DFT production pipeline** for the membrane results in the sense of AGENTS block 3; the paper cites higher-level MD/QM-hybrid literature for proton transport context in the Introduction.

## Findings

- **Outcomes and mechanisms:** Higher **λ** swells the membrane, promotes **water-channel** formation, and increases **OH⁻ diffusion** relative to the lower hydration case for each chemistry.
- **Comparisons across headgroups:** At the **high** hydration level studied, **PPO–TMA** gives the **largest OH⁻ diffusion constant** among the three membranes.
- **Alkaline stability lever:** At the **same** water content, replacing a methyl on the quaternary center with a **longer alkyl** chain increases **hydrophobic shielding** of nitrogen from OH⁻ approach, **lowering degradation rate** and improving **alkaline stability** (emphasis on **PPO–DMOA** in the abstract).
- **Design takeaway (authored framing):** A high-performance AEM should **balance conductivity and chemical stability**, because headgroup and hydration choices move transport and degradation in different directions.

## Limitations

The ingested file is a **proof / “XXXX” volume-page placeholder** layout in the corpus filename; reconcile pagination, Supporting Information, and any **post-technical-edit** changes against the **version-of-record** *J. Phys. Chem. C* article when replacing the blob. Numerical diffusion coefficients and additional sensitivity analyses are tabulated in the main text and should be copied from the primary PDF for high-precision reuse, not from this summary alone.

## Relevance to group

Penn State / van Duin group work on reactive MD of polymer electrolyte membranes for electrochemical energy conversion.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.5b07271](https://doi.org/10.1021/acs.jpcc.5b07271)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
