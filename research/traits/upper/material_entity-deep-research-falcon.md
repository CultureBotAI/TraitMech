---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:12:44.620320'
end_time: '2026-08-04T12:18:49.003162'
duration_seconds: 364.38
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: material entity
  trait_identifier: METPO:1000186
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: material_entity
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An object or portion of a substance or mixture of substances that consists
    of matter
  parent_traits: ''
  synonyms: ''
  evidence_summary: 'DOI:10.3233/AO-220262: BFO is a genuine top-level ontology (Supports
    material entity as a top-level ontology class rather than a concrete microbial
    trait.) | DOI:10.7551/mitpress/9780262527811.001.0001: specific top-level ontology,
    the Basic Formal Ontology (Supports BFO as the upper ontology context for material
    entity.)'
  causal_graph_summary: 'material_entity_bfo_upper_context: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** material entity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000186
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An object or portion of a substance or mixture of substances that consists of matter
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.3233/AO-220262: BFO is a genuine top-level ontology (Supports material entity as a top-level ontology class rather than a concrete microbial trait.) | DOI:10.7551/mitpress/9780262527811.001.0001: specific top-level ontology, the Basic Formal Ontology (Supports BFO as the upper ontology context for material entity.)
- **Existing causal graph summary:** material_entity_bfo_upper_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **material entity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/material_entity.yaml`.

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
- **Trait label:** material entity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000186
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An object or portion of a substance or mixture of substances that consists of matter
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.3233/AO-220262: BFO is a genuine top-level ontology (Supports material entity as a top-level ontology class rather than a concrete microbial trait.) | DOI:10.7551/mitpress/9780262527811.001.0001: specific top-level ontology, the Basic Formal Ontology (Supports BFO as the upper ontology context for material entity.)
- **Existing causal graph summary:** material_entity_bfo_upper_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **material entity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/material_entity.yaml`.

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


# Curation report: **material entity** (`METPO:1000186`)

## Executive curation decision

`METPO:1000186` denotes an **upper-level ontological class**, not a microbial phenotype, physiological capacity, environmental preference, or assay-observed property. In BFO terms, a material entity is a continuant that can bear qualities, dispositions, functions, and roles and can participate in processes. It is therefore the **bearer/context of microbial traits**, not itself an appropriate endpoint for a mechanistic TraitMech graph. BFO separates continuants, which lack temporal parts, from occurrents/processes, which have temporal parts; it also distinguishes a material bearer from dependent properties such as qualities and realizable entities. (rabenberg2024groundingrealizableentities pages 1-3)

**Recommendation:** retain the existing small upper-context graph and, at most, add schema-level relations. Do **not** add genes, proteins, pathways, nutrients, chemicals, environments, or inhibitors as direct causes of “material entity.” Those mechanisms belong under narrower targets such as motility, substrate utilization, oxygen tolerance, toxin production, antibiotic resistance, pathogenic disposition, or a measured cellular quality.

