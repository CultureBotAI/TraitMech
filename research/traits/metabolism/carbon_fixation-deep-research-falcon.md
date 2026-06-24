---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:16:32.415120'
end_time: '2026-06-18T04:36:47.992668'
duration_seconds: 1215.58
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: carbon fixation
  trait_identifier: traitmech:000019
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: carbon_fixation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolic process in which an organism assimilates inorganic carbon
    (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural
    autotrophic carbon-fixation pathways are currently recognized.
  parent_traits: METPO:1000060
  synonyms: CO2 fixation, autotrophic carbon assimilation
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of\
    \ autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham\
    \ cycle, five further autotrophic carbon-fixation pathways are known, parent of\
    \ the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert, \"Beyond the Calvin cycle\", supports multiple autotrophic\
    \ carbon-fixation pathways operating among ocean microorganisms.)"
  causal_graph_summary: 'carbon_fixation_co2_assimilation: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carbon fixation
- **METPO identifier:** traitmech:000019
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolic process in which an organism assimilates inorganic carbon (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural autotrophic carbon-fixation pathways are currently recognized.
- **Parent traits:** METPO:1000060
- **Synonyms:** CO2 fixation, autotrophic carbon assimilation
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham cycle, five further autotrophic carbon-fixation pathways are known, parent of the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert, "Beyond the Calvin cycle", supports multiple autotrophic carbon-fixation pathways operating among ocean microorganisms.)
- **Existing causal graph summary:** carbon_fixation_co2_assimilation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **carbon fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/carbon_fixation.yaml`.

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
- **Trait label:** carbon fixation
- **METPO identifier:** traitmech:000019
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolic process in which an organism assimilates inorganic carbon (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural autotrophic carbon-fixation pathways are currently recognized.
- **Parent traits:** METPO:1000060
- **Synonyms:** CO2 fixation, autotrophic carbon assimilation
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham cycle, five further autotrophic carbon-fixation pathways are known, parent of the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert, "Beyond the Calvin cycle", supports multiple autotrophic carbon-fixation pathways operating among ocean microorganisms.)
- **Existing causal graph summary:** carbon_fixation_co2_assimilation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **carbon fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/carbon_fixation.yaml`.

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


# Microbial TraitMech Curation Report: Carbon Fixation (traitmech:000019)

**Target trait:** carbon fixation (CO2 fixation; autotrophic carbon assimilation)  
**METPO identifier:** traitmech:000019 (category: METABOLISM; term kind: CLASS; mapping status: REVIEWED)  

## 1) Scope summary (Trait scope and boundary cases)

**Trait meaning (curation scope).** Microbial carbon fixation is the **physiological capacity for net assimilation of dissolved inorganic carbon (DIC; CO2/HCO3−/CO3=) into organic compounds** via recognized autotrophic carbon-fixation pathways (autotrophy), rather than only single-step carboxylations. Scott et al. define DIC as “CO2 + HCO3− + CO3=” and note that fixation of DIC occurs via “autotrophic and anaplerotic pathways” (scott2024widespreaddissolvedinorganic pages 1-2). For TraitMech, the intended phenotype is **organism-level autotrophic carbon assimilation**, not merely presence of one carboxylase.

**Near traits / boundary cases.**
- **Anaplerotic carboxylation ≠ autotrophy.** Enzymes such as phosphoenolpyruvate carboxylase and pyruvate carboxylase use HCO3− (Table 1 in Scott et al.) but often function in **anaplerosis** rather than full autotrophic carbon fixation (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic media b4dc8e23). Curate cautiously unless embedded in a full pathway.
- **Mixotrophy.** Many microbes (and symbionts) can co-utilize inorganic and organic carbon. For example, Riftia symbionts express both CBB and rTCA pathways and appear to modulate them with environmental conditions, which is consistent with mixed trophic strategies (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4).
- **Gene presence may not imply net CO2 fixation.** In deep aquifers, Atencio et al. caution that organisms encoding the Wood–Ljungdahl pathway “may use it for energy conservation rather than net CO2 fixation” (atencio2024metabolicadaptationsunderpin pages 8-9). Curate pathway presence separately from demonstrated net fixation.
- **C1 assimilation of reduced substrates** (e.g., formate, methanol) is adjacent but not identical: Chemical Reviews highlights “reduced CO2 derivates, such as formate or methanol” as alternatives to direct CO2 use (bierbaumer2023enzymaticconversionof pages 1-2). These can support carbon incorporation but may not represent canonical inorganic-carbon autotrophy unless coupled to net autotrophic growth.

## 2) Key concepts and definitions (current understanding)

### 2.1 Dissolved inorganic carbon (DIC) chemistry as a primary constraint
Carbon fixation is constrained by **DIC speciation, transport, and interconversion kinetics**:
- **pH governs DIC speciation**: “CO2 dominates at low pH, HCO3− at circumneutral pH, and CO3= at alkaline pH” (scott2024widespreaddissolvedinorganic pages 1-2). Scott et al. further quantify that at pH <4.3 nearly all DIC is CO2, while at >8.3 CO2 is <1% of DIC (scott2024widespreaddissolvedinorganic pages 10-13).
- **CO2 vs HCO3− permeability:** “CO2 diffuses through cell membranes more rapidly than HCO3−” (scott2024widespreaddissolvedinorganic pages 1-2).
- **Uncatalyzed CO2↔HCO3− interconversion is slow** relative to metabolic demand; thus microbes use **carbonic anhydrase (CA; EC 4.2.1.1)** and transporters (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 2-4).

Scott et al. provide a visual summary of DIC toolkits (transporters and CA) and enzyme substrate specificities (Table 1) that is directly relevant for curating supply-to-demand causal edges (scott2024widespreaddissolvedinorganic media d68b56dc, scott2024widespreaddissolvedinorganic media b4dc8e23).

### 2.2 “DIC toolkit” and CO2 concentrating mechanisms (CCMs)
**Carbonic anhydrase** catalyzes CO2 hydration/dehydration and “speeds the interconversion of CO2 and HCO3−” (scott2024widespreaddissolvedinorganic pages 2-4). **Transporters** include HCO3− systems (SbtA, BicA/SulP, CmpABCD) and CO2-active systems such as the DIC-accumulating complex (DAC) (scott2024widespreaddissolvedinorganic pages 2-4). In CCMs, transporters elevate cytosolic HCO3− and deliver it to **carboxysomes**, where carboxysomal CA converts HCO3− to CO2 for Rubisco (scott2024widespreaddissolvedinorganic pages 2-4). Spatial segregation is crucial; cytosolic CA can induce “massive CO2 leakage” and loss of low-CO2 growth in engineered cyanobacteria (scott2024widespreaddissolvedinorganic pages 2-4).

### 2.3 Recognized natural microbial carbon-fixation pathways
Recent sources enumerate the canonical natural pathways. Scott et al. list (besides CBB): **rTCA, Wood–Ljungdahl (WL), dicarboxylate/4-hydroxybutyrate (DC/HB), hydroxypropionate/4-hydroxybutyrate (HP/HB), hydroxypropionate bicycle (HP), reverse oxidative TCA (roTCA), and the reductive glycine pathway (rGlyP)** (scott2024widespreaddissolvedinorganic pages 1-2). Kurt et al. similarly list CBB, WLP, rGlyP, rTCA, 3HP bicycle, HP/HB, and DC/HB, and discuss pathway energetics (kurt2023perspectivesforusing pages 6-8).

## 3) Recent developments and latest research (prioritize 2023–2024)

### 3.1 2024: DIC supply–demand framing across pathways (beyond CBB)
Scott et al. (AEM, Feb 2024) synthesize how **DIC toolkit genes occur across organisms using non-CBB pathways** and propose that environmental pH and DIC species availability shape which toolkit components are retained (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10). They explicitly connect enzyme substrate specificity to speciation constraints (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic media b4dc8e23).

### 3.2 2024: Pathway co-regulation and “metabolic alliances” around CBB vs rTCA
Mitchell et al. (Nature Microbiology, Jun 2024) show that hydrothermal vent Riftia symbionts express **both CBB and rTCA**, and that each pathway is allied to distinct redox metabolisms: **rTCA with hydrogenases and dissimilatory nitrate reduction; CBB with sulfide oxidation and assimilatory nitrate reduction** (mitchell2024coexpressionanalysisreveals pages 1-2). They identify key rTCA markers (e.g., **aclAB**, **korABCD**) and demonstrate that environmental limitation (ΣH2S and/or O2) shifts expression toward rTCA and a group 1e hydrogenase (mitchell2024coexpressionanalysisreveals pages 4-4, mitchell2024coexpressionanalysisreveals pages 2-3).

### 3.3 2024: Quantification of dark chemosynthetic productivity and genomic prevalence in deep aquifers
Atencio et al. (Scientific Reports, Aug 2024) measure chemosynthetic productivity rates in deep aquifers and report: **0.55 ± 0.06 to 0.82 ± 0.07 µg C L−1 d−1** (atencio2024metabolicadaptationsunderpin pages 1-2), with an additional single observation of 2.14 µg C L−1 d−1 without replicates (atencio2024metabolicadaptationsunderpin pages 5-6). They reconstruct 148 MAGs and report **60% of reconstructed MAGs** carry genes indicative of autotrophic carbon fixation, “mainly the Calvin–Benson–Bassham cycle and the Wood–Ljungdahl pathway” (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8). They also quantify well-specific autotrophy prevalence (e.g., **68% in S1 and 55% in S3**) and provide marker-gene criteria for WL detection (cdhD, cdhE, cooS) (atencio2024metabolicadaptationsunderpin pages 8-9).

### 3.4 2023: Enzyme-centric synthesis and cofactor constraints
- Bährle et al. (Nov 2023) provide canonical CBB stoichiometry: **3 CO2 → 1 GAP costs 9 ATP and 6 NADPH** (bahrle2023currentstatusof pages 1-2), anchoring energetic edges.
- Kang et al. (Jun 2023) emphasize **redox cofactors** and summarize cofactor needs for non-CBB pathways (e.g., rTCA needing reduced ferredoxin and ATP; 3HP/4HB needing NADPH and ATP) (kang2023insightsintoenzyme pages 4-4).
- Bierbaumer et al. (Chemical Reviews, Jan 2023) frame natural and artificial enzymatic CO2 fixation and highlight process/engineering strategies including the use of reduced C1 substrates (formate, methanol) (bierbaumer2023enzymaticconversionof pages 1-2).

## 4) Current applications and real-world implementations

### 4.1 Biomanufacturing using CO2 and C1 feedstocks
Kurt et al. review strategies for using CO2 as a biomanufacturing feedstock, including **one-step direct CO2 fixation** versus **two-step strategies** where CO2 is first converted (electrochemically) to C1/C2 compounds (formate, methanol, acetate, ethanol) and then fermented (kurt2023perspectivesforusing pages 6-8). They discuss pathway choice as constrained by ATP/redox cost and oxygen tolerance (kurt2023perspectivesforusing pages 8-9).

### 4.2 Bioelectrochemical systems and microbial electrosynthesis (MES)
Li (Jan 2024) discusses microbial electrosynthesis as a route to enhance microbial CO2 conversion to organic acids, emphasizing electron supply constraints and process integration (li2024processstudyon pages 1-2). This is supportive for engineering edges but should be curated cautiously because it is not a high-authority primary mechanistic study.

### 4.3 Environmental carbon sinks and dark primary production
The aquifer study provides direct evidence of **dark chemosynthetic productivity** and high genomic prevalence of carbon fixation potential in subsurface waters, motivating real-world ecosystem models and carbon sink accounting (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 8-9).

## 5) Candidate nodes (grouped by type) with suggested ontology grounding

### 5.1 Pathways / metabolic modules
- **Calvin–Benson–Bassham cycle (CBB)** (label; commonly GO:0019253 “reductive pentose-phosphate cycle”) (scott2024widespreaddissolvedinorganic pages 1-2, bahrle2023currentstatusof pages 1-2)
- **Reverse / reductive TCA cycle (rTCA)** (label; sometimes GO:0019674?) (scott2024widespreaddissolvedinorganic pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4)
- **Wood–Ljungdahl pathway (WL/WLP; reductive acetyl‑CoA pathway)** (label) (scott2024widespreaddissolvedinorganic pages 1-2, atencio2024metabolicadaptationsunderpin pages 1-2)
- **3-hydroxypropionate (3HP) bicycle** (label) (scott2024widespreaddissolvedinorganic pages 1-2, kurt2023perspectivesforusing pages 6-8)
- **3HP/4-hydroxybutyrate (HP/HB) cycle** (label) (scott2024widespreaddissolvedinorganic pages 1-2, kang2023insightsintoenzyme pages 4-4)
- **Dicarboxylate/4-hydroxybutyrate (DC/HB) cycle** (label) (scott2024widespreaddissolvedinorganic pages 1-2, kurt2023perspectivesforusing pages 6-8)
- **Reverse oxidative TCA (roTCA)** (label) (scott2024widespreaddissolvedinorganic pages 1-2)
- **Reductive glycine pathway (rGlyP)** (label) (scott2024widespreaddissolvedinorganic pages 1-2, kurt2023perspectivesforusing pages 6-8)

### 5.2 Core enzymes/genes (markers)
- **Rubisco** EC:4.1.1.39; genes **cbbL/cbbS** (form I), **cbbM** (form II) (scott2024widespreaddissolvedinorganic pages 2-4, mitchell2024coexpressionanalysisreveals pages 4-4)
- **Carbonic anhydrase** EC:4.2.1.1 (scott2024widespreaddissolvedinorganic pages 2-4)
- **ATP citrate lyase** (rTCA marker) genes **aclA/aclB** (mitchell2024coexpressionanalysisreveals pages 4-4)
- **2-oxoglutarate oxidoreductase (OGOR)** genes **korABCD** (mitchell2024coexpressionanalysisreveals pages 4-4)
- **CODH/ACS complex** (Wood–Ljungdahl) EC:1.2.7.4 / EC:2.3.1.169; markers include **cooS, cdhD, cdhE** (scott2024widespreaddissolvedinorganic pages 1-2, atencio2024metabolicadaptationsunderpin pages 8-9)
- **Formate dehydrogenase** (CO2 ↔ formate interconversion class; enzyme-substrate noted in Table 1 as CO2) (scott2024widespreaddissolvedinorganic pages 1-2)
- **PEP carboxylase** EC:4.1.1.31 (HCO3− substrate) (scott2024widespreaddissolvedinorganic pages 1-2)
- **Pyruvate carboxylase** EC:6.4.1.1 (HCO3− substrate) (scott2024widespreaddissolvedinorganic pages 1-2)
- **Acetyl‑CoA/propionyl‑CoA carboxylase** EC:6.4.1.2/6.4.1.3 (HCO3− substrate) (scott2024widespreaddissolvedinorganic pages 1-2)

### 5.3 DIC transport / CCM components
- **SbtA** (HCO3− transporter; label) (scott2024widespreaddissolvedinorganic pages 2-4)
- **BicA / SulP-family HCO3− transporter** (label) (scott2024widespreaddissolvedinorganic pages 2-4)
- **CmpABCD ABC transporter** (label) (scott2024widespreaddissolvedinorganic pages 2-4)
- **DIC accumulating complex (DAC)** (label; mechanism unresolved) (scott2024widespreaddissolvedinorganic pages 2-4)
- **Carboxysome** (bacterial microcompartment; label) (scott2024widespreaddissolvedinorganic pages 2-4)

### 5.4 Cofactors / electron carriers
- **ATP** CHEBI:15422 (bahrle2023currentstatusof pages 1-2, kang2023insightsintoenzyme pages 4-4)
- **NADPH** CHEBI:16474 (bahrle2023currentstatusof pages 1-2, kang2023insightsintoenzyme pages 4-4)
- **NAD(P)H** (label; cofactor class) (kang2023insightsintoenzyme pages 4-4)
- **Reduced ferredoxin** (label; ferredoxin redox state) (kang2023insightsintoenzyme pages 4-4, mitchell2024coexpressionanalysisreveals pages 2-3)

### 5.5 Environmental drivers / experimental factors
- **pH** (controls DIC speciation) (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 10-13)
- **O2 availability / limitation** (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4)
- **Sulfide (ΣH2S) availability / limitation** (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4)
- **Nitrate (NO3−)** (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 6-7)
- **Hydrogen (H2)** (linked via hydrogenases) (mitchell2024coexpressionanalysisreveals pages 2-3, mitchell2024coexpressionanalysisreveals pages 4-4)

## 6) Candidate causal edges (evidence-backed) for TraitMech

The following table is intended to be directly actionable for `data/traits/metabolism/carbon_fixation.yaml` curation.

| Edge triple | Edge type | Suggested node grounding (CURIEs where possible) | Evidence snippet (short quote) | Source (first author year, DOI, URL, publication month/year) | Curation notes/uncertainty |
|---|---|---|---|---|---|
| low pH **increases availability of** CO2 | environmental | ENVO:environmental pH; CHEBI:16526 carbon dioxide | “CO2 dominates at low pH” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Strong general rule for DIC speciation; curate as environmental control of substrate availability. |
| circumneutral pH **increases availability of** bicarbonate | environmental | ENVO:environmental pH; CHEBI:17544 bicarbonate | “HCO3− at circumneutral pH” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Strong general rule; important for distinguishing CO2- vs HCO3−-using pathways. |
| carbonic anhydrase **accelerates interconversion of** CO2 and bicarbonate | mechanistic | EC:4.2.1.1; GO:0004089 carbonic anhydrase activity; CHEBI:16526; CHEBI:17544 | “CA activity speeds the interconversion of CO2 and HCO3−” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Core mechanistic edge; highly curation-ready. |
| CO2 **diffuses across** cell membrane **more rapidly than** bicarbonate | environmental | CHEBI:16526; CHEBI:17544; GO:0016020 membrane | “CO2 diffuses through cell membranes more rapidly than HCO3−” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Useful edge linking extracellular chemistry to intracellular supply. |
| RubisCO **uses substrate** CO2 | mechanistic | EC:4.1.1.39; GO:0016984 ribulose-bisphosphate carboxylase activity; CHEBI:16526 | “Ribulose 1,5-bisphosphate carboxylase/oxygenase… Substrate CO2” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Strong enzyme–substrate edge; applies broadly to CBB-associated fixation. |
| phosphoenolpyruvate carboxylase **uses substrate** bicarbonate | mechanistic | EC:4.1.1.31; GO:0008964 phosphoenolpyruvate carboxylase activity; CHEBI:17544 | “Phosphoenolpyruvate carboxylase… HCO3−” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Relevant especially for anaplerotic or module-level CO2 assimilation rather than full autotrophy. |
| pyruvate carboxylase **uses substrate** bicarbonate | mechanistic | EC:6.4.1.1; GO:0004736 pyruvate carboxylase activity; CHEBI:17544 | “Pyruvate carboxylase… HCO3−” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Same caution as above: carboxylation does not by itself prove autotrophy. |
| acetyl-CoA/propionyl-CoA carboxylase **uses substrate** bicarbonate | mechanistic | EC:6.4.1.2; EC:6.4.1.3; CHEBI:17544 | “Acetyl-CoA/propionyl-CoA carboxylase… HCO3−” (scott2024widespreaddissolvedinorganic pages 1-2) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Important for 3HP/4HB- and related pathways/modules. |
| bicarbonate transporters **increase intracellular availability of** bicarbonate | mechanistic | SbtA; KEGG:cmpABCD; SulP family; CHEBI:17544 | “Transporters (SbtA, BicA/SulP, and CmpABCD)… generate elevated intracellular HCO3− concentrations” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Strong DIC-toolkit edge; transporter family grounding partly label-only. |
| carboxysomal carbonic anhydrase **converts** bicarbonate **to** CO2 | mechanistic | CsoSCA; bacterial microcompartment/carboxysome; CHEBI:17544; CHEBI:16526 | “carboxysomal CA converts some of the HCO3− to CO2, which is then fixed by RubisCO” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Strong compartment-specific edge for CCM-equipped CBB organisms. |
| cytoplasmic carbonic anhydrase in low-CO2 cyanobacterial cells **causes** CO2 leakage | mechanistic | EC:4.2.1.1; CHEBI:16526 | “human CA in the cytoplasm… results in loss of the ability to grow under low CO2 conditions and massive CO2 leakage” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23, Feb 2024 | Valid but context-specific to CCM architecture; mark as assay/system-specific. |
| Calvin–Benson–Bassham cycle **consumes** ATP | mechanistic | KEGG/MetaCyc: Calvin cycle; CHEBI:15422 ATP | “fixation of three CO2 to one GAP at the cost of nine ATP and six NADPH” (bahrle2023currentstatusof pages 1-2) | Bährle 2023, DOI:10.1186/s40643-023-00705-9, https://doi.org/10.1186/s40643-023-00705-9, Nov 2023 | Strong pathway–cofactor consumption edge; stoichiometry useful in notes. |
| Calvin–Benson–Bassham cycle **consumes** NADPH | mechanistic | Calvin cycle; CHEBI:16474 NADPH | “fixation of three CO2 to one GAP at the cost of nine ATP and six NADPH” (bahrle2023currentstatusof pages 1-2) | Bährle 2023, DOI:10.1186/s40643-023-00705-9, https://doi.org/10.1186/s40643-023-00705-9, Nov 2023 | Strong edge; general for canonical CBB operation. |
| photosystems **regenerate** NADPH/energy carriers for CBB carbon fixation | mechanistic | GO:0015979 photosynthesis; CHEBI:16474 NADPH | “regeneration of reducing equivalents/energy carriers is performed by photosystems” (bahrle2023currentstatusof pages 1-2) | Bährle 2023, DOI:10.1186/s40643-023-00705-9, https://doi.org/10.1186/s40643-023-00705-9, Nov 2023 | Best curated as photosynthetic context; not universal for all CBB autotrophs. |
| reverse TCA cycle **requires** reduced ferredoxin | mechanistic | rTCA cycle; CHEBI:18248 ferredoxin(reduced) | “rTCA cycle… cofactors NAD(P)H, ATP, Fdred, FADH” (kang2023insightsintoenzyme pages 4-4) | Kang 2023, DOI:10.4014/jmb.2306.06005, https://doi.org/10.4014/jmb.2306.06005, Jun 2023 | Strong cofactor requirement edge from review summary. |
| reverse TCA cycle **requires** ATP | mechanistic | rTCA cycle; CHEBI:15422 ATP | “rTCA cycle… cofactors NAD(P)H, ATP, Fdred, FADH” (kang2023insightsintoenzyme pages 4-4) | Kang 2023, DOI:10.4014/jmb.2306.06005, https://doi.org/10.4014/jmb.2306.06005, Jun 2023 | Broad pathway-level edge. |
| 3HP/4HB cycle **requires** NADPH | mechanistic | 3-hydroxypropionate/4-hydroxybutyrate cycle; CHEBI:16474 NADPH | “3-HP/4-HB cycle… NADPH and ATP required” (kang2023insightsintoenzyme pages 4-4) | Kang 2023, DOI:10.4014/jmb.2306.06005, https://doi.org/10.4014/jmb.2306.06005, Jun 2023 | Strong pathway–cofactor edge. |
| 3HP/4HB cycle **requires** ATP | mechanistic | 3-hydroxypropionate/4-hydroxybutyrate cycle; CHEBI:15422 ATP | “3-HP/4-HB cycle… NADPH and ATP required” (kang2023insightsintoenzyme pages 4-4) | Kang 2023, DOI:10.4014/jmb.2306.06005, https://doi.org/10.4014/jmb.2306.06005, Jun 2023 | Strong pathway–cofactor edge. |
| Wood–Ljungdahl pathway **fixes** CO2 **to produce** acetyl-CoA | mechanistic | Wood-Ljungdahl pathway; EC:1.2.7.4 CODH; EC:2.3.1.169 ACS; CHEBI:16526; CHEBI:15351 acetyl-CoA | “WLP is employed for CO2 fixation and acetyl-CoA production” (kurt2023perspectivesforusing pages 6-8) | Kurt 2023, DOI:10.3390/bioengineering10121357, https://doi.org/10.3390/bioengineering10121357, Nov 2023 | Strong pathway-to-product edge; suitable central node. |
| Wood–Ljungdahl pathway **is ATP-efficient relative to** many other natural fixation pathways | mechanistic | Wood-Ljungdahl pathway | “WLP and rGlyP are ATP-efficient” (kurt2023perspectivesforusing pages 6-8) | Kurt 2023, DOI:10.3390/bioengineering10121357, https://doi.org/10.3390/bioengineering10121357, Nov 2023 | Comparative claim; useful as annotation, not a strict biochemical edge. |
| 3HP bicycle **has ATP cost of about** 2.3 ATP per CO2 | mechanistic | 3-hydroxypropionate bicycle; CHEBI:15422 ATP; CHEBI:16526 | “3HP ≈2.3 ATP/CO2” (kurt2023perspectivesforusing pages 6-8) | Kurt 2023, DOI:10.3390/bioengineering10121357, https://doi.org/10.3390/bioengineering10121357, Nov 2023 | Quantitative pathway property; curate as efficiency attribute if schema permits. |
| dicarboxylate/4-hydroxybutyrate cycle **has ATP cost of about** 1.6 ATP per CO2 | mechanistic | DC/4HB cycle; CHEBI:15422 ATP; CHEBI:16526 | “DC/HB ≈1.6 ATP/CO2” (kurt2023perspectivesforusing pages 6-8) | Kurt 2023, DOI:10.3390/bioengineering10121357, https://doi.org/10.3390/bioengineering10121357, Nov 2023 | Quantitative pathway property; same curation note as above. |
| reduced C1 derivatives such as formate and methanol **can substitute for direct use of** CO2 in biocatalytic assimilation strategies | engineering | CHEBI:15740 formate; CHEBI:17790 methanol; CHEBI:16526 | “use of reduced C1 derivatives (formate, methanol) as alternative substrates” (bierbaumer2023enzymaticconversionof pages 1-2) | Bierbaumer 2023, DOI:10.1021/acs.chemrev.2c00581, https://doi.org/10.1021/acs.chemrev.2c00581, Jan 2023 | Engineering-oriented edge; not a natural-trait-defining mechanism by itself. |
| low sulfide and/or oxygen limitation **upregulates** rTCA-associated genes and group 1e hydrogenase in Riftia symbionts | environmental | rTCA cycle; ATP citrate lyase aclAB; group 1e [NiFe]-hydrogenase | “limitation of seawater ΣH2S and/or O2 is associated with upregulation of rTCA and a [NiFe] hydrogenase” (mitchell2024coexpressionanalysisreveals pages 2-3) | Mitchell 2024, DOI:10.1038/s41564-024-01704-y, https://doi.org/10.1038/s41564-024-01704-y, Jun 2024 | Strong but taxon-specific regulatory edge from vent symbiosis. |
| rTCA cycle **is co-expressed with** hydrogenases and dissimilatory nitrate reduction | mechanistic | rTCA cycle; hydrogenase; napAB/nirS/nosZ | “the rTCA is allied with hydrogenases and dissimilatory nitrate reduction” (mitchell2024coexpressionanalysisreveals pages 1-2) | Mitchell 2024, DOI:10.1038/s41564-024-01704-y, https://doi.org/10.1038/s41564-024-01704-y, Jun 2024 | Strong systems-level association; curate as co-expression/functional-alliance edge, not direct catalysis. |
| Calvin cycle **is co-expressed with** sulfide oxidation and assimilatory nitrate reduction | mechanistic | CBB cycle; RubisCO cbbM/cbbL; Sox/rDSR/aprAB/sat/sqrA/fccA | “the CBB is allied with sulfide oxidation and assimilatory nitrate reduction” (mitchell2024coexpressionanalysisreveals pages 1-2) | Mitchell 2024, DOI:10.1038/s41564-024-01704-y, https://doi.org/10.1038/s41564-024-01704-y, Jun 2024 | Strong systems-level association; taxon/environment specific. |
| ATP citrate lyase (aclAB) **enables** reverse TCA carbon fixation | mechanistic | EC:2.3.3.8 ATP citrate lyase; gene:aclA/aclB | “aclAB for ATP citrate lyase… one of four key enzymes needed to run the TCA cycle in reverse” (mitchell2024coexpressionanalysisreveals pages 4-4) | Mitchell 2024, DOI:10.1038/s41564-024-01704-y, https://doi.org/10.1038/s41564-024-01704-y, Jun 2024 | Strong marker-gene edge for rTCA. |
| chemolithoautotrophic productivity in deep aquifers **can be supported by** CBB and Wood–Ljungdahl pathways | environmental | CBB cycle; Wood-Ljungdahl pathway; aquifer biome | “60% of MAGs harbored genes for autotrophic pathways, mainly the Calvin–Benson–Bassham cycle and the Wood–Ljungdahl pathway” (atencio2024metabolicadaptationsunderpin pages 1-2) | Atencio 2024, DOI:10.1038/s41598-024-68868-9, https://doi.org/10.1038/s41598-024-68868-9, Aug 2024 | Environmental prevalence/statistics edge; stronger as habitat-association than direct mechanism. |
| deep aquifer microbial communities **exhibit** chemosynthetic productivity of 0.55–0.82 µg C L−1 d−1 | environmental | aquifer microbial community; carbon fixation rate | “productivity rates ranging from 0.55 ± 0.06 to 0.82 ± 0.07 µg C L−1 d−1” (atencio2024metabolicadaptationsunderpin pages 1-2) | Atencio 2024, DOI:10.1038/s41598-024-68868-9, https://doi.org/10.1038/s41598-024-68868-9, Aug 2024 | Phenotype/rate evidence for dark carbon fixation in situ; not a causal edge between molecular nodes. |
| microbial electrosynthesis **enhances electron supply for** acetogenic CO2 fixation | engineering | microbial electrosynthesis; acetogen; CO2 fixation | “Microbial electrosynthesis (MES) systems have shown … prominently facilitated by acetogenic bacteria” (li2024processstudyon pages 1-2) | Li 2024, DOI:10.5376/be.2024.14.0016, https://doi.org/10.5376/be.2024.14.0016, Jan 2024 | Process-level engineering edge; evidence source is lower authority than primary mechanistic papers. |
| gas/photon transfer optimization **improves** engineered microbial CO2 fixation processes | engineering | process parameter node; CO2 fixation bioprocess | “gas and photon transfer rates, high-density cultivation” were noted as process controls (li2024processstudyon pages 5-7) | Li 2024, DOI:10.5376/be.2024.14.0016, https://doi.org/10.5376/be.2024.14.0016, Jan 2024 | Useful for applications section; mechanism indirect and process-specific. |
| heterologous expression of reverse TCA genes in E. coli **enables** succinate production from CO2-assimilation modules | engineering | Escherichia coli NCBITaxon:562; rTCA module; succinate CHEBI:15741 | “heterologous rTCA gene expression in E. coli for succinate” (li2024processstudyon pages 5-7) | Li 2024, DOI:10.5376/be.2024.14.0016, https://doi.org/10.5376/be.2024.14.0016, Jan 2024 | Engineering/inference edge from review-style process paper; should be curated cautiously. |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for curating a TraitMech causal graph of microbial carbon fixation. It prioritizes mechanistic pathway, enzyme, cofactor, and environmental-control relationships, while separating more tentative engineering and habitat-association claims.*

**Visual evidence supporting key nodes:** Scott et al. Table 1 (enzyme substrate specificity) and a DIC toolkit schematic are provided as extracted images (scott2024widespreaddissolvedinorganic media b4dc8e23, scott2024widespreaddissolvedinorganic media d68b56dc).

## 7) Relevant statistics and data (recent studies)

- **Deep aquifer chemosynthetic productivity:** 0.55 ± 0.06 to 0.82 ± 0.07 µg C L−1 d−1 fixed carbon (with an additional single unreplicated observation of 2.14 µg C L−1 d−1) (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 5-6).
- **Genomic prevalence in deep aquifers:** 60% of reconstructed MAGs carried genes indicative of autotrophic carbon fixation; dominant pathways were CBB and Wood–Ljungdahl (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8). Well-specific prevalence: 68% (S1) and 55% (S3) (atencio2024metabolicadaptationsunderpin pages 8-9).
- **Rubisco form distribution in aquifer MAGs:** RuBisCO encoded by 32 MAGs (16 form I, 2 form II, 14 both forms) (atencio2024metabolicadaptationsunderpin pages 6-8).

## 8) Expert opinions / analysis (authoritative-source synthesis)

**Carbon fixation is a supply–demand problem.** Scott et al. articulate that the “bedeviling nature” of DIC arises from pH-driven speciation, enzyme substrate specificity, membrane permeability differences, and slow uncatalyzed interconversion—driving evolution of toolkits (CA and transporters) that “bridge supply from the environment to demand by the autotrophic pathway” (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 2-4). This framing is directly useful for causal graph organization: **environment → DIC species → transport/interconversion → enzyme substrate → pathway flux → trait**.

**Pathway choice and regulation are redox-environment dependent.** Mitchell et al. demonstrate in situ that two pathways can be maintained and dynamically regulated: rTCA linked to H2/nitrate-related energy flow and responsive to sulfide/O2 limitation, whereas CBB is aligned with sulfide oxidation and different nitrate assimilation modes (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4). This supports curation of pathway edges that include **conditional regulation by O2 and electron donor availability**, not only constitutive pathway presence.

**Energetics and cofactors are primary limiting variables.** Reviews emphasize that ATP and reducing equivalents constrain feasibility and engineering outcomes. CBB has explicit high ATP/NADPH demand (bahrle2023currentstatusof pages 1-2), while non-CBB pathways rely on reduced ferredoxin and other cofactors sensitive to oxygen/redox conditions (kang2023insightsintoenzyme pages 4-4, mitchell2024coexpressionanalysisreveals pages 2-3).

## 9) Warnings (claims not yet suitable for strong curation)

1. **Do not equate single enzyme presence with carbon fixation trait.** PEP carboxylase/pyruvate carboxylase and other carboxylases often support anaplerosis (scott2024widespreaddissolvedinorganic pages 1-2). Require a full pathway module or net-fixation evidence.
2. **Gene presence ≠ net fixation.** WLP genes may support energy conservation or other roles; Atencio et al. highlight this explicitly (atencio2024metabolicadaptationsunderpin pages 8-9). Curate as “potential” unless coupled to flux/labeling/physiology.
3. **Engineering and process claims** from non-authoritative or low-citation sources (e.g., Li 2024 process study) should be curated as **application/process context** or **hypothesis** rather than mechanism (li2024processstudyon pages 1-2, li2024processstudyon pages 5-7).
4. **Taxon-specific regulation edges** (e.g., Riftia symbiont co-expression alliances) are strong within that system but may not generalize; curate with appropriate scope qualifiers (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4).

## 10) DOI-first bibliography (with URLs and publication dates where available)

1. **Scott KM, Payne RR, Gahramanova A.** Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea and how they are likely to bridge supply from the environment to demand by autotrophic pathways. *Applied and Environmental Microbiology*. **Published Feb 1, 2024**. DOI: **10.1128/aem.01557-23**. URL: https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 2-4)
2. **Mitchell JH, Freedman AH, Delaney JA, Girguis PR.** Co-expression analysis reveals distinct alliances around two carbon fixation pathways in hydrothermal vent symbionts. *Nature Microbiology*. **Jun 2024**. DOI: **10.1038/s41564-024-01704-y**. URL: https://doi.org/10.1038/s41564-024-01704-y (mitchell2024coexpressionanalysisreveals pages 1-2, mitchell2024coexpressionanalysisreveals pages 4-4)
3. **Atencio B, et al.** Metabolic adaptations underpin high productivity rates in relict subsurface water. *Scientific Reports*. **Aug 2024**. DOI: **10.1038/s41598-024-68868-9**. URL: https://doi.org/10.1038/s41598-024-68868-9 (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 5-6)
4. **Bährle R, et al.** Current status of carbon monoxide dehydrogenases (CODH) and their potential for electrochemical applications. *Bioresources and Bioprocessing*. **Nov 2023**. DOI: **10.1186/s40643-023-00705-9**. URL: https://doi.org/10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 1-2)
5. **Kang D-K, et al.** Insights into Enzyme Reactions with Redox Cofactors in Biological Conversion of CO2. *Journal of Microbiology and Biotechnology*. **Jun 2023**. DOI: **10.4014/jmb.2306.06005**. URL: https://doi.org/10.4014/jmb.2306.06005 (kang2023insightsintoenzyme pages 4-4)
6. **Kurt E, et al.** Perspectives for Using CO2 as a Feedstock for Biomanufacturing of Fuels and Chemicals. *Bioengineering*. **Nov 2023**. DOI: **10.3390/bioengineering10121357**. URL: https://doi.org/10.3390/bioengineering10121357 (kurt2023perspectivesforusing pages 6-8)
7. **Bierbaumer S, et al.** Enzymatic Conversion of CO2: From Natural to Artificial Utilization. *Chemical Reviews*. **Jan 2023**. DOI: **10.1021/acs.chemrev.2c00581**. URL: https://doi.org/10.1021/acs.chemrev.2c00581 (bierbaumer2023enzymaticconversionof pages 1-2)
8. **Li M.** Process Study on Microbial Fixation of CO2 and Its Conversion into Organic Acids. *Biological Evidence*. **Jan 2024**. DOI: **10.5376/be.2024.14.0016**. URL: https://doi.org/10.5376/be.2024.14.0016 (li2024processstudyon pages 1-2)


