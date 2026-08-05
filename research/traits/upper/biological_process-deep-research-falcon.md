---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:11:35.027425'
end_time: '2026-08-04T12:19:24.812361'
duration_seconds: 469.79
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'biological_process_go_upper_context: 8 nodes, 9 edges'
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
- **Trait label:** biological process
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000630
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/database/bat054: gene product can be associated to a GO term (Supports biological process as a Gene Ontology aspect used for annotating gene-product roles.) | DOI:10.1093/database/bat054: biological process, molecular function, or cellular component (Supports biological process as one of the core GO annotation aspects.)
- **Existing causal graph summary:** biological_process_go_upper_context: 8 nodes, 9 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000630
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/database/bat054: gene product can be associated to a GO term (Supports biological process as a Gene Ontology aspect used for annotating gene-product roles.) | DOI:10.1093/database/bat054: biological process, molecular function, or cellular component (Supports biological process as one of the core GO annotation aspects.)
- **Existing causal graph summary:** biological_process_go_upper_context: 8 nodes, 9 edges

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


# Curation report: microbial “biological process”

## Executive recommendation

The target trait **“biological process” (`METPO:1000630`)** is an upper-level ontology class, not a directly measurable microbial phenotype. It denotes execution of a genetically encoded, coordinated program whose component molecular activities occur in an organized sequence to achieve a biological objective. GO similarly distinguishes biological process (coordinated program), molecular function (activity of a gene product), and cellular component (where the activity occurs). Therefore, the safest TraitMech graph for this term should remain a small, taxon-neutral **metamodel** connecting gene products, molecular functions, component processes, cellular locations, and biological-process execution. Specific pathways such as motility, denitrification, or sulfur oxidation should be examples or descendants—not defining components of every biological process. (g2026thegeneontology pages 1-2, antonazzo2024representationofnoncoding pages 1-2)

## 1. Scope and boundaries

### In scope

`METPO:1000630` represents an **occurring process**: a coordinated biological program involving one or more gene products and normally multiple steps or activities. Examples in microbes include flagellum assembly, bacterial motility, ammonium assimilation, denitrification, sulfur oxidation, polysaccharide degradation, sporulation, and DNA replication. A process may contain subprocesses and may be represented computationally as a pathway or causal activity model. (g2026thegeneontology pages 1-2, g2026thegeneontology pages 7-9)

### Important boundary cases

- **Molecular function is not biological process.** Catalysis, binding, transport activity, or motor activity describes what a molecular machine does; a process describes the broader objective achieved by coordinated activities. For example, a reductase activity is not itself denitrification. (g2026thegeneontology pages 7-9, antonazzo2024representationofnoncoding pages 1-2)
- **Cellular component is not biological process.** A flagellum, membrane, cytosol, or protein complex is a material/location entity in or at which activities occur. (antonazzo2024representationofnoncoding pages 1-2)
- **Pathway/module is a representation or organized subset of a process.** GO-CAM organizes gene-product activities into causal networks; it does not make every pathway node synonymous with the upper biological-process class. (antonazzo2024representationofnoncoding pages 7-8, g2026thegeneontology pages 5-7)
- **Phenotype is an observed disposition or outcome.** Motility measured in soft agar is a phenotype/assay result; bacterial motility is the underlying process. Likewise, ammonia removal is a system-level outcome that may result from several processes.
- **Genomic potential is not process execution.** Presence of marker genes or a complete predicted module supports capacity, but not expression, flux, substrate turnover, or in situ activity. The biofloc study consistently frames MAG-derived findings as “functional potential” or “genomic potential.” (rajeev2024genomecentricmetagenomicsprovides pages 12-14, rajeev2024genomecentricmetagenomicsprovides pages 9-12, rajeev2024genomecentricmetagenomicsprovides pages 1-2)
- **Regulation is distinct from execution.** A regulator may positively or negatively regulate a process without being a structural or catalytic part of it. GO annotations and GO-CAM can represent these downstream positive and negative effects explicitly. (antonazzo2024representationofnoncoding pages 7-8)

## 2. Candidate nodes grouped by type

### Core upper-level nodes

| Node | Grounding | Curation role |
|---|---|---|
| biological process | `METPO:1000630` — quote verbatim | Target trait. |
| biological process | `GO:0008150` | Cross-ontology grounding candidate for the GO aspect/class. |
| molecular function | `GO:0003674` | Activity performed by a gene product or molecular machine. |
| cellular component | `GO:0005575` | Location or material cellular structure in which an activity occurs. |
| gene product | Label-only upper node | Protein or functional RNA that enables an activity. |
| component biological process | Label-only | Subprocess connected by `part_of`. |
| biological-process execution | Label-only | Optional event node separating capacity from actual occurrence. |
| functional potential | Label-only | Explicitly represents genome-predicted capacity; must not be equated with execution. |

The three cited GO identifiers are established root terms; nevertheless, identifiers for narrower nodes should be resolved against the ontology release used by TraitMech rather than inferred from labels.