| Proposed content | Decision | Rationale | Evidence strength |
|---|---|---|---|
| `METPO:1000186 material entity` as an upper-ontology class (`is_a` BFO-style continuant / independent continuant context) | curate | This is the safest, ontology-level content for the term: BFO divides reality into continuant vs. occurrent, and material entity is a bearer-category rather than a microbial phenotype. Suitable as schema/context in `upper/` curation. (rabenberg2024groundingrealizableentities pages 1-3) | Strong |
| `material entity` bears `quality` and may bear `disposition` / other realizable entities | curate | BFO-based sources explicitly state that qualities and realizable entities depend on bearers, and that realizable entities such as dispositions inhere in material entities. This supports only generic bearer relations, not trait-specific mechanisms. (rabenberg2024groundingrealizableentities pages 1-3, rabenberg2024groundingrealizableentities pages 3-6, rabenberg2024groundingrealizableentities pages 8-11) | Strong |
| `material entity` participates in `process` | curate | The BFO distinction between continuants and occurrents implies that material entities participate in processes, while processes are not themselves material entities. This is a high-level ontological relation appropriate for context. (rabenberg2024groundingrealizableentities pages 1-3, rabenberg2024groundingrealizableentities pages 3-6) | Strong |
| Direct mechanistic graph from `material entity` to generic genes, proteins, pathways, metabolites, chemicals, nutrients, inhibitors, transporters, or environments | do not curate | These entities can causally explain narrower microbial qualities/dispositions/functions, but attaching them directly to the top-level class `material entity` creates a category error: the class is too broad and not itself a phenotype, capacity, or assay-observed property. (rabenberg2024groundingrealizableentities pages 1-3, rabenberg2024groundingrealizableentities pages 3-6, santangelo2024integratingbiologicalknowledge pages 3-5, santangelo2024integratingbiologicalknowledge pages 2-3) | Strong |
| Build a direct mechanistic TraitMech causal graph for `material entity` | do not curate | Current microbiome KG guidance stresses semantically well-defined, inference-ready relations and alignment to ontologies; mechanistic graphs should target specific microbial traits/functions, not an upper-level bearer class. (santangelo2024integratingbiologicalknowledge pages 1-2, santangelo2024integratingbiologicalknowledge pages 2-3, santangelo2024integratingbiologicalknowledge pages 12-13, callahan2024anopensource pages 1-2) | Strong |
| `pathogenic disposition` as an example of a narrower microbial target | context-only | The host-pathogen example shows how a microbial disposition borne by a material entity can be modeled mechanistically. Useful as a pointer to the kind of downstream trait that should receive a causal graph instead of `material entity`. (rabenberg2024groundingrealizableentities pages 8-11) | Strong |
| `host role` as an example of a narrower realizable-entity target | context-only | Role is externally grounded and distinct from disposition; this is useful for boundary-setting and for identifying alternative trait targets, but it is not evidence for curating mechanisms under `material entity` itself. (rabenberg2024groundingrealizableentities pages 3-6, rabenberg2024groundingrealizableentities pages 8-11) | Strong |
| Correlation-only microbial findings (e.g., microbe ↔ host phenotype/feed efficiency associations) | do not curate | Recent KG work distinguishes mechanistic from correlative knowledge. Correlation-only findings should not be attached as causal edges to `material entity`, and often should not be curated causally at all without mechanistic support. (santangelo2024integratingbiologicalknowledge pages 3-5, santangelo2024integratingbiologicalknowledge pages 2-3, zhang2024knowledgegraphderivedfeed pages 1-3, zhang2024knowledgegraphderivedfeed pages 3-4) | Strong |
| Real-world KG / ontology implementations as precedent for curation style | context-only | PheKnowLator and microbiome KGs show best practices: ontologically grounded identifiers, semantically typed edges, interoperability, and careful separation of heterogeneous entity types. They support curation policy, not direct biological edges for this term. (callahan2024anopensource pages 1-2, callahan2024anopensource pages 2-4, santangelo2024integratingbiologicalknowledge pages 12-13, zhang2024knowledgegraphderivedfeed pages 1-3, zhang2024knowledgegraphderivedfeed pages 3-4) | Moderate |
| Recommended curation outcome for `data/traits/upper/material_entity.yaml` | curate | Keep only upper-ontology/context relations (placement, bearer-of, participates-in). Do not populate with mechanistic microbial genes/pathways/chemicals/environment edges. No direct mechanistic causal graph should be built for this upper class. (rabenberg2024groundingrealizableentities pages 1-3, rabenberg2024groundingrealizableentities pages 8-11, santangelo2024integratingbiologicalknowledge pages 2-3, santangelo2024integratingbiologicalknowledge pages 12-13) | Strong |


*Table: This table summarizes what should and should not be curated for METPO:1000186. It is useful for preventing category errors by restricting this upper-level term to ontology/context relations rather than direct microbial mechanism edges.*

## 1. Trait scope

### 1.1 What the term represents

The supplied definition—“An object or portion of a substance or mixture of substances that consists of matter”—identifies what kind of entity something is. It does not specify a biological variation, measurable state, or capacity. Relevant microbial instances include a microbial cell, cell aggregate, organelle, protein molecule, metabolite portion, membrane, biofilm aggregate, or environmental sample portion. These are heterogeneous bearers and participants, not instances of one shared microbial phenotype.

BFO is the OBO Foundry’s designated top-level ontology and supplies general classes such as quality, process, function, and role, together with relations such as `participates in` and `member of`. A 2024 analysis reports that BFO is used by more than 600 open-source ontology projects and is standardized as ISO/IEC 21838-2. (rabenberg2024groundingrealizableentities pages 1-3)

### 1.2 Boundary cases

