---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:15:42.368006'
end_time: '2026-06-17T21:46:21.436032'
duration_seconds: 1839.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: anaerobic
  trait_identifier: METPO:1000603
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which growth occurs in the absence of molecular\
    \ oxygen (O\u2082)."
  parent_traits: METPO:1000601
  synonyms: Ox_anaerobic, anaerobe
  evidence_summary: 'PMID:21413255: Anaerobes, on the other hand, cannot grow in the
    presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.)
    | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides
    fragilis is described as an anaerobic organism.)'
  causal_graph_summary: 'anaerobic_trait_oxygen_exclusion: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anaerobic
- **METPO identifier:** METPO:1000603
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the absence of molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_anaerobic, anaerobe
- **Existing evidence:** PMID:21413255: Anaerobes, on the other hand, cannot grow in the presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an anaerobic organism.)
- **Existing causal graph summary:** anaerobic_trait_oxygen_exclusion: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/anaerobic.yaml`.

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
- **Trait label:** anaerobic
- **METPO identifier:** METPO:1000603
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the absence of molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_anaerobic, anaerobe
- **Existing evidence:** PMID:21413255: Anaerobes, on the other hand, cannot grow in the presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an anaerobic organism.)
- **Existing causal graph summary:** anaerobic_trait_oxygen_exclusion: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/anaerobic.yaml`.

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


## Microbial trait causal graph curation report: **anaerobic** (METPO:1000603)

### 1) Scope summary (trait meaning, boundaries, and current understanding)

**Trait definition (curation-ready):** The METPO:1000603 trait “anaerobic” is most directly operationalized as the capacity for **growth when molecular oxygen (O2) is absent**, with “obligate anaerobes” characterized by the stronger constraint that **O2 blocks growth**. A recent mechanistic study on gut commensal *Faecalibacterium* states explicitly: “**The defining trait of obligate anaerobes is that O2 blocks their growth**.” (botin2023thetoleranceof pages 1-2)

**Boundary cases / nearby traits (do not over-interpret without further sources):**
- Many microbes labeled “strict/obligate anaerobes” still encounter **physiological low-O2 niches** in vivo (especially in animal-associated ecosystems), requiring oxygen stress management rather than absolute exclusion. For example, *Clostridioides difficile* (described as a strict anaerobe) is exposed to a **longitudinal gut O2 gradient** of ~4–5% in the small intestine down to ~0.1–0.4% in the colon lumen, plus a **lateral gradient** increasing toward mucus (1–2%) and tissue (~5%). (caulat2024physiologicalroleand pages 1-2)
- Even within obligate anaerobe taxa, **strain-dependent oxygen tolerance** occurs (e.g., faecalibacteria differ in oxygen sensitivity, and mechanisms may allow limited growth under low O2). (botin2023thetoleranceof pages 1-2)
- Classification terms like “facultative anaerobe,” “aerotolerant anaerobe,” and “microaerophile” are not explicitly defined in the retrieved full text excerpts; treat these distinctions as **out-of-scope for curation** unless additional definitional sources are added. (okabe2023oxygentoleranceand pages 12-12)

**Mechanistic framing for the trait graph:** Anaerobic growth can be supported by (i) **fermentation** (redox balancing without external electron acceptors) and/or (ii) **anaerobic respiration** that uses **alternative terminal electron acceptors** (TEAs) via respiratory reductases. Recent gut-focused work emphasizes that “respiratory reductases enable microbes to utilize molecules present in anaerobic ecosystems as energy-generating respiratory electron acceptors.” (little2024dietaryandhostderived pages 31-33)

### 2) Candidate causal-graph nodes (grouped by type)

Below are candidate nodes supported by recent evidence; some are generic and others are taxon-anchored exemplars.

#### A. Environmental / experimental factors
- **Anoxia / low oxygen tension** (label-only; consider ENVO terms for anoxic environments)
- **Gastrointestinal O2 gradients** (longitudinal and lateral gradients) (caulat2024physiologicalroleand pages 1-2)
- **Anaerobic chamber / anaerobic incubation** (assay condition) (kim2024anaerobicrespirationof pages 13-15)

#### B. Chemicals / redox species
- **Molecular oxygen**: O2 (CHEBI:15379) (okabe2023oxygentoleranceand pages 2-3)
- **Reactive oxygen species (ROS)** (label-only), including:
  - superoxide (O2•−) (label-only) (okabe2023oxygentoleranceand pages 2-3)
  - hydrogen peroxide (H2O2) (label-only) (okabe2023oxygentoleranceand pages 2-3)
  - hydroxyl radical (•OH) (label-only) (okabe2023oxygentoleranceand pages 2-3)
