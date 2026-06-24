---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:03:44.257104'
end_time: '2026-06-17T21:22:09.676557'
duration_seconds: 1105.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: aerotolerant
  trait_identifier: METPO:1000609
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: aerotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that does not use O\u2082 for growth but tolerates\
    \ its presence."
  parent_traits: METPO:1000601
  synonyms: aerotolerant anaerobe
  evidence_summary: 'https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements:
    they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance
    without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant
    and survives limited oxygen exposure (Organism example: Clostridium perfringens
    is described as aerotolerant.)'
  causal_graph_summary: 'aerotolerant_anaerobe_ros_defense: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** aerotolerant
- **METPO identifier:** METPO:1000609
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that does not use O₂ for growth but tolerates its presence.
- **Parent traits:** METPO:1000601
- **Synonyms:** aerotolerant anaerobe
- **Existing evidence:** https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements: they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant and survives limited oxygen exposure (Organism example: Clostridium perfringens is described as aerotolerant.)
- **Existing causal graph summary:** aerotolerant_anaerobe_ros_defense: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **aerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerotolerant.yaml`.

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
- **Trait label:** aerotolerant
- **METPO identifier:** METPO:1000609
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that does not use O₂ for growth but tolerates its presence.
- **Parent traits:** METPO:1000601
- **Synonyms:** aerotolerant anaerobe
- **Existing evidence:** https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements: they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant and survives limited oxygen exposure (Organism example: Clostridium perfringens is described as aerotolerant.)
- **Existing causal graph summary:** aerotolerant_anaerobe_ros_defense: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **aerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerotolerant.yaml`.

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


## Microbial TraitMech Causal-Graph Research Report: **aerotolerant** (METPO:1000609)

**Trait label:** aerotolerant (syn. aerotolerant anaerobe)  
**Definition (given):** “An oxygen preference that does not use O₂ for growth but tolerates its presence.”  

### 1) Trait scope (what the trait represents; boundaries)

**Operational phenotype.** Recent work supports treating oxygen response as a *spectrum* even among “strict/obligate anaerobes,” because survival at low O2 can be mediated by dedicated O2-reducing and ROS-detoxifying systems rather than aerobic growth. For example, *Clostridioides difficile* is described as a “strict/obligate anaerobe,” yet is exposed to physiologic O2 tensions in the gut and encodes multiple O2-reductases that enable tolerance over defined O2 ranges; some strains can grow up to 2% O2 (caulat2024physiologicalroleand pages 1-2). Likewise, *Geobacter sulfurreducens* was “reclassified as aerotolerant,” with reported tolerance for O2 exposure up to 24 h and ability to use O2 as an electron acceptor under microaerobic conditions (10% v/v O2) (portela2023exploringoxidativestress pages 1-2).

**Boundary cases and nearby traits.** 
- **Strict/obligate anaerobe:** highly sensitive to oxygen, but can still show measurable low-O2 tolerance if protective systems exist (e.g., *C. difficile* O2-reductases spanning 0.1% to air; see below) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 11-13).  
- **Microaerophile:** requires low O2 for growth; may include aerotolerant strains (e.g., *Campylobacter* spp. review frames aerotolerant strains as able to survive aerobic conditions) (delaporte2024aerotolerancyofcampylobacter pages 8-9).  
- **Facultative anaerobe:** uses O2 when available; distinct from aerotolerant anaerobes which tolerate O2 but need not respire it for growth (keating2024microbialsinglecellapplications pages 1-2).  
- **Anoxic vs anaerobic:** anoxic is an oxygen-free (or below detection) *environment*; anaerobic describes *metabolism* conducted without measurable oxygen (keating2024microbialsinglecellapplications pages 1-2).

**Host-relevant context.** In the gut, *C. difficile* faces a longitudinal gradient from ~4–5% O2 in the small intestine to ~0.1–0.4% in the colonic lumen, with a lateral gradient rising toward mucus (1–2%) and tissues (~5%), illustrating why “aerotolerance” can be ecologically and clinically relevant even for anaerobes (caulat2024physiologicalroleand pages 1-2).

### 2) Key concepts and mechanistic entities (current understanding)

Aerotolerance in anaerobes is most consistently linked to two mechanistic modules:

1. **Reactive oxygen species (ROS) detoxification**
   - Key ROS: **superoxide anion (O2•−)** and **H2O2**, with downstream formation of **hydroxyl radical (•OH)** from superoxide/H2O2 chemistry (okabe2023oxygentoleranceand pages 2-3).  
   - Detox enzymes emphasized in recent studies and reviews include **superoxide dismutase (SOD)**, **catalase (Cat)**, diverse **peroxidases** (e.g., cytochrome c peroxidase, peroxiredoxins), and **rubrerythrins** (okabe2023oxygentoleranceand pages 11-12, portela2023exploringoxidativestress pages 1-2).

2. **O2 scavenging / O2-reducing systems (lowering intracellular O2)**
   - In *C. difficile*, four O2-reducing enzymes (two **flavodiiron proteins** FdpA/FdpF and two **reverse rubrerythrins** revRbr1/revRbr2) cover different O2 ranges (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 1-2).  
   - In sulfate-reducing bacteria (SRB) exposed to periodic oxic pulses, inferred O2-reducing routes include **rubredoxin:oxygen oxidoreductase (Roo/NorV)** and membrane **cytochrome bd oxidase (CydAB)**, plus other oxidases (dyksma2024growthofsulfatereducing pages 5-6).

