---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:48:16.596252'
end_time: '2026-06-18T12:56:58.664563'
duration_seconds: 522.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** material entity
- **METPO identifier:** METPO:1000186
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
- **METPO identifier:** METPO:1000186
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


# Curation-Focused Research Report: METPO:1000186 **material entity** (UPPER) as a TraitMech causal-graph candidate

## Executive scope summary
**METPO:1000186 “material entity”** corresponds to an *upper-ontology* category used in Basic Formal Ontology (BFO) and BFO-aligned suites (e.g., Common Core Ontologies, CCO). In BFO-aligned usage, **material entity** is an **independent continuant** that is distinguished by **having material parts**, whereas **immaterial entity** lacks material parts and includes entities such as *sites* and *continuant fiat boundaries*; the two are treated as disjoint. (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3, smart2023secureontologiesfor pages 35-42)

**Curation implication for TraitMech:** “material entity” should be treated as a **typing/context superclass** for downstream mechanistic nodes (cells, proteins, metabolites, substrates, devices), not as a microbial phenotype or mechanistic trait that participates in biological causal edges. Attempting to model “material entity → phenotype” is a category error: causal graphs should instead connect *specific* material entities and dependent continuants (qualities/dispositions) through processes. (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3)

## 1) Key concepts and definitions (current understanding)

### 1.1 BFO placement and definition signal
Recent BFO/CCO-facing sources consistently place material entity under independent continuant:
- **Independent continuant** has two BFO subclasses: **material entity** and **immaterial entity**. (beverley2024capabilities pages 3-6)
- In CCO documentation of BFO, independent continuants are further divided into **material entities “having material parts”** and immaterial entities **“lacking them.”** (jensen2024thecommoncore pages 1-3)

### 1.2 Boundary cases: material vs immaterial
**Material entity** examples in recent BFO-facing writing include ordinary objects and aggregates (e.g., individuals and groups). (beverley2024capabilities pages 3-6)

**Immaterial entity** boundary cases commonly arise in modeling location/boundary phenomena:
- A **site** is described (in a BFO/CCO design pattern) as “a three-dimensional immaterial entity whose boundaries coincide with some material entity.” This makes sites a paradigmatic “nearby” class that should *not* be modeled as a material entity. (jensen2024thecommoncore pages 3-6)
- BFO-aligned sources explicitly treat immaterial entities as **disjoint** from material entities, and they discuss immaterial entities as including sites and boundary-like entities that depend on material hosts for their shape/location. (smart2023secureontologiesfor pages 35-42)

### 1.3 Relation to dependent continuants (qualities, dispositions)
A key modeling use of “material entity” is as the **bearer** for dependent continuants:
- Qualities can be described as “a quality inhering in a material entity …” in CCO/BFO-aligned exposition. (jensen2024thecommoncore pages 3-6)
- Dispositions are characterized in BFO-facing security ontology work as realizable entities **whose bearer is “some material entity.”** This supports a common design pattern: *disposition inheres in material entity; disposition realized in process*. (smart2023secureontologiesfor pages 29-35)

## 2) Recent developments & latest research (prioritizing 2023–2024)

### 2.1 Increased attention to interoperability via BFO/CCO-aligned suites (2024)
The Common Core Ontologies (CCO) present themselves as a mid-level ontology suite that extends BFO, emphasizing that terms ultimately extend from BFO and serve as “guardrails” rather than exhaustive taxonomies. This reinforces “material entity” as a **top-level organizing node** used for consistent extension across domains. (jensen2024thecommoncore pages 1-3)

### 2.2 Microbiome knowledge bases increasingly rely on ontology grounding and schemas (2024)
A 2024 microbiome-focused review highlights that mechanistic inference depends on mapping microbes, metabolites, and functions to shared ontologies/identifiers, and that knowledge graphs (KGs) must adopt schemas that support interoperability (e.g., Biolink-aligned approaches). This is highly relevant to TraitMech curation because it frames why “material entity” is a useful *upper typing anchor* while mechanistic edges require more specific, ontology-grounded node types (metabolites, proteins, pathways, taxa, environments). (santangelo2024integratingbiologicalknowledge pages 10-11, santangelo2024integratingbiologicalknowledge pages 12-13, santangelo2024integratingbiologicalknowledge pages 1-2)

