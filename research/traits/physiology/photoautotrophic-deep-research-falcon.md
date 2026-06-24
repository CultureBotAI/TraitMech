---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:15:03.831369'
end_time: '2026-06-18T12:36:15.009174'
duration_seconds: 1271.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photoautotrophic
  trait_identifier: METPO:1000656
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of light as the energy source
    and carbon dioxide as the primary carbon source for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation,
    anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation,
    photoautotroph, photoautotrophy
  evidence_summary: 'DOI:10.3390/life10050071: capture solar energy (Review supports
    cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10:
    Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson
    cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis
    sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic
    cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation
    (Kaneko et al. 1996, DNA Res, full genome).)'
  causal_graph_summary: 'photoautotrophic_cyanobacterial_carbon_fixation: 11 nodes,
    8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoautotrophic
- **METPO identifier:** METPO:1000656
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation, anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation, photoautotroph, photoautotrophy
- **Existing evidence:** DOI:10.3390/life10050071: capture solar energy (Review supports cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** photoautotrophic_cyanobacterial_carbon_fixation: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **photoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoautotrophic.yaml`.

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
- **Trait label:** photoautotrophic
- **METPO identifier:** METPO:1000656
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation, anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation, photoautotroph, photoautotrophy
- **Existing evidence:** DOI:10.3390/life10050071: capture solar energy (Review supports cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** photoautotrophic_cyanobacterial_carbon_fixation: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **photoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoautotrophic.yaml`.

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


## Microbial trait causal-graph report: **photoautotrophic** (METPO:1000656)

**Trait label:** photoautotrophic  
**METPO identifier:** METPO:1000656  
**Trait category:** PHYSIOLOGY  
**Curated definition (given):** “A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.”

### Scope summary (what the trait represents)
Microbial **photoautotrophy** is best treated as a *physiological capacity* to (i) harvest **light** energy through photosynthetic reaction centers/electron transport to generate ATP and reductant, and (ii) use that energy to assimilate **inorganic carbon (CO2/HCO3−)** into biomass through an autotrophic carbon-fixation pathway (most commonly the **Calvin–Benson–Bassham (CBB) cycle** in cyanobacteria; often **reverse TCA** in some anoxygenic phototrophs such as green sulfur bacteria). (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2)

**Boundary cases / nearby traits:**
- **Oxygenic photoautotrophy (cyanobacteria):** electrons originate from **water oxidation** and O2 is produced. Carbon fixation typically uses the **CBB cycle** and is frequently supported by a **carbon concentrating mechanism (CCM)** involving bicarbonate transport and **carboxysomes**. (grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2)
- **Anoxygenic photoautotrophy:** does not evolve O2; uses reduced electron donors such as **H2S** (also H2 or reduced metals in some cases). Green sulfur bacteria (GSB) are highlighted as **photoautotrophs** that use CO2 and assimilate it via **reverse TCA** and often employ **chlorosomes** as antenna structures. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Aerobic anoxygenic phototrophs (AAP):** these are **photoheterotrophs** (heterotrophic growth relying on organic carbon; light supplements energy). They should *not* be curated under “photoautotrophic” unless independent evidence shows inorganic-carbon-based biomass formation. (stojan2024ecologyofaerobic pages 1-2, villenaalemany2024phenologyandecological pages 1-2, piwosz2024responseofaerobic pages 1-2)

### Key concepts and current understanding (2024 focus)
#### 1) Oxygenic photoautotrophy (cyanobacterial core mechanism)
A recent 2024 review describes cyanobacterial oxygenic photosynthesis as light harvested by antennae and passed to **photosystems II and I**; electrons originate from **photo-oxidation of water at PSII**, transit via plastoquinone/cytochrome b6f to PSI, and are transferred to ferredoxin/NADP+ to produce **NADPH**, while a proton gradient drives **ATP** synthesis. The reductant and ATP power **CO2 fixation via the CBB (Calvin) cycle**. (grettenberger2024limitingfactorsin pages 1-2)

#### 2) Cyanobacterial CO2 concentrating mechanism (CCM)
Two 2024 cyanobacteria-focused syntheses provide a current “parts list” for cyanobacterial CCMs:
- **Inorganic carbon uptake systems**: bicarbonate transporters **SbtA**, **BicA**, **BCT1**, plus specialized thylakoid-associated CO2 uptake complexes **NDH-13** and **NDH-14** that convert CO2 to HCO3−. (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, lucius2024theprimarycarbon pages 1-2)
- **Carboxysomes**: protein microcompartments encapsulating **RuBisCO** and **carbonic anhydrase (CA)**. HCO3− enters, CA generates CO2 inside, and the shell helps retain CO2 to elevate CO2 near RuBisCO and reduce oxygenation/ photorespiratory loss. (kurkela2024inorganiccarbonsensing pages 4-4, lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3)
- **Quantitative effect (review-level):** one 2024 review reports the CCM can suppress RuBisCO oxygenase activity to below ~1% by enriching intracellular inorganic carbon. (lucius2024theprimarycarbon pages 1-2)

A schematic of these CCM components (transporters + NDH complexes + carboxysome) is explicitly depicted in the Kurkela & Tyystjärvi 2024 minireview figures. (kurkela2024inorganiccarbonsensing media f4366bfa, kurkela2024inorganiccarbonsensing media b6613ad5)

#### 3) Carbon sensing/signaling and regulation (cyanobacteria)
The 2024 minireview on inorganic carbon sensing/signaling identifies:
- **Transcriptional regulators** of CCM genes (e.g., **CcmR/NdhR**, **CmpR**, **RbcR**) (kurkela2024inorganiccarbonsensing pages 1-2)
- **Metabolic signaling metabolites**: **2-oxoglutarate (2-OG)** and **2-phosphoglycolate (2-PG)**; 2-PG is linked to low Ci via photorespiration, while 2-OG reflects cellular C/N balance. These metabolites modulate CcmR and activate CmpR. (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 4-4)
- Example regulatory edges: **CmpR activates the cmp operon/BCT1** under low CO2, with **2-PG and RuBP** as co-activators; **2-OG and NADP+** can activate CcmR leading to downregulation of sbtA/bicA under high CO2. (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 5-5)

#### 4) Anoxygenic photoautotrophy (GSB emphasized)
A 2024 Frontiers in Microbiology review splits light-dependent bacterial metabolism into oxygenic and anoxygenic; it states that in anoxygenic photosynthesis **H2S** is used as the main electron donor (rather than water), GSB oxidize H2S to elemental sulfur, and CO2 is assimilated via the **reverse TCA cycle**. It also highlights **chlorosomes** as specialized light-harvesting structures in GSB. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

### Candidate nodes (curation targets)
The following node inventory is compiled from 2023–2024 evidence and includes suggested ontology grounding where available.

| Category | Node label | Suggested identifier | Evidence basis |
|---|---|---|---|
| Phenotype | photoautotrophic | METPO:1000656 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Phenotype | oxygenic photoautotrophy |  | (grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Phenotype | anoxygenic photoautotrophy |  | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| Pathway/module | oxygenic photosynthesis | GO:0015979 | (grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Pathway/module | anoxygenic photosynthesis | GO:0015978 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| Pathway/module | photosynthetic electron transport chain | GO:0009767 | (grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Pathway/module | Calvin-Benson-Bassham cycle | GO:0019253 | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3) |
| Pathway/module | carbon-concentrating mechanism |  | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing media f4366bfa) |
| Pathway/module | reverse tricarboxylic acid cycle | GO:0072351 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, fixacao2024universidadefederaldo pages 52-54, fixacao2024universidadefederaldo pages 54-58) |
| Pathway/module | photorespiration | GO:0009853 | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3) |
| Protein complex/system | photosystem II | GO:0009523 | (grettenberger2024limitingfactorsin pages 1-2) |
| Protein complex/system | photosystem I | GO:0009522 | (grettenberger2024limitingfactorsin pages 1-2) |
| Protein complex/system | cytochrome b6f complex | GO:0009512 | (grettenberger2024limitingfactorsin pages 1-2) |
| Protein complex/system | ferredoxin-dependent electron transfer system |  | (grettenberger2024limitingfactorsin pages 1-2) |
| Protein complex/system | BCT1 bicarbonate transporter |  | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3) |
| Protein complex/system | SbtA bicarbonate transporter |  | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3) |
| Protein complex/system | BicA bicarbonate transporter |  | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 5-5) |
| Protein complex/system | NDH-13/CupA CO2 uptake complex |  | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 5-5) |
| Protein complex/system | NDH-14/CupB CO2 uptake complex |  | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 5-5) |
| Protein complex/system | type II reaction center (AAP/anoxygenic) |  | (stojan2024ecologyofaerobic pages 1-2, villenaalemany2024phenologyandecological pages 1-2) |
| Gene/protein/regulator | RubisCO |  | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3) |
| Gene/protein/regulator | carbonic anhydrase |  | (kurkela2024inorganiccarbonsensing pages 1-2, lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3) |
| Gene/protein/regulator | CcmR/NdhR |  | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 8-8, kurkela2024inorganiccarbonsensing pages 9-10) |
| Gene/protein/regulator | CmpR |  | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 5-5) |
| Gene/protein/regulator | RbcR |  | (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 8-8) |
| Gene/protein/regulator | SbtB |  | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 5-5) |
| Metabolite/chemical | carbon dioxide | CHEBI:16526 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2) |
| Metabolite/chemical | bicarbonate | CHEBI:17544 | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3) |
| Metabolite/chemical | water | CHEBI:15377 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Metabolite/chemical | dioxygen | CHEBI:15379 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2) |
| Metabolite/chemical | hydrogen sulfide | CHEBI:16136 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| Metabolite/chemical | NADPH | CHEBI:16474 | (grettenberger2024limitingfactorsin pages 1-2) |
| Metabolite/chemical | ATP | CHEBI:15422 | (grettenberger2024limitingfactorsin pages 1-2) |
| Metabolite/chemical | 2-phosphoglycolate | CHEBI:17363 | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 5-5) |
| Metabolite/chemical | 2-oxoglutarate | CHEBI:16810 | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 8-8) |
| Metabolite/chemical | ribulose-1,5-bisphosphate | CHEBI:16710 | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 5-5) |
| Cellular structure/compartment | carboxysome | GO:0031469 | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing media f4366bfa) |
| Cellular structure/compartment | thylakoid membrane | GO:0042651 | (lucius2024theprimarycarbon pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3) |
| Cellular structure/compartment | chlorosome | GO:0019027 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| Environmental factor/condition | light | ENVO:01001148 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, grettenberger2024limitingfactorsin pages 1-2, lucius2024theprimarycarbon pages 1-2, moran2023daylightdrivencarbonexchange pages 1-2) |
| Environmental factor/condition | low CO2 / low inorganic carbon |  | (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 8-8, kurkela2024inorganiccarbonsensing pages 5-5) |
| Environmental factor/condition | alkaline pH |  | (kurkela2024inorganiccarbonsensing pages 2-3, grivalsky2024polyβhydroxybutyrateproductionby pages 1-2) |
| Assay/measurement | 13C-bicarbonate tracer uptake assay |  | (moran2023daylightdrivencarbonexchange pages 9-10, moran2023daylightdrivencarbonexchange pages 5-7, moran2023daylightdrivencarbonexchange pages 1-2) |
| Assay/measurement | stable-isotope proteomics |  | (moran2023daylightdrivencarbonexchange pages 9-10, moran2023daylightdrivencarbonexchange pages 7-8, moran2023daylightdrivencarbonexchange pages 1-2) |
| Assay/measurement | pufM gene metabarcoding |  | (stojan2024ecologyofaerobic pages 1-2, villenaalemany2024phenologyandecological pages 1-2) |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial photoautotrophy, grouped by node type and annotated with suggested ontology identifiers where reasonably supported. It is useful as a starting point for YAML curation because it ties each node to explicit evidence contexts from the retrieved literature.*

