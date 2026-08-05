---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:25:46.614232'
end_time: '2026-08-04T03:35:58.300637'
duration_seconds: 611.69
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: strictly anaerobic
  trait_identifier: METPO:1000611
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: strictly_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An obligately anaerobic oxygen preference in which a microorganism\
    \ does not grow in the presence of oxygen gas (O\u2082)."
  parent_traits: METPO:1000607
  synonyms: strict obligate anaerobe
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive
    if there is more than half a percent oxygen (Supports strict anaerobiosis as a
    highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is
    a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile
    is described as strictly anaerobic.)'
  causal_graph_summary: 'strict_anaerobe_oxygen_sensitivity: 8 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** strictly anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **strictly anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/strictly_anaerobic.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** strictly anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **strictly anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/strictly_anaerobic.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


# Curation report: strictly anaerobic

**Trait:** `METPO:1000611`  
**Label:** strictly anaerobic  
**Category:** ENVIRONMENT | **Kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** `METPO:1000607`

## 1. Scope summary

`METPO:1000611` should denote an **oxygen-dependent vegetative-growth phenotype**: the microorganism does not grow when exposed to molecular oxygen. The most defensible operational interpretation is growth arrest under a stated O₂ concentration, exposure time, medium, and culture geometry—not necessarily immediate death. In *Bacteroides thetaiotaomicron*, full aeration stops growth within minutes and rapidly stalls glucose catabolism, yet obligate anaerobes can remain viable and resume growth after restoration of anoxia. Thus, “does not grow in O₂,” “loses metabolic activity,” and “does not survive O₂” must not be treated as equivalent observations. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 22-27)

Current expert understanding rejects the old universal explanation that strict anaerobes simply lack superoxide dismutase and catalase. Anaerobes commonly possess SOD or superoxide reductase and catalase or peroxidase systems. Their persistent growth restriction instead often reflects an intrinsic biochemical trade-off: highly efficient anaerobic metabolism depends on low-potential metal centers and radical enzymes that are directly damaged by O₂ and that also generate damaging ROS during aeration. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 13-15)

### Boundary cases

- **Aerotolerant anaerobe:** cannot use O₂ for respiration but tolerates exposure and may grow fermentatively in its presence; exclude from this trait if reproducible growth occurs.
- **Facultative anaerobe:** grows both with and without O₂; exclude.
- **Microaerophile:** requires or preferentially grows at low O₂; exclude unless the organism also has a separately demonstrated no-growth phenotype over the assay range used to define strict anaerobiosis.
- **Nanaerobic respiration:** some organisms conventionally called strict anaerobes grow at nanomolar-to-low-micromolar O₂. *B. fragilis*, for example, uses cytochrome bd at 1,000–1,500 ppm O₂ (reported as approximately 1–2 µM). This is a major boundary case and shows why “presence of any O₂” is too absolute without an assay threshold. (butler2023bacteroidesfragilismaintains pages 1-2)
- **Transient vegetative survival:** survival at 1%, 4%, or even air does not establish growth under those conditions. *C. difficile* cannot grow in air, although a fraction of vegetative cells survives a 4-hour exposure. (caulat2024physiologicalroleand pages 5-7)
- **Spores/dormant cells:** oxygen-resistant spores do not negate strict anaerobiosis of vegetative growth. Annotate life stage.
- **Activity versus growth:** reversible inhibition of anammox activity is not by itself evidence of growth failure. (okabe2023oxygentoleranceand pages 1-2)

## 2. Recommended graph architecture

The most defensible **core causal spine** is:

**O₂ exposure → direct damage to anaerobic radical/low-potential enzymes + adventitious ROS formation → loss of central metabolic and biosynthetic enzyme activity → failure of redox-balanced pyruvate dissimilation and other essential pathways → vegetative-growth arrest.**

Antioxidant and O₂-reduction systems should generally be represented as **modifiers that decrease oxygen sensitivity or increase transient survival**, not as defining causes of strict anaerobiosis. Their effects are strongly taxon-, concentration-, and assay-dependent.

## 3. Candidate nodes grouped by type

### Trait and phenotype nodes

- Strictly anaerobic — `METPO:1000611`
- Anaerobic oxygen preference — `METPO:1000607`
- Oxygen-dependent vegetative-growth arrest — label-only candidate
- Oxygen tolerance / oxygen sensitivity — label-only candidates; do not collapse into the target trait
- Survival after oxygen exposure — label-only assay phenotype
- Nanaerobic growth or respiration — label-only boundary phenotype

