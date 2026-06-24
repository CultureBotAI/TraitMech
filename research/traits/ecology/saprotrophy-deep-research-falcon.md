---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:47:17.782933'
end_time: '2026-06-17T21:03:36.489928'
duration_seconds: 978.71
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: saprotrophy
  trait_identifier: traitmech:000055
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: saprotrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic-ecology lifestyle in which an organism feeds on dead or decaying
    organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
  parent_traits: METPO:1000059
  synonyms: decomposer, saprophytic
  evidence_summary: 'DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial
    control over carbon cycling in soil", support microbial decomposition of organic
    matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer
    supports decomposer/saprotrophic activity as a key function of soil microbial
    communities.)'
  causal_graph_summary: 'saprotrophy_decomposition_cycling: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** saprotrophy
- **METPO identifier:** traitmech:000055
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which an organism feeds on dead or decaying organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
- **Parent traits:** METPO:1000059
- **Synonyms:** decomposer, saprophytic
- **Existing evidence:** DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial control over carbon cycling in soil", support microbial decomposition of organic matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports decomposer/saprotrophic activity as a key function of soil microbial communities.)
- **Existing causal graph summary:** saprotrophy_decomposition_cycling: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **saprotrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/saprotrophy.yaml`.

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
- **Trait label:** saprotrophy
- **METPO identifier:** traitmech:000055
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which an organism feeds on dead or decaying organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
- **Parent traits:** METPO:1000059
- **Synonyms:** decomposer, saprophytic
- **Existing evidence:** DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial control over carbon cycling in soil", support microbial decomposition of organic matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports decomposer/saprotrophic activity as a key function of soil microbial communities.)
- **Existing causal graph summary:** saprotrophy_decomposition_cycling: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **saprotrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/saprotrophy.yaml`.

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


## Microbial Trait Causal Graph Report: Saprotrophy (METPO traitmech:000055)

### 1) Scope summary (trait definition, phenotype boundaries)
Saprotrophy (syn. decomposer, saprophytic) is a trophic-ecology lifestyle in which microbes obtain carbon and energy from dead or decaying organic matter by secreting extracellular enzymes (hydrolases and oxidoreductases) that depolymerize insoluble substrates into soluble compounds available for uptake, thereby mineralizing organic matter and driving carbon and nutrient cycling. (wang2024mechanismsandimplications pages 4-5, wang2024mechanismsandimplications pages 5-7)

**What the trait represents (operationally):**
- A physiological capacity for extracellular depolymerization/oxidation of complex organic matter (e.g., cellulose/hemicellulose/lignin; microbial necromass), coupled to uptake and catabolism of released monomers/oligomers. (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8)
- At community/ecosystem scale, saprotrophic activity underpins decomposition, soil heterotrophic respiration, and biogeochemical fluxes. (wang2024mechanismsandimplications pages 2-3, wang2024mechanismsandimplications pages 1-2)

**Boundary cases / distinguishing from nearby traits:**
- **Saprotrophy vs. pathotrophy (pathogenic/parasitic trophic modes):** Wood-decay fungal lineages can show trophic plasticity; some taxa may attack living tissues (pathotrophy) while retaining the enzymatic/genomic repertoire typical of wood saprotrophs. Stable isotope data (δ13C/δ15N/14C) combined with CAZy (carbohydrate-active enzyme) content are used to infer such mixed strategies and challenge strict categorical assignments. (tome2024comparativegenomicsand pages 9-10, tome2024comparativegenomicsand pages 10-13)
- **Saprotrophy vs. symbiotrophy (e.g., ectomycorrhizal fungi):** Ectomycorrhizal fungi are described as “potential organic matter decomposers, yet not saprotrophs,” highlighting that some symbiotrophs retain partial decay capabilities while being obligately host-associated for carbon. (pena2024mycorrhizalsymbiosisand pages 13-13)
- **Saprotrophy vs. copiotrophy/oligotrophy (life-history strategies):** These are not trophic modes per se, but strategies influencing decomposition roles. For example, bacteria vs fungi partition substrates: bacteria outperform fungi on simple substrates, while fungi are more effective on complex substrates (quantified below), shaping saprotrophic niches. (wang2024mechanismsandimplications pages 1-2)

### 2) Key mechanistic concepts (current understanding)
#### 2.1 Extracellular enzyme suites for lignocellulose decomposition
Saprotrophic decomposition of plant biomass relies on coordinated **CAZymes** (carbohydrate-active enzymes) for polysaccharides and **oxidative enzymes** for lignin and aromatic structures.
- **Cellulose → glucose:** complete cellulose degradation requires concerted action of **cellobiohydrolases, endoglucanases, and β-glucosidases**. (gurovic2023regulationoflignocellulose pages 2-3)
- **Lignin oxidation:** lignin is a hydrophobic phenolic polymer requiring oxidative attack; **manganese peroxidase (MnP)** and **lignin peroxidase (LiP)** catalyze **H2O2-dependent** oxidative reactions, and **laccases** oxidize phenolics/aromatic amines and can act on lignin and monomers. (gurovic2023regulationoflignocellulose pages 2-3)
- **Oxalate–Mn chemistry (example mechanism in fungal delignification):** MnP oxidizes Mn2+; Mn3+ can be chelated by oxalate as a diffusible mediator; oxalate contributes to acidification and potentially opening the lignocellulose matrix. (duran2023thesecretomeof pages 7-8)

#### 2.2 Regulation: carbon catabolite repression (CCR) and induction
Saprotrophic enzyme expression is strongly regulated by carbon availability.
- **Fungal CCR:** simple sugars (e.g., glucose) repress cellulolytic enzymes; regulators include **CreA/Cre1**, and inducers include **cellobiose, sophorose, lactose, and oligosaccharides**; **sophorose** is described as a particularly powerful inducer in *Trichoderma reesei*. (gurovic2023regulationoflignocellulose pages 5-7)
- **Bacterial CCR:** Gram-negative CCR involves the PTS/EIIA state and **cAMP–CRP** signaling that activates catabolic gene expression at low glucose; Gram-positive CCR involves **HPr(Ser-P)** binding **CcpA**, repressing transcription of lignocellulose catabolic genes. (gurovic2023regulationoflignocellulose pages 5-7)

