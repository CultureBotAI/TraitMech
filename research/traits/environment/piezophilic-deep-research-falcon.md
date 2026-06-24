---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:53:44.339397'
end_time: '2026-06-18T01:03:40.606156'
duration_seconds: 596.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: piezophilic
  trait_identifier: traitmech:000001
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: piezophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental growth preference in which an organism grows optimally
    at hydrostatic pressures substantially above atmospheric pressure (0.1 MPa), characteristic
    of deep-sea and deep-subsurface microorganisms.
  parent_traits: METPO:1000059
  synonyms: barophilic, piezophile
  evidence_summary: 'DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP
    are usually known as piezophiles, referring to their preference for high pressure
    (Membrane-lipid adaptation review supports the definition of piezophiles as high-hydrostatic-pressure-adapted
    organisms, with adaptation involving unsaturated and branched-chain fatty acids.)
    | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at
    6 degrees C (Organism example: Colwellia marinimaniae strain MTCD1, the most piezophilic
    organism described, grows optimally at 120 MPa.)'
  causal_graph_summary: 'piezophilic_hhp_membrane_adaptation: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezophilic
- **METPO identifier:** traitmech:000001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows optimally at hydrostatic pressures substantially above atmospheric pressure (0.1 MPa), characteristic of deep-sea and deep-subsurface microorganisms.
- **Parent traits:** METPO:1000059
- **Synonyms:** barophilic, piezophile
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Membrane-lipid adaptation review supports the definition of piezophiles as high-hydrostatic-pressure-adapted organisms, with adaptation involving unsaturated and branched-chain fatty acids.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae strain MTCD1, the most piezophilic organism described, grows optimally at 120 MPa.)
- **Existing causal graph summary:** piezophilic_hhp_membrane_adaptation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezophilic.yaml`.

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
- **Trait label:** piezophilic
- **METPO identifier:** traitmech:000001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows optimally at hydrostatic pressures substantially above atmospheric pressure (0.1 MPa), characteristic of deep-sea and deep-subsurface microorganisms.
- **Parent traits:** METPO:1000059
- **Synonyms:** barophilic, piezophile
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Membrane-lipid adaptation review supports the definition of piezophiles as high-hydrostatic-pressure-adapted organisms, with adaptation involving unsaturated and branched-chain fatty acids.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae strain MTCD1, the most piezophilic organism described, grows optimally at 120 MPa.)
- **Existing causal graph summary:** piezophilic_hhp_membrane_adaptation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezophilic.yaml`.

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


# Microbial TraitMech Curation Report: **piezophilic** (barophilic/piezophile)

**Target trait:** piezophilic (METPO identifier: traitmech:000001; category: ENVIRONMENT; kind: CLASS)

## 1) Scope summary (trait meaning, boundaries, and measurement)

### Definition and operationalization
Piezophilic microorganisms are defined by an **optimal growth at pressures above atmospheric pressure (~0.1 MPa)**. (malas2024biologicalfunctionsat pages 1-2)

A curation-useful operational categorization in recent literature separates:
- **Non-piezophiles:** optimal growth at 0.1 MPa and **cannot** grow at higher pressures.
- **Piezosensitive:** optimal growth at 0.1 MPa but **can** still grow at higher pressures.
- **Piezophiles:** **optimal growth at high pressures**. (scheffer2023themysteryof pages 1-2)

Tamby et al. further distinguishes **piezotolerant** organisms (with similar/faster growth at atmospheric pressure but able to withstand high hydrostatic pressure) from **obligate piezophiles** (grow only under HHP). (tamby2023microbialmembranelipid pages 1-2)

### Environmental and assay context
Hydrostatic pressure in the ocean increases **~1 MPa per 100 m depth**; the deep sea is often operationally described as depths >1,000 m (pressure >10 MPa), with near-freezing average temperatures (~2°C). (tamby2023microbialmembranelipid pages 1-2, qiu2024metabolicadaptationsof pages 1-2)

Recent work emphasizes that on Earth, the highest explored deep-sea habitat pressures are **~110 MPa (Challenger Deep)**, while the **current demonstrated growth limit** is **140 MPa**; modeled extraterrestrial oceans (e.g., Titan) may exceed these (≥150 MPa). (malas2024biologicalfunctionsat pages 1-2)

