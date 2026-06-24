---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:04:42.548128'
end_time: '2026-06-18T06:20:55.611902'
duration_seconds: 973.06
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: 3-hydroxypropionate/4-hydroxybutyrate cycle
  trait_identifier: traitmech:000024
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: three_hydroxypropionate_four_hydroxybutyrate_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate
    per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates
    in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
  parent_traits: traitmech:000019
  synonyms: 3HP/4HB cycle
  evidence_summary: 'DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate
    autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg
    review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation
    pathways.)'
  causal_graph_summary: 'three_hp_four_hb_sulfolobales: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **METPO identifier:** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **METPO identifier:** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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


## Curation-focused research report: 3-hydroxypropionate/4-hydroxybutyrate cycle (3HP/4HB cycle)

**Target trait:** 3-hydroxypropionate/4-hydroxybutyrate cycle (3HP/4HB cycle)  
**METPO:** traitmech:000024  
**Category:** METABOLISM  

### 1) Scope summary (what the trait represents)

The **3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) cycle** is an **autotrophic inorganic-carbon (bicarbonate/CO2) fixation pathway** that assimilates inorganic carbon into central metabolism by converting **acetyl-CoA + 2 HCO3− → succinyl-CoA → 4-hydroxybutyrate intermediates** and regenerating acetyl-CoA, thereby yielding net fixed carbon for biosynthesis (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof pages 1-2). A canonical accounting from a 2023 review states that a complete turn **fixes two bicarbonate (HCO3−) to produce one acetyl-CoA** while consuming **~6 ATP and ~4 NADPH equivalents** (bahrle2023currentstatusof pages 2-4). A recent 2024 primary study frames the thaumarchaeal 3HP/4HB cycle as **“the most energy-efficient aerobic carbon fixation pathway”** and depicts the pathway as a compact module with ATP-dependent CoA ligations and carboxylations (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof media 87343693).

**Phenotype/physiological capacity represented by the trait:** the genetically encoded capacity for **aerobic or microaerophilic chemoautotrophic carbon fixation** via the 3HP/4HB route, typically coupled to energy generation from oxidation of reduced compounds (e.g., sulfur species) or nitrification in archaea (johnson2024crystalstructureof pages 1-2, ulas2012genomescalereconstructionand pages 6-9).

**Environmental preference/assay-observed property:** presence/expression of 3HP/4HB marker genes (e.g., **accA**, **4-hydroxybutyryl-CoA dehydratase**) in genomic/metagenomic data or activity inferred from carbon fixation under oxic/microoxic conditions; in applied settings, inferred operation can be linked to CO2 consumption in bioreactors (alvarez‐guzman2023effectofelectron pages 1-2).

#### Boundary cases and distinctions from nearby traits

* **vs. 3-hydroxypropionate bicycle (3HP bicycle):** the 3HP bicycle is classically associated with phototrophic bacteria (e.g., Chloroflexus) and is more energy demanding; a 2023 review summarizes it as fixing **3 CO2 to pyruvate** with costs of **~7 ATP and ~5 reducing equivalents**, whereas 3HP/4HB fixes **2 HCO3− to acetyl-CoA** (bahrle2023currentstatusof pages 2-4). Thus, the boundary is both **taxonomic (archaea vs bacteria)** and **stoichiometric/energetic** (bahrle2023currentstatusof pages 2-4, kang2023insightsintoenzyme pages 2-4).
* **vs. dicarboxylate/4-hydroxybutyrate cycle (DC/4HB):** DC/4HB is described as **strictly anaerobic** and reliant on **O2-sensitive enzymes/ferredoxin-dependent steps** (e.g., pyruvate synthase), whereas 3HP/4HB is categorized among **aerobic pathways** (bahrle2023currentstatusof pages 2-4, kang2023insightsintoenzyme pages 2-4). This is a key curation boundary: do not conflate DC/4HB gene sets with 3HP/4HB when oxygen sensitivity or ferredoxin-dependent modules dominate.

### 2) Candidate causal-graph nodes (grouped by type)