### 3) Recent developments and latest research (prioritizing 2023–2024)

#### 3.1 Quantitative oxygen tolerance metrics in anaerobes

**Anammox bacteria (2023):** Okabe et al. quantified O2 inhibition kinetics using **IC50** and **DOmax**. The marine anammox “Ca. *Scalindua* sp.” showed substantially higher oxygen tolerance (**IC50 = 18.0 µM; DOmax = 51.6 µM**) than freshwater anammox (**IC50 = 2.7–4.2 µM; DOmax = 10.9–26.6 µM**) (okabe2023oxygentoleranceand pages 1-2). Oxygen inhibition could be reversible after 12–24 h exposure to ambient air (okabe2023oxygentoleranceand pages 1-2).

**Mechanistic link to enzyme activities:** Only *Scalindua* exhibited high **SOD activity (22.6 ± 1.9 U/mg-protein)** with moderate **catalase activity (1.6 ± 0.7 U/mg-protein)**, consistent with the authors’ proposal that Sod–Cat detoxification contributes to higher O2 tolerance (okabe2023oxygentoleranceand pages 1-2).

**C. difficile (2024):** Caulat et al. provide a mechanistic partitioning of tolerance across O2 tensions: revRbr2 (<0.4% O2), FdpA (0.4–1%), revRbr1 (0.1–4%), and FdpF (>4% and air) (caulat2024physiologicalroleand pages 11-13). Mutant survival phenotypes show that loss of these enzymes can cause substantial survival defects at defined O2 tensions (e.g., near-complete loss of survival for fdpA mutants after 48 h at 1% O2; 2-log and 6-log losses for a double revrbr mutant at 24 h and 48 h at 1% O2) (caulat2024physiologicalroleand pages 2-5).

#### 3.2 Regulatory systems as “trait switches”

A 2024 advance is the explicit mapping of *regulatory logic* that gates oxygen defense:
- In *C. difficile*, the four O2-reductase genes are “controlled by the alternative sigma factor σB” and show gene-specific dual-promoter architecture (σA/σB for fdpA and revrbr2) (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17).  
- The Spx-family regulator **OseR** represses fdp/revrbr genes in anaerobiosis and repression is released after long-term exposure to 1% O2 (caulat2024physiologicalroleand pages 13-15).  
- **Rex** (NADH/NAD+ sensor) represses **fdpF**, linking redox state to oxygen defense deployment (caulat2024physiologicalroleand pages 11-13).

#### 3.3 Community and environmental-interface adaptation

Dyksma & Pester (2024) show that peatland SRB communities can persist despite weekly oxic pulses (**133 µM O2; 50% air saturation**) over >200 days, with metatranscriptomic evidence of transcription of genes for oxygen consumption, ROS detoxification, and repair, and some SRB maintaining high transcript levels of oxygen-defense genes even under anoxia (dyksma2024growthofsulfatereducing pages 1-2). This provides an ecologically realistic model for how “strict anaerobes” can manifest aerotolerance in fluctuating redox niches.

### 4) Current applications and real-world implementations

1. **Gut microbiology / pathogenesis:** Oxygen gradients in the gut create selective pressures for O2-tolerance systems in anaerobes. Caulat et al. explicitly relate O2-reductase activity ranges to physiologic O2 tensions during infection, implying that aerotolerance can contribute to persistence/fitness of anaerobic pathogens in host-associated micro-oxic microenvironments (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 11-13).

2. **Biogeochemistry and engineered anaerobic systems:** The ability of SRB to persist during periodic oxygenation supports their role in sulfur cycling at oxic–anoxic interfaces and indicates why anaerobic processes can remain active in environments with intermittent oxygen exposure (peatlands, wetlands, tidal sediments), informing ecosystem models and engineered bioreactor operation under redox fluctuations (dyksma2024growthofsulfatereducing pages 1-2).

3. **Bioelectrochemical / environmental biotechnology:** *G. sulfurreducens* is of applied interest for extracellular electron transfer. Its reclassification as aerotolerant and the identification of electron-transfer routes that can supply reducing power to oxidative stress defense (PpcA-E → MacA) suggests design principles for engineering oxygen-resilient electroactive strains or operating conditions near oxic–anoxic interfaces (portela2023exploringoxidativestress pages 1-2).

### 5) Relevant statistics and data points (recent studies)