| Nearby category | Distinction from material entity | Microbial example |
|---|---|---|
| **Quality** | A specifically dependent continuant that inheres in a bearer and is manifested whenever it exists. | Cell shape, membrane charge, or measured pigmentation. |
| **Disposition** | A realizable entity internally grounded in a material bearer’s physical make-up; it may exist without being realized. Loss of the disposition entails relevant physical change in the bearer. | Solubility, antibiotic susceptibility, capacity to metabolize a substrate, or pathogenic disposition. (rabenberg2024groundingrealizableentities pages 3-6) |
| **Function** | A realizable entity associated with a bearer and realized in a process; it is not the bearer itself. | Enzyme catalytic function or transporter function. |
| **Role** | An externally grounded, optional realizable entity that a bearer can gain or lose without corresponding physical alteration. | Host role or laboratory reagent role. Roles and dispositions are disjoint sibling classes in the cited BFO treatment. (rabenberg2024groundingrealizableentities pages 3-6) |
| **Process/occurrent** | Has temporal parts; a material entity participates in it but is not identical to it. | Growth, fermentation, chemotaxis, toxin secretion, or cell division. (rabenberg2024groundingrealizableentities pages 1-3) |
| **Immaterial entity** | Lacks material parts; it can include a site or boundary. It is not a material entity, although it may be spatially associated with one. | A cellular site or anatomical boundary. Dispositions cannot be borne by immaterial entities because they lack a physical basis. (rabenberg2024groundingrealizableentities pages 3-6) |
| **Assay measurement/data item** | An information entity about a material bearer or process, not the bearer itself. | Optical-density value, MIC result, or metabolomics abundance measurement. |

A key modeling principle is that a disposition is realized because of the bearer’s physical make-up under particular environmental circumstances. The cited analysis uses NaCl solubility to show the pattern: structural qualities ground a disposition, while an environmental condition enables its realization. (rabenberg2024groundingrealizableentities pages 3-6)

## 2. Candidate nodes grouped by type

These nodes are appropriate only for a **minimal upper-context model** or as templates for narrower downstream traits.

### 2.1 Upper-ontology entities

- **material entity** — `METPO:1000186` (quote verbatim in YAML).
- **continuant** — label-only unless the project has already selected the corresponding BFO CURIE.
- **independent continuant** — label-only pending confirmation against the imported BFO release.
- **quality** — label-only pending ontology import confirmation.
- **realizable entity** — label-only.
- **disposition** — label-only.
- **function** — label-only.
- **role** — label-only.
- **process** — label-only.
- **immaterial entity** — label-only.

No BFO identifiers are supplied here because they were not verified directly from the active ontology release; identifiers should not be reconstructed from memory.

### 2.2 Candidate material bearers

These are possible descendants or instances, not causes of the target class:

- microbial cell;
- microbial population or object aggregate;
- biofilm aggregate;
- cellular component or organelle;
- protein/enzyme molecule;
- transporter or protein complex;
- chemical portion/metabolite portion;
- culture-medium portion or environmental sample portion.

Use established ontology identifiers only after resolving each term against the intended ontology version—for example, NCBITaxon for organisms, GO for cellular components, ChEBI for chemicals, and Protein Ontology or UniProt for proteins.

### 2.3 Dependent traits and processes

- cellular morphology or other quality;
- metabolic disposition;
- pathogenic disposition;
- antimicrobial susceptibility/resistance disposition;
- transporter or enzyme function;
- host role;
- metabolic process;
- growth process;
- localization, infection, or toxin-production process.

The 2024 host–pathogen ontology analysis explicitly defines pathogenic disposition as a disposition borne by a material entity to establish localization or produce transmissible toxins capable of forming disorder. It models *S. aureus* pathogenicity as an internally grounded disposition that can exist even when no host disorder is currently realized. (rabenberg2024groundingrealizableentities pages 8-11)

### 2.4 Mechanistic entities to reserve for narrower traits

- genes and alleles;
- proteins, enzymes, transporters, and complexes;
- reactions and pathways;
- electron donors and acceptors;
- nutrients, metabolites, inhibitors, and antibiotics;
- oxygen level, pH, temperature, salinity, and medium composition;
- assay platform, incubation time, inoculum, and detection threshold.

