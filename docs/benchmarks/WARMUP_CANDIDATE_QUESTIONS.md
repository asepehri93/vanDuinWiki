# Candidate benchmark questions (LLM warm-up pool)

**Status:** Candidate pool for maintainer selection — **not** the frozen v1 benchmark set.  
**How produced:** Categories were inferred from a **survey of this repository’s PDF corpus** (paths, filenames, and recurring themes across ~190 PDFs; excluding AppleDouble `._*` sidecars). Questions were **authored at mid-level granularity** to avoid useless generality (“anything ReaxFF”) and avoid single-paper trivia.  
**Next step:** After an abstract-level warm-up pass over the PDFs, refine categories and swap any misfit questions; then **pick 50** (or fewer) to promote toward a frozen evaluation file in Phase 5.

See [`../PHASE0.md`](../PHASE0.md) for KPI thresholds and the official LLM warm-up workflow.

### Corpus evidence (Phase 3)

**Profile run:** 2026-04-20 — [`outputs/corpus_profile_2026-04.md`](../outputs/corpus_profile_2026-04.md) (190 PDFs registered; aggregate stats in [`normalized/corpus_summary.json`](../normalized/corpus_summary.json)). Title-keyword frequencies support the buckets below (e.g. strong **ReaxFF / reactive MD** presence; recurring **graphene**, **pyrolysis**, **nickel**, **water**, **carbon**, **oxidation**, **fuel**, **mechanical** / **plasma** themes). Taxonomy alignment notes: [`outputs/taxonomy_phase3_review.md`](../outputs/taxonomy_phase3_review.md).

---

## High-level categories (corpus-derived)

These buckets organize the question list; they are **not** the final Phase 2 taxonomy.

1. **Reactive MD, ReaxFF, and reactive force-field parameterization** — bond-order / ReaxFF family work, combustion and organics, Si/O/H systems, `eReaxFF`-style extensions where present.  
2. **Classical / empirical FF beyond single-bond-order** — CEMFF, hybrid or multi-scale mentions, specialized fits.  
3. **Battery materials and interfaces** — Li metal, Li–S, Li-ion carbons, Na-ion / NASICON-class, electrolytes and interphases.  
4. **Oxides and ceramic surfaces** — SiOₓ, TiO₂, AlOₓ, GeOₓ, ceria, complex oxides; corrosion / leaching angles where present.  
5. **2D materials and layered systems** — MoS₂, silicene, BN, graphene-related.  
6. **Carbon materials and hydrocarbons** — soot, DLC, graphite / petroleum coke, carbon oxidation, aromatic / PAH chemistry.  
7. **Catalysis and surface reactions** — noble metals, oxide-supported catalysis, fuel-related chemistry.  
8. **Ferroelectrics and polar polymers** — perovskite-adjacent and polymer ferroelectric / high-κ style topics where filenames suggest it.  
9. **Water, silica, and geochemical / environmental interfaces** — clays, water films, environmental chemistry.  
10. **Organic / polymer oxidation and pyrolysis** — CHO chemistry, polymers, energetic materials where present.  
11. **Mechanics, fracture, tribology, nanoindentation** — mechanical response coupled to chemistry.  
12. **Machine-learned potentials and emerging FF paradigms** — neural/network potentials, Allegro-class, reviews of ML for atomistic simulation.

---

## 50 candidate questions (numbered)

### Reactive MD, ReaxFF, parameterization (1–9)

1. Across our corpus, **which material or chemical classes** have received **multiple independent ReaxFF (or closely related reactive FF) parameterizations**, and where do documented **validation strategies** agree or differ?  
2. For **oxide–water or silica–water interfaces**, what **protocol choices** (system size, water model coupling, QM training data) recur in ReaxFF-oriented work, and what **limitations** are explicitly stated?  
3. Where does the KB document **eReaxFF or charge-equilibration-style extensions** relative to standard ReaxFF, and for **which application domains** (e.g. organics vs oxides) are they used?  
4. What **combustion or high-temperature hydrocarbon** studies in the KB rely on **reactive MD**, and how is **soot or PAH formation** tied to simulation setup and validation?  
5. For **Si/O/H-rich glasses or gels**, what **prior reactive FF coverage** does the KB summarize, and which **property targets** (structure, reactivity, mechanical) are emphasized?  
6. Which papers address **metal–oxide** interfaces under **reactive conditions**, and does the KB connect them to **consistent force-field or multi-scale protocols**?  
7. How does the KB represent **parameterization workflow** (training sets, QM level, objective functions) for **ReaxFF family** models, and where are **failure cases** noted?  
8. For **heterogeneous catalysis** treated with **reactive MD**, what **surface models and reaction diagnostics** appear across papers, and what **gaps** show up when linking to `methodprotocol` pages?  
9. Where do sources discuss **transferability** of a reactive parameter set **across temperatures or phases**, and does the KB surface **disagreements** with citations?

### Batteries and electrochemical interfaces (10–15)

10. What **Li-host or Li-metal interface** problems are represented, and which **interphase or electrolyte decomposition** mechanisms are tied to **specific simulation methods**?  
11. For **sulfur-based cathode chemistry** in the corpus, what **atomistic modeling approaches** are used, and how does the KB link them to **known limitations** (time scale, charge models)?  
12. How does the KB summarize **carbon anode / Li–C** modeling across papers—**intercalation vs surface reactions**—and which **force fields or DFT protocols** recur?  
13. What **Na-ion or NASICON-class** materials appear, and does the KB map them to **ionic transport** modeling traditions used in those papers?  
14. Where **solid electrolyte or ceramic electrolyte** interfaces appear, what **defect or grain-boundary** angles are emphasized, and are they connected to **broader protocol pages**?  
15. For **multivalent or non-Li systems** (if present), does the KB clarify **whether classical reactive MD is used vs DFT**, and with what **stated scope**?

