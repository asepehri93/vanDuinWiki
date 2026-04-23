---
id: paper:2020perras-j-phys-chem-full-scale-ab
type: paper
title: "Full-scale ab initio simulation of magic-angle-spinning dynamic nuclear polarization"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:reaxff
  - task:method-development
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:validation-experiment
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.0c00955"
year: 2020
authors:
  - "Frédéric A. Perras"
  - "Muralikrishna Raju"
  - "Scott L. Carnahan"
  - "Dooman Akbarian"
  - "Adri C. T. van Duin"
  - "Aaron J. Rossini"
  - "Marek Pruski"
venue: "The Journal of Physical Chemistry Letters"
pdf_sha256: "b59862ea03ecb189ac8acb61114bcbff67d483c1f8e68310aa1f5696b7223331"
pdf_path: "papers/Perras_Raju_Akbarian_MAS_JPC_Letters_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020perras-j-phys-chem-full-scale-ab -->

## Summary

The work extends **steady-state dynamic nuclear polarization (DNP)** modeling to **thousands of coupled nuclei** in periodic cells at **experimental** biradical and solvent concentrations. For each polarizing agent (**bTbK** or **TEKPol** in **16 mM** 1,1,2,2-tetrachloroethane (TCE)), **ReaxFF MD** supplies condensed-phase snapshots; selected structures are geometry-optimized into a **44.62 Å** cube with **1H** density matched to neat TCE (**592** TCE + one biradical; **1224** or **1256** **1H** spins in the spin Hamiltonian, depending on agent). A **large-scale ab initio MAS-DNP** treatment (LR-LCL and related Liouville restrictions in the paper; **MAS 10 kHz** in the reported comparisons) computes **steady-state** enhancements and MAS-rate dependence against **experiment** for frozen solutions and solids, with **quantitative** agreement in showcased cases and analysis of **distance-dependent depolarization**—linking **classical** ReaxFF solvent structures to **quantum** spin dynamics under **magic-angle spinning**.

## Methods

- **Structure sampling:** **ReaxFF-based MD** of TCE solutions (multiple trajectory lengths) with **five** snapshots per system, optimized into periodic cells (**592** TCE molecules + **one** polarizing agent; **1224** or **1256** **1H** spins depending on agent—see article).
- **DNP theory layer:** Ab initio MAS-DNP solver using aggressive Liouville-space restrictions (LR-LCL framework) and steady-state polarization constraints; **MAS 10 kHz** in the reported comparisons.
- **Experiment:** Companion DNP/NMR/EPR data and relaxation inputs summarized in the article/SI.

**1 — MD application (sampling for snapshots).** The *J. Phys. Chem. Lett.* text runs **ReaxFF-based molecular dynamics** on **16 mM 1,1,2,2-tetrachloroethane (TCE)** solutions of **bTbK** and **TEKPol**; **varying** trajectory lengths, **five** **snapshots** per solution, and **geometry-optimized** **cubic** **supercells** of **592 TCE** + **one** **biradical** (**44.62 Å** edge, **thousands of atoms** per **condensed-phase** **box**), matching the **1H** spin counts in the DNP model (**1224** vs **1256** protons) and **2** **electron** **spins** per agent. **PBC** are used so the DNP model can treat a **condensed** solution. **N/A —** the article cites prior ReaxFF MD work for engine-level settings (thermostat, **fs** timestep, total **ns** sampled); pull **timestep**, **ensemble** labels, and run lengths from `pdf_path` and **SI** when **reproducing** **MD** (this wiki only mirrors the **abstract/Methods**-level **summary**). **Barostat: N/A —** not part of the stated **LR-LCL** DNP **spin** **solver**; **N/A —** no **NPT** **sampling** in the ab initio MAS-DNP **layer** as summarized (optimization of **polarization** in **Liouville** **space**). **Electric** **(microwave) coupling:** treated in the DNP **theory** **(Landau–Zener**-style **rotor** **events)**, not as a **classical** **E-field** in **ReaxFF**. **Metadynamics / replica exchange: N/A —** not in the ReaxFF stage per this summary.

**2 — Force-field training: N/A —** this paper **uses** a published **ReaxFF** to **sample** **structures**, it does not **reparameterize** the FF here.

**3 — Static QM / DFT: N/A —** central advance is the **ab initio** MAS-DNP **spin** **dynamics** with LR-LCL, not a DFT **benchmark** of **barriers** for a new **surface** model. **4 — Other:** spin basis and **LR-LCL** **truncation** **tolerances** in **SI**.

## Findings

- Achieves **quantitative** reproduction of experimental DNP enhancements and their **MAS** dependence for the highlighted frozen-solution and solid cases.
- Highlights a structural motif in some agents that mitigates **spin-diffusion barrier** losses (as discussed in the abstract).
- Demonstrates feasibility of **full-scale** quantum simulations of DNP for large **1H** baths when combined with snapshot sampling.

The discussion ties agreement with experiment to radial organization of electron–nuclear proximities (agent-dependent), motivating improved rare-conformation sampling in future work. **Corpus honesty:** full spin-basis and MD engine details are in `pdf_path` and **SI**, not duplicated here.

## Limitations

Heavy dependence on polarizing-agent geometry sampling and electronic structure approximations inside the DNP model; ReaxFF solvent configurations are classical and may miss rare configurations.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

van Duin and Akbarian as co-authors; ReaxFF used as a practical sampler for condensed-phase spin coordinates feeding quantum DNP theory.

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