### Evidence-backed candidate causal edges (triples)
The following evidence-backed subject–predicate–object triples are proposed as candidates for a TraitMech causal graph for photoautotrophy.

| Edge (subject–predicate–object) | Evidence snippet | Reference (DOI + year) | Notes/uncertainty |
|---|---|---|---|
| Photosystem II (PSII) — oxidizes — H2O | “In oxygenic photosynthesis electrons originate from the photo-oxidation of water at PSII” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) | Oxygenic cyanobacteria-specific. |
| PSII electron transport chain — produces — proton gradient/ATP | Electrons pass through plastoquinone and cytochrome b6f; “a proton gradient generates ATP” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) | Oxygenic cyanobacteria-specific; ATP synthase not explicitly named in evidence snippet. |
| Photosystem I (PSI) electron transfer — produces — NADPH | Electrons are transferred to ferredoxin and NADP+ “to produce NADPH” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) | Oxygenic cyanobacteria-specific. |
| Light-driven photosynthetic electron transport — enables — Calvin–Benson–Bassham (CBB) cycle carbon fixation | Cyanobacteria “use light energy to drive a photosynthetic electron transport chain” and “CO2 fixation… occurs via the Calvin-Benson-Bassham (CBB) cycle” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680 (2024) | Mechanistic coupling stated at pathway level. |
| RubisCO — catalyzes first step of — CBB cycle | Carboxysomes contain RubisCO; “RubisCo… catalyzes the first step of the Calvin–Benson–Bassham cycle” (kurkela2024inorganiccarbonsensing pages 3-3) | 10.1111/ppl.14140 (2024) | Strong evidence for cyanobacterial CCM/CBB context. |
| Carbon-concentrating mechanism (CCM) — lowers — RubisCO oxygenase activity | The CCM “lowers RubisCO's oxygenase reaction to below ~1% by enriching intracellular inorganic carbon” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680 (2024) | Cyanobacterial model systems; quantitative but review-level. |
| BCT1 transporter — imports — HCO3− | “BCT1… [is an] ATP-driven pump” / “ABC-type high-affinity HCO3− pump” (kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 3-3) | 10.1111/ppl.14140 (2024) | Cyanobacterial CCM component; membrane uptake edge. |
| SbtA transporter — imports — HCO3− | “SbtA [is an] HCO3−/Na+ symporter” and part of cyanobacterial Ci uptake systems (kurkela2024inorganiccarbonsensing pages 2-3, lucius2024theprimarycarbon pages 1-2) | 10.1111/ppl.14140 (2024); 10.3389/fpls.2024.1417680 (2024) | Cyanobacterial CCM component; Na+-dependent. |
| BicA transporter — imports — HCO3− | “BicA [is an] HCO3−/Na+ symporter” and overexpression “increases photosynthetic activity, glycogen production and biomass” (kurkela2024inorganiccarbonsensing pages 2-3) | 10.1111/ppl.14140 (2024) | Cyanobacterial CCM component; uptake and phenotype support. |
| NDH-13 / NDH-14 complexes — convert — CO2 to HCO3− | “NDH-13/CupA and NDH-14/CupB convert CO2 to HCO3− in the cytoplasm” (kurkela2024inorganiccarbonsensing pages 2-3) | 10.1111/ppl.14140 (2024) | Cyanobacterial CCM component; taxon-specific. |
| Cytoplasmic HCO3− — diffuses into — carboxysome | “Cytoplasmic HCO3− diffuses into the carboxysome” (kurkela2024inorganiccarbonsensing pages 3-3) | 10.1111/ppl.14140 (2024) | Strong for cyanobacteria; physical transport step. |
| Carboxysomal carbonic anhydrase — converts — HCO3− to CO2 | In carboxysomes, “CA produces CO2” / “bicarbonate is converted back to CO2 by CA inside carboxysomes” (kurkela2024inorganiccarbonsensing pages 3-3, lucius2024theprimarycarbon pages 1-2) | 10.1111/ppl.14140 (2024); 10.3389/fpls.2024.1417680 (2024) | Core CCM edge. |
| Carboxysome shell — retains — CO2 near RubisCO | Carboxysomes “raise CO2 near the enzyme”; shell “prevents CO2 loss” (kurkela2024inorganiccarbonsensing pages 1-2, lucius2024theprimarycarbon pages 1-2) | 10.1111/ppl.14140 (2024); 10.3389/fpls.2024.1417680 (2024) | Strong cyanobacterial CCM evidence. |
| 2-Phosphoglycolate (2-PG) — activates — CmpR | “2-phosphoglycolate and ribulose-1,5-bisphosphate activate CmpR” (kurkela2024inorganiccarbonsensing pages 1-2) | 10.1111/ppl.14140 (2024) | Regulatory metabolite edge; cyanobacterial CCM regulation. |
| CmpR — activates expression of — BCT1/cmp operon | “cmpABCD is activated by the transcription factor CmpR in low CO2” (kurkela2024inorganiccarbonsensing pages 4-4) | 10.1111/ppl.14140 (2024) | Strong regulatory edge; low-Ci responsive. |
| 2-Oxoglutarate (2-OG) + NADP+ — activate — CcmR/NdhR repressor | “2-oxoglutarate (2-OG) and NADP+ can activate CcmR to downregulate sbtA and bicA under high CO2” (kurkela2024inorganiccarbonsensing pages 4-4) | 10.1111/ppl.14140 (2024) | Regulatory edge; condition-specific. |
| CcmR/NdhR — represses — sbtA and bicA | CcmR activation “downregulate[s] sbtA and bicA under high CO2” (kurkela2024inorganiccarbonsensing pages 4-4) | 10.1111/ppl.14140 (2024) | Strong for cyanobacterial Ci signaling; environment-dependent. |
| RbcR — activates expression of — RubisCO and main carboxysome shell operon | “RuBisCO and the main carboxysome shell operon are activated by RbcR in low CO2” (kurkela2024inorganiccarbonsensing pages 8-8) | 10.1111/ppl.14140 (2024) | Cyanobacterial low-CO2 acclimation; regulatory. |
| H2S — serves as electron donor for — anoxygenic photosynthesis | “Hydrogen sulfide (H2S) is used as the main electron donor” in anoxygenic photosynthesis (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) | Anoxygenic phototroph-specific; especially GSB/PSB. |
| Green sulfur bacteria (GSB) — oxidize — H2S to elemental sulfur | “GSB oxidize H2S to elemental sulfur” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) | Taxon-specific anoxygenic photoautotrophy. |
| Chlorosomes — function as — light-collecting antennae | “GSB possess special structures—chlorosomes… [that] serve as light-collecting antennas” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) | Anoxygenic phototroph-specific; mostly GSB. |
| Green sulfur bacteria — fix CO2 via — reverse TCA cycle | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) | Strong but taxon-specific; not universal across all anoxygenic phototrophs. |


