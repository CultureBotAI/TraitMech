---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:39:35.870151'
end_time: '2026-08-04T00:54:01.787366'
duration_seconds: 865.92
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively aerobic
  trait_identifier: METPO:1000608
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_aerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An oxygen preference in which growth can occur without oxygen but is
    capable of aerobic growth.
  parent_traits: METPO:1000601
  synonyms: facultative, facultative aerobe
  evidence_summary: 'PMID:21413255: preferentially utilize oxygen as a terminal electron
    acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505:
    A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism
    example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively
    aerobic.)'
  causal_graph_summary: 'facultative_aerobe_oxygen_flexible_growth: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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
- **Trait label:** facultatively aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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


# Curation-focused research report: facultatively aerobic

## 1. Scope summary

**Trait:** “facultatively aerobic”  
**Identifier:** **METPO:1000608**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Definition supplied:** growth can occur without oxygen, but aerobic growth is also possible.  
**Parent:** METPO:1000601  
**Synonyms:** facultative; facultative aerobe.

The trait is best represented as an **organism-level, experimentally demonstrated oxygen-flexible growth phenotype**, not as the presence of any single gene. Its two indispensable observations are:

1. growth under effectively anoxic conditions; and
2. growth in the presence of O₂ through an aerobic mode.

An authoritative review describes facultative organisms as able to grow “in the presence or in the absence of oxygen” and explains that they consume oxygen through terminal oxygen reductases when it is available. Thus, aerobic respiration plus an alternative anoxic energy/redox-balancing route is a strong mechanistic model, but neither module alone proves the phenotype (andre2021theselectiveadvantage pages 2-4).

### Boundary cases

- **Obligate aerobe:** requires O₂ for growth; fails the anoxic-growth criterion.
- **Obligate anaerobe:** grows without O₂ and may possess oxygen-detoxification enzymes, but does not conduct sustained aerobic growth. Oxygen survival or O₂ scavenging is insufficient.
- **Aerotolerant anaerobe:** tolerates oxygen while retaining essentially fermentative metabolism; tolerance is not equivalent to aerobic growth.
- **Microaerophile:** requires or preferentially grows at low O₂ and may be inhibited at atmospheric O₂. This is an oxygen-concentration optimum, not necessarily bidirectional oxic/anoxic growth.
- **Facultatively anaerobic:** commonly used for the same biological phenotype, but linguistically emphasizes anaerobic capability. The supplied METPO term emphasizes the capacity for aerobic growth despite oxygen-independent growth.
- **Respiro-fermentative/overflow metabolism:** simultaneous fermentation and respiration in oxygenated cultures does not by itself establish growth at zero O₂.
- **Nanaerobic or trace-oxygen respiration:** growth at extremely low O₂ remains oxygen-dependent unless genuine zero-O₂ growth is demonstrated.

### Recommended phenotype assay

Curate the trait only where matched cultures demonstrate biomass increase, colony formation, or serially transferable growth under both controlled oxic and anoxic conditions. Record medium, electron donor, alternative acceptors, O₂ concentration or redox indicator, temperature, pH, growth rate/yield, and whether anoxic growth is fermentative or respiratory. Oxygen consumption alone, genomic prediction, short-term viability, catalase positivity, or growth under an undefined “sealed” condition should not be sufficient.

## 2. Mechanistic interpretation

A robust generic graph has two convergent branches.

**Oxic branch:** O₂ availability → aerobic respiratory chain → terminal oxidase-mediated O₂ reduction to water → proton-motive force → ATP synthesis → aerobic growth. Terminal oxygen reductases include heme-copper oxidases and cytochrome bd-family oxidases; their distribution and energetic efficiencies are taxon-specific (andre2021theselectiveadvantage pages 2-4). A 2024 synthesis reports that *E. coli* may obtain approximately **15 ATP per glucose by aerobic respiration versus 4 ATP by anaerobic fermentation**, while noting that oxygen adaptation also reflects avoidance of O₂-sensitive enzyme damage, not simply energetic yield. The same analysis reports approximate proton-pumping stoichiometries of 4 H⁺/O₂ for aa₃/bo₃ oxidases, 2 H⁺/O₂ for cbb₃ oxidases, and no direct pumping by bd oxidases, although bd oxidases can still generate proton motive force through vectorial chemistry (mrnjavac2024theradicalimpact pages 15-17).