- **Methionine sulfoxide** (CHEBI:32367) as a TEA in a host-associated niche (kim2024anaerobicrespirationof pages 1-3)
- **Cysteine** (CHEBI:15356) as an extracellular ROS-modulating factor in an obligate anaerobe (botin2023thetoleranceof pages 1-2)

#### C. Enzymes / complexes (detoxification and anaerobic respiration)
- **Superoxide dismutase (Sod)** (EC:1.15.1.1) (okabe2023oxygentoleranceand pages 2-3)
- **Catalase (Cat)** (EC:1.11.1.6; label-only) (okabe2023oxygentoleranceand pages 2-3)
- **Peroxidases** (label-only; includes cytochrome c peroxidase etc.) (okabe2023oxygentoleranceand pages 11-12)
- **Flavodiiron proteins (FdpA/FdpF)** (taxon-specific exemplars in *C. difficile*) (caulat2024physiologicalroleand pages 1-2)
- **Reverse rubrerythrins (revRbr1/revRbr2)** (taxon-specific exemplars in *C. difficile*) (caulat2024physiologicalroleand pages 1-2)
- **DmsABC** (molybdenum cofactor-containing complex reducing methionine sulfoxide in *Salmonella*) (kim2024anaerobicrespirationof pages 1-3)

#### D. Regulators / signaling
- **Rex** (redox regulator sensing NADH/NAD+) regulating fdpF (taxon-specific exemplar) (caulat2024physiologicalroleand pages 1-2)
- **Spx-family regulator** inducing O2-response genes (taxon-specific exemplar) (caulat2024physiologicalroleand pages 1-2)
- **ArcAB two-component system** repressing aerobic respiration (facultative anaerobe regulatory module; boundary-related) (caulat2024physiologicalroleand pages 1-2)

### 3) Evidence-backed candidate causal edges (triples)

The following table is designed for direct curation into a TraitMech-style YAML after additional grounding work (where needed). It includes subject–predicate–object triples, quotes/snippets, DOI-first references, curation notes, and suggested CURIEs.