- **Anammox O2 tolerance:** *Scalindua* IC50 = 18.0 µM; DOmax = 51.6 µM vs freshwater anammox IC50 = 2.7–4.2 µM; DOmax = 10.9–26.6 µM (Okabe 2023) (okabe2023oxygentoleranceand pages 1-2).  
- **Enzyme activities (anammox):** SOD 22.6 ± 1.9 U/mg-protein; catalase 1.6 ± 0.7 U/mg-protein in *Scalindua* (okabe2023oxygentoleranceand pages 1-2).  
- **C. difficile mutant survival at 1% O2:** fdpA::erm shows “almost complete loss of survival… after 48 h”; double revrbr mutant shows “2-log reduction after 24 h… (6-logs) after 48 h” (caulat2024physiologicalroleand pages 2-5).  
- **SRB periodic oxygen stress:** weekly exposure to 133 µM O2 (50% air saturation), with SRB populations establishing despite oxic phases and expressing oxygen defense genes (dyksma2024growthofsulfatereducing pages 1-2).  
- **Geobacter aerotolerance boundary:** “tolerates oxygen exposure up to 24 h” and can use O2 as electron acceptor at “10% v/v of oxygen” (portela2023exploringoxidativestress pages 1-2).

### Candidate nodes (grouped by type; ontology grounding suggestions)

