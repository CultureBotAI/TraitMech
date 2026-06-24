---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:03:05.684036'
end_time: '2026-06-17T21:24:43.335730'
duration_seconds: 1297.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: aerobic
  trait_identifier: METPO:1000602
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: aerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which growth occurs in the presence of molecular\
    \ oxygen (O\u2082), typically using O\u2082 as the terminal electron acceptor."
  parent_traits: METPO:1000601
  synonyms: Ox_aerobic, aerobe
  evidence_summary: 'PMID:21413255: aerobes require molecular oxygen as a terminal
    electron acceptor (Supports aerobic growth as oxygen-dependent respiration.) |
    PMID:21183663: Bacillus subtilis is an aerobic spore-forming Gram-positive bacterium
    (Organism example: Bacillus subtilis is described as aerobic.)'
  causal_graph_summary: 'aerobic_trait_mechanism: 4 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** aerobic
- **METPO identifier:** METPO:1000602
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the presence of molecular oxygen (O₂), typically using O₂ as the terminal electron acceptor.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_aerobic, aerobe
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Supports aerobic growth as oxygen-dependent respiration.) | PMID:21183663: Bacillus subtilis is an aerobic spore-forming Gram-positive bacterium (Organism example: Bacillus subtilis is described as aerobic.)
- **Existing causal graph summary:** aerobic_trait_mechanism: 4 nodes, 4 edges

## Research Objective