These are biologically valuable nodes, but no source supports a direct causal relation from any of them to the universal class “material entity.” Current microbiome knowledge resources instead connect annotated genes to reactions and metabolic phenotypes and use genome-scale metabolic networks to simulate phenotypes in specified environments. (santangelo2024integratingbiologicalknowledge pages 3-5)

## 3. Candidate edges

### 3.1 Edges suitable for the upper-context YAML

These are **ontological or schema-level**, not biological causal edges.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation notes |
|---|---|---|---|---|---|
| `METPO:1000186` material entity | `is_a` | independent continuant | DOI:10.3233/AO-220262; DOI:10.48550/arXiv.2405.00197 | “BFO divides reality into disjoint categories of continuant and occurrent.” | Curate only after verifying the exact imported parent and CURIE in METPO/BFO. This is classification, not causation. (rabenberg2024groundingrealizableentities pages 1-3) |
| quality | `inheres_in` | material entity | DOI:10.48550/arXiv.2405.00197 | “all instances of specifically dependent continuant, including instances of quality and realizable entity, depend for their existence on other entities.” | Safe generic bearer relation; relation CURIE must be taken from the project’s RO/BFO import. (rabenberg2024groundingrealizableentities pages 1-3) |
| disposition | `inheres_in` | material entity | DOI:10.48550/arXiv.2405.00197 | “d’s bearer is some material entity.” | Generic axiom. Do not interpret it as saying every material entity bears every disposition. (rabenberg2024groundingrealizableentities pages 3-6) |
| disposition | `realized_in` | process | DOI:10.48550/arXiv.2405.00197 | Bearers “may participate in processes which realize the realizable entity.” | Generic schema relation; not a trait-specific causal edge. (rabenberg2024groundingrealizableentities pages 1-3) |
| material entity | `participates_in` | process | DOI:10.48550/arXiv.2405.00197 | Continuants and occurrents are distinct, while bearers participate in processes realizing their properties. | Appropriate upper-context pattern. Relation identifier requires release-level verification. (rabenberg2024groundingrealizableentities pages 1-3) |
| disposition | `internally_grounded_in` | quality | DOI:10.48550/arXiv.2405.00197 | “dispositions are internally grounded because they exhibit dependence grounding with respect to qualities that are not relational qualities.” | **Uncertain/proposed relation.** The authors describe this as a supplement requiring a new relation; it is not established here as a released BFO/RO predicate. (rabenberg2024groundingrealizableentities pages 8-11) |
| role | `externally_grounded_in` | relational quality | DOI:10.48550/arXiv.2405.00197 | “roles are externally grounded because they exhibit dependence grounding with respect to relational qualities.” | **Uncertain/proposed relation.** Do not curate until an approved relation and identifier exist. (rabenberg2024groundingrealizableentities pages 8-11) |

### 3.2 Illustrative narrower-trait patterns—not edges for `METPO:1000186`

| Subject | Predicate | Object | Evidence and snippet | Status |
|---|---|---|---|---|
| microbial pathogen | `bearer_of` | pathogenic disposition | “Pathogens bear such dispositions and so may establish localization in some host.” (rabenberg2024groundingrealizableentities pages 8-11) | Strong conceptual example, but requires a taxon- and trait-specific source before TraitMech curation. |
| pathogenic disposition | `realized_in` | host localization or toxin-production process | Definition refers to a disposition “to establish localization in or produce toxins.” (rabenberg2024groundingrealizableentities pages 8-11) | Curate only under a narrower pathogenicity trait and with validated process terms. |
| organism/acellular structure | `bearer_of` | host role | Host role is realized when the bearer is used as a site of pathogen reproduction or replication. (rabenberg2024groundingrealizableentities pages 8-11) | Contextual; not a mechanism of material entity. |
| microbial gene annotation | `supports/informs` | biochemical reaction capacity | GSMNs use annotated genes to identify reactions that their enzyme products can affect. (santangelo2024integratingbiologicalknowledge pages 3-5) | Methodological pattern; a particular gene–reaction edge requires organism-specific primary evidence. |
| microbial community metabolic network | `predicts_under_environment` | metabolic phenotype | GSMNs synthesize metabolism and simulate metabolic phenotypes in environments of interest. (santangelo2024integratingbiologicalknowledge pages 3-5) | Model prediction, not necessarily experimentally demonstrated causation; mark inferred. |

## 4. Recent developments, applications, and statistics

