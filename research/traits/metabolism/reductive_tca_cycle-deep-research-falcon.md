---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:45:50.044818'
end_time: '2026-06-18T06:02:43.770102'
duration_seconds: 1013.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: reductive tricarboxylic acid cycle
  trait_identifier: traitmech:000021
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: reductive_tca_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan
    cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates
    in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium)
    and Aquificales.
  parent_traits: traitmech:000019
  synonyms: reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive\
    \ citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) |\
    \ DOI:10.1146/annurev-marine-120709-142712:  (H\xFCgler & Sievert document the\
    \ rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)"
  causal_graph_summary: 'rtca_reverse_tricarboxylic_acid_co2_fixation: 3 nodes, 2
    edges'
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
- **Trait label:** reductive tricarboxylic acid cycle
- **METPO identifier:** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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
- **Trait label:** reductive tricarboxylic acid cycle
- **METPO identifier:** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Reductive Tricarboxylic Acid (rTCA) Cycle (METPO:traitmech:000021)

### 0. Target trait
**Trait label:** reductive tricarboxylic acid cycle (aka reductive citric acid cycle; reverse Krebs; Arnon–Buchanan cycle) (petushkova2024thecompletegenome pages 10-12, heker2025chemoorganoautotrophiclifestyleof pages 2-2)  
**METPO:** traitmech:000021  
**Category:** METABOLISM  

---

## 1. Trait scope (phenotype/capacity) and boundary cases

### 1.1 Current definition (curation-ready)
The **reductive tricarboxylic acid (rTCA) cycle** is an **autotrophic CO₂-fixation pathway** that uses **a net-reductive direction of central TCA reactions** to assimilate inorganic carbon into biomass precursors, with key oxidative-TCA irreversible steps replaced by alternative enzyme modules. Core rTCA-specific “direction-switch” steps include (i) **citrate cleavage** to acetyl‑CoA + oxaloacetate (via **ATP-citrate lyase, ACL**, or the **citryl‑CoA synthetase/citryl‑CoA lyase** two-enzyme system) and (ii) **reductive carboxylations** driven by **ferredoxin-dependent oxidoreductases** such as PFOR and OGOR/KOR. (sokolskyi2023roleofhorizontal pages 1-6, prioretti2023carbonfixationin pages 6-8)

### 1.2 What the trait is NOT (nearby traits)
* **Not** the oxidative (canonical) TCA cycle used for complete oxidation of acetyl‑CoA. A key genomic discriminator in some taxa is the presence of **rTCA marker genes (e.g., aclAB)** with **absence of oxidative-TCA marker citrate synthase (gltA)** in lineages relying primarily on rTCA for carbon assimilation. (power2024agenusin pages 5-6)
* **Not** “reductive carboxylation” of glutamine-derived carbon in eukaryotic mitochondria (a cancer/metazoan context); this is distinct from microbial autotrophic rTCA trait curation.
* **Not** Wood–Ljungdahl pathway autotrophy; rTCA may co-occur, but is a distinct mechanism.

### 1.3 Boundary cases (important for curation)
**Partial/open rTCA:** genomes may encode many rTCA enzymes but lack the citrate-cleavage substitute(s) required to close the cycle. In *Thiocapsa bogorovii* BBS, authors describe an “**open rTCA cycle**” because genes encoding enzymes that replace citrate synthase/citrate cleavage were **not identified**; such cases should be treated as **insufficient evidence for full trait presence**. (petushkova2024thecompletegenome pages 10-12)

---

## 2. Recent developments (2023–2024 prioritized)

### 2.1 Mechanistic enzymology and electron flow (2023)
**Ferredoxin partnering for rTCA carboxylations (Aquifex):** Proteomics/biochemistry in *Aquifex aeolicus* supports rTCA functionality and emphasizes that **PFOR and OGOR** are key rTCA enzymes requiring strong reductants. Two **low-potential, oxygen-stable [4Fe–4S] ferredoxins (Fd6/Fd7)** were purified and shown to **interact and exchange electrons with PFOR and OGOR**, supporting an explicit mechanistic edge from **reduced ferredoxin → PFOR/OGOR → CO₂-fixing carboxylations**. (prioretti2023carbonfixationin pages 6-8, prioretti2023carbonfixationin pages 16-17)

