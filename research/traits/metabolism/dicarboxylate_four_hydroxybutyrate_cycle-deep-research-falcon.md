---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:31:17.396797'
end_time: '2026-06-18T04:40:52.914470'
duration_seconds: 575.52
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dicarboxylate/4-hydroxybutyrate cycle
  trait_identifier: traitmech:000025
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dicarboxylate_four_hydroxybutyrate_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway that fixes one molecule of CO2
    and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate
    stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus
    and Thermoproteales.
  parent_traits: traitmech:000019
  synonyms: DC/4HB cycle
  evidence_summary: 'DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate
    cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg
    et al.''s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry
    shared by this cycle in Crenarchaeota.)'
  causal_graph_summary: 'dc_four_hb_anaerobic_archaeal_co2_fixation: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dicarboxylate/4-hydroxybutyrate cycle
- **METPO identifier:** traitmech:000025
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes one molecule of CO2 and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus and Thermoproteales.
- **Parent traits:** traitmech:000019
- **Synonyms:** DC/4HB cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg et al.'s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry shared by this cycle in Crenarchaeota.)
- **Existing causal graph summary:** dc_four_hb_anaerobic_archaeal_co2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dicarboxylate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`.

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
- **Trait label:** dicarboxylate/4-hydroxybutyrate cycle
- **METPO identifier:** traitmech:000025
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes one molecule of CO2 and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus and Thermoproteales.
- **Parent traits:** traitmech:000019
- **Synonyms:** DC/4HB cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg et al.'s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry shared by this cycle in Crenarchaeota.)
- **Existing causal graph summary:** dc_four_hb_anaerobic_archaeal_co2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dicarboxylate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`.

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


# Research report: dicarboxylate/4-hydroxybutyrate cycle (DC/4HB) — TraitMech candidate (traitmech:000025)

## 0. Scope summary (TraitMech-oriented)

**Trait meaning.** The dicarboxylate/4-hydroxybutyrate (DC/4HB) cycle is an **autotrophic carbon-fixation pathway** in which (per turn) acetyl‑CoA is regenerated while **one CO2 and one bicarbonate (HCO3−)** are incorporated into intermediates through two carboxylation reactions; the pathway proceeds through a **dicarboxylate stage** (incomplete rTCA-like segment) and a **4‑hydroxybutyrate (4HB) stage** that regenerates acetyl‑CoA. Key carboxylating enzymes are **pyruvate synthase (ferredoxin-dependent) and phosphoenolpyruvate carboxylase (PEPC)**. (quaranta2010carbondioxideas pages 59-61, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)

**Ecological/physiological association.** DC/4HB has been reported mainly from **anaerobic/microaerophilic autotrophic Crenarchaeota**, especially **Thermoproteales and Desulfurococcales**, and is strongly associated with **anoxic conditions** due to oxygen sensitivity of key enzymes/electron carriers. (berg2011ecologicalaspectsof pages 8-9, ramosvera2011identificationofmissing pages 1-2)

**Boundary cases / trait neighbors.**
- **Versus 3HP/4HB:** DC/4HB shares the **4HB-to-acetyl‑CoA regeneration chemistry** (including 4‑hydroxybutyryl‑CoA dehydratase) but differs in the upstream carbon‑fixing module and oxygen tolerance; the related **3‑hydroxypropionate/4‑hydroxybutyrate (3HP/4HB)** cycle is used by (micro)aerobic Sulfolobales and is comparatively oxygen‑tolerant, while DC/4HB is constrained to anaerobes via oxygen‑sensitive pyruvate synthase/ferredoxin. (berg2011ecologicalaspectsof pages 8-9, ramosvera2011identificationofmissing pages 1-2, fuchs2011alternativepathwaysof media 0cfdc547)
- **Versus rTCA:** DC/4HB includes an “incomplete reductive citric acid cycle” segment producing succinyl‑CoA, but DC/4HB is defined by the downstream **4HB branch** that returns to **two acetyl‑CoA**. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)