#### A. Pathways / modules
* **3HP/4HB cycle** (METPO:traitmech:000024) (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof media 87343693)
* **Wood–Ljungdahl pathway (WLP)** (often co-inferred in engineered/complex communities) (alvarez‐guzman2023effectofelectron pages 1-2)
* Comparator pathways for boundaries: **3HP bicycle**, **DC/4HB cycle**, **rTCA cycle** (bahrle2023currentstatusof pages 2-4, kang2023insightsintoenzyme pages 2-4)

#### B. Organisms / taxa (examples / contexts)
* **Ammonia-oxidizing Thaumarchaeota / Nitrososphaeria** (AOA; e.g., *Nitrosopumilus maritimus*) (johnson2024crystalstructureof pages 1-2)
* **Sulfolobales/Crenarchaeota** (historic discovery context; aerobic thermoacidophiles) (kang2023insightsintoenzyme pages 2-4, ulas2012genomescalereconstructionand pages 6-9)

#### C. Enzymes / genes / protein complexes (candidate nodes)
* **Acetyl-CoA/propionyl-CoA carboxylase** (primary carboxylase module) (johnson2024crystalstructureof pages 1-2, wang2023microbialconversionand pages 3-5)
  * Candidate marker gene: **accA** (curation warning: non-exclusive marker; see below) (wang2023microbialconversionand pages 3-5)
* **ADP-forming 3-hydroxypropionyl-CoA synthetase (Nmar_1309)** (Thaumarchaeota) (johnson2024crystalstructureof pages 1-2)
* **ADP-forming 4-hydroxybutyryl-CoA synthetase (Nmar_0206)** (Thaumarchaeota) (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof media 7983076e)
* **4-hydroxybutyryl-CoA dehydratase** (includes oxygen-tolerant forms in AOA) (johnson2024crystalstructureof pages 1-2)
* **Bifunctional crotonyl-CoA hydratase/3-hydroxypropionyl-CoA dehydratase** (johnson2024crystalstructureof pages 1-2)
* **Carbonic anhydrase (EC:4.2.1.1)** (supports HCO3− supply; cytosolic copy predicted in AOA genomes) (cornell2024genomeencodedmetabolicpotential pages 60-61)
* **Fusion/fission enzyme families including Hps/Hbl homologs** (3-hydroxypropionyl-CoA synthetase/4-hydroxybutyrate-CoA ligase; archaeal genome evolution context) (padalko2024fusionfissionproteinfamily pages 10-12)

#### D. Metabolites / chemicals
* **Bicarbonate (HCO3−)** (CHEBI:17544) (bahrle2023currentstatusof pages 2-4, cornell2024genomeencodedmetabolicpotential pages 60-61)
* **Acetyl-CoA** (CHEBI:15351) (bahrle2023currentstatusof pages 2-4)
* **Succinyl-CoA** (CHEBI:15435) (bahrle2023currentstatusof pages 2-4)
* **4-hydroxybutyrate (4HB)** (CHEBI:50211) and **4-hydroxybutyryl-CoA** (label-only) (johnson2024crystalstructureof pages 1-2)
* **Crotonyl-CoA** (CHEBI:37698) (bahrle2023currentstatusof pages 2-4)
* Cofactors: **ATP**, **NADPH**, **CoA** (bahrle2023currentstatusof pages 2-4, cornell2024genomeencodedmetabolicpotential pages 59-60)

#### E. Environmental / experimental factors
* **Oxygen regime:** aerobic vs microaerophilic (3HP/4HB) versus anaerobic (DC/4HB) (bahrle2023currentstatusof pages 2-4)
* **Electron donors / energy sources:** e.g., **hydrogen sulfide (H2S)/sulfide** supporting autotrophic modeling in *Sulfolobus*; sulfide also drives CO2 uptake in reactors (ulas2012genomescalereconstructionand pages 6-9, alvarez‐guzman2023effectofelectron pages 11-12)
* **Low nutrient / oligotrophy (selection pressure):** linked to energy-efficient thaumarchaeal enzyme variants (johnson2024crystalstructureof pages 1-2)

### 3) Candidate causal edges (evidence-backed triples)

The table below is designed to be directly translatable into a TraitMech YAML edge list, with curator notes.