### 2.2 Environmental genomics/ecology linking rTCA to geochemistry (2024)
**Hot-spring primary production coupling sulfur oxidation and rTCA:** A metagenomic analysis of the boiling (85°C) Lotus Pond hot spring vent-water reports that Aquificae likely act as key primary producers, with **chemolithotrophic sulfur oxidation (Sox) as the principal energy pathway** and **rTCA as the predominant carbon fixation pathway**. Quantitatively, Aquificae comprised **~80% of 16S rRNA reads** (Proteobacteria ~14%), and a Hydrogenobacter-related MAG accounted for **~56% of the metagenome**; two Aquificae MAGs together were **59.4%** of the metagenome. The same dataset reports **high counts of rTCA marker genes**, including homologs of **aclAB**, **frd**, and **kor**, supporting the environmental prevalence of rTCA gene complements in sulfur-rich hot spring ecosystems. (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 26-27, mondal2024aquificaeovercomescompetition pages 17-19, mondal2024aquificaeovercomescompetition pages 16-17)

**Microaerophilic niche association in Aquificota:** Comparative ecological + genomic analyses of *Venenivibrio stagnispumantis* CP.B2^T (Hydrogenothermaceae, Aquificota) report maximal read abundance at **pH 4–6 and 50–70°C** in low-ORP springs, and the genome encoded **ACL (aclAB)** consistent with rTCA. The strain shows **microaerophilic/low-O₂ adaptation** (cytochrome bd as sole terminal oxidase; O₂ tolerance tested in low ranges), supporting environmental “low O₂” as a recurring context where rTCA lineages thrive. (power2024agenusin pages 1-2, power2024agenusin pages 5-6)

### 2.3 Quantitative CO₂ fixation evidence in a non-model halophile (2023)
**Radiolabeled bicarbonate fixation + genomic rTCA (Halomonas):** *Halomonas rowanensis* was proposed as a facultative chemoautotroph whose genome contains a “**putative complete rTCA cycle**,” and chemoautotrophic CO₂ fixation was supported by **radiolabeled NaH¹⁴CO₃ incorporation** in mineral medium with **thiosulfate** as energy source. The study reports fixation rates such as **2.21 ± 0.75 nmol/h/mL** at OD600 = 4.0 (and increased incorporation upon transition to chemoautotrophic conditions). The precise sulfur-energy mechanism is uncertain because canonical Sox was not annotated, but thiosulfate dependence is explicit. (faulkner2023chemoautotrophicproductionof pages 7-9, faulkner2023chemoautotrophicproductionof pages 9-11)

---

## 3. Current applications and real-world implementations

### 3.1 Industrial biotechnology: engineered “reductive TCA” modules for organic acids
Although TraitMech curations typically focus on **native microbial traits**, recent biomanufacturing work shows how rTCA-like reductive modules are repurposed to drive carbon flux toward C4 products:

**High-level succinic acid via engineered reductive TCA branch (Yarrowia lipolytica):** Cui et al. engineered a strictly aerobic yeast for efficient succinic acid production, implementing a **reductive TCA branch** and addressing redox balance by coupling oxidative and reductive TCA reactions. Quantitative pilot-scale performance: **111.9 g/L succinic acid**, **yield 0.79 g/g glucose** within **62 h**, productivity **1.79 g/L/h**, with fermentation reaching very low pH (reported pH 2.49) and recovery of succinic acid crystals. As a key mechanistic intervention, they introduced and optimized a **fumarate reductase (Frd)** module and related enzymes (e.g., fumarase, malate dehydrogenase), then re-localized flux to the mitochondria for NADH regeneration. (cui2023reconfigurationofthe pages 1-2, cui2023reconfigurationofthe pages 5-6, cui2023reconfigurationofthe pages 2-3)

A pathway schematic of the engineered oxidative+reductive TCA coupling (mitochondrial rTCA branch enzymes annotated) is shown in the extracted figure. (cui2023reconfigurationofthe media 8b82cbd3)

### 3.2 CO₂-based production in halophiles (chemoautotrophic chassis)
**CO₂-powered product formation in Halomonas:** *H. rowanensis* can be used as a robust host for chemicals production in saline media; the paper demonstrates product formation (bio-propane, PHB/PHA, ectoine) and links chemoautotrophic growth to rTCA-based fixation supported by radiolabeled bicarbonate incorporation. Quantitative examples include bio-propane titers up to **1.2 mg/L** with butyrate supplementation (heterotrophic boost), and ectoine and PHA accumulation reported under heterotrophic vs chemoautotrophic conditions (values in the paper excerpted for ectoine/PHA). (faulkner2023chemoautotrophicproductionof pages 9-11, faulkner2023chemoautotrophicproductionof pages 11-13)

---

## 4. Expert opinion / authoritative mechanistic analysis (within retrieved sources)

### 4.1 Energetic constraints and CO₂ dependence
Environmental reconstructions emphasize that key rTCA carboxylations can be energetically challenging and are supported by strong electron donors and high CO₂ availability. For mangrove-associated MAG reconstructions, the reductive carboxylation catalyzed by PFOR is described as energetically unfavorable and requiring a **strong reduction potential** and **high CO₂ concentration**; rTCA/roTCA operation is discussed as being enabled when CO₂ partial pressure increases. (laux2024livinginmangroves pages 18-19)