### 2.3 Evidence base on foundational ontology usage remains thin despite adoption (2023)
A 2023 systematic literature mapping of foundational ontologies in biomedical research reported that BFO was the **most used** foundational ontology among 79 included papers (42 papers; ~53%). However, empirical testing of claimed advantages is scarce: only **1/79** papers included an empirical experiment testing such claims (~1.3%). Among 49 papers that developed ontologies, only **16/49** reported using an ontology engineering method (~33%), and only **4/49** used formal evaluation methods (~8%). These statistics support a cautious stance: treat upper-ontology alignment (like material entity) as valuable for semantics and interoperability, but avoid over-claiming empirically validated downstream benefits unless evaluated. (bernabe2023theuseof pages 4-6, bernabe2023theuseof pages 1-2, bernabe2023theuseof pages 8-10)

## 3) Current applications and real-world implementations

### 3.1 BFO/CCO design patterns used in applied knowledge graphs
- The **site** pattern (immaterial entity whose boundaries coincide with a material entity) is used in CCO-oriented modeling of tracking/locations and can generalize to microbial contexts (e.g., “biofilm site in host tissue,” “gut lumen site”), while keeping the site immaterial and the organismal structures material. (jensen2024thecommoncore pages 3-6)
- Microbiome knowledge resources are increasingly represented as KGs and benefit from schema and ontology alignment. The 2024 microbiome review notes that **KG-microbe aligns to the Biolink schema** and includes **manual curation** to represent microbial traits in that schema, illustrating a real implementation pathway relevant to TraitMech. (santangelo2024integratingbiologicalknowledge pages 12-13)

### 3.2 Genotype→phenotype pipelines inform what *should* be mechanistic nodes/edges (not “material entity”) 
A 2023 review of computational trait inference in microbes emphasizes mechanistic entities and representations (genes, proteins/enzymes, metabolites, pathways, genome-scale models) and mechanistic link motifs (e.g., enzyme→substrate processing→growth phenotype). These are concrete, domain-level nodes that are typically *material entities* (proteins, metabolites) or related dependent/occurrent entities (functions/processes), but they are not modeled causally via the abstract class “material entity.” (karlsen2023fromgenotypeto pages 2-3, karlsen2023fromgenotypeto pages 1-2)

## 4) Expert opinions and analysis (authoritative sources)

### 4.1 Expert framing: “material entity” is a top-level category, not a domain trait
BFO/CCO-aligned authors treat “material entity” as a component of foundational distinctions (continuant vs occurrent; independent vs dependent continuant) used to structure all domain modeling. This strongly supports curating METPO:1000186 as an **upper-context term** whose primary purpose is classification/typing and prevention of category mistakes (e.g., confusing sites/boundaries with material objects). (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3, smart2023secureontologiesfor pages 35-42)

### 4.2 Practical guidance: use upper ontology for interoperability but recognize cost/complexity
The 2023 systematic mapping reports that foundational ontologies are widely *claimed* to improve interoperability and reasoning, but the most commonly cited downside is complexity and the empirical evidence is sparse. This suggests that a TraitMech curation should keep upper nodes minimal (including material entity), focus effort on mechanistic nodes/edges with strong empirical support, and avoid over-modeling. (bernabe2023theuseof pages 1-2, bernabe2023theuseof pages 10-11)

## 5) Relevant statistics and data from recent studies

### 5.1 Foundational ontology adoption (biomedical literature mapping; published 2023-12)
From Bernabé et al. (2023):
- 79 selected papers (from 426 initial records; 364 after deduplication). (bernabe2023theuseof pages 4-6)
- BFO used in **42/79** selected papers (~53%). (bernabe2023theuseof pages 4-6)
- Only **1/79** had an empirical experiment testing claims (~1.3%). (bernabe2023theuseof pages 1-2)
- Among 49 ontology-development papers: **16/49** used an ontology engineering method (~33%); **4/49** used formal evaluation methods (~8%); **39/49** represented ontologies in OWL (~80%). (bernabe2023theuseof pages 1-2, bernabe2023theuseof pages 8-10)