| Subject (node) | Predicate | Object (node) | Evidence (short quote) | Reference (DOI, year, URL) | Notes/curation flags | Suggested ontology grounding (CURIEs when available) |
|---|---|---|---|---|---|---|
| molecular oxygen (O2) | causes | reactive oxygen species (ROS) | “molecular oxygen diffusion produces ROS (superoxide O2•−, H2O2) and secondary hydroxyl radicals (•OH)” (okabe2023oxygentoleranceand pages 2-3) | Okabe et al. 2023; doi:10.1038/s43705-023-00251-7; https://doi.org/10.1038/s43705-023-00251-7 | Broad mechanism across anaerobes; strong background edge | CHEBI:15379; label:reactive oxygen species |
| molecular oxygen (O2) | inhibits growth of | obligate anaerobe | “The defining trait of obligate anaerobes is that O2 blocks their growth” (botin2023thetoleranceof pages 1-2) | Botin et al. 2023; doi:10.1128/AEM.00606-23; https://doi.org/10.1128/AEM.00606-23 | Core phenotype-defining edge for trait scope | CHEBI:15379; METPO:1000603 |
| gastrointestinal tract oxygen gradient | determines exposure of | Clostridioides difficile to low O2 tensions | “a longitudinal gradient ranging from 4% to 5% in the small intestine… to 0.1% to 0.4% in the lumen of the colon” and lateral gradient “toward the mucus (1%–2%) and the tissues (5%)” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Environmental-context edge; taxon/example-specific | ENVO:00002036; NCBITaxon:1496 |
| revRbr2 | protects against | low O2 tension | “revRbr2 is specific to low O2 tensions (<0.4%)” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Taxon-specific to C. difficile; good mechanistic edge | label:reverse rubrerythrin revRbr2; NCBITaxon:1496 |
| FdpA | protects against | low/intermediate O2 tension | “FdpA [acts at] low and intermediate O2 tensions (0.4%–1%)” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Taxon-specific; could curate as enzyme-mediated O2 tolerance | label:flavodiiron protein FdpA; NCBITaxon:1496 |
| revRbr1 | protects against | broad O2 tension range | “revRbr1 has a wider spectrum of activity (0.1%–4%)” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Taxon-specific; complements oxygen-exclusion graph | label:reverse rubrerythrin revRbr1; NCBITaxon:1496 |
| FdpF | protects against | high O2 tension and air exposure | “FdpF is more specific to tensions > 4% and air” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Taxon-specific; unusual for obligate anaerobe; may support tolerance not trait definition | label:flavodiiron protein FdpF; NCBITaxon:1496 |
| Rex | regulates expression of | fdpF | “fdpF is regulated by Rex, a regulator sensing the NADH/NAD+ ratio” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Strong regulatory edge; taxon-specific | label:Rex regulator; label:fdpF gene |
| Spx-family regulator | positively regulates induction of | fdp and revRbr genes upon O2 exposure | “We also identified a regulator of the Spx family that plays a role in the induction of fdp and revrbr genes upon O2 exposure” (caulat2024physiologicalroleand pages 1-2) | Caulat et al. 2024; doi:10.1128/mbio.01591-24; https://doi.org/10.1128/mbio.01591-24 | Strong but taxon-specific; exact locus identity may need follow-up | label:Spx-family regulator; label:fdp/revRbr genes |
| superoxide dismutase activity | positively correlates with | oxygen tolerance in anammox bacteria | “only Scalindua exhibited high Sod activity… This Sod-Cat dependent detoxification system could be responsible for the higher O2 tolerance” (okabe2023oxygentoleranceand pages 12-12) | Okabe et al. 2023; doi:10.1038/s43705-023-00251-7; https://doi.org/10.1038/s43705-023-00251-7 | Correlative rather than universal causation; uncertain/generalized | EC:1.15.1.1; label:anammox bacteria |
| superoxide dismutase and catalase and peroxidases | detoxify | ROS | “organisms use anti-oxidative enzymes—superoxide dismutase (Sod), catalase (Cat), and peroxidases—to detoxify ROS” (okabe2023oxygentoleranceand pages 2-3) | Okabe et al. 2023; doi:10.1038/s43705-023-00251-7; https://doi.org/10.1038/s43705-023-00251-7 | Broad detoxification edge; acceptable generic mechanism | EC:1.15.1.1; EC:1.11.1.6; GO:0006979 |
| methionine sulfoxide | serves as terminal electron acceptor for | Salmonella anaerobic respiration via DmsABC | “methionine sulfoxide… serves as a vital terminal electron acceptor” and “Salmonella… use a molybdenum cofactor-containing DmsABC complex to reduce host-derived methionine sulfoxide” (kim2024anaerobicrespirationof pages 1-3) | Kim et al. 2024; doi:10.1016/j.chom.2024.01.004; https://doi.org/10.1016/j.chom.2024.01.004 | Strong mechanistic edge; taxon- and niche-specific | CHEBI:32367; label:DmsABC complex; NCBITaxon:28901 |
| scarcity of terminal electron acceptors | limits growth of | intracellular Salmonella | “scarcity of terminal electron acceptors limits growth of intracellular Salmonella” (kim2024anaerobicrespirationof pages 13-15) | Kim et al. 2024; doi:10.1016/j.chom.2024.01.004; https://doi.org/10.1016/j.chom.2024.01.004 | Strong context edge for respiratory limitation under low O2 | label:terminal electron acceptor; NCBITaxon:28901 |
| cysteine | protects | Faecalibacterium longum L2-6 from oxidative stress | “cysteine… limited the production of extracellular O2•− and improved the survival of Faecalibacterium longum L2-6 under high O2 tension” (botin2023thetoleranceof pages 1-2) | Botin et al. 2023; doi:10.1128/AEM.00606-23; https://doi.org/10.1128/AEM.00606-23 | Strain-specific; useful but uncertain for broad curation | CHEBI:15356; NCBITaxon:Faecalibacterium |
| respiratory reductases | enable utilization of | alternative anaerobic electron acceptors | “Respiratory reductases enable microbes to utilize molecules present in anaerobic ecosystems as energy-generating respiratory electron acceptors” (little2024dietaryandhostderived pages 31-33) | Little et al. 2024; doi:10.1038/s41564-023-01560-2; https://doi.org/10.1038/s41564-023-01560-2 | General statement; specific reductase-substrate pairs still needed | label:respiratory reductase; label:terminal electron acceptor |
| ArcAB two-component system | represses | aerobic respiration | “ArcAB, a two-component regulatory system that represses aerobic respiration, is a key mediator of metabolic adaptation” (caulat2024physiologicalroleand pages 1-2) | Brown et al. 2023; doi:10.1128/mbio.01448-23; https://doi.org/10.1128/mbio.01448-23 | Strong regulatory edge but from facultative anaerobes; boundary-case relevance | label:ArcAB two-component system |
| anaerobic chamber and anaerobic incubation | provides assay condition for | anaerobic growth measurements | “cells grown ‘in a Bactron anaerobic chamber’ and incubated ‘anaerobically or aerobically at 37°C’” (kim2024anaerobicrespirationof pages 13-15) | Kim et al. 2024; doi:10.1016/j.chom.2024.01.004; https://doi.org/10.1016/j.chom.2024.01.004 | Experimental factor only; useful assay node not organismal mechanism | ENVO:01001864; label:anaerobic incubation |