### Environmental and experimental factors

- Molecular oxygen — `CHEBI:15379`
- Anoxic environment — ontology grounding should be confirmed against ENVO before curation
- Full aeration / air, approximately 21% O₂ — experimental condition
- Low O₂: <0.4%; intermediate O₂: 0.4–1%; high physiological O₂: 4–5% — assay-specific conditions from *C. difficile*, not universal classes. (caulat2024physiologicalroleand pages 1-2)
- O₂ exposure duration, medium, headspace, agitation, inoculum, growth phase, and life stage — required edge qualifiers

### Reactive chemicals and cofactors

- Superoxide anion — `CHEBI:18421`
- Hydrogen peroxide — `CHEBI:16240`
- Hydroxyl radical — `CHEBI:29191`
- Iron(II) — `CHEBI:29033`
- [4Fe–4S] cluster — use a verified ChEBI identifier during implementation; no identifier asserted here
- Ferredoxin, NADH, NAD⁺, menaquinone, fumarate, succinate, pyruvate, formate, acetyl-CoA — verify exact ChEBI forms and protonation states before YAML entry

### Enzymes, proteins, and complexes

**Vulnerability modules**

- Pyruvate formate-lyase (PFL), a glycyl-radical enzyme
- Pyruvate:ferredoxin oxidoreductase (PFOR), an Fe–S enzyme
- Fumarase/[4Fe–4S] dehydratase
- Aconitase, isopropylmalate isomerase, ribulose-phosphate epimerase, peptide deformylase
- Anaerobic ribonucleotide reductase NrdD
- Hydrogenases and methyl-coenzyme-M reductase as broader taxon-specific candidates

**Protection and tolerance modules**

- Superoxide dismutase; GO molecular-function grounding can be added after verifying the exact term
- Superoxide reductase (Sor)
- Catalase, peroxidases, AhpC/Tpx, rubrerythrin, peroxiredoxin Bcp
- Flavodiiron proteins FdpA and FdpF
- Reverse rubrerythrins revRbr1 and revRbr2
- Cytochrome bd oxidase, CydAB
- Thioredoxin systems and Fe–S-cluster repair systems

### Regulators

- OxyR and PerR — ROS-responsive regulators
- σB — general stress sigma factor in *C. difficile*
- σA — contributes to *revrbr2* and *fdpA* expression in *C. difficile*
- OseR/CD1777 — Spx-like oxygen-responsive regulator in *C. difficile*
- Rex — NADH/NAD⁺-sensing regulator of *fdpF*

### Processes and pathways

- Direct molecular-oxygen inactivation of radical enzymes
- Adventitious one-electron reduction of O₂ and endogenous ROS generation
- Oxidative inactivation of Fe–S dehydratases
- Fenton chemistry and DNA damage
- Pyruvate dissimilation
- Redox-balanced fermentation
- Fumarate respiration
- Nanaerobic O₂ respiration
- O₂/ROS detoxification and oxygen scavenging
- Fe–S-cluster repair and recovery after return to anoxia

## 4. Candidate causal edges

The following table gives the strongest curation candidates and essential caveats.