| Node label | Node type | Brief role in aerotolerance | Suggested ontology grounding | Evidence source |
|---|---|---|---|---|
| molecular oxygen (O2) | environmental factor | Primary stressor whose diffusion into anaerobic cells triggers oxygen toxicity; low-to-intermediate O2 exposure defines the phenotype boundary for tolerance rather than use for growth | CHEBI:15379 | Caulat 2024 mBio; Okabe 2023 ISME Comm (caulat2024physiologicalroleand pages 1-2, okabe2023oxygentoleranceand pages 1-2) |
| microaerobic / low-O2 environment | environmental factor | Context in which anaerobes can persist if detoxification and O2-reduction systems are sufficient; relevant to oxic-anoxic interfaces and gut gradients | ENVO:01002357 (microaerobic habitat, candidate) | Caulat 2024 mBio; Portela 2023 Front Microbiol (caulat2024physiologicalroleand pages 1-2, portela2023exploringoxidativestress pages 1-2) |
| oxic-anoxic interface | environmental factor | Natural transition zone selecting for organisms that withstand transient oxygen exposure | ENVO label-only candidate | Portela 2023 Front Microbiol; Dyksma 2024 Microbiome (portela2023exploringoxidativestress pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| gut oxygen gradient | environmental factor | Host-associated O2 gradient creates niches where strict anaerobes still encounter enough O2 to require defense systems | ENVO label-only candidate | Caulat 2024 mBio (caulat2024physiologicalroleand pages 1-2) |
| superoxide anion | ROS | Toxic ROS formed during O2 reduction; central target of SOD/SOR defenses | CHEBI:18421 | Okabe 2023 ISME Comm (okabe2023oxygentoleranceand pages 2-3, okabe2023oxygentoleranceand pages 1-2) |
| hydrogen peroxide | ROS | ROS detoxified by catalase, peroxidases, rubrerythrins, and NADH/NADPH peroxidases | CHEBI:16240 | Okabe 2023 ISME Comm; Kushkevych 2023 Sci Rep (okabe2023oxygentoleranceand pages 11-12, kushkevych2023nadhandnadph pages 1-2) |
| hydroxyl radical | ROS | Highly damaging ROS generated from superoxide/H2O2 chemistry; motivates upstream detoxification of O2•− and H2O2 | CHEBI:16243 | Okabe 2023 ISME Comm (okabe2023oxygentoleranceand pages 2-3) |
| superoxide dismutase (SOD) | enzyme-protein | Converts superoxide to H2O2; higher activity associates with higher O2 tolerance in several anaerobes/aerotolerant strains | EC:1.15.1.1; GO:0004784 | Okabe 2023 ISME Comm; Delaporte 2024 Pathogens; Portela 2023 Front Microbiol (okabe2023oxygentoleranceand pages 11-12, delaporte2024aerotolerancyofcampylobacter pages 8-9, portela2023exploringoxidativestress pages 1-2) |
| catalase (KatA/Cat) | enzyme-protein | Decomposes H2O2 to water and O2; contributes to aerobic-condition survival in some aerotolerant strains | EC:1.11.1.6; GO:0004096 | Okabe 2023 ISME Comm; Delaporte 2024 Pathogens (okabe2023oxygentoleranceand pages 11-12, delaporte2024aerotolerancyofcampylobacter pages 8-9) |
| alkyl hydroperoxide reductase (AhpC) | enzyme-protein | Peroxide reductase induced in aerobic conditions; supports detoxification of peroxides during O2 exposure | EC:1.11.1.26; GO:0018689 | Delaporte 2024 Pathogens; Dyksma 2024 Microbiome (delaporte2024aerotolerancyofcampylobacter pages 8-9, dyksma2024growthofsulfatereducing pages 1-2) |
| peroxiredoxin | enzyme-protein | Peroxide-scavenging enzyme class contributing to ROS defense in oxygen-exposed anaerobes | GO:0051920; EC:1.11.1.15 | Portela 2023 Front Microbiol; Okabe 2023 ISME Comm (portela2023exploringoxidativestress pages 1-2, okabe2023oxygentoleranceand pages 11-12) |
| rubrerythrin / reverse rubrerythrin | enzyme-protein | Peroxidase-active defense proteins; in C. difficile reverse rubrerythrins also partition O2 reduction across low O2 ranges | GO label-only candidate; EC label-only candidate | Caulat 2024 mBio; Dyksma 2024 Microbiome; Portela 2023 Front Microbiol (caulat2024physiologicalroleand pages 1-2, dyksma2024growthofsulfatereducing pages 1-2, portela2023exploringoxidativestress pages 1-2) |
| cytochrome c peroxidase (MacA/Ccp) | enzyme-protein | Reduces peroxides using electron input from partner cytochromes; part of periplasmic oxidative stress defense | EC:1.11.1.5; GO:0004129 | Portela 2023 Front Microbiol; Okabe 2023 ISME Comm (portela2023exploringoxidativestress pages 1-2, okabe2023oxygentoleranceand pages 11-12) |
| NADH peroxidase | enzyme-protein | Uses NADH to reduce H2O2 to water; compensatory peroxide scavenger in anaerobes lacking catalase | EC:1.11.1.1 (candidate); GO label-only candidate | Kushkevych 2023 Sci Rep (kushkevych2023nadhandnadph pages 1-2) |
| NADPH peroxidase | enzyme-protein | Uses NADPH to reduce H2O2 to water; additional peroxide detox route in intestinal SRB | EC:1.11.1.2 (candidate) | Kushkevych 2023 Sci Rep (kushkevych2023nadhandnadph pages 1-2) |
| superoxide reductase / desulfoferrodoxin / neelaredoxin | enzyme-protein | Alternative anaerobe strategy to remove superoxide without canonical SOD | EC:1.15.1.2; GO label-only candidate | Okabe 2023 ISME Comm (okabe2023oxygentoleranceand pages 12-12) |
| flavodiiron protein (FdpA/FdpF) | enzyme-protein | Dedicated O2-reducing enzymes that lower intracellular O2; different paralogs act over different O2 ranges | GO:0016151 (oxidoreductase activity, acting on oxygen); EC label-only candidate | Caulat 2024 mBio (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |
| rubredoxin:oxygen oxidoreductase (Roo/NorV) | enzyme-protein | Cytoplasmic O2-reducing activity implicated in oxygen protection of sulfate reducers | EC label-only candidate | Dyksma 2024 Microbiome (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 5-6) |
| cytochrome bd oxidase (CydAB) | enzyme-protein | Membrane oxidase that consumes O2 and can help protect anaerobic metabolism during transient oxic periods | EC:7.1.1.7 | Dyksma 2024 Microbiome (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 5-6) |
| heme-copper cytochrome c oxidase | enzyme-protein | Membrane O2-reducing oxidase reported in oxygen-tolerant sulfate reducers | EC:7.1.1.9 | Dyksma 2024 Microbiome (dyksma2024growthofsulfatereducing pages 1-2) |
| flavorubredoxin | enzyme-protein | NO/O2 stress defense enzyme family cited as part of anaerobe oxygen/nitrosative stress tolerance arsenal | UniProt/EC label-only candidate | Okabe 2023 ISME Comm (okabe2023oxygentoleranceand pages 12-12) |
| Dps iron-sequestering protein | enzyme-protein | Limits iron-mediated oxidative damage and improves survival under oxidative stress | GO:0006879 (cellular iron ion homeostasis, broad); UniProt label-only candidate | Delaporte 2024 Pathogens (delaporte2024aerotolerancyofcampylobacter pages 11-12) |
| methionine sulfoxide reductase (MsrA/MsrB) | enzyme-protein | Repairs oxidized proteins damaged during O2/ROS exposure | EC:1.8.4.11 / EC:1.8.4.12 | Dyksma 2024 Microbiome; Delaporte 2024 Pathogens (dyksma2024growthofsulfatereducing pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 11-12) |
| thioredoxin reductase (TrxB) | enzyme-protein | Maintains thiol redox balance and supports oxidative stress survival | EC:1.8.1.9; GO:0004791 | Dyksma 2024 Microbiome; Delaporte 2024 Pathogens (dyksma2024growthofsulfatereducing pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 11-12) |
| reactive oxygen species detoxification | pathway-process | Core protective process converting superoxide/peroxides into less harmful products | GO:0098869 | Okabe 2023 ISME Comm; Dyksma 2024 Microbiome (okabe2023oxygentoleranceand pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| oxygen reduction / oxygen scavenging | pathway-process | Consumption of O2 without aerobic growth lowers intracellular O2 and mitigates toxicity | GO:0015671 (oxygen transport, not exact); pathway label-only candidate | Caulat 2024 mBio; Dyksma 2024 Microbiome (caulat2024physiologicalroleand pages 1-2, dyksma2024growthofsulfatereducing pages 5-6) |
| hydrogen peroxide catabolism | pathway-process | Downstream detox process essential after superoxide dismutation or direct peroxide exposure | GO:0042744 | Okabe 2023 ISME Comm; Kushkevych 2023 Sci Rep (okabe2023oxygentoleranceand pages 11-12, kushkevych2023nadhandnadph pages 1-2) |
| oxidative stress response | pathway-process | Broad adaptive response encompassing detox enzymes, repair, and regulatory induction | GO:0006979 | Delaporte 2024 Pathogens; Dyksma 2024 Microbiome (delaporte2024aerotolerancyofcampylobacter pages 8-9, dyksma2024growthofsulfatereducing pages 1-2) |
| repair of oxidized proteins | pathway-process | Restores function after ROS damage and improves persistence during periodic O2 exposure | GO label-only candidate | Dyksma 2024 Microbiome (dyksma2024growthofsulfatereducing pages 1-2) |
| sigma B (σB) | regulator | Alternative sigma factor controlling O2-reductase genes and oxygen stress adaptation in C. difficile | GO:0003899 (broad RNA polymerase activity, not exact); regulator label-only candidate | Caulat 2024 mBio (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 13-15) |
| sigma A (σA) | regulator | Basal/dual promoter control for specific O2-reductase genes at very low O2 tensions | regulator label-only candidate | Caulat 2024 mBio (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17) |
| OseR (Spx-family regulator) | regulator | O2-responsive repressor of fdp/revRbr genes in anaerobiosis; derepressed upon O2 exposure | regulator label-only candidate | Caulat 2024 mBio (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11) |
| Rex | regulator | Senses NADH/NAD+ ratio and regulates redox-linked O2 defense, especially fdpF | GO label-only candidate | Caulat 2024 mBio; Dyksma 2024 Microbiome (caulat2024physiologicalroleand pages 13-15, dyksma2024growthofsulfatereducing pages 5-6) |
| PerR | regulator | Oxidative stress regulator implicated in aerotolerance in Campylobacter, though not in C. difficile O2-reductase control | regulator label-only candidate | Delaporte 2024 Pathogens; Caulat 2024 mBio (delaporte2024aerotolerancyofcampylobacter pages 8-9, caulat2024physiologicalroleand pages 13-15) |
| CosR | regulator | Campylobacter oxidative-stress regulator affecting aerotolerance-associated gene expression | regulator label-only candidate | Delaporte 2024 Pathogens (delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 8-9) |
| Fur / iron-dependent regulation | regulator | Iron status influences oxidative stress regulation and peroxide-defense gene expression in Campylobacter | GO:0006879 (broad iron homeostasis); regulator label-only candidate | Delaporte 2024 Pathogens (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| PpcA–MacA redox complex | complex or electron-transfer component | Periplasmic cytochrome-peroxidase complex that channels electrons into peroxide detoxification | complex label-only candidate | Portela 2023 Front Microbiol (portela2023exploringoxidativestress pages 1-2) |
| PpcA-E triheme periplasmic cytochromes | complex or electron-transfer component | Electron donors supplying reducing power to MacA during oxidative stress defense | UniProt label-only candidate | Portela 2023 Front Microbiol (portela2023exploringoxidativestress pages 1-2) |
| MacA diheme peroxidase | complex or electron-transfer component | Peroxide-detoxifying acceptor of electrons from Ppc cytochromes | UniProt label-only candidate | Portela 2023 Front Microbiol (portela2023exploringoxidativestress pages 1-2) |
| rubredoxin | complex or electron-transfer component | Electron carrier supporting O2 scavenging systems in anaerobes | CHEBI label not applicable; protein label-only candidate | Okabe 2023 ISME Comm; Dyksma 2024 Microbiome (okabe2023oxygentoleranceand pages 12-12, dyksma2024growthofsulfatereducing pages 5-6) |
| NADH:rubredoxin oxidoreductase | complex or electron-transfer component | Transfers electrons from NADH to rubredoxin-linked O2 detox systems | EC label-only candidate | Okabe 2023 ISME Comm (okabe2023oxygentoleranceand pages 12-12) |
| NADH/NAD+ redox balance | complex or electron-transfer component | Redox state constrains expression and performance of O2-reducing enzymes, especially Rex-regulated systems | CHEBI:57945 / CHEBI:57540 | Caulat 2024 mBio (caulat2024physiologicalroleand pages 13-15) |


*Table: This table lists evidence-backed candidate nodes for a TraitMech causal graph of the aerotolerant phenotype. It groups environmental, molecular, enzymatic, regulatory, and electron-transfer components that recent sources link to anaerobe survival under oxygen exposure.*

### Candidate causal edges (evidence-backed triples)

| Subject node | Predicate | Object node | Evidence snippet (verbatim short quote) | Citation (with DOI/URL when possible) | Curation notes |
|---|---|---|---|---|---|
| superoxide dismutase (SOD) activity | increases | oxygen tolerance | "This Sod-Cat dependent detoxification system could be responsible for the higher O2 tolerance of Scalindua" | Okabe et al. 2023, ISME Communications, https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12) | Cross-taxon mechanistic edge; quantitative support in anammox: Sod activity 22.6 ± 1.9 U/mg-protein in Scalindua. Taxon-specific evidence but broadly plausible. |
| catalase (Cat) activity | enables | hydrogen peroxide detoxification | "catalase degrades H2O2 rapidly at higher concentrations" | Okabe et al. 2023, ISME Communications, https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 11-12) | Strong biochemical edge; generic to many microbes, not specific to aerotolerant phenotype alone. |
| rubrerythrin (Rbr) | decreases | hydrogen peroxide | "rubrerythrins scavenge low H2O2 levels" | Okabe et al. 2023, ISME Communications, https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 11-12) | Good candidate edge; role may vary by taxon and peroxide concentration. |
| flavodiiron protein FdpA | enables | tolerance to 0.4%–1% O2 | "FdpA to low and intermediate O2 tensions (0.4%–1%)" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 1-2) | Strong, directly quantified, but C. difficile-specific. Suitable as taxon-specific mechanistic edge. |
| reverse rubrerythrin revRbr2 | enables | tolerance to <0.4% O2 | "revRbr2 is specific to low O2 tensions (<0.4%)" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 1-2) | Strong C. difficile-specific edge with explicit O2 range. |
| reverse rubrerythrin revRbr1 | enables | tolerance to 0.1%–4% O2 | "revRbr1 has a wider spectrum of activity (0.1%–4%)" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 1-2) | Strong C. difficile-specific edge; useful for graded O2-tolerance modeling. |
| flavodiiron protein FdpF | enables | tolerance to >4% O2 and air | "FdpF is more specific to tensions > 4% and air" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 1-2) | Strong C. difficile-specific edge; especially relevant for brief high-O2 exposure. |
| fdpA disruption | decreases | survival at 1% O2 | "fdpA::erm and double fdp mutants show near-complete loss of survival after 48 h at 1% O2" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5) | Strong genetic evidence; assay-specific survival phenotype in C. difficile. |
| revrbr1/revrbr2 double disruption | decreases | survival at 1% O2 | "A double revrbr mutant shows large survival losses (2-log at 24 h; 6-log at 48 h)" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5) | Strong genetic evidence with quantitative log-loss values; C. difficile-specific. |
| FdpF | causes | oxygen reduction activity | "FdpF is a standalone enzyme, receiving electrons directly from NADH" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 1-2) | Strong mechanistic enzyme-function edge. Distinct from tolerance phenotype but likely causal upstream. |
| NADH | enables | FdpF-mediated oxygen reduction | "receiving electrons directly from NADH" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 1-2) | Strong biochemical edge; taxon-specific to FdpF-like class F flavodiiron proteins. |
| FdpA and revRbrs | required_for | electron donor partners | "cannot directly take electrons from NADH and therefore need partners" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 1-2) | Strong but incomplete edge because actual partners remain unidentified; curate with uncertainty on object specificity. |
| sigma B (σB) | regulates | O2-reductase genes | "The genes encoding the four O2-reductases are controlled by the alternative sigma factor σB" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 13-15) | Strong regulatory edge in C. difficile. Good candidate for taxon-specific graph branch. |
| sigma A (σA) | regulates | revrbr2 and fdpA | "revrbr2 and fdpA are also transcribed by σA" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17) | Strong regulatory edge but gene-specific and taxon-specific. |
| OseR (Spx-family regulator) | decreases | fdp/revrbr expression in anaerobiosis | "represses fdp and revrbr genes in anaerobiosis" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 9-11) | Strong regulatory edge; C. difficile-specific. |
| O2 exposure | decreases | OseR repression of fdp/revrbr genes | "this repression is released upon long-term exposure to 1% O2" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 15-17) | Causal direction inferred from text; should be marked moderately uncertain if strict triple semantics are required. |
| Rex | decreases | fdpF expression | "Rex represses fdpF (sensing NADH/NAD+ ratio)" | Caulat et al. 2024, mBio, https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 11-13) | Strong regulatory edge in C. difficile; broader applicability uncertain. |
| PpcA-E triheme cytochromes | enables | MacA peroxidase activity | "complete electron transfer from the cytochromes to the high-potential heme of MacA" | Portela et al. 2023, Frontiers in Microbiology, https://doi.org/10.3389/fmicb.2023.1253114 (portela2023exploringoxidativestress pages 1-2) | Strong electron-transfer edge in G. sulfurreducens; taxon-specific but mechanistically valuable. |
| PpcA-E triheme cytochromes | increases | oxidative stress protection | "providing the necessary reducing power to mitigate oxidative stress situations" | Portela et al. 2023, Frontiers in Microbiology, https://doi.org/10.3389/fmicb.2023.1253114 (portela2023exploringoxidativestress pages 1-2) | Mechanistic interpretation from authors; taxon-specific. |
| Geobacter sulfurreducens oxidative-stress enzyme repertoire | enables | aerotolerance | "tolerates oxygen exposure up to 24 h and can utilize this molecule as electron acceptor under microaerobic conditions (10% v/v of oxygen)" | Portela et al. 2023, Frontiers in Microbiology, https://doi.org/10.3389/fmicb.2023.1253114 (portela2023exploringoxidativestress pages 1-2) | Broad phenotype edge for a species, not a single-entity causal edge; may be too composite for direct YAML curation. |
| NADH peroxidase | decreases | hydrogen peroxide | "NADH + H+ + H2O2 ⇋ NAD+ + 2 H2O" | Kushkevych et al. 2023, Scientific Reports, https://doi.org/10.1038/s41598-023-41185-3 (kushkevych2023nadhandnadph pages 1-2) | Strong biochemical edge; evidence from intestinal sulfate-reducing bacteria cell-free extracts. |
| NADPH peroxidase | decreases | hydrogen peroxide | "an analogous NADPH peroxidase produces NADP+" | Kushkevych et al. 2023, Scientific Reports, https://doi.org/10.1038/s41598-023-41185-3 (kushkevych2023nadhandnadph pages 1-2) | Strong biochemical edge; organism-specific assay context. |
| NADH/NADPH peroxidases | enables | antioxidant defense | "putative antioxidant defense systems of intestinal SRB" | Kushkevych et al. 2023, Scientific Reports, https://doi.org/10.1038/s41598-023-41185-3 (kushkevych2023nadhandnadph pages 1-2) | Useful but somewhat inferential; authors frame as putative defense systems. Mark uncertain. |
| rubredoxin:oxygen oxidoreductase (Roo/NorV) | enables | oxygen protection | "Key O2-reducing enzymes identified include cytoplasmic rubredoxin:oxygen oxidoreductase/nitric oxide reductase (Roo/NorV)" | Dyksma & Pester 2024, Microbiome, https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 5-6) | Strong candidate edge for SRB, but transcript-level and genome-centric evidence rather than mutant validation. |
| cytochrome bd oxidase (CydAB) | enables | oxygen consumption during oxic stress | "all MAGs encoded cytochrome bd-type oxidases" | Dyksma & Pester 2024, Microbiome, https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 5-6) | Genomic/transcriptomic support only; functional role inferred from annotation and literature. Moderate uncertainty. |
| katA (catalase) | increases | aerotolerance | "katA mutants being more sensitive to H2O2 and aerobic conditions" | Delaporte et al. 2024, Pathogens, https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 8-9) | Strong in Campylobacter; microaerophile rather than anaerobe, so curation into generic aerotolerant-anaerobe graph should be cautious. |
| sodB (superoxide dismutase) | increases | aerotolerance | "aerotolerant strains show increased SOD activity/expression while sodB mutants are more susceptible" | Delaporte et al. 2024, Pathogens, https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 8-9) | Strong oxidative-stress edge, but derived from Campylobacter. |
| ahpC | increases | aerotolerance | "ahpC expression increases in aerobic conditions and its mutation impairs aerotolerance" | Delaporte et al. 2024, Pathogens, https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 8-9) | Strong in Campylobacter; oxygen-class boundary differs from strict anaerobes. |
| PerR inactivation | increases | aerotolerance | "perR inactivation raises resistance to H2O2 and upregulates katA, ahpC, rrc, and trxB" | Delaporte et al. 2024, Pathogens, https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 9-11) | Strong regulator edge in Campylobacter; not universal and opposite logic may not generalize across taxa. |
| high SOD and moderate catalase activities | increases | O2 tolerance of Scalindua | "only Scalindua exhibited high Sod activity of 22.6 ± 1.9 U/mg-protein with moderate Cat activity of 1.6 ± 0.7 U/mg-protein" | Okabe et al. 2023, ISME Communications, https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 1-2) | Quantitative comparative evidence; species-specific, but valuable for curation notes. |