### 5.2 Microbiome KG/ontology landscape signals (published 2024-04)
From Santangelo et al. (2024):
- Example of an OBO-aligned ontology for microbe–host interactions (OHMI) introducing ~1,000 terms and aligning to NCBI Taxonomy/ENVO/UBERON (illustrative of ontology grounding in this domain). (santangelo2024integratingbiologicalknowledge pages 9-10)
- Strong caution that **without mappings to a semantic standard, it is impossible to combine a resource with others**, highlighting why upper-level typing (e.g., material entity) plus downstream grounded nodes is essential for KG integration. (santangelo2024integratingbiologicalknowledge pages 10-11)

---

## Trait scope (for curation)

### What the trait represents
- **Trait label:** material entity
- **Identifier:** METPO:1000186
- **Interpretation for TraitMech:** an **upper-level ontological class** (BFO-style) for “objects/portions of matter” and physical bearers of qualities/dispositions.

### What it does *not* represent (important boundary)
- Not a microbial phenotype (e.g., growth rate, motility).
- Not a physiological capacity or environmental preference.
- Not an assay-observed property.

In other words, it is best curated as a **root typing node** (schema layer), not as a leaf trait used in biological causal inference. (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3)

---

## Candidate causal-graph entities (nodes) grouped by type
Because METPO:1000186 is an UPPER term, the appropriate curation is to (i) retain it as a top-level node and (ii) place *actual microbial-mechanism nodes* beneath it.

### A) Upper/schema nodes (safe)
- **material entity** (METPO:1000186; aligns to BFO:material entity) (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3)
- **independent continuant** (BFO) (beverley2024capabilities pages 3-6)
- **immaterial entity** (BFO) (smart2023secureontologiesfor pages 35-42)
- **site** (BFO:site; immaterial) (jensen2024thecommoncore pages 3-6)
- **quality**, **disposition** (dependent continuants tied to material bearers) (jensen2024thecommoncore pages 3-6, smart2023secureontologiesfor pages 29-35)

### B) Downstream mechanistic entities (examples; should be curated in domain traits, not here)
Grounding depends on which downstream traits are targeted; examples supported as relevant node types in microbial trait inference and microbiome mechanistic inference reviews:
- **Genes, variants, gene clusters** (sequence-level entities) (karlsen2023fromgenotypeto pages 5-6, karlsen2023fromgenotypeto pages 1-2)
- **Proteins/enzymes/transporters** (material entities; functions realized in processes) (karlsen2023fromgenotypeto pages 5-6, karlsen2023fromgenotypeto pages 2-3)
- **Metabolites/chemicals** (material entities; should be CHEBI-grounded in downstream graphs) (santangelo2024integratingbiologicalknowledge pages 3-5)
- **Pathways / reactions / genome-scale metabolic networks** (mechanistic model structures connecting genes→reactions→metabolites) (santangelo2024integratingbiologicalknowledge pages 3-5, karlsen2023fromgenotypeto pages 18-19)
- **Taxa and environments** (should be NCBITaxon / ENVO grounded in downstream graphs) (santangelo2024integratingbiologicalknowledge pages 3-5, santangelo2024integratingbiologicalknowledge pages 1-2)

---

## Candidate causal edges (triples) with evidence, snippets, and notes
The following artifact contains proposed edges, explicitly separating **schema/ontological edges** (appropriate for this UPPER trait file) from **mechanistic edges** that should be curated elsewhere.