**Boundary cases to curate carefully:**
- **Polyextremophily and confounding:** HHP commonly co-occurs with **low temperature** and sometimes salinity extremes; lipid and gene-expression changes can be pressure-, temperature-, nutrient-, or salinity-driven, so single-factor attribution can be weak without controls. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 15-16)
- **Piezotolerance vs piezophily:** e.g., Shewanella eurypsychrophilus YLB-09 is described as pressure-tolerant with **optimum at 0.1 MPa** but growth to ~50 MPa (experiments at 23 MPa). (qiu2024metabolicadaptationsof pages 1-2)

### Quantitative pressure optima examples (from a recent lipid-focused review)
Tamby et al. summarizes strain-level optima such as **Psychromonas JCM 11054 (10°C; 50 MPa)**, **Thermococcus MP (85°C; 40 MPa)**, and **Methanococcus jannaschii (85°C; 25 MPa)**, along with associated lipid compositional changes. (tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid media 2a9c4503, tamby2023microbialmembranelipid media aeae671d, tamby2023microbialmembranelipid media a29f80e0)

## 2) Key concepts & current mechanistic understanding (candidate nodes)

### A. Environmental / experimental factor nodes
- **High hydrostatic pressure** (HHP; label-only) (tamby2023microbialmembranelipid pages 1-2)
- Co-stressors (often confounded): **low temperature** (psychrophily), salinity; plus nutrient/carbon source effects (e.g., glucose dependence of some solute responses). (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10)
- Pressure ranges and constraints: deep sea pressures >10 MPa, Earth maxima ~110 MPa, growth limit 140 MPa. (malas2024biologicalfunctionsat pages 1-2)

**Ontology grounding suggestions:**
- ENVO (environmental pressure terms): label-only recommended unless a specific ENVO term is selected during curation.

### B. Cellular structures / processes
- **Membrane homeoviscous/homeophasic adaptation** (GO process candidate; label-only) regulating fluidity/phase via lipid packing changes. (tamby2023microbialmembranelipid pages 2-4)
- **Protein folding/stability stress response** (GO:0006457 “protein folding” candidate), including heat-shock and cold-shock proteins. (scheffer2023themysteryof pages 1-2, malas2024biologicalfunctionsat pages 1-2)
- **DNA repair / genome maintenance** (GO:0006281 “DNA repair” candidate). (malas2024biologicalfunctionsat pages 6-9)

### C. Genes/proteins/complexes (examples reported in 2023–2024 literature)
Membrane/envelope:
- **OmpH** outer-membrane porin; **toxR** regulon as regulator. (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7)
- Porins (generic). (tamby2023microbialmembranelipid pages 2-4)

Motility/chemotaxis:
- **MCP** (methyl-accepting chemotaxis proteins), **CheACD/CheY** cascade; flagellar gene clusters; archaellum-associated components (archaea). (scheffer2023themysteryof pages 6-7)

Energy metabolism and respiration:
- Pressure-dependent shifts among **cytochrome c oxidase**, **cytochrome c-551**, and **terminal quinol oxidase** in Shewanella spp. (scheffer2023themysteryof pages 7-9)

Stress response and transcriptomic regulators:
- **CspG** cold-shock protein (in S. oneidensis MR-1 at 158 MPa). (malas2024biologicalfunctionsat pages 1-2)
- Ion transporters (e.g., **nhaA**, **kefC**, **ktrA/ktrB**), metal export (**cusA**) upregulated under HHP stress. (malas2024biologicalfunctionsat pages 6-9)
- DNA repair factors (**recN**, **topB**, **dinB**, **dinG**). (malas2024biologicalfunctionsat pages 6-9)

Lipid biosynthesis:
- **pfa operon** (ω-3 polyunsaturated fatty acid synthase). (scheffer2023themysteryof pages 6-7)
- Fatty-acid synthesis genes impacted in HHP stress transcription (e.g., **fabH2**, **fabF**, **fabG**, **lpxM2**, **fadL**). (malas2024biologicalfunctionsat pages 6-9)