References

1. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

2. (scott2024widespreaddissolvedinorganic media b4dc8e23): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

3. (mitchell2024coexpressionanalysisreveals pages 1-2): Jessica H. Mitchell, Adam H. Freedman, Jennifer A. Delaney, and Peter R. Girguis. Co-expression analysis reveals distinct alliances around two carbon fixation pathways in hydrothermal vent symbionts. Nature Microbiology, 9:1526-1539, Jun 2024. URL: https://doi.org/10.1038/s41564-024-01704-y, doi:10.1038/s41564-024-01704-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

4. (mitchell2024coexpressionanalysisreveals pages 4-4): Jessica H. Mitchell, Adam H. Freedman, Jennifer A. Delaney, and Peter R. Girguis. Co-expression analysis reveals distinct alliances around two carbon fixation pathways in hydrothermal vent symbionts. Nature Microbiology, 9:1526-1539, Jun 2024. URL: https://doi.org/10.1038/s41564-024-01704-y, doi:10.1038/s41564-024-01704-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

5. (atencio2024metabolicadaptationsunderpin pages 8-9): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

6. (bierbaumer2023enzymaticconversionof pages 1-2): Sarah Bierbaumer, Maren Nattermann, Luca Schulz, Reinhard Zschoche, Tobias J. Erb, Christoph K. Winkler, Matthias Tinzl, and Silvia M. Glueck. Enzymatic conversion of co2: from natural to artificial utilization. Chemical Reviews, 123:5702-5754, Jan 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00581, doi:10.1021/acs.chemrev.2c00581. This article has 287 citations and is from a highest quality peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 10-13): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