| Edge type | Subject (label + CURIE) | Predicate (RO/BFO style relation) | Object (label + CURIE) | Evidence snippet | Reference (DOI + URL + year) | Notes/curation status |
|---|---|---|---|---|---|---|
| Schema | material entity (BFO:material entity; METPO:1000186) | subclass of | independent continuant (BFO:independent continuant) | “Independent continuant has two BFO sub-classes, namely material entity and immaterial …” (beverley2024capabilities pages 3-6) | 10.48550/arXiv.2405.00183 · https://doi.org/10.48550/arxiv.2405.00183 · 2024 | Safe as upper-ontology typing edge; not a microbial mechanism edge. |
| Schema | immaterial entity (BFO:immaterial entity) | disjoint with | material entity (BFO:material entity) | “immaterial entities are declared disjoint from material entities” (smart2023secureontologiesfor pages 35-42) | Source discussed in 2023 BFO-use exposition; excerpt from SOfIoTS/secure ontology material · 2023 | Safe schema edge if imported from BFO; do not treat as trait mechanism. |
| Schema | material entity (BFO:material entity) | has part | matter (label-only candidate) | “material entities ‘having material parts’ and immaterial entities ‘lacking them.’” (jensen2024thecommoncore pages 1-3) | 10.48550/arXiv.2404.17758 · https://doi.org/10.48550/arxiv.2404.17758 · 2024 | Useful definitional paraphrase; object not cleanly grounded in provided evidence. Curate cautiously. |
| Schema | site (BFO:site) | boundaries coincide with | material entity (BFO:material entity) | “site is a three-dimensional immaterial entity whose boundaries coincide with some material entity” (jensen2024thecommoncore pages 3-6) | 10.48550/arXiv.2404.17758 · https://doi.org/10.48550/arxiv.2404.17758 · 2024 | Safe BFO/CCO design-pattern edge; contextual only. |
| Schema | quality (BFO:quality) | inheres in | material entity (BFO:material entity) | “a quality inhering in a material entity in virtue of its location in a gravitational field” (jensen2024thecommoncore pages 3-6) | 10.48550/arXiv.2404.17758 · https://doi.org/10.48550/arxiv.2404.17758 · 2024 | Safe generic continuant pattern; too abstract for microbial trait graph unless specialized. |
| Schema | disposition (BFO:disposition) | bearer_of / inheres in | material entity (BFO:material entity) | “a disposition is a realizable entity whose bearer is ‘some material entity’” (smart2023secureontologiesfor pages 29-35) | SOfIoTS secure ontologies excerpt · 2023 | Safe ontological pattern; relevant when later specializing to resistance, motility, etc. |
| Schema | fiat object part (BFO:fiat object part) | subclass of | material entity (BFO:material entity) | “A fiat object part is explicitly asserted to be a material entity” (smart2023secureontologiesfor pages 35-42) | SOfIoTS secure ontologies excerpt · 2023 | Safe schema edge if needed for partonomy; likely unnecessary for TraitMech upper trait file. |
| Schema | material artifact (CCO:material artifact) | subclass of | material entity (BFO:material entity) | “material artifact - a material entity designed by some agent to realize some function” (jensen2024thecommoncore pages 3-6) | 10.48550/arXiv.2404.17758 · https://doi.org/10.48550/arxiv.2404.17758 · 2024 | Valid CCO example of specialization; not microbe-specific. |
| Mechanistic | gene (SO:gene, label-only here) | encodes | protein/enzyme (PR:protein, EC:enzyme label-only) | “Core entities include genes, proteins, and metabolites” and “gene→phenotype associations” (karlsen2023fromgenotypeto pages 1-2) | 10.1093/femsre/fuad030 · https://doi.org/10.1093/femsre/fuad030 · 2023 | Generic microbial-trait edge pattern; not evidence about material entity specifically. Do not curate under this upper trait. |
| Mechanistic | protein/enzyme (PR/EC label-only) | enables / catalyzes | reaction or substrate processing (Rhea/MetaCyc/KEGG label-only) | “cell-surface associated proteases that drive casein breakdown (linking enzyme → substrate processing → growth phenotype)” (karlsen2023fromgenotypeto pages 2-3) | 10.1093/femsre/fuad030 · https://doi.org/10.1093/femsre/fuad030 · 2023 | Valid mechanistic motif for downstream trait graphs; not specific to material entity. |
| Mechanistic | pathway or metabolic model (KEGG/MetaCyc/GSMN label-only) | has output | metabolite / metabolic phenotype (ChEBI label-only) | “KEGG and MetaCyc … represent relationships among … reactions/pathways, and metabolites” (santangelo2024integratingbiologicalknowledge pages 3-5) | 10.3389/fmicb.2024.1351678 · https://doi.org/10.3389/fmicb.2024.1351678 · 2024 | Appropriate for functional trait graphs; not for upper-class ‘material entity’. |
| Mechanistic | variant or promoter alteration (SO label-only) | affects | gene expression / protein function (GO/PR label-only) | “promoter/TF-binding alteration→gene expression→phenotype” and “variant→protein function” (karlsen2023fromgenotypeto pages 5-6) | 10.1093/femsre/fuad030 · https://doi.org/10.1093/femsre/fuad030 · 2023 | Mechanistic and useful elsewhere; should not be attached directly to material entity node. |
| Mechanistic | microbial trait knowledge graph node (e.g., microbe/taxon) | related to | ontology-grounded trait/function node | “KG-Microbe includes specific microbial traits to be represented in a way that aligns with the Biolink schema” (santangelo2024integratingbiologicalknowledge pages 12-13) | 10.3389/fmicb.2024.1351678 · https://doi.org/10.3389/fmicb.2024.1351678 · 2024 | Supports using ontology-grounded downstream nodes beneath material entity; schema/integration evidence only. |
| Mechanistic | material entity (BFO:material entity; METPO:1000186) | causes / positively regulates | microbial phenotype (label-only) | No direct evidence in gathered sources; sources treat material entity as an upper class, not a causal phenotype determinant (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3) | 10.48550/arXiv.2405.00183 · https://doi.org/10.48550/arxiv.2405.00183 · 2024; 10.48550/arXiv.2404.17758 · https://doi.org/10.48550/arxiv.2404.17758 · 2024 | Do **not** curate: category error. ‘Material entity’ is a typing/context node, not a mechanistic microbial trait edge. |


