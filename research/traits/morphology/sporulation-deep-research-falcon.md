---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:47:30.359089'
end_time: '2026-06-18T10:10:32.646126'
duration_seconds: 1382.29
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: sporulation
  trait_identifier: METPO:1000870
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sporulation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is relating to an organism's ability to form dormant,
    stress-resistant endospores.
  parent_traits: METPO:1000059
  synonyms: General.keywords, Physiology and metabolism.spore formation.spore formation
  evidence_summary: 'DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell
    into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis
    process producing a spore within a sporangium.)'
  causal_graph_summary: 'sporulation_spo0a_sigma_morphogenesis: 7 nodes, 6 edges'
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
- **Trait label:** sporulation
- **METPO identifier:** METPO:1000870
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's ability to form dormant, stress-resistant endospores.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Physiology and metabolism.spore formation.spore formation
- **Existing evidence:** DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis process producing a spore within a sporangium.)
- **Existing causal graph summary:** sporulation_spo0a_sigma_morphogenesis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **sporulation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sporulation.yaml`.

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
- **Trait label:** sporulation
- **METPO identifier:** METPO:1000870
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's ability to form dormant, stress-resistant endospores.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Physiology and metabolism.spore formation.spore formation
- **Existing evidence:** DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis process producing a spore within a sporangium.)
- **Existing causal graph summary:** sporulation_spo0a_sigma_morphogenesis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **sporulation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sporulation.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Sporulation (METPO:1000870)

### 1) Scope summary (trait definition and boundary cases)

**Trait meaning.** In TraitMech terms, *sporulation* should be scoped to the **capacity to form an endospore**, i.e., a developmental differentiation program that converts a vegetative cell into a **dormant, highly stress‑resistant spore**. In Bacillus, sporulation is described as producing “metabolically inactive, extremely resistant” spores and proceeds through morphogenetic and regulatory stages over **~7 h at 37 °C**. (iwanska2024translationinbacillus pages 1-2)

**Core morphogenesis.** Canonical endospore sporulation includes: entry during stationary phase/nutrient limitation, asymmetric division into **forespore and mother cell**, **forespore engulfment** (cell‑within‑a‑cell), construction of protective layers (cortex/coat; sometimes exosporium), and mother‑cell lysis releasing the mature spore. These steps are explicitly described for *Clostridioides difficile* spores (asymmetric division, engulfment, cortex/coat/exosporium deposition, mother‑cell lysis) and linked to resistance functions of layers. (cassona2024sporesofclostridioides pages 1-2)

**Boundary cases / near neighbors.**
- **Not included:** spore **germination/outgrowth** (revival program) as a trait, though many regulators overlap and some experiments measure sporulation via heat/ethanol‑resistant CFUs. (bidnenko2024complexsporulationspecificexpression pages 1-2, anjou2024themultiplicityof pages 18-20)
- **Not included:** **biofilm formation** or competence as separate traits; these can be **alternative Spo0A‑controlled fates** that share upstream signaling with sporulation. (gohari2024theimpactof pages 2-5, zhu2024plasmidencodedphosphataserapp pages 1-2)
- **Taxon boundary:** Endospore sporulation is primarily a Firmicutes trait (Bacilli/Clostridia). Clostridia often **lack the Bacillus‑style multicomponent phosphorelay**, so mechanistic edges are **not always portable** across taxa. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 2-5)

### 2) Key concepts and current mechanistic understanding (2023–2024 prioritized)

#### 2.1 Master regulator and initiation architectures

**Spo0A and phosphorylation state.** Sporulation entry is governed by Spo0A, a transcriptional “master regulator,” whose activity depends on phosphorylation (Spo0A~P) and, in Bacillus, also abundance. (feaga2023elongationfactorp pages 1-2, iwanska2024translationinbacillus pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2)

**Bacillus phosphorelay.** In Bacillus, multiple histidine kinases (KinA–E) feed signals through **Spo0F and Spo0B** to generate **Spo0A~P**. (liu2023transcriptionfactorspo0a pages 1-2, gohari2024theimpactof pages 2-5)

**Clostridial diversity (OHK model).** In many Clostridia, genomics and functional work support **direct phosphorylation of Spo0A by orphan histidine kinases (OHKs)**, with additional phosphotransfer proteins acting as kinases or phosphatases; no single universal pathway explains clostridial initiation. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 2-5)

#### 2.2 Commitment and crosstalk with other stationary‑phase fates

KinA/KinB are described as **primary sporulation initiators**, while KinD is described as promoting biofilm formation and **delaying sporulation**, illustrating Spo0A‑centered tradeoffs between fates. (gohari2024theimpactof pages 2-5)

A 2024 Nature Communications study of a plasmid‑encoded Rap phosphatase shows an explicit resource‑allocation framing: RapP enhances growth by **“preventing premature expression of the Spo0F‑Spo0A‑mediated adaptive response”** during exponential phase. (zhu2024plasmidencodedphosphataserapp pages 1-2)

#### 2.3 Sigma factor cascade and compartmentalization

**Compartment‑specific sigma cascade.** Bacillus sporulation is controlled by sequential compartment‑specific sigma factors (σF/σE/σG/σK). σF is activated first in the forespore, and **σE activation in the mother cell depends on σF**. (bidnenko2024complexsporulationspecificexpression pages 1-2)

**Late-stage maturation.** In Bacillus, σG drives spore maturation including “spore DNA protection via Ssp proteins,” while σK controls “spore coat and cortex maturation and mother‑cell lysis.” (iwanska2024translationinbacillus pages 1-2)

**Visual evidence (figure).** A 2024 Nature Communications figure provides a translational timeline (T0–T7 hours) and sigma‑regulon dynamics that align with the ~7 h developmental program. (iwanska2024translationinbacillus media 8e8b0f73, iwanska2024translationinbacillus media 77a6be13)

#### 2.4 Translation and transcription layers newly emphasized in 2023–2024

**Translation quality control impacts commitment.** A 2023 primary study shows that loss of EF‑P lowers spo0A expression and delays sporulation initiation; **ectopic Spo0A rescues** the phenotype, directly supporting a causal chain from translation stress → Spo0A abundance → sporulation initiation. Quantitatively, WT sporulation efficiency was ~85% vs ~15% for Δefp in DSM medium. (feaga2023elongationfactorp pages 1-2)

**Transcription termination factor Rho modulates initiation and spore quality.** A 2024 JBC study reports that **reduction of Rho during transition to stationary phase is necessary** for initiation and implementation of sporulation, while mis‑regulation affects spore morphology/resistance and revival. (bidnenko2024complexsporulationspecificexpression pages 1-2)

### 3) Candidate mechanistic entities (nodes) for `sporulation.yaml`

The following artifact lists curation‑ready candidate nodes with taxon notes and tentative grounding.

| Node label | Node type | Suggested ontology grounding | Taxon notes | Evidence source (citation id) |
|---|---|---|---|---|
| Spo0A | gene/protein | UniProt:P06532; GO:0009405 | General; central in Bacillus and many Clostridia | (feaga2023elongationfactorp pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2, gohari2024theimpactof pages 1-2) |
| Spo0A~P (phosphorylated Spo0A) | protein | GO:0016310 | General; active sporulation regulator state | (bidnenko2024complexsporulationspecificexpression pages 1-2, liu2023transcriptionfactorspo0a pages 1-2, gohari2024theimpactof pages 1-2) |
| KinA | gene/protein |  | Bacillus | (liu2023transcriptionfactorspo0a pages 1-2, gohari2024theimpactof pages 2-5, gohari2024theimpactof pages 14-15) |
| KinB | gene/protein |  | Bacillus | (bidnenko2024complexsporulationspecificexpression pages 1-2, gohari2024theimpactof pages 2-5, zhu2024plasmidencodedphosphataserapp pages 2-3) |
| KinC | gene/protein |  | Bacillus | (gohari2024theimpactof pages 2-5, gohari2024theimpactof pages 15-15, gohari2024theimpactof pages 14-15) |
| KinD | gene/protein |  | Bacillus | (liu2023transcriptionfactorspo0a pages 1-2, gohari2024theimpactof pages 2-5, gohari2024theimpactof pages 15-15) |
| Spo0F | gene/protein |  | Bacillus phosphorelay; absent from many Clostridia | (bidnenko2024complexsporulationspecificexpression pages 1-2, gohari2024theimpactof pages 2-5, zhu2024plasmidencodedphosphataserapp pages 1-2) |
| Spo0B | gene/protein |  | Bacillus phosphorelay; absent from many Clostridia | (liu2023transcriptionfactorspo0a pages 1-2, gohari2024theimpactof pages 2-5) |
| Spo0E | gene/protein |  | Bacillus | (liu2023transcriptionfactorspo0a pages 1-2, gangwal2023givingasignal pages 5-5) |
| RapP | gene/protein |  | Bacillus subtilis plasmid-encoded regulator | (zhu2024plasmidencodedphosphataserapp pages 2-3, zhu2024plasmidencodedphosphataserapp pages 1-2) |
| RapA | gene/protein |  | Bacillus | (liu2023transcriptionfactorspo0a pages 1-2, gangwal2023givingasignal pages 5-5) |
| EF-P | protein |  | Bacillus subtilis in cited evidence | (feaga2023elongationfactorp pages 1-2, iwanska2024translationinbacillus pages 1-2) |
| Rho | protein |  | Bacillus subtilis; also noted in other Firmicutes | (bidnenko2024complexsporulationspecificexpression pages 1-2, bidnenko2024complexsporulationspecificexpression pages 17-17) |
| SigH (σH) | protein | GO:0009399 | Bacillus | (feaga2023elongationfactorp pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2) |
| SigF (σF) | protein |  | General sporulation sigma; Bacillus evidence | (iwanska2024translationinbacillus pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2) |
| SigE (σE) | protein |  | General sporulation sigma; Bacillus evidence | (iwanska2024translationinbacillus pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2) |
| SigG (σG) | protein |  | Bacillus and C. difficile forespore programs | (iwanska2024translationinbacillus pages 1-2, cassona2024sporesofclostridioides pages 1-2) |
| SigK (σK) | protein |  | Bacillus | (iwanska2024translationinbacillus pages 1-2) |
| SpoIIIE | protein |  | Bacillus | (iwanska2024translationinbacillus pages 1-2) |
| SpoVT | protein |  | Clostridioides difficile | (cassona2024sporesofclostridioides pages 1-2) |
| SigD (σD) | protein |  | Clostridioides difficile | (cassona2024sporesofclostridioides pages 1-2) |
| cortex | process | GO:0030436 | General spore structure | (cassona2024sporesofclostridioides pages 1-2, iwanska2024translationinbacillus pages 1-2) |
| spore coat | process | GO:0031160 | General spore structure | (cassona2024sporesofclostridioides pages 1-2, iwanska2024translationinbacillus pages 1-2) |
| exosporium | process |  | Present in some taxa including C. difficile | (cassona2024sporesofclostridioides pages 1-2) |
| Ssp proteins (small acid-soluble spore proteins) | protein |  | Bacillus | (iwanska2024translationinbacillus pages 1-2) |
| heat-resistant spores | assay |  | General sporulation phenotype; common readout in Clostridia and Bacillus-related studies | (gohari2024theimpactof pages 12-14, gohari2024theimpactof pages 6-8) |
| translation silencing | process |  | Bacillus subtilis | (iwanska2024translationinbacillus pages 1-2) |
| stationary phase / nutrient limitation | environment | ENVO:01000355 | General trigger context | (bidnenko2024complexsporulationspecificexpression pages 1-2, iwanska2024translationinbacillus pages 1-2) |
| stringent response | process | GO:0009245 | Bacillus | (zhu2024plasmidencodedphosphataserapp pages 2-3, jaiaue2024inactivationofguanylate pages 15-16) |
| stomach acid | environment | CHEBI:30879 | Application context for spore-forming probiotics | (mourey2024theprobioticstrain pages 1-2) |
| bile salts | environment | CHEBI:3098 | Clostridioides difficile stress response / probiotic GI context | (crivelli2024thecomplexand pages 8-9, mourey2024theprobioticstrain pages 1-2) |
| high hydrostatic pressure | application |  | Food safety / spore control context | (payne2024thepotentialof pages 20-21) |
| lytic bacteriophages | application |  | Food safety combination approach; mentioned as prospective for spore-formers | (payne2024thepotentialof pages 20-21) |
| selenium nanoparticles | application |  | Food safety / antimicrobial targeting of spore-formers | (payne2024thepotentialof pages 1-2) |
| probiotic CFU dose | assay |  | Human probiotic implementation | (mourey2024theprobioticstrain pages 1-2, mcfarlin2024oralsporebasedprobiotic pages 2-4) |
| heat processing / baking 180°C 20 min | application |  | Food processing tolerance assay for Bacillus spores | (payne2024thepotentialof pages 3-5) |
| pelletization 80-85°C | application |  | Feed/food processing tolerance for Bacillus spores | (crivelli2024thecomplexand pages 8-9) |


*Table: This table lists curation-ready candidate nodes for a microbial endospore sporulation causal graph, grouped implicitly by node type and restricted to entities supported by evidence gathered in this chat. It is useful for seeding TraitMech YAML node definitions with taxon notes, tentative ontology grounding, and source traceability.*

### 4) Evidence-backed candidate causal edges (triples)

The following artifact provides **subject–predicate–object** edges with direct supporting snippets and DOI‑first references; these are suitable starting points for TraitMech YAML edges.

| Subject node | Predicate | Object node | Taxon scope | Evidence snippet | Reference (DOI · URL · year) and citation id | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| KinA–E | transfer phosphate to | Spo0F | Bacillus subtilis / Bacillus canon | “Surfactin activates sensor histidine kinases (KinA–E), which autophosphorylate; these phosphorylated kinases transfer phosphate via Spo0F and Spo0B to Spo0A” | 10.1128/spectrum.01044-23 · https://doi.org/10.1128/spectrum.01044-23 · 2023 (liu2023transcriptionfactorspo0a pages 1-2) | Canonical Bacillus phosphorelay; direct evidence summarized in B. amyloliquefaciens article background. |
| Spo0F | transfers phosphate to | Spo0B | Bacillus subtilis / Bacillus canon | “transfer phosphate via Spo0F and Spo0B to Spo0A” | 10.1128/spectrum.01044-23 · https://doi.org/10.1128/spectrum.01044-23 · 2023 (liu2023transcriptionfactorspo0a pages 1-2) | Strong canonical edge for Bacillus; likely not universal in Clostridia. |
| Spo0B | transfers phosphate to | Spo0A~P | Bacillus subtilis / Bacillus canon | “transfer phosphate via Spo0F and Spo0B to Spo0A, producing Spo0A~P” | 10.1128/spectrum.01044-23 · https://doi.org/10.1128/spectrum.01044-23 · 2023 (liu2023transcriptionfactorspo0a pages 1-2) | Strong canonical edge for Bacillus. |
| KinA | positively regulates | sporulation initiation | Bacillus subtilis | “KinA and KinB are primary initiators of sporulation” | 10.1128/mbio.02248-23 · https://doi.org/10.1128/mbio.02248-23 · 2024 (gohari2024theimpactof pages 2-5) | Supports Bacillus-specific upstream role; mechanistically via phosphorelay to Spo0A. |
| KinB | positively regulates | sporulation initiation | Bacillus subtilis | “KinA and KinB are primary initiators of sporulation” | 10.1128/mbio.02248-23 · https://doi.org/10.1128/mbio.02248-23 · 2024 (gohari2024theimpactof pages 2-5) | Strong Bacillus-specific edge. |
| KinD | delays | sporulation | Bacillus subtilis | “KinD specifically promotes biofilm formation and delays sporulation” | 10.1128/mbio.02248-23 · https://doi.org/10.1128/mbio.02248-23 · 2024 (gohari2024theimpactof pages 2-5) | Context-dependent, because KinD can also function as kinase/phosphatase depending on conditions. |
| RapP | dephosphorylates | Spo0F | Bacillus subtilis | “RapP phosphatase acts on the Spo0 phosphorelay by dephosphorylating Spo0F” | 10.1038/s41467-024-53992-x · https://doi.org/10.1038/s41467-024-53992-x · 2024 (zhu2024plasmidencodedphosphataserapp pages 1-2) | Strong direct edge. |
| RapP | prevents premature expression of | Spo0F–Spo0A adaptive response | Bacillus subtilis | “preventing premature expression of the Spo0F-Spo0A-mediated adaptive response during exponential phase” | 10.1038/s41467-024-53992-x · https://doi.org/10.1038/s41467-024-53992-x · 2024 (zhu2024plasmidencodedphosphataserapp pages 1-2) | Useful application/physiology edge linking phosphorelay control to resource allocation. |
| RapP | enhances | cell growth | Bacillus subtilis | “RapP enhances growth by preventing premature expression of the Spo0F-Spo0A-mediated adaptive response” | 10.1038/s41467-024-53992-x · https://doi.org/10.1038/s41467-024-53992-x · 2024 (zhu2024plasmidencodedphosphataserapp pages 1-2) | Growth effect is supported; mechanism partly via phosphatase activity and Spo0F binding. |
| Spo0E | decreases phosphorylation of | Spo0A | Bacillus / Bacillus amyloliquefaciens | “Spo0A~P levels are reduced by phosphatases such as RapA and Spo0E” | 10.1128/spectrum.01044-23 · https://doi.org/10.1128/spectrum.01044-23 · 2023 (liu2023transcriptionfactorspo0a pages 1-2) | Strong edge; generalized across Bacillus. |
| RapA | decreases phosphorylation of | Spo0A | Bacillus / Bacillus amyloliquefaciens | “Spo0A~P levels are reduced by phosphatases such as RapA and Spo0E” | 10.1128/spectrum.01044-23 · https://doi.org/10.1128/spectrum.01044-23 · 2023 (liu2023transcriptionfactorspo0a pages 1-2) | Likely mediated via phosphorelay flux; precise substrate not specified in this snippet. |
| EF-P | positively regulates expression of | spo0A | Bacillus subtilis | “expression of spo0A… is lower in a Δefp strain” | 10.1128/jb.00370-22 · https://doi.org/10.1128/jb.00370-22 · 2023 (feaga2023elongationfactorp pages 1-2) | Strong edge from primary study. |
| Spo0A ectopic expression | rescues defect in | sporulation initiation | Bacillus subtilis | “Ectopic expression of Spo0A rescues the sporulation initiation phenotype” | 10.1128/jb.00370-22 · https://doi.org/10.1128/jb.00370-22 · 2023 (feaga2023elongationfactorp pages 1-2) | Supports causal chain EF-P → Spo0A abundance → sporulation initiation. |
| Reduced EF-P | delays | sporulation-specific sigma factor activation | Bacillus subtilis | “results in a delay in the activation of multiple sporulation-specific sigma factors” | 10.1128/jb.00370-22 · https://doi.org/10.1128/jb.00370-22 · 2023 (feaga2023elongationfactorp pages 1-2) | Indirect downstream consequence of lower Spo0A. |
| Spo0A + SigH | govern entry into | sporulation | Bacillus subtilis | “Spo0A, in conjunction with the stationary-phase sigma factor sH, governs entry into sporulation” | 10.1128/jb.00370-22 · https://doi.org/10.1128/jb.00370-22 · 2023 (feaga2023elongationfactorp pages 1-2) | Strong edge for sporulation entry control. |
| Decrease in Rho level during transition to stationary phase | is necessary for | sporulation initiation | Bacillus subtilis | “the reduction of Rho levels during the transition to stationary phase is necessary for both initiation and implementation of the sporulation program” | 10.1016/j.jbc.2024.107905 · https://doi.org/10.1016/j.jbc.2024.107905 · 2024 (bidnenko2024complexsporulationspecificexpression pages 1-2) | Strong edge. |
| Rho deletion | increases | KinB expression | Bacillus subtilis | “Rho deletion increases KinB expression, accelerating accumulation of Spo0A~P and triggering sporulation” | 10.1016/j.jbc.2024.107905 · https://doi.org/10.1016/j.jbc.2024.107905 · 2024 (bidnenko2024complexsporulationspecificexpression pages 1-2) | Supports regulatory connection; mechanism may be transcriptional derepression. |
| Increased KinB expression | accelerates accumulation of | Spo0A~P | Bacillus subtilis | “increases KinB expression, accelerating accumulation of Spo0A~P” | 10.1016/j.jbc.2024.107905 · https://doi.org/10.1016/j.jbc.2024.107905 · 2024 (bidnenko2024complexsporulationspecificexpression pages 1-2) | Bacillus-specific causal inference from Rho study. |
| SigF | activates | SigE in mother cell | Bacillus subtilis | “SigF activated first in the forespore; SigE activation in the mother cell depends on SigF” | 10.1016/j.jbc.2024.107905 · https://doi.org/10.1016/j.jbc.2024.107905 · 2024 (bidnenko2024complexsporulationspecificexpression pages 1-2) | Core sigma-cascade edge. |
| SigG | drives | spore DNA protection via Ssp proteins | Bacillus subtilis | “σG drives spore maturation and ‘spore DNA protection via Ssp proteins’” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Strong late-sporulation edge. |
| SigK | controls | spore coat and cortex maturation | Bacillus subtilis | “mother-cell ‘σK’ controls spore coat and cortex maturation and mother-cell lysis” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Strong late morphogenesis edge. |
| SigK | promotes | mother-cell lysis | Bacillus subtilis | “σK controls spore coat and cortex maturation and mother-cell lysis” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Strong late-stage edge. |
| Asymmetric division | produces | mother cell + forespore | Bacillus subtilis, Clostridioides difficile, general endospores | “via an asymmetric division into a forespore and mother cell” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Central defining morphogenesis edge. |
| SpoIIIE | mediates | chromosome translocation | Bacillus subtilis | “recruitment of ‘SpoIIIE’ for chromosome translocation” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Strong morphogenetic edge. |
| Forespore engulfment | creates | cell-within-a-cell state | Bacillus subtilis | “forespore engulfment, creating a cell-within-a-cell state” | 10.1038/s41467-024-51654-6 · https://doi.org/10.1038/s41467-024-51654-6 · 2024 (iwanska2024translationinbacillus pages 1-2) | Strong morphological edge. |
| Spore coat/cortex/exosporium deposition | confers | heat and chemical resistance | Clostridioides difficile / general endospores | “deposition of cortex, coat and exosporium (conferring heat and chemical resistance)” | 10.1038/s42003-024-06521-x · https://doi.org/10.1038/s42003-024-06521-x · 2024 (cassona2024sporesofclostridioides pages 1-2) | Strong structural-resistance edge; exosporium not universal across all taxa. |
| Clostridial OHKs | directly phosphorylate | Spo0A | Clostridia | “several clostridial OHKs have been shown to directly phosphorylate Spo0A in vitro” | 10.1128/mbio.02248-23 · https://doi.org/10.1128/mbio.02248-23 · 2024 (gohari2024theimpactof pages 1-2) | Broad clostridial model; species-specific kinase identities vary. |
| PtpA/PtpB | inhibit | Spo0A activity and sporulation | Clostridioides difficile | “PtpA and PtpB act primarily as phosphatases… that inhibit Spo0A activity and repress sporulation” | 10.1128/mbio.02248-23 · https://doi.org/10.1128/mbio.02248-23 · 2024 (gohari2024theimpactof pages 8-10) | Strong negative-regulation edge in C. difficile. |
| σG + SpoVT | control | tcdR production in forespore | Clostridioides difficile | “the forespore-specific regulatory proteins σG and SpoVT control TcdR production” | 10.1038/s42003-024-06521-x · https://doi.org/10.1038/s42003-024-06521-x · 2024 (cassona2024sporesofclostridioides pages 1-2) | Strong lineage-specific edge tying sporulation compartment to toxin regulation. |
| TcdR | is essential for expression of | tcdA/tcdB and tcdE | Clostridioides difficile | “TcdR, an auto-regulatory RNA polymerase sigma factor essential for tcdA/B and tcdE expression” | 10.1038/s42003-024-06521-x · https://doi.org/10.1038/s42003-024-06521-x · 2024 (cassona2024sporesofclostridioides pages 1-2) | Relevant only for pathogenic C. difficile; not a general sporulation trait edge. |
| Bacillus spore-based probiotic 2 × 10^9 cfu/day for 4 weeks | increases | myeloid/monocyte activation and phagocytosis markers | Human application (B. subtilis CU1) | “88 participants… dosed at 2 × 10^9 cfu/day for 4 weeks… higher percentages of myeloid cells, increased CD69 expression on monocytes” | 10.1163/18762891-bja00028 · https://doi.org/10.1163/18762891-bja00028 · 2024 (mourey2024theprobioticstrain pages 1-2) | Application edge, not core mechanistic sporulation biology. |
| Spore-based probiotic 4 billion spores for 45 days | alters | post-prandial GI-associated mRNA expression | Human application (mixed Bacillus spores) | “containing 4 billion spores… completed 45 days of supplementation” | 10.3390/biomedicines12102386 · https://doi.org/10.3390/biomedicines12102386 · 2024 (mcfarlin2024oralsporebasedprobiotic pages 2-4) | Small trial (n=20); outcome is biomarker-level, not direct clinical efficacy. |
| Baking at 180 °C for 20 min | causes | ~2 log CFU/g reduction in Bacillus spores | Food-processing application | “baking at 180 ◦C for 20 min caused ~2 log CFU/g reduction for most strains” | 10.3390/foods13152444 · https://doi.org/10.3390/foods13152444 · 2024 (payne2024thepotentialof pages 3-5) | Application edge; strain and matrix specific. |
| Feed pelletization at 80–85 °C | is tolerated by | Bacillus spores | Feed/food-processing application | “resist high temperatures encountered in feed processing — explicitly tolerating pelletization at ‘80 to 85 ◦C’” | 10.3390/bacteria3030017 · https://doi.org/10.3390/bacteria3030017 · 2024 (crivelli2024thecomplexand pages 8-9) | Application/property edge; not direct sporulation mechanism. |


*Table: This table lists candidate evidence-backed subject–predicate–object edges for curating a microbial endospore sporulation TraitMech graph. It spans core Bacillus and Clostridia regulation, morphogenesis, lineage-specific toxin/sporulation links, and selected real-world application edges with direct source snippets.*

### 5) Recent developments and latest research highlights (2023–2024)

1. **Translational control during sporulation (Nature Communications, 2024).** Ribosome profiling and imaging identify translation silencing events and spatiotemporal ribosome localization changes across sporulation, connecting translational control to delayed sporulation and reduced germination efficiency in ribosomal protein paralog mutants. (iwanska2024translationinbacillus pages 1-2, iwanska2024translationinbacillus media 8e8b0f73)

2. **Plasmid-encoded regulation of Spo0 phosphorelay (Nature Communications, 2024).** RapP (pBS32) dephosphorylates Spo0F and constrains premature Spo0A‑mediated adaptive responses, highlighting mobile genetic elements shaping sporulation/biofilm tradeoffs and growth economics. (zhu2024plasmidencodedphosphataserapp pages 1-2)

3. **Mechanistic diversity of clostridial initiation (mBio, 2024).** Updated synthesis that some clostridia encode relay‑like components but many rely on OHKs; phosphotransfer proteins can act as phosphatases that reduce sporulation; and C. difficile inhibitory PtpA/PtpB systems are prominent while activating kinases remain unclear. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 8-10)

4. **Sporulation-to-virulence coupling (Communications Biology, 2024).** Toxin sigma factor module expression is shown in sporulating subpopulations; forespore regulators σG and SpoVT control TcdR production and downstream toxin expression, and toxin is detected at the spore surface supporting spores as toxin-delivery vehicles. (cassona2024sporesofclostridioides pages 1-2)

### 6) Current applications and real-world implementations

#### 6.1 Spore-forming probiotics (food and clinical)

**Clinical dosing and immune readouts.** A 2024 clinical study administered *Bacillus subtilis* CU1 at **2×10^9 CFU/day for 4 weeks** to **88 participants**, reporting immune‑priming signatures (e.g., increased myeloid/monocyte activation and enhanced phagocytosis), with reduced basal cytokines in the elderly subgroup. (mourey2024theprobioticstrain pages 1-2)

**Spore-based supplement trial design and dose.** A 2024 randomized, double‑blind study used a commercially formulated product with **4 billion spores** (five Bacillus species) for **45 days** in **n=20** (10 probiotic/10 placebo), assessing 579 immune-related mRNAs after a high‑fat meal challenge. (mcfarlin2024oralsporebasedprobiotic pages 2-4)

**Food processing resilience and product incorporation.** A 2024 Foods review emphasizes that Bacillus spores survive processing conditions that reduce viability of vegetative probiotics, enabling incorporation into baked goods and other matrices. Quantitatively, baking at **180 °C for 20 min** produced approximately **~2 log CFU/g reduction** for most Bacillus strains in one evaluation. (payne2024thepotentialof pages 3-5)

#### 6.2 Food safety and spore control

**Thermal processing and storage impacts (quantitative).** In sausage storage up to **45 days**, *B. subtilis* var. Natto ATCC 15245 decreased from **9.82 to 8.50 log CFU/g**, and *B. coagulans* ATCC 31284 from **9.26 to 8.78 log CFU/g**; inoculation before processing followed by cooking produced **3–4 log reductions**. (payne2024thepotentialof pages 17-18)

**High hydrostatic pressure (HHP) (quantitative).** A 2024 review compiles spore inactivation data, e.g., *Bacillus cereus* at **600 MPa, 5 min, 70 °C → 3.0 log reduction**, and *Clostridium botulinum* at **750 MPa, 10 min, 75 °C → 5.6 log reduction**, while some matrices show minimal inactivation even at high pressure/temperature combinations. (shymialevich2024thenovelconcept pages 7-8)

#### 6.3 Industrial/bioprocess use: spore production optimization

A 2024 Heliyon study optimized medium C:N ratio (8.57:1) to achieve a maximum spore concentration of **1.05×10^8 CFU/mL** (~8.76‑fold vs basal medium) for a Bacillus sp. strain, illustrating how sporulation is engineered as a manufacturable output. (jaiaue2024inactivationofguanylate pages 2-3)

### 7) Expert synthesis and analysis (authoritative viewpoints)

- **Bacillus as a model of a layered regulatory system.** Spo0A integrates signals from kinases, phosphorelay components, and phosphatases; changes in Spo0A flux can bias cells toward sporulation versus alternative stationary‑phase programs (biofilm/cannibalism/competence). (gohari2024theimpactof pages 2-5, zhu2024plasmidencodedphosphataserapp pages 1-2)
- **Clostridia: mechanistic pluralism.** The field consensus in 2024 is that clostridial sporulation initiation is **not explained by a single conserved pathway**, with direct OHK→Spo0A phosphorylation common and phosphatase-like regulators frequently shaping Spo0A activity. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 8-10)
- **New regulatory layers.** 2023–2024 work elevates translational control (EF‑P; ribosome dynamics) and transcription termination (Rho) as important modifiers of when cells commit to sporulation and the resulting spore quality. (feaga2023elongationfactorp pages 1-2, iwanska2024translationinbacillus pages 1-2, bidnenko2024complexsporulationspecificexpression pages 1-2)

### 8) Ontology grounding suggestions (non-exhaustive)

- **GO biological processes:** sporulation (GO:0043934), endospore formation/biogenesis-related terms; transcription regulation; phosphorylation (GO:0016310); stringent response (GO:0009245). (iwanska2024translationinbacillus pages 1-2, zhu2024plasmidencodedphosphataserapp pages 2-3)
- **ENVO:** stationary phase / nutrient limitation context (ENVO:01000355 used as a placeholder for growth phase environment). (iwanska2024translationinbacillus pages 1-2)
- **CHEBI:** bile salts (CHEBI:3098) and gastric acid context for probiotic applications. (mourey2024theprobioticstrain pages 1-2, crivelli2024thecomplexand pages 8-9)

### 9) Curation warnings (do-not-curate-yet / uncertainty flags)

1. **Cross‑taxon portability is limited.** Bacillus phosphorelay edges (Spo0F/Spo0B) should not be assumed for pathogenic Clostridia where relay components are often absent; curate those edges with explicit taxon constraints. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 2-5)
2. **Edges derived from review-style summaries.** Some phosphorelay descriptions in application/secondary‑metabolism papers are background; prioritize primary mechanistic studies when selecting final YAML edges. (liu2023transcriptionfactorspo0a pages 1-2)
3. **Application edges are context specific.** Processing log‑reductions, HHP outcomes, and probiotic immune outcomes are strain‑, matrix‑, and protocol‑dependent; include assay nodes and conditions when curating to avoid overgeneralization. (payne2024thepotentialof pages 17-18, shymialevich2024thenovelconcept pages 7-8, mourey2024theprobioticstrain pages 1-2)
4. **Virulence-to-sporulation coupling is lineage specific.** TcdR/toxin expression during sporulation is specific to *C. difficile* and should be curated as a taxon‑restricted subgraph rather than a generic sporulation mechanism. (cassona2024sporesofclostridioides pages 1-2)

---

## DOI-first bibliography (2023–2024 prioritized)

- Iwańska O, et al. *Translation in Bacillus subtilis is spatially and temporally coordinated during sporulation*. **Nature Communications** (Aug 2024). DOI: **10.1038/s41467-024-51654-6**. URL: https://doi.org/10.1038/s41467-024-51654-6 (iwanska2024translationinbacillus pages 1-2)
- Zhu M, et al. *Plasmid-encoded phosphatase RapP enhances cell growth in non-domesticated Bacillus subtilis strains*. **Nature Communications** (Nov 2024). DOI: **10.1038/s41467-024-53992-x**. URL: https://doi.org/10.1038/s41467-024-53992-x (zhu2024plasmidencodedphosphataserapp pages 1-2)
- Gohari IM, et al. *The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation*. **mBio** (Apr 2024). DOI: **10.1128/mbio.02248-23**. URL: https://doi.org/10.1128/mbio.02248-23 (gohari2024theimpactof pages 1-2)
- Cassona CP, et al. *Spores of Clostridioides difficile are toxin delivery vehicles*. **Communications Biology** (Jul 2024). DOI: **10.1038/s42003-024-06521-x**. URL: https://doi.org/10.1038/s42003-024-06521-x (cassona2024sporesofclostridioides pages 1-2)
- Bidnenko V, et al. *Complex sporulation-specific expression of transcription termination factor Rho highlights its involvement in Bacillus subtilis cell differentiation*. **J Biol Chem** (Dec 2024). DOI: **10.1016/j.jbc.2024.107905**. URL: https://doi.org/10.1016/j.jbc.2024.107905 (bidnenko2024complexsporulationspecificexpression pages 1-2)
- Feaga HA, et al. *Elongation Factor P Is Important for Sporulation Initiation*. **Journal of Bacteriology** (Feb 2023). DOI: **10.1128/jb.00370-22**. URL: https://doi.org/10.1128/jb.00370-22 (feaga2023elongationfactorp pages 1-2)
- Mourey F, et al. *The probiotic strain Bacillus subtilis CU1 primes antimicrobial innate immune response and reduces low-grade inflammation: a clinical study*. **Beneficial Microbes** (Aug 2024). DOI: **10.1163/18762891-bja00028**. URL: https://doi.org/10.1163/18762891-bja00028 (mourey2024theprobioticstrain pages 1-2)
- McFarlin BK, et al. *Oral Spore-Based Probiotic Supplementation Alters Post-Prandial Expression of mRNA Associated with Gastrointestinal Health*. **Biomedicines** (Oct 2024). DOI: **10.3390/biomedicines12102386**. URL: https://doi.org/10.3390/biomedicines12102386 (mcfarlin2024oralsporebasedprobiotic pages 2-4)
- Payne J, et al. *The Potential of Bacillus Species as Probiotics in the Food Industry: A Review*. **Foods** (Aug 2024). DOI: **10.3390/foods13152444**. URL: https://doi.org/10.3390/foods13152444 (payne2024thepotentialof pages 3-5)
- Shymialevich D, et al. *The Novel Concept of Synergically Combining: High Hydrostatic Pressure and Lytic Bacteriophages to Eliminate Vegetative and Spore-Forming Bacteria in Food Products*. **Foods** (Aug 2024). DOI: **10.3390/foods13162519**. URL: https://doi.org/10.3390/foods13162519 (shymialevich2024thenovelconcept pages 7-8)
- Jaiaue P, et al. *Inactivation of guanylate kinase in Bacillus sp. TL7-3… influenced GTP regeneration capability and sporulation*. **Heliyon** (Jun 2024). DOI: **10.1016/j.heliyon.2024.e31956**. URL: https://doi.org/10.1016/j.heliyon.2024.e31956 (jaiaue2024inactivationofguanylate pages 2-3)
- Liu N, et al. *Transcription Factor Spo0A Regulates the Biosynthesis of Difficidin in Bacillus amyloliquefaciens*. **Microbiology Spectrum** (Aug 2023). DOI: **10.1128/spectrum.01044-23**. URL: https://doi.org/10.1128/spectrum.01044-23 (liu2023transcriptionfactorspo0a pages 1-2)
- Crivelli XB, et al. *The Complex and Changing Genus Bacillus: A Diverse Bacterial Powerhouse for Many Applications*. **Bacteria** (Sep 2024). DOI: **10.3390/bacteria3030017**. URL: https://doi.org/10.3390/bacteria3030017 (crivelli2024thecomplexand pages 8-9)



References

1. (iwanska2024translationinbacillus pages 1-2): Olga Iwańska, Przemysław Latoch, Natalia Kopik, Mariia Kovalenko, Małgorzata Lichocka, Remigiusz Serwa, and Agata L. Starosta. Translation in bacillus subtilis is spatially and temporally coordinated during sporulation. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51654-6, doi:10.1038/s41467-024-51654-6. This article has 19 citations and is from a highest quality peer-reviewed journal.

2. (cassona2024sporesofclostridioides pages 1-2): Carolina P. Cassona, Sara Ramalhete, Khira Amara, Thomas Candela, Imad Kansau, Cécile Denève-Larrazet, Claire Janoir-Jouveshomme, Luís Jaime Mota, Bruno Dupuy, Mónica Serrano, and Adriano O. Henriques. Spores of clostridioides difficile are toxin delivery vehicles. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06521-x, doi:10.1038/s42003-024-06521-x. This article has 3 citations and is from a peer-reviewed journal.

3. (bidnenko2024complexsporulationspecificexpression pages 1-2): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (anjou2024themultiplicityof pages 18-20): Cyril Anjou, Aurélie Lotoux, Anna Zhukova, Marie Royer, Léo C. Caulat, Elena Capuzzo, Claire Morvan, and Isabelle Martin-Verstraete. The multiplicity of thioredoxin systems meets the specific lifestyles of clostridia. PLOS Pathogens, 20:e1012001, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012001, doi:10.1371/journal.ppat.1012001. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (gohari2024theimpactof pages 2-5): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (zhu2024plasmidencodedphosphataserapp pages 1-2): Manlu Zhu, Yiheng Wang, Haoyan Mu, Fei Han, Qian Wang, Yongfu Pei, Xin Wang, and Xiongfeng Dai. Plasmid-encoded phosphatase rapp enhances cell growth in non-domesticated bacillus subtilis strains. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53992-x, doi:10.1038/s41467-024-53992-x. This article has 11 citations and is from a highest quality peer-reviewed journal.

7. (gohari2024theimpactof pages 1-2): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (feaga2023elongationfactorp pages 1-2): Heather A. Feaga, Hye-Rim Hong, Cassidy R. Prince, Ananda Rankin, Allen R. Buskirk, and Jonathan Dworkin. Elongation factor p is important for sporulation initiation. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00370-22, doi:10.1128/jb.00370-22. This article has 17 citations and is from a peer-reviewed journal.

9. (liu2023transcriptionfactorspo0a pages 1-2): Na Liu, Huiwan Sun, Zhengyu Tang, Yuqing Zheng, Gaofu Qi, and Xiuyun Zhao. Transcription factor spo0a regulates the biosynthesis of difficidin in bacillus amyloliquefaciens. Aug 2023. URL: https://doi.org/10.1128/spectrum.01044-23, doi:10.1128/spectrum.01044-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (iwanska2024translationinbacillus media 8e8b0f73): Olga Iwańska, Przemysław Latoch, Natalia Kopik, Mariia Kovalenko, Małgorzata Lichocka, Remigiusz Serwa, and Agata L. Starosta. Translation in bacillus subtilis is spatially and temporally coordinated during sporulation. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51654-6, doi:10.1038/s41467-024-51654-6. This article has 19 citations and is from a highest quality peer-reviewed journal.

11. (iwanska2024translationinbacillus media 77a6be13): Olga Iwańska, Przemysław Latoch, Natalia Kopik, Mariia Kovalenko, Małgorzata Lichocka, Remigiusz Serwa, and Agata L. Starosta. Translation in bacillus subtilis is spatially and temporally coordinated during sporulation. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51654-6, doi:10.1038/s41467-024-51654-6. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (gohari2024theimpactof pages 14-15): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (zhu2024plasmidencodedphosphataserapp pages 2-3): Manlu Zhu, Yiheng Wang, Haoyan Mu, Fei Han, Qian Wang, Yongfu Pei, Xin Wang, and Xiongfeng Dai. Plasmid-encoded phosphatase rapp enhances cell growth in non-domesticated bacillus subtilis strains. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53992-x, doi:10.1038/s41467-024-53992-x. This article has 11 citations and is from a highest quality peer-reviewed journal.

14. (gohari2024theimpactof pages 15-15): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (gangwal2023givingasignal pages 5-5): Aakriti Gangwal, Nishant Kumar, Nitika Sangwan, Neha Dhasmana, U. Dhawan, Andaleeb Sajid, G. Arora, and Y. Singh. Giving a signal: how protein phosphorylation helps bacillus navigate through different life stages. FEMS microbiology reviews, Aug 2023. URL: https://doi.org/10.1093/femsre/fuad044, doi:10.1093/femsre/fuad044. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (bidnenko2024complexsporulationspecificexpression pages 17-17): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 9 citations and is from a domain leading peer-reviewed journal.

17. (gohari2024theimpactof pages 12-14): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

18. (gohari2024theimpactof pages 6-8): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

19. (jaiaue2024inactivationofguanylate pages 15-16): Phetcharat Jaiaue, Piroonporn Srimongkol, Sitanan Thitiprasert, Jirabhorn Piluk, Jesnipit Thammaket, Suttichai Assabumrungrat, Benjamas Cheirsilp, Somboon Tanasupawat, and Nuttha Thongchul. Inactivation of guanylate kinase in bacillus sp. tl7-3 cultivated under an optimized ratio of carbon and nitrogen sources influenced gtp regeneration capability and sporulation. Heliyon, 10:e31956, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e31956, doi:10.1016/j.heliyon.2024.e31956. This article has 0 citations.

20. (mourey2024theprobioticstrain pages 1-2): F. Mourey, P. Scholtens, J.-F. Jeanne, B. Rodriguez, A. Decherf, F. Machuron, A. Kardinaal, T. Scheithauer, M. Porbahaie, E. Narni-Mancinelli, and A. Crinier. The probiotic strain bacillus subtilis cu1 primes antimicrobial innate immune response and reduces low-grade inflammation: a clinical study. Beneficial microbes, 15:1-20, Aug 2024. URL: https://doi.org/10.1163/18762891-bja00028, doi:10.1163/18762891-bja00028. This article has 6 citations and is from a peer-reviewed journal.

21. (crivelli2024thecomplexand pages 8-9): Ximena Blanco Crivelli, Cecilia Cundon, María Paz Bonino, Mariana Soledad Sanin, and Adriana Bentancor. The complex and changing genus bacillus: a diverse bacterial powerhouse for many applications. Bacteria, 3:256-270, Sep 2024. URL: https://doi.org/10.3390/bacteria3030017, doi:10.3390/bacteria3030017. This article has 35 citations.

22. (payne2024thepotentialof pages 20-21): Jessie Payne, Danielle Bellmer, Ravi Jadeja, and Peter Muriana. The potential of bacillus species as probiotics in the food industry: a review. Foods, 13:2444, Aug 2024. URL: https://doi.org/10.3390/foods13152444, doi:10.3390/foods13152444. This article has 90 citations.

23. (payne2024thepotentialof pages 1-2): Jessie Payne, Danielle Bellmer, Ravi Jadeja, and Peter Muriana. The potential of bacillus species as probiotics in the food industry: a review. Foods, 13:2444, Aug 2024. URL: https://doi.org/10.3390/foods13152444, doi:10.3390/foods13152444. This article has 90 citations.

24. (mcfarlin2024oralsporebasedprobiotic pages 2-4): Brian K. McFarlin, Sarah E. Deemer, and Elizabeth A. Bridgeman. Oral spore-based probiotic supplementation alters post-prandial expression of mrna associated with gastrointestinal health. Biomedicines, 12:2386, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102386, doi:10.3390/biomedicines12102386. This article has 3 citations.

25. (payne2024thepotentialof pages 3-5): Jessie Payne, Danielle Bellmer, Ravi Jadeja, and Peter Muriana. The potential of bacillus species as probiotics in the food industry: a review. Foods, 13:2444, Aug 2024. URL: https://doi.org/10.3390/foods13152444, doi:10.3390/foods13152444. This article has 90 citations.

26. (gohari2024theimpactof pages 8-10): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

27. (payne2024thepotentialof pages 17-18): Jessie Payne, Danielle Bellmer, Ravi Jadeja, and Peter Muriana. The potential of bacillus species as probiotics in the food industry: a review. Foods, 13:2444, Aug 2024. URL: https://doi.org/10.3390/foods13152444, doi:10.3390/foods13152444. This article has 90 citations.

28. (shymialevich2024thenovelconcept pages 7-8): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 17 citations.

29. (jaiaue2024inactivationofguanylate pages 2-3): Phetcharat Jaiaue, Piroonporn Srimongkol, Sitanan Thitiprasert, Jirabhorn Piluk, Jesnipit Thammaket, Suttichai Assabumrungrat, Benjamas Cheirsilp, Somboon Tanasupawat, and Nuttha Thongchul. Inactivation of guanylate kinase in bacillus sp. tl7-3 cultivated under an optimized ratio of carbon and nitrogen sources influenced gtp regeneration capability and sporulation. Heliyon, 10:e31956, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e31956, doi:10.1016/j.heliyon.2024.e31956. This article has 0 citations.