### 3) Recent developments (prioritizing 2023–2024)
#### 3.1 High-resolution mapping of lignin vs cellulose utilizers under climate manipulation (2023)
A decade-long irrigation (drought mitigation) experiment coupled to 13C stable-isotope probing identified many taxa actively incorporating lignin- vs cellulose-derived carbon:
- **446 ASVs enriched on 13C-lignin** and **216 ASVs enriched on 13C-cellulose**. (hartmann2023longtermmitigationof pages 9-12)
- Lignin-C uptake dominated by fungal orders **Helotiales, Mortierellales, Hypocreales**; cellulose-C uptake mainly by bacterial families **Sphingomonadaceae, Devosiaceae, Xanthomonadaceae** and fungal orders **Sebacinales, Helociales**. (hartmann2023longtermmitigationof pages 9-12)
These results operationalize saprotrophy as **substrate-specific assimilation** and show that water availability reshapes decomposer membership and functional potential. (hartmann2023longtermmitigationof pages 9-12)

#### 3.2 Quantitative coupling of fungal guild shifts to soil carbon outcomes (2024)
A multi-year trenching experiment in temperate pine stands found that altering fungal guild composition (ectomycorrhizal vs saprotrophic fungi) can measurably change soil carbon stocks:
- After two years, trenching altered guild abundances and **decreased soil C stocks by 10%**, primarily through changes in particulate organic matter (POM) concentrated in the top 5 cm; trenching also stimulated root and fungal litter (necromass) decomposition. (delancey2024shiftingfungalguild pages 1-2)
- The study reports **suppression of decomposition with increased EMF/saprotroph ratio** across root and fungal necromass. (delancey2024shiftingfungalguild pages 9-10)
This provides curation-relevant evidence connecting “saprotrophic guild abundance” → “decomposition rate” → “soil carbon stocks,” with quantified effect size. (delancey2024shiftingfungalguild pages 1-2)

#### 3.3 Updated conceptual framing of bacterial–fungal substrate niches (2024)
A highly cited 2024 ISME Journal review quantifies differential decomposition niches:
- Bacteria are **1.4–5× more efficient** in uptake of **simple organic compounds**, whereas fungi are **1.1–4.1× more effective** in utilizing **complex compounds**. (wang2024mechanismsandimplications pages 1-2)
- Soil microbial **carbon use efficiency (CUE) is commonly < 0.4**, implying >60% of assimilated carbon is respired rather than converted to biomass. (wang2024mechanismsandimplications pages 1-2)
These quantitative statements are directly useful for edges linking substrate chemistry to saprotrophic partitioning and carbon cycling efficiency. (wang2024mechanismsandimplications pages 1-2)

#### 3.4 Saprotrophy–pathotrophy continua resolved with genomics + isotopes (2024)
A 2024 mBio study emphasizes that strict separation into mutualist/pathogen/saprotroph is frequently questioned and that CAZy profiles plus stable isotopes can indicate mixed strategies (“saprotrophic-pathogenic lifestyle”). (tome2024comparativegenomicsand pages 9-10, tome2024comparativegenomicsand pages 10-13)

### 4) Current applications and real-world implementations
1. **Mushroom cultivation and engineered decomposition of lignocellulosic substrates:** Temporal secretome dynamics in *Agaricus bisporus* (commercial mushroom) show coordinated lignin removal (~40% w/w) and cellulose degradation (~20% w/w) during substrate processing stages, under industrially relevant conditions, providing a direct applied system where saprotrophic enzyme deployment is leveraged for biomass conversion. (duran2023thesecretomeof pages 7-8)
2. **Soil/forest management and carbon sequestration modeling:** Manipulations that shift ectomycorrhizal vs saprotrophic guild balance can alter decomposition and short-term soil C stocks (10% change over 2 years in one experiment), motivating explicit representation of saprotrophic traits in ecosystem models. (delancey2024shiftingfungalguild pages 1-2, delancey2024shiftingfungalguild pages 9-10)
3. **Climate-change response assessment:** Long-term irrigation/drought experiments combined with 13C-labeled lignin/cellulose incubations are being used to identify decomposer taxa and functional potentials under altered precipitation regimes. (hartmann2023longtermmitigationof pages 9-12)

### 5) Candidate causal graph nodes (grouped) and ontology grounding suggestions
The following table provides a curation-ready inventory of candidate nodes (enzymes, regulators, substrates, environmental drivers, assays) with suggested CURIEs where possible.