*Table: This table lists evidence-backed subject-predicate-object edges for an aerotolerant anaerobe causal graph, with direct quotes, DOI/URL citations, and notes on taxon specificity and uncertainty. It is designed to support curation into a TraitMech YAML graph.*

### Visual evidence excerpts

Caulat et al. (2024) contains figures summarizing (i) survival of mutants at 1% and 4% O2 and (ii) a schematic mapping “Spectrum of activity of the O2-reductases” across O2 tensions; cropped excerpts were retrieved (caulat2024physiologicalroleand media fe4e8254, caulat2024physiologicalroleand media ba0d2fcb).

### Expert synthesis / analysis (what authoritative sources imply)

**Aerotolerance as an “enzyme systems” trait rather than a taxonomy label.** Across disparate taxa (anammox Planctomycetota, Firmicutes pathogens, SRB, electroactive *Geobacter*), oxygen tolerance correlates with (i) presence/levels of ROS detox enzymes and (ii) ability to rapidly remove O2 via dedicated O2-reductases or oxidases, often coordinated by redox and stress regulators (okabe2023oxygentoleranceand pages 1-2, caulat2024physiologicalroleand pages 11-13, dyksma2024growthofsulfatereducing pages 1-2, portela2023exploringoxidativestress pages 1-2). This suggests TraitMech curation should treat aerotolerance as an emergent property of *linked modules* (O2 reduction + ROS detox + repair + regulation) rather than any single marker gene.