| Edge (subject–predicate–object) | Node types (S/O) | Suggested ontology grounding (CURIEs where possible) | Evidence (citation id) | Source (DOI, year, URL) | Supporting snippet (short quote or close paraphrase) | Notes/strength |
|---|---|---|---|---|---|---|
| 3-hydroxypropionate/4-hydroxybutyrate cycle — fixes — 2 bicarbonate into 1 acetyl-CoA | pathway/chemical | METPO:traitmech:000024; CHEBI:17544 bicarbonate; CHEBI:15351 acetyl-CoA | (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof media 87343693) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | “A complete 3HP/4HB cycle fixes two HCO3− to produce one acetyl-CoA” and Figure 1 shows the full pathway schematic. | Strong pathway-defining edge; directly supports trait scope. |
| acetyl-CoA/propionyl-CoA carboxylase — mediates carboxylation in — 3HP/4HB cycle | enzyme/pathway | EC candidate: acetyl-CoA carboxylase / propionyl-CoA carboxylase; KEGG/MetaCyc label-only if exact subunits unresolved | (johnson2024crystalstructureof pages 1-2, wang2023microbialconversionand pages 3-5, kang2023insightsintoenzyme pages 2-4) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | “The cycle fixes CO2 onto acetyl-CoA (via an acetyl-CoA/propionyl-CoA carboxylase)” and this carboxylase is described as the “primary carboxylase.” | Strong for enzyme–pathway relation; exact subunit grounding may need curation. |
| bicarbonate — is substrate for — acetyl-CoA/propionyl-CoA carboxylase reactions | chemical/enzyme | CHEBI:17544 bicarbonate; enzyme CURIE unresolved | (kang2023insightsintoenzyme pages 2-4, cornell2024genomeencodedmetabolicpotential pages 60-61) | 10.4014/jmb.2306.06005 (2023) https://doi.org/10.4014/jmb.2306.06005 | 3HP/4HB is described as a “bicarbonate-fixing carbon assimilation pathway”; carbonic anhydrase matters because “HCO3- is the inorganic carbon substrate for the 3HP/4HB pathway.” | Strong biochemical context; direct for pathway substrate, indirect for specific individual carboxylase step. |
| 3HP/4HB cycle — forms intermediate — succinyl-CoA | pathway/chemical | METPO:traitmech:000024; CHEBI:15435 succinyl-CoA | (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof pages 1-2, ulas2012genomescalereconstructionand pages 6-9) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | The pathway “carboxylates acetyl-CoA/propionyl-CoA to form succinyl-CoA from two HCO3−.” | Strong; central intermediate in all descriptions. |
| succinyl-CoA — is reduced to — 4-hydroxybutyrate | chemical/chemical | CHEBI:15435 succinyl-CoA; CHEBI:50211 4-hydroxybutyrate | (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof pages 1-2, wang2023microbialconversionand pages 3-5) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | “Succinyl-CoA is reduced to 4-hydroxybutyrate” / “reduced to 4-hydroxybutyric acid.” | Strong pathway chemistry edge. |
| Nmar_0206 4-hydroxybutyryl-CoA synthetase — activates — 4-hydroxybutyrate to 4-hydroxybutyryl-CoA | protein/chemical | UniProt/GenBank locus label-only: Nmar_0206; CHEBI:50211 4-hydroxybutyrate; CHEBI label-only 4-hydroxybutyryl-CoA | (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof media 7983076e) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | “Nmar_0206… catalyzes 4HB + CoA → 4HB-CoA” and Figures 2/9 depict the reaction/mechanism. | Strong, thaumarchaeal and protein-specific. |
| 4-hydroxybutyryl-CoA dehydratase — dehydrates — 4-hydroxybutyryl-CoA to crotonyl-CoA | enzyme/chemical | EC label-only; CHEBI label-only 4-hydroxybutyryl-CoA; CHEBI:37698 crotonyl-CoA | (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof media 87343693) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | The cycle “dehydrates to crotonyl-CoA,” and the pathway diagram in Figure 1 shows the step. | Strong for step presence; exact reaction participants from figure/text synthesis. |
| crotonyl-CoA cleavage/processing — regenerates — acetyl-CoA | process/chemical | CHEBI:37698 crotonyl-CoA; CHEBI:15351 acetyl-CoA | (bahrle2023currentstatusof pages 2-4, ulas2012genomescalereconstructionand pages 6-9, johnson2024crystalstructureof media 87343693) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | The pathway “finally cleaves to yield acetyl-CoA”; modeling notes conversion “to acetyl-CoA for further turns.” | Moderate-to-strong; exact intervening steps compressed. |
| 3HP/4HB cycle — occurs in — aerobic archaea | pathway/environmental context | METPO:traitmech:000024; ENVO label-only aerobic environment; NCBITaxon:2157 Archaea | (bahrle2023currentstatusof pages 2-4, johnson2024crystalstructureof pages 1-2) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | The pathway is “classified among aerobic pathways” and in 2024 is called “the most energy-efficient aerobic carbon fixation pathway.” | Strong broad ecological context. |
| 3HP/4HB cycle — associated with — ammonia-oxidizing Thaumarchaeota | pathway/taxon | METPO:traitmech:000024; NCBITaxon label-only Thaumarchaeota/Nitrososphaeria | (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | “The 3HP/4HB cycle from ammonia-oxidizing Thaumarchaeota…” | Strong but clade-specific; important boundary case versus Sulfolobales version. |
| 3HP/4HB cycle — is encoded in — deep-sea seep Thaumarchaeota/AOA genomes | pathway/taxon | METPO:traitmech:000024; NCBITaxon label-only AOA | (johnson2024crystalstructureof pages 1-2) | 10.1186/s40168-024-01912-y (2024) https://doi.org/10.1186/s40168-024-01912-y | “With regard to carbon metabolism, the 3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) cycle… [is] widely encoded…” | Moderate; genomic encoding evidence, not direct flux assay. |
| carbonic anhydrase — supplies substrate for — 3HP/4HB cycle via HCO3− production | enzyme/pathway | EC:4.2.1.1; CHEBI:17544 bicarbonate; METPO:traitmech:000024 | (cornell2024genomeencodedmetabolicpotential pages 60-61) | Cornell 2024 thesis/article excerpt (2024) URL unavailable in metadata | Carbonic anhydrase “catalyzes reversible hydration of CO2 to HCO3-” and “HCO3- is the inorganic carbon substrate for the 3HP/4HB pathway.” | Moderate; supportive context, not always pathway-specific marker. |
| NADPH — is required by — 3HP/4HB cycle reactions | chemical/pathway | CHEBI:16474 NADPH; METPO:traitmech:000024 | (cornell2024genomeencodedmetabolicpotential pages 59-60, bahrle2023currentstatusof pages 2-4) | 10.1186/s40643-023-00705-9 (2023) https://doi.org/10.1186/s40643-023-00705-9 | “five reactions in the cycle require the oxidation of NADPH”; full cycle consumes “four NADPH.” | Strong for cofactor requirement; exact step mapping still needed. |
| ADP-forming 4-hydroxybutyryl-CoA synthetase (Nmar_0206) — reduces energetic burden of — thaumarchaeal 3HP/4HB cycle | protein/pathway-property | Nmar_0206 label-only; METPO:traitmech:000024 | (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | ADP-forming ligases “conserve phosphate… reducing cellular energetic burden” and this “reflect[s] thaumarchaeal success in adapting to low-nutrient environments.” | Strong but thaumarchaeal-specific mechanistic refinement. |
| ADP-forming 3-hydroxypropionyl-CoA synthetase (Nmar_1309) — reduces energetic burden of — thaumarchaeal 3HP/4HB cycle | protein/pathway-property | Nmar_1309 label-only; METPO:traitmech:000024 | (johnson2024crystalstructureof pages 1-2) | 10.1038/s42003-024-06432-x (2024) https://doi.org/10.1038/s42003-024-06432-x | The paper names “Nmar_1309 as an ADP-forming 3-hydroxypropionyl-CoA synthetase” and links ADP-forming ligases to phosphate conservation. | Strong but taxon-specific to modified thaumarchaeal cycle. |
| hydrogen sulfide — supports autotrophic growth using — 3HP/4HB cycle in Sulfolobus model | chemical/pathway | CHEBI:16136 hydrogen sulfide; METPO:traitmech:000024; NCBITaxon:2287 Sulfolobus (candidate genus-level) | (ulas2012genomescalereconstructionand pages 6-9) | 10.1371/journal.pone.0043401 (2012) https://doi.org/10.1371/journal.pone.0043401 | “Growth under this autotrophic mode required import/oxidation of hydrogen sulfide as a reducing agent/electron donor”; limiting H2S halved biomass yield. | Moderate; model-based and Sulfolobus-specific, but mechanistically useful. |
| accA — is marker gene for — 3HP/4HB cycle occurrence in environmental samples | gene/pathway | KEGG/UniProt label-only accA; METPO:traitmech:000024 | (wang2023microbialconversionand pages 3-5) | 10.29328/journal.acee.1001055 (2023) https://doi.org/10.29328/journal.acee.1001055 | Deep-sea sediment work notes “accA (from the 3HP/4HB pathway) were most abundant,” and earlier environmental assays targeted “key C fixation genes (accA, 4-bdh…).” | Moderate; marker use is strong in omics surveys, but accA can occur in other pathways—curate as non-exclusive marker. |
| 4-bud / 4-hydroxybutyryl-CoA dehydratase gene — is marker gene for — 3HP/4HB cycle occurrence | gene/pathway | gene label-only 4-bud / 4-hydroxybutyryl-CoA dehydratase; METPO:traitmech:000024 | (wang2023microbialconversionand pages 3-5, johnson2024crystalstructureof pages 1-2) | 10.1038/ismej.2010.197 (2011) https://doi.org/10.1038/ismej.2010.197 | Environmental gene surveys measured “key C fixation genes (accA, 4-bdh…) of 3-hydroxypropionate/4-hydroxybutyrate…” | Moderate; useful marker, but gene naming varies (4-bdh/4-bud) and should be standardized before curation. |


*Table: This table compiles candidate subject–predicate–object edges for curating a TraitMech graph of the 3-hydroxypropionate/4-hydroxybutyrate cycle. It emphasizes pathway-defining reactions, key enzymes and marker genes, energetic features, and ecological context, with citation-linked evidence and curation notes.*

### 4) Recent developments & latest research (prioritizing 2023–2024)

#### 4.1 Structural & mechanistic refinement of thaumarchaeal 3HP/4HB enzymes (2024)
A key 2024 advance is the crystal structure and mechanistic analysis of **Nmar_0206 (ADP-forming 4-hydroxybutyryl-CoA synthetase)** from *Nitrosopumilus maritimus* (Communications Biology, published Oct 2024). The study connects a specific enzyme architecture (including a conserved linker loop) to **improved energy efficiency** and emphasizes that the AOA 3HP/4HB cycle is considered **highly energy-efficient in aerobic settings** (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 6-8). The paper also provides a pathway schematic (Figure 1) and reaction/mechanism depictions for Nmar_0206 (Figures 2 and 9), which are useful as curation references for step directionality and metabolite naming (johnson2024crystalstructureof media 87343693, johnson2024crystalstructureof media 7983076e, johnson2024crystalstructureof media f7310cec).

A mechanistic concept highlighted is **“phosphate conservation”**: ADP-forming synthetases (e.g., Nmar_0206 and Nmar_1309) conserve an intact ADP rather than producing AMP, thereby **reducing energetic burden** in low-nutrient environments (johnson2024crystalstructureof pages 1-2).

#### 4.2 Updated energetic comparisons and thermodynamic context (2023)
A 2023 review discussing autotrophic CO2 fixation pathways provides a compact quantitative summary for 3HP/4HB: **2 HCO3− → acetyl-CoA** at a cost of **6 ATP and 4 NADPH**, and lists example reaction free energies for key steps (e.g., acetyl-CoA/propionyl-CoA carboxylase ΔrGm′ ≈ −61.9 kJ/mol) (bahrle2023currentstatusof pages 2-4). This review also contrasts energetic demands of the **3HP bicycle**, **rTCA**, and **Wood–Ljungdahl** pathways, which is helpful for boundary curation (bahrle2023currentstatusof pages 2-4).

#### 4.3 Reactor-scale CO2 capture by non-photosynthetic communities (2023)
A 2023 applied study (Microbial Biotechnology, Oct 2023) tested capture of CO2 from a **model cement flue gas (CO2/O2/N2 = 4.2:13.5:82.3% v/v)** using non-photosynthetic microbial communities, and inferred that the operative carbon fixation pathways included the **3HP/4HB cycle** and **Wood–Ljungdahl pathway** (alvarez‐guzman2023effectofelectron pages 1-2). Reported performance statistics include:
* After acclimation, **100% CO2 removal after 45 days** (batch) (alvarez‐guzman2023effectofelectron pages 1-2).
* Electron donor dependence: **Na2S achieved 100% CO2 consumption** while **FeCl2 achieved 28%** in batch tests (alvarez‐guzman2023effectofelectron pages 1-2).
* In a continuous **biotrickling filter**, CO2 consumption reached **up to 77%** with Na2S dosing (alvarez‐guzman2023effectofelectron pages 1-2, alvarez‐guzman2023effectofelectron pages 11-12).
* Major endpoint metabolites were **acetate and propionate** (alvarez‐guzman2023effectofelectron pages 1-2).

Curation warning: this study infers pathway usage (3HP/4HB + WLP) from community/metabolic analysis rather than direct isotopic flux partitioning; edges linking “3HP/4HB causes CO2 consumption in this reactor” should therefore be marked **uncertain / community-inferred**.

### 5) Current applications / real-world implementations

* **Industrial point-source CO2 capture (biotrickling filter / flue gas):** non-photosynthetic microbial communities consuming CO2 from a cement-like flue gas mixture, with performance modulated by electron donors (Na2S best) and achieving up to 77% consumption in continuous mode (alvarez‐guzman2023effectofelectron pages 11-12). This provides a concrete operational context for trait relevance in engineered ecosystems.
* **Enzyme engineering / synthetic biology targets:** the 2024 structural work emphasizes that AMP-forming acyl-CoA synthetase binding pockets can be “amenable to mutation,” implying design routes for modified carbon fixation modules; moreover, the ADP-forming ligase mechanism is positioned as a core efficiency feature to preserve in engineering efforts (johnson2024crystalstructureof pages 6-8, johnson2024crystalstructureof pages 1-2).

### 6) Expert opinions and analysis (authoritative sources)

* The 2024 Communications Biology paper explicitly frames the thaumarchaeal 3HP/4HB cycle as **“the most energy-efficient aerobic carbon fixation pathway”**, and connects enzyme mechanism (ADP-forming ligases) to ecological success under oligotrophy (johnson2024crystalstructureof pages 1-2).
* A 2023 peer-reviewed review provides a comparative framing across carbon fixation pathways (3HP/4HB, 3HP bicycle, rTCA, WL), emphasizing that organismal distribution and oxygen sensitivity align with key biochemical cofactors (NADPH/ATP dependence vs ferredoxin-dependent, O2-sensitive enzymes) (bahrle2023currentstatusof pages 2-4, kang2023insightsintoenzyme pages 2-4).

### 7) Relevant statistics and data points (recent studies)

* **Energetic cost (pathway-level):** 3HP/4HB fixes **two HCO3−** per turn to yield one acetyl-CoA and consumes **~6 ATP + ~4 NADPH** (bahrle2023currentstatusof pages 2-4).
* **Global impact estimate (recent claim):** A 2024 primary paper states the pathway may account for **~1% of global carbon fixation** (johnson2024crystalstructureof pages 1-2). (This should be curated cautiously unless corroborated by additional sources.)
* **Reactor performance:** up to **77% CO2 consumption** in a continuous biotrickling filter using Na2S as electron donor; **100% CO2 removal** in batch post-acclimation; best vs worst donor in batch: **Na2S 100%**, **FeCl2 28%** (alvarez‐guzman2023effectofelectron pages 1-2, alvarez‐guzman2023effectofelectron pages 11-12).

### 8) Bibliography (DOI-first; URLs and publication dates)

1. **Johnson J, et al.** *Crystal structure of the 4-hydroxybutyryl-CoA synthetase (ADP-forming) from Nitrosopumilus maritimus.* **Communications Biology**. Published **Oct 2024**. DOI: **10.1038/s42003-024-06432-x**. URL: https://doi.org/10.1038/s42003-024-06432-x (johnson2024crystalstructureof pages 1-2, johnson2024crystalstructureof pages 6-8, johnson2024crystalstructureof media 87343693, johnson2024crystalstructureof media 7983076e, johnson2024crystalstructureof media f7310cec)
2. **Padalko A, Nair G, Sousa FL.** *Fusion/fission protein family identification in Archaea.* **mSystems**. Published **Jun 2024**. DOI: **10.1128/msystems.00948-23**. URL: https://doi.org/10.1128/msystems.00948-23 (padalko2024fusionfissionproteinfamily pages 10-12)
3. **Alvarez-Guzmán CL, Muñoz-Páez KM, Valdez-Vazquez I.** *Effect of electron donors on CO2 fixation from a model cement industry flue gas by non-photosynthetic microbial communities in batch and continuous reactors.* **Microbial Biotechnology**. Published **Oct 2023**. DOI: **10.1111/1751-7915.14353**. URL: https://doi.org/10.1111/1751-7915.14353 (alvarez‐guzman2023effectofelectron pages 1-2, alvarez‐guzman2023effectofelectron pages 11-12, alvarez‐guzman2023effectofelectron pages 2-4)
4. **Bährle R, et al.** *Current status of carbon monoxide dehydrogenases (CODH) and their potential for electrochemical applications.* **Bioresources and Bioprocessing**. Published **Nov 2023**. DOI: **10.1186/s40643-023-00705-9**. URL: https://doi.org/10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 2-4)
5. **Kang D-K, et al.** *Insights into Enzyme Reactions with Redox Cofactors in Biological Conversion of CO2.* **Journal of Microbiology and Biotechnology**. Published **Jun 2023**. DOI: **10.4014/jmb.2306.06005**. URL: https://doi.org/10.4014/jmb.2306.06005 (kang2023insightsintoenzyme pages 2-4)
6. **Ulas T, et al.** *Genome-Scale Reconstruction and Analysis of the Metabolic Network in the Hyperthermophilic Archaeon Sulfolobus solfataricus.* **PLoS ONE**. Published **Aug 2012**. DOI: **10.1371/journal.pone.0043401**. URL: https://doi.org/10.1371/journal.pone.0043401 (ulas2012genomescalereconstructionand pages 6-9)
7. **Wang G-G, et al.** *Microbial Conversion and Utilization of CO2.* **Annals of Civil and Environmental Engineering**. Published **Sep 2023**. DOI: **10.29328/journal.acee.1001055**. URL: https://doi.org/10.29328/journal.acee.1001055 (wang2023microbialconversionand pages 3-5)

### 9) Warnings / claims needing curator caution before inclusion

1. **Marker gene specificity:** **accA** is often treated as a marker for the 3HP/4HB pathway in environmental surveys, but acetyl-CoA carboxylase subunits can participate in other metabolic contexts. Curate accA as a **supporting but non-exclusive** indicator unless paired with other pathway-specific genes (e.g., 4-hydroxybutyryl-CoA dehydratase, ADP-forming ligases) (wang2023microbialconversionand pages 3-5, johnson2024crystalstructureof pages 1-2).
2. **Community inference vs flux proof:** Reactor studies may infer 3HP/4HB operation from gene/pathway predictions; causal edges “3HP/4HB caused CO2 removal” should be tagged **uncertain** unless isotopic or enzyme-activity partitioning is shown (alvarez‐guzman2023effectofelectron pages 1-2).
3. **Global fraction claim (~1% of global carbon fixation):** this statement is useful as context but should be curated as **tentative** without corroboration from independent global budget analyses (johnson2024crystalstructureof pages 1-2).
4. **Model-based edges (Sulfolobus + H2S):** edges involving sulfide requirements in *Sulfolobus* derive from constraint-based simulations and should be flagged **model-dependent** (ulas2012genomescalereconstructionand pages 6-9).


References

1. (bahrle2023currentstatusof pages 2-4): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 27 citations and is from a peer-reviewed journal.

2. (johnson2024crystalstructureof pages 1-2): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

3. (johnson2024crystalstructureof media 87343693): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

4. (ulas2012genomescalereconstructionand pages 6-9): Thomas Ulas, S. Alexander Riemer, Melanie Zaparty, Bettina Siebers, and Dietmar Schomburg. Genome-scale reconstruction and analysis of the metabolic network in the hyperthermophilic archaeon sulfolobus solfataricus. PLoS ONE, 7:e43401, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0043401, doi:10.1371/journal.pone.0043401. This article has 72 citations and is from a peer-reviewed journal.

5. (alvarez‐guzman2023effectofelectron pages 1-2): Cecilia Lizeth Alvarez‐Guzmán, Karla María Muñoz‐Páez, and Idania Valdez‐Vazquez. Effect of electron donors on co2 fixation from a model cement industry flue gas by non‐photosynthetic microbial communities in batch and continuous reactors. Microbial Biotechnology, 16:2387-2400, Oct 2023. URL: https://doi.org/10.1111/1751-7915.14353, doi:10.1111/1751-7915.14353. This article has 7 citations and is from a peer-reviewed journal.

6. (kang2023insightsintoenzyme pages 2-4): Du-Kyeong Kang, Seung-Hwa Kim, Jung-Hoon Sohn, and Bong Hyun Sung. Insights into enzyme reactions with redox cofactors in biological conversion of co2. Journal of Microbiology and Biotechnology, 33:1403-1411, Jun 2023. URL: https://doi.org/10.4014/jmb.2306.06005, doi:10.4014/jmb.2306.06005. This article has 10 citations and is from a peer-reviewed journal.

7. (wang2023microbialconversionand pages 3-5): Ge-Ge Wang, Zhang Yuan, Xiao-Yan Wang, and Gen-Lin Zhang. Microbial conversion and utilization of co2. Annals of Civil and Environmental Engineering, 7:045-060, Sep 2023. URL: https://doi.org/10.29328/journal.acee.1001055, doi:10.29328/journal.acee.1001055. This article has 3 citations.

8. (johnson2024crystalstructureof media 7983076e): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

9. (cornell2024genomeencodedmetabolicpotential pages 60-61): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

10. (padalko2024fusionfissionproteinfamily pages 10-12): Anastasiia Padalko, Govind Nair, and Filipa L. Sousa. Fusion/fission protein family identification in archaea. mSystems, Jun 2024. URL: https://doi.org/10.1128/msystems.00948-23, doi:10.1128/msystems.00948-23. This article has 5 citations and is from a peer-reviewed journal.

11. (cornell2024genomeencodedmetabolicpotential pages 59-60): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

12. (alvarez‐guzman2023effectofelectron pages 11-12): Cecilia Lizeth Alvarez‐Guzmán, Karla María Muñoz‐Páez, and Idania Valdez‐Vazquez. Effect of electron donors on co2 fixation from a model cement industry flue gas by non‐photosynthetic microbial communities in batch and continuous reactors. Microbial Biotechnology, 16:2387-2400, Oct 2023. URL: https://doi.org/10.1111/1751-7915.14353, doi:10.1111/1751-7915.14353. This article has 7 citations and is from a peer-reviewed journal.

13. (johnson2024crystalstructureof pages 6-8): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

14. (johnson2024crystalstructureof media f7310cec): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 7 citations and is from a peer-reviewed journal.

15. (alvarez‐guzman2023effectofelectron pages 2-4): Cecilia Lizeth Alvarez‐Guzmán, Karla María Muñoz‐Páez, and Idania Valdez‐Vazquez. Effect of electron donors on co2 fixation from a model cement industry flue gas by non‐photosynthetic microbial communities in batch and continuous reactors. Microbial Biotechnology, 16:2387-2400, Oct 2023. URL: https://doi.org/10.1111/1751-7915.14353, doi:10.1111/1751-7915.14353. This article has 7 citations and is from a peer-reviewed journal.