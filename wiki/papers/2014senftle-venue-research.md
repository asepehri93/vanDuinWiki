---
id: paper:2014senftle-venue-research
type: paper
title: "A ReaxFF investigation of hydride formation in palladium nanoclusters (ACS author proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
  - task:validation
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1021/jp411015a"
year: 2014
authors:
  - "Thomas P. Senftle"
  - "Michael J. Janik"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C (ACS proof PDF; same DOI as jp411015a)"
pdf_sha256: "aa5ba5d5af9a3ac4bce74aae4e29bbc718b640a3f806f6826a37a289e24dfb4a"
pdf_path: "papers/Senftle_PdH_JPCCproof_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014senftle-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This manifest row registers an **ACS author-proof** PDF variant of **Senftle, Janik & van Duin**, *J. Phys. Chem. C*, on **Pd/H** **ReaxFF** modeling (DOI **10.1021/jp411015a**; canonical narrative: `paper:2014senftle-venue-jp411015a`). **Palladium** **dissociates** and **absorbs** **hydrogen**, motivating **membranes**, **storage**, and **catalyst** designs. The **abstract** describes deriving a **ReaxFF Pd/H** potential from **extensive quantum data** for **bulk** and **surface** properties, then applying a **hybrid grand-canonical Monte Carlo / molecular dynamics (GC-MC/MD)** method to compute **hydrogen absorption isotherms** for **Pd bulk** and **nanoclusters** over **H₂ pressures ~10⁻¹–10⁻¹⁴ atm** and **temperatures 300–500 K**. **Equilibrated** cluster structures illustrate roles of **surface**, **subsurface**, and **bulk** regions in **size-dependent** transitions between **low-H** **solid-solution (α-like)** and **high-H hydride (β-like)** regimes and **miscibility-gap** behavior. Additional **MD** studies address **dissociative adsorption kinetics** and extract **H diffusion coefficients**, **barriers**, and **pre-exponential** factors from **bulk Pd** trajectories. The abstract states **thermodynamic** (**GC-MC/MD**) and **kinetic** (**MD**) results **agree with experimental literature**, validating the **Pd/H** parameterization.

## Methods

This slug’s **ACS author-proof** PDF is the **same article** as **`[[2014senftle-venue-jp411015a]]`** (DOI **10.1021/jp411015a**). Methods mirror that page; only **PDF provenance** differs.

### ReaxFF training / sampling (see VOR page for authoritative pagination)

- **Pd/H ReaxFF** derived from **extensive QM data** for **bulk** and **surface** properties (abstract).
- **GC-MC/MD** **hydrogen absorption isotherms** for **Pd bulk** and **~1.0–2.0 nm** clusters over **p(H₂) = 10⁻¹–10⁻¹⁴ atm** and **T = 300–500 K** (abstract).
- **MD** for **dissociative adsorption** kinetics in clusters and **H diffusion** in bulk **Pd** (**coefficients**, **barriers**, **pre-exponentials** reported in the article).
- **Timestep / thermostat / cutoffs:** use the **version-of-record** Methods/SI—not inferred here.

**Grand-canonical / MD protocol:** identical to **`[[2014senftle-venue-jp411015a]]`**: **molecular dynamics** segments support **GC-MC/MD** **hydrogen absorption isotherms** for **Pd bulk** and **nanoclusters** with **H\(_2\)** **pressures** spanning **\(10^{-1}\)**–**\(10^{-14}\)** atm and **temperatures** **300–500 K** (abstract). **Ensemble:** **NVT** **molecular dynamics** is used for the relaxation/kinetics portions as described in the **JPCC** article (see **version-of-record** **`[[2014senftle-venue-jp411015a]]`**). **Engine, timestep (fs), thermostat, PBC, barostat, and full ps/ns tables:** **N/A —** not retyped on this **proof** wiki page—use **`papers/Senftle_PdH_JPCCproof_2014.pdf`** or the **typeset** sibling PDF.

## Findings

- **Proof extract** aligns with the **published** narrative summarized on **`[[2014senftle-venue-jp411015a]]`**: **thermodynamic** GC-MC/MD results and **kinetic** MD observables reported as **consistent with experiment**; **miscibility-gap** / **α–β** framing for **clusters** with **surface/subsurface/bulk** decomposition of **H** content.
- **Pd/H** parameters are described as **transferable** with prior **Pd/O** work for future **Pd/O/H** catalysis extensions (abstract).
- Use **`[[2014senftle-venue-jp411015a]]`** for **figure/table** citations; this **proof** slug exists for **byte-accurate** manifest hashing of the alternate PDF.

## Limitations

**Proof** PDFs may show **placeholder** metadata or **typography** drift—cite **`paper:2014senftle-venue-jp411015a`** for **pagination**. Maintain **separate** manifest rows for **hash** provenance only. **GC-MC/MD** **sampling** details (**chemical potential** grids, **cluster** **sizes**, **equilibration** lengths) materially affect **isotherm** shapes—reuse **numerical** **plateau** positions only after confirming the **Methods** section in the **version-of-record** article.

## Relevance to group

Duplicate **PDF** lineage for the **same** scientific artifact; useful when only the **proof** bytes are archived locally. The **Pd/H** **GC-MC/MD** workflow is a **canonical** example of **open ensemble** **ReaxFF** practice in the **van Duin** corpus and pairs with **hydrogen-storage** and **catalysis** notes on **Pd** surfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp411015a](https://doi.org/10.1021/jp411015a) — `papers/Senftle_PdH_JPCCproof_2014.pdf`; extract `normalized/extracts/2014senftle-venue-research_p1-2.txt`; canonical article page: `paper:2014senftle-venue-jp411015a`.

## Related topics

- [[reaxff-family]]
