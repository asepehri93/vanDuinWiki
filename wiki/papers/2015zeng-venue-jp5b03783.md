---
id: paper:2015zeng-venue-jp5b03783
type: paper
title: "Reactive Molecular Dynamics Simulations on the Disintegration of PVDF, FP-POSS, and Their Composite during Atomic Oxygen Impact"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5b03783"
year: 2015
authors:
  - "Fanlin Zeng"
  - "Chao Peng"
  - "Yizhi Liu"
  - "Jianmin Qu"
venue: "J. Phys. Chem. A"
pdf_sha256: "0eec5deb59fb9801a0753453fafc88ef728ec629e6c9c14ea63731527daafc0b"
pdf_path: "papers/ReaxFF_others/Zeng_PVDF_FP_POSS_JPCA_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015zeng-venue-jp5b03783 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes **J. Phys. Chem. A** (**DOI** `10.1021/acs.jpca.5b03783`) per `pdf_path`.

## Summary

Low-Earth-orbit spacecraft materials face hyperthermal atomic oxygen beams that oxidize and erode polymer surfaces; fluoropolymers and silicon-containing additives are used strategically to manage mass loss and heat loads. The introduction situates PVDF as a soft, piezoelectric polymer used in aerospace smart structures and cites literature measurements of atomic-oxygen erosion for PVDF in LEO, motivating quantitative benchmarking of simulation against experimentally reported erosion yields. This *Journal of Physical Chemistry A* article reports ReaxFF molecular dynamics simulations of atomic oxygen bombardment of polyvinylidene fluoride (PVDF), fluorinated polyhedral oligomeric silsesquioxane (FP-POSS), and PVDF/FP-POSS composites, tracking temperature rise, mass loss, and erosion yield as functions of oxygen dose. The abstract states that simulated PVDF erosion yields align closely with experiment, supporting parametrization quality for that subsystem, while FP-POSS exhibits stepwise erosion with a threshold atomic-oxygen dose attributed to a protective silicon–oxygen cage architecture absent in neat PVDF. Flight-chemistry analysis and structural snapshots are used to argue that erosion of PVDF and the composite follows continuous matrix-derived pathways, whereas FP-POSS shows a stepped onset tied to cage integrity. Composites reduce temperature rise, mass loss, and erosion yield relative to neat PVDF in the reported comparisons.

## Methods

**LAMMPS** **ReaxFF** for **C/H/F/O/Si** (`papers/ReaxFF_others/Zeng_PVDF_FP_POSS_JPCA_2015.pdf`, Simulation Models, §2); model building also references **Materials Studio**. Systems: **neat PVDF** (**32** chains, **50** repeats, **9664** atoms, **1.8 g cm⁻³** initial density), **neat FP-POSS** (**100** molecules), and **PVDF/FP-POSS** (**32** chains + **8** FP-POSS), Figs. 1–3. **50 000**-step **NPT** at **1 atm**, **200 K**, **0.5 fs** densifies packings to **~1.63**, **~1.83**, and **~1.72 g cm⁻³** respectively. Each slab sits in a **120 Å** “well”; **20 000**-step **NVT** at **200 K** equilibrates before impacts. **NVE** **40 000**-step cascades (**0.5 fs**) introduce **50** hyperthermal **O** atoms every **400** steps (**200 fs**) at **7.4 km s⁻¹** along **−z** (**~4.5 eV**/atom in the LEO-motivation text); **PBC** in **x/y**, free **z** in the well. **NPT** uses **1 atm** target; no barostat during **NVE** impacts. **Thermostat** for **NPT** packing: **N/A —** not spelled out in the indexed excerpt (see PDF). **200 K** preparation; **NVE** allows sharp heating. Tracked observables include **temperature**, **mass loss**, **erosion yield**, and **flight-chemistry** vs dose (abstract, §3). No electric field or enhanced sampling.

**Force-field training:** **N/A —** prior **CHON** / fluoropolymer **ReaxFF** parametrizations are cited and applied.

**Static QM / DFT:** **N/A —** not the primary modality.

## Findings

**Simulated PVDF erosion yields** match **experimental** LEO-style yields cited in the article, supporting the **PVDF** subsystem (abstract). **FP-POSS** shows **stepped** erosion with a dose threshold explained by a protective **Si–O cage**. **PVDF** and **PVDF/FP-POSS** follow **continuous matrix-derived** erosion in the authors’ classification versus the **stepped** **neat FP-POSS** mode. **§3** compares **neat** vs **composite** temperature and mass-loss traces. The **AO** insertion schedule sets how fast **non-equilibrium heating** and fragmentation build; the Discussion flags **model-size** and **non-equilibrium** caveats for late-stage temperature spikes. External **Harbin / Northwestern** reference for **LEO polymer erosion** with **ReaxFF**.

## Limitations

Beam simulations omit synergistic low-Earth-orbit effects such as ultraviolet radiation and electron bombardment that modify real degradation rates. ReaxFF cannot capture charge-transfer excitations or electronic sputtering explicitly; readers should treat chemistry as ground-state reactive dynamics with known force-field approximations.

## Relevance to group

The study is a reference application of ReaxFF to space-environment polymer erosion, adjacent to oxidative and materials-durability modeling threads in the corpus.

## MAS / retrieval notes

For LEO materials durability queries, combine `keyword:polymer`, `keyword:reaxff-application`, and `keyword:validation-experiment`; cite hyperthermal oxygen flux and dose metrics from the article when users ask for erosion yield comparisons between PVDF and FP-POSS.

## Citations and evidence anchors

- **DOI:** `10.1021/acs.jpca.5b03783` — `papers/ReaxFF_others/Zeng_PVDF_FP_POSS_JPCA_2015.pdf`.

## Related topics

- [[reaxff-family]]