| priority | subject | predicate | object | organism/context | evidence strength | key caveat |
|---|---|---|---|---|---|---|
| High | oxygen (CHEBI:15379) | directly inactivates | pyruvate:formate lyase (PFL) | *Bacteroides thetaiotaomicron*; aeration blocks pyruvate breakdown | Strong, direct primary evidence (khademian2020doreactiveoxygen pages 1-2) | Strongly taxon-grounded here; broader generalization to all strict anaerobes should remain cautious |
| High | oxygen (CHEBI:15379) | directly inactivates | pyruvate:ferredoxin oxidoreductase (PFOR) | *B. thetaiotaomicron*; rate unaffected by superoxide/peroxide levels | Strong, direct primary evidence (khademian2020doreactiveoxygen pages 1-2) | Mechanism is direct O2 damage in this organism; enzyme isoforms differ across taxa |
| High | aeration / endogenous superoxide | inactivates | fumarase [4Fe-4S] enzyme | *B. thetaiotaomicron*; oxidative damage to Fe-S dehydratase during O2 exposure | Strong primary + review support (lu2021whenanaerobesencounter pages 9-11, khademian2020doreactiveoxygen pages 1-2) | Better curated as superoxide-mediated, not direct O2 damage |
| High | loss of PFL and/or PFOR activity | blocks | pyruvate dissimilation | *B. thetaiotaomicron* central metabolism under aeration | Strong mechanistic support (khademian2020doreactiveoxygen pages 1-2, khademian2020doreactiveoxygen pages 9-10) | Exact logical structure may be OR rather than strict AND, since either block can prohibit growth |
| High | impaired pyruvate dissimilation | causes growth arrest in | strictly anaerobic vegetative cells | *B. thetaiotaomicron*; growth stops within minutes upon aeration | Strong phenotype-mechanism linkage (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 22-27) | Growth arrest is not equivalent to immediate killing; survival and regrowth on return to anoxia are distinct |
| High | revRbr2 | reduces | oxygen to water | *Clostridioides difficile*; low O2 tensions **<0.4%** | Strong recent primary evidence (caulat2024physiologicalroleand pages 1-2) | Range is taxon- and assay-specific; edge reflects contribution to tolerance, not proof of sole mechanism |
| High | FdpA | reduces | oxygen to water | *C. difficile*; low/intermediate O2 tensions **0.4%–1%** | Strong recent primary evidence (caulat2024physiologicalroleand pages 1-2) | Role inferred from mutant phenotypes plus prior in vitro activity; electron donor partners unresolved in vivo |
| High | revRbr1 | reduces | oxygen to water | *C. difficile*; broader O2 range **0.1%–4%** | Strong recent primary evidence (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | Broad-spectrum protector in this species; should not be generalized without taxon tag |
| High | FdpF | reduces | oxygen to water | *C. difficile*; higher O2 **>4%** and air exposure | Strong recent primary evidence (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | Best-supported for survival under high O2/air, not anaerobic growth per se |
| High | revRbr1 / FdpA / revRbr2 / FdpF | promotes survival under | oxygen exposure | *C. difficile*; differential effects across 1%, 4%, and air assays | Strong recent primary evidence (caulat2024physiologicalroleand pages 5-7) | Survival assay on plates is not the same phenotype as growth in oxygenated broth |
| Medium | cytochrome bd oxidase (cydAB) | enables | nanaerobic respiration using O2 as terminal electron acceptor | *Bacteroides fragilis*; **1,000–1,500 ppm O2 (~1–2 µM)** near epithelium | Strong recent primary evidence (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 5-7) | Important boundary case: this is a strict anaerobe with microoxic/nanaerobic respiration, so it should not be overused as a generic trait-defining mechanism |
| Medium | cytochrome bd oxidase (cydAB) | increases activity under | nanaerobic conditions | *B. fragilis*; ~5-fold higher O2-dependent NADH consumption in nanaerobically grown cells | Strong recent biochemical evidence (butler2023bacteroidesfragilismaintains pages 5-7) | Activity increase does not necessarily imply transcriptional induction; post-transcriptional effects likely |
| Medium | superoxide dismutase activity + catalase activity | is associated with increased | oxygen tolerance | anammox "*Ca. Scalindua* sp."; IC50 **18.0 µM**, DOmax **51.6 µM** vs freshwater species IC50 **2.7–4.2 µM**, DOmax **10.9–26.6 µM** | Strong recent comparative evidence (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12) | Association is taxon-specific and comparative; not sufficient alone for a universal causal edge for strict anaerobiosis |


*Table: This table prioritizes the best-supported causal edges and boundary-case mechanisms relevant to METPO:1000611. It is designed to help decide which edges are ready for TraitMech curation and which should remain taxon-qualified or cautious.*

Additional curation-ready triples are listed below. Snippets are short extracts or close textual excerpts from the retrieved source.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|---|
| O₂ (`CHEBI:15379`) | reacts with | PFL glycyl radical | 10.1038/s41579-021-00583-y | “O₂ acts as a diradical that directly reacts with the glycyl radical…causing protein cleavage and inactivation.” | **Strong/general enzyme mechanism**, although physiological importance must be taxon-qualified. Reaction can occur within seconds even at low O₂. (lu2021whenanaerobesencounter pages 4-6) |
| PFL inactivation | inhibits | pyruvate dissimilation | 10.1111/mmi.14516 | “Pyruvate dissimilation…depend[s] upon…PFL and PFOR, that lose activity upon aeration.” | **Strong, *B. thetaiotaomicron*-specific.** Either PFL or PFOR can support growth under the tested anoxic conditions, so encode alternative-path logic carefully. (khademian2020doreactiveoxygen pages 1-2, khademian2020doreactiveoxygen pages 9-10) |
| O₂ (`CHEBI:15379`) | directly inactivates | PFOR | 10.1111/mmi.14516 | “The rate of PFOR damage was unaffected by the level of superoxide or peroxide, showing that molecular oxygen itself is the culprit.” | **High-priority primary edge.** Do not generalize to all PFOR isoenzymes; oxygen-tolerant variants exist. (khademian2020doreactiveoxygen pages 1-2, khademian2020doreactiveoxygen pages 9-10) |
| PFOR inactivation | blocks | redox-balanced pyruvate breakdown | 10.1111/mmi.14516 | PFOR and PFL “fracture pyruvate without generating NADH,” while their catalytic features are incompatible with oxygen. | **Strong but taxon-specific.** Useful intermediate between enzyme damage and growth arrest. (khademian2020doreactiveoxygen pages 9-10) |
| Aeration | increases | endogenous superoxide production | 10.1111/mmi.14516 | “The superoxide stress derives from rapid endogenous O₂⁻ formation.” | **Strong for *B. thetaiotaomicron*.** Candidate upstream source is electron leakage from redox enzymes, but individual source enzymes remain incompletely resolved. (khademian2020doreactiveoxygen pages 9-10) |
| Endogenous superoxide | inactivates | fumarase [4Fe–4S] cluster | 10.1073/pnas.1800120115; 10.1038/s41579-021-00583-y | Endogenous O₂⁻ and H₂O₂ oxidize [4Fe–4S] clusters, causing iron loss and enzyme inactivation. | **Strong.** Curate superoxide-mediated rather than direct-O₂ damage for the demonstrated *Bacteroides* edge. (lu2021whenanaerobesencounter pages 9-11, khademian2020doreactiveoxygen pages 1-2) |
| Superoxide/ROS injury | inhibits | amino-acid biosynthesis and NADPH-producing pathways | 10.1111/mmi.14516 | Damage includes aconitase, isopropylmalate isomerase, ribulose-phosphate epimerase, and peptide deformylase. | **Moderate-to-strong, taxon-specific aggregate edge.** Prefer enzyme-specific edges if graph size permits. (khademian2020doreactiveoxygen pages 9-10) |
| H₂O₂ + Fe(II) | produces via Fenton chemistry | hydroxyl radicals | 10.1038/s41579-021-00583-y | “H₂O₂ reacts with intracellular Fe(II) to generate hydroxyl radicals that damage DNA.” | **Mechanistically strong but not necessarily the proximate cause of growth arrest in every anaerobe.** (lu2021whenanaerobesencounter pages 11-13) |
| PFL/PFOR and fumarase inactivation | causes | aerobic growth arrest | 10.1111/mmi.14516 | “Upon aeration its glucose catabolism quickly stalled”; growth “stops within minutes.” | **High-priority phenotype edge for *B. thetaiotaomicron*.** Growth arrest should not be encoded as cell death. (khademian2020doreactiveoxygen pages 1-2) |
| revRbr2 | increases tolerance to | <0.4% O₂ | 10.1128/mbio.01591-24 | “revRbr2 is specific to low O₂ tensions (<0.4%).” | **Strong, *C. difficile*-specific modifier.** (caulat2024physiologicalroleand pages 1-2) |
| FdpA | increases tolerance to | 0.4–1% O₂ | 10.1128/mbio.01591-24 | “FdpA [acts at] low and intermediate O₂ tensions (0.4%–1%).” | **Strong, taxon-specific.** In vivo electron-delivery partners remain unidentified. (caulat2024physiologicalroleand pages 1-2) |
| revRbr1 | increases survival under | 0.1–4% O₂ | 10.1128/mbio.01591-24 | “revRbr1 has a wider spectrum of activity (0.1%–4%).” | **Strong, taxon-specific.** At 4% O₂, deletion caused greater survival loss than wild type and complementation restored the phenotype. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) |
| FdpF | promotes survival under | >4% O₂ and air | 10.1128/mbio.01591-24 | “FdpF is more specific to tensions >4% and air”; Δ*fdpF* had a marked air-survival defect. | **Strong, taxon-specific.** This concerns survival rather than growth in air. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) |
| σB | promotes expression of | *fdpF* and *revrbr1* | 10.1128/mbio.01591-24 | Their expression is “strictly σB-dependent.” | **Strong in *C. difficile*.** Regulatory edges should carry strain and growth-state qualifiers. (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11) |
| σA and σB | promote expression of | *revrbr2* | 10.1128/mbio.01591-24 | “*revrbr2*…is expressed under the dual control of σA and σB.” | **Strong; condition-dependent.** Relative promoter importance differs between liquid culture and plates. (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11) |
| O₂ exposure | relieves repression by | OseR | 10.1128/mbio.01591-24 | OseR represses *fdpA*, *fdpF*, *revrbr1*, and *revrbr2* anaerobically; “O₂ exposure releases the repression.” | **Strong genetic-expression evidence, but direct O₂ sensing by OseR is unproven.** Curate O₂-dependent regulation, not direct ligand binding. (caulat2024physiologicalroleand pages 9-11) |
| Rex | represses | *fdpF* expression | 10.1128/mbio.01591-24 | “*fdpF* expression is repressed by Rex, a redox regulator that senses the NADH/NAD⁺ ratio.” | **Strong regulatory edge.** No Rex-dependent survival difference was observed under the tested long-term O₂ conditions. (caulat2024physiologicalroleand pages 13-15) |
| Cytochrome bd/CydAB | reduces | O₂ to water | 10.1128/jb.00389-22 | Heme d is the site “where oxygen binds and is reduced to water.” | **Strong biochemical edge.** (butler2023bacteroidesfragilismaintains pages 5-7) |
| Cytochrome bd | enables | nanaerobic respiration and growth | 10.1128/jb.00389-22 | *B. fragilis* “thrive[s] under…nanaerobic conditions using oxygen…via cytochrome bd.” | **Strong boundary-case edge**, not a cause of strict anaerobiosis. It reduces sensitivity at low O₂. (butler2023bacteroidesfragilismaintains pages 1-2) |
| Nanaerobic growth | increases | cytochrome bd activity | 10.1128/jb.00389-22 | O₂-dependent NADH consumption was approximately fivefold higher after nanaerobic growth. | **Strong biochemical result.** *cyd* transcription itself was similar under anoxic and nanaerobic conditions; do not infer transcriptional induction. (butler2023bacteroidesfragilismaintains pages 5-7) |
| SOD plus catalase activity | associates with increased | anammox O₂ tolerance | 10.1038/s43705-023-00251-7 | *Ca. Scalindua* had SOD 22.6 ± 1.9 and catalase 1.6 ± 0.7 U mg⁻¹ protein and higher O₂ tolerance. | **Comparative and taxon-specific; mark uncertain as a direct causal triple** because genetic perturbation was not the primary evidence. (okabe2023oxygentoleranceand pages 1-2) |