**Grounding suggestions:**
- Gene/protein identifiers are organism-specific; curate as label-only nodes unless mapping to UniProt/EC/GO is performed per taxon.

### D. Chemicals / metabolites / solutes (CHEBI-groundable)
- **Trimethylamine N-oxide (TMAO)** (CHEBI:15891). (qiu2024metabolicadaptationsof pages 1-2, scheffer2023themysteryof pages 9-10)
- **Glutamate** (CHEBI:29985). (scheffer2023themysteryof pages 9-10)
- **Betaine** (CHEBI:17750). (scheffer2023themysteryof pages 9-10)
- **β-hydroxybutyrate** (CHEBI:15973). (scheffer2023themysteryof pages 9-10)

Membrane lipid features (some not cleanly CHEBI-grounded at “feature” level):
- **Branched-chain fatty acids**, **unsaturated fatty acids**, **ω-3 PUFAs** including **C20:5 (EPA)** and **C22:6 (DHA)**. (tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid pages 2-4)

## 3) Evidence-backed candidate causal edges (triples) for TraitMech

The table below lists candidate edges that are (i) mechanistically meaningful for piezophily/HHP adaptation and (ii) supported by direct recent evidence and quotable snippets.

| Subject node (label + grounding CURIE if known) | Predicate | Object node (label + grounding) | Evidence snippet | Reference (DOI + publication year + URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| high hydrostatic pressure (HHP) [label-only] | increases | unsaturated fatty acids [CHEBI candidate], branched-chain fatty acids [label-only] | “The abundance of specific membrane lipids, such as those containing unsaturated and branched-chain fatty acids, rises with increasing HHP.” (tamby2023microbialmembranelipid pages 1-2) | 10.3389/fmolb.2022.1058381 (2023) https://doi.org/10.3389/fmolb.2022.1058381 | Broad review support; exact lipid classes and direction can vary by taxon and co-vary with temperature. |
| pfa operon [label-only] | enables | ω-3 polyunsaturated fatty acid production [label-only] | “The pfa operon encodes an ω-3 polyunsaturated fatty acid synthase” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Strong gene-to-function edge; role in piezophily is supportive but not universal across all taxa. |
| toxR regulon [label-only] | upregulates | ompH / OmpH porin [label-only] | “ompH regulated by the toxR regulon” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Taxon-specific regulatory evidence from pressure-adapted bacteria; grounding uncertain. |
| increased pressure [label-only] | increases | OmpH abundance [label-only] | “OmpH abundance increases ~10–100× between 0.1 and 28 MPa” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Quantitative edge; likely species-specific and linked to porin-mediated transport under pressure. |
| high hydrostatic pressure (HHP) [label-only] | switches_to | high-pressure respiratory chain featuring cytochrome c-551 and terminal quinol oxidase [label-only] | “Shewanella spp. switch from NADH dehydrogenase + bc1 + cytochrome c oxidase at low pressure to cytochrome c-551 and a terminal quinol oxidase at high pressure (quinol oxidase expressed only at high pressure)” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Strong mechanistic summary, but explicitly taxon-specific (Shewanella spp.). |
| high hydrostatic pressure (HHP) [label-only] | increases | TMAO reductase activity / TMAO respiration [CHEBI:15891 for TMAO] | “increased TMAO reductase activity support[s] growth at high pressure” (scheffer2023themysteryof pages 7-9); “switching from aerobic intracellular energy metabolism to trimethylamine N-oxide respiration” (qiu2024metabolicadaptationsof pages 1-2) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629; 10.3389/fmicb.2024.1467153 (2024) https://doi.org/10.3389/fmicb.2024.1467153 | Supported by review and primary study; likely lineage- and condition-dependent. |
| high hydrostatic pressure (HHP) [label-only] | accumulates | piezolytes: glutamate [CHEBI:29985], betaine [CHEBI:17750], β-hydroxybutyrate [CHEBI:15973], TMAO [CHEBI:15891] | “Compatible solutes (termed ‘piezolytes’) detected include glutamate, betaine, and β-hydroxybutyrate”; “TMAO is highlighted as both an energetic substrate and a pressure-tolerance molecule” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Useful mechanistic node set; some examples depend on glucose availability or lack direct genetic linkage. |
| high hydrostatic pressure (158 MPa) [label-only] | upregulates | argA, argB, argC, argF (arginine biosynthesis genes) [label-only] | “Adaptations include upregulation of the genes argA, argB, argC, and argF involved in arginine biosynthesis” (malas2024biologicalfunctionsat pages 1-2) | 10.3389/fmicb.2024.1293928 (2024) https://doi.org/10.3389/fmicb.2024.1293928 | Primary transcriptomic evidence from Shewanella oneidensis MR-1; response in a non-piezophile under extreme HHP, so curate as HHP-response, not universal piezophile mechanism. |
| high hydrostatic pressure (158 MPa) [label-only] | upregulates | cspG cold-shock protein [label-only] and antioxidant defense genes [label-only] | “stress-response factors such as cold-shock protein CspG and antioxidant-defense genes” (malas2024biologicalfunctionsat pages 1-2) | 10.3389/fmicb.2024.1293928 (2024) https://doi.org/10.3389/fmicb.2024.1293928 | Strong HHP-response evidence; may reflect general stress adaptation rather than piezophile-specific mechanism. |
| high hydrostatic pressure (158 MPa) [label-only] | alters_expression_of | fatty acid synthesis / membrane lipid genes: fabH2, fabF_2, fabG_3, acpP_3, acpS, dgkA, lpxM2, fadL [label-only] | “Membrane lipid metabolism shows modulation… authors infer a shift favoring branched-chain fatty acid synthesis (fabH2) over straight chains” (malas2024biologicalfunctionsat pages 6-9) | 10.3389/fmicb.2024.1293928 (2024) https://doi.org/10.3389/fmicb.2024.1293928 | Inferred pathway-level edge from transcriptomics; exact biochemical output should be curated cautiously. |
| high hydrostatic pressure (158 MPa) [label-only] | induces | DNA repair / genome maintenance genes: recN, topB, dinB, dinG_1 [label-only] | “DNA repair/replication factors (recN, topB, dinB, dinG_1) are highly induced” (malas2024biologicalfunctionsat pages 6-9) | 10.3389/fmicb.2024.1293928 (2024) https://doi.org/10.3389/fmicb.2024.1293928 | Good primary evidence for HHP stress response; not specific enough alone to define piezophily. |
| high hydrostatic pressure (HHP) [label-only] | increases | polyunsaturated fatty acids C20:5 and C22:6 [label-only] | “HHP-driven increases in C20:5/C22:6 in Photobacterium profundum SS9, Psychromonas strains, and Shewanella piezotolerans WP3” (tamby2023microbialmembranelipid pages 2-4) | 10.3389/fmolb.2022.1058381 (2023) https://doi.org/10.3389/fmolb.2022.1058381 | Specific lipid species strengthen membrane-adaptation branch; response is not universal (counterexamples noted in same review). |
| OmpH porin [label-only] | enables | transport of amino acids and sugars under pressure [label-only] | “high-pressure–resistant porins maintain uptake of amino acids and sugars” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629 (2023) https://doi.org/10.3390/microorganisms11071629 | Functional interpretation from review; mechanism plausible but partly inferred rather than directly assayed in all taxa. |


*Table: This table lists candidate mechanistic causal edges for the piezophilic trait, linking high hydrostatic pressure to membrane, respiratory, osmolyte, stress-response, and gene-regulatory adaptations. It is formatted for curation use and highlights taxon specificity and uncertainty where appropriate.*

## 4) Recent developments (2023–2024) and latest research themes

### 4.1 Membrane lipid remodeling remains a central, but non-universal, mechanism
A 2023 Frontiers review emphasizes that many piezophiles increase **unsaturated and branched-chain fatty acids** with increasing HHP to maintain membrane integrity, but also that this strategy is **not universal**, motivating further mechanistic work and better separation of pressure from temperature effects. (tamby2023microbialmembranelipid pages 1-2)

Tamby et al. additionally compile multiple taxa in a single table linking **optimal growth pressures/temperatures** to **lipid composition shifts** (e.g., PUFA increases such as C20:5/C22:6), with a conceptual figure illustrating how increased unsaturation impacts membrane packing/fluidity. (tamby2023microbialmembranelipid media 2a9c4503, tamby2023microbialmembranelipid media 458754cd)

### 4.2 Respiratory rewiring and osmolyte/piezolyte usage connect pressure to energetics
Scheffer & Gieg (2023) synthesize evidence that pressure can remodel respiratory chains (e.g., Shewanella spp. shifting terminal oxidases and expressing a terminal quinol oxidase only at high pressure) and that TMAO/DMSO-linked pathways may support high-pressure growth in some lineages. (scheffer2023themysteryof pages 7-9)

A 2024 metabolomics/transcriptomics study on **Shewanella eurypsychrophilus** reports that elevated pressure can drive a switch “from aerobic intracellular energy metabolism to **TMAO respiration**” and is associated with glycerolipid and amino-acid metabolic remodeling, illustrating a concrete metabolic implementation of the review-level hypothesis. (qiu2024metabolicadaptationsof pages 1-2)

### 4.3 High-pressure stress responses: transcriptome-scale insights under extreme HHP
Malas et al. (2024) show that even a non-piezophile (S. oneidensis MR-1) remains metabolically active during exposure to **158 MPa** and regulates **264 genes** in response, including arginine biosynthesis genes and membrane reconfiguration processes, plus stress and antioxidant responses. (malas2024biologicalfunctionsat pages 1-2)

These findings are useful as *HHP-response nodes/edges* but require caution if curating as *piezophile-specific mechanisms*, because the system is not an obligate piezophile and the exposure is beyond most Earth ocean pressures. (malas2024biologicalfunctionsat pages 1-2)

## 5) Current applications and real-world implementations

### 5.1 Deep biosphere sampling/cultivation and bias reduction (technology implementation)
Recent reviews emphasize that discovering and studying piezophiles is constrained by the need to **maintain in situ pressure** during sampling, transfer, cultivation, and isolation; decompression can bias community composition and isolate physiology, motivating specialized pressure-retaining devices and shared high-pressure facilities. (scheffer2023themysteryof pages 15-16)

### 5.2 Bioprospecting for pressure-active enzymes and stress-tolerant biocatalysts
Work on deep-sea Shewanella highlights that understanding pressure-driven metabolic regulation could provide a foundation for “industrial development of extreme enzymes.” (qiu2024metabolicadaptationsof pages 1-2)

### 5.3 Astrobiology and planetary analog experiments
The Titan-relevant pressure transcriptomics study explicitly frames HHP as an analog for icy moon oceans and suggests that microorganisms may use adaptations “akin to those demonstrated by terrestrial organisms,” supporting cross-domain interest in piezophily mechanisms. (malas2024biologicalfunctionsat pages 1-2)

## 6) Relevant statistics and quantitative data (recently summarized)

- **Ocean coverage at high pressure:** “areas >35 MPa encompass >70% of the ocean.” (qiu2024metabolicadaptationsof pages 1-2)
- **Pressure gradient:** ~**1 MPa per 100 m** depth. (qiu2024metabolicadaptationsof pages 1-2)
- **Earth pressure maxima and growth limits:** ~**110 MPa** at Challenger Deep; **140 MPa** growth limit. (malas2024biologicalfunctionsat pages 1-2)
- **Porin response magnitude:** OmpH increases **~10–100×** from 0.1 to 28 MPa in a cited model. (scheffer2023themysteryof pages 7-9)
- **Transcriptome response scale:** **264 genes** regulated in S. oneidensis MR-1 at 158 MPa. (malas2024biologicalfunctionsat pages 1-2)
- **Lipid storage change example:** unsaturated wax esters rising from **~3% to ~46%** under pressure (example summarized in Scheffer & Gieg). (scheffer2023themysteryof pages 9-10)

## 7) Expert opinion / authoritative synthesis (what is “safe” to curate)

Authoritative 2023 reviews converge that a **membrane-centric view**—homeoviscous adaptation via lipid remodeling (unsaturation/branching, sometimes PUFAs; headgroup changes; sterol/hopanoid modulation)—is a core mechanistic axis for piezophiles, but that **taxon-to-taxon variability** and **pressure–temperature confounding** remain major interpretive issues. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10)

