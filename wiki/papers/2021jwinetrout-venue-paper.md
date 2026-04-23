---
id: paper:2021jwinetrout-venue-paper
type: paper
title: "Implementing Reactivity in Molecular Dynamics Simulations with the Interface Force Field (IFF-R) and Other Harmonic Force Fields"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:classical-ff-specialized
  - domain:methods-software
  - method:reactive-md-generic
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2021
authors:
  - "Jordan J. Winetrout"
  - "Krishan Kanhaiya"
  - "Geeta Sachdeva"
  - "Ravindra Pandey"
  - "Behzad Damirchi"
  - "Adri van Duin"
  - "Gregory Odegard"
  - "Hendrik Heinz"
venue: "Archived preprint / conference manuscript in corpus (IFFR_archived_2021.pdf)"
pdf_sha256: "d79c0ed9a9b94d0cb7943b28a1877fbc576369bb6a75decb4aaab3b9e37dda27"
pdf_path: "papers/IFFR_archived_2021.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021jwinetrout-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the manuscript identified by `pdf_path`. For definitive program names, numerical inputs, and benchmark tables, use the full PDF (or a peer-reviewed venue of record) rather than this page alone.

## Summary

Interface force field (IFF) models reproduce interfacial and bulk energetics for many multiphase systems, but bond rupture to failure is often out of scope. Winetrout *et al.* introduce Reactive IFF (IFF-R): selected harmonic bond terms are replaced with Morse potentials so bonds can dissociate with user-set dissociation energies and curvatures, while preserving nonreactive IFF parameters when those bonds are intact. The abstract advertises stress–strain to failure in molecular dynamics for Fe, carbon-nanotube-like models, and polymers (e.g. polyacrylonitrile, cellulose Iβ), with sample parameters from experiment and MP2 where stated, and claims about 50× higher throughput than ReaxFF in their examples. The checked-in file is an archived venue draft—confirm bibliography and any revised parameters if citing externally.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** The abstract and first-page text describe **molecular dynamics** with **IFF/IFF-R**-compatible **bonding**; **N/A** — a specific program (e.g. LAMMPS) is not named in the indexed first pages. Confirm in `pdf_path` if a code string is required.
- **System size & composition:** Illustrative systems from the abstract: **Fe**; a carbon-**nanotube**-like model; **polyacrylonitrile** and **cellulose** Iβ. Atom counts and supercell construction: see the full PDF and any supplement.
- **Boundaries / periodicity:** **N/A** in the first-page **extract**; PBC in tensile/condensed demos is plausible—**verify** in the archived file.
- **Ensemble, temperature, barostat, and pressure control:** **N/A** in the lead excerpt. Tensile **ramp** work often uses fixed **T**; **NPT** bulk pressure control and **N/A**-style hydrostatic setpoints are **not** assumed. **N/A** — isotropic NPT is not stated; anisotropic tensile load is not a bulk hydrostatic **pressure** in the same sense. Follow the full article for the load path.
- **Timestep, duration, stages, thermostat:** **N/A** in p.1–2; pull equilibration **duration**, **ps** / **ns** **production** spans, and **thermostat** family from the VOR. Common **NVT**-class control in tensile studies is a reasonable expectation but is not in the lead excerpt.
- **Electric field:** **N/A** in the lead excerpt.
- **Enhanced sampling (umbrella, metadynamics, etc.):** **N/A** in the lead excerpt. Morse reactivity is a force-field form, not umbrella or metadynamics in the usual sense.

### 2 — Force-field training

IFF extension, not a ReaxFF refit. **Morse** **bonds** replace selected **harmonic** **bonds**; inherited Lennard–Jones and other **nonreactive** IFF **parameters** are unchanged for inactive bonds. **N/A** — this is not a global ReaxFF (ParReax, QEq) **parameter** **fit**. The abstract cites **MP2** and **experiment** to anchor dissociation-related **data** and positions **~50×** **lower** **cost** than ReaxFF in the authors’ **comparative** **runs** (stated in the **abstract**).

### 3 — Static QM / DFT

**MP2**-level and related **high-level** data plus **laboratory** **measurements** (per abstract) back selected Morse/IFF **choices**; not a DFT-sweep primary study in the p.1 summary sense.

### 4 — Reviews, perspectives, or non-simulation studies

**N/A** — methods paper with case studies, not a broad literature review (venue may be report-like).

## Findings

The **abstract** claims that computed **moduli**, **tensile** **strength**, **structures**, and **surface** **energies** track **available** **experiment** when the Morse layer is inert, keeping **nonreactive** properties close to **IFF** by design, and that throughput can exceed that of ReaxFF **trajectories** in their **side-by-side** **stated** **comparisons**. Sensitivity to Morse well depth and stiffness is inherent; detailed stress–strain to **failure** must be read from the **full** **PDF** at `pdf_path`, not retyped on this page. **Corpus / KB honesty:** `doi` in front matter is **empty**; the corpus holds an **archived** preprint—confirm a **formal** **publication** if a citation must be final.

**Comparisons:** to standard IFF in nonreactive limits and to ReaxFF in **comparative** **cost** language in the **abstract**. **Limitations (authored + KB):** extract-thin; **N/A** for reproducing the full result section from p.1–2 alone.

## Limitations

IFF-R targets **localized** **bond** **scission** with Morse **bonds**; it is not a ReaxFF-style **broad** **reaction** field. Verify **bibliography** and any **tabled** parameters against a VOR or updated PDF if one exists off-repo.

## Relevance to group

**van** **Duin** is a coauthor; the paper is a **contrast** to ReaxFF-family work when the chemistry is **failure**-limited rather than a full **reaction** **network** at scale.

## Citations and evidence anchors

`papers/IFFR_archived_2021.pdf` — title, abstract, author list (p.1–2 indexed in `normalized/extracts/` when present).

## Related topics

- [[reaxff-family]]