### 4.1 Ontological refinement in 2024

Rabenberg and colleagues proposed explicit grounding relations among qualities, dispositions, and roles and demonstrated them using host–pathogen interactions. Their main expert conclusion is that dispositions are grounded in qualities of their bearers, whereas roles depend on relational qualities and external circumstances. They also warn that the proposed additions are supplements rather than changes to the BFO hierarchy and could impose ontology-version maintenance costs. (rabenberg2024groundingrealizableentities pages 11-13, rabenberg2024groundingrealizableentities pages 8-11)

This work supports a TraitMech architecture of the form:

`material bearer → bears quality/disposition → disposition realized in process under environment → observed phenotype`

It does **not** support:

`gene/pathway/environment → causes material entity`.

### 4.2 Mechanistic microbiome knowledge resources

A review published **4 April 2024** distinguishes mechanistic knowledge—an assertion of causal relationships—from correlative knowledge—an assertion of statistical association. It argues that the most effective integrated resources link multiple knowledge categories and align entities to ontology or primary-database identifiers. (santangelo2024integratingbiologicalknowledge pages 3-5, santangelo2024integratingbiologicalknowledge pages 1-2)

The same review identifies KEGG and MetaCyc as mechanistically curated resources linking genes, reactions/pathways, and metabolites. It highlights genome-scale metabolic networks as tools that synthesize an organism’s metabolism and simulate metabolic phenotypes under environmental conditions, while warning that model reconstructions differ according to databases, annotation tools, and reconstruction methods. (santangelo2024integratingbiologicalknowledge pages 3-5)

For TraitMech, this supports use of:

- **GO** for molecular functions, biological processes, and cellular components;
- **ChEBI** for metabolites and chemicals;
- **Rhea**, EC, KEGG, or MetaCyc for reactions/pathways;
- **NCBITaxon** for organisms;
- standardized schemas such as **Biolink Model** and **Relation Ontology** for graph relations.

The review notes that KG-Microbe aligns to Biolink, ingests microbial-trait databases, and combines them with ChEBI and GO; it contrasts this with graphs whose arbitrary edge types reduce interoperability. (santangelo2024integratingbiologicalknowledge pages 12-13)

### 4.3 Real-world implementations

**PheKnowLator**, published in *Scientific Data* in 2024, provides an open-source system for FAIR, ontologically grounded KG construction with customizable representations. It evaluated **12** large-scale KG configurations varying class-versus-instance modeling, standard-versus-inverse relations, and OWL/OWL-NETS abstraction and harmonization. This demonstrates that representation choices materially affect graph construction and should be made explicitly rather than hidden in ad hoc edges. (callahan2024anopensource pages 17-18, callahan2024anopensource pages 1-2)

Callahan and colleagues emphasize that simple graphs often have ad hoc or overloaded edge semantics, decreasing interoperability and making machine inference difficult. That warning is directly relevant here: labeling a relation as “causes” merely because a gene or environment is associated with a material organism would collapse typing, bearer, and causal relations into one ambiguous edge. (callahan2024anopensource pages 2-4)

A 2024 pig-gut implementation constructed the PGMKG by integrating manual reading, PubTator, and structured databases. It used **157 publications**, produced **42,547 nodes and 58,896 triples**, linked microbes to **53 metabolites** and **87 pathways**, and reported that 27 of the 53 metabolites were feed-related (**50.94%**). (zhang2024knowledgegraphderivedfeed pages 1-3, zhang2024knowledgegraphderivedfeed pages 3-4) These figures illustrate the practical value of domain-specific causal/associational graphs, but the study also reports many microbe–feed-efficiency findings as correlations—including significance at *P* < 0.05—so they should not automatically be converted into causal TraitMech edges. (zhang2024knowledgegraphderivedfeed pages 3-4)

## 5. Recommended content for `data/traits/upper/material_entity.yaml`

A conservative record should contain:

1. the supplied identifier, label, definition, category, term kind, and reviewed status;
2. verified upper-ontology parentage;
3. provenance to the BFO foundational sources;
4. a note stating that this is a **bearer class**, not a mechanistic microbial phenotype;
5. only generic schema edges such as `is_a`, `bearer_of`/inverse `inheres_in`, and `participates_in`, where those relations are supported by the project’s imported ontology versions;
6. an explicit exclusion or warning against direct gene/pathway/environment causal edges.