### Mechanistic exemplar: flagellum and motility

- Flagellar gene products; preferably use taxon-specific UniProt accessions only when a strain is fixed.
- Flagellar rod, hook, C ring, motor/MS ring, and export complex.
- Flagellum assembly.
- Assembled bacterial flagellum.
- Bacterial motility.
- Proton motive force or sodium motive force, depending on the experimentally established motor type.
- Motility assay result as a separate observation node.

ProkFunFind represented flagellar function using **18 genes/gene families in five categories**—rod, hook, C ring, motor/MS ring, and export complex—and combined HMM, domain, and orthology evidence. The broader core is described as approximately 21 conserved genes, illustrating that a complex process cannot safely be reduced to a single marker. (dufaultthompson2024annotatingmicrobialfunctions pages 4-7, dufaultthompson2024annotatingmicrobialfunctions pages 2-4)

### Metabolic exemplars from biofloc aquaculture

- **Ammonium assimilation module:** `glnA`, `gltB`, `gltD`; GS–GOGAT pathway; ammonia/ammonium; glutamate/glutamine.
- **Denitrification module:** `napAB` or `narGHI`, `nirS`/`nirK`, `norBC`, `nosZ`; nitrate, nitrite, nitric oxide, nitrous oxide, dinitrogen.
- **DNRA module:** `nirBD` or `nrfAH`; nitrate/nitrite and ammonium.
- **Sulfur oxidation module:** `soxXAYZBCD`, especially `soxB`; thiosulfate/sulfide oxidation.
- **Reverse Dsr module:** `rdsrAB`; sulfide-to-sulfite oxidation, only after phylogenetic discrimination from reductive `dsrAB`.
- **Complex-carbohydrate degradation:** CAZymes including GH13, GH43, GH16, GH5 and PL1; polysaccharide substrates and oligosaccharide products.
- **Environmental context:** biofloc microbial aggregate, high carbon-to-nitrogen management, oxygenated bulk water, localized low-oxygen microniches, starch/cellulose inputs, and toxic nitrogen/sulfide burden.
- **Taxa:** Rhodobacteraceae, Flavobacteriaceae, Saprospiraceae, Nitrosomonas, Nitrospirota, Nitrococcus, and Arenicellales. Ground these to `NCBITaxon` only after exact species or accepted taxon concepts are verified.

The 2024 study found 145 MAGs with complete `glnA/gltB/gltD`, 128 MAGs with `nirS/K` denitrification markers, 30 with `nirBD` DNRA markers, 51 MAGs—about 10%—with complete `soxXAYZBCD`, and 7,540 CAZyme genes. Only six MAGs represented recognized nitrifying groups, supporting a conclusion of limited autotrophic nitrification potential in that system. (rajeev2024genomecentricmetagenomicsprovides pages 12-14, rajeev2024genomecentricmetagenomicsprovides pages 9-12, rajeev2024genomecentricmetagenomicsprovides pages 7-9)

### Experimental and evidence nodes

- Genome or metagenome sequence.
- Metagenome-assembled genome.
- Gene/ortholog/domain annotation.
- Transcript or protein abundance.
- Enzyme-activity measurement.
- Metabolite concentration and isotope-tracer flux.
- Process-rate assay.
- Presence/absence prediction.
- Evidence code, taxon, strain, medium, temperature, oxygen condition, substrate, and assay.

These evidence-layer nodes are essential because sequence annotation assigns **putative** functions. ProkFunFind combines sequence, HMM, protein-domain, KEGG Orthology, and COG evidence, while biofloc pathway calls used DRAM annotations across KOfam, UniRef90, Pfam, CAZy, and MEROPS. (dufaultthompson2024annotatingmicrobialfunctions pages 1-2, dufaultthompson2024annotatingmicrobialfunctions pages 4-7, rajeev2024genomecentricmetagenomicsprovides pages 5-7)

## 3. Candidate causal edges

The most reusable subset is summarized below.