**Graph design implication.** Evidence supports at least two mechanistic “routes” to curate:
1) **ROS-first route:** O2 exposure → ROS (O2•−, H2O2) → detox enzymes (SOD, catalase, peroxidases, rubrerythrin, peroxiredoxins) → improved survival/tolerance (okabe2023oxygentoleranceand pages 2-3, okabe2023oxygentoleranceand pages 11-12, okabe2023oxygentoleranceand pages 1-2).  
2) **O2-removal route:** O2 exposure → O2-reductases/oxidases (Fdp, revRbr, Roo/NorV, CydAB) consuming NADH/reducing power → decreased intracellular O2 / reduced ROS formation → improved survival; gated by regulators (σB/OseR/Rex) (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 13-15, dyksma2024growthofsulfatereducing pages 5-6).

### Warnings / curation cautions

1. **Taxon-specific edges vs trait-general edges.** Many strongest mechanistic results (O2 range partitioning; mutant survival log-loss) are from *C. difficile* and should be tagged taxon-specific if curated into a general “aerotolerant” trait graph (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 2-5).  
2. **Transcriptomic presence ≠ causal necessity.** For SRB under periodic oxic pulses, some O2-reduction/detox links are genome-centric or transcript-level and not validated by mutants; these edges should be curated as *uncertain/inferred* unless additional functional validation is added (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 1-2).  
3. **Campylobacter is a boundary example.** *Campylobacter* aerotolerance mechanisms are informative (ROS detox, PerR/CosR regulation), but the organism is microaerophilic rather than a strict anaerobe; edges may not transfer cleanly to anaerobe-focused TraitMech graphs and should be flagged as boundary/contrast evidence (delaporte2024aerotolerancyofcampylobacter pages 8-9, delaporte2024aerotolerancyofcampylobacter pages 9-11).  
4. **Avoid over-claiming “does not use O2.”** Some organisms labeled aerotolerant may also use O2 as an electron acceptor under microaerobic conditions (e.g., *G. sulfurreducens*), so the trait definition should be applied carefully depending on the ontology’s intended meaning (tolerance only vs microaerobic respiration) (portela2023exploringoxidativestress pages 1-2).