*Table: This table compiles candidate causal edges for curating the microbial trait photoautotrophic (METPO:1000656), spanning oxygenic cyanobacterial mechanisms and anoxygenic phototrophic mechanisms. Each edge is tied to evidence already gathered in this chat, with DOI/year references and notes on scope or uncertainty.*

### Recent developments & latest research (prioritizing 2023–2024)
#### A) Engineering fast-growing cyanobacteria for enhanced CO2 fixation (2024)
A 2024 review on engineering fast-growing cyanobacteria summarizes biomass productivities and scale-up gaps. It reports:
- **Microalgal BECCS** productivities around **~15 g m−2 d−1** (areal). (kim2024recentadvancesin pages 12-13)
- An **outdoor trial** of engineered *Synechococcus elongatus* UTEX 2973 achieving up to **48 g m−2 d−1** (with limonene production). (kim2024recentadvancesin pages 12-13)
- A range of lab-scale maximum productivities across cyanobacteria of ~0.4–2.6 gDCW L−1 d−1, and multiple pilot/outdoor areal productivities across reactor types (e.g., raceway ponds, flat panels) including examples near ~8–9 gDCW m−2 d−1 for *Synechococcus* strains in specific pilot contexts. (kim2024recentadvancesin pages 6-8)
The review also provides expert perspective that some promising strains may reach higher yields but remain insufficiently tested at larger outdoor scale, highlighting translational needs in cultivation and testing platforms. (kim2024recentadvancesin pages 12-13)

