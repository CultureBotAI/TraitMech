---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:44:37.019429'
end_time: '2026-06-18T13:01:01.150587'
duration_seconds: 984.13
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biological process
  trait_identifier: METPO:1000630
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: biological_process
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A execution of a genetically-encoded biological module or program. It
    consists of all the steps required to achieve the specific biological objective
    of the module. A biological process is accomplished by a particular set of molecular
    functions carried out by specific gene products (or macromolecular complexes),
    often in a highly regulated manner and in a particular temporal sequence.
  parent_traits: ''
  synonyms: ''
  evidence_summary: 'DOI:10.1093/database/bat054: gene product can be associated to
    a GO term (Supports biological process as a Gene Ontology aspect used for annotating
    gene-product roles.) | DOI:10.1093/database/bat054: biological process, molecular
    function, or cellular component (Supports biological process as one of the core
    GO annotation aspects.)'
  causal_graph_summary: 'biological_process_go_upper_context: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biological process
- **METPO identifier:** METPO:1000630
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/database/bat054: gene product can be associated to a GO term (Supports biological process as a Gene Ontology aspect used for annotating gene-product roles.) | DOI:10.1093/database/bat054: biological process, molecular function, or cellular component (Supports biological process as one of the core GO annotation aspects.)
- **Existing causal graph summary:** biological_process_go_upper_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **biological process** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/biological_process.yaml`.

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
- **Trait label:** biological process
- **METPO identifier:** METPO:1000630
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/database/bat054: gene product can be associated to a GO term (Supports biological process as a Gene Ontology aspect used for annotating gene-product roles.) | DOI:10.1093/database/bat054: biological process, molecular function, or cellular component (Supports biological process as one of the core GO annotation aspects.)
- **Existing causal graph summary:** biological_process_go_upper_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **biological process** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/biological_process.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **biological process** (METPO:1000630)

### Scope summary (curation-oriented)
The METPO upper trait **biological process** (METPO:1000630) is best grounded to the Gene Ontology (GO) *Biological Process* aspect (BP): a coordinated, multi-step biological “program”/module that proteins contribute to, distinct from **molecular function** (MF; the activity of a single gene product) and **cellular component** (CC; where activities occur). BP differs from MF in that BP generally requires multiple stages and a defined beginning/end, while MF is an “elementary molecular activity” of a gene product. In practice for microbial trait curation, “biological process” should be treated as an **upper context** under which **specific processes** (e.g., glycolysis, nitrogen fixation, biofilm formation) are represented as **causal graphs** linking gene products → molecular activities → pathway steps/subprocesses → higher-level biological process outcomes, with explicit cellular localization and chemical inputs/outputs where possible. (podkolodnyy2025ontologiesinmodelling pages 3-4, kulmanov2024proteinfunctionprediction pages 1-2)

**Boundary cases / nearby traits**:
- **Not a phenotype measurement**: BP is not itself an assay readout (e.g., growth rate, MIC); those are phenotype traits that may be *evidence* for a BP, but are not equivalent. BP is a mechanistic/functional category. (reiser2024thearabidopsisinformation pages 1-2, prakash2023semanticrepresentationof pages 1-3)
- **Not “molecular function”**: MF nodes encode specific activities (e.g., isomerase activity) that *compose* a BP via **part_of** and can be causally linked to one another in GO-CAM. (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof pages 4-5)
- **Not “cellular component”**: CC nodes provide spatial context (where an activity/process occurs). (kulmanov2024proteinfunctionprediction pages 1-2, reiser2024thearabidopsisinformation pages 1-2)

### Key concepts and definitions (current understanding)
**GO’s three-aspect model**: GO organizes gene/gene product descriptions into three independent aspects: BP, MF, and CC. (mandal2024integrationofadverse pages 1-4)

**BP vs MF vs CC in current usage**:
- BP: processes to which proteins can contribute (multi-gene, system-level). (kulmanov2024proteinfunctionprediction pages 1-2)
- MF: functions/activities of a single protein, often more directly inferable from sequence/structure than BP. (kulmanov2024proteinfunctionprediction pages 1-2)
- CC: locations where proteins are active. (kulmanov2024proteinfunctionprediction pages 1-2)

**GO-CAM (Gene Ontology Causal Activity Modeling)**: GO-CAM extends single GO annotations into structured causal models of biological processes by **causally linking molecular functions** (activities) and relating them to processes and locations using Relations Ontology (RO) / BFO relations and evidence (ECO). (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof pages 4-5)

A key modeling convention is that **MF↔BP** is commonly modeled via **part_of**, while **MF↔MF** is commonly modeled via causal relations (e.g., *causally upstream of or within*). (prakash2023semanticrepresentationof pages 4-5)

**Representative GO-CAM relations and example**: Box 1 / Figure example in Prakash et al. shows relations such as *has input*, *has output*, *occurs in*, and *enabled by*, and illustrates an MF activity asserted to occur in a CC and enabled by a gene product. (prakash2023semanticrepresentationof media 2c5336ec)

### Recent developments and latest research (prioritize 2023–2024)
#### 1) GO as a formal axiomatic system enabling reasoning and ML
GO is described as a formal axiomatic theory (with >100,000 axioms) spanning the three subontologies and supporting prediction/reasoning tasks. (kulmanov2024proteinfunctionprediction pages 1-2)

#### 2) GO-CAM as an operational framework for causal knowledge graphs
Recent work demonstrates how GO-CAM can represent author statements as semantic triples and assemble them into causal models (knowledge graphs) of biological processes, explicitly specifying relations such as *RO:0002418 causally upstream of or within* and *BFO:0000066 occurs in*. (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof pages 1-3, prakash2023semanticrepresentationof media 2c5336ec)

#### 3) Microbial pathway knowledgebases and their modernization
Multiple 2023–2024 resources show practical, large-scale microbial implementations that can be leveraged for TraitMech curation:
- **IMG/M v7 (2023)**: recomputes **MetaCyc v24.5** pathways using EC numbers derived from KO terms, and states an intent to update reference databases annually (resource permitting). (chen2023theimgmdata pages 1-2)
- **CyanoCyc (2024)**: a cyanobacterial portal within BioCyc, integrating 277 cyanobacterial genomes and extensive manual curation + computational inferences (predicted pathways/operons/complexes/orthologs) with imported UniProt GO annotations. (moore2024cyanocyccyanobacterialweb pages 1-2, moore2024cyanocyccyanobacterialweb pages 2-3)
- **Enteropathway (2024)**: a gut-microbiota metabolic pathway database integrating compounds/reactions/modules from manual literature curation and cross-referencing MetaCyc/KEGG/UniProt, including enrichment analysis and REST API support. (shiroma2024enteropathwaythemetabolic pages 1-2, shiroma2024enteropathwaythemetabolic pages 2-4)

### Current applications and real-world implementations
#### GO/GO-CAM-based causal graphs
GO-CAM is explicitly framed as arranging GO annotations into **structured causal models** of biological processes by causally linking molecular functions, using semantic triples and RO/BFO relations. (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec)

#### Microbial functional inference pipelines (KO→EC→MetaCyc)
IMG/M operationalizes pathway inference by mapping KO annotations to EC numbers and recomputing MetaCyc pathways at large scale, enabling process-capability assignment across isolate genomes and (partially) metagenomes. (chen2023theimgmdata pages 1-2)

#### Knowledge portals for curated microbial processes
CyanoCyc demonstrates an applied knowledgebase that supports microbial process understanding through pathway browsers, comparative genomics, and omics visualization/enrichment on pathways/network diagrams. (moore2024cyanocyccyanobacterialweb pages 7-10, moore2024cyanocyccyanobacterialweb pages 1-2)

#### Microbiome-specific pathway modules and enrichment workflows
Enteropathway provides an end-to-end implementation: curated modules plus enrichment analysis using hypergeometric tests to identify significant modules from KO or reaction lists, and interactive diagram highlighting. (shiroma2024enteropathwaythemetabolic pages 2-4)

### Expert opinions and analysis (authoritative sources)
- A microbiome-focused review argues that mechanistic knowledge bases represent biological processes causally and are rooted in human curation, while also cataloging integration challenges (nomenclature inconsistencies; ontology rooting; structure/access limiting applications). This supports a curation strategy emphasizing explicit ontology grounding and clear provenance. (santangelo2024integratingbiologicalknowledge pages 6-7)
- GO-CAM-focused work emphasizes the need for extensions across ontologies (GO/ECO/ECTO) to faithfully represent experimental statements and notes limitations (e.g., representing negative results). This flags areas where TraitMech curation should be cautious. (prakash2023semanticrepresentationof pages 21-22)

### Relevant statistics and recent quantitative data (2023–2024 priority)
**GO/annotation scale**:
- GO described as having **>100,000 axioms**. (Kulmanov et al., 2024) (kulmanov2024proteinfunctionprediction pages 1-2)
- UniProtKB/Swiss-Prot contains manually curated GO annotations for **>550,000 proteins** (as reported in the same 2024 source). (kulmanov2024proteinfunctionprediction pages 1-2)

**Species/knowledgebase coverage examples**:
- TAIR reports **74%** of the Arabidopsis proteome annotated to ≥1 GO term (Oct 2023), and of annotated loci, **~50%** have experimental support for ≥1 of MF/BP/CC. (Reiser et al., 2024) (reiser2024thearabidopsisinformation pages 1-2)

**Microbial platforms and pathway resources**:
- IMG/M (as of 8/2022): **34,196 metagenomes**, **197,851 metagenome bins**, **8,499 metatranscriptomes**; MetaCyc pathways recomputed using KO-derived EC numbers; annual reference updates planned (resource dependent). (Chen et al., 2023) (chen2023theimgmdata pages 1-2)
- CyanoCyc: **277 cyanobacterial genomes** across **56 genera**; manual curation integrating **>1,765 publications**; five manually curated PGDBs have ~**191–256 pathways** each and associated counts of genes and cited publications. (Moore et al., 2024) (moore2024cyanocyccyanobacterialweb pages 1-2, moore2024cyanocyccyanobacterialweb pages 2-3)
- Enteropathway: **3,269 compounds**, **3,677 reactions**, **876 modules** curated from **1,012 papers**; **698 modules** reported as unique (not found in other databases in their comparison), and **687/876 modules** include host/diet/disease descriptions. (Shiroma et al., 2024) (shiroma2024enteropathwaythemetabolic pages 1-2, shiroma2024enteropathwaythemetabolic pages 2-4)

## Candidate mechanistic nodes (grouped, grounded when possible)
The following node inventory is designed for curation into `data/traits/upper/biological_process.yaml` and for building downstream, trait-specific graphs (e.g., glycolysis, nitrogen fixation, sulfur respiration).

| Node type | Label | Suggested CURIE/ID | Rationale/role in causal graph | Primary supporting citation IDs |
|---|---|---|---|---|
| GO aspect | biological process | GO aspect: BP; target trait: METPO:1000630 | Upper-level process node representing a multistep biological program to which gene products contribute; central scope for this TraitMech graph. | (kulmanov2024proteinfunctionprediction pages 1-2, reiser2024thearabidopsisinformation pages 1-2) |
| GO aspect | molecular function | GO aspect: MF | Activity-level node type used to decompose a biological process into causally linked gene-product activities in GO-CAM. | (kulmanov2024proteinfunctionprediction pages 1-2, prakash2023semanticrepresentationof pages 3-4) |
| GO aspect | cellular component | GO aspect: CC | Localization/context node type capturing where an activity or subprocess occurs. | (kulmanov2024proteinfunctionprediction pages 1-2, reiser2024thearabidopsisinformation pages 1-2) |
| GO-CAM model entity | GO-CAM / Gene Ontology Causal Activity Model | GO-CAM | Core modeling framework for representing biological processes as causal graphs linking molecular functions, processes, locations, inputs, and outputs. | (prakash2023semanticrepresentationof pages 3-4, mandal2024integrationofadverse pages 1-4) |
| Example biological process | canonical glycolysis | GO:0061621 | Example BP node explicitly used in GO-CAM-style triples; suitable template for microbial process curation. | (prakash2023semanticrepresentationof pages 3-4) |
| Example molecular function | glucose-6-phosphate isomerase activity | GO:0004374 | Example MF node shown as part_of canonical glycolysis in GO-CAM examples; useful prototype for process-enabling activities. | (prakash2023semanticrepresentationof pages 3-4) |
| Example cellular component | cytosol | GO:0005829 | Example CC node used to contextualize where a molecular function occurs. | (prakash2023semanticrepresentationof pages 3-4) |
| GO-CAM relation | part of | BFO/RO relation; commonly rendered part_of | Links an MF to the BP it realizes, or links subprocesses to larger processes. | (prakash2023semanticrepresentationof pages 4-5, prakash2023semanticrepresentationof media 2c5336ec) |
| GO-CAM relation | causally upstream of or within | RO:0002418 | Generic causal-flow relation connecting activities/processes when exact subtype is not asserted. | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) |
| GO-CAM relation | has input | RO:0002233 | Connects an activity/process to required input chemicals or entities. | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) |
| GO-CAM relation | has output | RO:0002234 | Connects an activity/process to produced output chemicals or entities. | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) |
| GO-CAM relation | occurs in | BFO:0000066 | Places a molecular activity or subprocess in a cellular component or other location. | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) |
| GO-CAM relation | enabled by | RO:0002333 | Connects a molecular function to its gene product/protein catalyst; essential for mechanistic gene-to-process edges. | (prakash2023semanticrepresentationof media 2c5336ec) |
| Chemical/ontology | ChEBI | CHEBI | Preferred stable ontology for chemicals, metabolites, ligands, inputs, outputs, and cofactors in causal graphs. | (prakash2023semanticrepresentationof pages 4-5, chen2023theimgmdata pages 1-2) |
| Evidence/ontology | Evidence & Conclusion Ontology | ECO | Evidence typing node/ontology for attaching support to assertions and edge provenance. | (prakash2023semanticrepresentationof pages 4-5) |
| Environmental factor placeholder | Environment Ontology | ENVO | Candidate source of environment/habitat/exposure context nodes for microbial process graphs when supported by trait-specific evidence. | (santangelo2024integratingbiologicalknowledge pages 6-7) |
| Experimental factor placeholder | Environmental Conditions, Treatments & Exposures Ontology | ECTO | Candidate source of exposure/condition nodes for representing assay or treatment context in GO-CAM-like statements. | (prakash2023semanticrepresentationof pages 21-22) |
| Pathway/module resource | MetaCyc pathway | MetaCyc | Widely used curated pathway reference for microbial pathway inference and process grounding across platforms. | (chen2023theimgmdata pages 1-2, shiroma2024enteropathwaythemetabolic pages 1-2) |
| Pathway/module resource | KEGG module | KEGG Module | Compact functional-module representation useful for mapping genome content to biological-process capability. | (shiroma2024enteropathwaythemetabolic pages 2-4, shiroma2024enteropathwaythemetabolic pages 1-2) |
| Pathway/module resource | Enteropathway module | Enteropathway module | Gut-microbiota-focused curated module unit integrating reactions, compounds, and host/diet/disease context. | (shiroma2024enteropathwaythemetabolic pages 2-4, shiroma2024enteropathwaythemetabolic pages 1-2) |
| Data platform | IMG/M | IMG/M | Large-scale microbial genome/metagenome platform that recomputes MetaCyc pathways from KO→EC mappings; relevant implementation target for process inference. | (chen2023theimgmdata pages 1-2) |
| Data platform | CyanoCyc | CyanoCyc | Cyanobacterial pathway/genome portal with predicted pathways, operons, complexes, GO imports, and manual curation; demonstrates microbial process knowledgebase implementation. | (moore2024cyanocyccyanobacterialweb pages 2-3, moore2024cyanocyccyanobacterialweb pages 1-2) |
| Data platform | KBase | KBase | Systems-biology platform integrating MetaCyc/KEGG/BiGG-style metabolic knowledge for microbial metabolic modeling and mechanistic inference. | (santangelo2024integratingbiologicalknowledge pages 6-7) |
| Data platform | Virtual Metabolic Human | VMH | Cross-resource metabolic knowledgebase linking microbial and host metabolism; useful for microbe-host process context. | (santangelo2024integratingbiologicalknowledge pages 6-7) |
| Gene product entity | gene product / protein | UniProtKB protein; generic node class | Mechanistic entity that enables molecular function and links gene content to process execution. | (mandal2024integrationofadverse pages 1-4, prakash2023semanticrepresentationof media 2c5336ec) |
| Complex/entity type | protein complex | BioCyc/CyanoCyc complex; label-only candidate if ungrounded | Relevant intermediate node for activities executed by macromolecular complexes rather than single proteins. | (moore2024cyanocyccyanobacterialweb pages 1-2) |
| Process context | pathway step-enabling entity | label-only candidate | Useful abstraction for grouping alternative genes/proteins that can realize the same pathway step in enrichment or causal models. | (prakash2023semanticrepresentationof pages 3-4) |
| Location/context | cellular localization context | GO CC term (trait-specific) | General placeholder for subcellular localization nodes beyond cytosol, depending on curated microbial process. | (kulmanov2024proteinfunctionprediction pages 1-2, prakash2023semanticrepresentationof pages 4-5) |


*Table: This table lists curation-ready node candidates for a microbial causal graph centered on the upper trait 'biological process'. It covers GO/GO-CAM core entities, example grounded nodes, pathway resources, platforms, and supporting context ontologies needed to build evidence-backed mechanistic graphs.*

## Candidate evidence-backed causal edges (triples)
The following edges include (a) GO/GO-CAM schema edges appropriate for an **upper** trait graph and (b) implementation/provenance edges documenting how microbial platforms operationalize process inference and pathway knowledgebases. Where an edge is more pipeline/provenance than biology, it is flagged.

| Edge (subject–predicate–object) | Suggested grounding for nodes/relation | Evidence snippet / quote | Source (DOI + URL + pub date) | Citation ID(s) | Notes including uncertainty / taxon-specificity |
|---|---|---|---|---|---|
| Gene Ontology — has_aspect — biological process | subject: GO; predicate: label-only `has_aspect`; object: GO aspect `BP` / target trait `METPO:1000630` | “GO organizes gene/product descriptions into three independent aspects: biological process (BP), molecular function (MF), and cellular component (CC).” | Mandal et al. 2024. DOI:10.7921/76ke-by69. https://doi.org/10.7921/76ke-by69. 2024 | (mandal2024integrationofadverse pages 1-4) | High-level ontology-organizational edge; useful as upper-context only, not organism-mechanistic. |
| Gene Ontology — has_aspect — molecular function | subject: GO; predicate: label-only `has_aspect`; object: GO aspect `MF` | “GO organizes gene/product descriptions into three independent aspects...” | Mandal et al. 2024. DOI:10.7921/76ke-by69. https://doi.org/10.7921/76ke-by69. 2024 | (mandal2024integrationofadverse pages 1-4) | Same as above; organizational/context edge, not microbe-specific mechanism. |
| Gene Ontology — has_aspect — cellular component | subject: GO; predicate: label-only `has_aspect`; object: GO aspect `CC` | “GO organizes gene/product descriptions into three independent aspects...” | Mandal et al. 2024. DOI:10.7921/76ke-by69. https://doi.org/10.7921/76ke-by69. 2024 | (mandal2024integrationofadverse pages 1-4) | Same as above; upper ontology context. |
| glucose-6-phosphate isomerase activity — part_of — canonical glycolysis | subject: GO:0004374; predicate: BFO/RO `part_of`; object: GO:0061621 | “[glucose-6-phosphate isomerase activity (GO:0004374)] part of [canonical glycolysis (GO:0061621)]” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof pages 3-4) | Strong template edge showing how MF activities compose a BP. Example is general, not specifically microbial, but directly transferable to microbial GO-CAM curation. |
| molecular function — part_of — biological process | subject: GO aspect `MF`; predicate: BFO/RO `part_of`; object: GO aspect `BP` | “a GO Molecular Function and a GO Biological Process (BP) are linked by mereological (part_of) relations” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof pages 4-5) | High-level GO-CAM modeling rule; curatable as schema guidance rather than biological assertion. |
| molecular function — causally_upstream_of_or_within — molecular function | subject: GO MF term; predicate: RO:0002418; object: GO MF term | “GO–CAMs arrange GO annotations into structured models of biological processes by causally linking GO Molecular Functions” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) | Strong GO-CAM relation template. Exact upstream/downstream MF pair must be trait-specific before final curation. |
| molecular activity — occurs_in — cellular component | subject: GO MF term / activity; predicate: BFO:0000066; object: GO CC term | “Occurs in [BFO: 0000066]” and example “glucokinase activity occurs in cytosol” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof media 2c5336ec) | Strong schema/example edge for localization of activities. Trait-specific CC term still needed for microbial curation. |
| molecular activity — has_input — chemical entity | subject: GO MF term / activity; predicate: RO:0002233; object: CHEBI term | “Has input [RO:0002233]” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) | Strong relation template; actual input chemical should be trait-specific and grounded to ChEBI. |
| molecular activity — has_output — chemical entity | subject: GO MF term / activity; predicate: RO:0002234; object: CHEBI term | “Has output [RO:0002234]” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof media 2c5336ec) | Strong relation template; actual output chemical should be trait-specific and grounded to ChEBI. |
| molecular function — enabled_by — gene product | subject: GO MF term; predicate: RO:0002333; object: gene product / protein | Figure example: “glucokinase activity enabled by Hxk1” | Prakash et al. 2023. DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5. Nov 2023 | (prakash2023semanticrepresentationof media 2c5336ec) | Essential mechanistic edge for TraitMech graphs. Example gene is not microbial; use as modeling precedent. |
| KO annotation — mapped_to — EC number | subject: KEGG Orthology term; predicate: label-only `mapped_to`; object: EC number | “MetaCyc v24.5 pathways are recomputed using the new Enzyme Commission (EC) numbers derived from KO terms” | Chen et al. 2023. DOI:10.1093/nar/gkac976. https://doi.org/10.1093/nar/gkac976. Nov 2023 | (chen2023theimgmdata pages 1-2) | Operational inference edge in IMG/M pipeline; not a biological mechanism per se, but highly relevant to process-capability assignment. |
| EC number — used_to_recompute — MetaCyc pathway | subject: EC number; predicate: label-only `used_to_recompute`; object: MetaCyc pathway | “MetaCyc v24.5 pathways are recomputed using the new Enzyme Commission (EC) numbers...” | Chen et al. 2023. DOI:10.1093/nar/gkac976. https://doi.org/10.1093/nar/gkac976. Nov 2023 | (chen2023theimgmdata pages 1-2) | Database-pipeline edge documenting pathway inference. Appropriate for provenance layer; uncertain as direct causal biology edge. |
| IMG/M isolate genome annotation set — refreshes_annotation_for — Pfam/KO/EC annotations | subject: IMG/M; predicate: label-only `refreshes_annotation_for`; object: Pfam/KO/EC annotations | “Pfam, KO and EC annotations were refreshed for all isolate genomes in IMG” | Chen et al. 2023. DOI:10.1093/nar/gkac976. https://doi.org/10.1093/nar/gkac976. Nov 2023 | (chen2023theimgmdata pages 1-2) | Implementation/provenance edge; useful for confidence in inferred biological-process capability. |
| CyanoCyc genome database — imports — UniProt GO annotations | subject: CyanoCyc; predicate: label-only `imports`; object: UniProt GO terms | “UniProtKB data (protein features, GO annotations, accessions) were imported.” | Moore et al. 2024. DOI:10.3389/fmicb.2024.1340413. https://doi.org/10.3389/fmicb.2024.1340413. Jan 2024 | (moore2024cyanocyccyanobacterialweb pages 2-3) | Strong knowledgebase integration edge; not direct biology but supports node grounding and propagation of process annotations. |
| CyanoCyc genome database — predicts — metabolic pathway | subject: CyanoCyc; predicate: label-only `predicts`; object: MetaCyc/BioCyc pathway | “computational inferences including predicted metabolic pathways, operons, protein complexes, and orthologs” | Moore et al. 2024. DOI:10.3389/fmicb.2024.1340413. https://doi.org/10.3389/fmicb.2024.1340413. Jan 2024 | (moore2024cyanocyccyanobacterialweb pages 1-2) | Strong microbial implementation edge; pathway predictions are inferred, so curate as uncertain/provenance unless manually validated. |
| CyanoCyc genome database — predicts — operon | subject: CyanoCyc; predicate: label-only `predicts`; object: operon | “predicted metabolic pathways, operons, protein complexes, and orthologs” | Moore et al. 2024. DOI:10.3389/fmicb.2024.1340413. https://doi.org/10.3389/fmicb.2024.1340413. Jan 2024 | (moore2024cyanocyccyanobacterialweb pages 1-2) | Useful for linking co-regulated genes to process execution; prediction-based and cyanobacteria-focused. |
| CyanoCyc genome database — predicts — protein complex | subject: CyanoCyc; predicate: label-only `predicts`; object: protein complex | “predicted metabolic pathways, operons, protein complexes, and orthologs” | Moore et al. 2024. DOI:10.3389/fmicb.2024.1340413. https://doi.org/10.3389/fmicb.2024.1340413. Jan 2024 | (moore2024cyanocyccyanobacterialweb pages 1-2) | Useful mechanistic intermediate for process graphs; inference-based and taxon/resource-specific. |
| Enteropathway module — cross_references — MetaCyc pathway | subject: Enteropathway module; predicate: label-only `cross_references`; object: MetaCyc pathway | “manually links Enteropathway modules to KEGG Modules and MetaCyc Pathway” | Shiroma et al. 2024. DOI:10.1093/bib/bbae419. https://doi.org/10.1093/bib/bbae419. Jun 2024 | (shiroma2024enteropathwaythemetabolic pages 2-4) | Strong resource-integration edge; useful for grounding microbiome-specific process modules to established pathway vocabularies. |
| KO list / Enteropathway reaction list — enriched_for — Enteropathway module | subject: KO list or reaction list; predicate: label-only `enriched_for`; object: Enteropathway module | “A built-in enrichment analysis accepts lists of KO or Enteropathway reaction IDs and uses a hypergeometric test to identify and highlight significant modules” | Shiroma et al. 2024. DOI:10.1093/bib/bbae419. https://doi.org/10.1093/bib/bbae419. Jun 2024 | (shiroma2024enteropathwaythemetabolic pages 2-4) | Assay/analysis edge rather than biology. Valuable for mapping observed data to biological-process candidates in microbiome studies. |
| Enteropathway module — annotated_with — host/diet/disease information | subject: Enteropathway module; predicate: label-only `annotated_with`; object: host/diet/disease context | “Of 876 Enteropathway modules, 687 were enriched with host/diet/disease information.” | Shiroma et al. 2024. DOI:10.1093/bib/bbae419. https://doi.org/10.1093/bib/bbae419. Jun 2024 | (shiroma2024enteropathwaythemetabolic pages 2-4, shiroma2024enteropathwaythemetabolic pages 1-2) | Contextual annotation edge; useful for environmental or host-associated process context, not direct mechanism. |
| biological process knowledge graph — rooted_in — curated causal relationships | subject: mechanistic microbiome knowledge base; predicate: label-only `rooted_in`; object: curated causal biological-process relationships | “The relationships represented capture biological processes in a causal way, and are rooted in human curation” | Santangelo et al. 2024. DOI:10.3389/fmicb.2024.1351678. https://doi.org/10.3389/fmicb.2024.1351678. Apr 2024 | (santangelo2024integratingbiologicalknowledge pages 6-7) | Expert-opinion/supporting edge for using curated causal graphs in microbiome mechanism inference; broad, not trait-specific. |


*Table: This table compiles evidence-backed candidate triples for curating the upper microbial trait 'biological process' as a causal graph. It emphasizes GO/GO-CAM schema edges plus microbial pathway-resource implementation edges that can guide what is safe to curate now versus what should remain provenance or inferred context.*

## Warnings / claims not ready for direct TraitMech curation
1. **Pipeline edges vs biological causality**: KO→EC→MetaCyc recomputation in IMG/M and module enrichment tests are critical for *annotation provenance* but do not constitute biological causation; curate these as provenance/derivation edges (or in metadata), not as mechanism edges for microbial physiology. (chen2023theimgmdata pages 1-2, shiroma2024enteropathwaythemetabolic pages 2-4)
2. **Prediction-derived nodes/edges** (e.g., CyanoCyc predicted pathways/operons/complexes): these should be marked **uncertain** unless backed by manual curation or direct experimental evidence for the organism/taxon. (moore2024cyanocyccyanobacterialweb pages 1-2)
3. **Over-general upper-trait graphs**: For METPO:1000630, a safe curation target is a **schema-like** GO-CAM upper context (relations and node types). TraitMech mechanistic graphs require narrowing to a specific BP term (e.g., GO:0061621) and anchoring to microbial gene products, inputs/outputs, and conditions. (prakash2023semanticrepresentationof pages 4-5, prakash2023semanticrepresentationof media 2c5336ec)
4. **Environmental/exposure context**: ENVO/ECTO nodes are appropriate only when sources explicitly link specific environments/exposures to process execution in microbes; current evidence supports the *need* for such ontologies in modeling but does not provide microbe-specific, curatable environment→process edges for METPO:1000630 alone. (prakash2023semanticrepresentationof pages 21-22, santangelo2024integratingbiologicalknowledge pages 6-7)

## DOI-first bibliography (with URLs; publication dates from retrieved records)
- Prakash SJ, Van Auken KM, Hill DP, Sternberg PW. *Semantic representation of neural circuit knowledge in Caenorhabditis elegans.* **Brain Informatics** (Nov 2023). DOI:10.1186/s40708-023-00208-5. https://doi.org/10.1186/s40708-023-00208-5 (prakash2023semanticrepresentationof pages 3-4, prakash2023semanticrepresentationof pages 4-5, prakash2023semanticrepresentationof pages 1-3, prakash2023semanticrepresentationof media 2c5336ec)
- Chen I-MA, Chu K, Palaniappan K, et al. *The IMG/M data management and analysis system v.7: content updates and new features.* **Nucleic Acids Research** (Nov 2023). DOI:10.1093/nar/gkac976. https://doi.org/10.1093/nar/gkac976 (chen2023theimgmdata pages 1-2)
- Moore LR, Caspi R, Campbell DA, et al. *CyanoCyc cyanobacterial web portal.* **Frontiers in Microbiology** (Jan 2024). DOI:10.3389/fmicb.2024.1340413. https://doi.org/10.3389/fmicb.2024.1340413 (moore2024cyanocyccyanobacterialweb pages 1-2, moore2024cyanocyccyanobacterialweb pages 2-3, moore2024cyanocyccyanobacterialweb pages 7-10)
- Kulmanov M, Guzmán-Vega FJ, Roggli PDD, Lane L, Arold ST, Hoehndorf R. *Protein function prediction as approximate semantic entailment.* **Nature Machine Intelligence** (Feb 2024). DOI:10.1038/s42256-024-00795-w. https://doi.org/10.1038/s42256-024-00795-w (kulmanov2024proteinfunctionprediction pages 1-2)
- Reiser L, Bakker E, Subramaniam S, et al. *The Arabidopsis Information Resource in 2024.* **GENETICS** (Mar 2024). DOI:10.1093/genetics/iyae027. https://doi.org/10.1093/genetics/iyae027 (reiser2024thearabidopsisinformation pages 1-2)
- Santangelo BE, Apgar M, Colorado ASB, et al. *Integrating biological knowledge for mechanistic inference in the host-associated microbiome.* **Frontiers in Microbiology** (Apr 2024). DOI:10.3389/fmicb.2024.1351678. https://doi.org/10.3389/fmicb.2024.1351678 (santangelo2024integratingbiologicalknowledge pages 6-7)
- Shiroma H, Darzi Y, Terajima E, et al. *Enteropathway: the metabolic pathway database for the human gut microbiota.* **Briefings in Bioinformatics** (Jun 2024). DOI:10.1093/bib/bbae419. https://doi.org/10.1093/bib/bbae419 (shiroma2024enteropathwaythemetabolic pages 1-2, shiroma2024enteropathwaythemetabolic pages 2-4)
- Mandal M, Ceger P, Fecho K, et al. *Integration of Adverse Outcome Pathway Information into the Biomedical Data Translator.* (2024). DOI:10.7921/76ke-by69. https://doi.org/10.7921/76ke-by69 (mandal2024integrationofadverse pages 1-4)

### Appendix: optional broader background (not 2023–2024)
- Podkolodnyy NL, Podkolodnaya OA, Ivanisenko VA, Marchenko MA. *Ontologies in modelling and analysing of big genetic data.* **Vavilov Journal of Genetics and Breeding** (Jan 2025). DOI:10.18699/vjgb-24-101. https://doi.org/10.18699/vjgb-24-101 (used for explicit BP/MF/CC definitions and GOA scale, but outside requested 2023–2024 priority window) (podkolodnyy2025ontologiesinmodelling pages 3-4)


References

1. (podkolodnyy2025ontologiesinmodelling pages 3-4): N. L. Podkolodnyy, O. A. Podkolodnaya, V. A. Ivanisenko, and M. A. Marchenko. Ontologies in modelling and analysing of big genetic data. Vavilov Journal of Genetics and Breeding, 28:940-949, Jan 2025. URL: https://doi.org/10.18699/vjgb-24-101, doi:10.18699/vjgb-24-101. This article has 2 citations.

2. (kulmanov2024proteinfunctionprediction pages 1-2): Maxat Kulmanov, Francisco J. Guzmán-Vega, Paula Duek Roggli, Lydie Lane, Stefan T. Arold, and Robert Hoehndorf. Protein function prediction as approximate semantic entailment. Nat. Mac. Intell., 6:220-228, Feb 2024. URL: https://doi.org/10.1038/s42256-024-00795-w, doi:10.1038/s42256-024-00795-w. This article has 147 citations.

3. (reiser2024thearabidopsisinformation pages 1-2): Leonore Reiser, Erica Bakker, Sabarinath Subramaniam, Xingguo Chen, Swapnil Sawant, Kartik Khosa, Trilok Prithvi, and Tanya Z Berardini. The arabidopsis information resource in 2024. GENETICS, Mar 2024. URL: https://doi.org/10.1093/genetics/iyae027, doi:10.1093/genetics/iyae027. This article has 147 citations and is from a domain leading peer-reviewed journal.

4. (prakash2023semanticrepresentationof pages 1-3): Sharan J. Prakash, Kimberly M. Van Auken, David P. Hill, and Paul W. Sternberg. Semantic representation of neural circuit knowledge in caenorhabditis elegans. Brain Informatics, Nov 2023. URL: https://doi.org/10.1186/s40708-023-00208-5, doi:10.1186/s40708-023-00208-5. This article has 1 citations.

5. (prakash2023semanticrepresentationof pages 3-4): Sharan J. Prakash, Kimberly M. Van Auken, David P. Hill, and Paul W. Sternberg. Semantic representation of neural circuit knowledge in caenorhabditis elegans. Brain Informatics, Nov 2023. URL: https://doi.org/10.1186/s40708-023-00208-5, doi:10.1186/s40708-023-00208-5. This article has 1 citations.

6. (prakash2023semanticrepresentationof pages 4-5): Sharan J. Prakash, Kimberly M. Van Auken, David P. Hill, and Paul W. Sternberg. Semantic representation of neural circuit knowledge in caenorhabditis elegans. Brain Informatics, Nov 2023. URL: https://doi.org/10.1186/s40708-023-00208-5, doi:10.1186/s40708-023-00208-5. This article has 1 citations.

7. (mandal2024integrationofadverse pages 1-4): Meisha Mandal, Patricia Ceger, Karamarie Fecho, Virginia Hench, Gaurav Vaidya, and James Balhoff. Integration of adverse outcome pathway information into the biomedical data translator. 2024. URL: https://doi.org/10.7921/76ke-by69, doi:10.7921/76ke-by69. This article has 0 citations.

8. (prakash2023semanticrepresentationof media 2c5336ec): Sharan J. Prakash, Kimberly M. Van Auken, David P. Hill, and Paul W. Sternberg. Semantic representation of neural circuit knowledge in caenorhabditis elegans. Brain Informatics, Nov 2023. URL: https://doi.org/10.1186/s40708-023-00208-5, doi:10.1186/s40708-023-00208-5. This article has 1 citations.

9. (chen2023theimgmdata pages 1-2): I-Min A Chen, Ken Chu, Krishnaveni Palaniappan, Anna Ratner, Jinghua Huang, Marcel Huntemann, Patrick Hajek, Stephan J Ritter, Cody Webb, Dongying Wu, Neha J Varghese, T B K Reddy, Supratim Mukherjee, Galina Ovchinnikova, Matt Nolan, Rekha Seshadri, Simon Roux, Axel Visel, Tanja Woyke, Emiley A Eloe-Fadrosh, Nikos C Kyrpides, and Natalia N Ivanova. The img/m data management and analysis system v.7: content updates and new features. Nucleic Acids Research, 51:D723-D732, Nov 2023. URL: https://doi.org/10.1093/nar/gkac976, doi:10.1093/nar/gkac976. This article has 409 citations and is from a highest quality peer-reviewed journal.

10. (moore2024cyanocyccyanobacterialweb pages 1-2): Lisa R. Moore, Ron Caspi, Douglas A. Campbell, John R. Casey, Sophie Crevecoeur, David J. Lea-Smith, Bin Long, Naaman M. Omar, Suzanne M. Paley, Nicolas M. Schmelling, Alejandro Torrado, Jonathan P. Zehr, and Peter D. Karp. Cyanocyc cyanobacterial web portal. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1340413, doi:10.3389/fmicb.2024.1340413. This article has 21 citations and is from a peer-reviewed journal.

11. (moore2024cyanocyccyanobacterialweb pages 2-3): Lisa R. Moore, Ron Caspi, Douglas A. Campbell, John R. Casey, Sophie Crevecoeur, David J. Lea-Smith, Bin Long, Naaman M. Omar, Suzanne M. Paley, Nicolas M. Schmelling, Alejandro Torrado, Jonathan P. Zehr, and Peter D. Karp. Cyanocyc cyanobacterial web portal. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1340413, doi:10.3389/fmicb.2024.1340413. This article has 21 citations and is from a peer-reviewed journal.

12. (shiroma2024enteropathwaythemetabolic pages 1-2): Hirotsugu Shiroma, Youssef Darzi, Etsuko Terajima, Zenichi Nakagawa, Hirotaka Tsuchikura, Naoki Tsukuda, Yuki Moriya, Shujiro Okuda, Susumu Goto, and Takuji Yamada. Enteropathway: the metabolic pathway database for the human gut microbiota. Briefings in Bioinformatics, Jun 2024. URL: https://doi.org/10.1093/bib/bbae419, doi:10.1093/bib/bbae419. This article has 13 citations and is from a domain leading peer-reviewed journal.

13. (shiroma2024enteropathwaythemetabolic pages 2-4): Hirotsugu Shiroma, Youssef Darzi, Etsuko Terajima, Zenichi Nakagawa, Hirotaka Tsuchikura, Naoki Tsukuda, Yuki Moriya, Shujiro Okuda, Susumu Goto, and Takuji Yamada. Enteropathway: the metabolic pathway database for the human gut microbiota. Briefings in Bioinformatics, Jun 2024. URL: https://doi.org/10.1093/bib/bbae419, doi:10.1093/bib/bbae419. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (moore2024cyanocyccyanobacterialweb pages 7-10): Lisa R. Moore, Ron Caspi, Douglas A. Campbell, John R. Casey, Sophie Crevecoeur, David J. Lea-Smith, Bin Long, Naaman M. Omar, Suzanne M. Paley, Nicolas M. Schmelling, Alejandro Torrado, Jonathan P. Zehr, and Peter D. Karp. Cyanocyc cyanobacterial web portal. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1340413, doi:10.3389/fmicb.2024.1340413. This article has 21 citations and is from a peer-reviewed journal.

15. (santangelo2024integratingbiologicalknowledge pages 6-7): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

16. (prakash2023semanticrepresentationof pages 21-22): Sharan J. Prakash, Kimberly M. Van Auken, David P. Hill, and Paul W. Sternberg. Semantic representation of neural circuit knowledge in caenorhabditis elegans. Brain Informatics, Nov 2023. URL: https://doi.org/10.1186/s40708-023-00208-5, doi:10.1186/s40708-023-00208-5. This article has 1 citations.