8. (scott2024widespreaddissolvedinorganic pages 2-4): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

9. (scott2024widespreaddissolvedinorganic media d68b56dc): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

10. (kurt2023perspectivesforusing pages 6-8): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.

11. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

12. (mitchell2024coexpressionanalysisreveals pages 2-3): Jessica H. Mitchell, Adam H. Freedman, Jennifer A. Delaney, and Peter R. Girguis. Co-expression analysis reveals distinct alliances around two carbon fixation pathways in hydrothermal vent symbionts. Nature Microbiology, 9:1526-1539, Jun 2024. URL: https://doi.org/10.1038/s41564-024-01704-y, doi:10.1038/s41564-024-01704-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

13. (atencio2024metabolicadaptationsunderpin pages 1-2): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

14. (atencio2024metabolicadaptationsunderpin pages 5-6): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

15. (atencio2024metabolicadaptationsunderpin pages 6-8): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

16. (bahrle2023currentstatusof pages 1-2): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 27 citations and is from a peer-reviewed journal.

17. (kang2023insightsintoenzyme pages 4-4): Du-Kyeong Kang, Seung-Hwa Kim, Jung-Hoon Sohn, and Bong Hyun Sung. Insights into enzyme reactions with redox cofactors in biological conversion of co2. Journal of Microbiology and Biotechnology, 33:1403-1411, Jun 2023. URL: https://doi.org/10.4014/jmb.2306.06005, doi:10.4014/jmb.2306.06005. This article has 10 citations and is from a peer-reviewed journal.

18. (kurt2023perspectivesforusing pages 8-9): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.

19. (li2024processstudyon pages 1-2): Manman Li. Process study on microbial fixation of co&lt;sub&gt;2&lt;/sub&gt; and its conversion into organic acids. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0016, doi:10.5376/be.2024.14.0016. This article has 1 citations.

20. (mitchell2024coexpressionanalysisreveals pages 6-7): Jessica H. Mitchell, Adam H. Freedman, Jennifer A. Delaney, and Peter R. Girguis. Co-expression analysis reveals distinct alliances around two carbon fixation pathways in hydrothermal vent symbionts. Nature Microbiology, 9:1526-1539, Jun 2024. URL: https://doi.org/10.1038/s41564-024-01704-y, doi:10.1038/s41564-024-01704-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

21. (li2024processstudyon pages 5-7): Manman Li. Process study on microbial fixation of co&lt;sub&gt;2&lt;/sub&gt; and its conversion into organic acids. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0016, doi:10.5376/be.2024.14.0016. This article has 1 citations.