#### B) Novel regulatory understanding: CCM control via metabolites and transcription factors (2024)
The inorganic carbon sensing/signaling minireview consolidates a model in which CCM expression is tuned by intracellular metabolic state via molecules such as **2-PG** and **2-OG**, acting through transcription factors (e.g., **CmpR**, **CcmR/NdhR**, **RbcR**) and post-translational control (e.g., SbtA regulation via SbtB). This supports curating regulatory nodes/edges in addition to metabolic ones. (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 5-5)

#### C) Expanding phototrophy diversity (2023–2024)
A 2024 preprint review of early microbial life emphasizes two reaction-center classes (Type I/II) and suggests that anoxygenic photosynthesis preceded oxygenic photosynthesis, and that coupling two photosystems enabled oxygen production—useful evolutionary context but less directly curation-ready for a mechanism graph. (kacar2406foundationsforreconstructing pages 15-18)

### Current applications and real-world implementations (with recent quantitative data)
#### 1) Pilot-scale wastewater treatment + bioplastic precursor via photoautotrophic cyanobacteria
An outdoor pilot thin-layer raceway pond study (working volume **100 L**) grew a *Synechocystis* strain in **urban wastewater** (as sole nutrient source), reaching biomass densities up to **3.5 g L−1 CDW**. Under nutrient limitation, **PHB reached 23.7 ± 2.2% of CDW**, while the system removed **~72% nitrogen** and **~67% phosphorus** from wastewater. Highly alkaline pH (~10.5; also pH 9–10 cited) was used to control grazers; the system used ambient CO2 outdoors. (grivalsky2024polyβhydroxybutyrateproductionby pages 1-2)

