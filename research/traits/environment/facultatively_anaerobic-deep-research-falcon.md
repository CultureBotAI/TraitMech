---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:42:49.186600'
end_time: '2026-08-04T00:50:47.041527'
duration_seconds: 477.85
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively anaerobic
  trait_identifier: METPO:1000605
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which growth can occur with or without molecular\
    \ oxygen (O\u2082)."
  parent_traits: METPO:1000601
  synonyms: facultative, facultative anaerobe
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the
    presence or absence of oxygen (Supports facultative anaerobiosis as growth under
    oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is
    a facultative anaerobe (Organism example: Escherichia coli is described as facultatively
    anaerobic.)'
  causal_graph_summary: 'facultative_anaerobe_oxygen_switch: 8 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000605
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur with or without molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the presence or absence of oxygen (Supports facultative anaerobiosis as growth under oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is a facultative anaerobe (Organism example: Escherichia coli is described as facultatively anaerobic.)
- **Existing causal graph summary:** facultative_anaerobe_oxygen_switch: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **facultatively anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_anaerobic.yaml`.

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
- **Trait label:** facultatively anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000605
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur with or without molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the presence or absence of oxygen (Supports facultative anaerobiosis as growth under oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is a facultative anaerobe (Organism example: Escherichia coli is described as facultatively anaerobic.)
- **Existing causal graph summary:** facultative_anaerobe_oxygen_switch: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **facultatively anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_anaerobic.yaml`.

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


# Curation report: facultatively anaerobic

## 1. Scope summary

**Target:** `METPO:1000605` — **facultatively anaerobic**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Definition:** growth can occur both with and without molecular oxygen (O₂).

The trait is a **growth phenotype/capacity**, not a single pathway. A positive assignment requires reproducible growth under both oxic and anoxic conditions. Under oxic conditions, many facultative anaerobes use O₂ respiration; under anoxia they may use alternative-electron-acceptor respiration, fermentation, or both. Thus, nitrate respiration is neither necessary nor sufficient by itself, and “survives oxygen exposure” is weaker than “grows with oxygen.” Facultative anaerobes differ from strict aerobes, which require O₂; strict anaerobes, whose growth is inhibited by O₂; and aerotolerant anaerobes, which tolerate O₂ but characteristically retain anaerobic energy metabolism. A 2021 expert review uses this growth-based distinction and reports that facultative anaerobes represented 8 of 12 organisms on the cited WHO antibiotic-resistant priority-pathogen list. (andre2021theselectiveadvantage pages 1-2)

The most defensible graph is therefore a **taxon-qualified E. coli/Enterobacterales mechanism** explaining metabolic switching, not a universal molecular definition. FNR, ArcBA, NarXL, electron-acceptor repertoires, terminal oxidases, and fermentation products vary substantially among taxa. Reviews explicitly caution that respiratory regulatory systems outside E. coli remain incompletely characterized. (price2021bacterialapproachesto pages 11-12)

## 2. Recommended graph architecture

Use `METPO:1000605` as the terminal phenotype node and represent two experimentally demonstrated branches:

1. **O₂ available → aerobic respiratory growth**.
2. **O₂ absent → anaerobic growth**, supported by either:
   - alternative-acceptor respiration, or
   - fermentation/redox balancing when suitable external acceptors are unavailable.

For the existing eight-node graph, the highest-value expansion is an E. coli-centered regulatory layer comprising **FNR**, **ArcB–ArcA**, **NarX–NarL**, the **quinone redox pool**, and explicit separation of **anaerobic respiration** from **fermentation**.

## 3. Candidate nodes grouped by type

### Trait and assay states

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| facultatively anaerobic | trait | `METPO:1000605` | Preserve identifier verbatim. |
| oxygen preference | parent trait | `METPO:1000601` | Supplied parent. |
| growth in presence of O₂ | assay phenotype | Label only | Must denote growth, not survival. |
| growth in absence of O₂ | assay phenotype | Label only | Record medium, acceptors, redox conditions, and duration. |
| anoxia / oxygen limitation | environmental state | ENVO candidate; verify locally | Do not equate microaerobiosis with complete anoxia. |

### Chemicals and electron acceptors

| Node | Suggested grounding | Role |
|---|---|---|
| molecular oxygen | `CHEBI:15379` | Terminal electron acceptor in aerobic respiration; also the direct signal that destroys active FNR’s anaerobic Fe–S state. |
| nitrate | `CHEBI:17632` | Alternative terminal acceptor and NarX/NarL signal in E. coli-like systems. |
| nitrite | `CHEBI:16301` | Related Nar-system signal/intermediate; effects differ between NarX/NarQ. |
| fumarate | `CHEBI:18012` | Alternative acceptor through fumarate reductase in applicable taxa. |
| dimethyl sulfoxide | `CHEBI:28262` | Alternative acceptor through DMSO reductase in applicable taxa. |
| trimethylamine N-oxide | CHEBI candidate; verify | Alternative acceptor; taxon-specific. |
| ubiquinone, menaquinone, demethylmenaquinone pools | CHEBI candidates; verify species | Electron carriers whose oxidation state modulates ArcB; avoid collapsing them into one chemically identical node. |
| [4Fe–4S] cluster | CHEBI candidate; verify exact oxidation state | Cofactor supporting active, dimeric FNR under anoxia. |
| [2Fe–2S] cluster | CHEBI candidate; verify exact oxidation state | O₂-induced FNR conversion product associated with inactive monomer. |

### Regulators, proteins, and complexes

| Node | Type | Grounding recommendation | Scope |
|---|---|---|---|
| FNR | O₂-responsive transcription factor | UniProt/NCBI Gene for the curated strain | Direct Fe–S O₂ sensor in E. coli; not universal. |
| ArcB | membrane-associated sensor kinase | Strain-specific UniProt | Responds primarily to respiratory/quinone redox state rather than simply binding O₂. |
| ArcA | response regulator | Strain-specific UniProt | ArcA-P is the active transcriptional regulatory state. |
| NarX | nitrate/nitrite sensor kinase | Strain-specific UniProt | E. coli NarXL paradigm. |
| NarL | response regulator | Strain-specific UniProt | Cooperates with FNR at `narGHJI`. |
| NarGHIJ nitrate reductase | respiratory enzyme complex | Strain-specific UniProt subunits; EC/Rhea where verified | Enables nitrate respiration; neither universal nor required for the trait. |
| FrdABCD fumarate reductase | respiratory complex | Strain-specific UniProt | Candidate alternative-acceptor module. |
| DmsABC DMSO reductase | respiratory complex | Strain-specific UniProt | Candidate alternative-acceptor module. |
| pyruvate formate-lyase/PflB | fermentative enzyme | Strain-specific UniProt; EC candidate | Representative mixed-acid fermentation node, not a universal marker. |

### Processes and cellular locations

| Node | Suggested grounding | Note |
|---|---|---|
| aerobic respiration | `GO:0009060` | Verify exact GO label/version before YAML insertion. |
| anaerobic respiration | `GO:0009061` | Keep separate from fermentation. |
| fermentation | `GO:0006113` | Does not use an external terminal electron acceptor. |
| tricarboxylic-acid cycle | `GO:0006099` | ArcA chiefly represses the oxidative/aerobic program in the E. coli model. |
| electron-transport chain | GO candidate | Cytoplasmic membrane in bacteria. |
| transcriptional regulation | GO candidate | FNR/ArcA/NarL act at target promoters. |
| cytoplasmic membrane | `GO:0005886` | Appropriate location for respiratory chains and ArcB. |
| cytoplasm | `GO:0005737` | FNR and ArcA regulatory activity. |

### Taxon/context nodes

Use `NCBITaxon:562` for *Escherichia coli* only when evidence is species-level; preferably ground to the experimental strain when reported. Other useful explicit contexts include *Salmonella enterica*, *Shewanella oneidensis* MR-1, and Enterobacterales. Do not transfer E. coli edges to all facultative anaerobes solely because they share the phenotype.

## 4. Candidate causal edges

The compact high-confidence edge set is summarized below; the expanded evidence table follows.

| subject | predicate | object | scope/confidence |
|---|---|---|---|
| molecular oxygen (CHEBI:15379) | inhibits | active FNR dimer ([4Fe-4S]-FNR) | High; E. coli model and close Enterobacterales paradigms, not universal across all facultative anaerobes (unden2021sensingofo2 pages 1-7, sevilla2019redoxbasedtranscriptionalregulation pages 14-16, beilen2016allthreeendogenous pages 4-5) |
| anoxia / low O2 | enables | FNR [4Fe-4S] dimer DNA-binding state | High; E. coli-specific mechanistic evidence widely used as reference model for facultative anaerobiosis (unden2021sensingofo2 pages 1-7, sevilla2019redoxbasedtranscriptionalregulation pages 14-16, unden2021sensingofo2 pages 25-31) |
| active FNR | activates expression of | anaerobic respiration and fermentation genes | High; especially nar/dms/frd and fermentative functions in E. coli/Salmonella-like systems (sevilla2019redoxbasedtranscriptionalregulation pages 14-16, unden2021sensingofo2 pages 1-7) |
| anaerobiosis / microaerobiosis | activates | ArcB-to-ArcA phosphotransfer | High; ArcAB evidence is strongest in E. coli and related facultative Enterobacterales (beilen2016allthreeendogenous pages 1-2, brown2022thearcabtwocomponent pages 2-3, beilen2016allthreeendogenous pages 4-5) |
| phosphorylated ArcA (ArcA-P) | represses | aerobic respiration and oxidative TCA-cycle genes | High; E. coli/Enterobacterales-centered regulatory model, not a universal bacterial rule (beilen2016allthreeendogenous pages 1-2, brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15) |
| phosphorylated ArcA (ArcA-P) | promotes | fermentation / mixed-acid fermentation programs | High-moderate; strongest support in E. coli and related Enterobacterales (brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15) |
| nitrate (CHEBI:17632) | activates | NarX/NarL signaling | High; classic E. coli nitrate-sensing pathway, taxon-specific to Nar systems carrying bacteria (unden2021sensingofo2 pages 1-7, unden2021sensingofo2 pages 25-31) |
| NarL + active FNR | activates expression of | narGHJI nitrate reductase operon | High; direct promoter-level support in E. coli paradigm (unden2021sensingofo2 pages 1-7, unden2021sensingofo2 pages 25-31) |
| oxygen availability | has-priority-over | nitrate as terminal electron acceptor | High; respiratory hierarchy well supported for E. coli-like facultative anaerobes (unden2021sensingofo2 pages 1-7, brown2022thearcabtwocomponent pages 14-15) |
| nitrate respiration | has-priority-over | alternative electron acceptors (e.g., fumarate, DMSO, TMAO/tetrathionate depending taxon) | Moderate-high; hierarchy is strong but exact acceptor set is taxon-specific (unden2021sensingofo2 pages 1-7, price2021bacterialapproachesto pages 11-12) |
| absence of suitable external electron acceptors | causes shift to | fermentation | High; applies broadly to the E. coli/Enterobacterales model of facultative anaerobiosis (beilen2016allthreeendogenous pages 1-2, brown2022thearcabtwocomponent pages 14-15) |


*Table: This table summarizes compact, high-confidence candidate causal edges for curating facultatively anaerobic physiology, emphasizing the best-supported E. coli/Enterobacterales regulatory model. It is useful as a starting point for TraitMech graph editing while clearly flagging scope limits.*

| # | Subject—predicate—object | Reference and supporting snippet | Curation notes |
|---|---|---|---|
| 1 | **anoxia → enables → [4Fe–4S]-FNR homodimer/DNA binding** | Unden & Klein: under anoxia, FNR is an active homodimer carrying `[4Fe-4S]²⁺` clusters and capable of promoter binding. DOI: [10.1111/1462-2920.15293](https://doi.org/10.1111/1462-2920.15293), published November 2021. (unden2021sensingofo2 pages 1-7) | **High confidence; E. coli paradigm.** Qualify by organism and cluster state. |
| 2 | **O₂ → converts/inactivates → active FNR** | O₂ decomposes the FNR `[4Fe-4S]²⁺` state to `[2Fe-2S]²⁺`, yielding an inactive monomer unable to bind FNR sites. (unden2021sensingofo2 pages 1-7) | **High confidence; direct molecular mechanism.** Better modeled as conversion plus loss of DNA binding than generic inhibition. |
| 3 | **active FNR → activates transcription of → anaerobic respiratory operons (`nar`, `dms`, `frd`)** | Review evidence states that anaerobic `[4Fe-4S]` FNR activates nitrate-, DMSO-, and fumarate-respiratory genes. DOI: [10.1089/ars.2017.7442](https://doi.org/10.1089/ars.2017.7442), published May 2019. (sevilla2019redoxbasedtranscriptionalregulation pages 14-16) | **High confidence for E. coli.** Split into operon-specific edges if YAML permits. |
| 4 | **active FNR → activates → fermentative-enzyme expression** | The same review reports activation of fermentative enzymes under anaerobic conditions. (sevilla2019redoxbasedtranscriptionalregulation pages 14-16) | **Moderate–high.** Prefer named targets supported by primary promoter/genetic evidence rather than an undifferentiated fermentation node. |
| 5 | **active FNR → represses → aerobic respiratory genes** | FNR represses aerobic respiratory functions including cytochrome oxidase and NADH-dehydrogenase genes. (sevilla2019redoxbasedtranscriptionalregulation pages 14-16) | **High for E. coli; target-specific.** Do not imply all oxidases are regulated identically. |
| 6 | **anaerobic/microaerobic respiratory state → activates → ArcB-to-ArcA phosphotransfer** | Under anaerobic conditions ArcB autophosphorylates and transfers phosphate to ArcA; aerobic growth lacks this transphosphorylation. DOI: [10.3389/fmicb.2016.01339](https://doi.org/10.3389/fmicb.2016.01339), published September 2016. (beilen2016allthreeendogenous pages 1-2, beilen2016allthreeendogenous pages 4-5) | **High for E. coli.** The input is respiratory redox state, not necessarily O₂ binding by ArcB. |
| 7 | **ArcB → phosphorylates → ArcA** | ArcB senses microaerobic/anaerobic respiratory conditions and phosphorylates ArcA. DOI: [10.1128/mmbr.00110-21](https://doi.org/10.1128/mmbr.00110-21), published June 2022. (brown2022thearcabtwocomponent pages 2-3) | **High.** An explicit phosphotransfer edge is preferable to “activates.” |
| 8 | **ArcA-P → represses → aerobic respiration/oxidative TCA program** | ArcA-P primarily represses aerobic respiration; reviewed targets include oxidative TCA-cycle and other oxidative catabolic genes. (brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15) | **High in Enterobacterales model.** The regulon is broad—over 1,100 genes were reported as directly or indirectly regulated in E. coli—so avoid asserting every target is direct. (brown2022thearcabtwocomponent pages 2-3) |
| 9 | **ArcA-P → promotes → mixed-acid fermentation program** | ArcA-P promotes fermentation as the principal energy-generating pathway when respiration is unavailable and promotes mixed-acid-fermentation genes. (brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15) | **Moderate–high.** “Promotes” includes direct and indirect regulation; use named genes for direct edges. |
| 10 | **quinone-pool redox state → modulates → ArcB activity** | Ubiquinone and menaquinone redox states regulate ArcBA and can have opposing effects. DOI: [10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795), published August 2021. (price2021bacterialapproachesto pages 11-12) | **Mechanistically important but curate cautiously.** The retrieved evidence does not justify a universal “reduced quinone directly activates ArcB” edge; quinone-species effects and models remain contested. |
| 11 | **nitrate → activates → NarX/NarL signaling** | NarX senses nitrate/nitrite, discriminates the signals, and phosphorylates NarL in nitrate’s presence; without nitrate, NarL is dephosphorylated. (unden2021sensingofo2 pages 1-7, unden2021sensingofo2 pages 25-31) | **High for E. coli.** Encode nitrate concentration and NarX/NarQ specificity if known. |
| 12 | **FNR + NarL-P → activates transcription of → `narGHJI`** | Expression of membrane nitrate reductase `narGHJI` requires promoter binding/functions of both FNR and NarL. (unden2021sensingofo2 pages 1-7, unden2021sensingofo2 pages 25-31) | **High; combinatorial regulation.** A conjunction/reified regulatory event is more accurate than two independent sufficient-cause edges. |
| 13 | **O₂ availability → prioritizes → aerobic respiration over anaerobic respiration/fermentation** | O₂ represses anaerobic respiration and fermentation; aerobic growth activates the citric-acid cycle for more complete glucose oxidation. The review contrasts approximately 24 reducing equivalents (`[H]`) aerobically with 8 anaerobically in its accounting. (unden2021sensingofo2 pages 1-7) | **High as an E. coli physiological hierarchy; medium for exact numeric generalization.** Do not encode the 24-versus-8 values as universal stoichiometry. |
| 14 | **nitrate under anoxia → prioritizes → nitrate respiration over lower-potential acceptors and fermentation** | Under anoxia, nitrate respiration is preferred and represses pathways using fumarate, tetrathionate, DMSO, or TMAO and fermentation. (unden2021sensingofo2 pages 1-7) | **Moderate–high; taxon and medium dependent.** Exact hierarchy varies with organism, concentrations, toxicity, and ecological history. (price2021bacterialapproachesto pages 11-12) |
| 15 | **absence of usable external electron acceptor → causes shift to → fermentation** | ArcAB review describes carbon catabolism as aerobic respiration with O₂, anaerobic respiration with alternatives, or fermentation when cells cannot respire. (brown2022thearcabtwocomponent pages 14-15) | **High conceptual edge.** Fermentative capacity depends on substrate and biosynthetic sufficiency. |
| 16 | **aerobic respiratory chain activity → consumes → local O₂** | Expert review identifies bacterial aerobic respiration as central to oxygen consumption and formation of hypoxic infectious sites. (andre2021theselectiveadvantage pages 1-2) | **Moderate for TraitMech.** Ecological feedback edge, not required to establish the intrinsic trait. |
| 17 | **amino-acid supplementation → permits/facilitates → fermentative growth of *S. oneidensis* MR-1 in defined glucose medium** | A 2023 study found that amino-acid sources facilitate fermentative growth and used transcriptomics with `log₂ FC >1`, `P<0.05`; data are deposited as GEO GSE220284. DOI: [10.1128/aem.00868-23](https://doi.org/10.1128/aem.00868-23), July 2023. (ikeda2023supplementationwithamino pages 10-11) | **Assay- and taxon-specific.** Important boundary case: possessing apparent pathway genes does not guarantee growth in unsupplemented anoxic minimal medium. |
| 18 | **anoxic culture conditions → alter → Salmonella–phage infection kinetics/population control** | A 2023 Salmonella–ϕSan23 study reports that anoxia changes phage life-cycle length, bacterial control, resistance emergence, cell size, and expression of nitrate-reduction and sulfur-compound-transport genes. DOI: [10.1128/aem.01491-23](https://doi.org/10.1128/aem.01491-23), December 2023. (villamizar2023anaerobiosisaneglected pages 1-2) | **Application evidence, not a core trait edge.** Mechanisms remain incompletely resolved; do not place phage resistance downstream of facultative anaerobiosis without additional evidence. |
| 19 | **ArcA/ArcB-mediated flexibility → contributes to → bloodstream fitness** | A five-species 2024 murine bacteremia study associates Arc-system switching with metabolic flexibility; it evaluated 18 conserved genes/operons and reports that at least 80% of Gram-negative bacilli causing bacteremia are facultative anaerobes. DOI: [10.1371/journal.ppat.1012495](https://doi.org/10.1371/journal.ppat.1012495), August 2024. (mobley2024fitnessfactorgenes pages 22-24) | **Moderate and context-specific.** Association and mutant fitness do not establish that facultative anaerobiosis alone causes bacteremia. |

## 5. Current understanding and recent developments

### Regulatory interpretation

Authoritative reviews now describe ArcAB not as a binary O₂ switch but as a **respiratory-flux/redox-responsive continuum**. ArcA activity is inversely associated with aerobiosis, yet nitrate and other acceptors can change ArcA activity independently of O₂. Recent evidence also challenges the older description of ArcAB as exclusively anaerobic. (brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15)

FNR and ArcAB are complementary rather than redundant. FNR directly senses O₂ through an Fe–S cluster, whereas ArcB integrates the state of membrane electron transport through quinones and associated respiratory signals. NarXL overlays acceptor-specific information, permitting nitrate respiration only when both anoxic and nitrate signals are appropriate. (price2021bacterialapproachesto pages 11-12, unden2021sensingofo2 pages 1-7)

### 2023–2024 applications

* **Infection biology:** Facultative anaerobic Enterobacterales dominate Gram-negative bacteremia; the 2024 five-species study reports at least 80% of causative Gram-negative bacilli as facultative anaerobes and identifies `arcA` among conserved infection-fitness factors in multiple species. This supports ArcA as a potential therapeutic or pathogenesis-research node, but species-level effects are not identical. (mobley2024fitnessfactorgenes pages 22-24)
* **Phage therapy:** Oxygen status materially changes phage infection dynamics in a facultative Salmonella model. Because intended phage-therapy sites such as intestines and wounds can be anoxic, aerobic-only efficacy testing may misestimate performance. (villamizar2023anaerobiosisaneglected pages 1-2)
* **Bioelectrochemistry and fermentation:** Nutrient supplementation can expose otherwise cryptic fermentative growth in *S. oneidensis* MR-1, illustrating that trait assays depend on medium composition and biosynthetic constraints. (ikeda2023supplementationwithamino pages 10-11)
* **Synthetic metabolism:** A 2024 study engineered controlled respiro-fermentative *E. coli* by combining fermentative metabolism with selected respiratory modules, demonstrating that O₂ can be used selectively to rebalance otherwise redox-unbalanced product pathways. DOI: [10.1038/s41467-024-51029-x](https://doi.org/10.1038/s41467-024-51029-x), published August 2024. This is a real implementation of modular respiratory/fermentative logic, although it describes an engineered strain and should not be treated as evidence for the natural trait mechanism.

## 6. Recommended minimal YAML graph

A conservative first curation should contain these mechanistic paths:

```text
O2 --inactivates--> [4Fe-4S]-FNR
anoxia --enables--> [4Fe-4S]-FNR dimer
[4Fe-4S]-FNR --activates--> anaerobic respiratory/fermentative gene program

respiratory quinone redox state --modulates--> ArcB
ArcB --phosphorylates--> ArcA
ArcA-P --represses--> aerobic oxidative metabolism
ArcA-P --promotes--> fermentative metabolism

nitrate --activates--> NarX/NarL
FNR + NarL-P --activate--> narGHJI
narGHJI --enables--> nitrate respiration

O2 respiration --supports--> oxic growth
alternative-acceptor respiration OR fermentation --supports--> anoxic growth
oxic growth AND anoxic growth --constitute--> METPO:1000605
```

Every molecular edge should carry a taxon qualifier such as *E. coli* K-12 unless the cited source experimentally establishes broader conservation.

## 7. Claims not yet ready for TraitMech curation

1. **Do not curate “FNR causes facultative anaerobiosis” universally.** Many facultative anaerobes lack the E. coli FNR architecture or use different oxygen sensors.
2. **Do not treat ArcB as a simple direct O₂ receptor.** Current reviews favor respiratory/quinone redox sensing, and competing molecular models remain. (price2021bacterialapproachesto pages 11-12, brown2022thearcabtwocomponent pages 2-3)
3. **Do not curate “reduced quinone activates ArcB” without specifying quinone species, organism, and assay.** Ubiquinone, menaquinone, and demethylmenaquinone may contribute differently.
4. **Do not make nitrate reductase necessary for the trait.** Anaerobic growth can be fermentative; acceptor repertoires vary.
5. **Do not equate aerotolerance with facultative anaerobiosis.** Oxygen survival or ROS-detoxification genes alone do not demonstrate oxic growth. (andre2021theselectiveadvantage pages 1-2)
6. **Do not infer phenotype from genome content alone.** *S. oneidensis* illustrates that complete-looking fermentative pathways may fail to support growth in a particular minimal medium unless nutritional constraints are relieved. (ikeda2023supplementationwithamino pages 10-11)
7. **Do not curate ROS-detoxification enzymes as defining causes.** Catalase, superoxide dismutase, peroxidases, and repair systems can aid oxygen tolerance, but they occur in aerobes, facultative organisms, and oxygen-tolerant anaerobes; trait-specific sufficiency is unsupported.
8. **Do not universalize the electron-acceptor hierarchy.** The order O₂ > nitrate > fumarate/DMSO/TMAO > fermentation is robust for the E. coli paradigm but changes with taxon, concentrations, toxicity, and ecological niche. (unden2021sensingofo2 pages 1-7, price2021bacterialapproachesto pages 11-12)
9. **Do not promote infection or phage-response associations to intrinsic trait edges.** They are downstream ecological consequences with substantial host-, strain-, and assay-dependence. (mobley2024fitnessfactorgenes pages 22-24, villamizar2023anaerobiosisaneglected pages 1-2)
10. **Avoid the reported “36 to 3 ATP molecules” nitrate-respiration comparison as a graph datum.** It is a secondary, organism-specific accounting cited in the phage study and is not reliable as general facultative-anaerobe stoichiometry. (villamizar2023anaerobiosisaneglected pages 16-18)

## 8. DOI-first bibliography

1. André AC, Debande L, Marteyn BS. “The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.” *Cellular Microbiology*. Published April 2021. [https://doi.org/10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338). (andre2021theselectiveadvantage pages 1-2)
2. Unden G, Klein R. “Sensing of O₂ and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration by O₂ and nitrate.” *Environmental Microbiology*. Published November 2021. [https://doi.org/10.1111/1462-2920.15293](https://doi.org/10.1111/1462-2920.15293). (unden2021sensingofo2 pages 1-7, unden2021sensingofo2 pages 25-31)
3. Price EE, Román-Rodríguez F, Boyd JM. “Bacterial approaches to sensing and responding to respiration and respiration metabolites.” *Molecular Microbiology* 116:1009–1021. Published August 2021. [https://doi.org/10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795). (price2021bacterialapproachesto pages 11-12)
4. Brown AN et al. “The ArcAB Two-Component System: Function in Metabolism, Redox Control, and Infection.” *Microbiology and Molecular Biology Reviews* 86(2). Published June 2022. [https://doi.org/10.1128/mmbr.00110-21](https://doi.org/10.1128/mmbr.00110-21). (brown2022thearcabtwocomponent pages 2-3, brown2022thearcabtwocomponent pages 14-15)
5. van Beilen JWA, Hellingwerf KJ. “All Three Endogenous Quinone Species of Escherichia coli Are Involved in Controlling the Activity of the Aerobic/Anaerobic Response Regulator ArcA.” *Frontiers in Microbiology* 7. Published September 2016. [https://doi.org/10.3389/fmicb.2016.01339](https://doi.org/10.3389/fmicb.2016.01339). (beilen2016allthreeendogenous pages 1-2, beilen2016allthreeendogenous pages 4-5)
6. Sevilla E et al. “Redox-Based Transcriptional Regulation in Prokaryotes: Revisiting Model Mechanisms.” *Antioxidants & Redox Signaling* 30:1651–1696. Published May 2019. [https://doi.org/10.1089/ars.2017.7442](https://doi.org/10.1089/ars.2017.7442). (sevilla2019redoxbasedtranscriptionalregulation pages 14-16)
7. Villamizar SH et al. “Anaerobiosis, a neglected factor in phage-bacteria interactions.” *Applied and Environmental Microbiology* 89(12). Published December 2023. [https://doi.org/10.1128/aem.01491-23](https://doi.org/10.1128/aem.01491-23). (villamizar2023anaerobiosisaneglected pages 16-18, villamizar2023anaerobiosisaneglected pages 1-2)
8. Ikeda S et al. “Supplementation with Amino Acid Sources Facilitates Fermentative Growth of Shewanella oneidensis MR-1 in Defined Media.” *Applied and Environmental Microbiology* 89(7). Published July 2023. [https://doi.org/10.1128/aem.00868-23](https://doi.org/10.1128/aem.00868-23). (ikeda2023supplementationwithamino pages 10-11)
9. Mobley HLT et al. “Fitness factor genes conserved within the multi-species core genome of Gram-negative Enterobacterales species contribute to bacteremia pathogenesis.” *PLOS Pathogens* 20:e1012495. Published August 2024. [https://doi.org/10.1371/journal.ppat.1012495](https://doi.org/10.1371/journal.ppat.1012495). (mobley2024fitnessfactorgenes pages 22-24)
10. Schulz-Mirbach H et al. “Engineering new-to-nature biochemical conversions by combining fermentative metabolism with respiratory modules.” *Nature Communications* 15. Published August 2024. [https://doi.org/10.1038/s41467-024-51029-x](https://doi.org/10.1038/s41467-024-51029-x).

**Curation judgment:** proceed with an explicitly **E. coli/Enterobacterales-scoped oxygen-switch graph**, with the phenotype defined by the conjunction of oxic and anoxic growth. Treat FNR, ArcBA, and NarXL as well-supported exemplar mechanisms, not universal necessary components of `METPO:1000605`.

References

1. (andre2021theselectiveadvantage pages 1-2): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.

2. (price2021bacterialapproachesto pages 11-12): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

3. (unden2021sensingofo2 pages 1-7): Gottfried Unden and Robin Klein. Sensing of <scp>o<sub>2</sub></scp> and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration by <scp>o<sub>2</sub></scp> and nitrate. Nov 2021. URL: https://doi.org/10.1111/1462-2920.15293, doi:10.1111/1462-2920.15293. This article has 27 citations and is from a domain leading peer-reviewed journal.

4. (sevilla2019redoxbasedtranscriptionalregulation pages 14-16): Emma Sevilla, María Teresa Bes, Andrés González, María Luisa Peleato, and María F. Fillat. Redox-based transcriptional regulation in prokaryotes: revisiting model mechanisms. Antioxidants &amp; Redox Signaling, 30:1651-1696, May 2019. URL: https://doi.org/10.1089/ars.2017.7442, doi:10.1089/ars.2017.7442. This article has 49 citations and is from a domain leading peer-reviewed journal.

5. (beilen2016allthreeendogenous pages 4-5): Johan W. A. van Beilen and Klaas J. Hellingwerf. All three endogenous quinone species of escherichia coli are involved in controlling the activity of the aerobic/anaerobic response regulator arca. Frontiers in Microbiology, Sep 2016. URL: https://doi.org/10.3389/fmicb.2016.01339, doi:10.3389/fmicb.2016.01339. This article has 74 citations and is from a peer-reviewed journal.

6. (unden2021sensingofo2 pages 25-31): Gottfried Unden and Robin Klein. Sensing of <scp>o<sub>2</sub></scp> and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration by <scp>o<sub>2</sub></scp> and nitrate. Nov 2021. URL: https://doi.org/10.1111/1462-2920.15293, doi:10.1111/1462-2920.15293. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (beilen2016allthreeendogenous pages 1-2): Johan W. A. van Beilen and Klaas J. Hellingwerf. All three endogenous quinone species of escherichia coli are involved in controlling the activity of the aerobic/anaerobic response regulator arca. Frontiers in Microbiology, Sep 2016. URL: https://doi.org/10.3389/fmicb.2016.01339, doi:10.3389/fmicb.2016.01339. This article has 74 citations and is from a peer-reviewed journal.

8. (brown2022thearcabtwocomponent pages 2-3): Aric N. Brown, Mark T. Anderson, Michael A. Bachman, and Harry L. T. Mobley. The arcab two-component system: function in metabolism, redox control, and infection. Jun 2022. URL: https://doi.org/10.1128/mmbr.00110-21, doi:10.1128/mmbr.00110-21. This article has 115 citations and is from a domain leading peer-reviewed journal.

9. (brown2022thearcabtwocomponent pages 14-15): Aric N. Brown, Mark T. Anderson, Michael A. Bachman, and Harry L. T. Mobley. The arcab two-component system: function in metabolism, redox control, and infection. Jun 2022. URL: https://doi.org/10.1128/mmbr.00110-21, doi:10.1128/mmbr.00110-21. This article has 115 citations and is from a domain leading peer-reviewed journal.

10. (ikeda2023supplementationwithamino pages 10-11): Sota Ikeda, Keisuke Tomita, Gen Nakagawa, Atsushi Kouzuma, and Kazuya Watanabe. Supplementation with amino acid sources facilitates fermentative growth of shewanella oneidensis mr-1 in defined media. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00868-23, doi:10.1128/aem.00868-23. This article has 4 citations and is from a peer-reviewed journal.

11. (villamizar2023anaerobiosisaneglected pages 1-2): Santiago Hernández Villamizar, Luis A. Chica Cárdenas, Laura T. Morales Mancera, and Martha J. Vives Florez. Anaerobiosis, a neglected factor in phage-bacteria interactions. Dec 2023. URL: https://doi.org/10.1128/aem.01491-23, doi:10.1128/aem.01491-23. This article has 11 citations and is from a peer-reviewed journal.

12. (mobley2024fitnessfactorgenes pages 22-24): Harry L. T. Mobley, Mark T. Anderson, Bridget S. Moricz, Geoffrey B. Severin, Caitlyn L. Holmes, Elizabeth N. Ottosen, Tad Eichler, Surbhi Gupta, Santosh Paudel, Ritam Sinha, Sophia Mason, Stephanie D. Himpsl, Aric N. Brown, Margaret Gaca, Christina M. Kiser, Thomas H. Clarke, Derrick E. Fouts, Victor J. DiRita, and Michael A. Bachman. Fitness factor genes conserved within the multi-species core genome of gram-negative enterobacterales species contribute to bacteremia pathogenesis. PLOS Pathogens, 20:e1012495, Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012495, doi:10.1371/journal.ppat.1012495. This article has 10 citations and is from a highest quality peer-reviewed journal.

13. (villamizar2023anaerobiosisaneglected pages 16-18): Santiago Hernández Villamizar, Luis A. Chica Cárdenas, Laura T. Morales Mancera, and Martha J. Vives Florez. Anaerobiosis, a neglected factor in phage-bacteria interactions. Dec 2023. URL: https://doi.org/10.1128/aem.01491-23, doi:10.1128/aem.01491-23. This article has 11 citations and is from a peer-reviewed journal.