## 5. Recent developments and quantitative findings

### *Clostridioides difficile* oxygen-reduction network, 2024

Caulat and colleagues resolved four overlapping O₂-reduction modules rather than a single generic “antioxidant defense”: revRbr2 acts chiefly below 0.4% O₂, FdpA at 0.4–1%, revRbr1 across 0.1–4%, and FdpF above 4% and during air exposure. At 4% O₂ for 24 hours, the parental strain lost approximately three logs of survival; deleting *revrbr1* produced a significantly larger loss. Four hours in air also caused approximately a three-log survival loss in the parent, while Δ*fdpF* showed a stronger defect. These experiments establish concentration-specific survival functions while confirming that *C. difficile* still cannot grow in air. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7)

The same work identified a multilayer regulatory architecture: σB controls all four systems to varying degrees; σA supplies additional promoters for *fdpA* and *revrbr2*; OseR represses all four genes anaerobically and repression is relieved at 1% O₂; Rex links *fdpF* to NADH/NAD⁺ status. Direct molecular sensing by OseR remains unresolved. (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11)

### Nanaerobic respiration in *Bacteroides fragilis*, 2023

At 1,000–1,500 ppm O₂, *B. fragilis* retains both fumarate respiration and cytochrome-bd-dependent O₂ respiration. NQR and NDH2 supplied 77% and 23% of NADH:quinone oxidoreductase activity under nanaerobic conditions. Fumarate reductase remained synthesized and active, while cytochrome bd activity increased approximately fivefold despite little change in *cyd* promoter activity. This real-world gut adaptation shows that “strict anaerobe” can coexist with beneficial respiration at very low O₂. (butler2023bacteroidesfragilismaintains pages 5-7, butler2023bacteroidesfragilismaintains pages 1-2)