#### 2) Carbon capture to biomass to downstream bioprocess feedstock
A 2024 study cultured marine *Synechococcus* sp. PCC 7002 photoautotrophically in a 3-L reactor (2 L working volume) with biomass productivity **~0.8 g L−1 day−1**. The biomass hydrolysate was used as feedstock for fungal processes, yielding **~50% higher titers** of products (cellulase/citric acid) versus traditional media—an example of coupling photoautotrophic CO2 fixation to biomanufacturing supply chains. (gupta2024marinecyanobacterialbiomass pages 1-2)

#### 3) Microalgal CO2 capture process windows relevant to industrial streams
A 2024 review on *Chlorella* and microalgae CO2 capture provides operating-window constraints useful for real deployments, including: aeration CO2 below ~0.5% limits growth; moderately elevated CO2 (~15%) often maximizes fixation and upregulates RuBisCO (reported **16.3× vs air**); and dissolved oxygen >25 ppm inhibits CO2 fixation while large DO reductions (30-fold) increased fixation 3-fold in *Chlorella* in cited examples. It also contextualizes CO2 capture targets by noting typical CO2 percentages in emissions streams (e.g., ~3–4% power plant flue gas; ~10–13% coal flue gas; up to ~80% in some biorefinery streams). (ashour2024usageofchlorella pages 9-10, ashour2024usageofchlorella pages 1-2)

#### 4) Ecosystem implementation: rapid carbon exchange in microbial mats driven by photoautotrophy
A 2023 13C-bicarbonate tracer study in a vertically structured microbial mat found that carbon mobility (between strata and taxa) is highest during daylight periods of active photoautotrophy; it observed substantial fixed bicarbonate-derived carbon below the photic depth and rapid transfer to heterotrophs (protein labeling within hours). It also quantified stronger night-associated loss for bicarbonate-derived carbon than for tested organics and found less exchange for organic substrate incubations compared to bicarbonate. (moran2023daylightdrivencarbonexchange pages 1-2, moran2023daylightdrivencarbonexchange pages 5-7, moran2023daylightdrivencarbonexchange pages 7-8)

### Expert opinions / analysis (authoritative sources)
- **CCM as central to cyanobacterial photoautotrophy:** 2024 cyanobacteria-focused reviews treat CCM components (transporters, NDH complexes, carboxysomes) as essential for efficient CBB-based CO2 fixation under low inorganic carbon, and highlight regulation by transcription factors and metabolic signals. (kurkela2024inorganiccarbonsensing pages 1-2, lucius2024theprimarycarbon pages 1-2)
- **Environmental constraints on photosystems matter for applied photoautotrophy:** a 2024 review emphasizes that cyanobacterial photosynthesis can be limited by light intensity/wavelength, UV exposure, nutrient limitation, temperature, and salinity—important for bioprocess and field implementation decisions. (grettenberger2024limitingfactorsin pages 1-2)
- **Scale-up gap in carbon-negative biotechnology:** a 2024 review on engineering fast-growing cyanobacteria argues for pairing high-productivity chassis strains with improved models and industrial biotechnology to make photosynthesis-driven carbon removal more scalable and economically favorable; it also presents comparative areal-energy reasoning versus DAC. (kim2024recentadvancesin pages 12-13)

### Relevant statistics and data points (recent studies)
- **Outdoor engineered cyanobacteria areal productivity:** up to **48 g m−2 d−1** in an outdoor trial of engineered UTEX 2973 (with limonene). (kim2024recentadvancesin pages 12-13)
- **Pilot pond bioplastic precursor:** **23.7 ± 2.2% PHB (CDW)** at **3.5 g L−1** biomass in 100 L raceway pond; **~72% N** and **~67% P** removal from wastewater. (grivalsky2024polyβhydroxybutyrateproductionby pages 1-2)
- **Bioreactor productivity (marine cyanobacterium):** **~0.8 g L−1 d−1** biomass productivity in a 3-L externally illuminated reactor. (gupta2024marinecyanobacterialbiomass pages 1-2)
- **AAP (boundary case) abundance & definition:** AAP bacteria are photoheterotrophs using bacteriochlorophyll-a reaction centers; in an Adriatic Sea study, spring maximum average abundance was **2.136 ± 0.081 × 10^4 cells mL−1** (and minimum 0.86 × 10^4 cells mL−1 in summer). Freshwater AAP can constitute up to **22%** of bacterial communities in some observations. (stojan2024ecologyofaerobic pages 1-2, villenaalemany2024phenologyandecological pages 1-2)