## 1. Key concepts and definitions (current understanding)

### 1.1 Canonical reaction logic
A succinct description from an authoritative synthesis describes the cycle as:
- starting from **acetyl‑CoA**, “**reductively carboxylated to pyruvate**,”
- pyruvate → PEP, “**then carboxylated to oxaloacetate**,”
- oxaloacetate reduced to **succinyl‑CoA** through an incomplete rTCA-like set,
- succinyl‑CoA “**reduced to 4‑hydroxybutyrate**,”
- and the “**subsequent conversion … into two acetyl‑CoA molecules proceeds in the same way as in the 3‑hydroxypropionate/4‑hydroxybutyrate cycle**.” (quaranta2010carbondioxideas pages 59-61)

### 1.2 Active inorganic carbon species
The two carboxylation steps use different inorganic carbon species:
- “**CO2 as cosubstrate for pyruvate synthase**” and
- “**bicarbonate as cosubstrate for PEP** [carboxylation].” (quaranta2010carbondioxideas pages 59-61)

### 1.3 Hallmark enzyme
A key hallmark reaction in the 4HB branch is dehydration of 4‑hydroxybutyryl‑CoA:
- “**dehydrated by a radical 4‑hydroxybutyryl‑CoA dehydratase to crotonyl‑CoA**.” (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)

## 2. Recent developments (prioritizing 2023–2024)

### 2.1 2024: DIC (CO2/HCO3−) acquisition toolkits in DC/4HB (DCHB) genomes
A 2024 AEM minireview surveying finished genomes across autotrophic pathways reports that organisms inferred to use the DC/4HB cycle (termed **DCHB**) show **unusual scarcity of known DIC transporters**:
- “**organisms inferred to use the DCHB … cycle generally lack genes for known DIC transporters**.” (scott2024widespreaddissolvedinorganic pages 15-18)
It further notes:
- “**about half of these genomes encode cytoplasmic carbonic anhydrase (cCA), with those cCA-containing genomes belonging to the genus Pyrobaculum**.” (scott2024widespreaddissolvedinorganic pages 15-18)
The same source emphasizes uncertainty in pathway calls for some taxa:
- “**For members of genus Pyrobaculum, genome data suggest the DCHB pathway, but other evidence is less conclusive**” and some organisms “**may use rTCA instead**.” (scott2024widespreaddissolvedinorganic pages 15-18, scott2024widespreaddissolvedinorganic pages 7-10)
**Curation implication:** DIC-toolkit nodes/edges should be curated with an explicit “unknown transporter” placeholder where appropriate, and with pathway-uncertainty flags for Pyrobaculum-associated edges.

### 2.2 2022 (still recent comparative genomics underpinning 2023–2024 work): expanded phylogenetic breadth from MAGs
A large-scale MAG study analyzed **52,515 MAGs** and identified carbon fixation pathways in **1,007 MAGs**. (garritano2022carbonfixationpathways pages 1-2)
Within that, it specifically reports:
- “**two MAGs classified as Lokiarchaeia (phylum Asgardarchaeota) contain all genes for the DC/HB cycle**.” (garritano2022carbonfixationpathways pages 5-7)
It also reports first-time genomic evidence in **Sulfolobus**:
- “**genomic evidence for the DC/HB cycle in the genus Sulfolobus, supported by the presence of all required enzymes**.” (garritano2022carbonfixationpathways pages 5-7)
**Curation implication:** “presence of all genes” edges are valuable but should be marked as **genomics-only** until physiological/biochemical confirmation.

## 3. Current applications and real-world implementations