**Anoxic branch:** O₂ depletion → redox/O₂ sensing → induction of fermentation and/or anaerobic respiration → NAD⁺ regeneration and/or ion-gradient formation → ATP generation → growth without O₂. In enteric bacteria, nitrate, fumarate, nitrite, trimethylamine-N-oxide and related compounds can serve as alternative respiratory acceptors; fermentative growth instead uses internal organic acceptors to maintain redox balance (gunsalus1994aerobicanaerobicgeneregulation pages 3-5).

**Protection branch:** O₂ exposure also creates superoxide, peroxide and damage to oxygen-sensitive enzymes. Superoxide dismutase, catalase, peroxidases, repair systems and some terminal oxidases improve oxygen tolerance. These defenses are enabling rather than defining: strict anaerobes can carry substantial O₂-defense machinery without becoming facultative aerobes. Recent evolutionary analysis further argues that adaptation to oxygen-sensitive enzymes and O₂-dependent biosynthesis preceded or accompanied the emergence of aerobic respiratory chains (mrnjavac2024theradicalimpact pages 15-17, mrnjavac2024theradicalimpact pages 7-9).

## 3. Candidate nodes grouped by type

### Environmental and experimental factors

- Molecular oxygen — **CHEBI:15379**
- Oxic condition — label-only pending verified ENVO mapping
- Anoxic condition — label-only pending verified ENVO mapping
- Dissolved oxygen concentration
- Oxygen gradient / microoxic transition
- Redox potential
- Carbon-source identity and concentration
- Electron-acceptor availability
- Iron limitation
- Protonophore/uncoupler CCCP — useful perturbation node, not part of the native phenotype
- Carbon monoxide — terminal-oxidase inhibitor/perturbation, taxon- and oxidase-specific

### Chemicals, cofactors and metabolites

- Water — **CHEBI:15377**
- ATP — **CHEBI:15422**
- ADP, inorganic phosphate
- NAD⁺ — **CHEBI:57540**
- NADH
- Ubiquinone/ubiquinol and menaquinone/menaquinol pools
- Nitrate — **CHEBI:17632**
- Fumarate — **CHEBI:18012**
- Nitrite, TMAO, DMSO — retain label-only until identifiers are verified
- Glucose, pyruvate, acetyl-CoA
- Fermentation products: lactate, acetate, ethanol, formate and succinate
- Reactive oxygen species: superoxide, hydrogen peroxide, hydroxyl radical
- Iron–sulfur clusters, especially FNR [4Fe–4S] and O₂-converted [2Fe–2S] forms

### Genes, proteins and complexes

These should generally be represented as **taxon-specific exemplars**, not universal requirements.

- **FNR**, global O₂-responsive transcription factor
- **ArcB**, membrane-associated sensor kinase
- **ArcA**, response regulator; phosphorylated ArcA as the active regulatory state
- NADH dehydrogenases
- Quinol/cytochrome terminal oxidases: cytochrome bo₃, bd-I, bd-II, aa₃, cbb₃ and related complexes
- F₁F₀ ATP synthase
- Nitrate reductase NarGHJI
- Fumarate reductase FrdABCD
- Nitrite, TMAO and DMSO reductases
- Pyruvate-formate lyase, lactate dehydrogenase, alcohol dehydrogenase, phosphotransacetylase/acetate kinase
- Superoxide dismutases, catalases and peroxidases
- Isocitrate dehydrogenase and other TCA-cycle enzymes regulated by ArcA/FNR

### Pathways and biological processes

- Aerobic respiration — candidate **GO:0009060**
- Aerobic electron-transport chain — candidate **GO:0019646**
- Anaerobic respiration — candidate **GO:0009061**
- Fermentation — candidate **GO:0006113**
- Proton-motive-force generation — candidate **GO:0015992**
- ATP synthesis coupled to transmembrane transport — use a verified GO term at implementation time
- TCA cycle, glycolysis, mixed-acid fermentation
- NAD⁺ regeneration
- Cellular redox homeostasis
- Reactive-oxygen-species detoxification
- Oxygen sensing and transcriptional metabolic switching
- Aerobic growth and anoxic growth as assay-level outcome nodes

### Cellular localizations

- Cytoplasmic membrane: respiratory complexes, quinone pool, ArcB, F₁F₀ ATP synthase
- Cytoplasm: FNR, ArcA, glycolytic and fermentative enzymes
- Periplasm/extracytoplasmic side: relevant domains of respiratory reductases and proton translocation, architecture dependent

