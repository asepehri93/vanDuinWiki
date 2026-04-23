---
id: paper:2020sim-acs-enhanced-fuel
type: paper
title: "Enhanced Fuel Decomposition in the Presence of Colloidal Functionalized Graphene Sheet-Supported Platinum Nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:graphene-carbon
  - keyword:nvt-simulation
  - keyword:reaxff-application
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1021/acsaem.0c01010"
year: 2020
authors:
  - "Hyung Sub Sim"
  - "Richard A. Yetter"
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
  - "Daniel M. Dabbs"
  - "Ilhan A. Aksay"
venue: "ACS Appl. Energy Mater. 2020, 3, 7637–7648"
pdf_sha256: "e33e68a6ce487279b06297b4fef98e92f3339756f2c529aa3489c606d88bd9b6"
pdf_path: "papers/Sim_ACS_ApplEngMat_2020_Pt_graphene.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020sim-acs-enhanced-fuel -->

## Summary

**Experiments** and **ReaxFF MD** address **Pt nanoparticles on functionalized graphene (Pt@FGS)** in **n-dodecane** under **supercritical** conditions. Under **4.75 MPa** and **753–803 K**, a suspension of **50 ppmw Pt@FGS** (reported as **~10 ppmw Pt**) increases **fuel conversion** by up to **~24%** and strongly increases **H₂** yield (up to **~12.5×** in the abstract’s comparison). **ReaxFF** trajectories of **n-dodecane** **pyrolysis** support a **synergistic Pt–FGS** mechanism favoring **dehydrogenation** relative to **FGS-only** or **Pt-cluster** baselines. **Pt@FGS** is reported **colloidally stable**; post-reaction **Pt–FGS** characterization shows **no gross deterioration** of the composite under the conditions studied.

## Methods

- **Experiments:** **Supercritical** **n-dodecane** pyrolysis at **4.75 MPa** and **753, 773, or 803 K** with **5.0 mL/min** flow; loadings **50 ppmw** **Pt@FGS** (quoted as **~10 ppmw Pt**), **FGS**, **Pt** cluster, and neat fuel baselines; **K-type** thermocouples and **degas** at **0.05 MPa** before pressurization (see article for reactor and **GC** analytics).
- **ReaxFF MD (ADF):** **ReaxFF** for **C/H/O/Pt** in **ADF** (parallel **ReaxFF-MD**); **energy minimization**, **equilibration at 100 K**, then **heat to 3000 K at 10 K/ps**; production **NVT** at **1500-1900 K** for **1.0 or 2.0 ns**, **time step 0.2 fs**. **NVT** product snapshots at **~0.31 g/cm3** (see figure discussion).

**MD application (n-dodecane pyrolysis).** Amsterdam Density Functional (ADF) **reactive molecular dynamics** (**ReaxFF** for C/H/O/Pt); 3D PBC supercells of n-dodecane (with Pt/FGS chemistry as in the paper) near **0.31 g cm⁻³**; **0.2 fs** timestep; **thermostat**-controlled **NVT** production segments at **1500–1900 K** for **1.0** or **2.0** **ns** after a **10 K ps⁻¹** ramp to **3000** **K** from a **100 K** **preequilibration** (see `pdf_path` for the full sequence). **Pressure:** the **4.75 MPa** and **bar**-scale **reactor** **readings** are **for** the **flow**-**reactor** **(experiment)**; the **NVT** **reactive** **trajectories** **as** **summarized** **are** run **at** **constant** **volume** with **no** **hydrostatic** **barostat** in **those** **1–2** **ns** **stages** **(see** **article** **if** a **separate** **NPT** **preequilibration** **exists**)**. **Barostat: N/A** in the **quoted** **NVT** **spans** **(constant**-**cell**). **Shear / shock, static electric field, umbrella / replica: N/A** in the ReaxFF ramp as summarized here.

## Findings

- **Pt@FGS** additives **stabilize Pt** in suspension and, under the reported supercritical conditions, **increase fuel conversion** compared with relevant baselines.
- At **50 ppmw Pt@FGS**, conversion increases by up to **~24%**, with large increases in **low-MW pyrolysis products** and **H₂ yield** up to **~12.5×** relative to the comparison cited in the abstract.
- **ReaxFF MD** supports a mechanism in which **Pt and FGS act together** to promote **dehydrogenation** during **n-C₁₂H₂₆** pyrolysis, more so than either component alone in the modeled scenario.
- **Post-reaction** examination of **platinum-decorated FGS** suggests **no significant degradation** of the **composite particle** morphology or function under the reported conditions.

Together, the reactor data and atomistic trajectories support a picture in which **nanoscale Pt** and **functionalized graphene** cooperate at the **fuel–additive interface**, shifting pyrolysis branching toward **dehydrogenation**-favored product channels under the stated supercritical conditions. **Limitations and outlook (as in article):** see **## Limitations**; **reactor** **pressure** **(MPa)** **in** **experiment** **is** **not** **the** same **constraint** as **NVT** **reactive** **MD**—compare **across** **stages** **only** **with** **the** **PDF**.

## Limitations

Atomistic models necessarily **simplify** nanoparticle–solvent interfaces and **long-time** kinetics; quantitative alignment with the **flow-reactor** experiments requires careful comparison of **temperature**, **pressure**, and **time scales** between MD and experiment.

## Relevance to group

**van Duin** co-authorship; combines **jet-fuel–relevant** pyrolysis chemistry with **ReaxFF** interpretation of **metal–carbon** synergy.

## Citations and evidence anchors

- DOI: `10.1021/acsaem.0c01010`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
