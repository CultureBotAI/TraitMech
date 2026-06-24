---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:02:57.524085'
end_time: '2026-06-18T06:16:32.601386'
duration_seconds: 815.08
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: 3-hydroxypropionate bicycle
  trait_identifier: traitmech:000023
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: three_hydroxypropionate_bicycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway in which two molecules of bicarbonate
    are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It
    is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
  parent_traits: traitmech:000019
  synonyms: 3-hydroxypropionate cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate\
    \ bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert include the 3-hydroxypropionate pathway among autotrophic\
    \ carbon-fixation strategies.)"
  causal_graph_summary: 'three_hp_bicycle_chloroflexus: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate bicycle
- **METPO identifier:** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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
- **Trait label:** 3-hydroxypropionate bicycle
- **METPO identifier:** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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


# Microbial Trait Causal Graph Curation Report: 3‑hydroxypropionate bicycle (METPO:traitmech:000023)

## 0. Executive scope summary (TraitMech curation focus)

**Trait definition (operationalized for curation).** The **3‑hydroxypropionate bicycle (3‑HP bicycle; 3‑hydroxypropionate cycle; 3‑HP/malyl‑CoA cycle)** is an **autotrophic inorganic carbon fixation pathway** in which **bicarbonate (HCO3−)** is enzymatically activated and incorporated through **biotin‑dependent carboxylases** and downstream CoA‑thioester chemistry, producing **glyoxylate** (first cycle) and net **pyruvate** (overall) while regenerating **acetyl‑CoA** (second cycle). The pathway is classically associated with **Chloroflexus aurantiacus** and (historically) the family **Chloroflexaceae**. (hugler2011beyondthecalvin pages 9-10, hugler2011beyondthecalvin pages 7-9, zarzycki2011coassimilationoforganic pages 5-7)

**Boundary conditions / nearby traits.** 
- Distinct from the archaeal **3‑hydroxypropionate/4‑hydroxybutyrate (3HP/4HB) cycle**, which shares the *carboxylation logic* (acetyl‑CoA and propionyl‑CoA carboxylation) but differs in downstream acetyl‑CoA regeneration and product (3HP/4HB produces acetyl‑CoA; 3‑HP bicycle produces pyruvate and glyoxylate intermediacy). (mclean2022invitrorealisation pages 22-29)
- Distinct from the **Calvin–Benson–Bassham (CBB) cycle**, **rTCA**, **Wood–Ljungdahl**, etc., by its diagnostic enzyme set (e.g., malonyl‑CoA reductase and propionyl‑CoA synthase) and malyl/citramalyl‑CoA lyase chemistry. (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 1-2)

**What the trait represents for causal-graph purposes.** A microbe possessing this trait has the **physiological capacity for autotrophic growth on inorganic carbon** using the **3‑HP bicycle module**, under conditions that supply **energy (e.g., light for phototrophs)** and reducing power/ATP for the required carboxylation and reduction steps. (kang2023insightsintoenzyme pages 2-4, freches2024thebiotechnologicalpotential pages 14-15)


## 1. Key concepts and current understanding (mechanism-level)

### 1.1 Two-cycle architecture and overall output
A central conceptual feature is that the pathway comprises **two linked cycles**: 
1) a **first cycle** that **fixes two bicarbonate molecules to produce glyoxylate**, and 
2) a **second cycle** that uses **glyoxylate and propionyl‑CoA** to yield **pyruvate and acetyl‑CoA** (disproportionation) while regenerating acetyl‑CoA. (hugler2011beyondthecalvin pages 7-9, hugler2011beyondthecalvin pages 9-10)

A widely cited stoichiometric summary is that the bicycle produces **“one molecule of pyruvate from three molecules of bicarbonate.”** (hugler2011beyondthecalvin pages 9-10)

### 1.2 Core CO2/HCO3− fixation chemistry: biotin-dependent carboxylases
Carboxylation steps are catalyzed by **biotin‑dependent acetyl‑CoA carboxylase (Acc; EC 6.4.1.2)** and **propionyl‑CoA carboxylase (Pcc; EC 6.4.1.3)**.
- Acc converts **acetyl‑CoA + bicarbonate → malonyl‑CoA** (ATP-dependent). (mclean2022invitrorealisation pages 22-29)
- Pcc converts **propionyl‑CoA + bicarbonate → (2S)-methylmalonyl‑CoA** (ATP-dependent). (mclean2022invitrorealisation pages 22-29)

Recent CO2‑conversion reviews reiterate that **two bicarbonate molecules are incorporated by acetyl‑CoA carboxylase and propionyl‑CoA carboxylase** and that these steps require ATP. (kang2023insightsintoenzyme pages 2-4)

Mechanistically, biotin-dependent carboxylases activate bicarbonate/CO2 through ATP-dependent chemistry and a swinging biotin arm, enabling carboxyl transfer to activated substrates—this is relevant when curating nodes for “ATP requirement” or “biotin cofactor dependency.” (grundling2020propionylcoasynthasecharacterization pages 21-24)

### 1.3 Diagnostic enzymes and metabolite flow
The bicycle is notable for using **multifunctional enzymes**: a review reports **13 enzymes catalyzing 19 reactions**. (hugler2011beyondthecalvin pages 9-10)

Key diagnostic enzymes (often used to identify the pathway genomically/biochemically) include:
- **Malonyl‑CoA reductase (Mcr)**: reduces malonyl‑CoA toward 3‑hydroxypropionate. (hugler2011beyondthecalvin pages 9-10)
- **Propionyl‑CoA synthase (Pcs/Pcr)**: converts 3‑hydroxypropionate/3‑hydroxypropionyl‑CoA through acryloyl‑CoA to **propionyl‑CoA**. (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 2-3)
- **MMC lyase / Mcl** (malyl‑CoA / β‑methylmalyl‑CoA / citramalyl‑CoA lyase): performs multiple functions, including **cleaving malyl‑CoA to acetyl‑CoA + glyoxylate** and **cleaving citramalyl‑CoA to pyruvate + acetyl‑CoA**. (hugler2011beyondthecalvin pages 9-10)

