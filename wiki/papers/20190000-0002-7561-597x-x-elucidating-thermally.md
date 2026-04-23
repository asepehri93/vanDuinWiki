---
id: paper:20190000-0002-7561-597x-x-elucidating-thermally
type: paper
title: Elucidating Thermally Induced Structural and Chemical Transformations in Kaolinite
  Using Reactive Molecular Dynamics Simulations and X-ray Scattering Measurements
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:water-silica-geo
- domain:reactive-md
- method:reaxff
- task:experiment-integrated
- task:validation
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:thermal-decomposition
- keyword:validation-experiment
- keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: 10.1021/acs.chemmater.9b03929
year: 2019
authors:
- Murali Gopal Muraleedharan
- Hassnain Asgar
- Sohaib Mohammed
- Greeshma Gadikota
- Adri C. T. van Duin
venue: Chem. Mater. (proof PDF in corpus)
pdf_sha256: 11fec810c429b768407937efd70f02585c784921871c9bac44752f22d197986b
pdf_path: papers/Muraleedharan_ChemMat_2019_kaolinite_proof.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:20190000-0002-7561-597x-x-elucidating-thermally -->

## Summary

**ReaxFF MD** is coupled with **in situ / operando WAXS** and **X-ray PDF** on **kaolinite** heated from **298 K to 1673 K**. The study is designed so diffraction-derived pair distributions anchor the atomistic model before mechanistic claims: after matching **PDF** and **WAXS** features between **experiment and simulation**, the authors use **MD** to resolve **dehydroxylation**, **sintering**, and **mullite** formation pathways, including **barrier** estimates and a **heating-rate** sensitivity study. **Kaolinite** **calcination** is industrially relevant for **ceramics** and **geopolymer** precursors; linking **atomistic** **reaction** sequences to **operando** **scattering** reduces ambiguity when multiple **solid** **phases** overlap in **diffraction** patterns.

## Methods

- **Experiment:** **WAXS** and **PDF** during **thermal ramps** on **kaolinite** (Cornell collaboration); temperatures span **298–1673 K** (abstract).
- **Simulation:** **ReaxFF MD** on comparable thermal schedules; **structure factors / PDFs** computed from trajectories and compared to **X-ray** data (abstract), iterating structure until experimental oscillations are reproduced where possible.
- **Mechanistic analysis:** Identify **reaction intermediates** and **transition** configurations for **dehydroxylation** and **sintering**; extract **reaction barriers** from MD (abstract).
- **Heating-rate study:** Compare **fast** vs **10× slower** ramp: report **onset** shifts for **dehydroxylation** and **sintering** (abstract gives example temperatures).
- **Structure factor** computation from **trajectories** follows the experimental **Q** range where **WAXS** features are most diagnostic.

**MD application (proof §2.1.3 “Simulation Settings”).** **Engine / code:** **ReaxFF** **molecular dynamics** is run inside **ADF** (Amsterdam Density Functional) as stated in the **Methods**. **Ensemble:** **canonical (NVT)** for all equilibration and heating **stages** with a **weak Berendsen** **thermostat** (**temperature** damping **0.1 ps**). **Timestep / integrator:** **0.25 fs** with **velocity Verlet**. **Heating / duration:** the equilibrated **kaolinite** cell is heated in **stages** from **298 K** up to **1673 K** (Figure 2 in the article) to capture **dehydroxylation** and **sintering** branches discussed alongside **WAXS**/**PDF**; the proof text describes multi-**stage** thermal programs rather than a single isothermal **production** block. **Barostat / pressure:** **N/A —** **NVT** (constant **volume**). **PBC** **supercell** with **atom** count per the **kaolinite** model in §2.1. **Electric field / enhanced sampling:** **N/A —** not part of the stated **ReaxFF** **protocol**.
## Findings

- **298–873 K:** **Dehydroxylation** converts **octahedral Al** in crystalline **kaolinite** toward **metakaolin** with **~90% tetrahedral Al** (abstract).
- **1055–1673 K (metakaolin branch):** **Sintering** leads to **mullite** emergence (abstract).
- **Heating rate:** **Fast** heating lowers **onset** temperatures (**dehydroxylation ~425 K**, **sintering ~1055 K**) versus **slow** heating (**~622 K** and **~1100 K** respectively in abstract).
- **Model–experiment map:** Strong agreement **below ~1000 K**; **minor deviations** at **T > 1000 K** on their regime map (abstract), motivating cautious interpretation of highest-temperature defect chemistry.
- **Mullite** emergence is discussed in connection with **Al/Si** **reorganization** after **metakaolin** forms, tying **exothermic** events in **thermal** traces to **specific** **atomic** **rearrangements** in the **simulation** logs.

## Limitations

**Proof PDF**; confirm polished **Chem. Mater.** values after publication. **ReaxFF** kinetics can diverge from experiment at the highest **T** where **defect** chemistry is complex. Heating-rate shifts in onset temperatures are valuable for qualitative process maps but should be cross-checked against furnace calibrations and beam heating artifacts that operando X-ray setups can introduce independently of the MD model.

## Relevance to group

Joint **experimental X-ray** + **ReaxFF** workflow for **clay mineral** processing and **high-temperature** geochemical materials.

## Citations and evidence anchors

- [10.1021/acs.chemmater.9b03929](https://doi.org/10.1021/acs.chemmater.9b03929) — corpus PDF is a **Chem. Mater. proof**; confirm final pagination against the version-of-record.

## Reader notes (navigation)

- Clay / aluminosilicate thermal chemistry + X-ray validation: cluster with [[theme-oxides-silica-ceramics]].
- Corpus PDF is an ACS **proof**; see [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section D for proof-handling guidance.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