| Node label | Type | Suggested ontology grounding | Notes / evidence source |
|---|---|---|---|
| saprotrophy | process/trait | METPO:traitmech:000055 | Heterotrophic lifestyle feeding on dead/decaying organic matter; boundary with pathotrophy/symbiotrophy can be inferred using CAZy content and stable isotopes (tome2024comparativegenomicsand pages 1-2, tome2024comparativegenomicsand pages 9-10, pena2024mycorrhizalsymbiosisand pages 13-13, tome2024comparativegenomicsand pages 10-13) |
| decomposition of dead organic matter | process | GO:0044243 | Central ecological function of saprotrophs; extracellular hydrolysis/oxidation releases soluble compounds for uptake (wang2024mechanismsandimplications pages 4-5, wang2024mechanismsandimplications pages 5-7, wang2024mechanismsandimplications pages 2-3) |
| extracellular enzyme activity | process | GO:0005576 | Insoluble complex substrates require extracellular exoenzymes for saprotrophic resource capture (wang2024mechanismsandimplications pages 4-5, wang2024mechanismsandimplications pages 5-7) |
| cellulose catabolic process | process | GO:0030245 | Cellulose breakdown is a core saprotrophic mechanism, requiring coordinated hydrolase action (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| lignin catabolic process | process | GO:0046274 | Lignin oxidation is a prerequisite for access to hydrophobic plant cell-wall polymers in many saprotrophs (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| cellobiohydrolase | enzyme | EC:3.2.1.91 | One of the canonical cellulases required for complete cellulose degradation; detected as GH6/GH7 CBM1-linked proteins in saprotrophic secretomes (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| endoglucanase | enzyme | EC:3.2.1.4 | Core cellulase acting with CBHs and beta-glucosidases in cellulose depolymerization (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| beta-glucosidase | enzyme | EC:3.2.1.21 | Releases glucose from cellobiose/cellooligosaccharides; also implicated in sophorose generation via transglycosylation in fungal induction models (gurovic2023regulationoflignocellulose pages 5-7, gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| xylanase | enzyme | EC:3.2.1.8 | Major hemicellulase in saprotrophic polysaccharide breakdown; regulated by carbon source and transcription factors such as XlnR/XYR1 (gurovic2023regulationoflignocellulose pages 5-7, gurovic2023regulationoflignocellulose pages 2-3) |
| beta-mannanase | enzyme | EC:3.2.1.78 | Hemicellulose-active enzyme repeatedly cited among saprotrophic fiber-degrading repertoires (gurovic2023regulationoflignocellulose pages 2-2, wunderlich2023understandingthemicrobial pages 4-6) |
| laccase | enzyme | EC:1.10.3.2 | Multicopper phenol oxidase central to oxidative lignin modification; abundant in wood/compost saprotroph secretomes (shabaev2024saprotrophicwooddecay pages 8-10, gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| manganese peroxidase (MnP) | enzyme | EC:1.11.1.13 | H2O2-dependent ligninolytic peroxidase; oxidizes Mn2+ to a diffusible mediator for lignin attack (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| lignin peroxidase (LiP) | enzyme | EC:1.11.1.14 | Canonical fungal ligninase involved in nonspecific oxidative lignin depolymerization (gurovic2023regulationoflignocellulose pages 2-3, gurovic2023regulationoflignocellulose pages 3-4) |
| lytic polysaccharide monooxygenase (LPMO) | enzyme | EC:1.14.99.54 | Oxidative polysaccharide-cleaving enzyme present in saprotrophic secretomes; important for plant cell-wall saccharification (shabaev2024saprotrophicwooddecay pages 8-10, gurovic2023regulationoflignocellulose pages 2-2) |
| cellulosome | gene complex/enzyme complex | GO:1902494 | Multi-enzyme scaffolded complex enhancing lignocellulose deconstruction, especially in anaerobic saprotrophs (gurovic2023regulationoflignocellulose pages 2-3, wunderlich2023understandingthemicrobial pages 4-6, gurovic2023regulationoflignocellulose pages 3-4) |
| CAZy AA1 family | enzyme family | CAZy:AA1 | Includes laccases and related multicopper oxidases linked to lignin/aromatic oxidation (shabaev2024saprotrophicwooddecay pages 8-10, duran2023thesecretomeof pages 7-8) |
| CAZy GH3 family | enzyme family | CAZy:GH3 | Includes beta-glucosidases detected in saprotrophic cellulose degradation (duran2023thesecretomeof pages 7-8) |
| CAZy GH5 family | enzyme family | CAZy:GH5 | Includes endoglucanases and beta-mannosidase/beta-mannanase-related activities in saprotrophic secretomes (duran2023thesecretomeof pages 7-8, wunderlich2023understandingthemicrobial pages 4-6) |
| CAZy GH6 family | enzyme family | CAZy:GH6 | Includes cellobiohydrolase activity in saprotrophic cellulose degradation (duran2023thesecretomeof pages 7-8) |
| CAZy GH7 family | enzyme family | CAZy:GH7 | Includes abundant cellobiohydrolases in saprotrophic cellulose attack (duran2023thesecretomeof pages 7-8) |
| CAZy GH16 family | enzyme family | CAZy:GH16 | Includes xyloglucanase activity documented in saprotrophic secretomes (shabaev2024saprotrophicwooddecay pages 8-10, duran2023thesecretomeof pages 7-8) |
| CAZy CE4 family | enzyme family | CAZy:CE4 | Carbohydrate esterase family detected in wood-decay saprotroph secretomes (shabaev2024saprotrophicwooddecay pages 8-10) |
| CAZy CE16 family | enzyme family | CAZy:CE16 | Carbohydrate esterase family detected alongside oxidative CAZymes in saprotrophic wood decay (shabaev2024saprotrophicwooddecay pages 8-10) |
| CreA/Cre1 | regulator | label only | Fungal carbon catabolite repression regulator repressing lignocellulolytic genes under preferred/simple carbon sources (gurovic2023regulationoflignocellulose pages 5-7) |
| CRP (cAMP receptor protein) | regulator | label only | Gram-negative bacterial CCR regulator activated by cAMP under low glucose to induce catabolic genes (gurovic2023regulationoflignocellulose pages 5-7) |
| cAMP | chemical/regulator | CHEBI:17489 | Second messenger that binds CRP during bacterial relief of carbon catabolite repression (gurovic2023regulationoflignocellulose pages 5-7) |
| CcpA | regulator | label only | Gram-positive bacterial CCR regulator that represses lignocellulose catabolic transcription with HPr(Ser-P) (gurovic2023regulationoflignocellulose pages 5-7) |
| HPr | regulator/PTS component | label only | Phosphocarrier protein in Gram-positive CCR; HPr(Ser-P) partners with CcpA (gurovic2023regulationoflignocellulose pages 5-7) |
| PTS EIIA | regulator/transport component | label only | Glucose-responsive phosphotransferase component controlling CRP-cAMP signaling in Gram-negative CCR (gurovic2023regulationoflignocellulose pages 5-7) |
| CLR-1 / ClrA | regulator | label only | Major ascomycete transcriptional regulator of cellulose/hemicellulose degrading enzymes (gurovic2023regulationoflignocellulose pages 5-7) |
| CLR-2 / ClrB | regulator | label only | Major ascomycete transcriptional regulator of cellulolytic gene expression (gurovic2023regulationoflignocellulose pages 5-7, gurovic2023regulationoflignocellulose pages 2-2) |
| XlnR / XYR1 / XLN1 | regulator | label only | Major ascomycete regulator controlling xylanases, cellulases, or both depending on species (gurovic2023regulationoflignocellulose pages 5-7) |
| cellulose | chemical/substrate | CHEBI:62966 | Principal plant cell-wall polysaccharide decomposed by saprotrophic cellulases (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| hemicellulose | chemical/substrate | CHEBI:25988 | Heteropolymeric plant cell-wall substrate attacked by xylanases, beta-mannanases and related CAZymes (gurovic2023regulationoflignocellulose pages 2-3, wunderlich2023understandingthemicrobial pages 4-6) |
| lignin | chemical/substrate | CHEBI:6457 | Hydrophobic phenolic polymer requiring oxidative attack by laccases/peroxidases before or during polysaccharide access (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| glucose | chemical | CHEBI:17234 | Preferred simple carbon source and common trigger of carbon catabolite repression (gurovic2023regulationoflignocellulose pages 5-7) |
| cellobiose | chemical | CHEBI:28053 | Cellulose breakdown product and transcriptional inducer in many cellulolytic systems (gurovic2023regulationoflignocellulose pages 5-7, duran2023thesecretomeof pages 7-8) |
| sophorose | chemical | CHEBI:50511 | Strong fungal inducer of cellulase expression, especially in T. reesei models (gurovic2023regulationoflignocellulose pages 5-7) |
| oxalate | chemical | CHEBI:16995 | Chelates Mn3+, contributes to acidification, and participates in lignin-oxidation chemistry (duran2023thesecretomeof pages 7-8) |
| Mn2+ | chemical | CHEBI:29035 | Substrate for MnP; oxidation to Mn3+ creates a diffusible lignin-oxidation mediator (duran2023thesecretomeof pages 7-8) |
| hydrogen peroxide | chemical | CHEBI:16240 | Required co-substrate for MnP/LiP oxidative ligninolysis (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) |
| substrate complexity | environmental factor | label only | Complex substrates favor fungal competitiveness, while simple substrates favor bacteria (wang2024mechanismsandimplications pages 1-2) |
| drought | environmental factor | ENVO:01000267 | Long-term drought selects oligotrophic/drought-tolerant decomposer functions and stress-protection genes (hartmann2023longtermmitigationof pages 9-12) |
| irrigation | experimental/environmental factor | ENVO:00000027 | Long-term irrigation shifts decomposition gene diversity and lignin/cellulose-utilizer composition (hartmann2023longtermmitigationof pages 9-12) |
| elevation | environmental factor | ENVO:00000446 | Elevation correlates with shifts in CAZyme pools and decomposition potentials across soils (chen2023metagenomichighlightcontrasting pages 9-10) |
| stable isotope trophic profiling (δ13C/δ15N/14C) | assay | label only | Used to distinguish saprotrophic from mycorrhizal/pathotrophic signatures and identify mixed trophic modes (tome2024comparativegenomicsand pages 9-10, tome2024comparativegenomicsand pages 10-13) |
| CAZy repertoire profiling | assay | label only | Comparative genomic/secretomic evidence for wood-saprotrophic capacity and trophic inference (tome2024comparativegenomicsand pages 1-2, tome2024comparativegenomicsand pages 10-13, shabaev2024saprotrophicwooddecay pages 8-10) |
| 13C-lignin stable-isotope probing | assay | label only | Identifies lignin-C assimilating taxa in soil decomposition experiments (hartmann2023longtermmitigationof pages 9-12) |
| 13C-cellulose stable-isotope probing | assay | label only | Identifies cellulose-C assimilating taxa in decomposition experiments (hartmann2023longtermmitigationof pages 9-12) |


*Table: This table lists candidate nodes for a saprotrophy TraitMech causal graph, spanning mechanisms, molecules, regulators, environmental drivers, and assays. It is useful for selecting ontology-grounded entities to curate into a causal graph with evidence-linked scope and boundary conditions.*

**Visual evidence:** Shabaev et al. (2024) provide figures showing CAZyme family composition and secretome class proportions (GH vs AA vs CE) across control vs sawdust conditions in a wood-decay saprotroph, supporting node inclusion for AA1 laccases, LPMOs, AA3/AA7 oxidoreductases, GH/CE families and the concept that substrate shifts the deployed enzyme suite. (shabaev2024saprotrophicwooddecay media f0c43fde, shabaev2024saprotrophicwooddecay media 54fb5969)

### 6) Evidence-backed candidate causal edges (triples)
The following table lists proposed subject–predicate–object edges, with evidence snippets, DOI-first references, and curation notes.

| Edge (subject—predicate—object) | Node type(s) | Suggested grounding | Evidence snippet | Reference | Strength/notes |
|---|---|---|---|---|---|
| Cellobiohydrolase + endoglucanase + β-glucosidase — enables depolymerization of — cellulose to glucose | enzyme/process/chemical | EC:3.2.1.91; EC:3.2.1.4; EC:3.2.1.21; CHEBI:62966 cellulose; CHEBI:17234 glucose | “The complete degradation of cellulose into glucose involves a concerted action of several enzymes including cellobiohydrolases, endoglucanases, and β-glucosidases.” (gurovic2023regulationoflignocellulose pages 2-3) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong, broad mechanism across lignocellulose-degrading microbes |
| Extracellular CAZymes — hydrolyze — hemicellulose polysaccharides | enzyme/process/chemical | CAZy:GH; CHEBI:25988 hemicellulose | CAZymes “act on glycosidic bonds” and cellulose/hemicellulose are their substrates; hemicellulose is targeted by xylanases, β-mannanases, pectate lyases and related enzymes (gurovic2023regulationoflignocellulose pages 2-3, wunderlich2023understandingthemicrobial pages 4-6) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002; DOI:10.1186/s42523-022-00224-6 (2023) https://doi.org/10.1186/s42523-022-00224-6 | Strong, but generic family-level edge |
| GH16 xyloglucanase — degrades — xyloglucan | enzyme/chemical | CAZy:GH16; CHEBI:140417 xyloglucan | “xyloglucanases - GH16” were identified in secretomes during saprotrophic substrate degradation (duran2023thesecretomeof pages 7-8) | DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Strong for Agaricus bisporus; taxon-specific exemplar |
| GH7-CBM1/GH6-CBM1 cellobiohydrolases — release — cellobiose from cellulose | enzyme/chemical/process | CAZy:GH7; CAZy:GH6; CHEBI:28053 cellobiose | “The release of cellobiose was highest… corroborating with cellobiohydrolase activity”; CBHs GH7-CBM1 and GH6-CBM1 were detected (duran2023thesecretomeof pages 7-8) | DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Strong but taxon- and assay-specific |
| LPMO — oxidatively cleaves — polysaccharides in plant cell walls | enzyme/process | EC:1.14.99.54; CAZy:AA9/label LPMO; GO:0000272 polysaccharide catabolic process | Secretomes of saprotrophs include “lytic polysaccharide monooxygenases (LPMO X325)” among key plant cell-wall degrading enzymes (shabaev2024saprotrophicwooddecay pages 8-10) | DOI:10.3390/jof11010021 (2024) https://doi.org/10.3390/jof11010021 | Strong for oxidative saccharification; family grounding partly label-based |
| Laccase — oxidizes/depolymerizes — lignin and phenolic substrates | enzyme/chemical/process | EC:1.10.3.2; CAZy:AA1; CHEBI:6457 lignin | “Laccases and peroxidases degrade not only lignin but also the corresponding monomers”; laccases “modify lignin via hydrogen atom abstraction or via electron transfer” (gurovic2023regulationoflignocellulose pages 2-3, duran2023thesecretomeof pages 7-8) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002; DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Strong, widely supported |
| Manganese peroxidase (MnP) — catalyzes H2O2-dependent oxidation of — lignin | enzyme/chemical/process | EC:1.11.1.13; CHEBI:16240 hydrogen peroxide; CHEBI:6457 lignin | “Fungal ligninolytic enzymes are mainly manganese peroxidases (MnP), lignin peroxidases (LiP) catalyzing a variety of oxidative reactions that are dependent on H2O2” (gurovic2023regulationoflignocellulose pages 2-3) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong, broad fungal mechanism |
| Lignin peroxidase (LiP) — catalyzes H2O2-dependent oxidation of — lignin | enzyme/chemical/process | EC:1.11.1.14; CHEBI:16240; CHEBI:6457 | “Ligninases catalyze oxidative, nonspecific reactions”; LiP is listed among H2O2-dependent fungal ligninolytic enzymes (gurovic2023regulationoflignocellulose pages 2-3) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong, but mostly fungal |
| MnP — oxidizes — Mn2+ to diffusible Mn3+ mediator | enzyme/chemical/process | EC:1.11.1.13; CHEBI:29035 Mn2+; label Mn3+ | “MnPs having a high redox potential, first oxidize Mn2+, which then can be chelated by oxalate and acts as a diffusible charge transfer mediator” (duran2023thesecretomeof pages 7-8) | DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Strong but described from A. bisporus-focused discussion |
| Oxalate — chelates — Mn3+ and facilitates lignin oxidation | chemical/process | CHEBI:16995 oxalate; label Mn3+ | Oxalate “can be chelated by oxalate and acts as a diffusible charge transfer mediator” and contributes to acidification/opening the matrix (duran2023thesecretomeof pages 7-8) | DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Strong mechanistic support; mediator role should be curated carefully |
| Oxalate oxidase/decarboxylase activity — produces or recycles — H2O2/oxalate during delignification | enzyme/chemical/process | EC:1.2.3.4 oxalate oxidase; EC:4.1.1.2 oxalate decarboxylase; CHEBI:16240; CHEBI:16995 | OXO “converts oxalate to CO2 and will generate hydrogen peroxide”; ODC/OXO linked to oxalate turnover during lignocellulose attack (duran2023thesecretomeof pages 7-8) | DOI:10.1016/j.isci.2023.107087 (2023) https://doi.org/10.1016/j.isci.2023.107087 | Moderate; enzyme identity/function ambiguity noted in source |
| Simple sugars/glucose — activates carbon catabolite repression and represses — lignocellulolytic genes | chemical/process/regulator | CHEBI:17234 glucose; GO:0000019 regulation of catabolite gene expression | “Glucose is a repressor of fungal cellulolytic enzymes” and preferred simple carbon sources cause CreA/Cre1-mediated repression/localization (gurovic2023regulationoflignocellulose pages 5-7) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong across many taxa, though molecular details differ |
| Cellobiose/sophorose/oligosaccharides — induce transcription of — cellulolytic CAZyme genes | chemical/process/regulator | CHEBI:28053 cellobiose; CHEBI:50511 sophorose; label CAZyme genes | “Cellobiose, sophorose, lactose, and oligosaccharides may act as inducers”; sophorose is “one of the most powerful inducers in T. reesei” (gurovic2023regulationoflignocellulose pages 5-7) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong, but inducer strength is species-specific |
| Phosphorylated EIIA/adenylyl cyclase/cAMP-CRP signaling — activates transcription of — catabolic genes under low glucose | regulator/process | KEGG:CRP? label CRP-cAMP; label EIIA; label adenylyl cyclase | “At low glucose… phosphorylated EIIA activates adenylyl cyclase… cAMP binds CRP… expression of CCR-sensitive operons is induced” (gurovic2023regulationoflignocellulose pages 5-7) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong in Gram-negative bacteria; not specific to saprotrophy alone |
| HPr(Ser-P)-CcpA complex — represses transcription of — lignocellulose catabolic genes | regulator/process | label HPr(Ser-P); UniProt/label CcpA | “Phosphorylated HPr binds CcpA… prevent RNA polymerase from initializing transcription of genes involved in lignocellulose catabolism” (gurovic2023regulationoflignocellulose pages 5-7) | DOI:10.1093/jambio/lxac002 (2023) https://doi.org/10.1093/jambio/lxac002 | Strong in Gram-positive bacteria |
| Complex organic substrates — increase competitiveness of — fungi relative to bacteria | environment/process/taxon group | label complex organic compounds; NCBITaxon:4751 Fungi; NCBITaxon:2 Bacteria | “Bacteria are 1.4–5 times more efficient in the uptake of simple organic compounds… fungi are 1.1–4.1 times more effective in utilizing complex compounds” (wang2024mechanismsandimplications pages 1-2) | DOI:10.1093/ismejo/wrae073 (2024) https://doi.org/10.1093/ismejo/wrae073 | Strong ecological edge; community-level, not gene-specific |
| Long-term drought — selects for — oligotrophic/drought-tolerant decomposition microbiome with stress-protection genes | environment/process/community | ENVO:01000267 drought; label oligotrophic lifestyle | Under dry conditions there was “increased relative abundance of regulatory genes encoding for cofactors, cell wall components, dormancy and sporulation” and drought-tolerant taxa increased (hartmann2023longtermmitigationof pages 9-12) | DOI:10.3389/fmicb.2023.1267270 (2023) https://doi.org/10.3389/fmicb.2023.1267270 | Strong at community-function level |
| Long-term irrigation — shifts decomposition functional potential toward — altered CAZy/gene diversity and changed lignin/cellulose utilizers | environment/process/community | ENVO:00000027 irrigation; label CAZy gene diversity | Irrigation “increased gene diversity and selected for different functional potentials”; 446 ASVs enriched on 13C-lignin and 216 on 13C-cellulose, with treatment-shifted decomposer composition (hartmann2023longtermmitigationof pages 9-12) | DOI:10.3389/fmicb.2023.1267270 (2023) https://doi.org/10.3389/fmicb.2023.1267270 | Strong community-level edge; not direct trait-defining mechanism |
| Stable isotope signatures + CAZy repertoire — support inference of — saprotrophic vs pathotrophic trophic mode | assay/genome/process/trait | label stable isotope analysis; label CAZy profile; METPO:traitmech:000055 saprotrophy | “Stable isotope analysis and CAZy content jointly suggest a pathotrophic lifestyle” and species may “maintain all the metabolic repertoire of a wood saprotroph” (tome2024comparativegenomicsand pages 9-10, tome2024comparativegenomicsand pages 10-13) | DOI:10.1128/mbio.01423-24 (2024) https://doi.org/10.1128/mbio.01423-24 | Useful diagnostic edge; assay/inference, not mechanistic causal biology |
| Wood-decay CAZyme repertoire — supports capacity for — saprotrophic lignocellulose decomposition | pathway/genome/trait | label wood-decay CAZyme repertoire; METPO:traitmech:000055 | Comparative genomics showed some fungi retain “all the metabolic repertoire of a wood saprothroph,” using CAZy content as evidence of saprotrophic capacity (tome2024comparativegenomicsand pages 1-2, tome2024comparativegenomicsand pages 10-13) | DOI:10.1128/mbio.01423-24 (2024) https://doi.org/10.1128/mbio.01423-24 | Moderate; genomic inference of capacity, not direct activity proof |
| Extracellular exoenzymes — convert insoluble complex organic matter into — soluble compounds available for microbial uptake | enzyme/process/chemical | GO:0005576 extracellular region; label soluble organic compounds | “Saprotrophic microbes obtain carbon and energy by hydrolyzing/oxidizing dead organic matter into soluble compounds”; insoluble compounds require extracellular enzymes (wang2024mechanismsandimplications pages 4-5, wang2024mechanismsandimplications pages 5-7) | DOI:10.1093/ismejo/wrae073 (2024) https://doi.org/10.1093/ismejo/wrae073 | Strong, high-level foundational edge for saprotrophy |
| High ectomycorrhizal:saprotroph ratio — suppresses — decomposition of root/fungal litter and promotes higher soil C | community/process/ecosystem | label EMF:saprotroph ratio; label decomposition; label soil carbon stock | “significant suppression of decomposition with an increased EMF/saprotroph ratio”; trenching reduced soil C stocks by 10% and stimulated root/fungal litter decomposition (delancey2024shiftingfungalguild pages 1-2, delancey2024shiftingfungalguild pages 9-10) | DOI:10.1007/s10021-024-00934-9 (2024) https://doi.org/10.1007/s10021-024-00934-9 | Strong ecosystem-level interaction; indirect relevance to saprotrophy trait |


*Table: This table lists evidence-backed candidate causal edges for a TraitMech saprotrophy graph, spanning lignocellulose depolymerization, lignin oxidation, regulatory control, environmental modulation, and assay-based trophic-mode inference. It is useful for selecting which edges are strong mechanistic candidates versus ecological or assay-derived inferences that may need cautious curation.*

### 7) Warnings / claims to treat as uncertain or not yet ready for curation
1. **Assay-derived “inference” edges vs mechanistic edges:** Edges using stable isotopes + CAZy content to infer trophic mode are valuable for *classification/diagnosis*, but they do not necessarily encode a mechanistic causal relationship inside the microbe (they connect “assay readout” → “inferred lifestyle”). Curate as “evidence/assay supports trait assignment,” not as a biochemical mechanism. (tome2024comparativegenomicsand pages 9-10, tome2024comparativegenomicsand pages 10-13)
2. **Taxon- and context-specific secretome edges:** CAZyme family lists and temporal dynamics from *A. bisporus* or *Crucibulum laeve* are strong exemplars but may not generalize across all saprotrophs; mark as taxon-specific unless supported by broader reviews. (shabaev2024saprotrophicwooddecay pages 8-10, duran2023thesecretomeof pages 7-8)
3. **Oxalate oxidase vs decarboxylase ambiguity:** The *A. bisporus* oxalate enzyme is discussed with possible oxidase vs decarboxylase activity; curate with caution and annotate ambiguity. (duran2023thesecretomeof pages 7-8)
4. **Ecosystem-level edges are indirect:** Edges linking EMF:saprotroph ratios to soil carbon stocks reflect community interactions and ecosystem responses; these are valuable but not “within-organism” mechanisms, and may require separate graph layers (community/ecosystem). (delancey2024shiftingfungalguild pages 1-2, delancey2024shiftingfungalguild pages 9-10)

---

## DOI-first bibliography (with URLs and publication dates where available)
- Wang C, Kuzyakov Y. **Mechanisms and implications of bacterial–fungal competition for soil resources.** *The ISME Journal.* Advance access publication 1 May 2024 (Issue: 2024; Vol 18). DOI: **10.1093/ismejo/wrae073**. URL: https://doi.org/10.1093/ismejo/wrae073 (wang2024mechanismsandimplications pages 1-2)
- DeLancey LC, Maillard F, Hobbie SE, Kennedy PG. **Shifting fungal guild abundances are associated with altered temperate forest soil carbon stocks.** *Ecosystems.* Oct 2024. DOI: **10.1007/s10021-024-00934-9**. URL: https://doi.org/10.1007/s10021-024-00934-9 (delancey2024shiftingfungalguild pages 1-2)
- Tomé LMR et al. **Comparative genomics and stable isotope analysis reveal the saprotrophic-pathogenic lifestyle of a neotropical fungus.** *mBio.* Aug 2024. DOI: **10.1128/mbio.01423-24**. URL: https://doi.org/10.1128/mbio.01423-24 (tome2024comparativegenomicsand pages 1-2)
- Pena R, Tibbett M. **Mycorrhizal symbiosis and the nitrogen nutrition of forest trees.** *Applied Microbiology and Biotechnology.* Sep 2024. DOI: **10.1007/s00253-024-13298-w**. URL: https://doi.org/10.1007/s00253-024-13298-w (pena2024mycorrhizalsymbiosisand pages 13-13)
- Shabaev AV et al. **Saprotrophic wood decay ability and plant cell wall degrading enzyme system of the white rot fungus *Crucibulum laeve*: secretome, metabolome and genome investigations.** *Journal of Fungi.* Dec 2024. DOI: **10.3390/jof11010021**. URL: https://doi.org/10.3390/jof11010021 (shabaev2024saprotrophicwooddecay pages 8-10, shabaev2024saprotrophicwooddecay media f0c43fde, shabaev2024saprotrophicwooddecay media 54fb5969)
- Gurovic MSV et al. **Regulation of lignocellulose degradation in microorganisms.** *Journal of Applied Microbiology.* Dec 2023. DOI: **10.1093/jambio/lxac002**. URL: https://doi.org/10.1093/jambio/lxac002 (gurovic2023regulationoflignocellulose pages 5-7, gurovic2023regulationoflignocellulose pages 2-3)
- Hartmann M et al. **Long-term mitigation of drought changes the functional potential and life-strategies of the forest soil microbiome involved in organic matter decomposition.** *Frontiers in Microbiology.* Sep 2023. DOI: **10.3389/fmicb.2023.1267270**. URL: https://doi.org/10.3389/fmicb.2023.1267270 (hartmann2023longtermmitigationof pages 9-12)
- Duran K et al. **The secretome of *Agaricus bisporus*: Temporal dynamics of plant polysaccharides and lignin degradation.** *iScience.* 21 Jul 2023. DOI: **10.1016/j.isci.2023.107087**. URL: https://doi.org/10.1016/j.isci.2023.107087 (duran2023thesecretomeof pages 7-8)
- Chen L et al. **Metagenomic highlight contrasting elevational pattern of bacteria- and fungi-derived compound decompositions in forest soils.** *Plant and Soil.* Jun 2023. DOI: **10.1007/s11104-023-06104-5**. URL: https://doi.org/10.1007/s11104-023-06104-5 (chen2023metagenomichighlightcontrasting pages 9-10)
- Wunderlich G et al. **Understanding the microbial fibre degrading communities & processes in the equine gut.** *Animal Microbiome.* Jan 2023. DOI: **10.1186/s42523-022-00224-6**. URL: https://doi.org/10.1186/s42523-022-00224-6 (wunderlich2023understandingthemicrobial pages 4-6)


References

1. (wang2024mechanismsandimplications pages 4-5): Chaoqun Wang and Yakov Kuzyakov. Mechanisms and implications of bacterial–fungal competition for soil resources. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae073, doi:10.1093/ismejo/wrae073. This article has 586 citations.

2. (wang2024mechanismsandimplications pages 5-7): Chaoqun Wang and Yakov Kuzyakov. Mechanisms and implications of bacterial–fungal competition for soil resources. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae073, doi:10.1093/ismejo/wrae073. This article has 586 citations.

3. (gurovic2023regulationoflignocellulose pages 2-3): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

4. (duran2023thesecretomeof pages 7-8): Katharina Duran, Joris Magnin, Antoine H.P. America, Mao Peng, Roelant Hilgers, Ronald P. de Vries, Johan J.P. Baars, Willem J.H. van Berkel, Thomas W. Kuyper, and Mirjam A. Kabel. The secretome of agaricus bisporus: temporal dynamics of plant polysaccharides and lignin degradation. iScience, 26:107087, Jul 2023. URL: https://doi.org/10.1016/j.isci.2023.107087, doi:10.1016/j.isci.2023.107087. This article has 15 citations and is from a peer-reviewed journal.

5. (wang2024mechanismsandimplications pages 2-3): Chaoqun Wang and Yakov Kuzyakov. Mechanisms and implications of bacterial–fungal competition for soil resources. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae073, doi:10.1093/ismejo/wrae073. This article has 586 citations.

6. (wang2024mechanismsandimplications pages 1-2): Chaoqun Wang and Yakov Kuzyakov. Mechanisms and implications of bacterial–fungal competition for soil resources. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae073, doi:10.1093/ismejo/wrae073. This article has 586 citations.

7. (tome2024comparativegenomicsand pages 9-10): Luiz Marcelo Ribeiro Tomé, Gabriel Quintanilha-Peixoto, Diogo Henrique Costa-Rezende, Carlos A. Salvador-Montoya, Domingos Cardoso, Daniel S. Araújo, Jorge Marcelo Freitas, Gabriela Bielefeld Nardoto, Genivaldo Alves-Silva, Elisandro Ricardo Drechsler-Santos, and Aristóteles Góes-Neto. Comparative genomics and stable isotope analysis reveal the saprotrophic-pathogenic lifestyle of a neotropical fungus. Aug 2024. URL: https://doi.org/10.1128/mbio.01423-24, doi:10.1128/mbio.01423-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (tome2024comparativegenomicsand pages 10-13): Luiz Marcelo Ribeiro Tomé, Gabriel Quintanilha-Peixoto, Diogo Henrique Costa-Rezende, Carlos A. Salvador-Montoya, Domingos Cardoso, Daniel S. Araújo, Jorge Marcelo Freitas, Gabriela Bielefeld Nardoto, Genivaldo Alves-Silva, Elisandro Ricardo Drechsler-Santos, and Aristóteles Góes-Neto. Comparative genomics and stable isotope analysis reveal the saprotrophic-pathogenic lifestyle of a neotropical fungus. Aug 2024. URL: https://doi.org/10.1128/mbio.01423-24, doi:10.1128/mbio.01423-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (pena2024mycorrhizalsymbiosisand pages 13-13): Rodica Pena and Mark Tibbett. Mycorrhizal symbiosis and the nitrogen nutrition of forest trees. Applied Microbiology and Biotechnology, Sep 2024. URL: https://doi.org/10.1007/s00253-024-13298-w, doi:10.1007/s00253-024-13298-w. This article has 49 citations and is from a domain leading peer-reviewed journal.

10. (gurovic2023regulationoflignocellulose pages 5-7): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

11. (hartmann2023longtermmitigationof pages 9-12): Martin Hartmann, Claude Herzog, Ivano Brunner, Beat Stierli, Folker Meyer, Nina Buchmann, and Beat Frey. Long-term mitigation of drought changes the functional potential and life-strategies of the forest soil microbiome involved in organic matter decomposition. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1267270, doi:10.3389/fmicb.2023.1267270. This article has 20 citations and is from a peer-reviewed journal.

12. (delancey2024shiftingfungalguild pages 1-2): Lang C. DeLancey, François Maillard, Sarah E. Hobbie, and Peter G. Kennedy. Shifting fungal guild abundances are associated with altered temperate forest soil carbon stocks. Ecosystems, 27:986-998, Oct 2024. URL: https://doi.org/10.1007/s10021-024-00934-9, doi:10.1007/s10021-024-00934-9. This article has 9 citations and is from a domain leading peer-reviewed journal.

13. (delancey2024shiftingfungalguild pages 9-10): Lang C. DeLancey, François Maillard, Sarah E. Hobbie, and Peter G. Kennedy. Shifting fungal guild abundances are associated with altered temperate forest soil carbon stocks. Ecosystems, 27:986-998, Oct 2024. URL: https://doi.org/10.1007/s10021-024-00934-9, doi:10.1007/s10021-024-00934-9. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (tome2024comparativegenomicsand pages 1-2): Luiz Marcelo Ribeiro Tomé, Gabriel Quintanilha-Peixoto, Diogo Henrique Costa-Rezende, Carlos A. Salvador-Montoya, Domingos Cardoso, Daniel S. Araújo, Jorge Marcelo Freitas, Gabriela Bielefeld Nardoto, Genivaldo Alves-Silva, Elisandro Ricardo Drechsler-Santos, and Aristóteles Góes-Neto. Comparative genomics and stable isotope analysis reveal the saprotrophic-pathogenic lifestyle of a neotropical fungus. Aug 2024. URL: https://doi.org/10.1128/mbio.01423-24, doi:10.1128/mbio.01423-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

15. (gurovic2023regulationoflignocellulose pages 2-2): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

16. (wunderlich2023understandingthemicrobial pages 4-6): Georgia Wunderlich, Michelle Bull, Tom Ross, Michael Rose, and Belinda Chapman. Understanding the microbial fibre degrading communities & processes in the equine gut. Animal Microbiome, Jan 2023. URL: https://doi.org/10.1186/s42523-022-00224-6, doi:10.1186/s42523-022-00224-6. This article has 54 citations and is from a peer-reviewed journal.

17. (shabaev2024saprotrophicwooddecay pages 8-10): Alexander V. Shabaev, Olga S. Savinova, Konstantin V. Moiseenko, Olga A. Glazunova, and Tatyana V. Fedorova. Saprotrophic wood decay ability and plant cell wall degrading enzyme system of the white rot fungus crucibulum laeve: secretome, metabolome and genome investigations. Journal of Fungi, 11:21, Dec 2024. URL: https://doi.org/10.3390/jof11010021, doi:10.3390/jof11010021. This article has 8 citations.

18. (gurovic2023regulationoflignocellulose pages 3-4): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

19. (chen2023metagenomichighlightcontrasting pages 9-10): Lan Chen, Jieying Wang, Liyuan He, Xiaofeng Xu, Jun Wang, Chengjie Ren, Yaoxin Guo, and Fazhu Zhao. Metagenomic highlight contrasting elevational pattern of bacteria- and fungi-derived compound decompositions in forest soils. Plant and Soil, 490:617-629, Jun 2023. URL: https://doi.org/10.1007/s11104-023-06104-5, doi:10.1007/s11104-023-06104-5. This article has 15 citations and is from a domain leading peer-reviewed journal.

20. (shabaev2024saprotrophicwooddecay media f0c43fde): Alexander V. Shabaev, Olga S. Savinova, Konstantin V. Moiseenko, Olga A. Glazunova, and Tatyana V. Fedorova. Saprotrophic wood decay ability and plant cell wall degrading enzyme system of the white rot fungus crucibulum laeve: secretome, metabolome and genome investigations. Journal of Fungi, 11:21, Dec 2024. URL: https://doi.org/10.3390/jof11010021, doi:10.3390/jof11010021. This article has 8 citations.

21. (shabaev2024saprotrophicwooddecay media 54fb5969): Alexander V. Shabaev, Olga S. Savinova, Konstantin V. Moiseenko, Olga A. Glazunova, and Tatyana V. Fedorova. Saprotrophic wood decay ability and plant cell wall degrading enzyme system of the white rot fungus crucibulum laeve: secretome, metabolome and genome investigations. Journal of Fungi, 11:21, Dec 2024. URL: https://doi.org/10.3390/jof11010021, doi:10.3390/jof11010021. This article has 8 citations.