**Direct applied deployment of the native DC/4HB cycle** is not yet a standard industrial chassis in the evidence retrieved here; however, two application-relevant themes emerge:
1) **Climate/biomanufacturing framing:** Recent reviews position multiple carbon-fixation pathways (including DC/4HB) as conceptual building blocks for CO2 bioconversion, highlighting the broader engineering relevance of understanding these pathways (e.g., supply of ATP/NAD(P)H, carboxylase selection). (scott2024widespreaddissolvedinorganic pages 10-13)
2) **Genome-informed bioprospecting and ecosystem modeling:** MAG-based discovery and distribution mapping (including DC/4HB in deep-branching archaeal groups) is an active real-world implementation in environmental microbiology—used to infer primary production strategies in diverse habitats and to identify candidate organisms/enzymes for future biotechnological exploration. (garritano2022carbonfixationpathways pages 5-7, garritano2022carbonfixationpathways pages 1-2)

## 4. Expert opinions and authoritative analysis

### 4.1 Oxygen sensitivity as a primary ecological constraint (authoritative synthesis)
An authoritative ecological review states the pathway is:
- “**restricted to organisms growing under anoxic conditions due to oxygen sensitivity of key enzymes and electron carriers**,” and contrasts it with oxygen-tolerant HP/4HB in (micro)aerobic Sulfolobales. (berg2011ecologicalaspectsof pages 8-9)
This provides a mechanistic ecological rationale suitable for a high-level **Environment → Pathway activity** causal edge.

### 4.2 Shared 4HB chemistry with distinct upstream fixation modules
Multiple authoritative sources emphasize that DC/4HB and 3HP/4HB share the succinyl‑CoA→acetyl‑CoA regeneration chemistry but differ in carbon fixation entry. This comparison is visually summarized in the pathway diagram (Figure 3) from an Annual Reviews synthesis. (fuchs2011alternativepathwaysof pages 7-8, fuchs2011alternativepathwaysof media 0cfdc547)

## 5. Relevant statistics and data from recent studies

- **52,515 MAGs** analyzed and **1,007 MAGs** with confidently identified carbon fixation pathways (CFPs) in a 2022 global MAG study that includes DC/4HB among analyzed pathways. (garritano2022carbonfixationpathways pages 1-2)
- “**two MAGs classified as Lokiarchaeia … contain all genes for the DC/HB cycle**” (explicit quantitative statement for DC/4HB-like gene sets). (garritano2022carbonfixationpathways pages 5-7)
- 2024 genome-survey qualitative statistic: “**about half**” of DCHB-assigned genomes encode **cytoplasmic carbonic anhydrase**, and those belong to **Pyrobaculum** (no absolute counts in retrieved excerpt). (scott2024widespreaddissolvedinorganic pages 15-18)

## 6. Trait scope details for curation (what is “in” vs “out”)

### In-scope phenotype/capacity
- **Autotrophic growth supported by DC/4HB carbon fixation** (capacity inferred by enzymology + isotope tracing, or by genomic completeness with caution). (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, garritano2022carbonfixationpathways pages 5-7)
- **Preference/compatibility with anoxic conditions** due to oxygen-sensitive ferredoxin-dependent carboxylation machinery. (berg2011ecologicalaspectsof pages 8-9)

### Out-of-scope / boundary conditions
- **Organisms with only partial 4HB branch** (e.g., possessing 4-hydroxybutyryl‑CoA dehydratase but lacking upstream carboxylation steps) should not be annotated as full DC/4HB.
- **3HP/4HB cycle organisms** (aerobic/microaerobic Sulfolobales) should be mapped to the separate trait unless specific evidence supports DC/4HB use.
- **rTCA-only organisms**: Given the explicit caution that some DCHB genomic assignments (e.g., in Pyrobaculum) could represent rTCA usage, treat those as uncertain without additional evidence. (scott2024widespreaddissolvedinorganic pages 15-18)

## 7. Candidate causal-graph nodes (grouped)

### 7.1 Pathways / metabolic modules
- DC/4HB cycle (METPO:traitmech:000025)
- 4‑hydroxybutyrate branch (shared with 3HP/4HB) (label-only)
- Incomplete reductive TCA segment to succinyl‑CoA (label-only) (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)

