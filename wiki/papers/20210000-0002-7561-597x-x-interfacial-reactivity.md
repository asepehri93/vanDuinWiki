---
id: paper:20210000-0002-7561-597x-x-interfacial-reactivity
type: paper
title: "Interfacial Reactivity and Speciation Emerging from Na-Montmorillonite Interactions with Water and Formic Acid at 200 °C"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:oxide-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsearthspacechem.0c00286"
year: 2021
authors:
  - "Murali Gopal Muraleedharan"
  - "Hassnain Asgar"
  - "Seung Ho Hahn"
  - "Nabankur Dasgupta"
  - "Greeshma Gadikota"
  - "Adri C. T. van Duin"
venue: "ACS Earth Space Chem."
pdf_sha256: "0dccb1338208f2468a74bbee495f6891bd27ea8b0bc35130dc823ee9e89e5758"
pdf_path: "papers/Muraleedharan_ACS_EarthSpace_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20210000-0002-7561-597x-x-interfacial-reactivity -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Earth Space Chem.** (**DOI** in front matter). The registered PDF is a **galley**; confirm pagination against the **version of record** if needed.

## Summary

The study couples **ReaxFF molecular dynamics** at **473 K** (**200 °C**) and **1 atm** with **FTIR** and **small-/wide-angle X-ray scattering (SAXS/WAXS)** to probe **water**–**formic acid** chemistry on **Na-montmorillonite**. A **new ReaxFF** parametrization for **clay–fluid** interactions is benchmarked against **spectroscopy** and **scattering**, then used to map **reaction pathways** and **speciation** across **basal**, **edge**, and **interlayer** environments—highlighting how **local** **solvation** and **faceting** alter **catalytic** behavior.

The scientific motivation is **subsurface** and **planetary** **analog** chemistry where **clays** interact with **organic acids** and **hot water**, producing **carbonate**, **formate**, and **hydroxide**-related moieties that are detectable spectroscopically but difficult to assign without **atomistic** models.

## Methods

**1 — MD application.** **ReaxFF** **(LAMMPS) MD** of **Na-montmorillonite** + **water** + **formic** **acid** in **3D** **PBC** **(clay** **slab/aggregate)** **supercells** at **473 K** and **1 atm** (≈1 **bar** **NPT** or **fixed** **NVT**+**H** **(P)**-style setup—see *ACS Earth Space Chem.* for whether **NPT** **Parrinello**–**Rahman** or **NVT**+**Langevin** **+** **external** **pressure** **correction** is used). Sub-1 **fs** **timestep**; **ps–ns** **(multi-stage)** **equilibration**/**production**; **Nose**–**Hoover**-type **(or** **Berendsen** **+** **NH)** **thermostat**; **NPT** **(if** interlayer** **d-spacing** is relaxed) **/ NVT** **(if** only **interlayer** **spacing** is **manually** **held)**. **Interfacial** **reactivity** **(basal** **vs** **edge** **vs** **interlayer)** in **reactive** **clay-FF** **runs**. **Electric** **field**; **rare**-**event** **(umbrella)**—**N/A** unless the **SI** adds a method. **Coulomb**+**EEM** in **ReaxFF** (paper).

**2 — Experiments (integrated).** **FTIR** of **H₂O/FA** **(formic** **acid)** **+** **clay**; **SAXS/WAXS** for **interlayer** **spacing** and **precipitate** **(carbonate)**-related **contrast**—benchmarks the **ReaxFF** speciation and **d**-**spacing** trends.

**3 — Force-field training** for **clay+fluid+organic** **acid** **(Na**+**H₂O+FA)**: **ReaxFF** is **(re)parametrized** against **DFT** **(training** set**)** on **relevant** **Si–O–H**, **H-bonding**, and **C–H/O** **subsets**—see the **J.** **for** the **PBE**/**functional**+**k-mesh** **(QM** **line)** and **optimization** **(parrex)**, plus **IR**+**SAXS/WAXS** **(experiment)** for **post-fit** **validation** **(benchmarks)**.

**4 — Galley** `pdf_path`—confirm **VOR** **(Limitations**).

## Findings

**Spectroscopy agreement.** The authors state **ReaxFF** **MD** can reproduce **key** **FTIR** **features** for the **H₂O/FA**+**clay** **compositions** **(discussion)**. **Scattering** **(SAXS/WAXS)**: **interlayer** **carbonate**-**signal**-consistent** **(and** **d**-**spacing)** **scenarios** **vs** **simulation**. **Mechanisms:** **basal/edge/interlayer** **(faceting,** **solvent** **penetration)** show **diverging** **reaction** **networks** **(carboxylate,** **formate,** **carbonate** **(OH)** **(authors’** **narrative)**. **Comparisons** = **ReaxFF**+**clay-FF** **vs** **laboratory** **IR+** **scattering** **(experiment)**, with **N/A** **(atomistic** **+** **continuum)** for **upscaling** to **reactor** **(Limitations**).

## Limitations

**Galley** PDF; **long-time** **geochemical** equilibria may require larger cells and longer trajectories. **ReaxFF** for **clay** systems must be validated when **cation** identity, **layer** **charge**, or **salinity** changes.

## Relevance to group

Demonstrates **van Duin**-line **ReaxFF** integrated with **spectroscopy** and **scattering** for **clay**–**fluid** chemistry relevant to **Earth**/**space** geochemistry and **interface** science.

## Citations and evidence anchors

- DOI [10.1021/acsearthspacechem.0c00286](https://doi.org/10.1021/acsearthspacechem.0c00286).
- Excerpt alignment: `normalized/extracts/20210000-0002-7561-597x-x-interfacial-reactivity_p1-2.txt`.

## Reader notes (extended)

Operators refreshing **`source_refs`** on theme hubs should treat this article as an exemplar of **spectroscopically anchored** **clay** simulations: updates to the **ReaxFF** database for **interlayer** ions or **edge** chemistry should trigger a **light** review of claims tied to **IR**/**scattering** agreement.

## Related topics

- [[reaxff-family]]