### 4.2 Community/ecosystem coupling: energy metabolism as driver
Hot-spring metagenomics frames rTCA predominance not in isolation but as coupled to **chemolithotrophic energy metabolisms** (notably sulfur oxidation via Sox), consistent with a causal-graph representation where electron donors/acceptors and respiratory modules are upstream of carbon fixation capacity. (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 16-17)

---

## 5. Relevant statistics and data points (recent sources)

### 5.1 Environmental prevalence and marker-gene counts (hot spring)
* Lotus Pond vent-water: **~8.5 × 10⁴ cells mL⁻¹**, live:dead **1.7**; **~80%** of 16S rRNA reads attributed to Aquificae; Hydrogenobacter-related MAG alone **~56%** of metagenome. (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 26-27)
* rTCA marker gene counts in Lotus Pond assembled metagenome include homologs for **ACL (aclAB)**, **fumarate reductase (frdABCDE)**, and **ferredoxin-dependent 2‑oxoglutarate synthase (korABCD)** among others (counts reported in the manuscript excerpts). (mondal2024aquificaeovercomescompetition pages 17-19)

### 5.2 Quantified CO₂ fixation assays (Halomonas)
* Radiolabeled bicarbonate fixation in *H. rowanensis*: **2.21 ± 0.75 nmol/h/mL** at OD600 = 4.0; increased incorporation after pre-growth under chemoautotrophic conditions. (faulkner2023chemoautotrophicproductionof pages 7-9)

### 5.3 Bioprocess performance (engineered reductive TCA branch)
* *Y. lipolytica* succinic acid: **111.9 g/L**, **0.79 g/g**, **62 h**, **1.79 g/L/h** (pilot scale). (cui2023reconfigurationofthe pages 1-2, cui2023reconfigurationofthe pages 5-6)

---

## 6. Candidate causal-graph nodes (grouped by type)

### 6.1 Pathways / modules
* rTCA cycle / reverse TCA (METPO:traitmech:000021) (petushkova2024thecompletegenome pages 10-12, prioretti2023carbonfixationin pages 6-8)
* Sulfur oxidation via Sox system (module; gene set soxXABYZW, etc.) (mondal2024aquificaeovercomescompetition pages 16-17)
* Inorganic carbon uptake pump (DabAB complex; label) (prioretti2023carbonfixationin pages 6-8)

### 6.2 Genes / proteins / enzyme complexes (with grounding candidates)
* **ATP citrate lyase (ACL)** (EC:2.3.3.8; KEGG K15230/K15231; genes **aclAB**) (sokolskyi2023roleofhorizontal pages 1-6, power2024agenusin pages 5-6)
* **Citryl‑CoA synthetase (CCS)** (EC:6.2.1.18; KEGG K15232/K15233) (sokolskyi2023roleofhorizontal pages 1-6)
* **Citryl‑CoA lyase (CCL)** (EC:4.1.3.34; KEGG K15234) (sokolskyi2023roleofhorizontal pages 1-6)
* **Pyruvate:ferredoxin oxidoreductase (PFOR/Por)** (EC:1.2.7.1) (prioretti2023carbonfixationin pages 6-8)
* **2‑Oxoglutarate:ferredoxin oxidoreductase (OGOR/KOR)** (EC:1.2.7.3/1.2.7.11; often korAB) (prioretti2023carbonfixationin pages 6-8, laux2024livinginmangroves pages 18-19)
* **Ferredoxins (Fd6/Fd7)** low potential [4Fe–4S] (UniProt IDs not extracted here) (prioretti2023carbonfixationin pages 6-8)
* **Fumarate reductase (Frd)** (engineered example) (cui2023reconfigurationofthe pages 2-3)

### 6.3 Chemicals / metabolites (grounding candidates)
* CO₂ (CHEBI:16526) (sokolskyi2023roleofhorizontal pages 1-6)
* Reduced ferredoxin (CHEBI:57925 candidate) (prioretti2023carbonfixationin pages 6-8)
* NADH (CHEBI:57945) (laux2024livinginmangroves pages 18-19, cui2023reconfigurationofthe pages 5-6)
* Thiosulfate (CHEBI:9568 candidate) (faulkner2023chemoautotrophicproductionof pages 7-9)
* Succinate / succinic acid (CHEBI:15741) (cui2023reconfigurationofthe pages 1-2)

### 6.4 Environmental/external factors (grounding candidates)
* Low O₂ / microaerophily (ENVO term candidate) (power2024agenusin pages 5-6)
* High CO₂ partial pressure (ENVO/condition; CHEBI CO₂) (laux2024livinginmangroves pages 18-19)
* Hot spring / geothermal environment (ENVO:00000051 candidate) (mondal2024aquificaeovercomescompetition pages 1-2)
* Reducing ORP / low oxidation–reduction potential (environmental parameter) (power2024agenusin pages 1-2)

