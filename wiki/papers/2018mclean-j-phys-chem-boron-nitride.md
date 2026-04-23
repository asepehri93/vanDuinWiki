---
id: paper:2018mclean-j-phys-chem-boron-nitride
type: paper
title: "Boron Nitride Nucleation Mechanism during Chemical Vapor Deposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:npt-simulation
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b05785"
year: 2018
authors:
  - "Ben McLean"
  - "Grant B. Webber"
  - "Alister J. Page"
venue: "J. Phys. Chem. C 2018, 122, 24341–24349"
pdf_sha256: "682bdc2ee043a62577eae13476c8773c54ab042b0d51e6518188b61110017288"
pdf_path: "papers/ReaxFF_others/McLean_Page_BN_CVD_JPC_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018mclean-j-phys-chem-boron-nitride -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **J. Phys. Chem. C** (**DOI** in front matter). Temperatures, durations, and stoichiometries below follow **Table 1**/**Figure** captions in the article.

## Summary

**Nonequilibrium ReaxFF molecular dynamics** in **SCM** software uses the **HBN** parameterization cited in the paper to simulate **gas-phase** chemistry relevant to **boron-oxide-assisted** **chemical vapor deposition** of **BN** from precursors such as **B₂O₂** and **NH₃** in the presence of a **boron nanoparticle** seed. Subsequent long **annealing** of **amorphous BN** networks explores conversion toward **tube-like** **nanostructures**, offering a mechanistic narrative for **nucleation** and **defect healing** under **high-temperature** **nonequilibrium** conditions.

The study emphasizes distinct roles for **H₂O** and **H₂** in **clustering**, **BN** **ring** formation, and **passivation** pathways, connecting **gas-phase** speciation to **surface** chemistry at the **boron** **particle**.

## Methods

### A — Force-field training / scope

- **ReaxFF** **HBN** parameterization for **B/N/O/H** chemistry as cited in *J. Phys. Chem. C* (training data and element coverage in **Methods**/**SI**).

### B — Nonequilibrium reactive MD (gas-phase CVD chemistry)

- **Software:** **SCM** **ReaxFF** implementation (as stated in the article).
- **Ensemble / conditions:** **NPT** **nonequilibrium** trajectories modeling **boron-oxide-assisted** **BOCVD**-like stoichiometries (**1100 °C**, **1 atm** per **Table 1** caption); multiple runs vary **initial** **gas** cells (**Fig. 1** / **Table 1**).
- **Species / chemistry:** gas-phase **B–O**, **NH\(_3\)**, **H\(_2\)O**, **H\(_2\)**, and **boron nanoparticle** seed motifs as built in the published setups.

### C — Annealing of condensed BN networks

- **Long (~20 ns)** **trajectories** on **amorphous BN** networks to probe **defect** relaxation and evolution toward **tube-like** **nanostructures** (duration/statistics in **Results**).

### D — Experiments

- **Not a primary experimental paper**; **CVD** motivation is **literature**-driven with **atomistic** mechanism focus.

### MD application (nonequilibrium gas-phase + anneal)

**Engine / code:** **ReaxFF** as implemented in **SCM** software (§2.1 of *J. Phys. Chem. C*). **System & composition:** periodic cells for **B\(_2\)O\(_2\)** + **NH\(_3\)** **BOCVD**-like stoichiometries with a **boron nanoparticle** seed; initial volumes summarized in **Table 1** / **Figure 1** of the article (`papers/ReaxFF_others/McLean_Page_BN_CVD_JPC_2018.pdf`). **PBC:** **three-dimensional PBC** for the gas/nanoparticle supercells described in **Table 1**. **Ensemble:** **NPT** **nonequilibrium MD** for the gas-phase nucleation trajectories (**1100 °C**, **1 atm** per **Table 1** caption). **Timestep / thermostat / barostat specifics:** **N/A — not transcribed** in this excerpt-based note—copy from §2.1 and **Table 1** footnotes. **Temperature:** **1100 °C** (**~1373 K**) for the tabulated **NPT-MD** reaction ensemble; additional **annealing** stages use the **~20 ns** **amorphous BN** trajectories quoted in the abstract. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** for the nonequilibrium **BOCVD** runs in the abstract framing.
## Findings

**BN ring** formation is **mediated** by the **boron nanoparticle** and promoted by pathways producing **H₂O** as described in the mechanism section. **H₂** assists **BₓOᵧ** clustering into **catalytic** **B** nanoparticles, whereas **H₂O** promotes **BN** bond formation and **ring condensation** in **gas phase** and at the **particle** surface. Extended **annealing** converts **amorphous BN** networks toward **tube-like** motifs in the reported trajectories.

**Comparisons / sensitivity.** The abstract contrasts roles of **H\(_2\)** vs **H\(_2\)O** partial pressures and highlights **nanoparticle** presence vs purely gas-phase pathways—central **sensitivity** axes for **BOCVD** nucleation in this model.

**Limitations / outlook.** **ReaxFF** kinetics remain empirical; **reactor-scale** transport and **substrate** effects are outside the emphasized **gas-phase** narrative (see **## Limitations**).

**Corpus honesty.** Quantitative rates and additional simulation IDs beyond **Table 1** should be read from the **PDF**; this page summarizes abstract + indexed extract alignment only.
## Limitations

**High-temperature** **reactive** kinetics are sensitive to **ReaxFF** parameterization; quantitative **growth** rates require **experimental** calibration. **Gas-phase** models omit **full reactor** transport and **substrate** interactions present in real **CVD**.

The **nonequilibrium** framing matters for **retrieval**: this is not an equilibrium **phase diagram** study; it is a **kinetic** narrative about how **B**-rich **clusters**, **H₂O**/**H₂** speciation, and **BN** **ring** formation interact in **hot** gas environments relevant to **CVD** **precursor** chemistry.

## Relevance to group

Demonstrates **ReaxFF** on **BN** **CVD** **nucleation** with explicit **nonequilibrium** **gas/surface** pathways—useful alongside **2D** **TMD** and **oxide** **CVD** simulation literature.

Downstream **retrieval** questions about **BN** **nanotube** vs **sheet** formation should cite this work for **early-stage** **ring** formation and **defect** **annealing** language, while recognizing that **substrate**-mediated growth modes may require additional models not emphasized in the **gas-phase** focus here.

## Citations and evidence anchors

- DOI [10.1021/acs.jpcc.8b05785](https://doi.org/10.1021/acs.jpcc.8b05785).
- Excerpt alignment: `normalized/extracts/2018mclean-j-phys-chem-boron-nitride_p1-2.txt`.

## MAS / retrieval

`paper_keywords` **`keyword:npt-simulation`** flags the **nonequilibrium** **gas-cell** work; pair with **`keyword:reaxff-application`** when indexing **BN** **CVD** questions in **Phase 5** chunks.

## Related topics

- [[reaxff-family]]
