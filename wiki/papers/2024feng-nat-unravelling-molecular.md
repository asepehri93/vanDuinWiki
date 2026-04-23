---
id: paper:2024feng-nat-unravelling-molecular
type: paper
title: "Unravelling molecular origins of improved tribological properties of amino acid ionic liquid water-based lubricants"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reactive-md-generic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:validation-experiment
  - keyword:nvt-simulation
candidate_tags:
  - "AAIL-lubrication"
source_refs: []
doi: "10.1016/j.triboint.2024.110268"
year: 2024
authors:
  - "Yang Feng"
  - "Ahmad Jabbarzadeh"
venue: "Tribol. Int. 201 (2025) 110268"
pdf_sha256: "946f1b1a1fb3362828d718e029ef44d933fac02ec38ab5b2fe524c848aeaea68"
pdf_path: "papers/ReaxFF_others/Feng_Amino_IL_Tibology_Int_2025.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024feng-nat-unravelling-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **Tribology International** article (**DOI** in front matter). The abstract states **reactive molecular dynamics**; the **specific reactive force field** (for example **ReaxFF** vs another reactive model) must be taken from the article **Computational Methods** section—**not** from the short corpus extract alone.

!!! note "Year vs venue"

    The PDF path references **2025** volume/page numbering while wiki `year` follows the **accepted article** metadata; adjust for your bibliography style if you require the **print** year only.

## Summary

The work combines **tribometer experiments** and **reactive molecular dynamics** to explain how **water-based lubricants (WBLs)** gain **friction** and **rheology** benefits from **amino-acid ionic liquids (AAILs)** based on **tetrabutylphosphonium (P₄₄₄₄)** cations paired with **serine** or **tryptophan** anions. The authors measure **coefficient of friction** for **AAIL–water** blends versus neat **water** and interpret improvements through **interfacial** structure on **iron oxide** surfaces under **shear**, emphasizing **hydration shells** around **amino-acid** anions and **cation**-rich **load-bearing** regions in the **film** interior.

The abstract attributes up to **~34%** **friction** reduction versus baseline **WBL** performance and proposes a **dual-layer** mechanism: **hydration lubrication** stabilizes a **chemisorbed** **tribofilm** anchored by **anion**–**surface** interactions, while **P₄₄₄₄** contributes **mechanical** support in the **midplane** of the **film**. Thicker, more **stable** **hydrated** **tribofilms** correlate with larger **friction** reductions among fluids tested.

## Methods

### Tribology experiments

**Coefficient of friction** and **rheology** for **P\(_{4444}\)** **AAIL**/**water** blends vs neat **water**—concentrations and test geometry in *Tribol. Int.* **Methods**.

### Reactive MD under shear (B)

**Reactive MD** on **iron oxide**/**lubricant** interfaces (**bond-making/breaking**, **shear**); **FF** identity (**ReaxFF** vs other), **cutoffs**, **thermostat**, **Δt**, **shear** rate in **Computational Methods**—**not** in `normalized/extracts/2024feng-nat-unravelling-molecular_p1-2.txt` (abstract/intro only).

**MD application (reactive, tribology).** **Molecular dynamics** under **shear** in the **Tribology International** text: **MD** **package** and **reactive** **force field** (see **Tribol. Int.**), **N/A** for full table here; **atom** counts, **PBC**/**fixed**-**substrate** regions, **NVE**/**NVT** choice, **time step** (fs), **equilibration**/**production** (ps/**ns**), **Nosé–Hoover**/**Langevin** **thermostat** parameters, **NPT** **Parrinello**/**Berendsen** **barostat** (if isotropic **stress** is targeted), and **shear** **strain** **rate** (s\(^{-1}\)) as tabulated; copy from the **version-of-record** **PDF** rather than the short **extract**. **Temperature** matches **laboratory**-aligned conditions in **Methods**. **N/A**—separate static **E-field** protocol; **N/A**—**metadynamics**/**umbrella** unless the article states otherwise. **Hydrostatic** **pressure** **N/A** if **NVT**/**NVE** **shear** is used without **NPT** coupling.

## Findings

The study links **macroscopic** **friction** trends to **molecular** **film** structure: **hydration** around **amino-acid** anions supports **tribofilm** formation on **oxide**, while **cation** layering contributes **load support**. The **dual-layer** picture is presented as reconciling **fluidity** with **load-bearing** capacity in **green** **tribology** contexts.

**Comparisons, sensitivity, corpus note.** The abstract reports up to **~34%** **reduction** in **coefficient of friction** under stated conditions, **comparing** **blends** to baseline **WBLs**; **sensitivity** to **anion** identity (**serine** vs **tryptophan**) and **P₄₄₄₄**-rich midplane support is a central theme. **version-of-record** **Tribol. Int.** is authoritative for the **reactive** **FF** name and **slab** **protocols**.

## Limitations

Without naming the **reactive model** from the abstract alone, avoid attributing results specifically to **ReaxFF** until confirmed in the **Methods**. **Room-temperature** **tribology** experiments may not map one-to-one to **idealized** simulation **slabs** and **shear rates**.

The **serine vs tryptophan** anion pairing with **P₄₄₄₄** is a chemically meaningful axis: **aromatic** **tryptophan** versus **polar** **serine** changes **hydrophobic/hydrophilic** balance and likely changes **tribofilm** **stability**, consistent with the abstract’s emphasis on **hydration-shell**-mediated films.

## Relevance to group

Adjacent **reactive MD** **tribology** on **oxide** **surfaces** in **aqueous ionic** environments—comparator for **ReaxFF** **interfacial** studies in **mechanochemistry** and **lubrication** themes.

## Citations and evidence anchors

- DOI [10.1016/j.triboint.2024.110268](https://doi.org/10.1016/j.triboint.2024.110268).

## Related topics

- [[reaxff-family]]