### 7.2 Environmental factors (ENVO candidates)
- Anoxic conditions / low oxygen (ENVO label-only)
- Thermophilic/hyperthermophilic habitat (hot springs/hydrothermal) (label-only; see thermophile context in DIC toolkit discussion) (scott2024widespreaddissolvedinorganic pages 15-18)

### 7.3 Genes / proteins / enzyme activities
(Include EC where clear; gene IDs given when available)
- Pyruvate synthase / pyruvate:ferredoxin oxidoreductase (PFOR) (EC candidate 1.2.7.1) (quaranta2010carbondioxideas pages 59-61, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
- Phosphoenolpyruvate carboxylase (PEPC) (EC:4.1.1.31) (quaranta2010carbondioxideas pages 59-61)
- Succinyl‑CoA reductase (gene candidates Msed_0709 / Tneu_0421) (fuchs2011alternativepathwaysof pages 7-8)
- Succinic semialdehyde reductase (gene candidates Msed_1424 / Tneu_0419) (fuchs2011alternativepathwaysof pages 7-8)
- 4‑hydroxybutyrate‑CoA ligase (Tneu_0420; gene unknown in some taxa) (fuchs2011alternativepathwaysof pages 7-8)
- 4‑hydroxybutyryl‑CoA dehydratase (e.g., Igni_0595; Msed_1321; Tneu_0422) (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, fuchs2011alternativepathwaysof pages 7-8)
- Putative DC/4HB gene cluster region in Thermoproteus neutrophilus (Tneu_0420–Tneu_0425) (ramosvera2009autotrophiccarbondioxide pages 8-9)

### 7.4 Metabolites / chemicals (CHEBI candidates)
- CO2 (CHEBI:16526) (quaranta2010carbondioxideas pages 59-61)
- bicarbonate (CHEBI:17544) (quaranta2010carbondioxideas pages 59-61)
- acetyl‑CoA (CHEBI:15351), pyruvate (CHEBI:15361), PEP (CHEBI:18021), oxaloacetate (CHEBI:16452) (quaranta2010carbondioxideas pages 59-61)
- succinyl‑CoA (CHEBI:15380), succinic semialdehyde (CHEBI:16384), 4‑hydroxybutyrate (CHEBI:30830), crotonyl‑CoA (CHEBI:37554) (fuchs2011alternativepathwaysof pages 7-8, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
- acetate (CHEBI:30089) (regulatory condition) (ramosvera2009autotrophiccarbondioxide pages 8-9)

### 7.5 Experimental factors / assays
- Enzyme activity assays demonstrating presence of all steps (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
- Isotope tracer incorporation into intermediates/biomass (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
- Genomic pathway reconstruction / presence of complete gene sets (garritano2022carbonfixationpathways pages 5-7)

## 8. Candidate causal edges (evidence-backed triples)

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (verbatim, short) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|---|
| dicarboxylate/4-hydroxybutyrate cycle (METPO:traitmech:000025) | occurs_in | anaerobic autotrophic Thermoproteales and Desulfurococcales (NCBITaxon candidates) | “reported mainly from mostly anaerobic autotrophic representatives of Thermoproteales and Desulfurococcales” (berg2011ecologicalaspectsof pages 8-9) | 10.1128/AEM.02473-10; https://doi.org/10.1128/AEM.02473-10; 2011 | Strong scope statement; taxon grounding should be refined to specific clades/species before curation. |
| molecular oxygen (CHEBI:15379) | negatively_regulates / constrains | dicarboxylate/4-hydroxybutyrate cycle (METPO:traitmech:000025) | “restricted to organisms growing under anoxic conditions due to oxygen sensitivity of key enzymes and electron carriers” (berg2011ecologicalaspectsof pages 8-9) | 10.1128/AEM.02473-10; https://doi.org/10.1128/AEM.02473-10; 2011 | Strong ecological constraint; mechanism attributed to O2-sensitive enzymes/electron carriers. |
| carbon dioxide (CHEBI:16526) | is_cosubstrate_for | pyruvate synthase / pyruvate:ferredoxin oxidoreductase (EC candidate 1.2.7.1) | “CO2 as cosubstrate for pyruvate synthase” (quaranta2010carbondioxideas pages 59-61) | 10.1002/9783527629916; https://doi.org/10.1002/9783527629916; 2010 | Strong biochemical distinction for one carboxylation step in DC/4HB. |
| bicarbonate (CHEBI:17544) | is_cosubstrate_for | phosphoenolpyruvate carboxylase (EC:4.1.1.31) | “bicarbonate as cosubstrate for PEP” (quaranta2010carbondioxideas pages 59-61) | 10.1002/9783527629916; https://doi.org/10.1002/9783527629916; 2010 | Supports mixed CO2/HCO3- usage in cycle. |
| pyruvate synthase / pyruvate:ferredoxin oxidoreductase (EC candidate 1.2.7.1) | carboxylates / converts | acetyl-CoA (CHEBI:15351) to pyruvate (CHEBI:15361) | “starts from acetyl-CoA, which is reductively carboxylated to pyruvate” (quaranta2010carbondioxideas pages 59-61) | 10.1002/9783527629916; https://doi.org/10.1002/9783527629916; 2010 | Mechanistic edge for first fixation step; exact reaction direction depends on pathway context. |
| phosphoenolpyruvate carboxylase (EC:4.1.1.31) | carboxylates / converts | phosphoenolpyruvate (CHEBI:18021) to oxaloacetate (CHEBI:16452) | “Pyruvate is converted to PEP and then carboxylated to oxaloacetate.” (quaranta2010carbondioxideas pages 59-61) | 10.1002/9783527629916; https://doi.org/10.1002/9783527629916; 2010 | Strong pathway step; enzyme identity supported in multiple reviews/primary studies. |
| succinyl-CoA reductase (label; gene candidates Msed_0709/Tneu_0421) | converts | succinyl-CoA (CHEBI:15380) to succinic semialdehyde (CHEBI:16384) | “succinyl-CoA reductase (Msed_0709/Tneu_0421)” (fuchs2011alternativepathwaysof pages 7-8) | 10.1146/annurev-micro-090110-102801; https://doi.org/10.1146/annurev-micro-090110-102801; 2011 | Gene-to-enzyme assignment is candidate-level in figure caption; curate as somewhat uncertain unless primary enzymology is added. |
| succinic semialdehyde reductase (label; gene candidates Msed_1424/Tneu_0419) | converts | succinic semialdehyde (CHEBI:16384) to 4-hydroxybutyrate (CHEBI:30830) | “succinic semialdehyde reductase (Msed_1424/Tneu_0419)” (fuchs2011alternativepathwaysof pages 7-8) | 10.1146/annurev-micro-090110-102801; https://doi.org/10.1146/annurev-micro-090110-102801; 2011 | Candidate enzyme/reaction from comparative pathway reconstruction. |
| 4-hydroxybutyrate-CoA ligase (label; gene candidate Tneu_0420) | activates / converts | 4-hydroxybutyrate (CHEBI:30830) to 4-hydroxybutyryl-CoA (CHEBI candidate) | “4-hydroxybutyrate-CoA ligase (gene unknown in Metallosphaera sedula/Tneu_0420)” (fuchs2011alternativepathwaysof pages 7-8) | 10.1146/annurev-micro-090110-102801; https://doi.org/10.1146/annurev-micro-090110-102801; 2011 | Important step, but gene assignment explicitly uncertain in some taxa. |
| 4-hydroxybutyryl-CoA dehydratase (label; GO candidate 0018798) | converts | 4-hydroxybutyryl-CoA (CHEBI candidate) to crotonyl-CoA (CHEBI:37554) | “dehydrated by a radical 4-hydroxybutyryl-CoA dehydratase to crotonyl-CoA” (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2) | 10.1073/pnas.0801043105; https://doi.org/10.1073/pnas.0801043105; 2008 | Core hallmark enzyme of 4HB branch; strong mechanistic support. |
| crotonyl-CoA (CHEBI:37554) | is_converted_via_beta_oxidation_to | acetyl-CoA (CHEBI:15351) | “via -oxidation yields two acetyl-CoA” (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2) | 10.1073/pnas.0801043105; https://doi.org/10.1073/pnas.0801043105; 2008 | Strong overall branch outcome; intermediate enzymes can be expanded separately if needed. |
| Tneu_0420-Tneu_0425 gene cluster (label) | encodes_components_of | DC/4HB 4-hydroxybutyrate branch enzymes (label set) | “a putative gene cluster encoding multiple DC/4HB enzymes (PEP carboxylase, succinic semialdehyde reductase, 4-hydroxybutyryl-CoA dehydratase, fumarate reductase) … with gene identifiers such as Tneu_0420–Tneu_0425” (ramosvera2009autotrophiccarbondioxide pages 8-9) | 10.1128/JB.00145-09; https://doi.org/10.1128/JB.00145-09; 2009 | Good genomic-support edge; use “encodes_components_of” rather than exact per-gene enzymatic assertions unless individually validated. |
| Igni_0595 (label) | encodes | 4-hydroxybutyryl-CoA dehydratase (label) | “the genome contains a gene for 4-hydroxybutyryl-CoA dehydratase (Igni_0595” (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2) | 10.1073/pnas.0801043105; https://doi.org/10.1073/pnas.0801043105; 2008 | Strong gene-presence evidence in Ignicoccus hospitalis; direct biochemical confirmation of protein product should still be checked. |
| acetate (CHEBI:30089) | represses | carbon fixation cycle key enzymes including fumarase/fumarate reductase (label) | “acetate represses the carbon fixation cycle by downregulating key enzymes (notably fumarase and fumarate reductase)” (ramosvera2009autotrophiccarbondioxide pages 8-9) | 10.1128/JB.00145-09; https://doi.org/10.1128/JB.00145-09; 2009 | Condition-specific regulatory edge in Thermoproteus neutrophilus; likely taxon- and growth-condition-specific. |
| DCHB/DC/4HB genomes (label) | often_lack | known DIC transporter genes (label) | “organisms inferred to use the DCHB (dicarboxylate/4-hydroxybutyrate) cycle generally lack genes for known DIC transporters” (scott2024widespreaddissolvedinorganic pages 15-18) | 10.1128/AEM.01557-23; https://doi.org/10.1128/AEM.01557-23; 2024 | Recent comparative-genomics result; useful but pathway assignments for some genomes are uncertain. |
| DCHB/DC/4HB genomes (label) | sometimes_encode | cytoplasmic carbonic anhydrase (GO:0004089) | “about half of these genomes encode cytoplasmic carbonic anhydrase (cCA), with those cCA-containing genomes belonging to the genus Pyrobaculum” (scott2024widespreaddissolvedinorganic pages 15-18) | 10.1128/AEM.01557-23; https://doi.org/10.1128/AEM.01557-23; 2024 | Recent genome-survey finding; likely genus-biased and sensitive to small sample size. |
| Lokiarchaeia MAGs (NCBITaxon candidate) | have_genomic_evidence_for | dicarboxylate/4-hydroxybutyrate cycle (METPO:traitmech:000025) | “two MAGs classified as Lokiarchaeia (phylum Asgardarchaeota) contain all genes for the DC/HB cycle” (garritano2022carbonfixationpathways pages 5-7) | 10.1093/pnasnexus/pgac226; https://doi.org/10.1093/pnasnexus/pgac226; 2022 | Important expansion of inferred distribution; genomics-only, not physiological proof. |
| Sulfolobus (NCBITaxon:2285) | has_genomic_evidence_for | dicarboxylate/4-hydroxybutyrate cycle (METPO:traitmech:000025) | “for the first time, genomic evidence for the DC/HB cycle in the genus Sulfolobus, supported by the presence of all required enzymes” (garritano2022carbonfixationpathways pages 5-7) | 10.1093/pnasnexus/pgac226; https://doi.org/10.1093/pnasnexus/pgac226; 2022 | Potentially important boundary case because Sulfolobus is classically associated with 3HP/4HB; should be curated cautiously pending physiological validation. |


*Table: This table compiles candidate causal edges for curating the dicarboxylate/4-hydroxybutyrate cycle trait, linking pathway steps, enzymes, genes, environmental constraints, and recent comparative-genomics findings. It is useful as a starting evidence matrix for deciding which nodes and edges are ready for TraitMech curation versus which remain uncertain or taxa-specific.*

## 9. Key figure supporting pathway structure

A curated pathway comparison figure is available as **Figure 3** (DC/4HB vs 3HP/4HB) from Annual Review of Microbiology; it is useful for confirming node/edge ordering and shared vs distinct steps. (fuchs2011alternativepathwaysof media 0cfdc547)

## 10. DOI-first bibliography (with URLs and publication dates)

1. Scott KM, Payne RR, Gahramanova A. **Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…** *Applied and Environmental Microbiology.* **2024-02**. DOI: **10.1128/aem.01557-23**. https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 15-18, scott2024widespreaddissolvedinorganic pages 4-7, scott2024widespreaddissolvedinorganic pages 13-15, scott2024widespreaddissolvedinorganic pages 7-10, scott2024widespreaddissolvedinorganic pages 10-13)
2. Garritano AN, Song W, Thomas T. **Carbon fixation pathways across the bacterial and archaeal tree of life.** *PNAS Nexus.* **2022-10**. DOI: **10.1093/pnasnexus/pgac226**. https://doi.org/10.1093/pnasnexus/pgac226 (garritano2022carbonfixationpathways pages 5-7, garritano2022carbonfixationpathways pages 1-2, garritano2022carbonfixationpathways pages 7-9)
3. Berg IA. **Ecological aspects of the distribution of different autotrophic CO2 fixation pathways.** *Applied and Environmental Microbiology.* **2011-03**. DOI: **10.1128/AEM.02473-10**. https://doi.org/10.1128/AEM.02473-10 (berg2011ecologicalaspectsof pages 8-9)
4. Fuchs G. **Alternative pathways of carbon dioxide fixation: insights into the early evolution of life?** *Annual Review of Microbiology.* **2011-10**. DOI: **10.1146/annurev-micro-090110-102801**. https://doi.org/10.1146/annurev-micro-090110-102801 (fuchs2011alternativepathwaysof pages 7-8, fuchs2011alternativepathwaysof media 0cfdc547)
5. Ramos‑Vera WH, Berg IA, Fuchs G. **Autotrophic carbon dioxide assimilation in Thermoproteales revisited.** *Journal of Bacteriology.* **2009-07**. DOI: **10.1128/jb.00145-09**. https://doi.org/10.1128/jb.00145-09 (ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2009autotrophiccarbondioxide pages 8-9)
6. Huber H, Gallenberger M, Jahn U, et al. **A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum Ignicoccus hospitalis.** *PNAS.* **2008-06**. DOI: **10.1073/pnas.0801043105**. https://doi.org/10.1073/pnas.0801043105 (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
7. Berg IA, Kockelkorn D, Ramos‑Vera WH. **Carbon dioxide as chemical feedstock.** (book chapter; retrieved as arXiv-linked source). **2010-02**. DOI: **10.1002/9783527629916**. https://doi.org/10.1002/9783527629916 (quaranta2010carbondioxideas pages 59-61)

## 11. Warnings / claims not yet ready for curation

1. **Pyrobaculum DC/4HB assignment is uncertain in some cases.** Genome data may suggest DCHB/DC‑4HB, but “other evidence is less conclusive” and some may use **rTCA** instead; edges tying Pyrobaculum to DC/4HB should be marked **uncertain** unless supported by physiology/biochemistry. (scott2024widespreaddissolvedinorganic pages 15-18)
2. **“All genes present” ≠ demonstrated phenotype.** MAG-based detection (e.g., Lokiarchaeia MAGs; Sulfolobus) is strong for hypothesis generation but should be curated as **genomic potential** rather than confirmed pathway activity. (garritano2022carbonfixationpathways pages 5-7)
3. **Gene-to-enzyme mappings in pathway figures are candidate-level.** Some enzyme assignments explicitly note “gene unknown” in certain taxa; curate these edges with uncertainty or require primary enzymology/proteomics confirmation before promoting to high-confidence. (fuchs2011alternativepathwaysof pages 7-8)


References

1. (quaranta2010carbondioxideas pages 59-61): IA Berg, D Kockelkorn, and WH Ramos‐Vera. Carbon dioxide as chemical feedstock. ArXiv, Feb 2010. URL: https://doi.org/10.1002/9783527629916, doi:10.1002/9783527629916. This article has 769 citations.

2. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2): Harald Huber, Martin Gallenberger, Ulrike Jahn, Eva Eylert, Ivan A. Berg, Daniel Kockelkorn, Wolfgang Eisenreich, and Georg Fuchs. A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum ignicoccus hospitalis. Proceedings of the National Academy of Sciences, 105:7851-7856, Jun 2008. URL: https://doi.org/10.1073/pnas.0801043105, doi:10.1073/pnas.0801043105. This article has 433 citations and is from a highest quality peer-reviewed journal.

3. (berg2011ecologicalaspectsof pages 8-9): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1005 citations and is from a peer-reviewed journal.

4. (ramosvera2011identificationofmissing pages 1-2): W. Hugo Ramos-Vera, Michael Weiss, Eric Strittmatter, Daniel Kockelkorn, and Georg Fuchs. Identification of missing genes and enzymes for autotrophic carbon fixation in <i>crenarchaeota</i>. Mar 2011. URL: https://doi.org/10.1128/jb.01156-10, doi:10.1128/jb.01156-10. This article has 61 citations and is from a peer-reviewed journal.

5. (fuchs2011alternativepathwaysof media 0cfdc547): Georg Fuchs. Alternative pathways of carbon dioxide fixation: insights into the early evolution of life? Oct 2011. URL: https://doi.org/10.1146/annurev-micro-090110-102801, doi:10.1146/annurev-micro-090110-102801. This article has 859 citations and is from a peer-reviewed journal.

6. (scott2024widespreaddissolvedinorganic pages 15-18): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

8. (garritano2022carbonfixationpathways pages 1-2): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

9. (garritano2022carbonfixationpathways pages 5-7): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

10. (scott2024widespreaddissolvedinorganic pages 10-13): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

11. (fuchs2011alternativepathwaysof pages 7-8): Georg Fuchs. Alternative pathways of carbon dioxide fixation: insights into the early evolution of life? Oct 2011. URL: https://doi.org/10.1146/annurev-micro-090110-102801, doi:10.1146/annurev-micro-090110-102801. This article has 859 citations and is from a peer-reviewed journal.

12. (ramosvera2009autotrophiccarbondioxide pages 8-9): W. Hugo Ramos-Vera, Ivan A. Berg, and Georg Fuchs. Autotrophic carbon dioxide assimilation in <i>thermoproteales</i> revisited. Jul 2009. URL: https://doi.org/10.1128/jb.00145-09, doi:10.1128/jb.00145-09. This article has 104 citations and is from a peer-reviewed journal.

13. (scott2024widespreaddissolvedinorganic pages 4-7): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

14. (scott2024widespreaddissolvedinorganic pages 13-15): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

15. (garritano2022carbonfixationpathways pages 7-9): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

16. (ramosvera2009autotrophiccarbondioxide pages 1-2): W. Hugo Ramos-Vera, Ivan A. Berg, and Georg Fuchs. Autotrophic carbon dioxide assimilation in <i>thermoproteales</i> revisited. Jul 2009. URL: https://doi.org/10.1128/jb.00145-09, doi:10.1128/jb.00145-09. This article has 104 citations and is from a peer-reviewed journal.