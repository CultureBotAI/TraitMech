---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:47:06.299090'
end_time: '2026-06-18T11:10:19.995761'
duration_seconds: 1393.7
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoautotrophic
  trait_identifier: METPO:1000635
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from oxidation of
    inorganic compounds and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: chemoautotroph
  evidence_summary: 'DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in
    Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.)
    | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review
    supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)'
  causal_graph_summary: 'chemoautotrophic_chemical_energy_co2_fixation: 9 nodes, 9
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautotrophic
- **METPO identifier:** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautotrophic.yaml`.

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
- **Trait label:** chemoautotrophic
- **METPO identifier:** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **chemoautotrophic** (METPO:1000635)

**Trait label:** chemoautotrophic (CLASS; PHYSIOLOGY)  
**Definition (given):** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.  

### Scope summary (what the trait represents)
Chemoautotrophy (often overlapping with **chemolithoautotrophy** in microbial literature) is best treated as a **physiological capacity**: the ability to convert dissolved inorganic carbon (DIC; CO2/HCO3−) into biomass **powered by chemical energy rather than light**, typically via oxidation of reduced inorganic electron donors. Deep-sea and sediment studies operationalize “putative chemoautotrophy” as **co-occurrence of a DIC-fixation pathway plus an inorganic catabolism** (e.g., sulfur oxidation, CO oxidation, nitrification) in a genome (MAG) (salcedo2026substantialgeneticpotential pages 11-14, salcedo2026substantialgeneticpotential pages 8-9).

**Boundary cases / nearby traits**
- **Photoautotrophy** differs by using **light** energy; chemoautotrophy is “dark carbon fixation” in many ecosystems (salcedo2026substantialgeneticpotential pages 1-3, wang2025phylogeneticallyandmetabolically pages 2-4).  
- **Chemoheterotrophy** differs by using **organic carbon** for biomass. However, many genomes with DIC-fixation and inorganic catabolism also encode extensive **organic transport** genes, consistent with **facultative chemoautotrophy / mixotrophy**, which should be modeled as a boundary condition rather than excluded (salcedo2026substantialgeneticpotential pages 1-3, salcedo2026substantialgeneticpotential pages 11-14).  
- **Mixotrophy/facultative autotrophy**: community/genome surveys note near-ubiquitous organic substrate transporters among putative chemoautotrophs, and thus warn that genomic potential alone cannot determine in situ carbon source partitioning without physiological/transcript evidence (salcedo2026substantialgeneticpotential pages 11-14, salcedo2026substantialgeneticpotential pages 9-11).

### Current mechanistic understanding (key concepts and definitions)
Chemoautotrophy requires two mechanistic pillars:
1) **Energy conservation from inorganic redox chemistry** (electron donor oxidation coupled to electron acceptor reduction), and  
2) **Autotrophic inorganic carbon fixation** (pathways/modules that incorporate CO2/HCO3− into central metabolites).

A central mechanistic theme in aerobic bacterial chemoautotrophs using the Calvin cycle is the **CO2-concentrating mechanism (CCM)**: DIC transporters elevate cytoplasmic HCO3− and **carboxysomes** encapsulate **Rubisco** and **carbonic anhydrase (CA)**; CA converts HCO3− to CO2 within the compartment, supplying CO2 to Rubisco for fixation (wieschollek2024anewtype pages 1-2).

### Recent developments (prioritizing 2023–2024)
#### (A) 2024: Novel carboxysomal carbonic anhydrase (ιCA) required for low-CO2 growth in sulfur chemolithoautotrophs
Wieschollek et al. (Applied and Environmental Microbiology, **Sep 2024**) provide direct genetic causality connecting a CCM component to autotrophic performance under low CO2. In *Thiomicrospira pelophila*, **interrupting the gene encoding iota-class carbonic anhydrase (ιCA)** eliminates detectable carboxysome CA activity and abolishes growth under low CO2; heterologous expression restores low-CO2 growth and CA activity in an E. coli CA-deficient strain (wieschollek2024anewtype pages 1-2). This supports curation of edges linking **ιCA → carboxysome CA activity → low-CO2 growth**.

The paper also grounds key CCM node candidates: **cbbL/cbbS** (Rubisco form I), **cbbM** (Rubisco form II), and locus architecture including **csoSX** replacing canonical **csoSCA** in these taxa (wieschollek2024anewtype pages 1-2). Visual evidence of carboxysome locus architecture and carboxysome protein composition is available (wieschollek2024anewtype media e1b160e0, wieschollek2024anewtype media b30f4a4b).

#### (B) 2024: Structural basis for energy-efficient archaeal 3HP/4HB carbon fixation
Johnson et al. (Communications Biology, **Oct 2024**) state that the **3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) cycle** in ammonia-oxidizing Thaumarchaeota is “currently considered the most energy-efficient aerobic carbon fixation pathway” and “may be responsible for **1% of global carbon fixation**” (johnson2024crystalstructureof pages 1-2). A key mechanistic contributor is **phosphate conservation**: thaumarchaeal synthetases (including **Nmar_0206**, 4-hydroxybutyryl-CoA synthetase) are **ADP-forming** rather than AMP-forming, reducing energetic burden (johnson2024crystalstructureof pages 1-2). Nmar_0206 catalyzes conversion of **4-hydroxybutyrate + CoA → 4HB-CoA** using energy from a single ATP dephosphorylation (johnson2024crystalstructureof pages 1-2).

#### (C) 2023: Electron transfer constraints in rTCA-based chemoautotrophy (Aquifex)
Prioretti et al. (Life, **Feb 2023**) provide biochemical evidence in the chemolithoautotroph *Aquifex aeolicus* that rTCA carboxylation enzymes (**PFOR, OGOR**) require very low-potential electron donors and can directly interact with low-potential ferredoxins (**Fd6/Fd7**, E0 ~ −440 to −460 mV) (prioretti2023carbonfixationin pages 1-2). This strongly supports edges connecting **ferredoxins → PFOR/OGOR → reductive carboxylation reactions → rTCA carbon fixation**.

#### (D) 2024: CBB prevalence and Rubisco constraints (psychrophile chemolithoautotrophy)
Harrison et al. (bioRxiv, **Aug 2024**) report that the **CBB cycle accounts for >99% of global autotrophy** and is also used by chemolithoautotrophs coupled to oxidation of inorganic donors (sulfur, iron, ammonia, nitrite) (harrison2024prevalenceofthe pages 1-5). Quantitatively, Rubisco’s activity at Earth mean surface temperature (~15°C) is estimated at **~4–13%** of its peak activity (45–60°C) and photorespiration can cost plants up to **49%** of gross primary production (contextual constraint motivating enzyme/CCM optimization) (harrison2024prevalenceofthe pages 1-5).

### Current applications / real-world implementations
1) **Engineering CCM components for robust autotrophy under challenging chemistry**: The discovery of carboxysomal **ιCA** in alkaliphilic sulfur chemolithoautotrophs is explicitly framed as potentially useful for engineering autotrophic organisms to synthesize industrial products under **alkaline/high-pH** conditions (wieschollek2024anewtype pages 1-2).  
2) **Bioprospecting/biocatalyst discovery from efficient carbon-fixing enzymes**: Structural characterization of **3HP/4HB** enzymes (e.g., Nmar_0206) is positioned as informing engineering of efficient carbon-cycling enzymes for remediation/biotechnology (johnson2024crystalstructureof pages 6-8).  
3) **Ecosystem modeling and carbon budgets**: Genome-resolved surveys emphasize chemoautotrophic diversity and the need to incorporate multiple energy metabolisms (e.g., CO oxidation) into deep-ocean carbon models; however, these are primarily 2026 preprint statistics and should be used cautiously for curation (salcedo2026substantialgeneticpotential pages 1-3, salcedo2026substantialgeneticpotential pages 14-18).

### Candidate nodes (grouped by type)
The following artifact provides a curation-ready node inventory with suggested grounding and evidence pointers.

| Category | Node label | Suggested ontology grounding | Notes/evidence pointer |
|---|---|---|---|
| Pathway/Module | Calvin-Benson-Bassham cycle | GO:0015977 carbon fixation | Dominant chemolithoautotrophic pathway in subzero environments; used by sulfur chemolithoautotrophs with Rubisco/carboxysomes (harrison2024prevalenceofthe pages 1-5, wieschollek2024anewtype pages 1-2) |
| Pathway/Module | reverse tricarboxylic acid cycle | label only; KEGG map00720 candidate | Explicit CO2 assimilation pathway in *Aquifex aeolicus* (prioretti2023carbonfixationin pages 1-2) |
| Pathway/Module | 3-hydroxypropionate/4-hydroxybutyrate cycle | label only | Described as the most energy-efficient aerobic carbon fixation pathway in ammonia-oxidizing Thaumarchaeota (johnson2024crystalstructureof pages 1-2) |
| Pathway/Module | Wood-Ljungdahl pathway | label only | Mentioned as an additional/partial carbon assimilation route; stronger ecological support in later sediment studies but weaker in 2023-2024 focal papers (prioretti2023carbonfixationin pages 1-2) |
| Pathway/Module | carbon-concentrating mechanism | GO:0009760 carbon dioxide concentrating mechanism | Defined as DIC transporters plus carboxysomes in sulfur chemolithoautotrophs (wieschollek2024anewtype pages 1-2) |
| Enzyme/Complex | Rubisco (form I) | EC:4.1.1.39 | Carboxysomal form I Rubisco in Thiomicrospira; core CO2-fixing enzyme of CBB cycle (wieschollek2024anewtype pages 1-2) |
| Enzyme/Complex | Rubisco (form II) | EC:4.1.1.39 | Non-carboxysomal form II Rubisco; highlighted in cold-adaptation/psychrophile study (harrison2024prevalenceofthe pages 1-5) |
| Enzyme/Complex | carbonic anhydrase | EC:4.2.1.1 | Converts HCO3- to CO2 inside carboxysomes; required for CCM function (wieschollek2024anewtype pages 1-2) |
| Enzyme/Complex | iota-class carbonic anhydrase (ιCA) | EC:4.2.1.1 | Novel carboxysomal CA type in sulfur chemolithoautotrophs; direct functional genetics evidence (wieschollek2024anewtype pages 1-2) |
| Enzyme/Complex | carboxysome | GO:0034715 carboxysome | Encapsulates Rubisco and CA; central to bacterial chemoautotrophic CCMs (wieschollek2024anewtype pages 1-2) |
| Enzyme/Complex | 4-hydroxybutyryl-CoA synthetase (Nmar_0206) | EC:6.2.1.- candidate | Structurally characterized 3HP/4HB-cycle enzyme in *Nitrosopumilus maritimus* (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 2-3, johnson2024crystalstructureof pages 5-6) |
| Enzyme/Complex | pyruvate:ferredoxin oxidoreductase (PFOR) | EC:1.2.7.1 | Key rTCA carboxylating enzyme in *A. aeolicus* (prioretti2023carbonfixationin pages 1-2) |
| Enzyme/Complex | 2-oxoglutarate:ferredoxin oxidoreductase (OGOR) | EC:1.2.7.3 | Key rTCA carboxylating enzyme in *A. aeolicus* (prioretti2023carbonfixationin pages 1-2) |
| Enzyme/Complex | low-potential ferredoxins Fd6/Fd7 | label only | Electron donors to PFOR and OGOR in rTCA-based chemoautotrophy (prioretti2023carbonfixationin pages 1-2) |
| Enzyme/Complex | uptake hydrogenase HupSL | label only | Hydrogen uptake linked to chemolithotrophic energy metabolism in purple sulfur bacterium example (petushkova2024thecompletegenome pages 16-17) |
| Gene marker | cbbL | label only | Encodes Rubisco large subunit of carboxysomal form I (wieschollek2024anewtype pages 1-2) |
| Gene marker | cbbS | label only | Encodes Rubisco small subunit of carboxysomal form I (wieschollek2024anewtype pages 1-2) |
| Gene marker | cbbM | label only | Encodes non-carboxysomal form II Rubisco (wieschollek2024anewtype pages 1-2) |
| Gene marker | csoSCA | label only | Canonical alpha-carboxysome CA marker; absent from Thiomicrospira loci in focal 2024 study (wieschollek2024anewtype pages 1-2) |
| Gene marker | csoSX | label only | Small carboxysome-locus gene replacing canonical csoSCA in Thiomicrospira (wieschollek2024anewtype pages 1-2) |
| Gene marker | ιCA gene | label only | Gene disruption abolished low-CO2 growth and carboxysome CA activity (wieschollek2024anewtype pages 1-2) |
| Gene marker | Nmar_0206 | label only | Marker for thaumarchaeal ADP-forming 4-hydroxybutyryl-CoA synthetase (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 2-3) |
| Gene marker | Nmar_1309 | label only | Companion ADP-forming 3HP/4HB synthetase gene discussed with Nmar_0206 (johnson2024crystalstructureof pages 1-2) |
| Metabolite/chemical | carbon dioxide | CHEBI:16526 | Canonical carbon source for chemoautotrophy (johnson2024crystalstructureof pages 1-2, wieschollek2024anewtype pages 1-2) |
| Metabolite/chemical | bicarbonate | CHEBI:17544 | DIC species transported and converted to CO2 in carboxysomes (wieschollek2024anewtype pages 1-2) |
| Metabolite/chemical | coenzyme A | CHEBI:15346 | Substrate in Nmar_0206-catalyzed 4HB-CoA formation (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 5-6) |
| Metabolite/chemical | 4-hydroxybutyrate | CHEBI:30830 | Substrate for Nmar_0206 in 3HP/4HB cycle (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 5-6) |
| Metabolite/chemical | 4-hydroxybutyryl-CoA | label only | Product of Nmar_0206 reaction in 3HP/4HB cycle (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 5-6) |
| Metabolite/chemical | acetyl-CoA | CHEBI:57288 | rTCA intermediate; reductively carboxylated by PFOR to pyruvate (prioretti2023carbonfixationin pages 1-2) |
| Metabolite/chemical | pyruvate | CHEBI:15361 | Product of PFOR reductive carboxylation in rTCA (prioretti2023carbonfixationin pages 1-2) |
| Metabolite/chemical | succinyl-CoA | CHEBI:57292 | OGOR substrate in rTCA reductive carboxylation (prioretti2023carbonfixationin pages 1-2) |
| Metabolite/chemical | 2-oxoglutarate | CHEBI:16810 | OGOR product in rTCA reductive carboxylation (prioretti2023carbonfixationin pages 1-2) |
| Electron donor | reduced sulfur compounds | CHEBI:26896 sulfur atom; label only | Sulfur oxidation repeatedly linked to chemolithoautotrophic CO2 fixation (wieschollek2024anewtype pages 1-2, petushkova2024thecompletegenome pages 16-17) |
| Electron donor | thiosulfate | CHEBI:9569 | Supports chemolithotrophic CO2 assimilation in the dark in purple sulfur bacterium example (petushkova2024thecompletegenome pages 16-17) |
| Electron donor | hydrogen | CHEBI:18276 | Used as inorganic electron donor in multiple focal studies (prioretti2023carbonfixationin pages 1-2, petushkova2024thecompletegenome pages 16-17) |
| Electron donor | ammonia | CHEBI:16134 | Coupled to 3HP/4HB autotrophy in Thaumarchaeota context (johnson2024crystalstructureof pages 1-2) |
| Electron donor | nitrite | CHEBI:16301 | Listed as chemolithotrophic electron donor in CBB-focused review/preprint on psychrophiles (harrison2024prevalenceofthe pages 1-5) |
| Electron donor | ferrous iron | CHEBI:29033 | Listed among inorganic electron donors in broader chemoautotrophy definitions; less direct in focal 2023-2024 mechanistic papers (wang2025phylogeneticallyandmetabolically pages 2-4, wang2025phylogeneticallyandmetabolically pages 1-2) |
| Electron acceptor | oxygen | CHEBI:15379 | Relevant to aerobic chemoautotrophy and Rubisco oxygen sensitivity; low-CO2/O2 tradeoffs discussed (harrison2024prevalenceofthe pages 1-5) |
| Electron acceptor | elemental sulfur | CHEBI:26896 sulfur atom | Reduced by HydSL-linked metabolism in purple sulfur bacterium example (petushkova2024thecompletegenome pages 16-17) |
| Environmental factor | low CO2 | label only | Growth phenotype directly dependent on ιCA in Thiomicrospira (wieschollek2024anewtype pages 1-2) |
| Environmental factor | low DIC | label only | Used to enrich carboxysomes/induce CCM relevance in Thiomicrospira (wieschollek2024anewtype pages 2-5) |
| Environmental factor | alkaline/high pH conditions | ENVO:3100031 alkaline environment candidate | ιCA may confer advantage to alkaliphilic autotrophs (wieschollek2024anewtype pages 1-2) |
| Environmental factor | subzero/cold environment | ENVO:01001852 permafrost environment candidate; label only | Cold-adapted Rubisco and CBB prevalence in chemolithoautotrophic psychrophiles (harrison2024prevalenceofthe pages 1-5) |
| Environmental factor | oligotrophic conditions | ENVO:01000772 oligotrophic environment candidate | Energy-efficient thaumarchaeal 3HP/4HB enzymes interpreted as adaptation to low-nutrient settings (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 6-8) |
| Cellular compartment/structure | carboxysome shell | GO:0034715 carboxysome | Structural microcompartment for Rubisco and CA (wieschollek2024anewtype pages 1-2, wieschollek2024anewtype pages 2-5) |
| Cellular compartment/structure | cytoplasmic DIC pool | label only | Elevated by DIC transporters before conversion in carboxysome (wieschollek2024anewtype pages 1-2) |
| Cellular compartment/structure | ubiquinone pool | CHEBI:16389 ubiquinone | Receives electrons from HupSL hydrogenase in chemolithotrophic metabolism example (petushkova2024thecompletegenome pages 16-17) |
| Assay/measurement | carboxysome CA activity assay | label only | Used to show ιCA-dependent CA activity in purified carboxysomes (wieschollek2024anewtype pages 2-5, wieschollek2024anewtype pages 1-2) |
| Assay/measurement | low-CO2 growth phenotype | label only | Knockout/complementation phenotype for ιCA function (wieschollek2024anewtype pages 1-2) |
| Assay/measurement | X-ray crystal structure of Nmar_0206 | label only | Structural evidence for 3HP/4HB enzyme mechanism (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 2-3, johnson2024crystalstructureof pages 5-6) |
| Assay/measurement | ferredoxin-enzyme interaction/electron exchange assay | label only | Demonstrated Fd6/Fd7 interaction with PFOR and OGOR (prioretti2023carbonfixationin pages 1-2) |
| Assay/measurement | shotgun proteomics | label only | Detected rTCA enzymes and relative abundance patterns in *A. aeolicus* (prioretti2023carbonfixationin pages 1-2) |


*Table: This table lists candidate nodes for a TraitMech causal graph of the chemoautotrophic trait, grouped by biological category and grounded where possible to standard ontologies. It prioritizes mechanistically supported entities from 2023-2024 studies while flagging a small number of broader contextual nodes supported by later work.*

### Evidence-backed candidate causal edges (triples)
The following artifact provides a candidate edge list with snippets, DOI-first references, grounding suggestions, and strength notes (direct perturbation vs inference).

| Edge (subject–predicate–object) | Node types | Suggested identifiers | Evidence snippet (verbatim/near-verbatim) | Reference (DOI + URL + year) | Strength/notes |
|---|---|---|---|---|---|
| Sulfur oxidation — supports → chemoautotrophic CO2 fixation | metabolism → trait | GO:sulfur compound metabolic process; METPO:1000635 chemoautotrophic | “sulfur-oxidizing (chemolithoautotrophic) Thiomicrospira spp.” with CCMs for CO2 fixation (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Direct physiological context in sulfur chemolithoautotrophs; taxon-specific but strong organismal support. |
| Thiosulfate oxidation — provides energy for → CO2 assimilation | chemical/metabolism → process | CHEBI:9569 thiosulfate(2-); label: chemolithotrophic CO2 assimilation | “thiosulfate specifically supports chemolithotrophic CO2 assimilation in the dark” (petushkova2024thecompletegenome pages 16-17) | 10.3390/microorganisms12020391 · https://doi.org/10.3390/microorganisms12020391 · 2024 | Direct statement, but from Thiocapsa/related taxa; likely curatable as taxon-scoped support. |
| Hydrogen oxidation — supports → chemoautotrophic growth/CO2 fixation | metabolism → trait/process | CHEBI:18276 hydrogen molecular entity; label: hydrogen oxidation | “HupSL for hydrogen uptake (feeding electrons to the ubiquinone pool)… thiosulfate, sulfur, or H2 as inorganic electron donors” (petushkova2024thecompletegenome pages 16-17) | 10.3390/microorganisms12020391 · https://doi.org/10.3390/microorganisms12020391 · 2024 | Supports inorganic-energy side of chemoautotrophy; linkage to CO2 fixation is organism-level, not single-reaction direct. |
| CO oxidation — can fuel → dissolved inorganic carbon fixation | metabolism → process | CHEBI:17245 carbon monoxide; label: aerobic carbon monoxide dehydrogenase coxMSL | “detection of coxMSL in putatively chemoautotrophic MAGs” and “co-expression of coxL and rubisco” (salcedo2026substantialgeneticpotential pages 9-11) | 10.64898/2026.01.13.699260 · https://doi.org/10.64898/2026.01.13.699260 · 2026 | Genomic/transcriptomic inference; broad environmental support, not isolate-level proof. |
| Ammonia oxidation — coupled to → 3HP/4HB autotrophy | metabolism → pathway | CHEBI:16134 ammonia; label: 3HP/4HB cycle | “Nitrososphaeria couple ammonia oxidation to 3HP/4HB autotrophy” (salcedo2026substantialgeneticpotential pages 1-3) | 10.64898/2026.01.13.699260 · https://doi.org/10.64898/2026.01.13.699260 · 2026 | Environmental genomic synthesis; useful for edge proposal, but indirect for TraitMech unless taxon-labeled. |
| Calvin–Benson–Bassham cycle — enables → inorganic carbon assimilation | pathway → process | GO:0015977 carbon fixation; label: Calvin-Benson-Bassham cycle | “The CBB cycle accounts for >99% of global autotrophy” and is used “in chemolithoautotrophs” (harrison2024prevalenceofthe pages 1-5) | 10.1101/2024.08.01.606197 · https://doi.org/10.1101/2024.08.01.606197 · 2024 | Strong pathway-level support; preprint. Broad but not specific to any one chemotroph lineage. |
| Reverse TCA cycle — enables → CO2 assimilation in Aquifex aeolicus | pathway → process | label: reverse tricarboxylic acid cycle; GO:0015977 | “A. aeolicus… assimilates CO2 via the reverse tricarboxylic acid cycle (rTCA)” (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 · https://doi.org/10.3390/life13030627 · 2023 | Strong species-specific evidence with biochemical follow-up. |
| Wood–Ljungdahl pathway — predominates in → anoxic dark carbon fixation niches | pathway → ecological process | label: Wood-Ljungdahl pathway; ENVO:00002005 sediment | “the Wood-Ljungdahl (WL) pathway [was] predominant” and active in deeper layers; “WL requires strict anoxia” (wang2025phylogeneticallyandmetabolically pages 2-4, wang2025phylogeneticallyandmetabolically pages 1-2) | 10.1186/s40168-025-02177-9 · https://doi.org/10.1186/s40168-025-02177-9 · 2025 | Good ecological evidence; mainly community-level, not isolate genetic causation. |
| 3HP/4HB cycle — is → energy-efficient aerobic carbon fixation pathway | pathway → phenotype | label: 3-hydroxypropionate/4-hydroxybutyrate cycle | “currently considered the most energy-efficient aerobic carbon fixation pathway” (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x · https://doi.org/10.1038/s42003-024-06432-x · 2024 | Strong, direct statement from primary structural paper. |
| Nmar_0206 4-hydroxybutyryl-CoA synthetase — participates in → 3HP/4HB cycle | protein/enzyme → pathway | label: Nmar_0206; EC:6.2.1.- candidate; label: 4-hydroxybutyryl-CoA synthetase | “Nmar_0206… represents one of several enzymes from this cycle” (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x · https://doi.org/10.1038/s42003-024-06432-x · 2024 | Direct primary evidence; structurally characterized enzyme. |
| Nmar_0206 — catalyzes → 4-hydroxybutyrate + CoA → 4HB-CoA | enzyme → reaction | label: Nmar_0206; CHEBI:20827 coenzyme A; label: 4-hydroxybutyrate; label: 4-hydroxybutyryl-CoA | “catalyzes the conversion of 4HB and CoA to 4HB-CoA using the energy from a single dephosphorylation of ATP” (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x · https://doi.org/10.1038/s42003-024-06432-x · 2024 | Strong enzyme-to-reaction edge; useful mechanistic detail for pathway graph. |
| Low-potential ferredoxins Fd6/Fd7 — donate electrons to → PFOR/OGOR | protein → enzyme complex | label: Fd6/Fd7 ferredoxins; EC:1.2.7.1 PFOR; EC:1.2.7.3 OGOR candidate | “Fd6 and Fd7… can physically interact and exchange electrons with both PFOR and OGOR” (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 · https://doi.org/10.3390/life13030627 · 2023 | Strong biochemical evidence in A. aeolicus. |
| PFOR — performs → reductive carboxylation of acetyl-CoA to pyruvate | enzyme → reaction | EC:1.2.7.1; CHEBI:15351 pyruvate; CHEBI:57288 acetyl-CoA | “PFOR… responsible for the reductive carboxylation of acetyl-CoA to pyruvate” (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 · https://doi.org/10.3390/life13030627 · 2023 | Direct mechanistic support; species-specific. |
| OGOR — performs → reductive carboxylation of succinyl-CoA to 2-oxoglutarate | enzyme → reaction | EC:1.2.7.3 candidate; CHEBI:57292 succinyl-CoA; CHEBI:16810 2-oxoglutarate | “OGOR… responsible for… reductive carboxylation of succinyl-CoA to 2-oxoglutarate” (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 · https://doi.org/10.3390/life13030627 · 2023 | Direct mechanistic support; species-specific. |
| DIC transporters — supply substrate for → carbon-concentrating mechanism | transporter/process → complex/process | label: DIC transporters; CHEBI:17544 bicarbonate; CHEBI:16526 carbon dioxide | “CCMs consist of CO2 and HCO3− transporters and carboxysomes” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Strong mechanistic statement; broad for CBB autotrophic bacteria. |
| Carboxysome — encapsulates → RubisCO and carbonic anhydrase | organelle/compartment → proteins | GO:0034715 carboxysome; EC:4.1.1.39 RuBisCO; EC:4.2.1.1 carbonic anhydrase | “Carboxysomes encapsulate RubisCO and carbonic anhydrase (CA) within a protein shell” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Strong direct mechanistic evidence. |
| Carboxysomal carbonic anhydrase (including ιCA) — converts → HCO3− to CO2 inside carboxysome | enzyme → reaction/localized process | EC:4.2.1.1; label: iota carbonic anhydrase; CHEBI:17544 bicarbonate; CHEBI:16526 carbon dioxide | “Inside carboxysomes, CA converts HCO3− to CO2, which RubisCO then fixes” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Strong mechanistic evidence. |
| ιCA gene disruption — abolishes → growth under low-CO2 conditions | gene perturbation → phenotype | label: iota carbonic anhydrase gene; label: low-CO2 growth | “When the gene encoding ιCA was interrupted in T. pelophila, cells could no longer grow under low-CO2 conditions” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Very strong causal evidence: direct genetic knockout phenotype. |
| ιCA gene disruption — eliminates → carboxysome CA activity | gene perturbation → molecular function | label: iota carbonic anhydrase gene; EC:4.2.1.1 carbonic anhydrase activity | “CA activity was no longer detectable in their carboxysomes” after ιCA interruption (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Very strong causal evidence: direct perturbation-to-function link. |
| Heterologous ιCA expression — restores → low-CO2 growth and CA activity | transgene expression → phenotype/function | label: T. pelophila ιCA; label: low-CO2 growth; EC:4.2.1.1 | “this strain recovered an ability to grow under low CO2 conditions, and CA activity was present” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Very strong complementation evidence. |
| cbbL/cbbS — encode → carboxysomal form I RubisCO | genes → protein complex | label: cbbL; label: cbbS; EC:4.1.1.39 | “carboxysomal form I RubisCO (cbbL and cbbS)” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Strong gene-to-protein assignment. |
| cbbM — encodes → non-carboxysomal form II RubisCO | gene → protein | label: cbbM; EC:4.1.1.39 | “a non-carboxysomal form II RubisCO (cbbM)” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Strong gene-to-protein assignment; taxon-specific. |
| csoSX replacing csoSCA — suggests altered/novel → carboxysomal CA function | gene architecture → function | label: csoSX; label: csoSCA; label: carboxysomal carbonic anhydrase | “CsoSCA genes are absent… replaced by a smaller gene csoSX that lacks residues for CsoSCA activity” (wieschollek2024anewtype pages 1-2) | 10.1128/AEM.01075-24 · https://doi.org/10.1128/AEM.01075-24 · 2024 | Good locus-based inference; function resolved by accompanying ιCA evidence. |
| Organic-matter ABC transporters — indicate → facultative chemoautotrophy/mixotrophy | transporter genes → lifestyle boundary case | label: amino-acid ABC transporters; label: facultative chemoautotrophy; label: mixotrophy | “amino-acid ABC transporters are nearly ubiquitous… supporting potential facultative chemoautotrophy or mixotrophy” (salcedo2026substantialgeneticpotential pages 9-11, salcedo2026substantialgeneticpotential pages 11-14) | 10.64898/2026.01.13.699260 · https://doi.org/10.64898/2026.01.13.699260 · 2026 | Useful boundary-case edge; genomic inference only, should be marked uncertain. |
| Glycine cleavage pathway genes — indicate → facultative chemoautotrophy/mixotrophy | pathway genes → lifestyle boundary case | label: glycine cleavage system; label: facultative chemoautotrophy; label: mixotrophy | “glycine cleavage genes are nearly ubiquitous, supporting potential facultative chemoautotrophy or mixotrophy” (salcedo2026substantialgeneticpotential pages 9-11, salcedo2026substantialgeneticpotential pages 11-14) | 10.64898/2026.01.13.699260 · https://doi.org/10.64898/2026.01.13.699260 · 2026 | Boundary-case, inferential; not sufficient alone to curate as definitive lifestyle. |


*Table: This table lists candidate causal edges for a chemoautotrophic TraitMech graph, spanning inorganic energy metabolisms, carbon fixation pathways, carbon-concentrating mechanisms, key enzymes, and boundary-case mixotrophy signals. It is designed to support curation by pairing each proposed edge with near-verbatim evidence, references, identifiers, and confidence notes.*

### Visual evidence for curation
- **Figure:** Carboxysome loci including ιCA homologs across taxa (useful for gene-neighborhood evidence and node inclusion decisions) (wieschollek2024anewtype media e1b160e0).  
- **Table:** Relative abundance of carboxysome-associated proteins in carboxysome preparations (supports which proteins are enriched and plausibly functional components) (wieschollek2024anewtype media b30f4a4b).

### Statistics and quantitative data (recent)
- **3HP/4HB global contribution:** The thaumarchaeal 3HP/4HB cycle “may be responsible for **1% of global carbon fixation**” (Communications Biology, 2024) (johnson2024crystalstructureof pages 1-2).  
- **Global dominance of CBB:** The CBB cycle accounts for **>99%** of global autotrophy (bioRxiv, 2024) (harrison2024prevalenceofthe pages 1-5).  
- **Rubisco temperature constraint:** At ~15°C Rubisco operates at **~4–13%** of peak activity (bioRxiv, 2024) (harrison2024prevalenceofthe pages 1-5).  
- **Direct causal phenotype:** Disruption of **ιCA** abolishes **low-CO2 growth** in *Thiomicrospira pelophila* (AEM, 2024) (wieschollek2024anewtype pages 1-2).  

### Curation warnings (claims not ready for strong TraitMech edges)
1) **Genome-only inference of lifestyle**: Edges stating “organic transporters → mixotrophy” should be curated as **uncertain**, because genomic potential does not confirm substrate usage without transcript/physiology (salcedo2026substantialgeneticpotential pages 11-14, salcedo2026substantialgeneticpotential pages 9-11).  
2) **Environment-specific donor/acceptor lists**: Sediment/dark carbon fixation donor–acceptor lists (e.g., Fe(II), nitrate, sulfate) are valid ecological context but may require ENVO-scoped edges (sediment redox gradients) to avoid overgeneralization (wang2025phylogeneticallyandmetabolically pages 2-4, wang2025phylogeneticallyandmetabolically pages 1-2).  
3) **Preprints vs peer-reviewed**: Harrison et al. 2024 and Salcedo et al. 2026 are preprints; mechanistic claims they make should be cross-validated when possible, but they are still useful for hypothesis generation and node discovery (harrison2024prevalenceofthe pages 1-5, salcedo2026substantialgeneticpotential pages 1-3).

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Wieschollek J, et al. **A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments.** *Applied and Environmental Microbiology.* **Sep 2024**. DOI: **10.1128/AEM.01075-24**. URL: https://doi.org/10.1128/AEM.01075-24 (wieschollek2024anewtype pages 1-2, wieschollek2024anewtype pages 2-5, wieschollek2024anewtype media e1b160e0, wieschollek2024anewtype media b30f4a4b)

2. Johnson J, et al. **Crystal structure of the 4-hydroxybutyryl-CoA synthetase (ADP-forming) from Nitrosopumilus maritimus.** *Communications Biology.* **Oct 2024**. DOI: **10.1038/s42003-024-06432-x**. URL: https://doi.org/10.1038/s42003-024-06432-x (johnson2024crystalstructureof pages 1-2)

3. Prioretti L, et al. **Carbon Fixation in the Chemolithoautotrophic Bacterium Aquifex aeolicus Involves Two Low-Potential Ferredoxins as Partners of the PFOR and OGOR Enzymes.** *Life.* **Feb 2023**. DOI: **10.3390/life13030627**. URL: https://doi.org/10.3390/life13030627 (prioretti2023carbonfixationin pages 1-2)

4. Petushkova E, et al. **The Complete Genome of a Novel Typical Species Thiocapsa bogorovii and Analysis of Its Central Metabolic Pathways.** *Microorganisms.* **Feb 2024**. DOI: **10.3390/microorganisms12020391**. URL: https://doi.org/10.3390/microorganisms12020391 (petushkova2024thecompletegenome pages 16-17)

5. Harrison K, et al. **Prevalence of the Calvin-Benson-Bassham cycle in chemolithoautotrophic psychrophiles and the potential for cold-adapted Rubisco.** *bioRxiv.* **Aug 2024**. DOI: **10.1101/2024.08.01.606197**. URL: https://doi.org/10.1101/2024.08.01.606197 (harrison2024prevalenceofthe pages 1-5)

Additional (contextual; outside 2023–2024 but provides useful statistics and comparative energetics):  
6. Salcedo RSR, Jaffe AL, Dekas AE. **Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers.** *bioRxiv.* **Jan 2026**. DOI: **10.64898/2026.01.13.699260**. URL: https://doi.org/10.64898/2026.01.13.699260 (salcedo2026substantialgeneticpotential pages 1-3, salcedo2026substantialgeneticpotential pages 14-18, salcedo2026substantialgeneticpotential pages 9-11)

7. Wang S, et al. **Phylogenetically and metabolically diverse active carbon-fixing microbes reside in mangrove sediments.** *Microbiome.* **Sep 2025**. DOI: **10.1186/s40168-025-02177-9**. URL: https://doi.org/10.1186/s40168-025-02177-9 (wang2025phylogeneticallyandmetabolically pages 2-4)


References

1. (salcedo2026substantialgeneticpotential pages 11-14): Rebecca S. R. Salcedo, Alexander L. Jaffe, and Anne E. Dekas. Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.13.699260, doi:10.64898/2026.01.13.699260. This article has 0 citations.

2. (salcedo2026substantialgeneticpotential pages 8-9): Rebecca S. R. Salcedo, Alexander L. Jaffe, and Anne E. Dekas. Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.13.699260, doi:10.64898/2026.01.13.699260. This article has 0 citations.

3. (salcedo2026substantialgeneticpotential pages 1-3): Rebecca S. R. Salcedo, Alexander L. Jaffe, and Anne E. Dekas. Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.13.699260, doi:10.64898/2026.01.13.699260. This article has 0 citations.

4. (wang2025phylogeneticallyandmetabolically pages 2-4): Shasha Wang, Zhuoming Zhao, Ruolin Cheng, Liang Cui, Jun Wang, Maxim Rubin-Blum, Yao Zhang, Bolin Liu, Xing Chen, Federico Baltar, Xiaxing Cao, Xuezhe Wen, Karine Alain, Zhen Chen, Jing Liao, Lijing Jiang, and Zongze Shao. Phylogenetically and metabolically diverse active carbon-fixing microbes reside in mangrove sediments. Microbiome, Sep 2025. URL: https://doi.org/10.1186/s40168-025-02177-9, doi:10.1186/s40168-025-02177-9. This article has 15 citations and is from a highest quality peer-reviewed journal.

5. (salcedo2026substantialgeneticpotential pages 9-11): Rebecca S. R. Salcedo, Alexander L. Jaffe, and Anne E. Dekas. Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.13.699260, doi:10.64898/2026.01.13.699260. This article has 0 citations.

6. (wieschollek2024anewtype pages 1-2): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

7. (wieschollek2024anewtype media e1b160e0): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

8. (wieschollek2024anewtype media b30f4a4b): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

9. (johnson2024crystalstructureof pages 1-2): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

10. (prioretti2023carbonfixationin pages 1-2): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 7 citations.

11. (harrison2024prevalenceofthe pages 1-5): Kaitlin Harrison, Josephine Z. Rapp, Alexander L. Jaffe, Jody W. Deming, and Jodi Young. Prevalence of the calvin-benson-bassham cycle in chemolithoautotrophic psychrophiles and the potential for cold-adapted rubisco. BioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.01.606197, doi:10.1101/2024.08.01.606197. This article has 1 citations.

12. (johnson2024crystalstructureof pages 6-8): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

13. (salcedo2026substantialgeneticpotential pages 14-18): Rebecca S. R. Salcedo, Alexander L. Jaffe, and Anne E. Dekas. Substantial genetic potential for deep-sea chemoautotrophy extends beyond nitrifiers. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.13.699260, doi:10.64898/2026.01.13.699260. This article has 0 citations.

14. (johnson2024crystalstructureof pages 2-3): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

15. (johnson2024crystalstructureof pages 5-6): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

16. (petushkova2024thecompletegenome pages 16-17): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

17. (wang2025phylogeneticallyandmetabolically pages 1-2): Shasha Wang, Zhuoming Zhao, Ruolin Cheng, Liang Cui, Jun Wang, Maxim Rubin-Blum, Yao Zhang, Bolin Liu, Xing Chen, Federico Baltar, Xiaxing Cao, Xuezhe Wen, Karine Alain, Zhen Chen, Jing Liao, Lijing Jiang, and Zongze Shao. Phylogenetically and metabolically diverse active carbon-fixing microbes reside in mangrove sediments. Microbiome, Sep 2025. URL: https://doi.org/10.1186/s40168-025-02177-9, doi:10.1186/s40168-025-02177-9. This article has 15 citations and is from a highest quality peer-reviewed journal.

18. (wieschollek2024anewtype pages 2-5): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.