## Warnings / claims not ready for TraitMech curation
1. **Do not conflate AAP photoheterotrophy with photoautotrophy.** AAP definitions explicitly describe dependence on organic carbon; they should be excluded from “photoautotrophic” unless a separate CO2-fixation mechanism is demonstrated. (stojan2024ecologyofaerobic pages 1-2, villenaalemany2024phenologyandecological pages 1-2, piwosz2024responseofaerobic pages 1-2)
2. **Taxon specificity:** chlorosomes and rTCA-based photoautotrophy are well-supported for green sulfur bacteria, but should not be generalized to all anoxygenic phototrophs without additional sources. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
3. **Preprint-only evolutionary claims:** reaction-center evolution framing is informative but lower priority for a mechanistic causal graph intended to represent trait capacity and its proximate determinants. (kacar2406foundationsforreconstructing pages 15-18)
4. **Non-peer-reviewed/unclear provenance sources:** one retrieved 2024 thesis-like document was used only where it aligned with better-supported content; it should not be primary evidence in the curated YAML without verification from peer-reviewed literature. (fixacao2024universidadefederaldo pages 49-52, fixacao2024universidadefederaldo pages 52-54, fixacao2024universidadefederaldo pages 54-58)

## DOI-first bibliography (with dates and URLs where available)
- Grettenberger CL, Abou-Shanab R, Hamilton TL. **Limiting factors in the operation of photosystems I and II in cyanobacteria.** *Microbial Biotechnology* (Aug 2024). DOI: **10.1111/1751-7915.14519**. https://doi.org/10.1111/1751-7915.14519 (grettenberger2024limitingfactorsin pages 1-2)
- Lucius S, Hagemann M. **The primary carbon metabolism in cyanobacteria and its regulation.** *Frontiers in Plant Science* (Jul 2024). DOI: **10.3389/fpls.2024.1417680**. https://doi.org/10.3389/fpls.2024.1417680 (lucius2024theprimarycarbon pages 1-2)
- Kurkela J, Tyystjärvi T. **Inorganic carbon sensing and signalling in cyanobacteria.** *Physiologia Plantarum* (Jan 2024). DOI: **10.1111/ppl.14140**. https://doi.org/10.1111/ppl.14140 (kurkela2024inorganiccarbonsensing pages 4-4, kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 5-5, kurkela2024inorganiccarbonsensing media f4366bfa)
- Kushkevych I, Procházka V, Vítězová M, et al. **Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.** *Frontiers in Microbiology* (Jul 2024). DOI: **10.3389/fmicb.2024.1417714**. https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Kim DS, Moreno-Cabezuelo JÁ, Schulz EN, Lea-Smith DJ, Sagaram US. **Recent advances in engineering fast-growing cyanobacterial species for enhanced CO2 fixation.** *Frontiers in Climate* (Jun 2024). DOI: **10.3389/fclim.2024.1412232**. https://doi.org/10.3389/fclim.2024.1412232 (kim2024recentadvancesin pages 12-13, kim2024recentadvancesin pages 6-8)
- Grivalský T, Lakatos GE, Štěrbová K, et al. **Poly-β-hydroxybutyrate production by Synechocystis MT_a24 in a raceway pond using urban wastewater.** *Applied Microbiology and Biotechnology* (Jan 2024). DOI: **10.1007/s00253-023-12924-3**. https://doi.org/10.1007/s00253-023-12924-3 (grivalsky2024polyβhydroxybutyrateproductionby pages 1-2)
- Gupta JK, Jain KK, Kaushal M, et al. **Marine cyanobacterial biomass is an efficient feedstock for fungal bioprocesses.** *Biotechnology for Biofuels and Bioproducts* (Feb 2024). DOI: **10.1186/s13068-024-02469-6**. https://doi.org/10.1186/s13068-024-02469-6 (gupta2024marinecyanobacterialbiomass pages 1-2)
- Ashour M, Mansour AT, Alkhamis YA, Elshobary M. **Usage of Chlorella and diverse microalgae for CO2 capture - towards a bioenergy revolution.** *Frontiers in Bioengineering and Biotechnology* (Aug 2024). DOI: **10.3389/fbioe.2024.1387519**. https://doi.org/10.3389/fbioe.2024.1387519 (ashour2024usageofchlorella pages 9-10, ashour2024usageofchlorella pages 1-2)
- Moran JJ, Bernstein HC, Mobberley JM, et al. **Daylight-driven carbon exchange through a vertically structured microbial community.** *Frontiers in Microbiology* (May 2023). DOI: **10.3389/fmicb.2023.1139213**. https://doi.org/10.3389/fmicb.2023.1139213 (moran2023daylightdrivencarbonexchange pages 1-2, moran2023daylightdrivencarbonexchange pages 5-7, moran2023daylightdrivencarbonexchange pages 7-8)
- Villena-Alemany C, Mujakić I, Fecskeová LK, et al. **Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters.** *Microbiome* (Mar 2024). DOI: **10.1186/s40168-024-01786-0**. https://doi.org/10.1186/s40168-024-01786-0 (villenaalemany2024phenologyandecological pages 1-2)
- Stojan I, Šantić D, Villena-Alemany C, et al. **Ecology of aerobic anoxygenic phototrophs… Adriatic Sea…** *Environmental Microbiome* (Apr 2024). DOI: **10.1186/s40793-024-00573-6**. https://doi.org/10.1186/s40793-024-00573-6 (stojan2024ecologyofaerobic pages 1-2)
- Piwosz K, Villena-Alemany C, Całkiewicz J, et al. **Response of aerobic anoxygenic phototrophic bacteria to limitation and availability of organic carbon.** *FEMS Microbiology Ecology* (Jun 2024). DOI: **10.1093/femsec/fiae090**. https://doi.org/10.1093/femsec/fiae090 (piwosz2024responseofaerobic pages 1-2)