---

## 7. Evidence-backed candidate edges (triples)
The following table is intended to be directly actionable for TraitMech YAML curation.

| Subject node (suggested CURIE) | Predicate | Object node (CURIE) | Evidence snippet | Source (first author year, journal) | DOI/URL | Notes/uncertainty |
|---|---|---|---|---|---|---|
| low O2 / microaerophilic environment (ENVO:00002030 candidate) | associated_with | reductive tricarboxylic acid cycle (METPO:traitmech:000021) | “O2 tolerance reported as <1.25–10% (v/v), consistent with microaerophilic/low‑oxygen adaptation” and CP.B2T encoded Type I rTCA | Power 2024, Nature Communications | https://doi.org/10.1038/s41467-023-43960-2 | Environment-trait association from one Aquificota lineage; curate as taxon-supported, not universal. (power2024agenusin pages 5-6) |
| ATP citrate lyase complex aclAB (EC:2.3.3.8; KEGG K15230/K15231) | enables | reductive tricarboxylic acid cycle (METPO:traitmech:000021) | “citrate cleavage into oxaloacetate and acetyl-CoA … can be performed by either … ATP-citrate lyase (ACL)” | Sokolskyi 2023, bioRxiv | https://doi.org/10.1101/2022.10.25.513756 | Enzyme-definition edge; source is preprint but aligns with canonical biochemistry. (sokolskyi2023roleofhorizontal pages 1-6) |
| citryl-CoA synthetase/lyase route (EC:6.2.1.18/4.1.3.34; KEGG K15232/K15233/K15234) | alternative_to | ATP citrate lyase complex aclAB (EC:2.3.3.8) | “citrate cleavage … can be performed by either a two-enzyme system (CCS/CCL) or a single enzyme (ACL)” | Sokolskyi 2023, bioRxiv | https://doi.org/10.1101/2022.10.25.513756 | Alternative enzyme module for citrate cleavage in rTCA. (sokolskyi2023roleofhorizontal pages 1-6) |
| reduced ferredoxin (CHEBI:57925 candidate) | electron_donor_for | pyruvate:ferredoxin oxidoreductase PFOR (EC:1.2.7.1) | “PFOR and OGOR … require a strong reduction potential” and Fd6/Fd7 “could be the physiological electron donors” | Prioretti 2023, Life | https://doi.org/10.3390/life13030627 | Strong biochemical support in Aquifex; likely generalizable to ferredoxin-dependent rTCA variants. (prioretti2023carbonfixationin pages 6-8, prioretti2023carbonfixationin pages 16-17) |
| reduced ferredoxin (CHEBI:57925 candidate) | electron_donor_for | 2-oxoglutarate:ferredoxin oxidoreductase OGOR/KOR (EC:1.2.7.3/1.2.7.11) | “Fd6 and Fd7 … can physically interact and exchange electrons with both PFOR and OGOR” | Prioretti 2023, Life | https://doi.org/10.3390/life13030627 | Strong biochemical support from purified proteins in Aquifex aeolicus. (prioretti2023carbonfixationin pages 6-8) |
| pyruvate:ferredoxin oxidoreductase PFOR (EC:1.2.7.1) | part_of | reductive tricarboxylic acid cycle (METPO:traitmech:000021) | “Key enzymes of this pathway are pyruvate:ferredoxin oxidoreductase (PFOR) and 2-oxoglutarate:ferredoxin oxidoreductase (OGOR)” | Prioretti 2023, Life | https://doi.org/10.3390/life13030627 | Canonical rTCA enzyme; strong evidence. (prioretti2023carbonfixationin pages 6-8) |
| 2-oxoglutarate:ferredoxin oxidoreductase OGOR/KOR (EC:1.2.7.3/1.2.7.11) | part_of | reductive tricarboxylic acid cycle (METPO:traitmech:000021) | “Key enzymes of this pathway are pyruvate:ferredoxin oxidoreductase (PFOR) and 2-oxoglutarate:ferredoxin oxidoreductase (OGOR)” | Prioretti 2023, Life | https://doi.org/10.3390/life13030627 | Canonical rTCA enzyme; strong evidence. (prioretti2023carbonfixationin pages 6-8) |
| high CO2 concentration (CHEBI:16526; ENVO high-partial-pressure candidate) | promotes | reductive carboxylation by PFOR/roTCA operation | “requires … high CO2 concentration” and “rTCA genes can operate reversibly (roTCA) when CO2 partial pressure increases” | Laux 2024, BMC Microbiology | https://doi.org/10.1186/s12866-024-03390-6 | Mechanistic but context from mangrove MAG reconstruction; may be condition-dependent. (laux2024livinginmangroves pages 18-19) |
| high CO2 partial pressure (CHEBI:16526) | promotes | growth supported by rTCA-like metabolism | “faster growth at 20–40% CO2 … 17 h” versus “29 h at 5% CO2; no growth at ~1–2% CO2” | Heker 2025, Communications Biology | https://doi.org/10.1038/s42003-025-08172-y | Useful environment→phenotype edge; from anaerobic culture N47 discussion and comparative thermophile evidence, so curate as supportive/uncertain. (heker2025chemoorganoautotrophiclifestyleof pages 1-2) |
| sulfur oxidation via Sox system (KEGG module candidate) | provides_energy_for | rTCA-based carbon fixation (METPO:traitmech:000021) | “chemolithotrophic sulfur oxidation (Sox) as the principal energy-yielding pathway and the reductive tricarboxylic acid (rTCA) cycle as the predominant carbon fixation pathway” | Mondal 2024, PLOS ONE | https://doi.org/10.1371/journal.pone.0310595 | Ecosystem-level coupling; not direct regulation. Strong for Lotus Pond Aquificae. (mondal2024aquificaeovercomescompetition pages 1-2) |
| Sox gene complement (soxXABYZW; label) | encoded_by | Aquificae-dominated MAGs (NCBITaxon:Aquificota candidate) | “LotusPond_MAG_Unclassified_Aquificaceae encodes SoxX/A/B/Y/Z and SoxW” | Mondal 2024, PLOS ONE | https://doi.org/10.1371/journal.pone.0310595 | Taxon-specific gene-content edge supporting sulfur oxidation capacity. (mondal2024aquificaeovercomescompetition pages 17-19, mondal2024aquificaeovercomescompetition pages 16-17) |
| Aquificae-dominated community (NCBITaxon:Aquificota candidate) | enriched_in | rTCA marker genes aclAB/frd/kor | “5, 218, and 57 homologs for ATP-citrate lyase … fumarate reductase … and … KorABCD”; “Most … closest sequence similarities with … Aquificae” | Mondal 2024, PLOS ONE | https://doi.org/10.1371/journal.pone.0310595 | Community-genomic association; good edge for taxa↔pathway support. (mondal2024aquificaeovercomescompetition pages 17-19) |
| reductive tricarboxylic acid cycle (METPO:traitmech:000021) | fixes | carbon dioxide (CHEBI:16526) | “a carbon-fixation pathway” that “can incorporate four molecules of CO2 per full cycle” | Sokolskyi 2023, bioRxiv | https://doi.org/10.1101/2022.10.25.513756 | Stoichiometry from preprint; use cautiously because some sources frame net output differently. (sokolskyi2023roleofhorizontal pages 1-6) |
| rTCA gene complement in Halomonas rowanensis (label) | supports | bicarbonate incorporation / CO2 fixation | “a putative complete reductive tricarboxylic acid (rTCA) cycle” and radiolabelled bicarbonate fixation “2.21 ± 0.75 nmol/h/mL” | Faulkner 2023, Biotechnol Biofuels Bioprod | https://doi.org/10.1186/s13068-023-02404-1 | Strong genome+assay evidence for functional CO2 fixation; pathway assignment remains genomic rather than enzyme-purified. (faulkner2023chemoautotrophicproductionof pages 7-9, faulkner2023chemoautotrophicproductionof pages 1-2) |
| thiosulfate oxidation (CHEBI:9568 candidate) | provides_energy_for | CO2 fixation in Halomonas rowanensis | “thiosulfate as the sole energy source” with measurable radiolabelled bicarbonate incorporation | Faulkner 2023, Biotechnol Biofuels Bioprod | https://doi.org/10.1186/s13068-023-02404-1 | Energy mechanism unresolved because canonical Sox was not annotated; curate as supported but uncertain mechanistically. (faulkner2023chemoautotrophicproductionof pages 7-9, faulkner2023chemoautotrophicproductionof pages 9-11) |
| reductive TCA branch engineering in mitochondria (label) | increases | succinic acid production (CHEBI:15741) | “coupling the oxidative and reductive TCA cycle for NADH regeneration results in improved SA production” | Cui 2023, Nature Communications | https://doi.org/10.1038/s41467-023-44245-4 | Engineered-system edge, not native microbial trait edge; useful application note. (cui2023reconfigurationofthe pages 1-2, cui2023reconfigurationofthe media 8b82cbd3) |
| mitochondrial fumarate reductase TbFrd + EcFum + YlMdh1/2 module (label) | enables | reductive TCA succinate branch flux | “the key enzyme fumarate reductase (Frd) was introduced” and co-expression with “EcFum and YlMdh1” reached “0.85 g/g glucose” | Cui 2023, Nature Communications | https://doi.org/10.1038/s41467-023-44245-4 | Specific to engineered Yarrowia; not evidence for native autotrophic rTCA. (cui2023reconfigurationofthe pages 2-3, cui2023reconfigurationofthe pages 3-4) |
| reductive TCA branch engineering in Yarrowia lipolytica (label) | produces | succinic acid 111.9 g/L, yield 0.79 g/g glucose | “111.9 g/L SA with a yield of 0.79 g/g glucose within 62 h” | Cui 2023, Nature Communications | https://doi.org/10.1038/s41467-023-44245-4 | Real-world biomanufacturing implementation; clearly engineered/non-native. (cui2023reconfigurationofthe pages 1-2, cui2023reconfigurationofthe pages 5-6) |
| absence of ACL/CCS/CCL substitute genes (label) | prevents_full_realization_of | closed rTCA cycle | “open rTCA cycle … genes for enzymes that would substitute citrate synthase were not identified” | Petushkova 2024, Microorganisms | https://doi.org/10.3390/microorganisms12020391 | Important boundary-case warning: partial/open rTCA should not automatically be curated as full trait presence. (petushkova2024thecompletegenome pages 10-12) |