### Quantified oxygen sensitivity of anammox bacteria, 2023

Marine *Ca. Scalindua* exhibited an O₂ IC50 of 18.0 µM and upper activity limit of 51.6 µM, versus IC50 values of 2.7–4.2 µM and upper limits of 10.9–26.6 µM among freshwater anammox taxa. Inhibition remained reversible after 12–24 hours of air exposure. These are activity and recovery measurements, not evidence of aerobic growth, but they are useful quantitative modifiers for oxygen sensitivity. (okabe2023oxygentoleranceand pages 1-2)

### Mechanistic consensus

The 2021 authoritative review concludes that strict anaerobiosis is best explained by oxygen incompatibility with the biochemical strategies that maximize anaerobic performance—not by wholesale absence of antioxidant systems. Direct O₂ attack on radical enzymes, overoxidation of low-potential metal centers, and secondary ROS formation jointly create multiple metabolic bottlenecks. (lu2021whenanaerobesencounter pages 13-15)

## 6. Applications and real-world relevance

- **Anaerobe cultivation and diagnostics:** O₂ concentration, exposure duration, redox state, medium reducing capacity, and recovery under anoxia should be recorded. A binary aerobic/anaerobic incubation label can misclassify organisms capable of nanaerobic growth.
- **Gut microbiome biogeography:** epithelial O₂ gradients select for low-O₂ respiratory and detoxification systems. In *C. difficile*, reported gastrointestinal ranges extend from 0.1–0.4% in the colon lumen to 4–5% in the small intestine and near tissues. (caulat2024physiologicalroleand pages 1-2)
- **Pathogenesis and transmission:** Fdp/revRbr, Sor, and peroxidase systems help strict anaerobes survive inflammatory ROS and transient oxygen exposure without converting them into aerobic growers. (caulat2024physiologicalroleand pages 1-2, lotoux2025defensearsenalof pages 1-2)
- **Anammox wastewater and nitrogen-loss models:** genus-specific IC50 and upper dissolved-O₂ limits are more informative than assigning one oxygen threshold to all anammox organisms. (okabe2023oxygentoleranceand pages 1-2)
- **Live biotherapeutic manufacturing:** protective formulation, oxygen-impermeable processing, and rapid recovery assays should target viability separately from growth. Nanaerobic respiration and sporulation require separate design considerations.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not curate “strict anaerobes lack SOD and catalase.”** It is obsolete as a universal mechanism; many possess SOD/catalase or functionally analogous reductases and peroxidases. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 13-15)
2. **Do not equate oxygen exposure with death.** Growth arrest, enzyme inhibition, viability loss, and failure to recover are distinct endpoints.
3. **Do not use a universal O₂ cutoff.** Relevant thresholds range from nanomolar/low-micromolar levels to several percent and depend on taxon and assay.
4. **Do not curate cytochrome bd, Fdp, revRbr, SOD, or catalase as causes of strict anaerobiosis.** They generally oppose oxygen sensitivity and should be modeled as tolerance modifiers.
5. **Do not generalize the *B. thetaiotaomicron* PFOR result to every PFOR.** Oxygen-tolerant PFOR variants exist. (khademian2020doreactiveoxygen pages 9-10)
6. **Do not assert that OseR directly binds or senses O₂.** The 2024 data establish O₂-dependent derepression, while direct sensing remains hypothetical. (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11)
7. **Do not treat antioxidant-gene presence as sufficient phenotype prediction.** Expression, enzyme activity, electron donors, repair capacity, O₂ flux, and vulnerable metabolic dependencies determine the phenotype.
8. **Do not merge spores with vegetative cells.** Oxygen-resistant spores can belong to organisms whose vegetative cells are strictly anaerobic.
9. **The 2025 *C. difficile* ROS study is corroborative, not within the requested 2023–2024 priority window.** It supports Sor, Rbr, Bcp, RevRbr2, and FdpF roles but should be clearly date-labeled if incorporated. (lotoux2025defensearsenalof pages 1-2)