### Taxa

- *Escherichia coli*: principal mechanistic exemplar
- Enterobacterales including *Citrobacter freundii*, *Klebsiella pneumoniae* and *Serratia marcescens*: recent ArcA infection evidence
- *Anoxybacillus kamchatkensis*: supplied organism-level example; **NCBITaxon identifier should be verified before curation**

## 4. Candidate causal edges

The following table is suitable as a starting point for `facultatively_aerobic.yaml`. It deliberately separates broadly defensible biochemical edges from *E. coli*/Enterobacterales-specific regulatory mechanisms.

| subject | predicate | object | proposed grounding | best DOI/date | short supporting snippet | evidence strength/taxon limitation |
|---|---|---|---|---|---|---|
| molecular oxygen (O2) | serves_as_terminal_electron_acceptor_for | terminal oxidase-dependent aerobic respiration | CHEBI:15379 → terminal oxidase (GO:0009055 for electron transfer activity, terminal oxidase label-only) | 10.1111/cmi.13338 (2021-04) | “terminal oxygen reductases reduce dioxygen to water” in facultative anaerobes/pathogens (andre2021theselectiveadvantage pages 2-4) | **Moderate**; review-level, broad bacterial scope rather than one taxon-specific experiment |
| terminal oxidases | catalyze_reduction_of | O2 to H2O | terminal oxidase label-only; O2 CHEBI:15379; water CHEBI:15377 | 10.3390/ijms25021277 (2024-01) | “The terminal oxidases of bacterial aerobic respiratory chains … catalyze the four-electron reduction of O2 to 2H2O” | **Strong** for oxidase chemistry; taxon example in *E. coli* cytochrome bd-I/bo3/bd-II study |
| aerobic respiratory electron transfer | generates | proton motive force | GO:0019646 aerobic electron transport chain; proton motive force GO:0015992 | 10.1016/j.bbabio.2015.11.001 (2016-03) | respiratory chains generate a “proton-motive force that is used by ATP synthase to synthesize ATP” | **Moderate**; broad bacterial respiration review, not trait-exclusive |
| proton motive force | drives | F1Fo-ATP synthase ATP production | proton motive force GO:0015992; ATP synthase GO:0046933; ATP CHEBI:15422 | 10.3390/ijms24065417 (2023-03) | F1Fo-ATP synthases “couple either ATP synthesis from ADP and phosphate … to a transmembrane electrochemical gradient of protons” | **Moderate**; broad bacterial enzyme review |
| absence of oxygen (anoxia) | activates | FNR | FNR label-only; anoxia ENVO label-only | 10.1046/j.1365-2958.1997.4731841.x (1997-07) | “In the absence of oxygen, FNR changes from the inactive to the active state” | **Strong**; canonical *E. coli* mechanism |
| O2 exposure | converts_and_inactivates | FNR [4Fe-4S] cluster | FNR label-only; [4Fe-4S] cluster label-only | 10.1073/pnas.94.12.6087 (1997-06) | “[4Fe-4S] to [2Fe-2S] conversion with loss of biological activity” | **Strong**; direct biochemical experiment in *E. coli* FNR |
| active FNR | activates_expression_of | anaerobic respiration / fermentation genes | FNR label-only; anaerobic respiration GO:0009061; fermentation GO:0006113 | 10.3390/inorganics11120450 (2023-11) | FNR is the “master switch for the transition between anaerobic and aerobic respiration, controlling the expression of >300 genes in response to O2 availability” | **Strong** for global regulation; exact downstream genes vary by taxon/context |
| quinone/quinol redox state | modulates | ArcB sensor kinase activity | quinone label-only; ArcB label-only | 10.1128/mmbr.00110-21 (2022-06) | “The bacterial quinone pool is the primary modulator of ArcAB activity” (brown2022thearcabtwocomponent pages 3-4) | **Moderate**; review synthesis, mechanism still debated in details |
| ArcB | phosphorylates/activates | ArcA | ArcB label-only; ArcA label-only | 10.1128/mmbr.00110-21 (2022-06) | ArcAB is “composed of sensor kinase ArcB and response regulator ArcA” (brown2022thearcabtwocomponent pages 3-4) | **Moderate**; phosphorylation step canonical but snippet is review-level |
| ArcA-P | represses | aerobic carbon oxidation pathways | ArcA label-only; carbon oxidation label-only | 10.1371/journal.pgen.1003839 (2013-10) | “under anaerobic conditions … carbon oxidation pathways that recycle redox carriers via respiration are transcriptionally repressed by ArcA” | **Strong**; direct *E. coli* regulon study |
| nitrate / fumarate | enable | anaerobic respiration when O2 is absent | nitrate CHEBI:17632; fumarate CHEBI:18012; anaerobic respiration GO:0009061 | 10.1016/S0005-2728(97)00034-0 (1997-07) | “In facultatively anaerobic bacteria, electron acceptors often …” with nitrate and fumarate reductive pathways described | **Moderate**; foundational review centered on *E. coli* energetics/regulation |
| fermentation pathways | regenerate | NAD+ | fermentation GO:0006113; NAD+ CHEBI:57540 | 10.1186/s13068-017-0867-0 (2017-07) | fermentative pathways “regenerate NAD+ … to enable continuation of metabolism under micro-aerobic and anaerobic” conditions | **Moderate**; model + experimental validation in *E. coli* context |
| NAD+ regeneration by fermentation | enables | anoxic growth | NAD+ CHEBI:57540; growth label-only; anoxia ENVO label-only | 10.1186/s13068-017-0867-0 (2017-07) | the same source ties NAD+ regeneration to continuation of metabolism under anaerobic conditions | **Moderate**; inferred growth-enabling edge from metabolic continuation |
| superoxide dismutase / catalase / peroxidases | protect_against | ROS during oxygen exposure | SOD label-only; catalase EC:1.11.1.6; peroxidase label-only; ROS CHEBI label uncertain | 10.3390/antiox10060839 (2021-05) | bacteria use ROS scavenging enzymes “such as superoxide dismutases, catalases, and peroxidases” to prevent oxidative stress | **Strong** for ROS defense generally; not unique to facultative aerobes |
| facultatively aerobic physiology | results_from_combination_of | aerobic respiration with O2 + anaerobic growth without O2 | METPO:1000608; aerobic respiration GO:0009060; anaerobic growth label-only | 10.1111/cmi.13338 (2021-04) | facultative anaerobes “have the unique ability to grow in the presence or in the absence of oxygen” (andre2021theselectiveadvantage pages 2-4) | **Strong** for phenotype boundary; wording from host-pathogen review, broad taxa |
| ArcA response to impaired respiratory activity | promotes_shift_to | fermentation independent of oxygen availability | ArcA label-only; fermentation GO:0006113 | 10.1128/mbio.01448-23 (2023-10) | CCCP experiments “support an ArcA-mediated shift to fermentation independent of oxygen availability” (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3) | **Moderate-strong**; recent direct phenotype evidence, but infection-context and taxon-specific to Enterobacterales |


