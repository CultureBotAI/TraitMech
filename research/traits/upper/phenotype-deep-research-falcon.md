---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:52:51.241164'
end_time: '2026-06-18T13:12:14.863063'
duration_seconds: 1163.62
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: phenotype
  trait_identifier: METPO:1000059
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: phenotype
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quality that differentiates specific instances of a species from other
    instances of the same species.
  parent_traits: METPO:1000188
  synonyms: ''
  evidence_summary: 'DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected
    (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2:
    specific characteristic or quality of that entity affected (Supports phenotype
    as an observed quality of an entity.)'
  causal_graph_summary: 'phenotype_quality_child_context: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phenotype
- **METPO identifier:** METPO:1000059
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that differentiates specific instances of a species from other instances of the same species.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity affected (Supports phenotype as an observed quality of an entity.)
- **Existing causal graph summary:** phenotype_quality_child_context: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **phenotype** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/phenotype.yaml`.

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
- **Trait label:** phenotype
- **METPO identifier:** METPO:1000059
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that differentiates specific instances of a species from other instances of the same species.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity affected (Supports phenotype as an observed quality of an entity.)
- **Existing causal graph summary:** phenotype_quality_child_context: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **phenotype** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/phenotype.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **phenotype** (METPO:1000059)

### Scope summary (curation-focused)
In TraitMech terms, **phenotype** is best treated as an *upper-level, assay-observed quality of a biological bearer* (cell/organism/population/community component) rather than a single specific measurable property. A widely used computable representation is the **Entity–Quality (EQ)** pattern, in which a phenotype statement minimally pairs an affected **entity (E)** with a **quality (Q)**, optionally adding a relational target entity (E2) and a qualifier/modifier (M). In EQ, phenotype is modeled as “a quality (Q) that inheres_in some entity (E)”. (mungall2010integratingphenotypeontologies pages 2-3, mungall2010integratingphenotypeontologies pages 5-6)

**Boundary and distinctions for curation**:
- **Phenotype ≠ genotype**: genotype annotations are linked/associated with phenotype classes, but the phenotype itself is the observable quality; the EQ representation is explicitly used to encode phenotype descriptions and then connect them to genotypes. (mungall2010integratingphenotypeontologies pages 2-3)
- **Phenotype depends on environment and measurement context**: phenotype is the “actual observable property… under given environmental conditions,” so assay and environment should typically be modeled as separate context nodes that constrain interpretation of the phenotype. (schofield2010phenotypeontologiesfor pages 1-2)
- **Phenotype vs. trait**: one framing distinguishes *trait* as heritable/measurable feature and *phenotype* as its realized, observed state under conditions; this matters when deciding whether to curate a node as a stable attribute vs. an assay readout. (schofield2010phenotypeontologiesfor pages 1-2)

### Key concepts & definitions (current understanding)
1. **Entity–Quality (EQ) phenotype modeling**: Phenotype descriptions are decomposed into an entity (E) affected and a quality (Q) describing the change; EQ may include a second entity (E2) for relational qualities and a modifier/qualifier (M). (mungall2010integratingphenotypeontologies pages 2-3)
2. **Formal computability**: EQ templates map into OWL/OBO logical expressions (e.g., “quality that inheres_in some entity”), enabling automated reasoning, subsumption, and integration. (mungall2010integratingphenotypeontologies pages 5-6)
3. **Contextualization requirement**: Phenotype comparisons and integration require explicit accounting of environmental and assay context; otherwise a phenotype statement is underspecified. (schofield2010phenotypeontologiesfor pages 1-2)

### Recent developments (prioritizing 2023–2024)
#### A. High-throughput microbial phenotyping platforms
- **Droplet microfluidics for screening engineered strains/enzymes (2023)**: droplet-based microfluidic HTS is emphasized as “fast speed, low cost, high automation, and high screening throughput,” using droplets as microreactors and enabling single-cell encapsulation and sorting (e.g., FADS/AADS). (hu2023advancesindropletbased pages 1-2)
- **Microfluidics + computer vision (2023)**: integration supports label-free, high-throughput single-cell analysis; image phenotypes include “size, morphology, texture, internal structure,” with computer vision needed to process the high-volume data. (zhou2023computervisionmeets pages 1-2)
- **Growth-curve phenotyping computation (2024)**: the open-source R package **gcplyr** supports high-throughput plate-reader growth curve analysis and extracts phenotypic traits such as growth rate, doubling time, lag time, carrying capacity, diauxie, AUC, and extinction time. (blazanin2024gcplyranr pages 2-5)
- **Phenotypic microarrays / substrate utilization phenotyping (2024)**: Biolog FF MicroPlates were used to assay fungal carbon/nitrogen assimilation across 95 substrates and identify substrates promoting sporulation, illustrating scalable phenotype collection for metabolic capacity and developmental phenotypes. (zhao2024highthroughputscreeningcarbon pages 1-2)
- **Emerging label-free metabolite phenotyping (2024)**: vibrational spectro-microscopy (Raman/IR) is positioned as a non-invasive approach to support intact-cell phenotyping, especially when integrated with microfluidics and sorting; throughput/LOD comparisons are given for NMR and FACS. (hanninen2024vibrationalimagingof pages 3-4)

#### B. Knowledge graphs and standards enabling phenotype/mechanism integration
- **KG-Hub (2023)**: provides standardized construction/exchange of biological KGs using modular ETL and Biolink compliance; supports ontology integration, versioned builds, and integration with graph ML (embeddings, link prediction). (caufield2023kghub—buildingandexchanging pages 1-3)
- **Monarch Initiative (2024)**: a cross-species phenotype–gene–disease platform integrating **33 resources and ontologies**, refreshed monthly, supporting deep phenotyping, variant prioritization, and profile matching via UI and API. (putman2024themonarchinitiative pages 1-2)
- **PheKnowLator (Scientific Data 2024)**: an open-source ecosystem for FAIR, ontologically grounded KGs; reports large-scale benchmark construction and provides explicit KG scale/performance metrics relevant to phenotype-driven mechanistic inference. (callahan2024anopensource pages 6-7, callahan2024anopensource pages 1-2)
- **Mechanistic inference in host-associated microbiome (2024 review)**: emphasizes KGs as inference-capable networks; highlights ontology/schema standards (OWL, Biolink), and the importance of mapping/nomenclature standardization for connecting microbes, metabolites, and phenotypes. (santangelo2024integratingbiologicalknowledge pages 11-12)

### Current applications and real-world implementations
1. **Industrial and applied microbiology**
   - **Substrate optimization for growth/sporulation**: high-throughput Biolog phenotyping is used to identify substrates that promote sporulation and may rejuvenate degenerated industrial strains (example: *Rhizopus arrhizus*). (zhao2024highthroughputscreeningcarbon pages 1-2)
   - **Biofoundry screening workflows**: droplet microfluidics and emerging label-free metabolite phenotyping support the “test” phase of design–build–test–learn cycles by enabling rapid screening and selection of improved production phenotypes. (hanninen2024vibrationalimagingof pages 3-4, hu2023advancesindropletbased pages 1-2)

2. **Computational phenotype prediction for antimicrobials and systems biology**
   - **Genome-scale metabolic models (GEMs) + phenotype data**: curated GEMs incorporate Biolog phenotype microarrays and gene essentiality datasets to improve predictions of growth on substrates, auxotrophy, and essential genes—supporting antimicrobial target discovery and rational design. (hirose2024agenomescalemetabolic pages 1-2, leonidou2024genomescalemodelof pages 1-2)

3. **Data integration and hypothesis generation**
   - **Standardized KG infrastructure**: KG-Hub and PheKnowLator provide repeatable pipelines to combine ontologies, databases, and experimental evidence into KGs that support query, reasoning, and machine learning for phenotype-driven inference. (callahan2024anopensource pages 6-7, caufield2023kghub—buildingandexchanging pages 1-3)

### Expert opinions / authoritative analysis (as directly supported)
- **Transporter function is a bottleneck for phenotype prediction**: a 2024 perspective argues that phenotype and interaction predictions from constraint-based models are only as good as transporter annotations; missing/incorrect transporter assignments can cause predicted non-growth, wrong extracellular metabolite accumulation/depletion, and disrupted mutualisms in community models. (casey2024transporterannotationsare pages 1-2, casey2024transporterannotationsare media 395fe32b)
- **KG methodology choices affect inference**: PheKnowLator notes trade-offs between simpler graph models and OWL/semantics-rich models for enabling inference and interoperability, and highlights the need for benchmarking to evaluate representation decisions. (callahan2024anopensource pages 2-4)
- **Mechanistic inference requires careful mapping**: microbiome mechanistic inference reviews emphasize inconsistent nomenclature and schema choice as key limitations when integrating microbial traits, metabolites, and host phenotypes across resources. (santangelo2024integratingbiologicalknowledge pages 11-12)

### Key quantitative statistics (recent)
> - iYH543 (*Streptococcus pyogenes* GEM) reported **92.6% gene-essentiality accuracy**, **95% amino-acid auxotrophy accuracy**, and **88% sole-carbon-source growth accuracy**; curated model size was **543 genes, 970 metabolites, and 1,145 reactions**. (hirose2024agenomescalemetabolic pages 1-2)
> - Biolog FF MicroPlate phenotyping in *Rhizopus arrhizus* assayed **69 strains** across **95 carbon and nitrogen substrates**; the species was reported to utilize **all 95 substrates**. (zhao2024highthroughputscreeningcarbon pages 1-2)
> - Flow cytometry/FACS was cited as enabling very high-throughput single-cell phenotyping at approximately **10^3–10^4 cells per second**. (hanninen2024vibrationalimagingof pages 3-4)
> - NMR-based metabolite phenotyping was described as having a typical **limit of detection of ~1 µM** and automated throughput of roughly **10^2–10^3 samples per day**. (hanninen2024vibrationalimagingof pages 3-4)
> - The largest PheKnowLator benchmark KG was reported to contain **13,803,521 nodes** and **41,116,791 triples**; the cleaned OBO merge contained **545,259 classes** and **13,748,009 triples**. (callahan2024anopensource pages 6-7)
> - Monarch 2024 was reported to integrate **33 biomedical resources and ontologies** into a knowledge graph that is **refreshed monthly**. (putman2024themonarchinitiative pages 1-2)
> - Droplet microfluidic screening reached very high reported frequencies, including **10^8 screens per hour** in one enzyme-evolution context and **kilohertz sorting frequencies** for absorbance-activated droplet sorting. (hu2023advancesindropletbased pages 9-10, hu2023advancesindropletbased pages 12-13)


*Blockquote: This blockquote compiles the main numerical findings most relevant to phenotype causal-graph curation, spanning predictive model accuracy, assay scale, throughput, and knowledge-graph size. It is useful as a quick reference for the strongest quantitative evidence cited in the report.*

---

## Candidate nodes (grouped by type)

### A. Trait/phenotype representation (upper-level)
- **phenotype** (METPO:1000059)
- **quality** (PATO:0000001; general)
- **affected entity** (label-only; may later map to CL/GO/NCBITaxon-specific entities)
- **relational target entity (E2)** (label-only)
- **qualifier/modifier** (label-only; e.g., abnormal/increased/decreased patterns) (mungall2010integratingphenotypeontologies pages 2-3, mungall2010integratingphenotypeontologies pages 5-6)

### B. Assay/measurement entities
- **phenotype microarray / Biolog microplate assay** (OBI label-only; used for substrate utilization phenotypes) (zhao2024highthroughputscreeningcarbon pages 1-2, hirose2024agenomescalemetabolic pages 1-2)
- **plate-reader growth curve assay** (OBI label-only; yields growth curve traits) (blazanin2024gcplyranr pages 2-5)
- **flow cytometry / FACS** (OBI label-only; single-cell throughput) (hanninen2024vibrationalimagingof pages 3-4)
- **NMR metabolomics** (OBI label-only; LOD/throughput) (hanninen2024vibrationalimagingof pages 3-4)
- **droplet microfluidic HTS** (OBI label-only; FADS/AADS etc.) (hu2023advancesindropletbased pages 1-2)
- **microfluidics + computer vision** (OBI label-only; extracts image phenotypes) (zhou2023computervisionmeets pages 1-2)

### C. Environmental & experimental context
- **environmental conditions** (ENVO label-only; nutrient availability, oxygen state, etc.)
- **nutritional conditions / media composition** (OBI label-only; used in GEM validation and phenotyping) (hirose2024agenomescalemetabolic pages 1-2, leonidou2024genomescalemodelof pages 1-2)

### D. Mechanistic biology entities (typical for microbial phenotype explanation)
- **genes** (label-only; e.g., essential genes)
- **transporters / transporter annotations** (GO:0055085 transmembrane transport as a candidate grounding) (casey2024transporterannotationsare pages 1-2)
- **metabolic reactions / pathways / modules** (label-only; e.g., KEGG pathways/modules in KG contexts) (ma2024metagenomickgaknowledge pages 4-5)
- **metabolites/substrates** (CHEBI; e.g., L-arabinose, xylitol; general metabolites) (zhao2024highthroughputscreeningcarbon pages 1-2)
- **genome-scale metabolic model (GEM)** (label-only; iYH543, iRM23NL as examples) (hirose2024agenomescalemetabolic pages 1-2, leonidou2024genomescalemodelof pages 1-2)

---

## Candidate causal edges (evidence-backed)
The following table is designed as a candidate edge set for `data/traits/upper/phenotype.yaml`, with explicit notes on uncertainty and context.

| Edge (subject–predicate–object) | Evidence snippet | Reference (DOI + URL + year/month) | Notes (strength/assay/taxon specificity, how to model context) | Suggested ontology grounding (CURIEs when known) |
|---|---|---|---|---|
| phenotype — represented_as — quality inheres_in entity | “a phenotype is encoded as a quality (Q) that inheres_in some entity (E)” (mungall2010integratingphenotypeontologies pages 5-6) | 10.1186/gb-2010-11-1-r2 · https://doi.org/10.1186/gb-2010-11-1-r2 · 2010-01 | Strong ontology-design evidence; foundational upper-level modeling edge for METPO:1000059 rather than organism-specific biology. | METPO:1000059; PATO:quality; RO:0000052 inheres in; label-only “entity” |
| phenotype — has_participant — entity | “a phenotype description minimally pairs an entity (E) that is affected with a quality (Q)” (mungall2010integratingphenotypeontologies pages 2-3) | 10.1186/gb-2010-11-1-r2 · https://doi.org/10.1186/gb-2010-11-1-r2 · 2010-01 | Strong conceptual edge; useful for graph skeleton. Entity may later be specialized to cell, colony, metabolite level. | METPO:1000059; label-only “affected entity”; PATO:quality |
| phenotype — has_quality — quality | “a phenotype description minimally pairs an entity (E) that is affected with a quality (Q)” (mungall2010integratingphenotypeontologies pages 2-3) | 10.1186/gb-2010-11-1-r2 · https://doi.org/10.1186/gb-2010-11-1-r2 · 2010-01 | Strong conceptual edge; captures phenotype as observed quality, not genotype. | METPO:1000059; PATO:0000001 quality |
| relational phenotype quality — towards — secondary entity | “EQ descriptions may also include an optional second entity (E2) for relational qualities and a modifier (M)” (mungall2010integratingphenotypeontologies pages 2-3) | 10.1186/gb-2010-11-1-r2 · https://doi.org/10.1186/gb-2010-11-1-r2 · 2010-01 | Strong for ontology patterning; curate as optional edge/template, not as universal requirement of phenotype. | PATO relational quality; label-only “secondary entity (E2)” |
| phenotype statement — has_qualifier — modifier | “can include additional relations (e.g., towards an additional entity E2 or has_qualifier M)” (mungall2010integratingphenotypeontologies pages 5-6) | 10.1186/gb-2010-11-1-r2 · https://doi.org/10.1186/gb-2010-11-1-r2 · 2010-01 | Strong for representation; qualifier relation noted by source as placeholder in some ontology contexts, so curation should be conservative. | RO/label-only has_qualifier; PATO abnormal/increased/decreased labels |
| environmental or assay context — constrains — observed phenotype | “phenotype denotes the actual observable property… under given environmental conditions” (schofield2010phenotypeontologiesfor pages 1-2) | 10.1242/dmm.002790 · https://doi.org/10.1242/dmm.002790 · 2010-05 | Strong scope boundary; context should often be modeled separately from phenotype node. Important warning against context-free phenotype assertions. | ENVO:environmental material/habitat labels as applicable; OBI assay labels |
| Biolog FF MicroPlate assay — measured_by — substrate utilization phenotype | “using the Biolog FF MicroPlate for the profiles of utilizing 95 carbon and nitrogen substrates” (zhao2024highthroughputscreeningcarbon pages 1-2) | 10.1186/s13568-024-01733-0 · https://doi.org/10.1186/s13568-024-01733-0 · 2024-06 | Strong assay edge; taxon-specific example is fungal (Rhizopus arrhizus), so assay generalizable but results species-specific. | OBI:assay label-only “Biolog FF MicroPlate assay”; CHEBI substrate labels |
| L-arabinose — promotes — sporulation phenotype | “Eight substrates, especially l-arabinose and xylitol, were capable of promoting sporulation” (zhao2024highthroughputscreeningcarbon pages 1-2) | 10.1186/s13568-024-01733-0 · https://doi.org/10.1186/s13568-024-01733-0 · 2024-06 | Moderate; species-specific to Rhizopus arrhizus and assay-specific. Mark uncertain for broad microbial phenotype curation. | CHEBI:17169 L-arabinose; GO:0043934 sporulation |
| xylitol — promotes — sporulation phenotype | “Eight substrates, especially l-arabinose and xylitol, were capable of promoting sporulation” (zhao2024highthroughputscreeningcarbon pages 1-2) | 10.1186/s13568-024-01733-0 · https://doi.org/10.1186/s13568-024-01733-0 · 2024-06 | Moderate; same caveat as above, taxon- and condition-specific. | CHEBI:17611 xylitol; GO:0043934 sporulation |
| transporter gene annotation accuracy — constrains — growth prediction | “missing assignments can cause a species not to grow” (casey2024transporterannotationsare pages 1-2, casey2024transporterannotationsare media 395fe32b) | 10.3389/fsysb.2024.1394084 · https://doi.org/10.3389/fsysb.2024.1394084 · 2024-07 | Strong mechanistic-modeling edge; applies to GEM prediction rather than direct wet-lab causal biology. Keep modeling context explicit. | label-only “transporter gene annotation”; GO:0055085 transmembrane transport; label-only “growth prediction” |
| transporter directionality annotation error — leads_to — incorrect extracellular metabolite accumulation/depletion prediction | “false assignments can lead to accumulation or depletion of extracellular metabolites” (casey2024transporterannotationsare pages 1-2, casey2024transporterannotationsare media 395fe32b) | 10.3389/fsysb.2024.1394084 · https://doi.org/10.3389/fsysb.2024.1394084 · 2024-07 | Strong for computational causal graph around phenotype prediction; not a direct organismal phenotype claim. | label-only “transporter directionality annotation”; CHEBI:24431 metabolite |
| transporter directionality annotation error — disrupts — mutualism prediction | “directionality errors can break mutualisms” (casey2024transporterannotationsare pages 1-2, casey2024transporterannotationsare media 395fe32b) | 10.3389/fsysb.2024.1394084 · https://doi.org/10.3389/fsysb.2024.1394084 · 2024-07 | Strong but community-model specific; likely too indirect for immediate phenotype.yaml unless community interactions are in scope. | label-only “mutualism prediction”; GO:0055085 transmembrane transport |
| Biolog phenotype microarray data — used_to_curate — genome-scale metabolic model | “Biolog phenotype microarrays were employed to examine the growth phenotypes of S. pyogenes, which further contributed to the refinement of iYH543” (hirose2024agenomescalemetabolic pages 1-2) | 10.1128/msystems.00736-24 · https://doi.org/10.1128/msystems.00736-24 · 2024-09 | Strong; ties assay-observed phenotype to model curation. Taxon-specific to S. pyogenes. | OBI:phenotype microarray label-only; label-only “iYH543 GEM”; NCBITaxon:1314? label-only Streptococcus pyogenes |
| genome-scale metabolic model iYH543 — predicts — gene essentiality phenotype | “92.6% for gene essentiality” (hirose2024agenomescalemetabolic pages 1-2) | 10.1128/msystems.00736-24 · https://doi.org/10.1128/msystems.00736-24 · 2024-09 | Strong quantitative support; prediction edge, not direct mechanistic proof. Model context should be explicit. | label-only “iYH543”; label-only “gene essentiality phenotype” |
| genome-scale metabolic model iYH543 — predicts — amino acid auxotrophy phenotype | “95% for amino acid auxotrophy” (hirose2024agenomescalemetabolic pages 1-2) | 10.1128/msystems.00736-24 · https://doi.org/10.1128/msystems.00736-24 · 2024-09 | Strong quantitative support; taxon-specific. | label-only “iYH543”; label-only “amino acid auxotrophy phenotype” |
| genome-scale metabolic model iYH543 — predicts — growth on sole carbon source phenotype | “88% for sole-carbon-source growth” (hirose2024agenomescalemetabolic pages 1-2) | 10.1128/msystems.00736-24 · https://doi.org/10.1128/msystems.00736-24 · 2024-09 | Strong quantitative support; useful for graph pattern linking model, nutrient, and phenotype. | label-only “sole carbon source growth phenotype”; CHEBI carbon source labels |
| nutritional conditions — modulate — essential gene effects on metabolism | “identified essential genes that impact the metabolism under various conditions” (leonidou2024genomescalemodelof pages 1-2) | 10.1128/spectrum.04006-23 · https://doi.org/10.1128/spectrum.04006-23 · 2024-06 | Moderate-strong; condition dependence explicit, but gene-specific edges are not given in excerpt. | ENVO/OBI condition labels; label-only “essential gene”; GO:0008152 metabolic process |
| microfluidic droplet screening platform — enables — high-throughput phenotype screening | “fast speed, low cost, high automation, and high screening throughput” (hu2023advancesindropletbased pages 1-2) | 10.3390/fermentation10010033 · https://doi.org/10.3390/fermentation10010033 · 2023-12 | Strong technology/application edge; about measurement capability rather than biology itself. | label-only “droplet-based microfluidic HTS”; OBI assay platform label-only |
| FACS/flow cytometry — measured_by — single-cell phenotype throughput | “flow cytometry/FACS provides very high throughput (∼10^3–10^4 cells/s)” (hanninen2024vibrationalimagingof pages 3-4) | 10.1117/1.jbo.29.s2.s22711 · https://doi.org/10.1117/1.jbo.29.s2.s22711 · 2024-07 | Strong measurement edge; relates single-cell phenotype acquisition to assay platform. | OBI:flow cytometry assay label-only; label-only “single-cell phenotype” |
| NMR metabolite profiling — measured_by — metabolite phenotype | “NMR is non-destructive and quantitative… typical LOD ∼1 μM and automated throughput of roughly 10^2–10^3 samples/day” (hanninen2024vibrationalimagingof pages 3-4) | 10.1117/1.jbo.29.s2.s22711 · https://doi.org/10.1117/1.jbo.29.s2.s22711 · 2024-07 | Strong assay-performance edge; useful for phenotype measurement metadata. | OBI:NMR spectroscopy assay label-only; CHEBI:24431 metabolite |
| microfluidics plus computer vision — extracts — cellular size/morphology/texture/internal-structure phenotypic features | “Images contain rich phenotypic signals (‘size, morphology, texture, internal structure’)” (zhou2023computervisionmeets pages 1-2) | 10.1038/s41378-023-00562-8 · https://doi.org/10.1038/s41378-023-00562-8 · 2023-09 | Strong for measurement graph; features are assay-derived observables, not necessarily stable traits. | PATO:size/shape/texture labels; label-only “internal structure phenotype feature” |
| KG-Hub / Monarch / PheKnowLator knowledge graph standards — enable — phenotype and mechanistic inference | “integrating heterogeneous biological data and making inferences” (caufield2023kghub—buildingandexchanging pages 1-3); “integrating phenotypes, genes and diseases across species” (putman2024themonarchinitiative pages 1-2); “ontologically grounded knowledge graphs” (callahan2024anopensource pages 1-2) | 10.1093/bioinformatics/btad418 · https://doi.org/10.1093/bioinformatics/btad418 · 2023-06; 10.1093/nar/gkad1082 · https://doi.org/10.1093/nar/gkad1082 · 2024-11; 10.1038/s41597-024-03171-w · https://doi.org/10.1038/s41597-024-03171-w · 2024-04 | Strong informatics edge; supports downstream causal graph infrastructure rather than biological mechanism. Consider as provenance/representation layer, not TraitMech biological edge. | Biolink:KnowledgeGraph (label-only); HPO/GO/Uberon/MonDO mentioned in sources; label-only KG-Hub, Monarch, PheKnowLator |


*Table: This table lists candidate causal and representation edges for the upper-level microbial trait 'phenotype' (METPO:1000059), spanning ontology structure, environmental and assay context, mechanistic prediction, and measurement technologies. It is designed to support conservative TraitMech curation with source-backed snippets, scope notes, and suggested ontology grounding.*

### Visual evidence (mechanistic modeling failure mode)
Casey et al. provide a schematic of transporter annotation error types and the downstream phenotype-prediction failures (predicted non-growth, metabolite accumulation/depletion, broken mutualism) that arise in metabolic models when transporter knowledge is wrong or missing. (casey2024transporterannotationsare media 395fe32b)

---

## Warnings / curation caveats (do not curate without additional constraints)
1. **Taxon- and assay-specific causal claims**: substrate→sporulation edges (e.g., L-arabinose→sporulation; xylitol→sporulation) were shown in *Rhizopus arrhizus* under Biolog assay conditions; these should be curated as **conditional edges** or marked **uncertain** if used at an upper-level phenotype trait. (zhao2024highthroughputscreeningcarbon pages 1-2)
2. **Prediction vs. biological causation**: GEM “predicts phenotype” edges are strong for linking genotype→network→phenotype in a modeling sense but are not direct causal demonstrations; consider separate predicates (e.g., *predicts*, *simulates*) vs. *causes*. (hirose2024agenomescalemetabolic pages 1-2, leonidou2024genomescalemodelof pages 1-2)
3. **Representation-level edges vs mechanistic edges**: EQ pattern edges define *how to represent phenotype* and should be curated as ontology-design scaffolding; avoid mixing them with organismal mechanisms in the same layer unless TraitMech expects representation edges. (mungall2010integratingphenotypeontologies pages 2-3, mungall2010integratingphenotypeontologies pages 5-6)
4. **Context separation is mandatory**: given that phenotype is environment/assay dependent, store assay/media/environment as separate nodes and edges (e.g., *measured_by*, *constrains*) rather than embedding them into the phenotype node label. (schofield2010phenotypeontologiesfor pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)
- Mungall CJ, et al. *Integrating phenotype ontologies across multiple species.* **Genome Biology** (2010-01). DOI: **10.1186/gb-2010-11-1-r2**. https://doi.org/10.1186/gb-2010-11-1-r2 (mungall2010integratingphenotypeontologies pages 2-3, mungall2010integratingphenotypeontologies pages 5-6)
- Schofield PN, et al. *Phenotype ontologies for mouse and man: bridging the semantic gap.* **Disease Models & Mechanisms** (2010-05). DOI: **10.1242/dmm.002790**. https://doi.org/10.1242/dmm.002790 (schofield2010phenotypeontologiesfor pages 1-2)
- Hu S, et al. *Advances in Droplet-Based Microfluidic High-Throughput Screening…* **Fermentation** (2023-12). DOI: **10.3390/fermentation10010033**. https://doi.org/10.3390/fermentation10010033 (hu2023advancesindropletbased pages 1-2, hu2023advancesindropletbased pages 9-10)
- Zhou S, et al. *Computer vision meets microfluidics: a label-free method for high-throughput cell analysis.* **Microsystems & Nanoengineering** (2023-09). DOI: **10.1038/s41378-023-00562-8**. https://doi.org/10.1038/s41378-023-00562-8 (zhou2023computervisionmeets pages 1-2)
- Caufield JH, et al. *KG-Hub—building and exchanging biological knowledge graphs.* **Bioinformatics** (2023-06). DOI: **10.1093/bioinformatics/btad418**. https://doi.org/10.1093/bioinformatics/btad418 (caufield2023kghub—buildingandexchanging pages 1-3)
- Santangelo BE, et al. *Integrating biological knowledge for mechanistic inference in the host-associated microbiome.* **Frontiers in Microbiology** (2024-04). DOI: **10.3389/fmicb.2024.1351678**. https://doi.org/10.3389/fmicb.2024.1351678 (santangelo2024integratingbiologicalknowledge pages 11-12)
- Callahan TJ, et al. *An open source knowledge graph ecosystem for the life sciences.* **Scientific Data** (2024-04). DOI: **10.1038/s41597-024-03171-w**. https://doi.org/10.1038/s41597-024-03171-w (callahan2024anopensource pages 6-7, callahan2024anopensource pages 2-4)
- Zhao H, et al. *High-throughput screening carbon and nitrogen sources to promote growth and sporulation in Rhizopus arrhizus.* **AMB Express** (2024-06). DOI: **10.1186/s13568-024-01733-0**. https://doi.org/10.1186/s13568-024-01733-0 (zhao2024highthroughputscreeningcarbon pages 1-2)
- Leonidou N, et al. *Genome-scale model of Rothia mucilaginosa predicts gene essentialities and reveals metabolic capabilities.* **Microbiology Spectrum** (2024-06). DOI: **10.1128/spectrum.04006-23**. https://doi.org/10.1128/spectrum.04006-23 (leonidou2024genomescalemodelof pages 1-2)
- Blazanin M. *gcplyr: an R package for microbial growth curve data analysis.* **BMC Bioinformatics** (2024-07). DOI: **10.1186/s12859-024-05817-3**. https://doi.org/10.1186/s12859-024-05817-3 (blazanin2024gcplyranr pages 2-5)
- Casey J, et al. *Transporter annotations are holding up progress in metabolic modeling.* **Frontiers in Systems Biology** (2024-07). DOI: **10.3389/fsysb.2024.1394084**. https://doi.org/10.3389/fsysb.2024.1394084 (casey2024transporterannotationsare pages 1-2, casey2024transporterannotationsare media 395fe32b)
- Hirose Y, et al. *A genome-scale metabolic model of a globally disseminated hyperinvasive M1 strain of Streptococcus pyogenes.* **mSystems** (2024-09). DOI: **10.1128/msystems.00736-24**. https://doi.org/10.1128/msystems.00736-24 (hirose2024agenomescalemetabolic pages 1-2)
- Putman TE, et al. *The Monarch Initiative in 2024: an analytic platform integrating phenotypes, genes and diseases across species.* **Nucleic Acids Research** (2024-11). DOI: **10.1093/nar/gkad1082**. https://doi.org/10.1093/nar/gkad1082 (putman2024themonarchinitiative pages 1-2)
- Hanninen A. *Vibrational imaging of metabolites for improved microbial cell strains.* **Journal of Biomedical Optics** (2024-07). DOI: **10.1117/1.jbo.29.s2.s22711**. https://doi.org/10.1117/1.jbo.29.s2.s22711 (hanninen2024vibrationalimagingof pages 3-4)



References

1. (mungall2010integratingphenotypeontologies pages 2-3): Christopher J Mungall, Georgios V Gkoutos, Cynthia L Smith, Melissa A Haendel, Suzanna E Lewis, and Michael Ashburner. Integrating phenotype ontologies across multiple species. Genome Biology, 11:R2-R2, Jan 2010. URL: https://doi.org/10.1186/gb-2010-11-1-r2, doi:10.1186/gb-2010-11-1-r2. This article has 334 citations and is from a highest quality peer-reviewed journal.

2. (mungall2010integratingphenotypeontologies pages 5-6): Christopher J Mungall, Georgios V Gkoutos, Cynthia L Smith, Melissa A Haendel, Suzanna E Lewis, and Michael Ashburner. Integrating phenotype ontologies across multiple species. Genome Biology, 11:R2-R2, Jan 2010. URL: https://doi.org/10.1186/gb-2010-11-1-r2, doi:10.1186/gb-2010-11-1-r2. This article has 334 citations and is from a highest quality peer-reviewed journal.

3. (schofield2010phenotypeontologiesfor pages 1-2): Paul N. Schofield, Georgios V. Gkoutos, Michael Gruenberger, John P. Sundberg, and John M. Hancock. Phenotype ontologies for mouse and man: bridging the semantic gap. Disease Models & Mechanisms, 3:281-289, May 2010. URL: https://doi.org/10.1242/dmm.002790, doi:10.1242/dmm.002790. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (hu2023advancesindropletbased pages 1-2): Shunyang Hu, Bangxu Wang, Qing Luo, Rumei Zeng, Jiamin Zhang, and Jie Cheng. Advances in droplet-based microfluidic high-throughput screening of engineered strains and enzymes based on ultraviolet, visible, and fluorescent spectroscopy. Fermentation, 10:33, Dec 2023. URL: https://doi.org/10.3390/fermentation10010033, doi:10.3390/fermentation10010033. This article has 17 citations.

5. (zhou2023computervisionmeets pages 1-2): Shizheng Zhou, Bingbing Chen, Edgar S. Fu, and Hong Yan. Computer vision meets microfluidics: a label-free method for high-throughput cell analysis. Microsystems & Nanoengineering, Sep 2023. URL: https://doi.org/10.1038/s41378-023-00562-8, doi:10.1038/s41378-023-00562-8. This article has 71 citations and is from a domain leading peer-reviewed journal.

6. (blazanin2024gcplyranr pages 2-5): Michael Blazanin. Gcplyr: an r package for microbial growth curve data analysis. BMC Bioinformatics, Jul 2024. URL: https://doi.org/10.1186/s12859-024-05817-3, doi:10.1186/s12859-024-05817-3. This article has 76 citations and is from a peer-reviewed journal.

7. (zhao2024highthroughputscreeningcarbon pages 1-2): Heng Zhao, Xiao Ju, Yong Nie, Timothy Y. James, and Xiao-Yong Liu. High-throughput screening carbon and nitrogen sources to promote growth and sporulation in rhizopus arrhizus. AMB Express, Jun 2024. URL: https://doi.org/10.1186/s13568-024-01733-0, doi:10.1186/s13568-024-01733-0. This article has 5 citations and is from a peer-reviewed journal.

8. (hanninen2024vibrationalimagingof pages 3-4): Adam Hanninen. Vibrational imaging of metabolites for improved microbial cell strains. Journal of Biomedical Optics, Jul 2024. URL: https://doi.org/10.1117/1.jbo.29.s2.s22711, doi:10.1117/1.jbo.29.s2.s22711. This article has 3 citations and is from a domain leading peer-reviewed journal.

9. (caufield2023kghub—buildingandexchanging pages 1-3): J Harry Caufield, Tim Putman, Kevin Schaper, Deepak R Unni, Harshad Hegde, Tiffany J Callahan, Luca Cappelletti, Sierra A T Moxon, Vida Ravanmehr, Seth Carbon, Lauren E Chan, Katherina Cortes, Kent A Shefchek, Glass Elsarboukh, Jim Balhoff, Tommaso Fontana, Nicolas Matentzoglu, Richard M Bruskiewich, Anne E Thessen, Nomi L Harris, Monica C Munoz-Torres, Melissa A Haendel, Peter N Robinson, Marcin P Joachimiak, Christopher J Mungall, and Justin T Reese. Kg-hub—building and exchanging biological knowledge graphs. Bioinformatics, Jun 2023. URL: https://doi.org/10.1093/bioinformatics/btad418, doi:10.1093/bioinformatics/btad418. This article has 48 citations and is from a highest quality peer-reviewed journal.

10. (putman2024themonarchinitiative pages 1-2): Tim E Putman, Kevin Schaper, Nicolas Matentzoglu, Vincent P Rubinetti, Faisal S Alquaddoomi, Corey Cox, J Harry Caufield, Glass Elsarboukh, Sarah Gehrke, Harshad Hegde, Justin T Reese, Ian Braun, Richard M Bruskiewich, Luca Cappelletti, Seth Carbon, Anita R Caron, Lauren E Chan, Christopher G Chute, Katherina G Cortes, Vinícius De Souza, Tommaso Fontana, Nomi L Harris, Emily L Hartley, Eric Hurwitz, Julius O B Jacobsen, Madan Krishnamurthy, Bryan J Laraway, James A McLaughlin, Julie A McMurry, Sierra A T Moxon, Kathleen R Mullen, Shawn T O’Neil, Kent A Shefchek, Ray Stefancsik, Sabrina Toro, Nicole A Vasilevsky, Ramona L Walls, Patricia L Whetzel, David Osumi-Sutherland, Damian Smedley, Peter N Robinson, Christopher J Mungall, Melissa A Haendel, and Monica C Munoz-Torres. The monarch initiative in 2024: an analytic platform integrating phenotypes, genes and diseases across species. Nucleic Acids Research, 52:D938-D949, Nov 2024. URL: https://doi.org/10.1093/nar/gkad1082, doi:10.1093/nar/gkad1082. This article has 124 citations and is from a highest quality peer-reviewed journal.

11. (callahan2024anopensource pages 6-7): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 80 citations and is from a peer-reviewed journal.

12. (callahan2024anopensource pages 1-2): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 80 citations and is from a peer-reviewed journal.

13. (santangelo2024integratingbiologicalknowledge pages 11-12): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

14. (hirose2024agenomescalemetabolic pages 1-2): Yujiro Hirose, Daniel C. Zielinski, Saugat Poudel, Kevin Rychel, Jonathon L. Baker, Yoshihiro Toya, Masaya Yamaguchi, Almut Heinken, Ines Thiele, Shigetada Kawabata, Bernhard O. Palsson, and Victor Nizet. A genome-scale metabolic model of a globally disseminated hyperinvasive m1 strain of <i>streptococcus pyogenes</i>. mSystems, Sep 2024. URL: https://doi.org/10.1128/msystems.00736-24, doi:10.1128/msystems.00736-24. This article has 11 citations and is from a peer-reviewed journal.

15. (leonidou2024genomescalemodelof pages 1-2): Nantia Leonidou, Lisa Ostyn, Tom Coenye, Aurélie Crabbé, and Andreas Dräger. Genome-scale model of <i>rothia mucilaginosa</i> predicts gene essentialities and reveals metabolic capabilities. Microbiology Spectrum, Jun 2024. URL: https://doi.org/10.1128/spectrum.04006-23, doi:10.1128/spectrum.04006-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (casey2024transporterannotationsare pages 1-2): John Casey, Brian Bennion, Patrik D’haeseleer, Jeffrey Kimbrel, Gianna Marschmann, and Ali Navid. Transporter annotations are holding up progress in metabolic modeling. Frontiers in Systems Biology, Jul 2024. URL: https://doi.org/10.3389/fsysb.2024.1394084, doi:10.3389/fsysb.2024.1394084. This article has 12 citations.

17. (casey2024transporterannotationsare media 395fe32b): John Casey, Brian Bennion, Patrik D’haeseleer, Jeffrey Kimbrel, Gianna Marschmann, and Ali Navid. Transporter annotations are holding up progress in metabolic modeling. Frontiers in Systems Biology, Jul 2024. URL: https://doi.org/10.3389/fsysb.2024.1394084, doi:10.3389/fsysb.2024.1394084. This article has 12 citations.

18. (callahan2024anopensource pages 2-4): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 80 citations and is from a peer-reviewed journal.

19. (hu2023advancesindropletbased pages 9-10): Shunyang Hu, Bangxu Wang, Qing Luo, Rumei Zeng, Jiamin Zhang, and Jie Cheng. Advances in droplet-based microfluidic high-throughput screening of engineered strains and enzymes based on ultraviolet, visible, and fluorescent spectroscopy. Fermentation, 10:33, Dec 2023. URL: https://doi.org/10.3390/fermentation10010033, doi:10.3390/fermentation10010033. This article has 17 citations.

20. (hu2023advancesindropletbased pages 12-13): Shunyang Hu, Bangxu Wang, Qing Luo, Rumei Zeng, Jiamin Zhang, and Jie Cheng. Advances in droplet-based microfluidic high-throughput screening of engineered strains and enzymes based on ultraviolet, visible, and fluorescent spectroscopy. Fermentation, 10:33, Dec 2023. URL: https://doi.org/10.3390/fermentation10010033, doi:10.3390/fermentation10010033. This article has 17 citations.

21. (ma2024metagenomickgaknowledge pages 4-5): Chunyu Ma, Shaopeng Liu, and David Koslicki. Metagenomickg: a knowledge graph for metagenomic applications. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.14.585056, doi:10.1101/2024.03.14.585056. This article has 6 citations.