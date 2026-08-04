---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:03:23.139128'
end_time: '2026-08-04T10:16:53.262802'
duration_seconds: 810.12
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
  causal_graph_summary: 'sporulation_spo0a_sigma_morphogenesis: 19 nodes, 13 edges'
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
- **Trait label:** sporulation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000870
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's ability to form dormant, stress-resistant endospores.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Physiology and metabolism.spore formation.spore formation
- **Existing evidence:** DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis process producing a spore within a sporangium.)
- **Existing causal graph summary:** sporulation_spo0a_sigma_morphogenesis: 19 nodes, 13 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000870
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's ability to form dormant, stress-resistant endospores.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Physiology and metabolism.spore formation.spore formation
- **Existing evidence:** DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis process producing a spore within a sporangium.)
- **Existing causal graph summary:** sporulation_spo0a_sigma_morphogenesis: 19 nodes, 13 edges

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


# Curation-focused research report: bacterial sporulation

## 1. Scope and recommended interpretation

**Target trait:** sporulation  
**Trait identifier:** **`METPO:1000870`**  
**Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED  
**Parent:** `METPO:1000059`

For this graph, sporulation should mean the **capacity of a vegetative bacterial cell to execute endospore-forming differentiation**, culminating in a dormant endospore. In the canonical *Bacillus* sequence, starvation or nutrient limitation activates Spo0A, followed by asymmetric septation, formation of mother-cell and forespore compartments, forespore engulfment, cortex and coat assembly, core maturation, mother-cell lysis, and release of the mature spore. A recent review describes seven morphological stages and the ordered σF–σE–σG–σK program; a 2024 primary study reports that the post-septation program takes approximately six hours in *Bacillus subtilis* and becomes irreversible after asymmetric division. (m.2023sporulationstructureassembly pages 4-6, updegrove2024altruisticfeedingand pages 1-2)

### Boundaries

Include:

- initiation of bacterial **endospore formation**;
- developmental asymmetric division and forespore morphogenesis;
- compartment-specific transcription and intercellular signaling;
- cortex, coat, and core maturation insofar as they are necessary to produce an endospore;
- mother-cell lysis and spore release.

Keep separate or model only as downstream/modifier branches:

- **germination and outgrowth**, which convert a dormant spore back to vegetative growth;
- **spore resistance**, persistence, and dormancy, which are products/properties of a mature spore rather than sporulation itself;
- bacterial **exospore** formation, fungal sporulation, conidiation, fruiting-body development, cyst formation, and akinetes. Endospore and exospore formation involve distinct, likely independently evolved pathways despite sharing nutrient limitation and extensive envelope remodeling. (beskrovnaya2021structuralmetabolicand pages 2-3)

Accordingly, the existing definition—“an organism’s ability to form dormant, stress-resistant endospores”—is appropriate, but the causal graph should terminate at **mature endospore formation/release**, with dormancy and resistance represented as downstream consequences.

## 2. Candidate nodes grouped by type

### Environmental and experimental inputs

- nutrient limitation / starvation;
- transition to stationary phase;
- sporulation-inducing medium or nutrient downshift;
- population-level glycerol signal/nutrient;
- favorable nutrient influx, as an antagonist after starvation but before commitment;
- heat, desiccation, radiation, disinfectants, and preservatives—**assay factors for mature-spore resistance, not primary sporulation triggers**.

Starvation is strongly supported as a trigger, but the immediate biochemical input to individual Kin proteins remains context dependent. Sporulation integrates multiple environmental and metabolic cues through the phosphorylation state of Spo0A. (gohari2024theimpactof pages 1-2, updegrove2024altruisticfeedingand pages 1-2)

### Regulatory proteins and signaling modules

- KinA, KinB and other sporulation-associated histidine kinases;
- Spo0F, Spo0B, Spo0A, and phosphorylated Spo0A (`Spo0A~P`);
- Rap phosphatases/Phr peptide regulators and Spo0E-family phosphatases;
- σH/SigH;
- SpoIIE, SpoIIAA, SpoIIAB, σF/SigF;
- SpoIIR, SpoIIGA, pro-σE, σE/SigE;
- SpoIIIA proteins and SpoIIQ transenvelope complex;
- σG/SigG;
- pro-σK and σK/SigK; SpoIVB–BofA–SpoIVFA–SpoIVFB should remain provisional unless separately evidenced in the target source set;
- Rho transcription-termination factor;
- ShfA/YabQ and ShfP/YvnB.

### Morphogenesis and envelope-remodeling entities