A primary-study enzyme list (pathway legend) for *C. aurantiacus* includes, among others: acetyl‑CoA carboxylase, malonyl‑CoA reductase, propionyl‑CoA synthase, propionyl‑CoA carboxylase, methylmalonyl‑CoA epimerase, methylmalonyl‑CoA mutase, succinyl‑CoA:(S)-malate‑CoA transferase, succinate dehydrogenase, fumarate hydratase, and mesaconyl‑CoA processing enzymes (Mch/Mct/Meh). (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7)


## 2. Trait scope details (what to curate vs. what not to)

### 2.1 Positive inclusion criteria (recommended)
Curate the trait when evidence supports:
- A **complete enzyme/gene complement** consistent with the two-cycle pathway (including at minimum diagnostic **Mcr + Pcs + MMC/Mcl** along with the relevant carboxylases and glyoxylate-assimilation segment). (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 5-7)
- Or **direct physiological/biochemical evidence** for autotrophic (or mixotrophic) bicarbonate fixation via the described intermediates in a given organism (classic case: *Chloroflexus aurantiacus*). (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 2-3)

### 2.2 Boundary cases and exclusion warnings
- **Partial gene presence is not sufficient**: multiple sources note partial distribution of individual genes (e.g., mcr/pcs) outside Chloroflexaceae. (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 5-7)
- MAG-based detection outside Chloroflexota should be treated as **genomic potential** and often incomplete; do not curate as “complete trait present” without completeness/physiology support. (garritano2022carbonfixationpathways pages 2-3)


## 3. Candidate causal-graph entities (nodes), grouped by type

The following node inventory is suitable for conversion into `three_hydroxypropionate_bicycle.yaml` (grounding suggestions where stable IDs are known).