*Table: This table lists candidate causal edges for curating the anaerobic trait graph, with concise evidence, references, curation notes, and suggested ontology grounding. It focuses on oxygen exclusion, ROS stress, detoxification, regulatory systems, alternative electron acceptors, and assay-context edges supported by the retrieved sources.*

**Visual evidence supporting a curated submodule (O2 detox / O2-reducing enzymes in an obligate anaerobe):** Caulat et al. provide a summarized model (Figure 8) showing the **O2-tension ranges** at which distinct O2-reducing enzymes protect *C. difficile* vegetative cells and an integrated regulatory model; this is useful to curate a taxon-anchored “oxygen tolerance under anaerobiosis” subgraph. (caulat2024physiologicalroleand media 03c93b07)

### 4) Recent developments (2023–2024 prioritized)

#### 4.1 Quantitative oxygen tolerance in anammox bacteria (2023)
A 2023 ISME Communications study quantified oxygen inhibition kinetics in anaerobic ammonium-oxidizing (anammox) bacteria and reported **species-level differences** in oxygen tolerance, linking them to detox enzyme activity profiles. The study describes that ROS arise when O2 is reduced and outlines canonical detox enzymes (Sod/Cat/peroxidases) for ROS removal. (okabe2023oxygentoleranceand pages 2-3)

Quantitative measurements included:
- Headspace O2 range **0–3.5% (v/v)** corresponding to dissolved oxygen (DO) **~0–65 µM at 25°C** (and ~0–53 µM at 37°C) in their calibrated setup. (okabe2023oxygentoleranceand pages 2-3)
- Example O2-reduction rates: ~**0.26 µmol O2/g-protein/h** (for “Ca. Scalindua sp.” and “Ca. Brocadia sinica”) vs ~**0.53 µmol O2/g-protein/h** (for “Ca. K. stuttgartiensis”). (okabe2023oxygentoleranceand pages 11-12)
These quantitative values can support curation of “O2 inhibits anaerobic metabolism” edges in a context-specific manner (but should not be generalized to all anaerobes without additional sources). (okabe2023oxygentoleranceand pages 11-12)

#### 4.2 Multi-enzyme O2 tolerance modules in an obligate anaerobe pathogen (2024)
A 2024 mBio paper on *Clostridioides difficile* (strict anaerobe) provides a strongly mechanistic decomposition of O2 tolerance into multiple O2-reducing enzymes with **distinct functional ranges** (e.g., revRbr2 <0.4% O2, FdpA 0.4–1%, revRbr1 0.1–4%, FdpF >4% and air) and links this to **multi-layer regulation** (σ factors, Spx family regulator, Rex sensing NADH/NAD+). (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media 03c93b07)

This supports curating a “**physiological oxygen exposure → induction of O2-reducing enzymes → improved survival/growth under low O2**” subgraph, while clearly labeling it as a **taxon-specific mechanistic module**. (caulat2024physiologicalroleand pages 1-2)

#### 4.3 Host-derived terminal electron acceptors enabling anaerobic respiration during infection (2024)
A 2024 Cell Host & Microbe study demonstrates that intracellular *Salmonella* can exploit **host-derived methionine sulfoxide** (generated by the phagocyte NADPH oxidase) as a **terminal electron acceptor** for anaerobic respiration via a molybdenum cofactor-containing DmsABC complex. (kim2024anaerobicrespirationof pages 1-3)

This is a contemporary example of how “anaerobic” growth can depend not only on oxygen absence, but on **availability of non-O2 electron acceptors** in the niche; it is also a clear infection-relevant mechanism for a candidate graph branch (“host oxidative burst → methionine sulfoxide generation → Salmonella anaerobic respiration”). (kim2024anaerobicrespirationof pages 1-3)

### 5) Current applications and real-world implementations