*Table: This table summarizes compact, curation-ready candidate causal edges for the facultatively aerobic trait, emphasizing oxygen respiration, anaerobic switching, regulatory control, and oxidative-stress protection. It is designed to help prioritize which mechanism statements are well supported versus broader or more taxon-limited.*

### Core graph recommendation

For a compact, taxon-neutral TraitMech graph, prioritize:

1. O₂ availability → enables aerobic respiration.
2. Aerobic respiratory chain → transfers electrons to terminal oxidase.
3. Terminal oxidase → reduces O₂ to H₂O.
4. Respiratory electron transfer → generates proton motive force.
5. Proton motive force → drives ATP synthesis.
6. ATP production → supports aerobic growth.
7. O₂ absence → requires oxygen-independent redox balancing/energy conservation.
8. Fermentation and/or alternative-acceptor respiration → supports anoxic growth.
9. ROS defense → protects cellular function during oxygen exposure.
10. Aerobic growth + anoxic growth → realizes **METPO:1000608**.

FNR and ArcAB should be placed in an **Enterobacterales/*E. coli* mechanistic branch**, rather than asserted as universal determinants. FNR and ArcAB are prominent sensors, but oxygen-responsive regulation has evolved multiple times and uses different regulators in other lineages (mrnjavac2024theradicalimpact pages 7-9, price2021bacterialapproachesto pages 11-12).

## 5. Recent developments, applications and quantitative findings

### 5.1 Oxygen sensing and metabolic regulation

A 2023 FNR study describes *E. coli* FNR as the master switch between aerobic and anaerobic respiration, controlling **more than 300 genes** in response to O₂ through reaction of its [4Fe–4S] cofactor. This supports anoxia → active FNR → anaerobic program, but FNR also senses nitric oxide, so downstream responses cannot always be attributed solely to oxygen.

The current expert view of ArcAB is more nuanced than a simple oxygen sensor. ArcAB senses respiratory activity principally through the oxidation state and behavior of the quinone pool; it therefore responds to oxygen consumption, electron flow and cellular energy demand rather than directly measuring extracellular O₂. Current reviews also caution that the molecular details of quinone–ArcB regulation remain contested and that ArcAB can function under aerobic conditions (brown2022thearcabtwocomponent pages 3-4).

### 5.2 Infection biology

In a 2023 study of Gram-negative bacteremia, ArcA promoted fitness in *C. freundii*, *K. pneumoniae* and *S. marcescens*, but not detectably in *E. coli*, demonstrating that even highly conserved regulators have species-dependent phenotypic effects. ArcA proteins were approximately **93.70–99.58% identical** among examined clinical strains, yet the infection phenotype was only semi-conserved (brown2023conservedmetabolicregulator pages 1-3).

The same study linked ArcA to rapid in-host replication and respiratory adaptation. Reported murine spleen population-doubling times were approximately **66 min for C. freundii, 39 min for K. pneumoniae and 61 min for S. marcescens**. Physiological oxygen was reported to decline from about **13.2% in arterial blood to 5.4% in liver**, illustrating the gradients encountered during dissemination (brown2023conservedmetabolicregulator pages 12-14). ArcA deletion caused a **37.7-fold** increase in serum susceptibility in *C. freundii*; wild types exhibited **44–138-fold** greater survival than corresponding arcA mutants under polymyxin-B challenge across the three species (brown2023conservedmetabolicregulator pages 8-10). These findings are important applications of oxygen-flexible regulation but are not generic defining edges for the METPO trait.

### 5.3 Biotechnology

Facultative organisms are industrially useful because biomass can first be accumulated aerobically and product formation then redirected under oxygen limitation. Recent work has engineered an obligately fermentative *E. coli* background with selected respiratory modules, allowing oxygen to dispose of surplus electrons while carbon flux remains directed toward lactate or isobutanol. This demonstrates that respiration and fermentation can be modularly combined to expand feasible substrate–product redox balances (DOI **10.1038/s41467-024-51029-x**, August 2024).

Large-scale *E. coli* bioreactors contain oxygen, substrate and mixing gradients. A 2024 industrially oriented study found that deleting **pta/poxB** or increasing TCA-cycle entry through **gltA** overexpression reduced acetate overflow, with the preferred intervention depending on carbon limitation and glucose pulses (DOI **10.3389/fbioe.2024.1339054**, February 2024). These are implementations of oxygen-responsive metabolic engineering, not evidence that the deleted genes determine facultative aerobiosis.

### 5.4 Terminal-oxidase specialization

A 2024 *E. coli* comparison found that cells expressing only cytochrome bd-I retained growth and respiration much better under carbon monoxide than cells expressing only bd-II or bo₃. This shows that alternative terminal oxidases confer robustness to inhibitors and changing respiratory environments, but no individual oxidase is expected to be universally necessary for the trait (DOI **10.3390/ijms25021277**, January 2024).

### 5.5 Environmental engineering

Alternating microaerobic/anoxic operation is used in wastewater nitrogen removal and anaerobic digestion. Facultative populations can consume infiltrating oxygen, remove organic substrates and protect obligate anaerobic partners. Such community effects are real-world consequences of oxygen flexibility, but community performance must not be converted directly into organism-level growth edges without isolate or resolved population evidence.

## 6. Expert synthesis

The most defensible causal interpretation is **metabolic redundancy coordinated by redox sensing**. Oxygen permits a high-potential terminal acceptor and efficient chemiosmotic ATP production; when oxygen disappears, cells redirect carbon and electrons toward fermentation or alternative respiratory acceptors. Regulatory systems prevent incompatible or wasteful pathways from operating at full strength simultaneously and coordinate redox balance, biosynthesis and stress defense. Reviews emphasize that respiration dissipates reductant and produces an electrochemical gradient, while regulatory systems prioritize energetically favorable acceptors and limit toxic by-products (andre2021theselectiveadvantage pages 2-4, brown2022thearcabtwocomponent pages 3-4).

However, “facultatively aerobic” is not equivalent to possession of FNR, ArcAB, cytochrome bd, nitrate reductase or catalase. The graph should therefore distinguish:

- **phenotype-defining outcomes:** aerobic and anoxic growth;
- **near-universal biochemical modules:** oxygen reduction, electron transport, redox balancing and ATP production;
- **alternative mechanisms:** fermentation versus anaerobic respiration;
- **taxon-specific implementations:** FNR/ArcAB regulons, particular oxidases and reductases;
- **supporting adaptations:** ROS defense and oxygen-stable biosynthetic pathways.

## 7. Warnings: claims not yet ready for TraitMech curation

1. **Do not curate FNR or ArcAB as universally required.** Their evidence is strongest in Proteobacteria, especially *E. coli* and Enterobacterales.
2. **Do not equate oxygen tolerance with aerobic growth.** Catalase, SOD, peroxidases or O₂-reducing detoxification enzymes can occur in obligate anaerobes.
3. **Do not require nitrate or fumarate respiration.** Fermentation alone can support the oxygen-independent branch; alternative acceptors depend on species and medium.
4. **Do not require a particular terminal oxidase.** bo₃, bd, aa₃, cbb₃ and other oxidases differ among taxa and oxygen regimes.
5. **Treat quantitative ATP yields as model- and condition-dependent.** The 15-versus-4 ATP comparison is useful mechanistic context, not a universal stoichiometry (mrnjavac2024theradicalimpact pages 15-17).
6. **Do not infer the trait from genome content alone.** Gene presence does not establish expression, pathway completeness or growth under both conditions.
7. **Avoid making “oxygen → ROS → defense → aerobic growth” sufficient.** ROS defenses are enabling and may not overcome direct O₂ damage to PFL, PFOR, nitrogenase or other sensitive enzymes (mrnjavac2024theradicalimpact pages 15-17).
8. **Mark ArcA infection edges as taxon- and assay-specific.** ArcA phenotypes differed among closely related Enterobacterales and depended on iron limitation, membrane stress and the murine infection model (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3).
9. **Do not curate CO resistance, polymyxin resistance or industrial acetate overflow as core trait edges.** They are informative applications or perturbation phenotypes.
10. **Verify all ontology accessions at implementation time.** The report supplies only identifiers with high confidence; genes/proteins should use taxon-specific UniProt accessions, and reactions should receive Rhea/EC identifiers only after selecting the exact enzyme and direction.
11. **The supplied *Anoxybacillus kamchatkensis* evidence is organism-description evidence, not a complete mechanism.** Its DOI is **10.1007/s00792-005-0479-7**; strain-level assays and genomic identifiers should be checked before adding organism-specific nodes.

## 8. DOI-first bibliography

1. Mrnjavac N, et al. “The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third.” *FEBS Letters* 598:1692–1714. **May 2024.** https://doi.org/10.1002/1873-3468.14906 (mrnjavac2024theradicalimpact pages 15-17, mrnjavac2024theradicalimpact pages 7-9)
2. Schulz-Mirbach H, et al. “Engineering new-to-nature biochemical conversions by combining fermentative metabolism with respiratory modules.” *Nature Communications* 15. **August 2024.** https://doi.org/10.1038/s41467-024-51029-x
3. Nastasi MR, Borisov VB, Forte E. “Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant Escherichia coli Growth and Respiration.” *International Journal of Molecular Sciences* 25:1277. **January 2024.** https://doi.org/10.3390/ijms25021277
4. Gecse G, et al. “Minimizing acetate formation from overflow metabolism in Escherichia coli.” *Frontiers in Bioengineering and Biotechnology* 12. **February 2024.** https://doi.org/10.3389/fbioe.2024.1339054
5. Brown AN, et al. “Conserved metabolic regulator ArcA responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia.” *mBio* 14. **October 2023.** https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 8-10, brown2023conservedmetabolicregulator pages 1-3)
6. Crack JC, et al. “Probing the Reactivity of [4Fe-4S] FNR with O₂ and NO.” *Inorganics* 11:450. **November 2023.** https://doi.org/10.3390/inorganics11120450
7. Zharova TV, Grivennikova VG, Borisov VB. “F1·Fo ATP Synthase/ATPase: Contemporary View on Unidirectional Catalysis.” *International Journal of Molecular Sciences* 24:5417. **March 2023.** https://doi.org/10.3390/ijms24065417
8. Brown AN, et al. “The ArcAB Two-Component System: Function in Metabolism, Redox Control, and Infection.” *Microbiology and Molecular Biology Reviews* 86. **June 2022.** https://doi.org/10.1128/mmbr.00110-21 (brown2022thearcabtwocomponent pages 3-4, brown2022thearcabtwocomponent pages 20-23)
9. André AC, Debande L, Marteyn BS. “The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.” *Cellular Microbiology* 23. **April 2021.** https://doi.org/10.1111/cmi.13338 (andre2021theselectiveadvantage pages 7-8, andre2021theselectiveadvantage pages 2-4)
10. Price EE, Román-Rodríguez F, Boyd JM. “Bacterial approaches to sensing and responding to respiration and respiration metabolites.” *Molecular Microbiology* 116:1009–1021. **August 2021.** https://doi.org/10.1111/mmi.14795 (price2021bacterialapproachesto pages 11-12)
11. Park DM, et al. “The Bacterial Response Regulator ArcA Uses a Diverse Binding Site Architecture to Regulate Carbon Oxidation Globally.” *PLoS Genetics* 9:e1003839. **October 2013.** https://doi.org/10.1371/journal.pgen.1003839
12. Gunsalus RP, Park S-J. “Aerobic-anaerobic gene regulation in Escherichia coli: control by the ArcAB and Fnr regulons.” *Research in Microbiology* 145:437–450. **1994.** https://doi.org/10.1016/0923-2508(94)90092-2 (gunsalus1994aerobicanaerobicgeneregulation pages 3-5)
13. Khoroshilova N, et al. “Iron-sulfur cluster disassembly in the FNR protein of Escherichia coli by O₂.” *PNAS* 94:6087–6092. **June 1997.** https://doi.org/10.1073/pnas.94.12.6087
14. Unden G, Schirawski J. “The oxygen-responsive transcriptional regulator FNR of Escherichia coli.” *Molecular Microbiology* 25:205–210. **July 1997.** https://doi.org/10.1046/j.1365-2958.1997.4731841.x
15. Unden G, Bongaerts J. “Alternative respiratory pathways of Escherichia coli.” *Biochimica et Biophysica Acta* 1320:217–234. **July 1997.** https://doi.org/10.1016/S0005-2728(97)00034-0
16. Kevbrin VV, et al. “Anoxybacillus kamchatkensis sp. nov., a novel thermophilic facultative aerobic bacterium…” *Extremophiles* 9:391–398. **September 2005.** https://doi.org/10.1007/s00792-005-0479-7

References

1. (andre2021theselectiveadvantage pages 2-4): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.

2. (mrnjavac2024theradicalimpact pages 15-17): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 16 citations and is from a peer-reviewed journal.

3. (gunsalus1994aerobicanaerobicgeneregulation pages 3-5): R.P. Gunsalus and S.-J. Park. Aerobic-anaerobic gene regulation in escherichia coli: control by the arcab and fnr regulons. Research in microbiology, 145 5-6:437-50, Jan 1994. URL: https://doi.org/10.1016/0923-2508(94)90092-2, doi:10.1016/0923-2508(94)90092-2. This article has 289 citations and is from a peer-reviewed journal.

4. (mrnjavac2024theradicalimpact pages 7-9): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 16 citations and is from a peer-reviewed journal.

5. (brown2022thearcabtwocomponent pages 3-4): Aric N. Brown, Mark T. Anderson, Michael A. Bachman, and Harry L. T. Mobley. The arcab two-component system: function in metabolism, redox control, and infection. Jun 2022. URL: https://doi.org/10.1128/mmbr.00110-21, doi:10.1128/mmbr.00110-21. This article has 115 citations and is from a domain leading peer-reviewed journal.

6. (brown2023conservedmetabolicregulator pages 12-14): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

7. (brown2023conservedmetabolicregulator pages 1-3): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

8. (price2021bacterialapproachesto pages 11-12): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (brown2023conservedmetabolicregulator pages 8-10): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

10. (brown2022thearcabtwocomponent pages 20-23): Aric N. Brown, Mark T. Anderson, Michael A. Bachman, and Harry L. T. Mobley. The arcab two-component system: function in metabolism, redox control, and infection. Jun 2022. URL: https://doi.org/10.1128/mmbr.00110-21, doi:10.1128/mmbr.00110-21. This article has 115 citations and is from a domain leading peer-reviewed journal.

11. (andre2021theselectiveadvantage pages 7-8): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.