| Node label | Node type (pathway/enzyme/metabolite/process/environment/taxon) | Brief definition/role in 3-HP bicycle | Suggested ontology grounding (CURIEs if known) | Key supporting reference (DOI, year, URL) |
|---|---|---|---|---|
| 3-hydroxypropionate bicycle | pathway | Autotrophic carbon-fixation pathway in two linked cycles that fixes bicarbonate via 3-hydroxypropionate chemistry and yields glyoxylate and net pyruvate (hugler2011beyondthecalvin pages 9-10, hugler2011beyondthecalvin pages 7-9) | METPO:traitmech:000023 | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| first cycle of 3-HP bicycle | process | First cycle fixes two bicarbonate molecules and produces glyoxylate as first fixation product (hugler2011beyondthecalvin pages 7-9) | label only | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| second cycle of 3-HP bicycle | process | Glyoxylate-assimilation cycle that disproportionates glyoxylate with propionyl-CoA to pyruvate and acetyl-CoA (hugler2011beyondthecalvin pages 9-10) | label only | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| bicarbonate | metabolite | Inorganic carbon substrate fixed by acetyl-CoA and propionyl-CoA carboxylases (mclean2022invitrorealisation pages 22-29, kang2023insightsintoenzyme pages 2-4) | CHEBI:17544 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| carbon dioxide | metabolite | Alternative inorganic carbon species discussed with bicarbonate in pathway and synthetic analogs (mclean2023exploringalternativepathways pages 1-2, mclean2023exploringalternativepathways pages 7-10) | CHEBI:16526 | 10.1126/sciadv.adh4299, 2023, https://doi.org/10.1126/sciadv.adh4299 |
| acetyl-CoA carboxylase (Acc) | enzyme | Biotin-dependent carboxylase converting acetyl-CoA + bicarbonate to malonyl-CoA at ATP expense (mclean2022invitrorealisation pages 22-29, kang2023insightsintoenzyme pages 2-4) | EC:6.4.1.2 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| propionyl-CoA carboxylase (Pcc) | enzyme | Biotin-dependent carboxylase converting propionyl-CoA + bicarbonate to (2S)-methylmalonyl-CoA at ATP expense (mclean2022invitrorealisation pages 22-29, kang2023insightsintoenzyme pages 2-4) | EC:6.4.1.3 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| malonyl-CoA reductase (Mcr) | enzyme | Key diagnostic enzyme reducing malonyl-CoA to 3-hydroxypropionate via malonic semialdehyde; multifunctional in Chloroflexus (mclean2023exploringalternativepathways pages 2-3, hugler2011beyondthecalvin pages 9-10) | EC:1.2.1.75 | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| propionyl-CoA synthase (Pcs/Pcr) | enzyme | Multifunctional enzyme converting 3-hydroxypropionate/3-hydroxypropionyl-CoA through acryloyl-CoA to propionyl-CoA (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 2-3) | label only | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| MMC lyase / Mcl | enzyme | Multifunctional lyase carrying out malyl-CoA cleavage, glyoxylate + propionyl-CoA condensation, and citramalyl-CoA cleavage (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 1-2) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| methylmalonyl-CoA epimerase (Epi) | enzyme | Interconverts methylmalonyl-CoA stereoisomers in the carboxylation branch (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | EC:5.1.99.1 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| methylmalonyl-CoA mutase (Mcm) | enzyme | Rearranges methylmalonyl-CoA to succinyl-CoA in the first-cycle branch (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | EC:5.4.99.2 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| succinyl-CoA:(S)-malate CoA transferase (Smt) | enzyme | CoA-transferase in glyoxylate-assimilation/oxidative segment; named core enzyme of the bicycle (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| succinate dehydrogenase (Sdh) | enzyme | Converts succinate/fumarate branch intermediate in the cycle’s central sequence (zarzycki2011coassimilationoforganic pages 1-2) | EC:1.3.5.1 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| fumarate hydratase (Fuh) | enzyme | Hydrates fumarate to malate in the central branch of the bicycle (zarzycki2011coassimilationoforganic pages 1-2) | EC:4.2.1.2 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| mesaconyl-C1-CoA hydratase (Mch) | enzyme | Core C5-transforming enzyme in glyoxylate-assimilation part of pathway (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| mesaconyl-CoA C1:C4 CoA transferase (Mct) | enzyme | Repositions CoA between mesaconyl-CoA isomers in C5 transformation segment (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| mesaconyl-C4-CoA hydratase (Meh) | enzyme | Hydratase in glyoxylate-assimilation segment of the 3-HP bicycle (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| biotin | metabolite | Covalent cofactor/swinging arm used by biotin-dependent acetyl-CoA and propionyl-CoA carboxylases (grundling2020propionylcoasynthasecharacterization pages 21-24) | CHEBI:15956 | 10.17192/z2020.0502, 2020, https://doi.org/10.17192/z2020.0502 |
| ATP | metabolite | Energy input for carboxylation steps catalyzed by Acc and Pcc (mclean2022invitrorealisation pages 22-29, kang2023insightsintoenzyme pages 2-4) | CHEBI:15422 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| NADPH | metabolite | Reducing cofactor used in malonyl-CoA/3-HP reduction chemistry and synthetic analog implementations (mclean2023exploringalternativepathways pages 2-3, mclean2023exploringalternativepathways pages 7-10) | CHEBI:16474 | 10.1126/sciadv.adh4299, 2023, https://doi.org/10.1126/sciadv.adh4299 |
| acetyl-CoA | metabolite | Starting substrate for first carboxylation and one regenerated product of the cycle (mclean2022invitrorealisation pages 22-29, hugler2011beyondthecalvin pages 9-10) | CHEBI:57288 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| malonyl-CoA | metabolite | Product of acetyl-CoA carboxylase and substrate of malonyl-CoA reductase (mclean2022invitrorealisation pages 22-29, hugler2011beyondthecalvin pages 9-10) | CHEBI:57384 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| malonic semialdehyde | metabolite | Intermediate between malonyl-CoA and 3-hydroxypropionate in Mcr-catalyzed route (mclean2023exploringalternativepathways pages 2-3, mclean2022invitrorealisation pages 29-35) | CHEBI:36010 | 10.1126/sciadv.adh4299, 2023, https://doi.org/10.1126/sciadv.adh4299 |
| 3-hydroxypropionate | metabolite | Signature intermediate of pathway formed from malonyl-CoA and converted toward propionyl-CoA (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 1-2) | CHEBI:36586 | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| 3-hydroxypropionyl-CoA | metabolite | CoA-thioester intermediate in Pcs-mediated conversion toward acryloyl-CoA and propionyl-CoA (zarzycki2011coassimilationoforganic pages 2-3, mclean2022invitrorealisation pages 29-35) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| acryloyl-CoA | metabolite | Reactive intermediate in conversion from 3-hydroxypropionyl-CoA to propionyl-CoA (zarzycki2011coassimilationoforganic pages 2-3, tommasi2024thebiochemistryof pages 12-14) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| propionyl-CoA | metabolite | Product of Pcs; substrate of Pcc; also combined with glyoxylate in second cycle (mclean2022invitrorealisation pages 22-29, hugler2011beyondthecalvin pages 9-10) | CHEBI:57347 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| (2S)-methylmalonyl-CoA | metabolite | Product of propionyl-CoA carboxylase and substrate for epimerase/mutase steps (mclean2022invitrorealisation pages 22-29, zarzycki2011coassimilationoforganic pages 1-2) | CHEBI:15541 | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| succinyl-CoA | metabolite | Central C4 CoA-thioester intermediate downstream of methylmalonyl-CoA mutase (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7) | CHEBI:57547 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| (S)-malyl-CoA | metabolite | Intermediate cleaved by MMC lyase to glyoxylate and acetyl-CoA (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 1-2) | label only | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| glyoxylate | metabolite | First CO2-fixation product of first cycle and substrate entering second cycle (hugler2011beyondthecalvin pages 9-10) | CHEBI:58049 | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| (S)-citramalyl-CoA | metabolite | Intermediate whose cleavage yields pyruvate and acetyl-CoA in second cycle (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 1-2) | label only | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| pyruvate | metabolite | Net output of complete 3-HP bicycle from fixed bicarbonate (hugler2011beyondthecalvin pages 9-10, mclean2022invitrorealisation pages 22-29) | CHEBI:15361 | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 |
| phototrophy | process | Physiological context in which Chloroflexus aurantiacus uses light energy while fixing carbon via the 3-HP bicycle (freches2024thebiotechnologicalpotential pages 14-15, kang2023insightsintoenzyme pages 2-4) | GO:0015979 | 10.4014/jmb.2306.06005, 2023, https://doi.org/10.4014/jmb.2306.06005 |
| thermophily | environment | Pathway is characteristic of thermophilic Chloroflexus aurantiacus and related Chloroflexaceae (mclean2022invitrorealisation pages 22-29, kang2023insightsintoenzyme pages 2-4) | label only | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| oxygen tolerance | process | Pathway/carboxylation logic described as oxygen-tolerant relative to many anaerobic fixation cycles (mclean2022invitrorealisation pages 22-29, wang2023microbialconversionand pages 3-5) | label only | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 |
| hydrogen | metabolite | Electron donor supporting photoautotrophic growth of C. aurantiacus using the 3-HP bicycle (freches2024thebiotechnologicalpotential pages 14-15) | CHEBI:18276 | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 |
| sulfide | metabolite | Electron donor supporting photoautotrophic growth of C. aurantiacus using the 3-HP bicycle (freches2024thebiotechnologicalpotential pages 14-15) | CHEBI:18421 | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 |
| coassimilation of acetate | process | 3-HP bicycle enzymes remain active during photoheterotrophy and support coassimilation of acetate/organic acids (zarzycki2011coassimilationoforganic pages 5-7, zarzycki2011coassimilationoforganic pages 2-3) | label only | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| Chloroflexus aurantiacus | taxon | Canonical organism in which the 3-HP bicycle was elucidated; thermophilic filamentous anoxygenic phototroph (hugler2011beyondthecalvin pages 9-10, freches2024thebiotechnologicalpotential pages 14-15) | NCBITaxon:324602 | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 |
| Chloroflexaceae | taxon | Family historically considered to contain the full gene set for the complete 3-HP bicycle (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 5-7) | NCBITaxon:200795 | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 |
| Chloroflexota | taxon | Broader bacterial phylum containing Chloroflexus; recent reviews discuss its biotechnological potential and carbon fixation roles (freches2024thebiotechnologicalpotential pages 14-15, freches2024thebiotechnologicalpotential pages 17-18) | NCBITaxon:200795? | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of the 3-hydroxypropionate bicycle, spanning pathway structure, enzymes, metabolites, physiology, and taxa. It is useful as a node inventory for curating grounded entities before assigning causal edges.*


## 4. Evidence-backed candidate causal edges (triples)

The following table provides curation-ready **subject–predicate–object** triples with supporting snippets, references, and uncertainty flags.

| Subject (node) | Predicate | Object (node) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested grounding (CURIEs for nodes where possible) |
|---|---|---|---|---|---|---|
| 3-hydroxypropionate bicycle | fixes | bicarbonate | “the first fixes two bicarbonate molecules to produce glyoxylate” (hugler2011beyondthecalvin pages 7-9) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong pathway-level evidence; review summarizing primary biochemistry | METPO:traitmech:000023; CHEBI:17544 bicarbonate |
| acetyl-CoA carboxylase | causally_upstream_of | malonyl-CoA | “acetyl-CoA carboxylase (EC 6.4.1.2) converts acetyl-CoA and bicarbonate to malonyl-CoA at the expense of ATP” (mclean2022invitrorealisation pages 22-29) | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 | Strong mechanistic statement; thesis/research text, but consistent with reviews | EC:6.4.1.2; CHEBI:57288 acetyl-CoA; CHEBI:57384 malonyl-CoA |
| propionyl-CoA carboxylase | causally_upstream_of | (2S)-methylmalonyl-CoA | “propionyl-CoA carboxylase (EC 6.4.1.3) converts propionyl-CoA and bicarbonate to (2S)-methylmalonyl-CoA at the expense of ATP” (mclean2022invitrorealisation pages 22-29) | 10.17192/z2022.0467, 2022, https://doi.org/10.17192/z2022.0467 | Strong mechanistic statement; consistent across sources | EC:6.4.1.3; CHEBI:57347 propionyl-CoA; CHEBI:15541 methylmalonyl-CoA |
| malonyl-CoA reductase | causally_upstream_of | 3-hydroxypropionate | “malonyl-CoA reductase reducing malonyl-CoA to 3-hydroxypropionate” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong, central diagnostic enzyme for pathway | EC:1.2.1.75; CHEBI:57384 malonyl-CoA; CHEBI:36586 3-hydroxypropionate |
| propionyl-CoA synthase | causally_upstream_of | propionyl-CoA | “propionyl-CoA synthase converting 3-hydroxypropionate to propionyl-CoA” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong; multifunctional fusion enzyme in Chloroflexus | CHEBI:36586 3-hydroxypropionate; CHEBI:57347 propionyl-CoA |
| (S)-malyl-CoA lyase activity of MMC lyase | produces | glyoxylate + acetyl-CoA | “cleavage of malyl-CoA to acetyl-CoA and glyoxylate” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong biochemical function; enzyme is multifunctional MMC lyase | CHEBI:58049 glyoxylate; CHEBI:57288 acetyl-CoA |
| MMC lyase | causally_upstream_of | pyruvate + acetyl-CoA | “cleavage of citramalyl-CoA to pyruvate and acetyl-CoA” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong biochemical function; supports second-cycle output | CHEBI:15361 pyruvate; CHEBI:57288 acetyl-CoA |
| glyoxylate + propionyl-CoA | participates_in | second cycle yielding pyruvate + acetyl-CoA | “glyoxylate and propionyl-CoA are disproportionated to pyruvate and acetyl-CoA” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong pathway-level edge; exact intermediate sequence compressed in review | CHEBI:58049 glyoxylate; CHEBI:57347 propionyl-CoA; CHEBI:15361 pyruvate; CHEBI:57288 acetyl-CoA |
| 3-hydroxypropionate bicycle | has_output | pyruvate | “producing one pyruvate from three bicarbonates” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong overall stoichiometric summary | METPO:traitmech:000023; CHEBI:15361 pyruvate; CHEBI:17544 bicarbonate |
| 3-hydroxypropionate bicycle | occurs_in | Chloroflexaceae | “the complete 3-HP bicycle appears restricted to Chloroflexaceae” (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712, 2011, https://doi.org/10.1146/annurev-marine-120709-142712 | Strong historical consensus, but see newer MAG evidence below | NCBITaxon:200795 Chloroflexaceae |
| complete 3-hydroxypropionate bicycle gene set | present_in | Chloroflexaceae members | “Only Chloroflexaceae members possess the full gene set for the complete bi-cycle” (zarzycki2011coassimilationoforganic pages 5-7) | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 | Strong for cultured genomes available then; taxon-specific | NCBITaxon:200795 Chloroflexaceae |
| 3-hydroxypropionate bicycle genes | potentially_occur_in | Gemmatimonadota / Proteobacteria MAGs | “all genes required for the 3HP bi-cycle in two Gemmatimonadota MAGs” and MAGs in Proteobacterial families above thresholds (garritano2022carbonfixationpathways pages 2-3) | 10.1093/pnasnexus/pgac226, 2022, https://doi.org/10.1093/pnasnexus/pgac226 | Uncertain for phenotype; genome-based potential only, not physiological validation | NCBITaxon:219685 Gemmatimonadota; NCBITaxon:1224 Proteobacteria |
| Actinobacteriota MAGs with key 3HP enzymes | supports_only_partial | 3-hydroxypropionate bicycle potential | “27 Actinobacteriota MAGs; however, the average pathway completeness there was only 68.6%” (garritano2022carbonfixationpathways pages 2-3) | 10.1093/pnasnexus/pgac226, 2022, https://doi.org/10.1093/pnasnexus/pgac226 | Do not curate as full trait without stronger evidence; incomplete pathway | NCBITaxon:201174 Actinobacteriota |
| glyoxylate-assimilation genes | clustered_in_genome_of | Chloroflexus aurantiacus | “genes for the glyoxylate-assimilation part are clustered” (zarzycki2011coassimilationoforganic pages 5-7) | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 | Genomic organization edge; taxon-specific, useful for curation heuristics | NCBITaxon:324602 Chloroflexus aurantiacus |
| mcr and pcs genes | located_separately_from | glyoxylate-assimilation gene cluster | “malonyl-CoA reductase and propionyl-CoA synthase are each located separately, far from that cluster” (zarzycki2011coassimilationoforganic pages 5-7) | 10.1128/AEM.00705-11, 2011, https://doi.org/10.1128/AEM.00705-11 | Genomic organization edge; taxon-specific | label:mcr; label:pcs; NCBITaxon:324602 Chloroflexus aurantiacus |
| Chloroflexus aurantiacus | grows_photoautotrophically_with | hydrogen or sulfide | “C. aurantiacus can grow photoautotrophically using hydrogen or sulfide as electron donors” (freches2024thebiotechnologicalpotential pages 14-15) | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 | Strong ecological/physiological context from recent review | NCBITaxon:324602 Chloroflexus aurantiacus; CHEBI:18276 hydrogen; CHEBI:18421 sulfide |
| 3-hydroxypropionate bicycle | associated_with | thermophilic phototrophy | “discovered in Chloroflexus aurantiacus, a thermophilic green nonsulfur bacterium that obtains energy from light” (kang2023insightsintoenzyme pages 2-4) | 10.4014/jmb.2306.06005, 2023, https://doi.org/10.4014/jmb.2306.06005 | Context edge rather than direct mechanism; useful for trait scope | ENVO:01000215 photic zone [candidate context only]; label:thermophilic phototrophy |
| acetyl-CoA and propionyl-CoA | are_precursors_of | polyhydroxyalkanoate accumulation | “some intermediates of the 3-HP pathway (notably acetyl-CoA and propionyl-CoA) are precursors for polyhydroxyalkanoate (PHA) accumulation” (freches2024thebiotechnologicalpotential pages 14-15) | 10.1128/AEM.01756-23, 2024, https://doi.org/10.1128/AEM.01756-23 | Application-oriented edge; indirect relation to trait | CHEBI:57288 acetyl-CoA; CHEBI:57347 propionyl-CoA; GO:0019377 polyhydroxyalkanoic acid biosynthetic process |
| HOPAC synthetic cycle | uses_enzyme | Chloroflexus aurantiacus malonyl-CoA reductase | “A specific enzyme borrowed from C. aurantiacus is malonyl-CoA reductase (Mcr)” (mclean2023exploringalternativepathways pages 2-3) | 10.1126/sciadv.adh4299, 2023, https://doi.org/10.1126/sciadv.adh4299 | Strong synthetic-biology link; not native trait edge but useful downstream application | EC:1.2.1.75; NCBITaxon:324602 Chloroflexus aurantiacus |
| HOPAC Version 4.0 | converts | ~3.0 mM CO2 to glycolate within 2 h | “Version 4.0 comprises 11 enzymes from six organisms and converts ~3.0 mM CO2 into glycolate within 2 hours” (mclean2023exploringalternativepathways pages 1-2) | 10.1126/sciadv.adh4299, 2023, https://doi.org/10.1126/sciadv.adh4299 | Recent implementation metric showing translational relevance; synthetic system, not native pathway | CHEBI:16526 carbon dioxide; CHEBI:57597 glycolate |


*Table: This table compiles candidate causal edges for curating the 3-hydroxypropionate bicycle, with evidence snippets, DOI-first references, uncertainty notes, and suggested ontology grounding. It highlights core pathway chemistry, ecological context, taxonomic distribution, and recent synthetic-biology applications.*


## 5. Recent developments (prioritizing 2023–2024)

### 5.1 2024: Chloroflexota review framing (ecology + application relevance)
A 2024 review of **Chloroflexota biotechnological potential** reiterates that *Chloroflexus aurantiacus* uses the **3‑HP bi‑cycle** for autotrophic CO2 fixation and can grow **photoautotrophically** using **hydrogen or sulfide as electron donors**; it also links pathway intermediates (acetyl‑CoA, propionyl‑CoA) to **polyhydroxyalkanoate (PHA) accumulation**, supporting a node/edge connecting carbon fixation to biopolymer precursor supply (application context). (freches2024thebiotechnologicalpotential pages 14-15)

### 5.2 2023–2024: Synthetic biology leveraging 3‑HP bicycle chemistry
The **HOPAC** new-to-nature CO2-fixation cycle is explicitly designed to be similar in topology to the 3‑HP bicycle and is compared energetically (one fewer ATP than the natural 3‑HP bicycle, in the authors’ accounting for their designed stoichiometry). (mclean2023exploringalternativepathways pages 2-3)

A key translational point for TraitMech is that components of the natural bicycle are being ported into engineered systems: **malonyl‑CoA reductase from *C. aurantiacus*** is used and kinetically characterized as active at mesophilic temperatures in the in vitro HOPAC system. (mclean2023exploringalternativepathways pages 2-3)

**Performance statistics (recent).** In the optimized HOPAC system (Version 4.0), the authors report converting **~3.0 mM CO2 into glycolate within 2 hours** using 11 enzymes from six organisms. (mclean2023exploringalternativepathways pages 1-2)

These data justify including “synthetic CO2 fixation cycles inspired by 3‑HP bicycle” as a downstream application node, but this is not the native trait itself.


## 6. Current applications and real-world implementations

### 6.1 Bioprocess potential (thermophilic phototroph chassis; bioplastics precursors)
The 2024 Chloroflexota review highlights **thermophilic** and **phototrophic** attributes and suggests their value in sustainable bio-based technologies; it specifically notes that 3‑HP pathway intermediates **acetyl‑CoA and propionyl‑CoA** can feed **PHA accumulation** (a bioplastics-relevant product class). (freches2024thebiotechnologicalpotential pages 14-15)

### 6.2 In vitro CO2 fixation modules (proof-of-principle engineering)
The HOPAC cycle constitutes a **real-world in vitro implementation** of CO2 fixation using enzyme sets partly derived from or analogous to 3‑HP bicycle steps, demonstrating practical reuse of bicycle enzymes in engineered carbon assimilation. (mclean2023exploringalternativepathways pages 1-2, mclean2023exploringalternativepathways pages 2-3)


## 7. Expert synthesis / authoritative interpretations (how experts frame the trait)

- Authoritative pathway reviews emphasize the 3‑HP bicycle as one of the “non‑Calvin” autotrophic strategies with a distinctive two‑cycle layout yielding glyoxylate then pyruvate, and note that it uses multifunctional enzymes (compressed enzyme count). (hugler2011beyondthecalvin pages 9-10)
- Primary biochemical/genomic work in *C. aurantiacus* provides enzyme lists and gene organization that constrain mechanistic graph structure (e.g., which enzymes are core vs accessory; clustering of glyoxylate-assimilation genes). (zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 5-7)
- Recent systems/synthetic biology studies treat the 3‑HP bicycle as an important design inspiration but also highlight practical issues such as thermophilic enzyme provenance and energetic costs that can be optimized by alternative chemistries (e.g., reductive carboxylation in HOPAC). (mclean2023exploringalternativepathways pages 2-3, mclean2023exploringalternativepathways pages 7-10)


## 8. Relevant statistics and quantitative data for curation decisions

### 8.1 Large-scale distribution statistics (genomic potential)
A broad MAG survey analyzed **52,515 MAGs** and reported carbon fixation pathway potential in **1,007 MAGs**, with **23 MAGs** carrying more than one carbon fixation pathway. (garritano2022carbonfixationpathways pages 1-2)

For pathway detection counts (Table 1): the same study reports detection in MAGs of **CBB (616), rTCA1 (207), rTCA2 (10), 3HP bi-cycle (21), HP/HB (135), DC/HB (18)**. (garritano2022carbonfixationpathways pages 2-3)

For the 3‑HP bicycle specifically, the authors state it is **not restricted to Chloroflexota** and note:
- detection of all genes required for the 3HP bi-cycle in **two Gemmatimonadota MAGs**, and some Proteobacteria-family MAGs above completeness thresholds; 
- but also that many Actinobacteriota MAGs had only partial completeness (average **68.6%**), limiting inference of a complete functional bicycle. (garritano2022carbonfixationpathways pages 2-3)

**Curation implication:** these results justify a candidate edge “genomic potential for 3HP bi-cycle outside Chloroflexota” but flagged **uncertain** until experimentally validated.

### 8.2 Synthetic in vitro implementation metrics (applied performance)
HOPAC Version 4.0: **~3.0 mM CO2 → glycolate in 2 hours** (in vitro enzyme system). (mclean2023exploringalternativepathways pages 1-2)


## 9. Warnings / claims not yet ready for TraitMech curation

1) **Do not curate ‘3‑HP bicycle present’ in non-Chloroflexaceae taxa solely from partial gene hits.** Individual key genes occur widely, and MAG-based pathway completeness can be below thresholds; treat as “potential” unless gene completeness plus physiological evidence is available. (hugler2011beyondthecalvin pages 9-10, zarzycki2011coassimilationoforganic pages 5-7, garritano2022carbonfixationpathways pages 2-3)

2) **Avoid over-generalizing electron donors/physiology beyond *C. aurantiacus* without taxon-specific evidence.** The strong evidence for photoautotrophy with H2/sulfide is for *C. aurantiacus* as presented in a Chloroflexota review; other taxa with partial gene sets may have different energetics/ecology. (freches2024thebiotechnologicalpotential pages 14-15)

3) **Keep synthetic biology edges separated from the native trait definition.** HOPAC and engineered modules are best curated as ‘downstream application/use’ rather than defining causal mechanisms of the natural trait. (mclean2023exploringalternativepathways pages 2-3, mclean2023exploringalternativepathways pages 1-2)


## 10. DOI-first bibliography (with URLs and publication dates where available)

1. **Freches A, Fradinho JC.** *The biotechnological potential of the Chloroflexota phylum.* **Applied and Environmental Microbiology**. **2024-06**. DOI: **10.1128/aem.01756-23**. URL: https://doi.org/10.1128/aem.01756-23 (freches2024thebiotechnologicalpotential pages 14-15, freches2024thebiotechnologicalpotential pages 17-18)

2. **McLean R, Schwander T, Diehl C, et al.** *Exploring alternative pathways for the in vitro establishment of the HOPAC cycle for synthetic CO2 fixation.* **Science Advances**. **2023-06**. DOI: **10.1126/sciadv.adh4299**. URL: https://doi.org/10.1126/sciadv.adh4299 (mclean2023exploringalternativepathways pages 2-3, mclean2023exploringalternativepathways pages 1-2, mclean2023exploringalternativepathways pages 6-7, mclean2023exploringalternativepathways pages 7-10)

3. **Kang D-K, Kim S-H, Sohn J-H, Sung BH.** *Insights into Enzyme Reactions with Redox Cofactors in Biological Conversion of CO2.* **Journal of Microbiology and Biotechnology**. **2023-06**. DOI: **10.4014/jmb.2306.06005**. URL: https://doi.org/10.4014/jmb.2306.06005 (kang2023insightsintoenzyme pages 2-4)

4. **Tommasi IC.** *The Biochemistry of Artificial CO2-Fixation Pathways: The Exploitation of Carboxylase Enzymes Alternative to Rubisco.* **Catalysts**. **2024-10**. DOI: **10.3390/catal14100679**. URL: https://doi.org/10.3390/catal14100679 (tommasi2024thebiochemistryof pages 10-12, tommasi2024thebiochemistryof pages 12-14)

5. **Garritano AN, Song W, Thomas T.** *Carbon fixation pathways across the bacterial and archaeal tree of life.* **PNAS Nexus**. **2022-10**. DOI: **10.1093/pnasnexus/pgac226**. URL: https://doi.org/10.1093/pnasnexus/pgac226 (garritano2022carbonfixationpathways pages 1-2, garritano2022carbonfixationpathways pages 2-3, garritano2022carbonfixationpathways pages 9-10)

6. **Zarzycki J, Fuchs G.** *Coassimilation of Organic Substrates via the Autotrophic 3‑Hydroxypropionate Bi‑Cycle in Chloroflexus aurantiacus.* **Applied and Environmental Microbiology**. **2011-09**. DOI: **10.1128/AEM.00705-11**. URL: https://doi.org/10.1128/AEM.00705-11 (zarzycki2011coassimilationoforganic pages 5-7, zarzycki2011coassimilationoforganic pages 1-2, zarzycki2011coassimilationoforganic pages 2-3)

7. **Hügler M, Sievert SM.** *Beyond the Calvin cycle: autotrophic carbon fixation in the ocean.* **Annual Review of Marine Science**. **2011-01**. DOI: **10.1146/annurev-marine-120709-142712**. URL: https://doi.org/10.1146/annurev-marine-120709-142712 (hugler2011beyondthecalvin pages 9-10, hugler2011beyondthecalvin pages 7-9)

8. **McLean R.** *In vitro Realisation of the Hydroxypropionyl-CoA/Acrylyl-CoA Cycle.* **2022-01**. DOI: **10.17192/z2022.0467**. URL: https://doi.org/10.17192/z2022.0467 (mclean2022invitrorealisation pages 22-29, mclean2022invitrorealisation pages 29-35, mclean2022invitrorealisation pages 88-91)

9. **Grundling I.** *Propionyl‑CoA synthase: Characterization, engineering and physiological role of a trifunctional fusion enzyme.* **2020-04**. DOI: **10.17192/z2020.0502**. URL: https://doi.org/10.17192/z2020.0502 (grundling2020propionylcoasynthasecharacterization pages 21-24)


References

1. (hugler2011beyondthecalvin pages 9-10): Michael Hügler and Stefan M. Sievert. Beyond the calvin cycle: autotrophic carbon fixation in the ocean. Annual review of marine science, 3:261-89, Jan 2011. URL: https://doi.org/10.1146/annurev-marine-120709-142712, doi:10.1146/annurev-marine-120709-142712. This article has 796 citations and is from a highest quality peer-reviewed journal.

2. (hugler2011beyondthecalvin pages 7-9): Michael Hügler and Stefan M. Sievert. Beyond the calvin cycle: autotrophic carbon fixation in the ocean. Annual review of marine science, 3:261-89, Jan 2011. URL: https://doi.org/10.1146/annurev-marine-120709-142712, doi:10.1146/annurev-marine-120709-142712. This article has 796 citations and is from a highest quality peer-reviewed journal.

3. (zarzycki2011coassimilationoforganic pages 5-7): Jan Zarzycki and Georg Fuchs. Coassimilation of organic substrates via the autotrophic 3-hydroxypropionate bi-cycle in chloroflexus aurantiacus. Applied and Environmental Microbiology, 77:6181-6188, Sep 2011. URL: https://doi.org/10.1128/aem.00705-11, doi:10.1128/aem.00705-11. This article has 95 citations and is from a peer-reviewed journal.

4. (mclean2022invitrorealisation pages 22-29): Richard McLean. In vitro realisation of the hydroxypropionyl-coa/acrylyl-coa cycle. Text, Jan 2022. URL: https://doi.org/10.17192/z2022.0467, doi:10.17192/z2022.0467. This article has 1 citations and is from a peer-reviewed journal.

5. (zarzycki2011coassimilationoforganic pages 1-2): Jan Zarzycki and Georg Fuchs. Coassimilation of organic substrates via the autotrophic 3-hydroxypropionate bi-cycle in chloroflexus aurantiacus. Applied and Environmental Microbiology, 77:6181-6188, Sep 2011. URL: https://doi.org/10.1128/aem.00705-11, doi:10.1128/aem.00705-11. This article has 95 citations and is from a peer-reviewed journal.

6. (kang2023insightsintoenzyme pages 2-4): Du-Kyeong Kang, Seung-Hwa Kim, Jung-Hoon Sohn, and Bong Hyun Sung. Insights into enzyme reactions with redox cofactors in biological conversion of co2. Journal of Microbiology and Biotechnology, 33:1403-1411, Jun 2023. URL: https://doi.org/10.4014/jmb.2306.06005, doi:10.4014/jmb.2306.06005. This article has 10 citations and is from a peer-reviewed journal.

7. (freches2024thebiotechnologicalpotential pages 14-15): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 113 citations and is from a peer-reviewed journal.

8. (grundling2020propionylcoasynthasecharacterization pages 21-24): Iria Grundling. Propionyl-coa synthase: characterization, engineering and physiological role of a trifunctional fusion enzyme. ArXiv, Apr 2020. URL: https://doi.org/10.17192/z2020.0502, doi:10.17192/z2020.0502. This article has 0 citations.

9. (zarzycki2011coassimilationoforganic pages 2-3): Jan Zarzycki and Georg Fuchs. Coassimilation of organic substrates via the autotrophic 3-hydroxypropionate bi-cycle in chloroflexus aurantiacus. Applied and Environmental Microbiology, 77:6181-6188, Sep 2011. URL: https://doi.org/10.1128/aem.00705-11, doi:10.1128/aem.00705-11. This article has 95 citations and is from a peer-reviewed journal.

10. (garritano2022carbonfixationpathways pages 2-3): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

11. (mclean2023exploringalternativepathways pages 1-2): Richard McLean, Thomas Schwander, Christoph Diehl, Niña Socorro Cortina, Nicole Paczia, Jan Zarzycki, and Tobias J. Erb. Exploring alternative pathways for the in vitro establishment of the hopac cycle for synthetic co <sub>2</sub> fixation. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adh4299, doi:10.1126/sciadv.adh4299. This article has 59 citations and is from a highest quality peer-reviewed journal.

12. (mclean2023exploringalternativepathways pages 7-10): Richard McLean, Thomas Schwander, Christoph Diehl, Niña Socorro Cortina, Nicole Paczia, Jan Zarzycki, and Tobias J. Erb. Exploring alternative pathways for the in vitro establishment of the hopac cycle for synthetic co <sub>2</sub> fixation. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adh4299, doi:10.1126/sciadv.adh4299. This article has 59 citations and is from a highest quality peer-reviewed journal.

13. (mclean2023exploringalternativepathways pages 2-3): Richard McLean, Thomas Schwander, Christoph Diehl, Niña Socorro Cortina, Nicole Paczia, Jan Zarzycki, and Tobias J. Erb. Exploring alternative pathways for the in vitro establishment of the hopac cycle for synthetic co <sub>2</sub> fixation. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adh4299, doi:10.1126/sciadv.adh4299. This article has 59 citations and is from a highest quality peer-reviewed journal.

14. (mclean2022invitrorealisation pages 29-35): Richard McLean. In vitro realisation of the hydroxypropionyl-coa/acrylyl-coa cycle. Text, Jan 2022. URL: https://doi.org/10.17192/z2022.0467, doi:10.17192/z2022.0467. This article has 1 citations and is from a peer-reviewed journal.

15. (tommasi2024thebiochemistryof pages 12-14): Immacolata C. Tommasi. The biochemistry of artificial co2-fixation pathways: the exploitation of carboxylase enzymes alternative to rubisco. Catalysts, 14:679, Oct 2024. URL: https://doi.org/10.3390/catal14100679, doi:10.3390/catal14100679. This article has 8 citations.

16. (wang2023microbialconversionand pages 3-5): Ge-Ge Wang, Zhang Yuan, Xiao-Yan Wang, and Gen-Lin Zhang. Microbial conversion and utilization of co2. Annals of Civil and Environmental Engineering, 7:045-060, Sep 2023. URL: https://doi.org/10.29328/journal.acee.1001055, doi:10.29328/journal.acee.1001055. This article has 3 citations.

17. (freches2024thebiotechnologicalpotential pages 17-18): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 113 citations and is from a peer-reviewed journal.

18. (garritano2022carbonfixationpathways pages 1-2): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

19. (mclean2023exploringalternativepathways pages 6-7): Richard McLean, Thomas Schwander, Christoph Diehl, Niña Socorro Cortina, Nicole Paczia, Jan Zarzycki, and Tobias J. Erb. Exploring alternative pathways for the in vitro establishment of the hopac cycle for synthetic co <sub>2</sub> fixation. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adh4299, doi:10.1126/sciadv.adh4299. This article has 59 citations and is from a highest quality peer-reviewed journal.

20. (tommasi2024thebiochemistryof pages 10-12): Immacolata C. Tommasi. The biochemistry of artificial co2-fixation pathways: the exploitation of carboxylase enzymes alternative to rubisco. Catalysts, 14:679, Oct 2024. URL: https://doi.org/10.3390/catal14100679, doi:10.3390/catal14100679. This article has 8 citations.

21. (garritano2022carbonfixationpathways pages 9-10): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 122 citations and is from a peer-reviewed journal.

22. (mclean2022invitrorealisation pages 88-91): Richard McLean. In vitro realisation of the hydroxypropionyl-coa/acrylyl-coa cycle. Text, Jan 2022. URL: https://doi.org/10.17192/z2022.0467, doi:10.17192/z2022.0467. This article has 1 citations and is from a peer-reviewed journal.