Scheffer & Gieg also highlight that the field is limited by expensive sampling and specialized instrumentation, which plausibly explains why “most known piezophilic organisms have been discovered within the last 40 years.” (scheffer2023themysteryof pages 1-2)

## 8) Warnings / non-curatable (or curate as uncertain)

1. **Pressure-only vs polyextreme causation:** Many lipid and transcriptomic responses are not uniquely attributable to pressure because deep-sea conditions also include low temperature and often varying salinity/nutrients. Curate edges as **pressure-associated** unless experimental controls isolate pressure. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10)
2. **Taxon specificity:** Respiratory rewiring (e.g., cytochrome oxidase ↔ quinol oxidase) and porin regulation (toxR→ompH) are well-motivated but may be **lineage-specific** (e.g., Shewanella/Photobacterium). (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7)
3. **Extreme HHP exposures:** Transcriptomics at 158 MPa is valuable for “HHP stress response” graphs but may not represent canonical deep-sea piezophily. Mark these edges as **HHP stress response** rather than piezophile-defining unless corroborated in obligate piezophiles. (malas2024biologicalfunctionsat pages 1-2)

---

# DOI-first bibliography (prioritizing 2023–2024)

1. **Tamby A, Sinninghe Damsté JS, Villanueva L.** *Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.* **Frontiers in Molecular Biosciences**. Publication date: **2023-01**. DOI: **10.3389/fmolb.2022.1058381**. URL: https://doi.org/10.3389/fmolb.2022.1058381 (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid media 2a9c4503, tamby2023microbialmembranelipid media 458754cd)