#### 5.1 Anaerobic processing in fecal microbiota transplantation (FMT) (2023)
A 2023 *Microorganisms* study evaluated donor-stool processing methods and reports that **aerobic (oxygen-exposed) processing adversely affects the number and composition of viable bacteria**, motivating anaerobic handling for clinical FMT manufacturing. (benard2023anaerobicfecesprocessing pages 11-13)

Key implementation-relevant outcomes:
- In strict anaerobic culturing, total CFU were higher under anaerobic processing (median **10.31 vs 10.16 log CFU/g**, p<0.001). (benard2023anaerobicfecesprocessing pages 6-7)
- The authors conclude that “**anaerobic processing of donor stool… should be applied for clinical use**” to retain obligate anaerobes and butyrate-producing taxa linked to response in ulcerative colitis, and note that clinical trials (including ongoing RCTs) are evaluating this approach. (benard2023anaerobicfecesprocessing pages 11-13, benard2023anaerobicfecesprocessing pages 1-2)

This is a direct example where the anaerobic trait affects **biobanking/processing SOPs** and downstream therapeutic performance, making it especially relevant for curation under “ENVIRONMENT” trait category. (benard2023anaerobicfecesprocessing pages 6-7)

#### 5.2 High-throughput phenotyping under strict anaerobic conditions (2024)
A 2024 Nature Protocols article describes high-throughput screening of drug effects on gut bacteria and emphasizes the need to modify standard growth assays because phenotypic analysis “must be performed under anaerobic conditions.” (muller2024highthroughputanaerobicscreening pages 1-2)

### 6) Expert analysis and curation guidance (what is safe to curate now vs. later)

**Curate now (high-confidence, generalizable edges):**
- **O2 → ROS formation** and ROS species list, as a universal physicochemical mechanism that creates selective pressure against oxygen exposure in anaerobes. (okabe2023oxygentoleranceand pages 2-3)
- **O2 blocks growth of obligate anaerobes** (definition-level; use to anchor trait semantics). (botin2023thetoleranceof pages 1-2)
- **ROS detox enzymes (Sod/Cat/peroxidases) → ROS detoxification**, with explicit statement of these enzyme classes detoxifying ROS. (okabe2023oxygentoleranceand pages 2-3)

**Curate with explicit taxon scoping (good mechanistic exemplars):**
- The *C. difficile* O2 tolerance module (Fdp/revRbr enzymes and their regulation) is mechanistically rich and supported by a figure summarizing functional ranges, but should be curated as either (i) a taxon-anchored subgraph or (ii) a generic “O2-reducing enzymes” module annotated as “e.g., *C. difficile*.” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media 03c93b07)
- Methionine sulfoxide as a terminal electron acceptor is compelling and mechanistically explicit, but should be curated as **host-associated, pathogen-specific** (intracellular *Salmonella* in oxidative-burst context) rather than a universal anaerobic-growth mechanism. (kim2024anaerobicrespirationof pages 1-3)

**Do not curate yet (needs stronger definitional sources or direct evidence):**
- Formal categorical boundaries for “facultative anaerobe,” “aerotolerant anaerobe,” and “microaerophile” (explicit definitions were not retrieved in accessible excerpts). (okabe2023oxygentoleranceand pages 12-12)
- Broad claims about all possible terminal electron acceptors in anaerobic respiration (the Nature Microbiology paper’s provided excerpt was primarily references; curate TEA edges only when specific reductase–substrate pairs are directly described in-text or experimentally supported). (little2024dietaryandhostderived pages 31-33)

### 7) DOI-first bibliography (with publication dates and URLs)

1. Botin T, et al. **The Tolerance of Gut Commensal *Faecalibacterium* to Oxidative Stress Is Strain Dependent and Relies on Detoxifying Enzymes.** *Applied and Environmental Microbiology*. **Published Jul 2023**. DOI: **10.1128/aem.00606-23**. https://doi.org/10.1128/aem.00606-23 (botin2023thetoleranceof pages 1-2)

2. Okabe S, et al. **Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria.** *ISME Communications*. **Published May 2023**. DOI: **10.1038/s43705-023-00251-7**. https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 2-3, okabe2023oxygentoleranceand pages 11-12)

3. Kim J-S, et al. **Anaerobic respiration of host-derived methionine sulfoxide protects intracellular Salmonella from the phagocyte NADPH oxidase.** *Cell Host & Microbe*. **Published Mar 2024**. DOI: **10.1016/j.chom.2024.01.004**. https://doi.org/10.1016/j.chom.2024.01.004 (kim2024anaerobicrespirationof pages 1-3)