- polar/asymmetric septum;
- mother cell and forespore;
- FtsZ/divisome—process-level candidate;
- SpoIID, SpoIIM, SpoIIP engulfment machinery;
- SpoIIIA–SpoIIQ transenvelope channel;
- SpoVE and SpoVD;
- *Clostridioides difficile* dcw-encoded sporulation PG synthases;
- forespore engulfment and membrane fission;
- cortex peptidoglycan;
- spore coat and coat proteins, including CotB, CotH, CotO, and CotE in *Bacillus thuringiensis*;
- SpoIVA and SpoVM as label-only coat-morphogenesis candidates pending direct edge evidence;
- CwlC mother-cell hydrolase in *B. thuringiensis*;
- mature endospore and spore release.

### Chemicals and metabolites

- phosphate/phosphoryl group;
- ATP/ADP—only if the kinase reaction is modeled explicitly;
- peptidoglycan and lipid II;
- dipicolinic acid, calcium ion, and calcium dipicolinate (Ca-DPA);
- glycerol;
- glycogen;
- water/core dehydration and small acid-soluble spore proteins (SASPs)—important maturation nodes, but direct edges should await source-specific evidence.

Useful ontology candidates include **CHEBI:17754** for glycerol, **CHEBI:29108** for calcium(2+), and **CHEBI:36342** for dipicolinic acid. These should be checked against the exact chemical form used in the YAML, particularly free DPA versus calcium dipicolinate.

### Processes and localizations

Potential GO-grounded concepts, subject to identifier verification before commit, include:

- sporulation resulting in formation of a cellular spore;
- establishment of cell polarity;
- asymmetric cell division;
- forespore engulfment;
- peptidoglycan biosynthesis/remodeling;
- spore-wall/cortex and coat assembly;
- protein phosphorylation and phosphorelay signaling;
- mother-cell lysis;
- forespore, mother-cell, septal membrane, intermembrane space, spore cortex, coat, and core.

Use the supplied trait identifier verbatim—**`METPO:1000870`**—and do not manufacture METPO, GO, UniProt, KEGG, or Rhea identifiers. Protein-name nodes are preferable to an incorrect cross-species UniProt accession.

## 3. Candidate causal graph architecture

The recommended conserved backbone is:

**starvation/nutrient limitation → elevated Spo0A~P → sporulation initiation → polar asymmetric septation → σF activation in forespore → SpoIIR signal → σE activation in mother cell → engulfment/morphogenesis → SpoIIIA–SpoIIQ-supported forespore transcription and σG → late mother-cell σK program → cortex/coat/core maturation → mother-cell lysis → mature endospore release → `METPO:1000870`.**

The *B. subtilis* phosphorelay can be represented as **KinA/KinB → Spo0F~P → Spo0B~P → Spo0A~P**. This should not be asserted as universal across Clostridia. (gohari2024theimpactof pages 1-2, beskrovnaya2021structuralmetabolicand pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18)

The following artifact summarizes the strongest edges:

| subject | predicate | object | taxon/scope | evidence strength | DOI |
|---|---|---|---|---|---|
| starvation / nutrient limitation | triggers | sporulation | bacterial endospore formers; especially *Bacillus subtilis* and Clostridia | strong review/primary consensus (gohari2024theimpactof pages 1-2, updegrove2024altruisticfeedingand pages 1-2) | 10.1128/mbio.02248-23; 10.1126/sciadv.adq0791 |
| KinA, KinB | phosphorylate via Spo0F | Spo0B→Spo0A phosphorelay | *Bacillus subtilis* / Bacilli | strong canonical, review-supported (beskrovnaya2021structuralmetabolicand pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | 10.3389/fmicb.2021.630573; 10.3390/microorganisms11081928 |
| Spo0A~P | initiates | sporulation program | endospore-forming bacteria | strong consensus (gohari2024theimpactof pages 1-2, updegrove2024altruisticfeedingand pages 1-2, beskrovnaya2021structuralmetabolicand pages 2-3) | 10.1128/mbio.02248-23; 10.1126/sciadv.adq0791; 10.3389/fmicb.2021.630573 |
| Spo0A~P | promotes | asymmetric division / asymmetric septation | *Bacillus subtilis* | strong, but process-level | 10.1126/sciadv.adq0791 |
| SpoIIE | activates | sigma F | *Bacillus subtilis* / Bacilli | strong canonical (jun2023timecoursetranscriptomeanalysis pages 17-18, m.2023sporulationstructureassembly pages 20-21) | 10.3390/microorganisms11081928; 10.3390/microbiolres14020035 |
| sigma F | induces | SpoIIR | *Bacillus subtilis* | strong canonical (meeske2016highthroughputgeneticscreens pages 18-20) | 10.1371/journal.pbio.1002341 |
| SpoIIR | activates via SpoIIGA processing | sigma E | *Bacillus subtilis* | strong canonical (meeske2016highthroughputgeneticscreens pages 18-20) | 10.1371/journal.pbio.1002341 |
| sigma F and sigma E | promote engulfment via | SpoIID, SpoIIM, SpoIIP | *Bacillus* spp. | strong canonical/review-supported (jun2023timecoursetranscriptomeanalysis pages 17-18, m.2023sporulationstructureassembly pages 4-6) | 10.3390/microorganisms11081928; 10.3390/microbiolres14020035 |
| SpoIIIA-SpoIIQ complex | maintains | forespore transcriptional potential / sigma G activity | *Bacillus subtilis* | strong (meeske2016highthroughputgeneticscreens pages 16-18) | 10.1371/journal.pbio.1002341 |
| sigma F → sigma E → sigma G → sigma K | drives | compartment-specific sporulation gene expression | *Bacillus* spp. / Bacilli | strong consensus (m.2023sporulationstructureassembly pages 4-6, jun2023timecoursetranscriptomeanalysis pages 17-18) | 10.3390/microbiolres14020035; 10.3390/microorganisms11081928 |
| SpoVA proteins | mediate uptake of | Ca-dipicolinic acid (Ca-DPA) into spore core | *Bacillus* spp. | strong review-supported (m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 |
| cortex and coat assembly | enables formation of | mature resistant spore | endospore-forming Bacilli | strong consensus (m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 |
| mother-cell hydrolase CwlC | promotes | mother-cell lysis / spore release | *Bacillus thuringiensis* | moderate; taxon-specific direct evidence (m.2023sporulationstructureassembly pages 20-21) | 10.3390/microbiolres14020035 |
| ShfA, ShfP | promote release of | glycerol | *Bacillus subtilis* | strong new primary evidence (updegrove2024altruisticfeedingand pages 1-2, updegrove2024altruisticfeedingand pages 3-4) | 10.1126/sciadv.adq0791 |
| glycerol released by early sporulating cells | delays | sporulation in neighboring nonsporulating cells | *Bacillus subtilis* population heterogeneity | strong new primary evidence (updegrove2024altruisticfeedingand pages 1-2) | 10.1126/sciadv.adq0791 |
| dcw-encoded PG synthases (specialized FtsW/FtsI-related machinery) | synthesize | septal peptidoglycan during sporulation-specific division | *Clostridioides difficile* | strong new primary evidence; taxon-specific (shrestha2023diversificationofdivision pages 1-2) | 10.1038/s41467-023-43595-3 |
| clostridial orphan histidine kinases (OHKs) | phosphorylate / regulate | Spo0A | Clostridia | moderate; mechanistically diverse, not universal (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 5-6) | 10.1128/mbio.02248-23 |
| candidate clostridial phosphotransfer proteins / phosphatases | reduce | sporulation / Spo0A activation state | some Clostridia | moderate; caveated, lineage-specific (gohari2024theimpactof pages 1-2) | 10.1128/mbio.02248-23 |
| sporulation-specific rho expression | supports | normal spore morphology and efficient revival/outgrowth | *Bacillus subtilis* | strong new primary evidence (bidnenko2024complexsporulationspecificexpression pages 6-7, bidnenko2024complexsporulationspecificexpression pages 3-4) | 10.1016/j.jbc.2024.107905 |
| glycogen accumulation | increases | spore resilience / structural integrity | *Clostridioides difficile* | strong new primary evidence; no effect on sporulation rate (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3, hasan2024roleofglycogen pages 5-7) | 10.1128/msphere.00310-24 |
| glycogen accumulation | does not significantly change | sporulation rate | *Clostridioides difficile* | strong new primary evidence (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3) | 10.1128/msphere.00310-24 |


*Table: This table lists the strongest curation-ready causal edges for bacterial endospore sporulation, emphasizing well-supported mechanisms and highlighting taxon-specific or caveated relationships. It is designed to help prioritize nodes and edges for TraitMech graph assembly.*

## 4. Evidence-backed edges with supporting snippets

| Subject | Predicate | Object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|---|
| nutrient starvation | triggers | endospore formation | “Starvation triggers bacterial spore formation” | Updegrove et al., 2024, DOI: [10.1126/sciadv.adq0791](https://doi.org/10.1126/sciadv.adq0791) | Strong in *B. subtilis*; general “nutrient limitation” is safer than a specific missing nutrient. (updegrove2024altruisticfeedingand pages 1-2) |
| Kin proteins | phosphorylate | Spo0F | “Kin proteins phosphorylating Spo0F” | Beskrovnaya et al., 2021, DOI: [10.3389/fmicb.2021.630573](https://doi.org/10.3389/fmicb.2021.630573) | Canonical *B. subtilis* phosphorelay. (beskrovnaya2021structuralmetabolicand pages 2-3) |
| Spo0F~P | transfers phosphoryl group to | Spo0B | “Spo0F…transfers phosphate to Spo0B” | Same | Canonical Bacilli edge. (beskrovnaya2021structuralmetabolicand pages 2-3) |
| Spo0B~P | phosphorylates | Spo0A | “Spo0B…then phosphorylates Spo0A” | Same | Canonical Bacilli edge. (beskrovnaya2021structuralmetabolicand pages 2-3) |
| Spo0A phosphorylation | activates | Spo0A DNA-binding regulation | Spo0A’s DNA-binding domain is activated by phosphorylation at a conserved aspartate | Gohari et al., 2024, DOI: [10.1128/mbio.02248-23](https://doi.org/10.1128/mbio.02248-23) | Strong and broadly conserved. (gohari2024theimpactof pages 1-2) |
| Spo0A~P | dimerizes and binds | 0A-box-containing promoters | “Spo0A~P dimerizes and directly binds…‘0A boxes’” | Same | Molecularly precise transcriptional edge. (gohari2024theimpactof pages 1-2) |
| elevated Spo0A~P | initiates | sporulation | “Once…the pool…reaches a high enough threshold, sporulation initiates” | Updegrove et al., 2024 | Strong; threshold is biological, not a fixed concentration. (updegrove2024altruisticfeedingand pages 1-2) |
| sporulation initiation | causes | asymmetric division | “An early hallmark…is the asymmetric division…[into] a larger mother cell and a smaller forespore” | Same | Strong process edge. (updegrove2024altruisticfeedingand pages 1-2) |
| SpoIIE phosphatase | dephosphorylates | SpoIIAA | “SpoIIE phosphatase…dephosphorylates SpoIIAA” | Jun et al., 2023, DOI: [10.3390/microorganisms11081928](https://doi.org/10.3390/microorganisms11081928) | This releases σF from anti-sigma-factor control; the latter step should be added only with direct evidence. (jun2023timecoursetranscriptomeanalysis pages 17-18) |
| σF | induces | SpoIIR | “SpoIIR, a secreted signaling protein made in the forespore under σF control” | Meeske et al., 2016, DOI: [10.1371/journal.pbio.1002341](https://doi.org/10.1371/journal.pbio.1002341) | Strong *B. subtilis* edge. (meeske2016highthroughputgeneticscreens pages 18-20) |
| SpoIIR | promotes SpoIIGA processing of | pro-σE | SpoIIR signal and septal SpoIIGA protease “processes pro-σE” | Same | Strong intercompartmental signaling edge. (meeske2016highthroughputgeneticscreens pages 18-20) |
| SpoIIGA-mediated processing | activates | σE | “SpoIIGA protease…activates Pro-SigE” | Jun et al., 2023 | Strong. (jun2023timecoursetranscriptomeanalysis pages 17-18) |
| σF and σE programs | promote via SpoIID/IIM/IIP | forespore engulfment | mutations in `spoIID`, `spoIIM`, and `spoIIP` impair the morphological changes of engulfment | Guerrero, 2023, DOI: [10.3390/microbiolres14020035](https://doi.org/10.3390/microbiolres14020035) | Strong in Bacilli; model individual hydrolase activities only with primary biochemical evidence. (m.2023sporulationstructureassembly pages 4-6) |
| mother cell | engulfs | forespore | “the mother cell engulfs the forespore” | Updegrove et al., 2024 | Strong morphology edge. (updegrove2024altruisticfeedingand pages 1-2) |
| SpoIIIA–SpoIIQ complex | maintains | forespore transcriptional potential | complex “maintains transcriptional potential in the forespore” and transports proteins/metabolites | Meeske et al., 2016 | Strong, but avoid calling it a simple nutrient channel without qualification. (meeske2016highthroughputgeneticscreens pages 16-18) |
| SpoIIIA operon | required for | σG activation | `spoIIIAA–spoIIIAH` are “required for σG activation” | Jun et al., 2023 | Strong. (jun2023timecoursetranscriptomeanalysis pages 17-18) |
| σF/σE | regulate | early compartment-specific genes | “σE and σF regulate early sporulation genes in mother cell and forespore respectively” | Same | Strong. (jun2023timecoursetranscriptomeanalysis pages 17-18) |
| σG/σK | regulate | late sporulation genes | “σK and σG regulate late sporulation genes” | Same | Strong; specify forespore σG and mother-cell σK where supported. (jun2023timecoursetranscriptomeanalysis pages 17-18) |
| SpoVA proteins | mediate uptake of | Ca-DPA into the core | “SpoVA proteins mediate Ca2+-dipicolinic acid uptake during spore core maturation” | Guerrero, 2023 | Strong review-supported maturation edge. (m.2023sporulationstructureassembly pages 4-6) |
| cortex and coat assembly | contributes to | mature endospore formation | seven stages include “cortex and coat assembly” followed by maturation and lysis | Same | Strong process-level edge. (m.2023sporulationstructureassembly pages 4-6) |
| CwlC | promotes | mother-cell lysis | CwlC is a “cell wall hydrolase essential for mother cell lysis” | Guerrero, 2023 | Taxon-specific evidence from *B. thuringiensis*; do not universalize. (m.2023sporulationstructureassembly pages 20-21) |
| mother-cell lysis | releases | mature spore | “the mother cell lyses, which releases the now-mature spore” | Updegrove et al., 2024 | Strong terminal morphology edge. (updegrove2024altruisticfeedingand pages 1-2) |
| ShfA/ShfP pathway | releases | glycerol | early sporulating cells use a calcineurin-like phosphoesterase “to release glycerol” | Updegrove et al., 2024 | Strong new population-level branch in *B. subtilis*. (updegrove2024altruisticfeedingand pages 1-2) |
| glycerol | delays | sporulation in nonsporulating neighbors | glycerol “acts as a signaling molecule and a nutrient to delay nonsporulating cells” | Same | Strong but population-level; not part of the cell-autonomous core. (updegrove2024altruisticfeedingand pages 1-2) |
| *C. difficile* dcw PG synthases | synthesize | sporulation septal PG | specialized enzymes fulfill “sporulation-specific roles, including synthesizing septal PG” | Shrestha et al., 2023, DOI: [10.1038/s41467-023-43595-3](https://doi.org/10.1038/s41467-023-43595-3) | Strong primary evidence; explicitly taxon-specific. (shrestha2023diversificationofdivision pages 1-2) |
| reduced Rho during transition | supports | initiation/implementation of sporulation | reduction of Rho during transition is necessary for initiation and implementation; later compartmental expression refuels Rho | Bidnenko et al., 2024, DOI: [10.1016/j.jbc.2024.107905](https://doi.org/10.1016/j.jbc.2024.107905) | Biphasic regulation; do not encode simply as “Rho activates sporulation.” (bidnenko2024complexsporulationspecificexpression pages 6-7, bidnenko2024complexsporulationspecificexpression pages 3-4) |
| SigH/Spo0A-regulated read-through | increases | mother-cell rho expression | read-through from the upstream promoter accounts for “at least half” of rho expression during sporulation | Same | Strong quantitative transcriptional edge. (bidnenko2024complexsporulationspecificexpression pages 3-4) |
| SigF-dependent promoter | drives | forespore rho expression | “forespore-specific expression of rho depends on…SigFPrho” | Same | Strong compartment-specific edge. (bidnenko2024complexsporulationspecificexpression pages 6-7) |
| glycogen accumulation | supports | *C. difficile* spore resilience | glycogen accumulation, but not utilization, is required for resilience | Hasan et al., 2024, DOI: [10.1128/msphere.00310-24](https://doi.org/10.1128/msphere.00310-24) | Modifier of mature-spore quality, not sporulation itself. (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3) |
| glycogen synthesis loss | does not significantly alter | sporulation rate | mutant exhibited “no significant changes in the sporulation rate” | Same | Important negative edge; exclude glycogen as a core cause of sporulation. (hasan2024roleofglycogen pages 1-3) |

## 5. Recent developments and quantitative findings, 2023–2024

### Population-level control of commitment

The 2024 ShfA/ShfP study changes the simple picture in which sporulation heterogeneity arises only from stochastic Spo0A phosphorylation. Early sporulating *B. subtilis* cells release glycerol, which both feeds and signals neighboring nonsporulating cells, delaying their commitment and improving the population’s ability to exploit a sudden nutrient influx. The developmental program takes about **six hours** after asymmetric division and is described as irreversible at that stage. This branch is mechanistically important but should be modeled as **cell–cell modulation of sporulation timing**, not as an obligate core pathway. (updegrove2024altruisticfeedingand pages 1-2)

### Evolutionary diversification of the sporulation divisome

Shrestha et al. showed in 2023 that *C. difficile* lacks a canonical FtsW/FtsI pair for ordinary septal PG synthesis. Its dcw-encoded PG synthases are specialized for sporulation-specific septal PG synthesis and are dispensable for normal vegetative division, which instead depends on a bifunctional class-A PBP. This is authoritative evidence against assuming that the *B. subtilis* divisome architecture applies universally. (shrestha2023diversificationofdivision pages 1-2)

### Clostridial initiation is not governed by one universal route

The 2024 mBio review concludes that some Clostridia retain phosphorelay components, whereas several medically or industrially important lineages lack the classical Bacillus relay. Several orphan histidine kinases directly phosphorylate Spo0A in vitro, but other kinase-like phosphotransfer proteins act as phosphatases and reduce sporulation. Clostridial Spo0A proteins share **57–76% amino-acid identity**, yet the upstream phosphotransfer proteins show little structural or sequence similarity. Therefore, “OHK phosphorylates Spo0A” requires a species/protein qualifier. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 5-6)

### Rho has stage- and compartment-dependent functions

The 2024 JBC study found that reducing Rho at entry into stationary phase supports sporulation, but Rho is subsequently replenished in both compartments. At least **half** of sporulation-associated rho expression derives from SigH-dependent upstream read-through, while a SigF-dependent promoter drives forespore expression. Perturbing compartment-specific Rho expression changes mature-spore morphology and revival/outgrowth. The correct graph representation is thus a temporally qualified regulatory branch rather than a monotonic activation edge. (bidnenko2024complexsporulationspecificexpression pages 6-7, bidnenko2024complexsporulationspecificexpression pages 3-4)

### Glycogen changes spore quality, not sporulation rate

In 2024, a *C. difficile glgC* mutant showed no significant sporulation-rate defect but produced spores with greater physical/chemical sensitivity, shorter storage life, and an approximately **1.2-fold smaller core/cortex ratio**. In a relapse model, disease occurred in **7/10** hamsters challenged with wild type versus **1/10** with the glycogen-deficient mutant. The mutant also produced **1.5-fold more toxin**, illustrating pleiotropy. These findings support glycogen → spore resilience/relapse, but not glycogen → sporulation. (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3)

### Other recent statistics

A 2023 *B. thuringiensis* review reports spores with **10–50-fold higher mRNA levels** than spores of other examined *Bacillus* and *Clostridium* species and states that **94%** of spore mRNA contributes to proteins affecting germination. These are species-specific observations and should not become causal sporulation edges. (m.2023sporulationstructureassembly pages 4-6)

## 6. Applications and real-world relevance

- **Clinical transmission and recurrence:** Endospores permit persistence and transmission of *C. difficile*, *C. botulinum*, *C. tetani*, and *C. perfringens*. The 2024 review cites nearly **500,000 US *C. difficile* infections and approximately 15,000 deaths annually**, and nearly **one million US *C. perfringens* food-poisoning cases annually**. These burden estimates explain why sporulation-specific PG synthesis, spore maturation, and germination are antimicrobial targets. (gohari2024theimpactof pages 1-2)
- **Food safety and sterilization:** Clostridial spores resist heat, cold, radiation, disinfectants, and preservatives. Variation among isolates means “sporulation-positive” does not imply a fixed resistance level. (gohari2024theimpactof pages 1-2)
- **Agricultural biotechnology:** *B. thuringiensis* forms resistant spores while producing insecticidal crystalline proteins; coordinated sporulation and crystal assembly underlie environmental persistence and commercial bioinsecticide performance. (m.2023sporulationstructureassembly pages 4-6)
- **Industrial fermentation:** Spo0A phosphorylation links sporulation to acetone–butanol–ethanol solvent production in solventogenic Clostridia. This connection is industrially useful but lineage-specific. (gohari2024theimpactof pages 1-2)
- **Biocontrol and probiotics:** Stable spore preparations exploit dormancy and resistance, but production yield, resistance, and germination performance are separate measurable traits and should not be collapsed into one ontology class.

## 7. Recommended first-pass YAML content

Prioritize the following high-confidence backbone:

1. nutrient limitation → increases Spo0A phosphorylation;
2. KinA/KinB → Spo0F~P → Spo0B~P → Spo0A~P (**Bacilli scope**);
3. Spo0A~P → sporulation-gene program;
4. sporulation initiation → asymmetric septation;
5. SpoIIE → SpoIIAA dephosphorylation → σF activation;
6. σF → SpoIIR;
7. SpoIIR/SpoIIGA → pro-σE processing → σE;
8. σF/σE programs → SpoIID/SpoIIM/SpoIIP-dependent engulfment;
9. SpoIIIA–SpoIIQ → forespore transcriptional potential/σG activation;
10. σG and σK → late forespore and mother-cell programs;
11. SpoVE/SpoVD and related PG machinery → cortex/septal PG synthesis;
12. SpoVA → Ca-DPA uptake into the developing core;
13. cortex/coat/core maturation → mature endospore;
14. mother-cell hydrolase/lysis → spore release;
15. mature endospore formation → `METPO:1000870`.

Add ShfA/ShfP–glycerol, Rho, *C. difficile* dcw synthases, and glycogen as separately scoped extension modules.

## 8. Warnings: claims not ready for unqualified TraitMech curation

1. **Do not universalize the Bacillus phosphorelay.** Clostridial Spo0A activation is highly diverse; some OHK-like proteins are phosphatases rather than kinases. (gohari2024theimpactof pages 1-2, gohari2024theimpactof pages 5-6)
2. **Do not equate sporulation with germination, resistance, or dormancy.** Glycogen is a clear example: it changes spore resilience and relapse but not sporulation rate. (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3)
3. **Do not curate glycerol as a universal sporulation inhibitor.** The evidence concerns population-level timing in *B. subtilis* and depends on ShfA/ShfP-mediated communication. (updegrove2024altruisticfeedingand pages 1-2)
4. **Do not encode a simple Rho → sporulation edge.** Rho regulation is biphasic, compartmentalized, and stage dependent. (bidnenko2024complexsporulationspecificexpression pages 6-7, bidnenko2024complexsporulationspecificexpression pages 3-4)
5. **Do not transfer *C. difficile* PG machinery directly to Bacilli.** The 2023 study specifically demonstrates evolutionary specialization and a noncanonical vegetative divisome. (shrestha2023diversificationofdivision pages 1-2)
6. **Treat CwlC and individual coat proteins as taxon-specific.** Their presence or role is not necessarily conserved in all endospore formers. (m.2023sporulationstructureassembly pages 20-21, m.2023sporulationstructureassembly pages 4-6)
7. **Keep SpoIVB/BofA/SpoIVFA/SpoIVFB, SpoIVA/SpoVM, SASPs, core dehydration, and exact Ca-DPA-resistance edges provisional** until direct primary-source snippets are attached.
8. **Do not curate numerical transcript abundance as causal.** The 10–50-fold mRNA and 94% germination-related figures are descriptive *B. thuringiensis* observations. (m.2023sporulationstructureassembly pages 4-6)

## 9. DOI-first bibliography

1. Updegrove TB et al. “Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity.” *Science Advances* 10, 2024. Published **18 October 2024**. DOI: [10.1126/sciadv.adq0791](https://doi.org/10.1126/sciadv.adq0791). (updegrove2024altruisticfeedingand pages 1-2)
2. Bidnenko V et al. “Complex sporulation-specific expression of transcription termination factor Rho highlights its involvement in *Bacillus subtilis* cell differentiation.” *Journal of Biological Chemistry* 300:107905, **December 2024**. DOI: [10.1016/j.jbc.2024.107905](https://doi.org/10.1016/j.jbc.2024.107905). (bidnenko2024complexsporulationspecificexpression pages 6-7, bidnenko2024complexsporulationspecificexpression pages 3-4)
3. Hasan MK et al. “Role of glycogen metabolism in *Clostridioides difficile* virulence.” *mSphere* 9, **September 2024**. DOI: [10.1128/msphere.00310-24](https://doi.org/10.1128/msphere.00310-24). (hasan2024roleofglycogen pages 10-13, hasan2024roleofglycogen pages 1-3)
4. Gohari IM et al. “The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation.” *mBio* 15, published **13 March 2024**; April issue. DOI: [10.1128/mbio.02248-23](https://doi.org/10.1128/mbio.02248-23). (gohari2024theimpactof pages 1-2)
5. Shrestha S et al. “Diversification of division mechanisms in endospore-forming bacteria revealed by analyses of peptidoglycan synthesis in *Clostridioides difficile*.” *Nature Communications* 14:7975, **2023**; accepted 14 November 2023. DOI: [10.1038/s41467-023-43595-3](https://doi.org/10.1038/s41467-023-43595-3). (shrestha2023diversificationofdivision pages 1-2)
6. Guerrero MGG. “Sporulation, Structure Assembly, and Germination in the Soil Bacterium *Bacillus thuringiensis*.” *Microbiology Research* 14:466–491, **April 2023**. DOI: [10.3390/microbiolres14020035](https://doi.org/10.3390/microbiolres14020035). (m.2023sporulationstructureassembly pages 4-6)
7. Jun J-S et al. “Time-Course Transcriptome Analysis of *Bacillus subtilis* DB104 during Growth.” *Microorganisms* 11:1928, **July 2023**. DOI: [10.3390/microorganisms11081928](https://doi.org/10.3390/microorganisms11081928). (jun2023timecoursetranscriptomeanalysis pages 17-18)
8. Beskrovnaya P et al. “Structural, Metabolic and Evolutionary Comparison of Bacterial Endospore and Exospore Formation.” *Frontiers in Microbiology* 12, **March 2021**. DOI: [10.3389/fmicb.2021.630573](https://doi.org/10.3389/fmicb.2021.630573). (beskrovnaya2021structuralmetabolicand pages 2-3)
9. Meeske AJ et al. “High-throughput genetic screens identify a large and diverse collection of new sporulation genes in *Bacillus subtilis*.” *PLOS Biology* 14:e1002341, **January 2016**. DOI: [10.1371/journal.pbio.1002341](https://doi.org/10.1371/journal.pbio.1002341). (meeske2016highthroughputgeneticscreens pages 16-18, meeske2016highthroughputgeneticscreens pages 18-20)
10. Existing supplied evidence: “conversion of a growing cell into a two-cell-chamber sporangium.” *Annual Review of Genetics* 30, **1996**. DOI: [10.1146/annurev.genet.30.1.297](https://doi.org/10.1146/annurev.genet.30.1.297). This remains suitable foundational support for sporulation as developmental morphogenesis.

References

1. (m.2023sporulationstructureassembly pages 4-6): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 24 citations.

2. (updegrove2024altruisticfeedingand pages 1-2): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

3. (beskrovnaya2021structuralmetabolicand pages 2-3): Polina Beskrovnaya, Danielle L. Sexton, Mona Golmohammadzadeh, Ameena Hashimi, and Elitza I. Tocheva. Structural, metabolic and evolutionary comparison of bacterial endospore and exospore formation. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.630573, doi:10.3389/fmicb.2021.630573. This article has 94 citations and is from a peer-reviewed journal.

4. (gohari2024theimpactof pages 1-2): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. mBio, Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (jun2023timecoursetranscriptomeanalysis pages 17-18): Ji-Su Jun, Hyang-Eun Jeong, Su-Yeong Moon, Se-Hee Shin, and Kwang-Won Hong. Time-course transcriptome analysis of bacillus subtilis db104 during growth. Microorganisms, 11:1928, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081928, doi:10.3390/microorganisms11081928. This article has 12 citations.

6. (m.2023sporulationstructureassembly pages 20-21): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 24 citations.

7. (meeske2016highthroughputgeneticscreens pages 18-20): Alexander J. Meeske, Christopher D. A. Rodrigues, Jacqueline Brady, Hoong Chuin Lim, Thomas G. Bernhardt, and David Z. Rudner. High-throughput genetic screens identify a large and diverse collection of new sporulation genes in bacillus subtilis. PLOS Biology, 14:e1002341, Jan 2016. URL: https://doi.org/10.1371/journal.pbio.1002341, doi:10.1371/journal.pbio.1002341. This article has 91 citations and is from a highest quality peer-reviewed journal.

8. (meeske2016highthroughputgeneticscreens pages 16-18): Alexander J. Meeske, Christopher D. A. Rodrigues, Jacqueline Brady, Hoong Chuin Lim, Thomas G. Bernhardt, and David Z. Rudner. High-throughput genetic screens identify a large and diverse collection of new sporulation genes in bacillus subtilis. PLOS Biology, 14:e1002341, Jan 2016. URL: https://doi.org/10.1371/journal.pbio.1002341, doi:10.1371/journal.pbio.1002341. This article has 91 citations and is from a highest quality peer-reviewed journal.

9. (updegrove2024altruisticfeedingand pages 3-4): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (shrestha2023diversificationofdivision pages 1-2): Shailab Shrestha, Najwa Taib, Simonetta Gribaldo, and Aimee Shen. Diversification of division mechanisms in endospore-forming bacteria revealed by analyses of peptidoglycan synthesis in clostridioides difficile. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43595-3, doi:10.1038/s41467-023-43595-3. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (gohari2024theimpactof pages 5-6): Iman Mehdizadeh Gohari, Adrianne N. Edwards, Shonna M. McBride, and Bruce A. McClane. The impact of orphan histidine kinases and phosphotransfer proteins on the regulation of clostridial sporulation initiation. mBio, Apr 2024. URL: https://doi.org/10.1128/mbio.02248-23, doi:10.1128/mbio.02248-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (bidnenko2024complexsporulationspecificexpression pages 6-7): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (bidnenko2024complexsporulationspecificexpression pages 3-4): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (hasan2024roleofglycogen pages 10-13): Md Kamrul Hasan, Marjorie Pizzarro-Guajardo, Javier Sanchez, and Revathi Govind. Role of glycogen metabolism in <i>clostridioides difficile</i> virulence. Sep 2024. URL: https://doi.org/10.1128/msphere.00310-24, doi:10.1128/msphere.00310-24. This article has 4 citations and is from a peer-reviewed journal.

15. (hasan2024roleofglycogen pages 1-3): Md Kamrul Hasan, Marjorie Pizzarro-Guajardo, Javier Sanchez, and Revathi Govind. Role of glycogen metabolism in <i>clostridioides difficile</i> virulence. Sep 2024. URL: https://doi.org/10.1128/msphere.00310-24, doi:10.1128/msphere.00310-24. This article has 4 citations and is from a peer-reviewed journal.

16. (hasan2024roleofglycogen pages 5-7): Md Kamrul Hasan, Marjorie Pizzarro-Guajardo, Javier Sanchez, and Revathi Govind. Role of glycogen metabolism in <i>clostridioides difficile</i> virulence. Sep 2024. URL: https://doi.org/10.1128/msphere.00310-24, doi:10.1128/msphere.00310-24. This article has 4 citations and is from a peer-reviewed journal.