2. **Scheffer G, Gieg LM.** *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface.* **Microorganisms**. Publication date: **2023-06**. DOI: **10.3390/microorganisms11071629**. URL: https://doi.org/10.3390/microorganisms11071629 (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 10-12)

3. **Malas J, Russo DC, Bollengier O, et al.** *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.* **Frontiers in Microbiology**. Publication date: **2024-02**. DOI: **10.3389/fmicb.2024.1293928**. URL: https://doi.org/10.3389/fmicb.2024.1293928 (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 6-9)

4. **Qiu X, Tang X.** *Metabolic adaptations of Shewanella eurypsychrophilus YLB-09 for survival in the high-pressure environment of the deep sea.* **Frontiers in Microbiology**. Publication date: **2024-10**. DOI: **10.3389/fmicb.2024.1467153**. URL: https://doi.org/10.3389/fmicb.2024.1467153 (qiu2024metabolicadaptationsof pages 1-2)

---

## Notes for `piezophilic.yaml` curation
- Candidate node grounding is strongest for **compatible solutes** (CHEBI IDs) and **general processes** (GO), while gene/protein nodes typically require taxon-specific mapping (UniProt/NCBI Gene) during implementation.
- The edge set in Artifact-00 is intended as a starting point for a TraitMech causal graph; several edges are explicitly flagged as **taxon-specific or inferred**, and should be reviewed against primary studies if curated as “core” rather than “example” edges.


References

1. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

2. (scheffer2023themysteryof pages 1-2): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

3. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

4. (qiu2024metabolicadaptationsof pages 1-2): Xu Qiu and Xixiang Tang. Metabolic adaptations of shewanella eurypsychrophilus ylb-09 for survival in the high-pressure environment of the deep sea. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1467153, doi:10.3389/fmicb.2024.1467153. This article has 1 citations and is from a peer-reviewed journal.

5. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

6. (scheffer2023themysteryof pages 15-16): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

7. (tamby2023microbialmembranelipid pages 6-7): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

8. (tamby2023microbialmembranelipid media 2a9c4503): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

9. (tamby2023microbialmembranelipid media aeae671d): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

10. (tamby2023microbialmembranelipid media a29f80e0): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

11. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

12. (malas2024biologicalfunctionsat pages 6-9): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

13. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

14. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

15. (tamby2023microbialmembranelipid media 458754cd): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

16. (scheffer2023themysteryof pages 10-12): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.