*Table: This table lists evidence-backed candidate causal edges for curating a TraitMech graph for the microbial reductive tricarboxylic acid cycle. It spans environmental context, key enzymes and electron carriers, pathway-level CO2 fixation, and engineered applications, while flagging uncertain or taxon-specific claims.*

---

## 8. Warnings / curation pitfalls (do not curate without stronger evidence)

1. **Do not curate “rTCA present” from partial gene sets** when citrate cleavage machinery is absent: “open rTCA” cases exist and should be captured as incomplete/uncertain. (petushkova2024thecompletegenome pages 10-12)
2. **Preprint-derived quantitative stoichiometry** (e.g., “CO₂ per cycle”) should be treated as lower-confidence until supported by peer-reviewed biochemical sources; use cautiously for hard-coded stoichiometric edges. (sokolskyi2023roleofhorizontal pages 1-6)
3. **Energy coupling claims** (e.g., thiosulfate oxidation mechanism) may be ambiguous: *H. rowanensis* chemoautotrophy is thiosulfate-dependent, but the precise sulfur oxidation system was not fully resolved (canonical Sox not annotated), so edges from “Sox system” to “energy for rTCA” should be **taxon/context-specific**. (faulkner2023chemoautotrophicproductionof pages 9-11)
4. **Engineered ‘reductive TCA’ in eukaryotes** (e.g., yeast succinate production) is **not** direct evidence that a microbe natively fixes CO₂ via rTCA; include as “application/implementation” evidence only. (cui2023reconfigurationofthe pages 1-2)