*Table: This table separates ontology/schema edges from biological/mechanistic edges for the upper-level trait ‘material entity’. It is useful for deciding which relations are safe to curate as BFO/CCO context and which should be excluded from TraitMech as non-specific or category errors.*

---

## Warnings / “do not curate yet” items
1. **Do not curate biological causal edges using the abstract class “material entity”** as a cause/effect node (e.g., “material entity causes phenotype”). This collapses essential BFO distinctions and is unsupported by evidence; BFO-facing sources treat material entity as a domain-neutral classifier. (beverley2024capabilities pages 3-6, jensen2024thecommoncore pages 1-3)
2. **Grounding gaps:** Some definitional paraphrases reference “matter” as a part criterion, but this object was not provided as a stable CURIE in the retrieved evidence; avoid asserting a grounded “matter” node unless you import an appropriate ontology term. (jensen2024thecommoncore pages 1-3)
3. **Immaterial vs material boundary in microbial contexts:** “site” modeling is powerful but can be misused; ensure sites are not treated as material things and respect disjointness constraints where imported. (jensen2024thecommoncore pages 3-6, smart2023secureontologiesfor pages 35-42)
4. **Interoperability claims:** Systematic mapping indicates widespread *claims* of benefits from foundational ontologies but very limited empirical testing; avoid over-stating performance or integration outcomes without project-specific evaluation. (bernabe2023theuseof pages 1-2, bernabe2023theuseof pages 8-10)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Beverley J, Limbaugh D, Merrell E, Koch PM, Smith B.** *Capabilities.* (arXiv preprint; **2024-04**). DOI: **10.48550/arXiv.2405.00183**. URL: https://doi.org/10.48550/arxiv.2405.00183 (beverley2024capabilities pages 3-6)

2. **Jensen M, De Colle G, Kindya S, More C, Cox AP, Beverley J.** *The Common Core Ontologies.* (arXiv preprint; **2024-04**). DOI: **10.48550/arXiv.2404.17758**. URL: https://doi.org/10.48550/arxiv.2404.17758 (jensen2024thecommoncore pages 1-3, jensen2024thecommoncore pages 3-6)