The existing four-node, three-edge `material_entity_bfo_upper_context` graph is therefore directionally appropriate. Expansion should focus on ontology alignment, not biological mechanism count.

## 6. Claims that should not yet be curated

- **No direct gene → material entity edge.** A gene may affect a quality or disposition of a specific organism, but does not cause the upper class.
- **No pathway → material entity edge.** Pathways are processes/modules in which material entities participate.
- **No chemical or nutrient → material entity edge.** Chemicals may be material entities themselves, environmental inputs, or participants in reactions; their relationship to a narrower phenotype must be specified.
- **No environment → material entity edge.** Environment can enable or inhibit realization of a disposition but does not explain membership in the material-entity class.
- **No correlation converted to causation.** Microbe–host, microbe–metabolite, or microbe–feed-efficiency associations require intervention, genetic evidence, biochemical validation, or another defensible causal design.
- **Do not adopt `internally_grounded_in` or `externally_grounded_in` as production predicates yet.** The 2024 paper proposes these as additions and explicitly notes implementation would require a new BFO relation. (rabenberg2024groundingrealizableentities pages 11-13)
- **Do not assign unverified CURIEs.** Label-only nodes are preferable to identifiers inferred from memory.
- **Do not generalize taxon-specific pathogenicity.** The host–pathogen paper stresses that pathogen status can be host-species- or developmental-stage-indexed. (rabenberg2024groundingrealizableentities pages 8-11)

## DOI-first bibliography