---

## 9. DOI-first bibliography (with publication dates and URLs)

* Prioretti L. et al. **Carbon Fixation in the Chemolithoautotrophic Bacterium *Aquifex aeolicus*…** *Life* (Feb 2023). DOI: **10.3390/life13030627**. https://doi.org/10.3390/life13030627 (prioretti2023carbonfixationin pages 6-8, prioretti2023carbonfixationin pages 16-17)
* Faulkner M. et al. **Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel *Halomonas* species**. *Biotechnology for Biofuels and Bioproducts* (Oct 2023). DOI: **10.1186/s13068-023-02404-1**. https://doi.org/10.1186/s13068-023-02404-1 (faulkner2023chemoautotrophicproductionof pages 7-9, faulkner2023chemoautotrophicproductionof pages 9-11, faulkner2023chemoautotrophicproductionof pages 11-13)
* Cui Z. et al. **Reconfiguration of the reductive TCA cycle enables high-level succinic acid production by *Yarrowia lipolytica***. *Nature Communications* (Dec 2023). DOI: **10.1038/s41467-023-44245-4**. https://doi.org/10.1038/s41467-023-44245-4 (cui2023reconfigurationofthe pages 1-2, cui2023reconfigurationofthe pages 5-6, cui2023reconfigurationofthe pages 2-3, cui2023reconfigurationofthe media 8b82cbd3)
* Power J.F. et al. **A genus in the bacterial phylum Aquificota appears to be endemic to Aotearoa-New Zealand**. *Nature Communications* (Jan 2024). DOI: **10.1038/s41467-023-43960-2**. https://doi.org/10.1038/s41467-023-43960-2 (power2024agenusin pages 5-6, power2024agenusin pages 1-2)
* Mondal N. et al. **Aquificae overcomes competition…** *PLOS ONE* (Oct 2024). DOI: **10.1371/journal.pone.0310595**. https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 26-27, mondal2024aquificaeovercomescompetition pages 16-17, mondal2024aquificaeovercomescompetition pages 17-19)
* Laux M. et al. **Living in mangroves: a syntrophic scenario unveiling a resourceful microbiome**. *BMC Microbiology* (Jun 2024). DOI: **10.1186/s12866-024-03390-6**. https://doi.org/10.1186/s12866-024-03390-6 (laux2024livinginmangroves pages 18-19)
* Petushkova E. et al. **The Complete Genome of a Novel Typical Species *Thiocapsa bogorovii*…** *Microorganisms* (Feb 2024). DOI: **10.3390/microorganisms12020391**. https://doi.org/10.3390/microorganisms12020391 (petushkova2024thecompletegenome pages 10-12)