---

## DOI-first bibliography (2023–2024 prioritized)

1. **Caulat LC, et al.** *Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe Clostridioides difficile.* mBio. **Oct 2024.** https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 11-13)  
2. **Delaporte E, Karki AB, Fakhr MK.** *Aerotolerancy of Campylobacter spp.: A Comprehensive Review.* Pathogens. **Sep 2024.** https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 8-9, delaporte2024aerotolerancyofcampylobacter pages 9-11)  
3. **Dyksma S, Pester M.** *Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O2 saturation.* Microbiome. **Oct 2024.** https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 5-6)  
4. **Portela PC, et al.** *Exploring oxidative stress pathways in Geobacter sulfurreducens: the redox network between MacA peroxidase and triheme periplasmic cytochromes.* Frontiers in Microbiology. **Oct 2023.** https://doi.org/10.3389/fmicb.2023.1253114 (portela2023exploringoxidativestress pages 1-2)  
5. **Kushkevych I, et al.** *NADH and NADPH peroxidases as antioxidant defense mechanisms in intestinal sulfate-reducing bacteria.* Scientific Reports. **Aug 2023.** https://doi.org/10.1038/s41598-023-41185-3 (kushkevych2023nadhandnadph pages 1-2)  
6. **Okabe S, et al.** *Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria.* ISME Communications. **May 2023.** https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12, okabe2023oxygentoleranceand pages 2-3)  
7. **Keating C, et al.** *Microbial single-cell applications under anoxic conditions.* Applied and Environmental Microbiology. **Nov 2024.** https://doi.org/10.1128/aem.01321-24 (terminology: anoxic/anaerobic; oxygen classes) (keating2024microbialsinglecellapplications pages 1-2)