| Subject | Predicate | Object | Evidence status | Curation note |
|---|---|---|---|---|
| gene product | enables | molecular function | direct ontology claim (g2026thegeneontology pages 1-2, antonazzo2024representationofnoncoding pages 1-2) | Safe upper-level edge for METPO:1000630 context; keep generic unless a specific gene product and GO molecular function are source-backed. |
| molecular function | causally upstream of or part of | biological process | direct ontology claim (antonazzo2024representationofnoncoding pages 7-8, g2026thegeneontology pages 5-7) | Appropriate as a GO/GO-CAM organizing edge; reflects causal organization of activities into processes. |
| component biological process | part_of | biological process | direct ontology claim (g2026thegeneontology pages 1-2, g2026thegeneontology pages 7-9) | Safe compositional edge for upper-level process graphs; do not over-specify named subprocesses without narrower-trait evidence. |
| flagellar genes / flagellar gene products | enable | flagellum assembly | mechanism-supported, but example-derived and taxon-patterned (dufaultthompson2024annotatingmicrobialfunctions pages 1-2, dufaultthompson2024annotatingmicrobialfunctions pages 2-4, dufaultthompson2024annotatingmicrobialfunctions pages 7-9) | Useful exemplar edge; curate as a lower-level microbial-process example rather than as defining edge for all biological processes. |
| assembled flagellum | enables | bacterial motility | mechanism-supported, but example-derived (dufaultthompson2024annotatingmicrobialfunctions pages 4-7, dufaultthompson2024annotatingmicrobialfunctions pages 7-9) | Good mechanistic exemplar linking organelle to process/phenotype boundary; note motility is narrower than the upper trait. |
| GS-GOGAT pathway genes (glnA, gltB, gltD) | contributes_to genomic potential for | ammonium assimilation | genome-inferred uncertain (rajeev2024genomecentricmetagenomicsprovides pages 14-16, rajeev2024genomecentricmetagenomicsprovides pages 9-12) | Presence in MAGs supports potential only, not demonstrated in situ activity; mark uncertain and assay/environment specific. |
| denitrification marker genes (napAB/narGHI/nirSK/norBC/nosZ) | contributes_to genomic potential for | denitrification | genome-inferred uncertain (rajeev2024genomecentricmetagenomicsprovides pages 14-16, rajeev2024genomecentricmetagenomicsprovides pages 9-12) | Strong for community functional potential in biofloc MAGs, but still not direct evidence of active denitrification rates. |
| sox gene cluster / soxB marker | contributes_to genomic potential for | sulfur oxidation | genome-inferred uncertain (rajeev2024genomecentricmetagenomicsprovides pages 12-14, rajeev2024genomecentricmetagenomicsprovides pages 9-12) | Supported as sulfur-oxidation potential in recovered MAGs; keep tied to biofloc context and avoid curating as universal microbial capability. |
| CAZyme genes (e.g., glycoside hydrolases, polysaccharide lyases) | contributes_to genomic potential for | polysaccharide degradation | genome-inferred uncertain (rajeev2024genomecentricmetagenomicsprovides pages 12-14, rajeev2024genomecentricmetagenomicsprovides pages 7-9) | Good example of carbon-degradation potential from metagenomics; not direct proof of substrate turnover without expression/activity data. |


*Table: This table summarizes the most defensible candidate edges for curating the upper-level trait biological process, separating direct ontology/mechanistic relations from genome-inferred microbial functional-potential claims. It is useful for deciding which edges are safe to curate now and which should remain uncertain or be deferred to narrower process traits.*

A more detailed curation table follows. “Snippet” is kept short and close to source language; uncertainty refers to suitability as a causal TraitMech assertion rather than the quality of the publication.