3. **Santangelo BE, Apgar M, Colorado ASB, et al.** *Integrating biological knowledge for mechanistic inference in the host-associated microbiome.* *Frontiers in Microbiology* (**2024-04**). DOI: **10.3389/fmicb.2024.1351678**. URL: https://doi.org/10.3389/fmicb.2024.1351678 (santangelo2024integratingbiologicalknowledge pages 9-10, santangelo2024integratingbiologicalknowledge pages 10-11, santangelo2024integratingbiologicalknowledge pages 3-5, santangelo2024integratingbiologicalknowledge pages 12-13, santangelo2024integratingbiologicalknowledge pages 1-2)

4. **Bernabé CH, Queralt-Rosinach N, Souza VES, et al.** *The use of foundational ontologies in biomedical research.* *Journal of Biomedical Semantics* (**2023-12**). DOI: **10.1186/s13326-023-00300-z**. URL: https://doi.org/10.1186/s13326-023-00300-z (bernabe2023theuseof pages 4-6, bernabe2023theuseof pages 1-2, bernabe2023theuseof pages 8-10)

5. **Karlsen ST, Rau MH, Sánchez BJ, Jensen K, Zeidan AA.** *From genotype to phenotype: computational approaches for inferring microbial traits relevant to the food industry.* *FEMS Microbiology Reviews* (**2023-06**). DOI: **10.1093/femsre/fuad030**. URL: https://doi.org/10.1093/femsre/fuad030 (karlsen2023fromgenotypeto pages 5-6, karlsen2023fromgenotypeto pages 2-3, karlsen2023fromgenotypeto pages 1-2)

---

## Minimal YAML-curation guidance (for `data/traits/upper/material_entity.yaml`)
- Treat **METPO:1000186** as a *root class* for material nodes used elsewhere.
- Curate only **schema-level edges** (subclass/disjointness/bearer patterns) that preserve BFO distinctions.
- Defer biological causal edges to domain traits (e.g., motility, fermentation capability, antibiotic resistance), where genes/proteins/metabolites can be grounded and evidenced.


References

1. (beverley2024capabilities pages 3-6): John Beverley, David Limbaugh, Eric Merrell, Peter M. Koch, and Barry Smith. Capabilities. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2405.00183, doi:10.48550/arxiv.2405.00183. This article has 8 citations.

2. (jensen2024thecommoncore pages 1-3): Mark Jensen, Giacomo De Colle, Sean Kindya, Cameron More, Alexander P. Cox, and John Beverley. The common core ontologies. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2404.17758, doi:10.48550/arxiv.2404.17758. This article has 43 citations.

3. (smart2023secureontologiesfor pages 35-42): P Smart, M Boniface, MA Jarwar, and J Watson. Secure ontologies for the internet of things: representing risk and security concepts using basic formal ontology. Unknown journal, 2023.

4. (jensen2024thecommoncore pages 3-6): Mark Jensen, Giacomo De Colle, Sean Kindya, Cameron More, Alexander P. Cox, and John Beverley. The common core ontologies. ArXiv, Apr 2024. URL: https://doi.org/10.48550/arxiv.2404.17758, doi:10.48550/arxiv.2404.17758. This article has 43 citations.

5. (smart2023secureontologiesfor pages 29-35): P Smart, M Boniface, MA Jarwar, and J Watson. Secure ontologies for the internet of things: representing risk and security concepts using basic formal ontology. Unknown journal, 2023.

6. (santangelo2024integratingbiologicalknowledge pages 10-11): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

7. (santangelo2024integratingbiologicalknowledge pages 12-13): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

8. (santangelo2024integratingbiologicalknowledge pages 1-2): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

