---
id: paper:2022castel-j-phys-chem-challenges-molecular
type: paper
title: "Challenges in Molecular Dynamics of Amorphous ZIFs Using Reactive Force Fields"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - method:aimd
  - material:zeolite-porous
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:aimd
  - keyword:lammps
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c06305"
year: 2022
authors:
  - "Nicolas Castel"
  - "François-Xavier Coudert"
venue: "J. Phys. Chem. C"
pdf_sha256: "7a2ac8b3ddd7d6db979b1b8d40a293480d17f3387b4cfd93c4026b6cf90814b4"
pdf_path: "papers/ReaxFF_others/ZIF_ReaxFF_AIMD_comparison_JPCC_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022castel-j-phys-chem-challenges-molecular -->

## Summary

The authors replicate literature melt-quench workflows that use the Yang et al. ReaxFF parameterization for zeolitic imidazolate frameworks (ZIFs) in LAMMPS and compare the resulting amorphous models to ab initio references and experiments. They conclude that outputs are highly sensitive to quench rate, thermostat/barostat choices, and supercell size, and that standard ReaxFF-quenched glasses can deviate strongly from AIMD and experiment, especially in local coordination statistics. The paper is explicitly cautionary for anyone porting ZIF melt-quench recipes across software versions or box sizes without revalidation.

## Methods

**1 — MD application (atomistic dynamics).** The study uses **LAMMPS** with the **Yang et al.** **ReaxFF** for **ZIF-4** (see *J. Phys. Chem. C* **Computational Methods** for the full parameter citation). **Timestep 0.25 fs**. **System:** a **(2×2×2) ZIF-4** supercell of **\(\sim 2176\)** atoms with **3D PBC**, following Yang et al. Melt, quench, and analysis stages are run mainly under **isotropic NPT** with a **Nosé–Hoover** thermostat and barostat; by default the paper fixes **\(\sim 100\,\text{fs}\)** and **\(\sim 1000\,\text{fs}\)** damping for temperature and pressure coupling (values retested in sensitivity analysis). **NVT** trajectories of **\(\sim 1\,\text{ns}\)** on ReaxFF-quenched glasses provide **RDFs**, **angular** distributions, **coordination** statistics, and **mass** **density** (sampling every **125 fs** for RDFs in the published protocol). The authors **replicate** the published **melt–quench** schedule, then **sweep** **quench** **rate**, **thermostat/barostat** details, and **(2×2×2)** vs other **supercell** choices; representative **input** files are **archived** in the authors’ **citable data** repository (URL in the **PDF**). **N/A** — static external **electric** field in the production protocol; **N/A** — umbrella or metadynamics (standard melt–quench only). **ReaxFF** **QEq** and **nonbonded** **cutoffs** follow the **Yang** **ZIF** **ReaxFF** + **LAMMPS** conventions detailed in the article.

**2 — Force-field training.** **N/A** — the work **applies** the **published** **Yang** **ZIF** **ReaxFF**; it does **not** refit the parameter set.

**3 — Static QM / DFT and AIMD (reference).** The paper reports shorter **PBE+TS**-class **VASP** **ab initio** **trajectories** (**\(\sim 60\,\text{ps}\)** **NVT** segments) on melt–quenched **ZIF-4** glasses for direct comparison to ReaxFF; **PBE**/**PAW**/**k**-mesh and related settings are in *J. Phys. Chem. C*.

**4 — Experiments.** **N/A** as a primary new experimental campaign; structural **comparisons** use **ab initio** data and **literature** **Raman**/**SAXS**-style information as referenced in the discussion.

## Findings

**Outcomes and mechanisms.** Reproducing published **Yang-style** **melt–quench** procedures still leaves **RDFs**, **coordination** (including **Zn**–**N** and imidazolate connectivities), and **angular** statistics **sensitive** to small **thermostat/barostat** and **quench** choices. **ReaxFF**-quenched **ZIF-4** glasses can **differ markedly** from the **PBE+TS** **ab initio** **melts** in the same study and from **known experimental** signposts for amorphous ZIFs, including **unphysical** local **coordination** that propagates to **medium-range** order, **density**, and derived properties.

**Comparisons.** Direct **ReaxFF** vs **VASP**-AIMD on **ZIF-4** glasses; **RDF** peak positions and amplitudes shift with **protocol** enough to make **blind** transfer of **RDFs** between publications **unsafe** without revalidation. Literature **experimental** trends enter as **context**, not as new in-house **synthesis** data in this paper.

**Sensitivity and design levers.** **Quench** **rate**, **thermostat**/**barostat** **damping** choices, and **box** size are the main **sensitivity** axes demonstrated in the article.

**Corpus / KB honesty.** Cite **numerical** **RDF**/**density** **values** from the **VOR** **PDF**; this wiki emphasizes **reproducibility** **warnings** from the **abstract** and **Discussion**.
## Limitations

AIMD length and size limits constrain reference data; force-field error may be entangled with protocol choices. Users should treat melt-quench “failure” here as a workflow sensitivity statement: modest thermostat tweaks or longer liquid annealing can shift glass densities enough to change conclusions about whether ReaxFF agrees with AIMD, so reproduction requires archiving full input decks rather than headline quench rates alone. Anyone reusing the **Yang** **ZIF** parameter set should therefore treat **RDF**/**coordination** checks as **mandatory** regression tests when **LAMMPS** builds or **supercell** sizes change.

## Relevance to group

Critical assessment of ReaxFF melt-quench for MOF glasses—directly relevant to users of ZIF ReaxFF workflows. Anyone porting Yang-parameter melt recipes into new LAMMPS builds should treat this paper as a mandatory regression check on coordination statistics before publishing new amorphous structures.

## Citations and evidence anchors

- [10.1021/acs.jpcc.2c06305](https://doi.org/10.1021/acs.jpcc.2c06305)

## Reader notes (navigation)

- Critical **ZIF / MOF glass** melt-quench methodology; compare with porous-material applications in [[theme-reactive-md-corpus]].

## Related topics

- [[reaxff-family]]
- [[theme-reactive-md-corpus]]