1. Otte JN, Beverley J, Ruttenberg A. **BFO: Basic Formal Ontology.** *Applied Ontology.* Published March 2022;17:17–43. DOI: [10.3233/AO-220262](https://doi.org/10.3233/AO-220262).
2. Arp R, Smith B, Spear AD. **Building Ontologies with Basic Formal Ontology.** MIT Press; 2015. DOI: [10.7551/mitpress/9780262527811.001.0001](https://doi.org/10.7551/mitpress/9780262527811.001.0001).
3. Rabenberg M, Benson C, Donato F, et al. **Grounding Realizable Entities.** Published April 2024. DOI: [10.48550/arXiv.2405.00197](https://doi.org/10.48550/arXiv.2405.00197). This is a preprint/formal-ontology contribution; proposed relations require community and release-level confirmation.
4. Santangelo BE, Apgar M, Colorado ASB, et al. **Integrating biological knowledge for mechanistic inference in the host-associated microbiome.** *Frontiers in Microbiology.* Published 4 April 2024;15:1351678. DOI: [10.3389/fmicb.2024.1351678](https://doi.org/10.3389/fmicb.2024.1351678). (santangelo2024integratingbiologicalknowledge pages 1-2)
5. Callahan TJ, Tripodi IJ, Stefanski AL, et al. **An open source knowledge graph ecosystem for the life sciences.** *Scientific Data.* 2024;11:363. DOI: [10.1038/s41597-024-03171-w](https://doi.org/10.1038/s41597-024-03171-w). (callahan2024anopensource pages 1-2)
6. Zhang J, Jiang Q, Du Z, et al. **Knowledge graph-derived feed efficiency analysis via pig gut microbiota.** *Scientific Reports.* Published June 2024;14:13939. DOI: [10.1038/s41598-024-64835-6](https://doi.org/10.1038/s41598-024-64835-6). (zhang2024knowledgegraphderivedfeed pages 1-3)
7. Jackson R, Matentzoglu N, Overton JA, et al. **OBO Foundry in 2021: operationalizing open data principles to evaluate ontologies.** *Database.* 2021:baab069. DOI: [10.1093/database/baab069](https://doi.org/10.1093/database/baab069). Listed as an ontology-standardization foundation in the 2024 microbiome review. (santangelo2024integratingbiologicalknowledge pages 13-14)
8. Bansal P, Morgat A, Axelsen KB, et al. **Rhea, the reaction knowledgebase in 2022.** *Nucleic Acids Research.* 2022;50:D693–D700. DOI: [10.1093/nar/gkab1016](https://doi.org/10.1093/nar/gkab1016). (santangelo2024integratingbiologicalknowledge pages 12-13)

## Final assessment

`METPO:1000186` should remain an **upper-ontology scaffold node**. The scientifically defensible graph records that material entities bear dependent properties and participate in processes. A mechanistic graph becomes meaningful only after selecting a narrower microbial quality, disposition, function, or assay phenotype. Populating this target with generic metabolic or molecular mechanisms would introduce category errors, weaken inference, and conflict with current expert recommendations for semantically typed, ontology-grounded microbiome knowledge graphs.

References

1. (rabenberg2024groundingrealizableentities pages 1-3): Michael Rabenberg, Carter Benson, Federico Donato, Yongqun He, Anthony Huffman, Shane Babcock, and John Beverley. Grounding realizable entities. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2405.00197, doi:10.48550/arxiv.2405.00197. This article has 8 citations.

2. (rabenberg2024groundingrealizableentities pages 3-6): Michael Rabenberg, Carter Benson, Federico Donato, Yongqun He, Anthony Huffman, Shane Babcock, and John Beverley. Grounding realizable entities. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2405.00197, doi:10.48550/arxiv.2405.00197. This article has 8 citations.

3. (rabenberg2024groundingrealizableentities pages 8-11): Michael Rabenberg, Carter Benson, Federico Donato, Yongqun He, Anthony Huffman, Shane Babcock, and John Beverley. Grounding realizable entities. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2405.00197, doi:10.48550/arxiv.2405.00197. This article has 8 citations.

4. (santangelo2024integratingbiologicalknowledge pages 3-5): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

5. (santangelo2024integratingbiologicalknowledge pages 2-3): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

6. (santangelo2024integratingbiologicalknowledge pages 1-2): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

7. (santangelo2024integratingbiologicalknowledge pages 12-13): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

8. (callahan2024anopensource pages 1-2): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 85 citations and is from a peer-reviewed journal.

9. (zhang2024knowledgegraphderivedfeed pages 1-3): Junmei Zhang, Qin Jiang, Zhihong Du, Yilin Geng, Yuren Hu, Qichang Tong, Yunfeng Song, Hong-Yu Zhang, Xianghua Yan, and Zaiwen Feng. Knowledge graph-derived feed efficiency analysis via pig gut microbiota. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-64835-6, doi:10.1038/s41598-024-64835-6. This article has 8 citations and is from a peer-reviewed journal.

10. (zhang2024knowledgegraphderivedfeed pages 3-4): Junmei Zhang, Qin Jiang, Zhihong Du, Yilin Geng, Yuren Hu, Qichang Tong, Yunfeng Song, Hong-Yu Zhang, Xianghua Yan, and Zaiwen Feng. Knowledge graph-derived feed efficiency analysis via pig gut microbiota. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-64835-6, doi:10.1038/s41598-024-64835-6. This article has 8 citations and is from a peer-reviewed journal.

11. (callahan2024anopensource pages 2-4): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 85 citations and is from a peer-reviewed journal.

12. (rabenberg2024groundingrealizableentities pages 11-13): Michael Rabenberg, Carter Benson, Federico Donato, Yongqun He, Anthony Huffman, Shane Babcock, and John Beverley. Grounding realizable entities. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2405.00197, doi:10.48550/arxiv.2405.00197. This article has 8 citations.

13. (callahan2024anopensource pages 17-18): Tiffany J. Callahan, Ignacio J. Tripodi, Adrianne L. Stefanski, Luca Cappelletti, Sanya B. Taneja, Jordan M. Wyrwa, Elena Casiraghi, Nicolas A. Matentzoglu, Justin Reese, Jonathan C. Silverstein, Charles Tapley Hoyt, Richard D. Boyce, Scott A. Malec, Deepak R. Unni, Marcin P. Joachimiak, Peter N. Robinson, Christopher J. Mungall, Emanuele Cavalleri, Tommaso Fontana, Giorgio Valentini, Marco Mesiti, Lucas A. Gillenwater, Brook Santangelo, Nicole A. Vasilevsky, Robert Hoehndorf, Tellen D. Bennett, Patrick B. Ryan, George Hripcsak, Michael G. Kahn, Michael Bada, William A. Baumgartner, and Lawrence E. Hunter. An open source knowledge graph ecosystem for the life sciences. Scientific Data, Apr 2024. URL: https://doi.org/10.1038/s41597-024-03171-w, doi:10.1038/s41597-024-03171-w. This article has 85 citations and is from a peer-reviewed journal.

14. (santangelo2024integratingbiologicalknowledge pages 13-14): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.