| Subject–predicate–object | Reference | Supporting snippet | Curation assessment |
|---|---|---|---|
| gene product — `enables` — molecular function | DOI: [10.1080/15476286.2024.2408523](https://doi.org/10.1080/15476286.2024.2408523), published October 2024 | MF terms capture the “specific mechanisms of action,” whereas BP captures regulatory context and impact. | **Strong, generic.** Recommended upper-level edge. Avoid implying that a gene itself is a process. (antonazzo2024representationofnoncoding pages 7-8, antonazzo2024representationofnoncoding pages 1-2) |
| molecular function — `causally_upstream_of_or_within` — biological process | Same; current GO synthesis DOI: [10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292), published December 2025 | GO-CAMs organize molecular activities into causal networks showing downstream consequences. | **Strong conceptual edge.** Use the exact relation supported by the imported GO-CAM or evidence model. (antonazzo2024representationofnoncoding pages 7-8, g2026thegeneontology pages 5-7) |
| component biological process — `part_of` — biological process | DOI: [10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) | GO uses `part_of` to organize pathways into component steps. | **Strong generic compositional edge.** It is not necessarily causal by itself. (g2026thegeneontology pages 1-2, g2026thegeneontology pages 7-9) |
| biological process — `occurs_in` — cellular component | DOI: [10.1080/15476286.2024.2408523](https://doi.org/10.1080/15476286.2024.2408523) | CC records where gene products perform their functions. | **Moderate at the upper level.** For precise models, attach location to the molecular activity rather than indiscriminately to an entire process. (antonazzo2024representationofnoncoding pages 1-2) |
| flagellar gene products — `contribute_to`/`enable` — flagellum assembly | DOI: [10.1128/msystems.00036-24](https://doi.org/10.1128/msystems.00036-24), published 16 February 2024 | The function definition included 18 genes/families in five categories required to assemble rod, hook, rings, motor, and export complexes. | **Strong exemplar, taxon-patterned.** Exact gene-to-step assertions require strain-specific literature. (dufaultthompson2024annotatingmicrobialfunctions pages 2-4) |
| flagellum assembly — `results_in_formation_of` — assembled flagellum | Same | Flagella are “complex organelles” whose synthesis involves dozens of genes. | **Mechanistically reasonable**, but confirm the predicate vocabulary used by TraitMech. (dufaultthompson2024annotatingmicrobialfunctions pages 4-7) |
| assembled flagellum — `enables` — bacterial motility | Same | “Flagella are complex organelles that are involved in bacterial motility.” | **Strong exemplar**, but not universal: nonflagellar motility exists, and some flagellar loci may be incomplete or repurposed. (dufaultthompson2024annotatingmicrobialfunctions pages 4-7, dufaultthompson2024annotatingmicrobialfunctions pages 7-9) |
| `glnA`/`gltB`/`gltD` — `contributes_to` — ammonium-assimilation potential | DOI: [10.1128/msystems.00782-24](https://doi.org/10.1128/msystems.00782-24), published 24 September 2024 | 145 MAGs possessed complete GS–GOGAT genes `glnA`, `gltB`, and `gltD`. | **Uncertain/genome-inferred.** Curate as potential unless expression, isotope incorporation, or flux is shown. (rajeev2024genomecentricmetagenomicsprovides pages 14-16, rajeev2024genomecentricmetagenomicsprovides pages 9-12) |
| `napAB` or `narGHI` — `contributes_to` — nitrate-reduction step of denitrification | Same | MAGs contained `narGHI` or `napAB`; downstream markers included `nirSK`, `norBC`, and `nosZ`. | **Uncertain and module-completeness dependent.** A partial gene set must not imply complete denitrification. (rajeev2024genomecentricmetagenomicsprovides pages 14-16, rajeev2024genomecentricmetagenomicsprovides pages 9-12) |
| low-oxygen biofloc microniche — `facilitates` — anaerobic respiratory processes | Same | Bioflocs of approximately 50–1,000 μm can develop localized low-oxygen microenvironments. | **Plausible, context-specific.** Environmental enabling is not evidence that any particular pathway ran. (rajeev2024genomecentricmetagenomicsprovides pages 14-16) |
| `soxXAYZBCD`/`soxB` — `contributes_to` — thiosulfate-oxidation potential | Same | About 10% of MAGs had complete `soxXAYZBCD`; all contained marker `soxB`. | **Uncertain/genome-inferred.** Appropriate only with biofloc/MAG context. (rajeev2024genomecentricmetagenomicsprovides pages 9-12) |
| oxidative `rdsrAB` — `enables` — sulfide-to-sulfite oxidation | Same | `dsrAB` may be reductive or reverse/oxidative; phylogenetic placement was used to distinguish them. | **Do not curate from `dsrAB` presence alone.** Require oxidative clade assignment and preferably biochemical support. (rajeev2024genomecentricmetagenomicsprovides pages 5-7) |
| GH/PL CAZymes — `contribute_to` — polysaccharide-degradation potential | Same | 7,540 CAZyme genes were identified; GH13, GH43, GH16, GH5 and PL1 supported complex-carbohydrate degradation potential. | **Uncertain/genome-inferred.** Substrate specificity and actual turnover require assays. (rajeev2024genomecentricmetagenomicsprovides pages 12-14, rajeev2024genomecentricmetagenomicsprovides pages 7-9) |
| high C:N management — `promotes` — heterotrophic bacterial growth/biofloc formation | Same | Raising C:N “stimulates the growth of heterotrophic bacteria,” which aggregate with microbes and organic matter. | **System-specific but comparatively direct.** Keep distinct from an assertion that it activates any one metabolic pathway. (rajeev2024genomecentricmetagenomicsprovides pages 1-2) |

## 4. Recent developments and applications

### Hierarchical microbial-function annotation

ProkFunFind, released in 2024, operationalizes a model close to TraitMech: an overall biological function is divided into components such as transport, metabolic enzymes, and regulation, and each component is linked to genes and heterogeneous search terms in YAML. In the flagellar benchmark, all core genes were found in 66 of 68 flagellated Bacillota genomes; overall the study reported flagellar-gene detection in 81% of annotated species and predicted 125 additional putative clusters. Some discrepancies reflected strain variation, pseudogenization, or homology to type III secretion systems—an important warning against single-marker causality. (dufaultthompson2024annotatingmicrobialfunctions pages 4-7, dufaultthompson2024annotatingmicrobialfunctions pages 7-9)

### Genome-to-trait machine learning

MICROPHERRET infers 86 metabolic/ecological functions from genome annotations and generally supports genomes above 70% completeness. Its acetoclastic-methanogenesis model achieved a Matthews correlation coefficient of 0.86 versus 0.45 for the comparator and recovered 13 of 17 known acetoclastic methanogens without false positives. It was applied to 4,146 genomes from FAPROTAX and anaerobic-digestion data. These outputs are useful candidate nodes or priors, but they remain predictions rather than causal evidence of process execution. (bizzotto2024micropherretmicrobialphenotypic pages 13-15, bizzotto2024micropherretmicrobialphenotypic pages 1-2)

### Engineered microbial systems

Genome-centric analysis of biofloc aquaculture recovered 520 nonredundant MAGs—517 bacterial and three archaeal—with approximately 93% unclassified at species level. The inferred carbon, nitrogen, and sulfur modules help identify organisms potentially responsible for nutrient recycling and removal of ammonia, nitrate, and sulfide in a real aquaculture technology. The work demonstrates the practical value of process-level graphs for water-quality management while also showing why uncultured diversity and MAG incompleteness must remain explicit provenance. (rajeev2024genomecentricmetagenomicsprovides pages 1-2, rajeev2024genomecentricmetagenomicsprovides pages 5-7)

### Synthetic communities and metabolic models

Recent expert reviews recommend designing microbial synthetic communities around functional traits and high-throughput assays rather than taxonomic abundance or co-occurrence alone. Genome-scale metabolic models can propose metabolite exchanges and community functions, but non-model strain coverage remains incomplete and black-box machine learning can obscure causal and ecological structure. Predictions require experimental validation because contamination, batch effects, overfitting, and spurious associations can produce apparently convincing but invalid biological links. (jing2024strategiesfortailoring pages 4-5, wu2024decipheringanddesigning pages 8-9)

## 5. Proposed minimal graph for `biological_process.yaml`

A conservative upper-class graph should contain approximately the following semantics:

1. **gene product `enables` molecular function**;
2. **molecular function `causally_upstream_of_or_within` biological process**;
3. **component biological process `part_of` biological process**;
4. **molecular function/activity `occurs_in` cellular component**;
5. **environmental condition `regulates` or `enables` biological-process execution**, only when experimentally supported;
6. **biological-process execution `results_in` assay-observed phenotype/outcome**;
7. **genome annotation `supports_inference_of` functional potential**, explicitly separate from execution.

This metamodel preserves the defining distinction between activity, process, location, potential, and observation. Specific flagellar or biogeochemical modules should preferably reside in narrower trait graphs and connect upward through `is_a` or analogous specialization relations.

## 6. Claims that should not yet be curated as causal facts

1. **Do not equate gene presence with active process execution.** MAG or genome evidence supports potential only.
2. **Do not infer a complete pathway from one marker.** `soxB`, `nirS`, `nosZ`, or `dsrAB` alone does not establish complete sulfur oxidation or denitrification.
3. **Do not infer oxidative Dsr direction from the label `dsrAB`.** Reductive and reverse enzymes require phylogenetic/mechanistic discrimination. (rajeev2024genomecentricmetagenomicsprovides pages 5-7)
4. **Do not treat missing genes in incomplete MAGs as definitive pathway absence.** The biofloc MAG collection included medium-quality genomes above 50% completeness. (rajeev2024genomecentricmetagenomicsprovides pages 5-7)
5. **Do not treat ML scores as mechanistic evidence.** MICROPHERRET and related tools prioritize candidates but do not demonstrate expression, reaction direction, flux, or ecological causality. (bizzotto2024micropherretmicrobialphenotypic pages 13-15, bizzotto2024micropherretmicrobialphenotypic pages 1-2)
6. **Do not generalize biofloc edges to all microbes or environments.** Oxygen gradients, supplied carbon, community interactions, and reactor management are essential context.
7. **Do not make bacterial motility synonymous with flagellar motility.** Gliding, twitching, and other mechanisms are boundary cases.
8. **Do not assign invented CURIEs.** Preserve label-only nodes until exact ontology releases, taxa, strains, reactions, and compounds have been verified.
9. **Do not import the entire exemplar graph into an upper-class definition.** Denitrification, sulfur oxidation, polysaccharide degradation, and flagellar assembly illustrate biological processes but are not necessary parts of every biological process.

## DOI-first bibliography

1. Dufault-Thompson K, Jiang X. **Annotating microbial functions with ProkFunFind.** *mSystems*. Published 16 February 2024; issue date March 2024. DOI: [10.1128/msystems.00036-24](https://doi.org/10.1128/msystems.00036-24). (dufaultthompson2024annotatingmicrobialfunctions pages 1-2)
2. Rajeev M, Jung I, Kang I, Cho J-C. **Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture.** *mSystems*. Published 24 September 2024; October 2024 issue. DOI: [10.1128/msystems.00782-24](https://doi.org/10.1128/msystems.00782-24). (rajeev2024genomecentricmetagenomicsprovides pages 1-2)
3. Bizzotto E, et al. **MICROPHERRET: MICRObial PHEnotypic tRait ClassifieR using Machine lEarning Techniques.** *Environmental Microbiome*. August 2024. DOI: [10.1186/s40793-024-00600-6](https://doi.org/10.1186/s40793-024-00600-6). (bizzotto2024micropherretmicrobialphenotypic pages 13-15, bizzotto2024micropherretmicrobialphenotypic pages 1-2)
4. Antonazzo G, Gaudet P, Lovering RC, Attrill H. **Representation of non-coding RNA-mediated regulation of gene expression using the Gene Ontology.** *RNA Biology*. October 2024. DOI: [10.1080/15476286.2024.2408523](https://doi.org/10.1080/15476286.2024.2408523). (antonazzo2024representationofnoncoding pages 7-8, antonazzo2024representationofnoncoding pages 1-2)
5. Jing J, Garbeva P, Raaijmakers JM, Medema MH. **Strategies for tailoring functional microbial synthetic communities.** *The ISME Journal*. 2024. DOI: [10.1093/ismejo/wrae049](https://doi.org/10.1093/ismejo/wrae049). (jing2024strategiesfortailoring pages 4-5)
6. Wu S, et al. **Deciphering and designing microbial communities by genome-scale metabolic modelling.** *Computational and Structural Biotechnology Journal*. 2024;23:1990–2000. DOI: [10.1016/j.csbj.2024.04.055](https://doi.org/10.1016/j.csbj.2024.04.055). (wu2024decipheringanddesigning pages 8-9)
7. Aleksander SA, et al. **The Gene Ontology knowledgebase in 2026.** *Nucleic Acids Research*. Published December 2025. DOI: [10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292). This post-2024 source is used only for the latest GO/GO-CAM status—over 1,500 models—not as the sole support for the core definition. (g2026thegeneontology pages 1-2, g2026thegeneontology pages 5-7)

**Curation priority:** implement the seven-edge upper-level metamodel first; retain the flagellar module as a well-supported exemplar; place all MAG-derived biofloc edges under an explicit “genomic functional potential” evidence qualifier until transcriptomic, proteomic, biochemical, or flux evidence demonstrates process execution.

References

1. (g2026thegeneontology pages 1-2): Suzi A Aleksander, James P Balhoff, Seth Carbon, J Michael Cherry, Dustin Ebert, Marc Feuermann, Pascale Gaudet, Nomi L Harris, David P Hill, Patrick Kalita, Raymond Lee, Huaiyu Mi, Sierra Moxon, Christopher J Mungall, Anushya Muruganujan, Tremayne Mushayahama, Paul W Sternberg, Paul D Thomas, Kimberly Van Auken, Edith D Wong, Valerie Wood, Jolene Ramsey, Deborah A Siegele, Rex L Chisholm, Robert Dodson, Petra Fey, Maria Cristina Aspromonte, Maria Victoria Nugnes, Ximena Aixa Castro Naser, Silvio C E Tosatto, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H Brown, Gil dos Santos, Steven Marygold, Katja Röper, Victor Strelets, Christopher J Tabone, Jim Thurmond, Pinglei Zhou, Rossana Zaru, Ruth C Lovering, Colin Logie, Daiqing Chen, Alexandra Naba, Karen Christie, Lori Corbani, Li Ni, Dmitry Sitnikov, Cynthia Smith, James Seager, Laurel Cooper, Justin Elser, Pankaj Jaiswal, Parul Gupta, Sushma Naithani, Pascal Carme, Kim Rutherford, Jeffrey L De Pons, Melinda R Dwinell, G Thomas Hayman, Mary L Kaldunski, Anne E Kwitek, Stanley J F Laulederkind, Marek A Tutaj, Mahima Vedi, Shur-Jen Wang, Peter D’Eustachio, Lucila Aimo, Kristian Axelsen, Alan Bridge, Nevila Hyka-Nouspikel, Anne Morgat, Gene Goldbold, Stacia R Engel, Stuart R Miyasato, Robert S Nash, Gavin Sherlock, Shuai Weng, Erika Bakker, Tanya Z Berardini, Leonore Reiser, Andrea Auchincloss, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Alex Bateman, Aduragbemi Adesina, Emily Bowler-Barnett, David Carpentier, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Nadya Urakova, Kate Warner, Conny Wing-Hen Yu, Juancarlos Chan, Stavros Diamantakis, Mark Quinton-Tulloch, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Doug Howe, Sridhar Ramachandran, Leyla Ruzicka, and Monte Westerfield. The gene ontology knowledgebase in 2026. Nucleic Acids Research, 54(D1):D1779-D1792, Dec 2025. URL: https://doi.org/10.1093/nar/gkaf1292, doi:10.1093/nar/gkaf1292. This article has 147 citations and is from a highest quality peer-reviewed journal.

2. (antonazzo2024representationofnoncoding pages 1-2): Giulia Antonazzo, Pascale Gaudet, Ruth C. Lovering, and Helen Attrill. Representation of non-coding rna-mediated regulation of gene expression using the gene ontology. Oct 2024. URL: https://doi.org/10.1080/15476286.2024.2408523, doi:10.1080/15476286.2024.2408523. This article has 13 citations and is from a peer-reviewed journal.

3. (g2026thegeneontology pages 7-9): Suzi A Aleksander, James P Balhoff, Seth Carbon, J Michael Cherry, Dustin Ebert, Marc Feuermann, Pascale Gaudet, Nomi L Harris, David P Hill, Patrick Kalita, Raymond Lee, Huaiyu Mi, Sierra Moxon, Christopher J Mungall, Anushya Muruganujan, Tremayne Mushayahama, Paul W Sternberg, Paul D Thomas, Kimberly Van Auken, Edith D Wong, Valerie Wood, Jolene Ramsey, Deborah A Siegele, Rex L Chisholm, Robert Dodson, Petra Fey, Maria Cristina Aspromonte, Maria Victoria Nugnes, Ximena Aixa Castro Naser, Silvio C E Tosatto, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H Brown, Gil dos Santos, Steven Marygold, Katja Röper, Victor Strelets, Christopher J Tabone, Jim Thurmond, Pinglei Zhou, Rossana Zaru, Ruth C Lovering, Colin Logie, Daiqing Chen, Alexandra Naba, Karen Christie, Lori Corbani, Li Ni, Dmitry Sitnikov, Cynthia Smith, James Seager, Laurel Cooper, Justin Elser, Pankaj Jaiswal, Parul Gupta, Sushma Naithani, Pascal Carme, Kim Rutherford, Jeffrey L De Pons, Melinda R Dwinell, G Thomas Hayman, Mary L Kaldunski, Anne E Kwitek, Stanley J F Laulederkind, Marek A Tutaj, Mahima Vedi, Shur-Jen Wang, Peter D’Eustachio, Lucila Aimo, Kristian Axelsen, Alan Bridge, Nevila Hyka-Nouspikel, Anne Morgat, Gene Goldbold, Stacia R Engel, Stuart R Miyasato, Robert S Nash, Gavin Sherlock, Shuai Weng, Erika Bakker, Tanya Z Berardini, Leonore Reiser, Andrea Auchincloss, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Alex Bateman, Aduragbemi Adesina, Emily Bowler-Barnett, David Carpentier, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Nadya Urakova, Kate Warner, Conny Wing-Hen Yu, Juancarlos Chan, Stavros Diamantakis, Mark Quinton-Tulloch, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Doug Howe, Sridhar Ramachandran, Leyla Ruzicka, and Monte Westerfield. The gene ontology knowledgebase in 2026. Nucleic Acids Research, 54(D1):D1779-D1792, Dec 2025. URL: https://doi.org/10.1093/nar/gkaf1292, doi:10.1093/nar/gkaf1292. This article has 147 citations and is from a highest quality peer-reviewed journal.

4. (antonazzo2024representationofnoncoding pages 7-8): Giulia Antonazzo, Pascale Gaudet, Ruth C. Lovering, and Helen Attrill. Representation of non-coding rna-mediated regulation of gene expression using the gene ontology. Oct 2024. URL: https://doi.org/10.1080/15476286.2024.2408523, doi:10.1080/15476286.2024.2408523. This article has 13 citations and is from a peer-reviewed journal.

5. (g2026thegeneontology pages 5-7): Suzi A Aleksander, James P Balhoff, Seth Carbon, J Michael Cherry, Dustin Ebert, Marc Feuermann, Pascale Gaudet, Nomi L Harris, David P Hill, Patrick Kalita, Raymond Lee, Huaiyu Mi, Sierra Moxon, Christopher J Mungall, Anushya Muruganujan, Tremayne Mushayahama, Paul W Sternberg, Paul D Thomas, Kimberly Van Auken, Edith D Wong, Valerie Wood, Jolene Ramsey, Deborah A Siegele, Rex L Chisholm, Robert Dodson, Petra Fey, Maria Cristina Aspromonte, Maria Victoria Nugnes, Ximena Aixa Castro Naser, Silvio C E Tosatto, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H Brown, Gil dos Santos, Steven Marygold, Katja Röper, Victor Strelets, Christopher J Tabone, Jim Thurmond, Pinglei Zhou, Rossana Zaru, Ruth C Lovering, Colin Logie, Daiqing Chen, Alexandra Naba, Karen Christie, Lori Corbani, Li Ni, Dmitry Sitnikov, Cynthia Smith, James Seager, Laurel Cooper, Justin Elser, Pankaj Jaiswal, Parul Gupta, Sushma Naithani, Pascal Carme, Kim Rutherford, Jeffrey L De Pons, Melinda R Dwinell, G Thomas Hayman, Mary L Kaldunski, Anne E Kwitek, Stanley J F Laulederkind, Marek A Tutaj, Mahima Vedi, Shur-Jen Wang, Peter D’Eustachio, Lucila Aimo, Kristian Axelsen, Alan Bridge, Nevila Hyka-Nouspikel, Anne Morgat, Gene Goldbold, Stacia R Engel, Stuart R Miyasato, Robert S Nash, Gavin Sherlock, Shuai Weng, Erika Bakker, Tanya Z Berardini, Leonore Reiser, Andrea Auchincloss, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Alex Bateman, Aduragbemi Adesina, Emily Bowler-Barnett, David Carpentier, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Nadya Urakova, Kate Warner, Conny Wing-Hen Yu, Juancarlos Chan, Stavros Diamantakis, Mark Quinton-Tulloch, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Doug Howe, Sridhar Ramachandran, Leyla Ruzicka, and Monte Westerfield. The gene ontology knowledgebase in 2026. Nucleic Acids Research, 54(D1):D1779-D1792, Dec 2025. URL: https://doi.org/10.1093/nar/gkaf1292, doi:10.1093/nar/gkaf1292. This article has 147 citations and is from a highest quality peer-reviewed journal.

6. (rajeev2024genomecentricmetagenomicsprovides pages 12-14): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

7. (rajeev2024genomecentricmetagenomicsprovides pages 9-12): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

8. (rajeev2024genomecentricmetagenomicsprovides pages 1-2): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

9. (dufaultthompson2024annotatingmicrobialfunctions pages 4-7): Keith Dufault-Thompson and Xiaofang Jiang. Annotating microbial functions with prokfunfind. Mar 2024. URL: https://doi.org/10.1128/msystems.00036-24, doi:10.1128/msystems.00036-24. This article has 7 citations and is from a peer-reviewed journal.

10. (dufaultthompson2024annotatingmicrobialfunctions pages 2-4): Keith Dufault-Thompson and Xiaofang Jiang. Annotating microbial functions with prokfunfind. Mar 2024. URL: https://doi.org/10.1128/msystems.00036-24, doi:10.1128/msystems.00036-24. This article has 7 citations and is from a peer-reviewed journal.

11. (rajeev2024genomecentricmetagenomicsprovides pages 7-9): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

12. (dufaultthompson2024annotatingmicrobialfunctions pages 1-2): Keith Dufault-Thompson and Xiaofang Jiang. Annotating microbial functions with prokfunfind. Mar 2024. URL: https://doi.org/10.1128/msystems.00036-24, doi:10.1128/msystems.00036-24. This article has 7 citations and is from a peer-reviewed journal.

13. (rajeev2024genomecentricmetagenomicsprovides pages 5-7): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

14. (dufaultthompson2024annotatingmicrobialfunctions pages 7-9): Keith Dufault-Thompson and Xiaofang Jiang. Annotating microbial functions with prokfunfind. Mar 2024. URL: https://doi.org/10.1128/msystems.00036-24, doi:10.1128/msystems.00036-24. This article has 7 citations and is from a peer-reviewed journal.

15. (rajeev2024genomecentricmetagenomicsprovides pages 14-16): Meora Rajeev, Ilsuk Jung, Ilnam Kang, and Jang-Cheon Cho. Genome-centric metagenomics provides insights into the core microbial community and functional profiles of biofloc aquaculture. Oct 2024. URL: https://doi.org/10.1128/msystems.00782-24, doi:10.1128/msystems.00782-24. This article has 34 citations and is from a peer-reviewed journal.

16. (bizzotto2024micropherretmicrobialphenotypic pages 13-15): Edoardo Bizzotto, Sofia Fraulini, Guido Zampieri, Esteban Orellana, Laura Treu, and Stefano Campanaro. Micropherret: microbial phenotypic trait classifier using machine learning techniques. Environmental Microbiome, Aug 2024. URL: https://doi.org/10.1186/s40793-024-00600-6, doi:10.1186/s40793-024-00600-6. This article has 9 citations and is from a peer-reviewed journal.

17. (bizzotto2024micropherretmicrobialphenotypic pages 1-2): Edoardo Bizzotto, Sofia Fraulini, Guido Zampieri, Esteban Orellana, Laura Treu, and Stefano Campanaro. Micropherret: microbial phenotypic trait classifier using machine learning techniques. Environmental Microbiome, Aug 2024. URL: https://doi.org/10.1186/s40793-024-00600-6, doi:10.1186/s40793-024-00600-6. This article has 9 citations and is from a peer-reviewed journal.

18. (jing2024strategiesfortailoring pages 4-5): Jiayi Jing, Paolina Garbeva, Jos M Raaijmakers, and Marnix H Medema. Strategies for tailoring functional microbial synthetic communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae049, doi:10.1093/ismejo/wrae049. This article has 185 citations.

19. (wu2024decipheringanddesigning pages 8-9): Shengbo Wu, Zheping Qu, Danlei Chen, Hao Wu, Qinggele Caiyin, and Jianjun Qiao. Deciphering and designing microbial communities by genome-scale metabolic modelling. Computational and Structural Biotechnology Journal, 23:1990-2000, Dec 2024. URL: https://doi.org/10.1016/j.csbj.2024.04.055, doi:10.1016/j.csbj.2024.04.055. This article has 30 citations and is from a peer-reviewed journal.