### Plan status
All objectives completed; this report is ready to support curation into `data/traits/physiology/photoautotrophic.yaml`.

References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

2. (grettenberger2024limitingfactorsin pages 1-2): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

3. (lucius2024theprimarycarbon pages 1-2): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 88 citations.

4. (stojan2024ecologyofaerobic pages 1-2): Iva Stojan, Danijela Šantić, Cristian Villena-Alemany, Željka Trumbić, Frano Matić, Ana Vrdoljak Tomaš, Ivana Lepen Pleić, Kasia Piwosz, Grozdan Kušpilić, Živana Ninčević Gladan, Stefanija Šestanović, and Mladen Šolić. Ecology of aerobic anoxygenic phototrophs on a fine-scale taxonomic resolution in adriatic sea unravelled by unsupervised neural network. Environmental Microbiome, Apr 2024. URL: https://doi.org/10.1186/s40793-024-00573-6, doi:10.1186/s40793-024-00573-6. This article has 6 citations and is from a peer-reviewed journal.

5. (villenaalemany2024phenologyandecological pages 1-2): Cristian Villena-Alemany, Izabela Mujakić, Livia K. Fecskeová, Jason Woodhouse, Adrià Auladell, Jason Dean, Martina Hanusová, Magdalena Socha, Carlota R. Gazulla, Hans-Joachim Ruscheweyh, Shinichi Sunagawa, Vinicius Silva Kavagutti, Adrian-Ştefan Andrei, Hans-Peter Grossart, Rohit Ghai, Michal Koblížek, and Kasia Piwosz. Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters. Microbiome, Mar 2024. URL: https://doi.org/10.1186/s40168-024-01786-0, doi:10.1186/s40168-024-01786-0. This article has 18 citations and is from a highest quality peer-reviewed journal.

6. (piwosz2024responseofaerobic pages 1-2): Kasia Piwosz, Cristian Villena-Alemany, Joanna Całkiewicz, Izabela Mujakić, Vít Náhlík, Jason Dean, and Michal Koblížek. Response of aerobic anoxygenic phototrophic bacteria to limitation and availability of organic carbon. FEMS Microbiology Ecology, Jun 2024. URL: https://doi.org/10.1093/femsec/fiae090, doi:10.1093/femsec/fiae090. This article has 6 citations and is from a peer-reviewed journal.

7. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