Lower-confidence / preprint (use cautiously):
* Sokolskyi T., DasSarma S. **Role of horizontal gene transfers…** *bioRxiv* (Oct 2023). DOI: **10.1101/2022.10.25.513756**. https://doi.org/10.1101/2022.10.25.513756 (sokolskyi2023roleofhorizontal pages 1-6, sokolskyi2023roleofhorizontal pages 18-23)

---

### Notes for `reductive_tca_cycle.yaml` drafting
A minimal TraitMech causal graph that is well supported by the above evidence can be built around: 
(1) environmental conditions (low O₂; high CO₂), 
(2) electron donors/energy modules (H₂, reduced sulfur/thiosulfate; Sox or sulfur oxidation modules), 
(3) electron carriers (reduced ferredoxin, NADH), 
(4) key enzyme modules (ACL or CCS/CCL; PFOR; OGOR/KOR; FRD as optional/variant), 
leading to 
(5) rTCA pathway activity → CO₂ fixation → biomass precursors.


References

1. (petushkova2024thecompletegenome pages 10-12): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

2. (heker2025chemoorganoautotrophiclifestyleof pages 2-2): Isabelle Heker, Christian Seitz, Lisa Voskuhl, Yachao Kong, Isabell Erdmann, Frederik Götz, Mohamed Hassoun, Claudia Huber, Wolfgang Eisenreich, and Rainer U. Meckenstock. Chemoorganoautotrophic lifestyle of the anaerobic enrichment culture n47 growing on naphthalene. Communications Biology, Jun 2025. URL: https://doi.org/10.1038/s42003-025-08172-y, doi:10.1038/s42003-025-08172-y. This article has 3 citations and is from a peer-reviewed journal.

3. (sokolskyi2023roleofhorizontal pages 1-6): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 5 citations.

4. (prioretti2023carbonfixationin pages 6-8): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 7 citations.

5. (power2024agenusin pages 5-6): Jean F. Power, Carlo R. Carere, Holly E. Welford, Daniel T. Hudson, Kevin C. Lee, John W. Moreau, Thijs J. G. Ettema, Anna-Louise Reysenbach, Charles K. Lee, Daniel R. Colman, Eric S. Boyd, Xochitl C. Morgan, Ian R. McDonald, S. Craig Cary, and Matthew B. Stott. A genus in the bacterial phylum aquificota appears to be endemic to aotearoa-new zealand. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-43960-2, doi:10.1038/s41467-023-43960-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (prioretti2023carbonfixationin pages 16-17): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 7 citations.

7. (mondal2024aquificaeovercomescompetition pages 1-2): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

8. (mondal2024aquificaeovercomescompetition pages 26-27): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

9. (mondal2024aquificaeovercomescompetition pages 17-19): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

10. (mondal2024aquificaeovercomescompetition pages 16-17): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

11. (power2024agenusin pages 1-2): Jean F. Power, Carlo R. Carere, Holly E. Welford, Daniel T. Hudson, Kevin C. Lee, John W. Moreau, Thijs J. G. Ettema, Anna-Louise Reysenbach, Charles K. Lee, Daniel R. Colman, Eric S. Boyd, Xochitl C. Morgan, Ian R. McDonald, S. Craig Cary, and Matthew B. Stott. A genus in the bacterial phylum aquificota appears to be endemic to aotearoa-new zealand. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-43960-2, doi:10.1038/s41467-023-43960-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