References

1. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

2. (portela2023exploringoxidativestress pages 1-2): Pilar C. Portela, Leonor Morgado, Marta A. Silva, Lukas Denkhaus, Oliver Einsle, and Carlos A. Salgueiro. Exploring oxidative stress pathways in geobacter sulfurreducens: the redox network between maca peroxidase and triheme periplasmic cytochromes. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1253114, doi:10.3389/fmicb.2023.1253114. This article has 8 citations and is from a peer-reviewed journal.

3. (caulat2024physiologicalroleand pages 11-13): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

4. (delaporte2024aerotolerancyofcampylobacter pages 8-9): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

5. (keating2024microbialsinglecellapplications pages 1-2): Ciara Keating, Kerstin Fiege, Martijn Diender, Diana Z. Sousa, and Laura Villanueva. Microbial single-cell applications under anoxic conditions. Nov 2024. URL: https://doi.org/10.1128/aem.01321-24, doi:10.1128/aem.01321-24. This article has 4 citations and is from a peer-reviewed journal.

6. (okabe2023oxygentoleranceand pages 2-3): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

7. (okabe2023oxygentoleranceand pages 11-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

8. (dyksma2024growthofsulfatereducing pages 5-6): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

9. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

10. (caulat2024physiologicalroleand pages 2-5): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (caulat2024physiologicalroleand pages 15-17): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (caulat2024physiologicalroleand pages 13-15): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

14. (kushkevych2023nadhandnadph pages 1-2): Ivan Kushkevych, Dani Dordević, Mohammad I. Alberfkani, Márió Gajdács, Eszter Ostorházi, Monika Vítězová, and Simon K.-M. R. Rittmann. Nadh and nadph peroxidases as antioxidant defense mechanisms in intestinal sulfate-reducing bacteria. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41185-3, doi:10.1038/s41598-023-41185-3. This article has 17 citations and is from a peer-reviewed journal.

15. (okabe2023oxygentoleranceand pages 12-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

16. (delaporte2024aerotolerancyofcampylobacter pages 11-12): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

17. (caulat2024physiologicalroleand pages 9-11): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

18. (delaporte2024aerotolerancyofcampylobacter pages 9-11): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

19. (caulat2024physiologicalroleand media fe4e8254): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

20. (caulat2024physiologicalroleand media ba0d2fcb): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.