8. (kurkela2024inorganiccarbonsensing pages 2-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

9. (kurkela2024inorganiccarbonsensing pages 4-4): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

10. (kurkela2024inorganiccarbonsensing pages 3-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

11. (kurkela2024inorganiccarbonsensing media f4366bfa): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

12. (kurkela2024inorganiccarbonsensing media b6613ad5): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

13. (kurkela2024inorganiccarbonsensing pages 5-5): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

14. (fixacao2024universidadefederaldo pages 52-54): DEC DE FIXAÇÃO, NAB TERMOFÍLICA, and SS CORREA. Universidade federal do rio de janeiro centro de ciências da saúde programa de pós-graduação em biotecnologia vegetal e …. Unknown journal, 2024.

15. (fixacao2024universidadefederaldo pages 54-58): DEC DE FIXAÇÃO, NAB TERMOFÍLICA, and SS CORREA. Universidade federal do rio de janeiro centro de ciências da saúde programa de pós-graduação em biotecnologia vegetal e …. Unknown journal, 2024.

16. (kurkela2024inorganiccarbonsensing pages 8-8): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

17. (kurkela2024inorganiccarbonsensing pages 9-10): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

18. (moran2023daylightdrivencarbonexchange pages 1-2): James J. Moran, Hans C. Bernstein, Jennifer M. Mobberley, Allison M. Thompson, Young-Mo Kim, Karl L. Dana, Alexandra B. Cory, Steph Courtney, Ryan S. Renslow, James K. Fredrickson, Helen W. Kreuzer, and Mary S. Lipton. Daylight-driven carbon exchange through a vertically structured microbial community. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1139213, doi:10.3389/fmicb.2023.1139213. This article has 1 citations and is from a peer-reviewed journal.

19. (grivalsky2024polyβhydroxybutyrateproductionby pages 1-2): Tomáš Grivalský, Gergely Ernő Lakatos, Karolína Štěrbová, João Artur Câmara Manoel, Romana Beloša, Petra Divoká, Julian Kopp, Ricarda Kriechbaum, Oliver Spadiut, Alexander Zwirzitz, Kevin Trenzinger, and Jiří Masojídek. Poly-β-hydroxybutyrate production by synechocystis mt_a24 in a raceway pond using urban wastewater. Applied Microbiology and Biotechnology, 108:1-12, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12924-3, doi:10.1007/s00253-023-12924-3. This article has 28 citations and is from a domain leading peer-reviewed journal.

20. (moran2023daylightdrivencarbonexchange pages 9-10): James J. Moran, Hans C. Bernstein, Jennifer M. Mobberley, Allison M. Thompson, Young-Mo Kim, Karl L. Dana, Alexandra B. Cory, Steph Courtney, Ryan S. Renslow, James K. Fredrickson, Helen W. Kreuzer, and Mary S. Lipton. Daylight-driven carbon exchange through a vertically structured microbial community. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1139213, doi:10.3389/fmicb.2023.1139213. This article has 1 citations and is from a peer-reviewed journal.

21. (moran2023daylightdrivencarbonexchange pages 5-7): James J. Moran, Hans C. Bernstein, Jennifer M. Mobberley, Allison M. Thompson, Young-Mo Kim, Karl L. Dana, Alexandra B. Cory, Steph Courtney, Ryan S. Renslow, James K. Fredrickson, Helen W. Kreuzer, and Mary S. Lipton. Daylight-driven carbon exchange through a vertically structured microbial community. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1139213, doi:10.3389/fmicb.2023.1139213. This article has 1 citations and is from a peer-reviewed journal.

22. (moran2023daylightdrivencarbonexchange pages 7-8): James J. Moran, Hans C. Bernstein, Jennifer M. Mobberley, Allison M. Thompson, Young-Mo Kim, Karl L. Dana, Alexandra B. Cory, Steph Courtney, Ryan S. Renslow, James K. Fredrickson, Helen W. Kreuzer, and Mary S. Lipton. Daylight-driven carbon exchange through a vertically structured microbial community. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1139213, doi:10.3389/fmicb.2023.1139213. This article has 1 citations and is from a peer-reviewed journal.

23. (kim2024recentadvancesin pages 12-13): David S. Kim, José Ángel Moreno-Cabezuelo, Eduardo Nicolas Schulz, David J. Lea-Smith, and Uma Shankar Sagaram. Recent advances in engineering fast-growing cyanobacterial species for enhanced co2 fixation. Frontiers in Climate, Jun 2024. URL: https://doi.org/10.3389/fclim.2024.1412232, doi:10.3389/fclim.2024.1412232. This article has 22 citations and is from a peer-reviewed journal.

24. (kim2024recentadvancesin pages 6-8): David S. Kim, José Ángel Moreno-Cabezuelo, Eduardo Nicolas Schulz, David J. Lea-Smith, and Uma Shankar Sagaram. Recent advances in engineering fast-growing cyanobacterial species for enhanced co2 fixation. Frontiers in Climate, Jun 2024. URL: https://doi.org/10.3389/fclim.2024.1412232, doi:10.3389/fclim.2024.1412232. This article has 22 citations and is from a peer-reviewed journal.

25. (kacar2406foundationsforreconstructing pages 15-18): Betul Kacar. Foundations for reconstructing early microbial life. Preprint, Jan 2406. URL: https://doi.org/10.48550/arxiv.2406.09354, doi:10.48550/arxiv.2406.09354. This article has 3 citations.

26. (gupta2024marinecyanobacterialbiomass pages 1-2): Jai Kumar Gupta, Kavish K. Jain, Mehak Kaushal, Daniel J. Upton, Manish Joshi, Piyush Pachauri, A. Jamie Wood, Syed Shams Yazdani, and Shireesh Srivastava. Marine cyanobacterial biomass is an efficient feedstock for fungal bioprocesses. Biotechnology for Biofuels and Bioproducts, Feb 2024. URL: https://doi.org/10.1186/s13068-024-02469-6, doi:10.1186/s13068-024-02469-6. This article has 4 citations and is from a domain leading peer-reviewed journal.

27. (ashour2024usageofchlorella pages 9-10): Mohamed Ashour, Abdallah Tageldein Mansour, Yousef A. Alkhamis, and Mostafa Elshobary. Usage of chlorella and diverse microalgae for co2 capture - towards a bioenergy revolution. Frontiers in Bioengineering and Biotechnology, Aug 2024. URL: https://doi.org/10.3389/fbioe.2024.1387519, doi:10.3389/fbioe.2024.1387519. This article has 87 citations.

28. (ashour2024usageofchlorella pages 1-2): Mohamed Ashour, Abdallah Tageldein Mansour, Yousef A. Alkhamis, and Mostafa Elshobary. Usage of chlorella and diverse microalgae for co2 capture - towards a bioenergy revolution. Frontiers in Bioengineering and Biotechnology, Aug 2024. URL: https://doi.org/10.3389/fbioe.2024.1387519, doi:10.3389/fbioe.2024.1387519. This article has 87 citations.

29. (fixacao2024universidadefederaldo pages 49-52): DEC DE FIXAÇÃO, NAB TERMOFÍLICA, and SS CORREA. Universidade federal do rio de janeiro centro de ciências da saúde programa de pós-graduação em biotecnologia vegetal e …. Unknown journal, 2024.