12. (faulkner2023chemoautotrophicproductionof pages 7-9): Matthew Faulkner, Robin Hoeven, Paul P. Kelly, Yaqi Sun, Helen Park, Lu-Ning Liu, Helen S. Toogood, and Nigel S. Scrutton. Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel halomonas species. Biotechnology for Biofuels and Bioproducts, Oct 2023. URL: https://doi.org/10.1186/s13068-023-02404-1, doi:10.1186/s13068-023-02404-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (faulkner2023chemoautotrophicproductionof pages 9-11): Matthew Faulkner, Robin Hoeven, Paul P. Kelly, Yaqi Sun, Helen Park, Lu-Ning Liu, Helen S. Toogood, and Nigel S. Scrutton. Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel halomonas species. Biotechnology for Biofuels and Bioproducts, Oct 2023. URL: https://doi.org/10.1186/s13068-023-02404-1, doi:10.1186/s13068-023-02404-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (cui2023reconfigurationofthe pages 1-2): Zhiyong Cui, Yutao Zhong, Zhijie Sun, Zhennan Jiang, Jingyu Deng, Qian Wang, Jens Nielsen, Jin Hou, and Qingsheng Qi. Reconfiguration of the reductive tca cycle enables high-level succinic acid production by yarrowia lipolytica. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44245-4, doi:10.1038/s41467-023-44245-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

15. (cui2023reconfigurationofthe pages 5-6): Zhiyong Cui, Yutao Zhong, Zhijie Sun, Zhennan Jiang, Jingyu Deng, Qian Wang, Jens Nielsen, Jin Hou, and Qingsheng Qi. Reconfiguration of the reductive tca cycle enables high-level succinic acid production by yarrowia lipolytica. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44245-4, doi:10.1038/s41467-023-44245-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

16. (cui2023reconfigurationofthe pages 2-3): Zhiyong Cui, Yutao Zhong, Zhijie Sun, Zhennan Jiang, Jingyu Deng, Qian Wang, Jens Nielsen, Jin Hou, and Qingsheng Qi. Reconfiguration of the reductive tca cycle enables high-level succinic acid production by yarrowia lipolytica. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44245-4, doi:10.1038/s41467-023-44245-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

17. (cui2023reconfigurationofthe media 8b82cbd3): Zhiyong Cui, Yutao Zhong, Zhijie Sun, Zhennan Jiang, Jingyu Deng, Qian Wang, Jens Nielsen, Jin Hou, and Qingsheng Qi. Reconfiguration of the reductive tca cycle enables high-level succinic acid production by yarrowia lipolytica. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44245-4, doi:10.1038/s41467-023-44245-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

18. (faulkner2023chemoautotrophicproductionof pages 11-13): Matthew Faulkner, Robin Hoeven, Paul P. Kelly, Yaqi Sun, Helen Park, Lu-Ning Liu, Helen S. Toogood, and Nigel S. Scrutton. Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel halomonas species. Biotechnology for Biofuels and Bioproducts, Oct 2023. URL: https://doi.org/10.1186/s13068-023-02404-1, doi:10.1186/s13068-023-02404-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

19. (laux2024livinginmangroves pages 18-19): Marcele Laux, Luciane Prioli Ciapina, Fabíola Marques de Carvalho, Alexandra Lehmkuhl Gerber, Ana Paula C. Guimarães, Moacir Apolinário, Jorge Eduardo Santos Paes, Célio Roberto Jonck, and Ana Tereza R. de Vasconcelos. Living in mangroves: a syntrophic scenario unveiling a resourceful microbiome. BMC Microbiology, Jun 2024. URL: https://doi.org/10.1186/s12866-024-03390-6, doi:10.1186/s12866-024-03390-6. This article has 15 citations and is from a peer-reviewed journal.

20. (heker2025chemoorganoautotrophiclifestyleof pages 1-2): Isabelle Heker, Christian Seitz, Lisa Voskuhl, Yachao Kong, Isabell Erdmann, Frederik Götz, Mohamed Hassoun, Claudia Huber, Wolfgang Eisenreich, and Rainer U. Meckenstock. Chemoorganoautotrophic lifestyle of the anaerobic enrichment culture n47 growing on naphthalene. Communications Biology, Jun 2025. URL: https://doi.org/10.1038/s42003-025-08172-y, doi:10.1038/s42003-025-08172-y. This article has 3 citations and is from a peer-reviewed journal.

21. (faulkner2023chemoautotrophicproductionof pages 1-2): Matthew Faulkner, Robin Hoeven, Paul P. Kelly, Yaqi Sun, Helen Park, Lu-Ning Liu, Helen S. Toogood, and Nigel S. Scrutton. Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel halomonas species. Biotechnology for Biofuels and Bioproducts, Oct 2023. URL: https://doi.org/10.1186/s13068-023-02404-1, doi:10.1186/s13068-023-02404-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

22. (cui2023reconfigurationofthe pages 3-4): Zhiyong Cui, Yutao Zhong, Zhijie Sun, Zhennan Jiang, Jingyu Deng, Qian Wang, Jens Nielsen, Jin Hou, and Qingsheng Qi. Reconfiguration of the reductive tca cycle enables high-level succinic acid production by yarrowia lipolytica. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44245-4, doi:10.1038/s41467-023-44245-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

23. (sokolskyi2023roleofhorizontal pages 18-23): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 5 citations.