## 8. DOI-first bibliography

1. **Caulat LC et al.** “Physiological role and complex regulation of O₂-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.” *mBio* 15 (published **27 August 2024**; issue October 2024). DOI: [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24). (caulat2024physiologicalroleand pages 1-2)
2. **Butler NL et al.** “*Bacteroides fragilis* Maintains Concurrent Capability for Anaerobic and Nanaerobic Respiration.” *Journal of Bacteriology* 205 (published **7 December 2022**; issue January 2023). DOI: [10.1128/jb.00389-22](https://doi.org/10.1128/jb.00389-22). (butler2023bacteroidesfragilismaintains pages 1-2)
3. **Okabe S et al.** “Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing bacteria.” *ISME Communications* 3 (published **May 2023**). DOI: [10.1038/s43705-023-00251-7](https://doi.org/10.1038/s43705-023-00251-7). (okabe2023oxygentoleranceand pages 1-2)
4. **Khademian M, Imlay JA.** “Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? The case of *Bacteroides thetaiotaomicron*.” *Molecular Microbiology* 114 (accepted **7 April 2020**). DOI: [10.1111/mmi.14516](https://doi.org/10.1111/mmi.14516). (khademian2020doreactiveoxygen pages 1-2)
5. **Lu Z, Imlay JA.** “When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.” *Nature Reviews Microbiology* 19, 774–785 (published **June 2021**). DOI: [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y). (lu2021whenanaerobesencounter pages 8-9)
6. **Lu Z, Sethu R, Imlay JA.** “Endogenous superoxide is a key effector of the oxygen sensitivity of a model obligate anaerobe.” *PNAS* 115, E3266–E3275 (published **March 2018**). DOI: [10.1073/pnas.1800120115](https://doi.org/10.1073/pnas.1800120115). (lu2021whenanaerobesencounter pages 9-11)
7. **Lotoux A et al.** “Defense arsenal of the strict anaerobe *Clostridioides difficile* against reactive oxygen species encountered during its infection cycle.” *mBio* 16 (published **20 March 2025**; post-window corroboration). DOI: [10.1128/mbio.03753-24](https://doi.org/10.1128/mbio.03753-24). (lotoux2025defensearsenalof pages 1-2)

## 9. Recommended minimum YAML graph

For a compact initial graph, prioritize these seven edges:

1. O₂ → **directly inactivates** → PFL  
2. O₂ → **directly inactivates** → PFOR  
3. Aeration → **increases production of** → endogenous superoxide  
4. Superoxide → **inactivates** → fumarase/[4Fe–4S] dehydratases  
5. PFL/PFOR inactivation → **blocks** → pyruvate dissimilation  
6. Fumarase/Fe–S-enzyme inactivation → **disrupts** → central metabolism and biosynthesis  
7. Combined metabolic disruption → **causes** → oxygen-dependent vegetative-growth arrest (`METPO:1000611`)

Attach *B. thetaiotaomicron* as the primary taxonomic evidence context. Add Fdp/revRbr, cytochrome bd, and SOD/catalase branches as taxon-qualified **negative modifiers of oxygen sensitivity**, rather than expanding the core mechanism into an unsupported universal model.

References

1. (khademian2020doreactiveoxygen pages 1-2): Maryam Khademian and James A. Imlay. Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? the case of <i>bacteroides thetaiotaomicron</i>. May 2020. URL: https://doi.org/10.1111/mmi.14516, doi:10.1111/mmi.14516. This article has 42 citations and is from a domain leading peer-reviewed journal.

2. (lu2021whenanaerobesencounter pages 22-27): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

3. (lu2021whenanaerobesencounter pages 13-15): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

4. (butler2023bacteroidesfragilismaintains pages 1-2): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

5. (caulat2024physiologicalroleand pages 5-7): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

7. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

8. (lu2021whenanaerobesencounter pages 9-11): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

9. (khademian2020doreactiveoxygen pages 9-10): Maryam Khademian and James A. Imlay. Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? the case of <i>bacteroides thetaiotaomicron</i>. May 2020. URL: https://doi.org/10.1111/mmi.14516, doi:10.1111/mmi.14516. This article has 42 citations and is from a domain leading peer-reviewed journal.

10. (butler2023bacteroidesfragilismaintains pages 5-7): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

11. (okabe2023oxygentoleranceand pages 11-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

12. (lu2021whenanaerobesencounter pages 4-6): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

13. (lu2021whenanaerobesencounter pages 11-13): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

14. (caulat2024physiologicalroleand pages 13-15): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (caulat2024physiologicalroleand pages 9-11): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (lotoux2025defensearsenalof pages 1-2): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

17. (lu2021whenanaerobesencounter pages 8-9): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.