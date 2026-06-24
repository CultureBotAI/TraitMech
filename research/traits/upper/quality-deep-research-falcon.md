---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:55:16.848019'
end_time: '2026-06-18T13:16:05.754965'
duration_seconds: 1248.91
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: quality
  trait_identifier: METPO:1000188
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: quality
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A characteristic of an entity that depends on the entity's existence,
    size, color, and physiological traits.
  parent_traits: ''
  synonyms: ''
  evidence_summary: 'DOI:10.1186/gb-2010-11-1-r2: ontology of qualities termed Phenotype
    and Trait ontology (Supports quality as an upper class used to construct phenotype
    descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality
    of that entity (Supports qualities as entity-dependent phenotype descriptors.)'
  causal_graph_summary: 'quality_upper_child_context: 4 nodes, 3 edges'
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
- **Trait label:** quality
- **METPO identifier:** METPO:1000188
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A characteristic of an entity that depends on the entity's existence, size, color, and physiological traits.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: ontology of qualities termed Phenotype and Trait ontology (Supports quality as an upper class used to construct phenotype descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity (Supports qualities as entity-dependent phenotype descriptors.)
- **Existing causal graph summary:** quality_upper_child_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **quality** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/quality.yaml`.

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
- **Trait label:** quality
- **METPO identifier:** METPO:1000188
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A characteristic of an entity that depends on the entity's existence, size, color, and physiological traits.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: ontology of qualities termed Phenotype and Trait ontology (Supports quality as an upper class used to construct phenotype descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity (Supports qualities as entity-dependent phenotype descriptors.)
- **Existing causal graph summary:** quality_upper_child_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **quality** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/quality.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **quality** (METPO:1000188)

### Executive scope summary
In ontology-driven phenotype modeling, **quality** is not a specific microbial phenotype (e.g., “motility” or “biofilm formation”), but an **upper-level attribute/characteristic** used to *construct* phenotype descriptions. The dominant formalism is the Entity–Quality (**EQ**) model, where a phenotype is represented as an **entity (E)** (e.g., a cell part, process, function, or chemical response) that **bears** a **quality (Q)** (e.g., increased size, decreased motility, sensitivity). In this framework, *qualities are typically drawn from PATO* and are linked to entities via Relations Ontology (RO) relations such as **inheres_in/characteristic_of**, with additional qualifiers for relational direction (“toward”), time (“during”), and reference comparisons (“altered_relative_to”). (matentzoglu2025theunifiedphenotype pages 5-6, gkoutos2018theanatomyof pages 5-6, gkoutos2012ontologybasedcrossspeciesintegration pages 3-5)

For **microbial phenotypes**, the Ontology of Microbial Phenotypes (OMP) explicitly builds microbial phenotype classes using PATO qualities—including **process quality** for phenotypes that inhere in **processes** (e.g., decreased motility)—and uses patterns that distinguish **independent** observations from **dependent/comparative** phenotypes that must specify a reference genotype/environment (“altered_relative_to”). (chibucos2014anontologyfor pages 2-5, chibucos2014anontologyfor pages 5-6)

A central boundary for curation is therefore:
- **Quality (upper class)**: an attribute/characteristic (Q) used in phenotype composition.
- **Trait/attribute vs phenotype value/state**: traits are general properties; phenotypes are values of traits (operational distinction highlighted in corpus work). (nedellec2024taecamanually pages 1-4)

### 1) Trait scope and boundary cases (curation guidance)

#### What “quality” represents in TraitMech
**Recommended interpretation for METPO:1000188 (UPPER/CLASS):**
- A schema-level node representing the *Q-component* of EQ phenotype descriptions: “a characteristic/attribute that inheres in some bearer entity” (entity may be continuant or process depending on modeling). (matentzoglu2025theunifiedphenotype pages 5-6, gkoutos2018theanatomyof pages 5-6, chibucos2014anontologyfor pages 2-5)

#### Boundary cases / nearby concepts
1. **Phenotype term vs quality term**: Phenotype classes are *composites* (E+Q), while “quality” is the reusable building block (Q) used across many phenotypes. (gkoutos2018theanatomyof pages 5-6, thessen2020transformingthestudy pages 8-11)
2. **Process quality**: PATO includes “process quality” for qualities inhering in processes; critical for microbial phenotypes like motility, chemotaxis, stress responses. (chibucos2014anontologyfor pages 2-5)
3. **Relational qualities**: Some qualities are **relational** and directed toward another entity (e.g., “sensitivity toward oxygen”). These are not purely unary descriptors like “size”. (gkoutos2018theanatomyof pages 5-6)
4. **Comparative/dependent phenotypes**: Many microbial phenotypes are only meaningful relative to a reference (wild type, parent strain, control environment); OMP encodes this with **altered_relative_to** and emphasizes that a phenotype statement may depend on a genotype/environment pairing. (chibucos2014anontologyfor pages 5-6)

### 2) Candidate causal-graph nodes (grouped by type)

Because **quality** is upper-level, the most curation-ready nodes are *design-pattern nodes* (schema) plus *exemplar biological nodes* demonstrating how mechanistic determinants connect to quality-bearing phenotypes.

#### A. Core trait/modeling nodes (ontology schema)
- **quality** (METPO:1000188) – focal upper-class.
- **PATO quality** (label-only; PATO:0000001 is referenced as a general quality class in EQ patterns in phenotype-ontology practice) (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5)
- **process quality** (PATO:0001236; label+ID explicitly cited) (chibucos2014anontologyfor pages 2-5)
- **relational quality** (PATO; label-only; unary vs relational noted) (gkoutos2018theanatomyof pages 5-6)
- **scalar quality** vs **non-scalar quality** (PATO; label-only) (gkoutos2018theanatomyof pages 5-6)

#### B. Key relations / predicates (ontology grounding)
- RO:0000052 **characteristic_of** (used in uPheno EQ patterns) (matentzoglu2025theunifiedphenotype pages 5-6)
- RO:0002314 **characteristic_of part of** (uPheno pattern) (matentzoglu2025theunifiedphenotype pages 5-6)
- RO **inheres_in** (used widely in EQ definitions; explicit in APO/OMP patterns) (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5, chibucos2014anontologyfor pages 5-6)
- RO:0000086 **has_quality** (explicit in OMP EQ modeling) (chibucos2014anontologyfor pages 5-6)
- RO **toward** (for directed relational qualities, e.g., sensitivity toward oxygen) (gkoutos2018theanatomyof pages 5-6)
- RO **during** (temporal/context qualifiers in phenotype terms) (matentzoglu2025theunifiedphenotype pages 4-5)
- OMP qualifier **altered_relative_to** (comparative phenotype reference pattern) (chibucos2014anontologyfor pages 2-5)
- BFO **has part** (used in OWL phenotype patterns) (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5)

#### C. Environmental/assay/condition context nodes
- **Microbial Conditions Ontology (MCO)** (label-only; used in RegulonDB and prior work to capture minimal reproducible condition descriptors) (santoszavaleta2019regulondbv10.5 pages 4-5)
- MCO condition elements (as curated fields): **Medium**, **supplements**, **aeration**, **temperature**, **pH**, **optical density**, **growth phase**, **growth rate** (santoszavaleta2019regulondbv10.5 pages 4-5)
- Missing phenotype metadata categories highlighted in microbial phenome integration work: **isolation**, **sampling**, **environment**, **culture/growth**, **safety**, **physiology/metabolism** information (liu2023mycobacteriaceaephenomeatlas pages 1-2)

#### D. Exemplar microbial phenotype entities (E side; grounding often GO/ChEBI/OMP)
- GO:0048870 **cell motility** (entity used in OMP EQ example) (chibucos2014anontologyfor pages 5-6)
- **chemotaxis** / **positive chemotaxis** (entity in OMP assay example; label-only grounding) (chibucos2014anontologyfor pages 5-6)
- GO:0009408 **response to heat** (yeast example entity for sensitivity phenotype) (gkoutos2012ontologybasedcrossspeciesintegration pages 5-8)
- GO:0042221 **response to chemical stimulus** (entity used with sensitivity toward NaCl) (gkoutos2012ontologybasedcrossspeciesintegration pages 5-8)
- CHEBI:26710 **sodium chloride** (toward target in ionic stress example) (gkoutos2012ontologybasedcrossspeciesintegration pages 5-8)
- CHEBI oxygen (label-only; used in sensitivity-toward example) (gkoutos2018theanatomyof pages 5-6)

#### E. Exemplar mechanistic determinant nodes (genes/pathways/modules)
(These demonstrate how causal edges can connect mechanism → phenotype (E+Q))
- **Cra** (catabolite repressor/activator) regulatory factor; **CRP** (cAMP receptor protein) (santoszavaleta2019regulondbv10.5 pages 4-5)
- Central carbon metabolism pathways: **TCA cycle**, **glyoxylate cycle**, **glycolysis** (KEGG-enriched condition-specific regulation) (santoszavaleta2019regulondbv10.5 pages 4-5)
- Mycobacteriaceae mechanisms/paths from MPA: **ESX-3 type VII secretion system**, **ESX-5 secretion system**, **nitrate reductase**, **sulfur metabolism pathway**, **protein export pathway**, **amino acid biosynthesis**; **drug-resistance mutations in 20 genes/intergenic regions (74 mutation types)** (liu2023mycobacteriaceaephenomeatlas pages 12-14)

### 3) Current understanding and recent developments (emphasis 2023–2024)

#### 3.1 Current understanding (definitions and modeling)
- Phenotype ontologies widely implement EQ: phenotype descriptions are formed by pairing an **entity** with a **quality** (Q from PATO), and PATO further organizes qualities as attributes/values, scalar/non-scalar, unary/relational—important when modeling microbial “tolerance/sensitivity” and “increase/decrease” outcomes. (gkoutos2018theanatomyof pages 5-6, gkoutos2018theanatomyof pages 6-7)
- In microbial phenotype ontologies, OMP uses EQ and emphasizes comparative context: the same assay can support an independent observation in a parent strain and a dependent phenotype (e.g., “chemotaxis deficient mutant” measured as decreased swim diameter) where the decreased quality is relative to a specified genotype/environment. (chibucos2014anontologyfor pages 5-6)

#### 3.2 2023–2024 developments relevant to curating ‘quality’ graphs
- **RegulonDB v12.0 (2024)**: continued modernization and explicitly reports integrating the **Microbial Conditions Ontology (MCO)** in the interface so curators can annotate conditions, supporting FAIR integration of regulatory and condition-dependent biology. (liu2023mycobacteriaceaephenomeatlas pages 1-2)
- **Mycobacteriaceae Phenome Atlas (MPA, 2023)**: large-scale phenome integration (10,755 strains) and pathway enrichment analyses; it highlights a key curatorial gap: missing data elements such as isolation/environment/culture conditions in microbial phenotype standards, directly relevant when interpreting qualities as environment-dependent. (liu2023mycobacteriaceaephenomeatlas pages 2-5, liu2023mycobacteriaceaephenomeatlas pages 1-2)
- **Trait vs phenotype value operationalization (2024)**: in trait/phenotype text-mining, traits are framed as observable characteristics while phenotypes are values of traits. This reinforces that “quality” aligns with attribute-like descriptors rather than full phenotype observations. (nedellec2024taecamanually pages 1-4)

### 4) Current applications and real-world implementations

1. **Microbial gene regulation knowledgebases and reproducible context annotation**: RegulonDB uses MCO to curate growth/experiment conditions alongside transcriptional regulation, enabling cross-condition comparison and integrative analysis. (santoszavaleta2019regulondbv10.5 pages 4-5, liu2023mycobacteriaceaephenomeatlas pages 1-2)
2. **Microbial phenome atlas/knowledge integration**: MPA demonstrates large-scale phenotype aggregation and downstream analyses (topological data analysis, Fisher’s exact tests for pathway enrichment) as a practical phenomics implementation for a microbial clade. (liu2023mycobacteriaceaephenomeatlas pages 2-5, liu2023mycobacteriaceaephenomeatlas pages 1-2)
3. **Ontology-based phenotype representation infrastructure (OMP)**: OMP provides a mechanism to store genotype/environment/evidence-linked phenotype annotations using EQ patterns; this is a direct substrate for building TraitMech causal graphs that connect molecular entities to phenotype qualities. (chibucos2014anontologyfor pages 5-6, chibucos2014anontologyfor pages 2-5)

### 5) Relevant statistics and data (recent studies)

- **MPA scale (2023)**: curated phenotypic data for **10,755 strains** across **236 species and 18 subspecies** of Mycobacteriaceae; **10,595** genome records downloaded; after QC, **10,164** genome records retained; **380 MAGs** collected with **86 retained** after dereplication; final set included **10,158 genomes and 31 MAGs**. (liu2023mycobacteriaceaephenomeatlas pages 2-5)
- **MPA phenotypic trait set (2023)**: recruited **82 microbial phenotypic traits**, organized into five polyphasic categories (20 subcategories) and three functional categories (eight subcategories). (liu2023mycobacteriaceaephenomeatlas pages 1-2)
- **MPA pathway analysis (2023)**: identified **260 potential pathogen-enriched pathways** by Fisher’s exact test. (liu2023mycobacteriaceaephenomeatlas pages 1-2)
- **RegulonDB condition-dependent regulation (2019, still operationally important)**: Cra regulation expanded from **79** classically reported genes to **338 additional** regulated genes detected under different carbon sources (fructose/glucose/acetate), highlighting that observed qualities often depend on the experimental condition. (santoszavaleta2019regulondbv10.5 pages 4-5)

### 6) Candidate causal edges (curation table)
The following table focuses on curation-ready edges for a TraitMech graph rooted at **quality**, combining (i) schema-level EQ modeling edges and (ii) exemplar mechanistic edges that yield quality-bearing phenotypes.

| Edge (subject–predicate–object) | Example instantiation | Evidence source (with DOI, year) | Supporting snippet (verbatim/near-verbatim) | Notes for curation |
|---|---|---|---|---|
| quality — characteristic_of / inheres_in — entity | increased size — characteristic_of — heart | Matentzoglu et al., *Genetics* (doi:10.1093/genetics/iyaf027, 2025) | “qualities are the ‘Q’ component… Phenotypes are modeled as an entity (E) that bears a quality (Q) (example: in ‘enlarged heart’, the heart bears the quality ‘increased size’)” (matentzoglu2025theunifiedphenotype pages 5-6) | Strong ontology-pattern edge for upper-class modeling. Suggested grounding: PATO quality class + RO:0000052 characteristic of. For METPO:1000188, curate as abstract design-pattern edge, not a biological mechanism edge. |
| quality — inheres_in — entity | morphology — inheres_in — cell motility feature / cellular structure | Gkoutos & Hoehndorf, *J Biomed Semantics* (doi:10.1186/2041-1480-3-s2-s6, 2012) | “an EQ definition is expressed as intersection_of: PATO:<quality> and intersection_of: inheres_in GO:<entity>” (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5) | Strong. Canonical EQ relation. Suggested grounding: RO:inheres in; entity from GO/UBERON/cell ontology analogs. Scope: ontology construction, not direct wet-lab causation. |
| process quality — inheres_in — process | decreased motility quality — inheres_in — cell motility | Chibucos et al., *BMC Microbiology* (doi:10.1186/s12866-014-0294-3, 2014) | “PATO provides phenotypic ‘qualities’… and explicitly defines ‘process quality’ (PATO:0001236) as ‘a quality which inheres in a process’” (chibucos2014anontologyfor pages 2-5) | Strong. Important for microbial phenotypes involving motility, growth, sporulation, secretion. Suggested grounding: PATO:0001236 process quality; GO process terms. |
| relational quality — toward — environmental entity | sensitivity toward oxygen — toward — oxygen | Gkoutos et al., *Brief Bioinform* (doi:10.1093/bib/bbx035, 2018) | “A microbial example given is ‘sensitivity toward oxygen’ modeled as a relational quality directed toward oxygen” (gkoutos2018theanatomyof pages 5-6) | Strong but relational. Suggested grounding: PATO relational quality + RO:towards + CHEBI:15379 oxygen. Useful template for tolerance/sensitivity traits. |
| phenotype term — equivalent_to — has_part some (entity and has_quality some quality) | phenotype term ‘abnormal femur length’ — equivalent_to — has_part some (femur and has_quality some decreased length) | Thessen et al., *PLoS Comput Biol* (doi:10.1371/journal.pcbi.1008376, 2020) | “[(decreased length and (inheres in some femur) and (has modifier some abnormal))]” and EQ classes “may be precomposed or post-composed” (thessen2020transformingthestudy pages 11-12) | Strong pattern edge. Suggested grounding: BFO has part, RO inheres in, PATO decreased length, anatomy/process entity ontology. Abstract OWL equivalence edge, not biological causation. |
| phenotype term — phenotype_of — has_part some (GO process and has_quality some quality) | decreased cell motility phenotype — phenotype_of — has_part some (GO:cell motility and has_quality some decreased) | Gkoutos & Hoehndorf, *J Biomed Semantics* (doi:10.1186/2041-1480-3-s2-s6, 2012) | “EquivalentTo: phenotype-of some (has-part some (GO:... and has-quality some PATO:...))” (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5) | Strong. Good candidate abstract edge for microbial process phenotypes. Suggested grounding: GO process + PATO + BFO has part. |
| phenotype term — has_part — part_of some process | budding-stage process phenotype — has_part — part_of some GO process | Gkoutos & Hoehndorf, *J Biomed Semantics* (doi:10.1186/2041-1480-3-s2-s6, 2012) | “Process-based phenotypes use part-of patterns: phenotype-of some (has-part some (part-of some GO:... and has-quality some PATO:...))” (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5) | Strong but modeling-specific. Suggested grounding: BFO has part; BFO/RO part of. Note authors “avoid using participates-in.” |
| phenotype quality — altered_relative_to — reference state | increased biofilm formation — altered_relative_to — wild-type/control genotype | Chibucos et al., *BMC Microbiology* (doi:10.1186/s12866-014-0294-3, 2014) | “dependent terms use a qualifier ‘altered_relative_to’ rather than ‘abnormal’, with the reference specified (e.g., control genotype or wild-type)” (chibucos2014anontologyfor pages 2-5) | Strong for dependent microbial phenotypes. Suggested grounding: OMP dependent phenotype pattern; reference may be genotype, strain, or condition. Important to avoid decontextualized ‘abnormal’. |
| phenotype term — during — temporal context | decreased cellular component number phenotype — during — vegetative growth | Matentzoglu et al., *Genetics* (doi:10.1093/genetics/iyaf027, 2025) | “the FYPO example explicitly includes condition/context text ‘during vegetative growth,’ showing that temporal/assay/context qualifiers are represented” (matentzoglu2025theunifiedphenotype pages 4-5) | Strong for context-qualified phenotype classes. Suggested grounding: RO:during + GO biological phase/process when possible. Context-sensitive; avoid overgeneralization across taxa. |
| phenotype statement — requires_context_from — assay/condition ontology | microbial phenotype annotation — requires_context_from — Microbial Conditions Ontology (MCO) | Santos-Zavaleta et al., *Nucleic Acids Res* (doi:10.1093/nar/gkad1072, 2024) | “The interface has integrated the Microbial Conditions Ontology (MCO) so curators use …” (liu2023mycobacteriaceaephenomeatlas pages 1-2) | Moderate-to-strong implementation edge. Useful curation reminder that quality/phenotype assertions need experimental-context metadata. Suggested grounding: MCO terms; possibly OBI for assays. |
| experiment description — uses_controlled_vocabulary_from — MCO | RNA-seq/condition metadata — uses_controlled_vocabulary_from — MCO | Santos-Zavaleta et al., *Nucleic Acids Res* (doi:10.1093/nar/gkad1072, 2024) and Santos-Zavaleta et al., *Nucleic Acids Res* (doi:10.1093/nar/gky1077, 2019) | “The interface has integrated the Microbial Conditions Ontology (MCO)” and earlier “We developed the Microbial Conditions Ontology with a controlled vocabulary for the minimal properties to reproduce an experiment” (liu2023mycobacteriaceaephenomeatlas pages 1-2) | Strong for metadata edges, though second wording is from earlier source summary. Curation use: link phenotype assertions to reproducible condition descriptors. |
| microbial phenotype resource — lacks_metadata_for — environmental/culture/growth information | OMP-aligned phenotype data element set — lacks_metadata_for — isolation/sampling/environment/culture-growth/safety/physiology info | Liu et al., *Phenomics* (doi:10.1007/s43657-023-00101-5, 2023) | “common data elements—‘isolation information, sampling information, environmental information, culture and growth information, safety information, and physiology and metabolism information’—are missing” (liu2023mycobacteriaceaephenomeatlas pages 1-2) | Moderate. This is a gap/needs edge rather than a biological causal edge. Useful warning for TraitMech: do not curate phenotype qualities without surrounding metadata where needed. |
| trait/phenotype corpus — distinguishes — trait vs phenotype value | disease resistance trait — distinguishes — highly resistant phenotype value | Nédellec et al., *PLOS ONE* (doi:10.1371/journal.pone.0305475, 2024) | “traits… e.g., plant height or disease resistance” versus “phenotypes defined as values of those traits” (nedellec2024taecamanually pages 1-4) | Moderate conceptual edge. Helpful boundary case: ‘quality’ is closer to attribute/trait side than to observed value/state. Scope limitation: plant text-mining source, not microbial-specific. |
| quality term — may_be_scalar_or_nonscalar — quality subtype | size — may_be_scalar_or_nonscalar — scalar quality; color — may_be_scalar_or_nonscalar — non-scalar quality | Gkoutos et al., *Brief Bioinform* (doi:10.1093/bib/bbx035, 2018) | “The ontology distinguishes scalar attributes… from non-scalar” (gkoutos2018theanatomyof pages 5-6) | Strong for upper-level organization of quality subclasses. Suggested grounding: PATO attribute hierarchy. Not a causal biological edge; curate only if TraitMech supports schema/context edges. |
| quality term — may_be_unary_or_relational — quality subtype | cell shape — may_be_unary_or_relational — unary; sensitivity toward oxygen — may_be_unary_or_relational — relational | Gkoutos et al., *Brief Bioinform* (doi:10.1093/bib/bbx035, 2018) | “PATO also separates unary qualities… from relational qualities” (gkoutos2018theanatomyof pages 5-6) | Strong ontology-organization edge. Important for modeling microbial environmental-response qualities. Suggested grounding: PATO slim/annotation categories where available. |
| comparative phenotype inference — derived_from — direct observations plus reference comparison | increased growth phenotype — derived_from — pair/set of observations under case vs control | Gkoutos et al., *Brief Bioinform* (doi:10.1093/bib/bbx035, 2018) | “Phenotype ontologies distinguish direct observations… from comparative statements derived by comparing a case to a control” (gkoutos2018theanatomyof pages 6-7) | Moderate. This is inference/provenance, not entity biology. Helpful warning to keep observed quality separate from computed comparative phenotype. |
| phenotype knowledgebase inference — implies_presence_of — bearer entity | count of dorsal fin rays phenotype — implies_presence_of — dorsal fin | Duque et al., *Biodiversity Information Science and Standards* (doi:10.3897/biss.8.115232, 2024) | “a reported count of supporting rays in a dorsal fin implies, by inference, the presence of a dorsal fin” (duque2024meetingreportfor pages 1-3) | Moderate analogical pattern. Useful for reasoning over quality-bearing entities. Scope limitation: non-microbial comparative morphology example; should be flagged uncertain if adapted directly to microbes. |
| quality assertion — should_be_linked_to — figure/schema support | EQ phenotype statement — should_be_linked_to — Figure 3 EQ formalism diagram | Thessen et al., *PLoS Comput Biol* (doi:10.1371/journal.pcbi.1008376, 2020) | “Figure 3… explains the Entity–Quality (EQ) Formalism… combining ontology terms from an anatomy ontology (Entity)… and a trait ontology (Quality)” (thessen2020transformingthestudy media 04915a38) | Supportive documentation edge for curation provenance. Not a graph edge for final YAML unless schema/provenance nodes are allowed. |


*Table: This table compiles curation-ready candidate edges for representing the upper-level trait 'quality' in microbial phenotype modeling. It emphasizes ontology-safe EQ design patterns, contextual qualifiers, and metadata requirements that should guide TraitMech curation.*

### 7) Visual evidence (EQ modeling)
Figure evidence for EQ’s conceptual structure (entity + quality and mapping to Character/Character State) is available in Thessen et al. (2020), Figure 3. (thessen2020transformingthestudy media 04915a38)

### 8) Bibliography (DOI-first; includes URLs and publication dates where available)

**Core sources for quality/EQ and microbial phenotype modeling**
- Chibucos MC et al. *An ontology for microbial phenotypes.* **BMC Microbiology**. **2014-11**. DOI: **10.1186/s12866-014-0294-3**. URL: https://doi.org/10.1186/s12866-014-0294-3 (chibucos2014anontologyfor pages 2-5, chibucos2014anontologyfor pages 5-6)
- Gkoutos GV, Schofield PN, Hoehndorf R. *The anatomy of phenotype ontologies: principles, properties and applications.* **Briefings in Bioinformatics**. **2018-04**. DOI: **10.1093/bib/bbx035**. URL: https://doi.org/10.1093/bib/bbx035 (gkoutos2018theanatomyof pages 5-6, gkoutos2018theanatomyof pages 6-7)
- Gkoutos GV, Hoehndorf R. *Ontology-based cross-species integration and analysis of Saccharomyces cerevisiae phenotypes.* **Journal of Biomedical Semantics**. **2012-09**. DOI: **10.1186/2041-1480-3-s2-s6**. URL: https://doi.org/10.1186/2041-1480-3-s2-s6 (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5, gkoutos2012ontologybasedcrossspeciesintegration pages 5-8)
- Matentzoglu N et al. *The Unified Phenotype Ontology: a framework for cross-species integrative phenomics.* **Genetics**. **2025-03**. DOI: **10.1093/genetics/iyaf027**. URL: https://doi.org/10.1093/genetics/iyaf027 (matentzoglu2025theunifiedphenotype pages 5-6, matentzoglu2025theunifiedphenotype pages 4-5)
- Thessen AE et al. *Transforming the study of organisms: Phenomic data models and knowledge bases.* **PLoS Computational Biology**. **2020-11**. DOI: **10.1371/journal.pcbi.1008376**. URL: https://doi.org/10.1371/journal.pcbi.1008376 (thessen2020transformingthestudy pages 8-11, thessen2020transformingthestudy media 04915a38)

**Recent developments / implementations (prioritize 2023–2024)**
- Salgado H et al. *RegulonDB v12.0: a comprehensive resource of transcriptional regulation in E. coli K-12.* **Nucleic Acids Research**. **2024-11**. DOI: **10.1093/nar/gkad1072**. URL: https://doi.org/10.1093/nar/gkad1072 (liu2023mycobacteriaceaephenomeatlas pages 1-2)
- Liu W et al. *Mycobacteriaceae Phenome Atlas (MPA): a standardized atlas for the Mycobacteriaceae phenome based on heterogeneous sources.* **Phenomics**. **2023-06**. DOI: **10.1007/s43657-023-00101-5**. URL: https://doi.org/10.1007/s43657-023-00101-5 (liu2023mycobacteriaceaephenomeatlas pages 1-2, liu2023mycobacteriaceaephenomeatlas pages 2-5, liu2023mycobacteriaceaephenomeatlas pages 12-14)
- N’edellec C et al. *TaeC: A manually annotated text dataset for trait and phenotype extraction and entity linking in wheat breeding literature.* **PLOS ONE**. **2024-06**. DOI: **10.1371/journal.pone.0305475**. URL: https://doi.org/10.1371/journal.pone.0305475 (nedellec2024taecamanually pages 1-4)

**Condition-dependent regulation and conditions ontology (important supporting evidence)**
- Santos-Zavaleta A et al. *RegulonDB v10.5…* **Nucleic Acids Research**. **2019-11**. DOI: **10.1093/nar/gky1077**. URL: https://doi.org/10.1093/nar/gky1077 (santoszavaleta2019regulondbv10.5 pages 4-5)

### 9) Warnings / “do not curate yet” items

1. **Do not treat “quality” as a microbial mechanism**: As an upper-class, “quality” is a modeling construct; mechanistic curation should target specific qualities (e.g., decreased motility, sensitivity to NaCl) *and* their bearers (GO processes, structures) rather than the abstract class itself. (matentzoglu2025theunifiedphenotype pages 5-6, thessen2020transformingthestudy pages 8-11)
2. **Separate observed qualities from inferred comparative phenotypes**: Some phenotype qualities are derived by comparing case/control or by statistical inference; this provenance is typically not captured by PATO alone and may require separate evidence/provenance models. (gkoutos2018theanatomyof pages 6-7)
3. **Comparative/dependent phenotypes require reference context**: OMP emphasizes genotype/environment pairing and altered_relative_to; curating dependent phenotypes without specifying the reference can create incorrect mechanistic edges. (chibucos2014anontologyfor pages 5-6)
4. **Environmental/experimental context is often missing but critical**: MPA explicitly notes missing common data elements (isolation/environment/culture/growth/safety/physiology) in microbial phenotype standards; edges that imply general causality across conditions should be flagged uncertain unless the condition is modeled (e.g., with MCO). (liu2023mycobacteriaceaephenomeatlas pages 1-2, santoszavaleta2019regulondbv10.5 pages 4-5)

---

### Suggested curation outcome for `data/traits/upper/quality.yaml`
Curate **quality** primarily as a *schema/upper node* that supports building downstream phenotype traits using EQ patterns, with strong links to:
- PATO quality space (including process quality)
- RO relations for bearer linkage (characteristic_of/inheres_in), direction (toward), time (during), and comparative reference (altered_relative_to)
- Context ontologies (MCO) for reproducible microbial experimental conditions

Mechanistic gene→phenotype edges should generally be curated under *specific lower-level phenotype traits* (e.g., motility, antibiotic resistance, virulence), using **quality** only as the upper scaffolding.


References

1. (matentzoglu2025theunifiedphenotype pages 5-6): Nicolas Matentzoglu, Susan M Bello, Ray Stefancsik, Sarah M Alghamdi, Anna V Anagnostopoulos, James P Balhoff, Meghan A Balk, Yvonne M Bradford, Yasemin Bridges, Tiffany J Callahan, Harry Caufield, Alayne Cuzick, Leigh C Carmody, Anita R Caron, Vinicius de Souza, Stacia R Engel, Petra Fey, Malcolm Fisher, Sarah Gehrke, Christian Grove, Peter Hansen, Nomi L Harris, Midori A Harris, Laura Harris, Arwa Ibrahim, Julius O B Jacobsen, Sebastian Köhler, Julie A McMurry, Violeta Munoz-Fuentes, Monica C Munoz-Torres, Helen Parkinson, Zoë M Pendlington, Clare Pilgrim, Sofia M C Robb, Peter N Robinson, James Seager, Erik Segerdell, Damian Smedley, Elliot Sollis, Sabrina Toro, Nicole Vasilevsky, Valerie Wood, Melissa A Haendel, Christopher J Mungall, James A McLaughlin, and David Osumi-Sutherland. The unified phenotype ontology : a framework for cross-species integrative phenomics. Genetics, Mar 2025. URL: https://doi.org/10.1093/genetics/iyaf027, doi:10.1093/genetics/iyaf027. This article has 17 citations and is from a domain leading peer-reviewed journal.

2. (gkoutos2018theanatomyof pages 5-6): Georgios V Gkoutos, Paul N Schofield, and Robert Hoehndorf. The anatomy of phenotype ontologies: principles, properties and applications. Briefings in Bioinformatics, 19:1008-1021, Apr 2018. URL: https://doi.org/10.1093/bib/bbx035, doi:10.1093/bib/bbx035. This article has 140 citations and is from a domain leading peer-reviewed journal.

3. (gkoutos2012ontologybasedcrossspeciesintegration pages 3-5): Georgios V Gkoutos and Robert Hoehndorf. Ontology-based cross-species integration and analysis of saccharomyces cerevisiae phenotypes. Journal of Biomedical Semantics, 3:S6-S6, Sep 2012. URL: https://doi.org/10.1186/2041-1480-3-s2-s6, doi:10.1186/2041-1480-3-s2-s6. This article has 9 citations and is from a peer-reviewed journal.

4. (chibucos2014anontologyfor pages 2-5): Marcus C Chibucos, Adrienne E Zweifel, Jonathan C Herrera, William Meza, Shabnam Eslamfam, Peter Uetz, Deborah A Siegele, James C Hu, and Michelle G Giglio. An ontology for microbial phenotypes. BMC Microbiology, Nov 2014. URL: https://doi.org/10.1186/s12866-014-0294-3, doi:10.1186/s12866-014-0294-3. This article has 54 citations and is from a peer-reviewed journal.

5. (chibucos2014anontologyfor pages 5-6): Marcus C Chibucos, Adrienne E Zweifel, Jonathan C Herrera, William Meza, Shabnam Eslamfam, Peter Uetz, Deborah A Siegele, James C Hu, and Michelle G Giglio. An ontology for microbial phenotypes. BMC Microbiology, Nov 2014. URL: https://doi.org/10.1186/s12866-014-0294-3, doi:10.1186/s12866-014-0294-3. This article has 54 citations and is from a peer-reviewed journal.

6. (nedellec2024taecamanually pages 1-4): Claire N'edellec, Clara Sauvion, Robert Bossy, Mariya Borovikova, and Louise Del'eger. Taec: a manually annotated text dataset for trait and phenotype extraction and entity linking in wheat breeding literature. Jun 2024. URL: https://doi.org/10.1371/journal.pone.0305475, doi:10.1371/journal.pone.0305475. This article has 6 citations and is from a peer-reviewed journal.

7. (thessen2020transformingthestudy pages 8-11): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (matentzoglu2025theunifiedphenotype pages 4-5): Nicolas Matentzoglu, Susan M Bello, Ray Stefancsik, Sarah M Alghamdi, Anna V Anagnostopoulos, James P Balhoff, Meghan A Balk, Yvonne M Bradford, Yasemin Bridges, Tiffany J Callahan, Harry Caufield, Alayne Cuzick, Leigh C Carmody, Anita R Caron, Vinicius de Souza, Stacia R Engel, Petra Fey, Malcolm Fisher, Sarah Gehrke, Christian Grove, Peter Hansen, Nomi L Harris, Midori A Harris, Laura Harris, Arwa Ibrahim, Julius O B Jacobsen, Sebastian Köhler, Julie A McMurry, Violeta Munoz-Fuentes, Monica C Munoz-Torres, Helen Parkinson, Zoë M Pendlington, Clare Pilgrim, Sofia M C Robb, Peter N Robinson, James Seager, Erik Segerdell, Damian Smedley, Elliot Sollis, Sabrina Toro, Nicole Vasilevsky, Valerie Wood, Melissa A Haendel, Christopher J Mungall, James A McLaughlin, and David Osumi-Sutherland. The unified phenotype ontology : a framework for cross-species integrative phenomics. Genetics, Mar 2025. URL: https://doi.org/10.1093/genetics/iyaf027, doi:10.1093/genetics/iyaf027. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (santoszavaleta2019regulondbv10.5 pages 4-5): Alberto Santos-Zavaleta, Heladia Salgado, Socorro Gama-Castro, Mishael Sánchez-Pérez, Laura Gómez-Romero, Daniela Ledezma-Tejeida, Jair Santiago García-Sotelo, Kevin Alquicira-Hernández, Luis José Muñiz-Rascado, Pablo Peña-Loredo, Cecilia Ishida-Gutiérrez, David A Velázquez-Ramírez, Víctor Del Moral-Chávez, César Bonavides-Martínez, Carlos-Francisco Méndez-Cruz, James Galagan, and Julio Collado-Vides. Regulondb v 10.5: tackling challenges to unify classic and high throughput knowledge of gene regulation in e. coli k-12. Nucleic Acids Research, 47:D212-D220, Nov 2019. URL: https://doi.org/10.1093/nar/gky1077, doi:10.1093/nar/gky1077. This article has 441 citations and is from a highest quality peer-reviewed journal.

10. (liu2023mycobacteriaceaephenomeatlas pages 1-2): Wangdao Liu, H. Cen, Zhile Wu, Haokui Zhou, Shuo Chen, Xilan Yang, Guoping Zhao, and Guoqing Zhang. Mycobacteriaceae phenome atlas (mpa): a standardized atlas for the mycobacteriaceae phenome based on heterogeneous sources. Phenomics, 3:439-456, Jun 2023. URL: https://doi.org/10.1007/s43657-023-00101-5, doi:10.1007/s43657-023-00101-5. This article has 6 citations.

11. (gkoutos2012ontologybasedcrossspeciesintegration pages 5-8): Georgios V Gkoutos and Robert Hoehndorf. Ontology-based cross-species integration and analysis of saccharomyces cerevisiae phenotypes. Journal of Biomedical Semantics, 3:S6-S6, Sep 2012. URL: https://doi.org/10.1186/2041-1480-3-s2-s6, doi:10.1186/2041-1480-3-s2-s6. This article has 9 citations and is from a peer-reviewed journal.

12. (liu2023mycobacteriaceaephenomeatlas pages 12-14): Wangdao Liu, H. Cen, Zhile Wu, Haokui Zhou, Shuo Chen, Xilan Yang, Guoping Zhao, and Guoqing Zhang. Mycobacteriaceae phenome atlas (mpa): a standardized atlas for the mycobacteriaceae phenome based on heterogeneous sources. Phenomics, 3:439-456, Jun 2023. URL: https://doi.org/10.1007/s43657-023-00101-5, doi:10.1007/s43657-023-00101-5. This article has 6 citations.

13. (gkoutos2018theanatomyof pages 6-7): Georgios V Gkoutos, Paul N Schofield, and Robert Hoehndorf. The anatomy of phenotype ontologies: principles, properties and applications. Briefings in Bioinformatics, 19:1008-1021, Apr 2018. URL: https://doi.org/10.1093/bib/bbx035, doi:10.1093/bib/bbx035. This article has 140 citations and is from a domain leading peer-reviewed journal.

14. (liu2023mycobacteriaceaephenomeatlas pages 2-5): Wangdao Liu, H. Cen, Zhile Wu, Haokui Zhou, Shuo Chen, Xilan Yang, Guoping Zhao, and Guoqing Zhang. Mycobacteriaceae phenome atlas (mpa): a standardized atlas for the mycobacteriaceae phenome based on heterogeneous sources. Phenomics, 3:439-456, Jun 2023. URL: https://doi.org/10.1007/s43657-023-00101-5, doi:10.1007/s43657-023-00101-5. This article has 6 citations.

15. (thessen2020transformingthestudy pages 11-12): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

16. (duque2024meetingreportfor pages 1-3): Jennifer C. Girón Duque, Meghan A. Balk, W. Dahdul, H. Lapp, István Mikó, Elie Alhajjar, Brenen M. Wynd, Sergei Tarasov, Christopher Lawrence, Basanta Khakurel, Arthur Porto, Lin Yan, Isadora E Fluck, D. Porto, Joseph Keating, Israel T. Borokini, Katja C. Seltmann, G. Montanaro, and Paula M. Mabee. Meeting report for the phenoscape traitfest 2023 with comments on organising interdisciplinary meetings. Biodiversity Information Science and Standards, Mar 2024. URL: https://doi.org/10.3897/biss.8.115232, doi:10.3897/biss.8.115232. This article has 0 citations.

17. (thessen2020transformingthestudy media 04915a38): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.