9. (bernabe2023theuseof pages 4-6): César H. Bernabé, Núria Queralt-Rosinach, Vítor E. Silva Souza, Luiz Olavo Bonino da Silva Santos, Barend Mons, Annika Jacobsen, and Marco Roos. The use of foundational ontologies in biomedical research. Journal of Biomedical Semantics, Dec 2023. URL: https://doi.org/10.1186/s13326-023-00300-z, doi:10.1186/s13326-023-00300-z. This article has 32 citations and is from a peer-reviewed journal.

10. (bernabe2023theuseof pages 1-2): César H. Bernabé, Núria Queralt-Rosinach, Vítor E. Silva Souza, Luiz Olavo Bonino da Silva Santos, Barend Mons, Annika Jacobsen, and Marco Roos. The use of foundational ontologies in biomedical research. Journal of Biomedical Semantics, Dec 2023. URL: https://doi.org/10.1186/s13326-023-00300-z, doi:10.1186/s13326-023-00300-z. This article has 32 citations and is from a peer-reviewed journal.

11. (bernabe2023theuseof pages 8-10): César H. Bernabé, Núria Queralt-Rosinach, Vítor E. Silva Souza, Luiz Olavo Bonino da Silva Santos, Barend Mons, Annika Jacobsen, and Marco Roos. The use of foundational ontologies in biomedical research. Journal of Biomedical Semantics, Dec 2023. URL: https://doi.org/10.1186/s13326-023-00300-z, doi:10.1186/s13326-023-00300-z. This article has 32 citations and is from a peer-reviewed journal.

12. (karlsen2023fromgenotypeto pages 2-3): Signe T Karlsen, Martin H Rau, Benjamín J Sánchez, Kristian Jensen, and Ahmad A Zeidan. From genotype to phenotype: computational approaches for inferring microbial traits relevant to the food industry. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad030, doi:10.1093/femsre/fuad030. This article has 32 citations and is from a domain leading peer-reviewed journal.

13. (karlsen2023fromgenotypeto pages 1-2): Signe T Karlsen, Martin H Rau, Benjamín J Sánchez, Kristian Jensen, and Ahmad A Zeidan. From genotype to phenotype: computational approaches for inferring microbial traits relevant to the food industry. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad030, doi:10.1093/femsre/fuad030. This article has 32 citations and is from a domain leading peer-reviewed journal.

14. (bernabe2023theuseof pages 10-11): César H. Bernabé, Núria Queralt-Rosinach, Vítor E. Silva Souza, Luiz Olavo Bonino da Silva Santos, Barend Mons, Annika Jacobsen, and Marco Roos. The use of foundational ontologies in biomedical research. Journal of Biomedical Semantics, Dec 2023. URL: https://doi.org/10.1186/s13326-023-00300-z, doi:10.1186/s13326-023-00300-z. This article has 32 citations and is from a peer-reviewed journal.

15. (santangelo2024integratingbiologicalknowledge pages 9-10): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

16. (karlsen2023fromgenotypeto pages 5-6): Signe T Karlsen, Martin H Rau, Benjamín J Sánchez, Kristian Jensen, and Ahmad A Zeidan. From genotype to phenotype: computational approaches for inferring microbial traits relevant to the food industry. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad030, doi:10.1093/femsre/fuad030. This article has 32 citations and is from a domain leading peer-reviewed journal.

17. (santangelo2024integratingbiologicalknowledge pages 3-5): Brook E. Santangelo, Madison Apgar, Angela Sofia Burkhart Colorado, Casey G. Martin, John D. Sterrett, Elena Wall, Marcin P. Joachimiak, Lawrence E. Hunter, and Catherine A. Lozupone. Integrating biological knowledge for mechanistic inference in the host-associated microbiome. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1351678, doi:10.3389/fmicb.2024.1351678. This article has 6 citations and is from a peer-reviewed journal.

18. (karlsen2023fromgenotypeto pages 18-19): Signe T Karlsen, Martin H Rau, Benjamín J Sánchez, Kristian Jensen, and Ahmad A Zeidan. From genotype to phenotype: computational approaches for inferring microbial traits relevant to the food industry. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad030, doi:10.1093/femsre/fuad030. This article has 32 citations and is from a domain leading peer-reviewed journal.