Research the microbial trait **aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerobic.yaml`.

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
- **Trait label:** aerobic
- **METPO identifier:** METPO:1000602
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the presence of molecular oxygen (O₂), typically using O₂ as the terminal electron acceptor.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_aerobic, aerobe
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Supports aerobic growth as oxygen-dependent respiration.) | PMID:21183663: Bacillus subtilis is an aerobic spore-forming Gram-positive bacterium (Organism example: Bacillus subtilis is described as aerobic.)
- **Existing causal graph summary:** aerobic_trait_mechanism: 4 nodes, 4 edges

## Research Objective

Research the microbial trait **aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerobic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **aerobic** (METPO:1000602)

### Scope summary (TraitMech-ready)
The trait **aerobic** denotes an oxygen preference/physiological capacity in which microbial growth occurs in the presence of molecular oxygen, typically because **O2 functions as the terminal electron acceptor** in a respiratory electron transport chain (ETC) that conserves energy as a proton motive force (PMF) for ATP synthesis. Canonically, this implies a membrane respiratory chain that transfers electrons from dehydrogenases to a quinone pool and then to **terminal oxidases** that reduce O2 to water. (“the terminal electron acceptor is molecular oxygen”) (borisov2015oxygenasacceptor pages 1-2).

**Boundary cases and nearby traits** matter for curation. Oxygen response is not binary; “O2 sensitivity is a matter of degree” and organisms labeled anaerobes may retain O2-directed respiratory enzymes that allow survival or even growth at low O2, whereas higher O2 arrests growth by disabling key O2-sensitive enzymes (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 1-3). A concrete boundary case is **Bacteroides fragilis**, where **cytochrome bd oxidase can enhance growth at low but finite O2**, leading to classification as “nanoaerophile” (lu2021whenanaerobesencounter pages 4-6). Conversely, oxygen blocks growth in obligate anaerobes because even low O2 can rapidly inactivate anaerobic core enzymes; e.g., “even low levels of O2 inactivate PFL in seconds” (pyruvate formate-lyase, a glycyl-radical enzyme) (lu2021whenanaerobesencounter pages 4-6).

Pragmatic curation distinctions:
- **Obligate aerobe** (subset of aerobic): requires O2 for growth (not directly quoted in retrieved sources; treat as label-level for now).
- **Facultative anaerobe**: can grow aerobically with O2 as acceptor and anaerobically using fermentation/alternative acceptors; mechanistic flexibility is consistent with branched chains and repair systems (e.g., E. coli as facultative model) (lu2021whenanaerobesencounter pages 13-15, borisov2015oxygenasacceptor pages 1-2).
- **Microaerophile/nanoaerophile**: grows optimally at low O2; often uses high-affinity oxidases (e.g., cbb3-type HCOs; bd-type oxidases) (lu2021whenanaerobesencounter pages 4-6, nastasi2024cyanideinsensitiveoxidase pages 2-3).
- **Aerotolerant anaerobe**: tolerates O2 but does not use it for growth via respiration; mechanistically may emphasize ROS detox rather than energy-conserving O2 respiration (concept supported by presence of antioxidant systems in anaerobes) (lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 16-17).

### Candidate mechanistic nodes (grouped by type)
The following curation-oriented node inventory is grounded where feasible; label-only nodes are included when stable identifiers were not explicit in the evidence.

| Node label | Suggested grounding | Evidence support | Key citations |
|---|---|---|---|
| **Environmental/assay factors** |  |  |  |
| molecular oxygen availability | CHEBI:15379 | Defining environmental factor for aerobic respiration; terminal electron acceptor | (borisov2015oxygenasacceptor pages 1-2, lu2021whenanaerobesencounter pages 1-3) |
| fully aerobic conditions | ENVO:01001405? / label-only | bo3/cyo operon favored under fully aerobic growth | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| microaerobic / low but finite O2 | ENVO:01000823? / label-only | bd/cbb3 systems support growth at low O2; boundary case with nanoaerophily | (lu2021whenanaerobesencounter pages 4-6, nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| 2% O2 growth condition | label-only | P. aeruginosa cco1/cco2 mutant still grows at 2% O2 if CIO present | (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| 56% aerobiosis | label-only | cydABX expression maximum reported at intermediate aerobiosis | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| 0% aerobiosis | label-only | appCBX expression maximum under anoxic/aerobiosis-zero condition | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| aeration / oxygen exposure | GO:0010644? / label-only | Causes oxidative stress and inactivates O2-sensitive anaerobic enzymes | (lu2021whenanaerobesencounter pages 8-9) |
| oxygraphy / O2 consumption assay | label-only | Used to quantify respiration and oxidase inhibitor tolerance | (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| cyanide titration assay | label-only | Used to separate bo3-like vs bd-like terminal oxidase contributions | (gonzalezmontalvo2024therespiratorychain pages 5-7) |
| **Chemicals/electron acceptors/inhibitors** |  |  |  |
| molecular oxygen (O2) | CHEBI:15379 | Terminal electron acceptor in aerobic growth | (borisov2015oxygenasacceptor pages 1-2, lu2021whenanaerobesencounter pages 1-3) |
| water (H2O) | CHEBI:15377 | Product of four-electron O2 reduction by terminal oxidases | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| ubiquinone / ubiquinol | CHEBI:16389 / label-only | Quinol donor for bo3 and bd oxidases in ETC | (borisov2015oxygenasacceptor pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2) |
| menaquinone | CHEBI:58046 | Part of quinone pool feeding respiratory chain | (borisov2015oxygenasacceptor pages 1-2) |
| cyanide (CN−) | CHEBI:18420 | Classic oxidase inhibitor; bd-type more tolerant than bo3-like components | (nastasi2024cyanideinsensitiveoxidase pages 2-3, gonzalezmontalvo2024therespiratorychain pages 5-7) |
| carbon monoxide (CO) | CHEBI:17245 | Competitive inhibitor of terminal oxidases; bd-I relatively resistant | (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 1-2) |
| nitric oxide (NO) | CHEBI:16480 | Reversible inhibitor of CIO; stressor selecting alternative oxidases | (nastasi2024cyanideinsensitiveoxidase pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 16-17) |
| hydrogen sulfide (H2S) | CHEBI:16136 | Inhibits many oxidases but CIO-dependent respiration is tolerant | (nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| superoxide | CHEBI:18421 | Endogenous ROS from oxygen/redox reactions | (lu2021whenanaerobesencounter pages 9-11, maslovska2023oxidativestressand pages 1-3) |
| hydrogen peroxide | CHEBI:16240 | Endogenous/exogenous ROS requiring scavenging | (lu2021whenanaerobesencounter pages 9-11, maslovska2023oxidativestressand pages 1-3) |
| hydroxyl radical | CHEBI:16243 | Highly damaging ROS produced downstream of oxidative stress | (maslovska2023oxidativestressand pages 1-3, bastos2025whatdowe pages 7-8) |
| **Pathways/modules/processes** |  |  |  |
| aerobic respiration | GO:0009060 | Core trait mechanism using O2 as terminal electron acceptor | (borisov2015oxygenasacceptor pages 1-2, lu2021whenanaerobesencounter pages 1-3) |
| electron transport chain | GO:0022900 | Transfers electrons from dehydrogenases via quinones to oxidases | (borisov2015oxygenasacceptor pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2) |
| quinol oxidation | GO:0050136? / label-only | Terminal quinol oxidases couple quinol oxidation to O2 reduction | (borisov2015oxygenasacceptor pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2) |
| proton motive force generation | GO:0015986 | Oxidases conserve energy as transmembrane electrochemical gradient | (lu2021whenanaerobesencounter pages 4-6, nastasi2024membraneboundredoxenzyme pages 1-2) |
| ATP synthesis coupled to PMF | GO:0006754 / GO:0015986 | PMF powers ATP synthesis | (lu2021whenanaerobesencounter pages 4-6) |
| oxidative stress response | GO:0006979 | Aerobic metabolism/oxygen exposure induces ROS defense programs | (hernandezmorfa2023theoxidativestress pages 3-4, maslovska2023oxidativestressand pages 1-3) |
| ROS detoxification | GO:0098869? / label-only | SOD/catalase/peroxidases remove radicals/peroxides | (maslovska2023oxidativestressand pages 1-3) |
| oxygen detoxification to water | label-only | rubredoxin oxidase, bd, and related systems can reduce O2 defensively | (lu2021whenanaerobesencounter pages 16-17) |
| **Complexes/enzymes (ETC)** |  |  |  |
| type I NADH dehydrogenase (NDH-1) | EC:7.1.1.2 | Protonmotive electron entry enzyme in respiratory chain | (borisov2015oxygenasacceptor pages 1-2) |
| type II NADH dehydrogenase (NDH-2) | EC:7.1.1.2? / label-only | Major electron entry point in K. aerogenes under tested conditions | (gonzalezmontalvo2024therespiratorychain pages 5-7) |
| succinate dehydrogenase | EC:1.3.5.1 | Feeds electrons into quinone pool | (nastasi2024membraneboundredoxenzyme pages 1-2, borisov2015oxygenasacceptor pages 1-2) |
| cytochrome bo3 oxidase | EC:7.1.1.3 / label-only | Heme-copper terminal oxidase favored in fully aerobic conditions | (nastasi2024membraneboundredoxenzyme pages 1-2, borisov2015oxygenasacceptor pages 1-2) |
| cyoABCDE operon | label-only | Encodes bo3 oxidase in E. coli / related taxa | (nastasi2024membraneboundredoxenzyme pages 1-2, gonzalezmontalvo2024therespiratorychain pages 5-7) |
| cytochrome bd-I oxidase | label-only | High CO resistance; supports respiration under inhibitor stress | (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 1-2) |
| cydABX operon | label-only | Encodes bd-I oxidase; expression favored below fully aerobic conditions | (nastasi2024membraneboundredoxenzyme pages 1-2, gonzalezmontalvo2024therespiratorychain pages 5-7) |
| cytochrome bd-II oxidase | label-only | Alternative bd oxidase with different CO/O2 kinetics | (nastasi2024membraneboundredoxenzyme pages 4-7) |
| appCBX operon | label-only | Encodes bd-II-type oxidase; maximal at 0% aerobiosis in E. coli | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| cytochrome cbb3 oxidase | label-only | High-affinity heme-copper oxidase supporting low-O2 growth | (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| cco1 / cco2 oxidase systems | label-only | P. aeruginosa cbb3-type oxidases important under microoxic conditions | (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| aa3-type cytochrome c oxidase | label-only | One branch of aerobic heme-copper oxidase repertoire | (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| cyanide-insensitive oxidase (CIO) | label-only | bd-type oxidase enabling H2S/NO/cyanide-tolerant aerobic respiration | (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| cioAB operon | label-only | Encodes CIO in P. aeruginosa | (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| ATP synthase | GO:0046933 / EC:7.1.2.2 | Uses PMF generated by respiration to synthesize ATP | (lu2021whenanaerobesencounter pages 4-6) |
| **ROS detox/repair systems** |  |  |  |
| superoxide dismutase (SOD) | EC:1.15.1.1 | Canonical radical-scavenging enzyme removing superoxide | (maslovska2023oxidativestressand pages 1-3, lu2021whenanaerobesencounter pages 16-17) |
| SodA | label-only | Aeration-upregulated SOD required for oxidative stress fitness in pneumococcus | (hernandezmorfa2023theoxidativestress pages 3-4) |
| catalase | EC:1.11.1.6 | Decomposes H2O2; canonical aerobic antioxidant enzyme | (maslovska2023oxidativestressand pages 1-3) |
| peroxidases | EC:1.11.1.- | General peroxide detoxification during oxidative stress | (maslovska2023oxidativestressand pages 1-3) |
| TpxD peroxiredoxin | label-only | Major H2O2 detox enzyme in S. pneumoniae | (hernandezmorfa2023theoxidativestress pages 3-4) |
| thioredoxin system (Trx/TrxR/NADPH) | GO:0006749? / label-only | Supplies reducing power for peroxiredoxin and redox defense | (hernandezmorfa2023theoxidativestress pages 3-4) |
| glutathione | CHEBI:16856 | Works with TpxD in protection from protein sulfenylation | (hernandezmorfa2023theoxidativestress pages 3-4) |
| OxyR regulator | UniProtKB:label-only | H2O2-responsive regulator tied to oxygen survival/virulence | (lu2021whenanaerobesencounter pages 16-17) |
| macromolecule repair after oxidation | GO:0006979? / label-only | Second major defense strategy besides ROS scavenging | (maslovska2023oxidativestressand pages 1-3, lu2021whenanaerobesencounter pages 8-9) |
| **Oxygen-sensitive enzymes (negative constraints)** |  |  |  |
| pyruvate formate-lyase (PFL) | EC:2.3.1.54 | Rapidly inactivated by even low O2; hallmark anti-aerobic constraint | (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 1-3) |
| pyruvate:ferredoxin oxidoreductase (PFOR) | EC:1.2.7.1 | Low-potential Fe-S enzyme impaired by oxygen exposure | (lu2021whenanaerobesencounter pages 8-9) |
| fumarase (O2/ROS-sensitive anaerobic context) | EC:4.2.1.2 | Inactivated in aerated anaerobes via endogenous ROS | (lu2021whenanaerobesencounter pages 8-9, lu2021whenanaerobesencounter pages 9-11) |
| aconitase | EC:4.2.1.3 | Solvent-exposed [4Fe-4S] enzyme vulnerable to ROS | (lu2021whenanaerobesencounter pages 9-11) |
| solvent-exposed [4Fe-4S] enzymes | GO:0051539 / label-only | Oxidative damage creates metabolic blocks upon aeration | (lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 6-8) |
| glycyl-radical enzymes | GO:0018580? / label-only | Direct O2 poisoning explains exclusion from true aerobic growth | (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 6-8) |


*Table: This table groups candidate nodes for curating an aerobic microbial TraitMech graph, organized by environment, chemicals, processes, respiratory machinery, ROS defenses, and oxygen-sensitive counterexamples. It is useful for selecting grounded nodes with direct literature support and for separating positive aerobic mechanisms from negative constraints.*

### Evidence-backed candidate causal edges (triples)
The table below proposes edges suitable for a TraitMech causal graph, including oxygen use, core ETC components, terminal oxidase specialization, inhibitor/stress effects, ROS generation/detoxification, and negative constraints (O2-sensitive enzymes). 

| Edge (S–P–O) | Evidence snippet (verbatim/near-verbatim) | Source (authors year, DOI, URL, publication month/year) | Notes (strength/uncertainty; taxon-specific) |
|---|---|---|---|
| Molecular oxygen (CHEBI:15379) – terminal electron acceptor for – aerobic respiratory chain | “the terminal electron acceptor is molecular oxygen” | Borisov & Verkhovsky 2015, doi:10.1128/ecosalplus.esp-0012-2015, https://doi.org/10.1128/ecosalplus.esp-0012-2015, Oct 2015 | Core defining edge for trait scope; broad bacterial support (borisov2015oxygenasacceptor pages 1-2) |
| Substrate dehydrogenases / NADH dehydrogenases – transfer electrons to – quinone pool | “Electrons are transferred from substrate-specific dehydrogenases… to a quinone pool (menaquinone, ubiquinone, dimethylmenoquinone)” | Borisov & Verkhovsky 2015, doi:10.1128/ecosalplus.esp-0012-2015, https://doi.org/10.1128/ecosalplus.esp-0012-2015, Oct 2015 | Good generic ETC edge; E. coli-centered but canonical (borisov2015oxygenasacceptor pages 1-2) |
| Quinol oxidases (bo3, bd, AppBCX) – oxidize – quinol and reduce O2 to H2O | “Quinol-to-O2 oxidation is catalyzed by quinol oxidases: cytochrome bo3 (CyoABCD… ) and cytochrome bd (CydABX…)… AppBCX also able to oxidize ubiquinol-8 and reduce O2 to H2O” | Borisov & Verkhovsky 2015, doi:10.1128/ecosalplus.esp-0012-2015, https://doi.org/10.1128/ecosalplus.esp-0012-2015, Oct 2015 | Strong mechanistic edge for terminal oxidase module; mostly E. coli nomenclature (borisov2015oxygenasacceptor pages 1-2) |
| Terminal oxidases – generate – proton motive force (PMF) | “terminal oxidases… catalyze the four-electron reduction of O2 to water” and “generate the proton motive force for ATP” | Nastasi et al. 2024, doi:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383, Mar 2024 | Strong, general respiratory mechanism; drawn from P. aeruginosa review/primary context (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| PMF – powers – ATP synthesis | “The transmembrane electrochemical gradient… powers the membrane proteins that synthesize ATP” | Lu & Imlay 2021, doi:10.1038/s41579-021-00583-y, https://doi.org/10.1038/s41579-021-00583-y, Jun 2021 | Broad mechanistic support; suitable generic edge from respiration to energy conservation (lu2021whenanaerobesencounter pages 4-6) |
| bo3 oxidase (cyoABCDE) – preferentially expressed under – fully aerobic conditions | “cyoABCDE is maximally induced under fully aerobic conditions” | Nastasi et al. 2024, doi:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277, Jan 2024 | Strong operon-to-environment edge; E. coli-specific but useful for oxygen-regulation node (nastasi2024membraneboundredoxenzyme pages 1-2) |
| bd-I oxidase (cydABX) – preferentially expressed under – intermediate/low O2 | “cydABX [is maximal] at 56% aerobiosis” | Nastasi et al. 2024, doi:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277, Jan 2024 | Strong but assay/regulation-specific; shows oxygen tuning rather than universal requirement (nastasi2024membraneboundredoxenzyme pages 1-2) |
| cbb3 oxidases / CIO – enable growth under – low but finite oxygen | “A cco1/cco2 double mutant… grows at 2% O2, but a triple mutant also lacking CIO cannot” | Nastasi et al. 2024, doi:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383, Mar 2024 | Strong low-O2 growth edge; P. aeruginosa-specific; useful for boundary with microaerophily (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| Cytochrome bd oxidase – has oxygen affinity – Km(O2) 4.0 ± 2.1 µM | “measured O2 affinity for CIO is relatively low (Km O2 = 4.0 ± 2.1 µM)” | Nastasi et al. 2024, doi:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383, Mar 2024 | Quantitative trait-mechanism parameter; P. aeruginosa CIO-specific, not universal for all bd enzymes (nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| Cytochrome bd-II / bo3 – have oxygen affinity – ~2 µM / ~6 µM Km(O2) | “reported Km(O2) values (bd-II Km(O2) ≈ 2 µM; bo3 Km(O2) ≈ 6 µM)” | Nastasi et al. 2024, doi:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277, Jan 2024 | Quantitative support for oxidase differentiation; E. coli-specific (nastasi2024membraneboundredoxenzyme pages 4-7) |
| Cyanide (CHEBI:18420) – inhibits – bo3-type oxidase more strongly than bd-type oxidase | “first component… Kiapp = 0.2 ± 0.1 μM… attributed to bo3-type oxidases” versus “second component… Kiapp = 106 ± 14 μM… attributed to bd-type oxidases” | González-Montalvo et al. 2024, doi:10.3389/fmicb.2024.1479714, https://doi.org/10.3389/fmicb.2024.1479714, Nov 2024 | Strong inhibitor edge; K. aerogenes membranes; supports bd stress-resilience (gonzalezmontalvo2024therespiratorychain pages 5-7) |
| CO – competitively inhibits – terminal oxidases | “Inhibition by CO decreases as [O2] rises, consistent with competitive inhibition: CO competes with O2 for the active site” | Nastasi et al. 2024, doi:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277, Jan 2024 | Strong mechanistic inhibitor edge; E. coli oxidases (nastasi2024membraneboundredoxenzyme pages 4-7) |
| bd-I oxidase – confers resistance to – carbon monoxide during aerobic growth | “bd-I confers high CO resistance” and “bd-I-only cells show minimal growth effect on CO” | Nastasi et al. 2024, doi:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277, Jan 2024 | Strong growth/respiration phenotype edge; E. coli-specific (nastasi2024membraneboundredoxenzyme pages 1-2, nastasi2024membraneboundredoxenzyme pages 4-7) |
| H2S – does not inhibit – P. aeruginosa CIO-dependent O2 consumption | “O2 consumption by CIO is unaltered even in the presence of high levels of H2S” | Nastasi et al. 2024, doi:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383, Mar 2024 | Strong stress-tolerance edge; taxon-specific to CIO in P. aeruginosa (nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| NO – reversibly inhibits – P. aeruginosa CIO, with rapid recovery | “CIO is reversibly inhibited by NO” and “activity recovery after NO exhaustion is full and fast” | Nastasi et al. 2024, doi:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383, Mar 2024 | Strong but taxon-specific; useful for inhibitor/recovery edges (nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| Aerobic respiration / respiratory flavoproteins – generate – ROS (superoxide, H2O2) | “ROS are formed endogenously during aerobic respiration due to activity of respiratory flavoproteins” | Maslovska et al. 2023, doi:10.30970/sbi.1702.716, https://doi.org/10.30970/sbi.1702.716, Jun 2023 | Strong generic edge; good for linking aerobic metabolism to oxidative stress (maslovska2023oxidativestressand pages 1-3) |
| Superoxide dismutase / catalase / peroxidases – eliminate – ROS | “elimination of radicals via ROS-scavenging enzymes — specifically superoxide dismutases (SODs), catalases and peroxidases” | Maslovska et al. 2023, doi:10.30970/sbi.1702.716, https://doi.org/10.30970/sbi.1702.716, Jun 2023 | Strong generic detox edge; broad bacterial support (maslovska2023oxidativestressand pages 1-3) |
| TpxD peroxiredoxin + thioredoxin system – reduce/detoxify – H2O2 | “TpxD plays a significant role in regulating H2O2 levels by facilitating its reduction” and “the thioredoxin (Trx) system… [provides] the electron source” | Hernandez-Morfa et al. 2023, doi:10.3389/fmicb.2023.1269843, https://doi.org/10.3389/fmicb.2023.1269843, Sep 2023 | Strong detox mechanism; S. pneumoniae-specific gene names but broadly representative peroxiredoxin/thioredoxin biology (hernandezmorfa2023theoxidativestress pages 3-4) |
| Oxygen exposure – inactivates – pyruvate formate-lyase (PFL) | “even low levels of O2 inactivate PFL in seconds” | Lu & Imlay 2021, doi:10.1038/s41579-021-00583-y, https://doi.org/10.1038/s41579-021-00583-y, Jun 2021 | Strong boundary-case edge explaining non-aerobic phenotypes; not a positive mechanism for aerobes but critical exclusion edge (lu2021whenanaerobesencounter pages 4-6) |
| Oxygen / endogenous ROS – inactivate – Fe-S enzymes such as fumarase, aconitase | “ROS inactivate solvent-exposed [4Fe–4S] enzymes (fumarase, aconitase, isopropylmalate isomerase)” | Lu & Imlay 2021, doi:10.1038/s41579-021-00583-y, https://doi.org/10.1038/s41579-021-00583-y, Jun 2021 | Strong negative-mechanism edge; important for distinguishing aerobes from oxygen-sensitive anaerobic metabolism (lu2021whenanaerobesencounter pages 9-11) |


*Table: This table lists candidate causal-graph edges for the microbial trait aerobic, emphasizing oxygen as terminal electron acceptor, terminal oxidases, energy conservation, inhibitor responses, and oxidative stress mechanisms. It is useful as a curation-ready starting point for selecting mechanistic nodes and edges with source-backed support.*

### Recent developments (prioritizing 2023–2024)
#### 1) Branched aerobic respiratory chains and stress-adaptive terminal oxidases
Recent work emphasizes that aerobic-capable bacteria often carry **multiple terminal oxidases** with distinct oxygen affinities and inhibitor sensitivities.
- **Pseudomonas aeruginosa**: A 2024 study details a highly branched chain (aa3, cbb3-1, cbb3-2, bo3, plus bd-type CIO) and shows the **cyanide-insensitive oxidase (CIO; bd-type)** supports aerobic respiration under stress; CIO-dependent O2 consumption is “unaltered” by high H2S and CIO expression increases to support growth, while NO inhibition is reversible with fast recovery (nastasi2024cyanideinsensitiveoxidase pages 1-2). The study reports **Km(O2) = 4.0 ± 2.1 µM** for CIO and shows that loss of both cbb3 oxidases plus CIO prevents growth under **2% O2**, connecting terminal oxidase repertoire to microoxic growth (nastasi2024cyanideinsensitiveoxidase pages 2-3).
- **Escherichia coli**: A 2024 study comparing single-oxidase mutants shows strong oxidase-specific stress phenotypes: cytochrome **bd-I** supports **CO-resistant growth/respiration**, whereas bd-II or bo3 are more CO-sensitive; CO inhibition decreases as O2 increases, consistent with competitive inhibition (nastasi2024membraneboundredoxenzyme pages 4-7). Quantitatively, the study reports **Km(O2) ≈ 2 µM (bd-II) and ≈ 6 µM (bo3)** and estimates **Ki(CO) = 2.5 ± 0.2 µM (bd-II) and 8.4 ± 0.7 µM (bo3)** from IC50 behavior (nastasi2024membraneboundredoxenzyme pages 4-7). The associated figures provide the inhibition curves/IC50 analysis (nastasi2024membraneboundredoxenzyme media 58b049ca, nastasi2024membraneboundredoxenzyme media c073ae8e, nastasi2024membraneboundredoxenzyme media d35d334b).

#### 2) Respiratory chain components as antimicrobial targets (real-world application focus)
Multiple 2023–2024 sources position bacterial terminal oxidases—especially **cytochrome bd**—as attractive drug targets due to prokaryote specificity and roles in stress tolerance.
- A 2024 review frames cytochromes bd as often present in pathogens but absent in mitochondria, and notes they can support growth under stressors including H2O2/NO/cyanide/sulfide; this supports the strategy of targeting bacterial energy metabolism (borisov2025carbonmonoxideand pages 5-7).
- In a clinically relevant niche model (urine-like conditions), **Klebsiella aerogenes** shows predominant reliance on bd-type oxidases; cyanide inhibition separates a bo3-like component with low Kiapp (~0.2–0.3 µM) from a bd-like component with much higher Kiapp (~106–123 µM), consistent with bd-type cyanide tolerance and suggesting a mechanistic basis for persistence in hostile host conditions (gonzalezmontalvo2024therespiratorychain pages 5-7).

#### 3) Updated oxidative stress mechanistic integration for aerobic growth
Recent reviews and pathogen-focused studies continue to consolidate the view that aerobic growth capacity is inseparable from managing **endogenous ROS**.
- A 2023 review explicitly links **aerobic respiration (respiratory flavoproteins)** to endogenous ROS formation (superoxide, H2O2, hydroxyl radical) and lists canonical detox enzymes—**SOD, catalase, peroxidases**—plus repair of damaged macromolecules as core defenses (maslovska2023oxidativestressand pages 1-3).
- A 2023 pneumococcal oxidative-stress review provides specific gene-level examples: aeration upregulates **SodA**, which is required for oxidative-stress fitness (reduced growth and paraquat sensitivity in mutants); peroxide detox involves **TpxD peroxiredoxin** and the **thioredoxin system (Trx/TrxR/NADPH)** as electron source (hernandezmorfa2023theoxidativestress pages 3-4).

### Current applications and real-world implementations
1. **Antimicrobial development / drug repurposing (respiration inhibitors):** Terminal oxidases (bd-type and heme–copper oxidases) are increasingly treated as antimicrobial targets because they underwrite ATP production and stress survival, including in host contexts with NO/H2S/CO-like inhibitory conditions (borisov2025carbonmonoxideand pages 5-7, nastasi2024cyanideinsensitiveoxidase pages 1-2).
2. **Clinical niche metabolism and pathogen persistence:** Pathogens or opportunists can rewire aerobic respiration in host-like media; in urine-like media, K. aerogenes shows evidence consistent with bd oxidases being major terminal oxidases, motivating respiratory-chain nodes/edges in infection models (gonzalezmontalvo2024therespiratorychain pages 5-7).
3. **Assay/diagnostics relevance:** Whole-cell and membrane oxygraphy plus inhibitor titration (CO, cyanide) are practical experimental factors that operationalize aerobic-respiration phenotypes by separating terminal oxidase contributions (nastasi2024membraneboundredoxenzyme pages 4-7, gonzalezmontalvo2024therespiratorychain pages 5-7).

### Quantitative statistics/data points suitable for curation
- **P. aeruginosa CIO (bd-type):** Km(O2) = **4.0 ± 2.1 µM** (nastasi2024cyanideinsensitiveoxidase pages 2-3).
- **E. coli oxidase O2 affinities used in inhibition analysis:** Km(O2) ≈ **2 µM** (bd-II) and ≈ **6 µM** (bo3) (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme media c073ae8e, nastasi2024membraneboundredoxenzyme media d35d334b).
- **E. coli CO inhibition kinetics:** Ki(CO) = **2.5 ± 0.2 µM** (bd-II) and **8.4 ± 0.7 µM** (bo3) derived from competitive inhibition fits (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme media c073ae8e, nastasi2024membraneboundredoxenzyme media d35d334b).
- **K. aerogenes terminal oxidase cyanide sensitivity partitioning:** bo3-like fraction Kiapp **0.2 ± 0.1 µM** (LB) / **0.3 ± 0.05 µM** (urine-like), vs bd-like fraction Kiapp **106 ± 14 µM** (LB) / **123 ± 2 µM** (urine-like) (gonzalezmontalvo2024therespiratorychain pages 5-7).

### Expert opinions / authoritative synthesis
- The Nature Reviews Microbiology synthesis emphasizes that oxygen sensitivity is graded and that apparent anaerobiosis can arise from vulnerability of a limited set of key enzymes, rather than absence of oxidative defenses; this supports modeling aerobic trait causality with both **positive** (O2 respiration machinery) and **negative constraints** (O2-sensitive enzymes/ROS damage) (lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 1-3).
- Mechanistic reviews of oxygen as an acceptor and of CO effects on prokaryotic energy metabolism emphasize that terminal oxidase superfamilies (heme–copper vs bd-type) differ in proton pumping, oxygen affinity, and inhibitor susceptibility, implying that “aerobic” is mechanistically heterogeneous and best represented as a graph with optional branches (borisov2015oxygenasacceptor pages 1-2, borisov2025carbonmonoxideand pages 5-7).

### Warnings / non-curation flags (TraitMech quality control)
1. **Do not equate “aerobic” with a single terminal oxidase gene.** The evidence strongly supports **branched** respiratory chains where different oxidases dominate under different O2 and inhibitor regimes (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024membraneboundredoxenzyme pages 1-2).
2. **Taxon-specific edges require careful scoping.** CIO-specific properties (e.g., heme composition differences; H2S/NO tolerance) are strong in P. aeruginosa but should be curated as conditional or taxon-scoped edges (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024cyanideinsensitiveoxidase pages 1-2).
3. **Definitions for facultative/microaerophilic/aerotolerant are not provided as glossary-style statements in the retrieved excerpts.** The mechanistic distinctions are supportable, but if strict dictionary definitions are required in the YAML, an additional dedicated source may be needed; treat such nodes as label-only for now (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 13-15).
4. **Some “applications” claims are review-level.** Drug-target assertions about bd oxidases are supported by review synthesis but may need primary inhibitor/efficacy papers for curation of “inhibits → kills” edges (borisov2025carbonmonoxideand pages 5-7, borisov2025carbonmonoxideand pages 20-21).

---

## DOI-first bibliography (with dates and URLs)
- Nastasi MR, Caruso L, Giordano F, et al. *Cyanide Insensitive Oxidase Confers Hydrogen Sulfide and Nitric Oxide Tolerance to Pseudomonas aeruginosa Aerobic Respiration.* **Antioxidants**. **Mar 2024**. https://doi.org/10.3390/antiox13030383 (nastasi2024cyanideinsensitiveoxidase pages 2-3)
- Nastasi MR, Borisov VB, Forte E. *Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant Escherichia coli Growth and Respiration.* **Int J Mol Sci**. **Jan 2024**. https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7)
- González-Montalvo MA, Sorescu JM, Baltes G, Juárez O, Tuz K. *The respiratory chain of Klebsiella aerogenes in urine-like conditions: critical roles of NDH-2 and bd-terminal oxidases.* **Front Microbiol**. **Nov 2024**. https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 5-7)
- Hernandez-Morfa M, Olivero NB, Zappia VE, et al. *The oxidative stress response of Streptococcus pneumoniae: its contribution to both extracellular and intracellular survival.* **Front Microbiol**. **Sep 2023**. https://doi.org/10.3389/fmicb.2023.1269843 (hernandezmorfa2023theoxidativestress pages 3-4)
- Maslovska O, Komplikevych S, Hnatush S. *Oxidative stress and protection against it in bacteria.* **Studia Biologica**. **Jun 2023**. https://doi.org/10.30970/sbi.1702.716 (maslovska2023oxidativestressand pages 1-3)
- Lu Z, Imlay JA. *When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.* **Nat Rev Microbiol**. **Jun 2021**. https://doi.org/10.1038/s41579-021-00583-y (lu2021whenanaerobesencounter pages 4-6)
- Borisov VB, Verkhovsky MI. *Oxygen as Acceptor.* **EcoSal Plus**. **Oct 2015**. https://doi.org/10.1128/ecosalplus.esp-0012-2015 (borisov2015oxygenasacceptor pages 1-2)
- Borisov VB, Forte E. *Carbon Monoxide and Prokaryotic Energy Metabolism.* **Int J Mol Sci**. **Mar 2025**. https://doi.org/10.3390/ijms26062809 (borisov2025carbonmonoxideand pages 5-7)

### Linked quantitative figure evidence
- CO inhibition/IC50 curves and Ki derivations for E. coli bd-II and bo3 oxidases (Figures 3–4) and CO resistance of bd-I (Figure 2) (nastasi2024membraneboundredoxenzyme media 58b049ca, nastasi2024membraneboundredoxenzyme media c073ae8e, nastasi2024membraneboundredoxenzyme media d35d334b).


References

1. (borisov2015oxygenasacceptor pages 1-2): Vitaliy B. Borisov and Michael I. Verkhovsky. Oxygen as acceptor. EcoSal Plus, Oct 2015. URL: https://doi.org/10.1128/ecosalplus.esp-0012-2015, doi:10.1128/ecosalplus.esp-0012-2015. This article has 118 citations.

2. (lu2021whenanaerobesencounter pages 4-6): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

3. (lu2021whenanaerobesencounter pages 1-3): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 13-15): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

5. (nastasi2024cyanideinsensitiveoxidase pages 2-3): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

6. (lu2021whenanaerobesencounter pages 16-17): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

7. (nastasi2024membraneboundredoxenzyme pages 1-2): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

8. (lu2021whenanaerobesencounter pages 8-9): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

9. (nastasi2024cyanideinsensitiveoxidase pages 1-2): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

10. (gonzalezmontalvo2024therespiratorychain pages 5-7): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

11. (nastasi2024membraneboundredoxenzyme pages 4-7): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

12. (nastasi2024cyanideinsensitiveoxidase pages 16-17): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

13. (lu2021whenanaerobesencounter pages 9-11): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

14. (maslovska2023oxidativestressand pages 1-3): Olha Maslovska, Solomiia Komplikevych, and Svitlana Hnatush. Oxidative stress and protection against it in bacteria. Studia Biologica, 17:153-172, Jun 2023. URL: https://doi.org/10.30970/sbi.1702.716, doi:10.30970/sbi.1702.716. This article has 16 citations.

15. (bastos2025whatdowe pages 7-8): Mírian Letícia Carmo Bastos, Gleison Gonçalves Ferreira, Isis de Oliveira Kosmiscky, Ieda Maria Louzada Guedes, José Augusto Pereira Carneiro Muniz, Liliane Almeida Carneiro, Ísis Lins de Carvalho Peralta, Marcia Nazaré Miranda Bahia, Cintya de Oliveira Souza, and Maria Fâni Dolabela. What do we know about staphylococcus aureus and oxidative stress? resistance, virulence, new targets, and therapeutic alternatives. Toxics, 13:390, May 2025. URL: https://doi.org/10.3390/toxics13050390, doi:10.3390/toxics13050390. This article has 16 citations.

16. (hernandezmorfa2023theoxidativestress pages 3-4): Mirelys Hernandez-Morfa, Nadia B. Olivero, Victoria E. Zappia, German E. Piñas, Nicolas M. Reinoso-Vizcaino, Melina B. Cian, Mariana Nuñez-Fernandez, Paulo R. Cortes, and Jose Echenique. The oxidative stress response of streptococcus pneumoniae: its contribution to both extracellular and intracellular survival. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1269843, doi:10.3389/fmicb.2023.1269843. This article has 32 citations and is from a peer-reviewed journal.

17. (lu2021whenanaerobesencounter pages 6-8): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

18. (nastasi2024membraneboundredoxenzyme media 58b049ca): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

19. (nastasi2024membraneboundredoxenzyme media c073ae8e): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

20. (nastasi2024membraneboundredoxenzyme media d35d334b): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

21. (borisov2025carbonmonoxideand pages 5-7): Vitaliy B. Borisov and Elena Forte. Carbon monoxide and prokaryotic energy metabolism. International Journal of Molecular Sciences, 26:2809, Mar 2025. URL: https://doi.org/10.3390/ijms26062809, doi:10.3390/ijms26062809. This article has 8 citations.

22. (borisov2025carbonmonoxideand pages 20-21): Vitaliy B. Borisov and Elena Forte. Carbon monoxide and prokaryotic energy metabolism. International Journal of Molecular Sciences, 26:2809, Mar 2025. URL: https://doi.org/10.3390/ijms26062809, doi:10.3390/ijms26062809. This article has 8 citations.