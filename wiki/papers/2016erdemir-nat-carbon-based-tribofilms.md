---
id: paper:2016erdemir-nat-carbon-based-tribofilms
type: paper
title: "Carbon-based tribofilms from lubricating oils"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:carbon-hydrocarbon
  - task:experiment-integrated
  - method:aimd
  - method:reactive-md-generic
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:combustion
  - keyword:validation-experiment
  - keyword:aimd
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1038/nature18948"
year: 2016
authors:
  - "Ali Erdemir"
  - "Giovanni Ramirez"
  - "Osman L. Eryilmaz"
  - "Badri Narayanan"
  - "Yifeng Liao"
  - "Ganesh Kamath"
  - "Subramanian K. R. S. Sankaranarayanan"
venue: "Nature"
pdf_sha256: "5c988305eb16abdbd21c766bf35aefb1fbfce89cca9ba6f681dd88100b6e2ff1"
pdf_path: "papers/ReaxFF_others/Erdemir_nature_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016erdemir-nat-carbon-based-tribofilms -->

## Summary

Erdemir *et al.* report **ball-on-disk** tribology experiments on **nanocrystalline MoNₓ–Cu** and related **nitride** coatings that can catalyze **in situ** formation of **diamond-like carbon (DLC)-like tribofilms** from **base-oil hydrocarbons**, achieving **low friction** and **near-zero wear** without conventional **zinc dialkyldithiophosphate (ZDDP)** antiwear additives (*Nature*, DOI `10.1038/nature18948`). The study couples **in operando** **tribometry** with **reactive** and **ab initio** **molecular dynamics** to propose a **tribochemical** mechanism: **olefin dehydrogenation**, **C–C scission**, and **reassembly** into an **amorphous carbon** film at **high-pressure** **sliding** contacts. Sankaranarayanan’s involvement links the work to the broader **reactive MD** community adjacent to **ReaxFF**-style hydrocarbon chemistry, even though the paper’s simulation stack is not exclusively **ReaxFF**.

## Methods

**Experiment (materials + tribology):** **Nanocomposite nitride** coatings (**~90–95 at.%** transition-metal nitride with **~5–10 at.% Cu** catalyst, e.g. **MoN\(_x\)–Cu** on **AISI 52100** steel) are synthesized and imaged by **cross-sectional TEM/HRTEM**, **EDS**, and **XPS** (see *Nature* Letter and **Extended Data**). **Ball-on-disk** tribometry at **~1.3 GPa** contact pressure compares **PAO** base oil, **fully formulated 5W30** (with **ZDDP**), and **uncoated** steel references; friction, wear, and **TOF-SIMS** evidence for tribofilms are reported in the main text.

**MD / AIMD application (supporting mechanism):** **Reactive** and **ab initio MD** illustrate **dehydrogenation** of **linear olefins**, **random C–C backbone scission**, and **recombination** into a compact **amorphous-carbon** tribofilm on **model catalytic** surfaces under **high-pressure, sliding-like** loads (*Nature* abstract and figures). **Slab** geometries use **in-plane PBC** as described in the **Letter** and **Supplementary Methods**. **Ensemble (NVT/NPT/NVE) for each AIMD segment:** **N/A — not on the short front-matter extract**; see **Supplementary Methods**. **Trajectory duration (ps/ns) per reported segment:** **N/A — not on the short extract**; see **SI**. **Engine, timestep, thermostat/barostat, supercell sizes, imposed shear or strain rate, and target temperatures:** **N/A — not on the short front-matter extract** used for this page; read **Supplementary Methods** for reproducible settings. **Replica / umbrella / metadynamics:** **N/A — not indicated** in the indexed text.

**Force-field training:** **N/A — not a parameterization study.**

**Static QM / DFT (standalone):** **N/A — folded into AIMD** in the main narrative; any separate **DFT** benchmarks appear at **SI** level.

## Findings

The **catalytic** coatings enable **tribofilms** with **coefficient of friction ~0.08** and **wear rates** approaching **zero** under **1.3 GPa** in **PAO**, reported to **outperform** **ZDDP** **films** in the same tests. Structural probes characterize the films as **DLC-like** **amorphous carbon**. **Simulations** support a pathway involving **dehydrogenation** of **linear olefins**, **random** **backbone scission**, and **recombination** into a **dense** **interfacial** **carbon** network. The **Nature** paper’s significance for **lubrication** science is conceptual as much as numerical: it shows **catalytic** **contacts** can **build** **carbonaceous** **films** from **base** **oil** **feedstocks** that rival **phosphorus**/**sulfur**-rich **ZDDP** **tribofilms** in the reported **metrics**, reframing **additive** design around **surface**-enabled **tribopolymerization** rather than only **ash**-forming chemistry. **Atomistic** readers should treat the MD/AIMD components as **mechanistic** cartoons—informative for **bond** **events**—while recognizing **tribological** **contact** **asperities**, **flash** **temperatures**, and **shear** **rates** span ranges only partially sampled by tractable **simulation** cells. **Fleet** **lubricant** **approvals** also depend on **oxidation** **stability**, **corrosivity**, and **seal** **compatibility** metrics not captured by **friction**/**wear** **tests** alone, even when **DLC**-like **films** form **in situ**.

## Relevance to group

Reactive MD / tribochemistry adjacent to hydrocarbon reactivity themes; Argonne co-author Sankaranarayanan.

## Citations and evidence anchors

- DOI: [10.1038/nature18948](https://doi.org/10.1038/nature18948)

## Related topics

- [[reaxff-family]]
