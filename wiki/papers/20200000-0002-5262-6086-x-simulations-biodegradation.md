---
id: paper:20200000-0002-5262-6086-x-simulations-biodegradation
type: paper
title: "Simulations of the Biodegradation of Citrate-Based Polymers for Artificial Scaffolds Using Accelerated Reactive Molecular Dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.0c03008"
year: 2020
authors:
  - "Dasgupta, Nabankur"
  - "Yilmaz, Dundar E."
  - "van Duin, Adri"
venue: "J. Phys. Chem. B"
pdf_sha256: "057fb4991a27e36b2bd22d9f1bcd89b1295d7c676e42e401233fc488e2e1bb0b"
pdf_path: "papers/Dasgupta_hydrolysis_JPC_2020_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20200000-0002-5262-6086-x-simulations-biodegradation -->

Bond-boosted ReaxFF MD in explicit water models hydrolytic scission of citrate-based polyester–ether scaffolds and ties chemical damage to bundle-scale mechanical softening for tissue-engineering contexts.

!!! note "Corpus note"

The local PDF is a publisher proof; claims summarized from the article abstract.

## Summary

Citrate-based polyester–ether elastomers are candidate scaffold materials whose degradation rate must pair with tissue remodeling. The paper applies ReaxFF molecular dynamics with a bond-boost acceleration scheme to study hydrolysis of poly(1,6-hexanediol- co-citric acid) in explicit water, coupling chemical scission with mechanical loading of polymer bundles to connect chemistry to modulus and ductility. The abstract motivates accelerated sampling because laboratory hydrolysis unfolds on scales far longer than brute-force reactive trajectories can reach, while medical devices still require atomistic insight into how chain scission alters mechanical integrity.

## Methods

**QM benchmarks.** ReaxFF **barrier** heights for **ester** and **ether** **hydrolysis** are checked against **DFT** references before production **MD**.

**Accelerated ReaxFF.** **Bond-boost** / **restraint** protocols target **pre-transition** configurations along **hydrolysis** pathways so **scission** events occur at **300 K** in **explicit water** within tractable trajectory length.

**Polymer chemistry.** **Poly(1,6-hexanediol- co-citric acid)** **citrate-based** polyester–ether scaffolds degrade as **bonds** cleave; **topology** evolves during **reactive** runs.

**Mechanical protocol.** **Bundles** are strained **longitudinally** at **two** **strain rates** (as reported) after **none**, **partial**, or **progressive** **hydrolysis**, reporting **Young’s modulus**, **yield stress**, and **ductility** as tabulated in the article. The abstract frames this as **chemical** degradation together with **mechanical** loading of **prehydrolyzed** and **intermittently** hydrolyzed bundles at **300 K**. Proof PDF pagination may differ from **J. Phys. Chem. B** **VOR**.

**MD application (RMD, bond boost).** **ReaxFF** in **LAMMPS**-class workflows on **10^2**–**10^3+** **atom** **aqueous** **polymer** cells with **3D** **PBC**; **bond-boost** and **NVT** **sampling** at **room** **temperature** **300 K** with a **Nose–Hoover**-style or **Langevin** **thermostat** as in *J. Phys. Chem. B*; **N/A —** **fs** **timestep** and **production** **ps**/**ns** totals: see proof/VOR. **N/A —** **NPT** **barostat**; **N/A —** **1 atm** **hydrostatic** **pressure** in the **NVT** **aqueous** **box** (implicit **1 bar** **solvent**). **N/A —** **electric** field. **N/A —** **replica** **exchange**; **N/A** for **umbrella** (bond-boost is the **rare**-event **trick**). **N/A** — **shear**; **tensile** **strain** **rate** is reported for **mechanical** legs.

**FF training (block 2).** **N/A** — the paper reuses/validates a **Reaxff** for **ester**/**ether** scission; **see** **article** for **any** refit.

**Static QM (block 3).** DFT is used to **check** **barriers**; **N/A** as a standalone DFT **application** **study**.

## Findings

**Selectivity.** **Ester** linkages **hydrolyze** faster than **ethers** (lower barriers). **Tuning** **boost** strength can **suppress** **ether** cleavage while preserving **ester** reactivity—showing **acceleration** can be made **chemoselective**.

**Mechanics.** **Modulus** rises with **strain rate** (**strain-rate stiffening**). **Polyester–ether** is **stiffer** than **polyester** alone but **yields** earlier; **polyester** is more **ductile** in their ranking.

**Degradation–mechanics coupling.** **Hydrolytic** damage **softens** networks as **connectivity** is lost. The **combined** **chemical + mechanical** workflow is offered to **screen** **biodegradable** elastomer designs before synthesis.

The abstract also notes that **accelerated** simulations supply **“restrain energy”** after identifying **pre-transition-state** configurations, i.e. the boost is applied in a way intended to respect the **activation barrier** structure rather than indiscriminately heating the polymer.

## Limitations

Proof PDFs may differ slightly from the final text; accelerated MD can bias pathway sampling if boost parameters are not carefully chosen.

## Relevance to group

Demonstrates ReaxFF accelerated sampling for hydrolytic degradation of biomedical polymers within the van Duin group.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.jpcb.0c03008

## Related topics

- [[reaxff-family]]