4. Caulat LC, et al. **Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.** *mBio*. **Published Oct 2024**. DOI: **10.1128/mbio.01591-24**. https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media 03c93b07)

5. Little AS, et al. **Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration.** *Nature Microbiology*. **Published Nov 2024**. DOI: **10.1038/s41564-023-01560-2**. https://doi.org/10.1038/s41564-023-01560-2 (little2024dietaryandhostderived pages 31-33)

6. Brown AN, et al. **Conserved metabolic regulator ArcA responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia.** *mBio*. **Published Oct 2023**. DOI: **10.1128/mbio.01448-23**. https://doi.org/10.1128/mbio.01448-23 (caulat2024physiologicalroleand pages 1-2)

7. Bénard MV, et al. **Anaerobic Feces Processing for Fecal Microbiota Transplantation Improves Viability of Obligate Anaerobes.** *Microorganisms*. **Published Sep 2023**. DOI: **10.3390/microorganisms11092238**. https://doi.org/10.3390/microorganisms11092238 (benard2023anaerobicfecesprocessing pages 6-7, benard2023anaerobicfecesprocessing pages 11-13, benard2023anaerobicfecesprocessing pages 1-2)

8. Müller P, et al. **High-throughput anaerobic screening for identifying compounds acting against gut bacteria in monocultures or communities.** *Nature Protocols*. **Volume 19, Issue 3 (2024)**. DOI: **10.1038/s41596-023-00926-4**. https://doi.org/10.1038/s41596-023-00926-4 (muller2024highthroughputanaerobicscreening pages 1-2)


References

1. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 19 citations and is from a peer-reviewed journal.

2. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

3. (okabe2023oxygentoleranceand pages 12-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

4. (little2024dietaryandhostderived pages 31-33): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 76 citations and is from a highest quality peer-reviewed journal.

5. (kim2024anaerobicrespirationof pages 13-15): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (okabe2023oxygentoleranceand pages 2-3): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

7. (kim2024anaerobicrespirationof pages 1-3): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (okabe2023oxygentoleranceand pages 11-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

9. (caulat2024physiologicalroleand media 03c93b07): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (benard2023anaerobicfecesprocessing pages 11-13): Mèlanie V. Bénard, Iñaki Arretxe, Koen Wortelboer, Hermie J. M. Harmsen, Mark Davids, Clara M. A. de Bruijn, Marc A. Benninga, Floor Hugenholtz, Hilde Herrema, and Cyriel Y. Ponsioen. Anaerobic feces processing for fecal microbiota transplantation improves viability of obligate anaerobes. Microorganisms, 11:2238, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092238, doi:10.3390/microorganisms11092238. This article has 31 citations.

11. (benard2023anaerobicfecesprocessing pages 6-7): Mèlanie V. Bénard, Iñaki Arretxe, Koen Wortelboer, Hermie J. M. Harmsen, Mark Davids, Clara M. A. de Bruijn, Marc A. Benninga, Floor Hugenholtz, Hilde Herrema, and Cyriel Y. Ponsioen. Anaerobic feces processing for fecal microbiota transplantation improves viability of obligate anaerobes. Microorganisms, 11:2238, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092238, doi:10.3390/microorganisms11092238. This article has 31 citations.

12. (benard2023anaerobicfecesprocessing pages 1-2): Mèlanie V. Bénard, Iñaki Arretxe, Koen Wortelboer, Hermie J. M. Harmsen, Mark Davids, Clara M. A. de Bruijn, Marc A. Benninga, Floor Hugenholtz, Hilde Herrema, and Cyriel Y. Ponsioen. Anaerobic feces processing for fecal microbiota transplantation improves viability of obligate anaerobes. Microorganisms, 11:2238, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092238, doi:10.3390/microorganisms11092238. This article has 31 citations.

13. (muller2024highthroughputanaerobicscreening pages 1-2): Patrick Müller, Jacobo de la Cuesta-Zuluaga, Michael Kuhn, Maral Baghai Arassi, Tim Treis, Sonja Blasche, Michael Zimmermann, Peer Bork, Kiran Raosaheb Patil, Athanasios Typas, Sarela Garcia-Santamarina, and Lisa Maier. High-throughput anaerobic screening for identifying compounds acting against gut bacteria in monocultures or communities. Nature protocols, 19:668-699, Dec 2024. URL: https://doi.org/10.1038/s41596-023-00926-4, doi:10.1038/s41596-023-00926-4. This article has 38 citations and is from a peer-reviewed journal.