### Oxides, ceramics, corrosion (16–20)

16. What **Al- or Si-rich oxide** thin-film or etching problems are covered, and how do **simulation choices** compare across studies (e.g. kinetics vs thermodynamics emphasis)?  
17. For **TiO₂–water or TiO₂ interface** work, what **reproducible modeling themes** emerge (surface facet, defects, photochemistry vs classical MD)?  
18. How does the KB treat **ceria or reducible oxide** surfaces in **catalysis or oxidation**, and where are **charge models** discussed relative to **classical MD**?  
19. Where **corrosion, leaching, or dissolution** appear, what **time-scale bridging** (MD vs continuum hints) is documented between papers?  
20. For **complex multi-cation oxides** (if present), does the KB aggregate **perovskite or ferroelectric-adjacent** simulation threads separately from **glass or silica** threads?

### 2D materials and carbon (21–26)

21. What **MoS₂ or transition-metal dichalcogenide** studies exist, and how does the KB relate them to **defect, edge, or contact** modeling?  
22. For **silicene or other 2D group-IV** mentions, what **stability or substrate effects** are emphasized across sources?  
23. How does the KB summarize **graphene or CNT** interface work—**functionalization, defects, or metal contacts**—and which **methods cluster** together?  
24. For **hexagonal BN or B–N chemistry**, what **reactive or classical** approaches appear, and for **which property questions**?  
25. What **soot, carbon black, or aromatic growth** mechanisms are represented, and how does the KB tie them to **reactive MD validation**?  
26. For **DLC or disordered carbon**, what **force-field or tight-binding** threads appear, and where does the KB mark **uncertainty**?

### Catalysis and organics / polymers (27–32)

27. Across **Pt-, Pd-, or Ni-based** surface chemistry papers, what **reaction families** recur, and does the KB map them to **shared simulation checklists**?  
28. For **CHO / oxygenate chemistry** on metals or oxides, where do sources agree on **key intermediates**, and where does the KB record **contested mechanisms** only with evidence?  
29. What **polymer or PVDF-related** polar materials appear, and how does the KB separate **ferroelectric / dielectric** questions from **purely mechanical** ones?  
30. For **pyrolysis, fuels, or oxygenate decomposition**, what **temperature and pressure regimes** dominate, and which **diagnostics** (species tracking, bond counts) are standard in the corpus?  
31. How does the KB treat **zeolite or confined porous** chemistry if present—**adsorption vs reaction**, and **force-field limitations**?  
32. Where **lipid, soft matter, or biological-adjacent** filenames appear, does the KB classify them under a **distinct protocol family**, or flag them as **out-of-band** for the core MAS scope?

### Ferroelectrics, mechanics, environment (33–38)

33. What **BaTiO₃ or perovskite-adjacent** polarization studies are in scope, and how does the KB connect them to **MD vs DFT** usage?  
34. For **ferroelectric polymers or high-κ organics**, what **property predictions** are emphasized, and are **force-field choices** justified consistently across papers?  
35. Where **fracture, crack propagation, or nanoindentation** appear, how does the KB relate **mechanical boundary conditions** to **chemical reactivity** when both are discussed?  
36. For **tribology or sliding interfaces**, what **wear chemistry** themes emerge, and does the KB link them to **reactive vs non-reactive** models?  
37. What **environmental or clay / mineral** interface studies exist, and how does the KB summarize **water structure vs reaction** contributions?  
38. For **HMX or energetic materials** (if present), what **safety-relevant decomposition** modeling traditions appear, and how are they **segregated** from general combustion work?

### Machine learning, multi-scale, reviews (39–44)

39. Where **neural or machine-learned potentials** appear, what **data sources and validation metrics** are emphasized, and does the KB separate **bulk vs surface** applications?  
40. How does the KB represent **Allegro- or graph-neural** potential lines vs **traditional FFs**—**when to use which**, per documented evidence?  
41. What **mixed QM/MM, DFT sampling, or tight-binding** hybrids show up as **feeds** into force-field fitting in our corpus?  
42. For **review or tutorial-style** PDFs, does the KB extract **actionable protocol bullets** without turning reviews into uncited claims?  
43. Where **PIMD or nuclear quantum effects** are mentioned, does the KB tie them to **specific material problems** (e.g. light elements) rather than generic statements?  
44. How does the KB handle **software or method papers** (LAMMPS ecosystem, accelerators) — as **`methodprotocol`** anchors or separate bibliographic notes?

### Cross-cutting KB / MAS utility (45–50)

45. For a **new oxide surface + water** study, what **prior group knowledge** does the KB surface about **recommended FF families, known failure modes, and benchmark comparisons**?  
46. If a MAS must choose between **classical reactive MD and on-the-fly quantum**, what **decision criteria** can be assembled **only** from cited work in the KB?  
47. Which **recurring validation quantities** (energies, barriers, structures, spectroscopic proxies) span multiple papers in the same theme, and where is **cross-paper consistency** weak?  
48. What **systematic gaps** appear—**material classes** mentioned often in titles but **without** associated `forcefield` or `methodprotocol` pages?  
49. Where might **contradictory claims** arise between papers on the **same material family**, and does the KB already route those to **`debate` pages** or flag them for one?  
50. Considering **group-wide research trajectories**, what **three cross-theme synthesis articles** would most improve **MAS planning** (concept-page candidates), and **which existing papers** would anchor each?

---

## Maintenance

- **Append** new candidate questions after each major ingest; **tag** with date and category.  
- **Demote** questions that become too easy after wiki maturity.  
- **Promote** a frozen subset per [`../PHASE0.md`](../PHASE0.md) before retrieval grading.
