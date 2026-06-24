---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:55:41.248051'
end_time: '2026-06-18T05:07:43.700233'
duration_seconds: 722.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ethanol fermentation
  trait_identifier: traitmech:000028
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: ethanol_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing
    CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic
    of yeasts and the bacterium Zymomonas mobilis.
  parent_traits: METPO:1002005
  synonyms: alcoholic fermentation
  evidence_summary: 'DOI:10.3390/molecules31020333:  (Review of classical fermentations
    describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated
    and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative
    energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)'
  causal_graph_summary: 'ethanol_fermentation_pyruvate_to_ethanol: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ethanol fermentation
- **METPO identifier:** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ethanol fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/ethanol_fermentation.yaml`.

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
- **Trait label:** ethanol fermentation
- **METPO identifier:** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ethanol fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/ethanol_fermentation.yaml`.

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


## Ethanol fermentation (traitmech:000028) — curation-focused research report (2023–2024 priority)

### 0) Scope summary (TraitMech/METPO)
**Ethanol fermentation (alcoholic fermentation)** is the microbial physiological capacity to convert **pyruvate to ethanol** through the intermediate **acetaldehyde**, primarily to **reoxidize NADH to NAD+** and thereby sustain glycolysis under conditions where respiration is limited or redirected. Canonically, pyruvate is decarboxylated by **pyruvate decarboxylase (PDC)** to acetaldehyde (releasing **CO2**), and acetaldehyde is reduced by **alcohol dehydrogenase (ADH)** to ethanol, regenerating NAD+ from NADH. (yan2024thebiochemicalbasis pages 2-5)

**Boundary cases / nearby traits** relevant for graph scoping:
- **Alternative bacterial route via acetyl‑CoA**: many anaerobic bacteria use **AdhE**, a bifunctional aldehyde/alcohol dehydrogenase, catalyzing acetyl‑CoA → acetaldehyde → ethanol (not the strict PDC route). (ziegler2024structuralcharacterizationand pages 1-3)
- **Other NADH-reoxidizing fermentations** (lactate, mixed-acid, 2,3‑butanediol/acetoin, glycerol) can compete with ethanol as electron sinks and should be treated as distinct traits with edges that modulate carbon/redox partitioning. For example, Zymomonas mobilis redirection from ethanol to acetoin via redox engineering explicitly leverages NAD+/NADH balance. (bao2023metabolicengineeringof pages 9-11)
- **Engineered phenotypes** (e.g., heterologous PDC/ADH in cyanobacteria) are real-world implementations of the same mechanistic module, but are not necessarily native traits of those chassis organisms. (gao2023rewiringcarbonflow pages 1-2)

### 1) Key concepts and current mechanistic understanding
#### 1.1 Canonical biochemical module (pyruvate → acetaldehyde → ethanol)
A 2024 review explicitly summarizes the core reaction sequence and its redox function: pyruvate is converted to acetaldehyde by PDC with CO2 release, then acetaldehyde is reduced to ethanol by ADH, **“regenerating NAD+ from NADH to sustain glycolysis”**. (yan2024thebiochemicalbasis pages 2-5)

Mechanistically, this module is best represented as a causal subgraph:
- Glycolysis produces pyruvate and NADH.
- PDC generates acetaldehyde and CO2.
- ADH consumes NADH to reduce acetaldehyde to ethanol, regenerating NAD+.

#### 1.2 Alternative ethanol-formation module in anaerobic bacteria (AdhE)
Recent structural work in *Clostridium thermocellum* (2024) emphasizes AdhE as the key ethanol-pathway enzyme, with **ALDH reducing acetyl‑CoA to acetaldehyde** and **ADH reducing acetaldehyde to ethanol**. (ziegler2024structuralcharacterizationand pages 1-3)

A major 2024 development is mechanistic evidence that AdhE forms **spirosomes** that can **channel/contain acetaldehyde**, a toxic intermediate: the extended spirosome presents an **“entirely enclosed channel”** between domains, consistent with intermediate sequestration and efficient conversion. (ziegler2024structuralcharacterizationand pages 11-12)

### 2) Recent developments and latest research (prioritize 2023–2024)
#### 2.1 Zymomonas mobilis: dominance/centrality of pdc and controllable redirection
Zymomonas mobilis is repeatedly characterized as an exceptional ethanologen with near-theoretical yields and high flux. A 2024 platform-strain paper highlights that PDC is the **“key enzyme converting pyruvate to acetaldehyde”** and notes **pdc is widely considered essential**, motivating inducible control strategies rather than deletion. (frohwitter2024anewzymomonas pages 1-2)

Quantitative engineering evidence for redirecting pyruvate away from ethanol:
- In a 2024 controllable-pdc strain context, lactate production reached **173.6 ± 2.2 mM (78% theoretical)** at specific lactate productivity **66.6 ± 0.6 mmol gCDW−1 h−1**, while ethanol dropped to **~18% of theoretical** (defined medium, 2% glucose). (frohwitter2024anewzymomonas pages 5-7)
- A 2023 study engineered *Z. mobilis* for co-production of D-lactate and ethanol by relocating/replacing pdc copies and strong-promoter ldh expression; it reports in pH-controlled fermenters **productivities 1.9–2.2 g/L/h** and total carbon conversion **~96–98%**, with waste feedstocks achieving up to **42.8 ± 0.0 g/L D‑lactate + 53.1 ± 0.7 g/L ethanol**. (hu2023metabolicengineeringof pages 1-2)

Gene grounding progress for curation:
- A 2023 transporter/fermentation study explicitly maps **Pdc = ZMO1360** and **AdhB = ZMO1596** in *Z. mobilis*. (zhang2023characterizationandapplication pages 2-4)

#### 2.2 Cofactor/redox engineering as a lever on ethanol vs byproduct partitioning
A 2023 *Z. mobilis* acetoin study makes the redox coupling explicit: Z. mobilis regenerates NAD+ mainly via ethanol production, while introducing competing pathways perturbs NADH balance; adding **water-forming NADH oxidase (NoxE)** increases NAD+/NADH and shifts outcomes. (bao2023metabolicengineeringof pages 9-11)

Engineering modulation of ethanol flux:
- **CRISPRi of pdc** increased acetoin by **11.24%** while decreasing ethanol by **15.57%** (with growth impairment). (bao2023metabolicengineeringof pages 9-11)

#### 2.3 Photosynthetic CO2-to-ethanol via heterologous PDC/ADH (real-world synthetic implementation)
A 2023 study demonstrates engineered *Synechocystis* sp. PCC6803 ethanol production from atmospheric CO2 by introducing heterologous **PDC (from *Z. mobilis*)** and **ADH/YqhD (from *E. coli*)**. (gao2023rewiringcarbonflow pages 4-6, gao2023rewiringcarbonflow pages 1-2)

Quantitative performance reported:
- Strain series produced (Table-reported) ethanol production rates up to **248 mg/L/day** (SYN009), and titers up to **>700 mg/L at 7 days** for intermediate strains; SYN009 is reported at **1.09 g/L ethanol** and **peak accumulation rate 248 mg/L/day**. (gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 6-7)

These results support a generalizable “ethanol module” that can be transferred across hosts as a causal graph motif.

#### 2.4 Stress biology: when ethanol fermentation becomes required vs inhibited
**Reactive nitrogen stress (RNS)**: In *Aspergillus nidulans* (2024), deletion of **pdcA** or **alcC** (ADH) causes retarded growth under acidified nitrite, indicating ethanol fermentation genes contribute causally to growth under RNS stress. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6)

**Benzoic acid inhibitor**: In *S. cerevisiae* molasses-like conditions (2024), benzoic acid inhibits fermentation physiology and gene expression: glycolytic/fermentation-associated genes including **PDC6** are downregulated (PDC6 log2FC −3.80), and authors interpret this as inhibited glycolysis and impaired alcohol fermentation. (xiufeng2024responsemechanismof pages 13-15, xiufeng2024responsemechanismof pages 17-18)

### 3) Current applications and real-world implementations
1. **Industrial ethanol production & high-gravity fermentation**: A 2024 review reports industrial processes achieving **up to 92% of theoretical ethanol yield (batch)** and **88% (fed-batch)** and **ethanol concentrations >15% v/v** in high-gravity contexts. (yan2024thebiochemicalbasis pages 7-9)
2. **Biorefinery chassis engineering (Z. mobilis)**: 2023–2024 primary studies provide concrete implementation patterns for redirecting pyruvate away from ethanol (e.g., controllable pdc, CRISPRi, cofactor balancing) to produce other chemicals while using the ethanol pathway as a flux/redox reference. (frohwitter2024anewzymomonas pages 5-7, bao2023metabolicengineeringof pages 9-11, frohwitter2024anewzymomonas pages 1-2)
3. **Carbon-negative/CO2 valorization concepts**: engineered cyanobacterial CO2-to-ethanol production provides a proof-of-concept for coupling carbon fixation to ethanol module expression, with measurable g/L titers under atmospheric conditions. (gao2023rewiringcarbonflow pages 6-7)
4. **Food & beverage process control**: enzyme-level manipulation of acetaldehyde-to-ethanol conversion has practical value because acetaldehyde affects wine sensory and health-relevant properties. Recombinant yeast ADH1 expressed and applied exogenously shows high specific activity (605.44 ± 44.30 U/mg) and reduces wine acetaldehyde under controlled cofactor supply. (geng2023enhancedexpressionof pages 12-14)

### 4) Expert opinions / analysis from authoritative sources
- **“Key enzyme” framing**: The 2024 *Microbial Cell Factories* study explicitly positions PDC as the key node constraining redirection of *Z. mobilis* away from ethanol, motivating inducible control. (frohwitter2024anewzymomonas pages 1-2)
- **Structural mechanistic interpretation**: The 2024 AdhE cryo-EM/MD work provides an authoritative mechanistic hypothesis that spirosome ultrastructures serve an intermediate-containment function to mitigate acetaldehyde toxicity and potentially regulate activity/cofactor pools. (ziegler2024structuralcharacterizationand pages 11-12, ziegler2024structuralcharacterizationand pages 1-3)
- **Stress adaptation viewpoint**: The 2024 fungal RNS study supports an expert-level metabolic adaptation narrative: when respiration is impaired, cells rely more on glycolysis and ethanol fermentation, and ethanol-pathway gene deletions reduce stress growth. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6)

### 5) Relevant statistics and quantitative data (recent)
- **Industrial (review-level)**: up to **92% theoretical yield (batch)**, **88% (fed-batch)**; **>15% v/v ethanol** in high-gravity processes. (yan2024thebiochemicalbasis pages 7-9)
- **Z. mobilis (2024)**: lactate **173.6 ± 2.2 mM (78% theoretical)**; ethanol reduced to **~18% theoretical** under redirection regime. (frohwitter2024anewzymomonas pages 5-7)
- **Z. mobilis waste feedstocks (2023)**: up to **42.8 ± 0.0 g/L D-lactate + 53.1 ± 0.7 g/L ethanol**, carbon conversion **≥97–99%**, productivity **~1.9–2.2 g/L/h**. (hu2023metabolicengineeringof pages 1-2)
- **Engineered Synechocystis (2023)**: ethanol production rates up to **248 mg/L/day**; reported titers up to **1.09 g/L** (SYN009). (gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 6-7)
- **Z. mobilis acetoin diversion (2023)**: acetoin titer **>8.84 g/L**, productivity **0.34 g·L−1·h−1** with NADH oxidase balancing; pdc CRISPRi decreased ethanol by **15.57%**. (bao2023metabolicengineeringof pages 9-11)

---

## Candidate nodes/entities for `ethanol_fermentation.yaml`
The following table is a curation-ready shortlist of mechanistic nodes with conservative ontology grounding.

| Node label | Type | Brief description | Suggested identifier(s) | Key supporting source(s) with DOI+URL+year |
|---|---|---|---|---|
| Alcoholic/ethanol fermentation | Process/Pathway | Fermentative conversion of pyruvate-derived intermediates to ethanol with NADH reoxidation to NAD+; core trait under curation. (yan2024thebiochemicalbasis pages 2-5, yan2024thebiochemicalbasis pages 1-2) | METPO: traitmech:000028; GO:0006113 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; existing trait definition/evidence context |
| Glycolysis (EMP pathway) | Process/Pathway | Upstream pathway producing pyruvate, ATP, and NADH that feeds alcoholic fermentation in many yeasts and bacteria. (yan2024thebiochemicalbasis pages 2-5, yan2024thebiochemicalbasis pages 1-2) | GO:0006096 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025 |
| Entner-Doudoroff pathway | Process/Pathway | High-flux glucose catabolism used by Zymomonas mobilis to supply pyruvate for ethanol production. (zhang2023characterizationandapplication pages 2-4, frohwitter2024anewzymomonas pages 1-2) | KEGG map00030; MetaCyc:ENTNER-DOUDOROFF-PWY | Zhang 2023, DOI:10.3390/ijms24065888, https://doi.org/10.3390/ijms24065888; Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9 |
| Pyruvate-to-acetaldehyde step | Process/Pathway | Canonical decarboxylation step releasing CO2 and committing carbon to ethanol fermentation. (yan2024thebiochemicalbasis pages 2-5, bao2023metabolicengineeringof pages 1-2) | EC:4.1.1.1-associated reaction | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| Acetaldehyde-to-ethanol step | Process/Pathway | Reductive terminal step that consumes reducing equivalents and completes ethanol formation. (yan2024thebiochemicalbasis pages 2-5, ziegler2024structuralcharacterizationand pages 1-3) | EC:1.1.1.1-associated reaction | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662 |
| NADH reoxidation / NAD+ regeneration | Process/Pathway | Redox-balancing function of ethanol fermentation that sustains glycolysis. (yan2024thebiochemicalbasis pages 2-5, bao2023metabolicengineeringof pages 9-11) | GO:0006735; CHEBI:57945/CHEBI:57540 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| Acetyl-CoA-to-ethanol via AdhE | Process/Pathway | Alternative bacterial ethanol-forming route using bifunctional aldehyde/alcohol dehydrogenase rather than pyruvate decarboxylase. (ziegler2024structuralcharacterizationand pages 1-3, yan2024thebiochemicalbasis pages 1-2) | EC:1.2.1.10 + EC:1.1.1.1 | Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662; Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025 |
| Pyruvate decarboxylase (PDC) | Enzymes/Genes | Enzyme catalyzing pyruvate decarboxylation to acetaldehyde + CO2; central control point for ethanol flux. (yan2024thebiochemicalbasis pages 2-5, frohwitter2024anewzymomonas pages 1-2) | EC:4.1.1.1; GO:0004737 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9 |
| Alcohol dehydrogenase (ADH) | Enzymes/Genes | Enzyme reducing acetaldehyde to ethanol while oxidizing NADH. (yan2024thebiochemicalbasis pages 2-5, geng2023enhancedexpressionof pages 12-14) | EC:1.1.1.1; GO:0004022 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Geng 2023, DOI:10.3390/microorganisms12010038, https://doi.org/10.3390/microorganisms12010038 |
| adhE | Enzymes/Genes | Bifunctional aldehyde/alcohol dehydrogenase that converts acetyl-CoA to acetaldehyde and acetaldehyde to ethanol in many anaerobic bacteria. (ziegler2024structuralcharacterizationand pages 1-3, yan2024thebiochemicalbasis pages 1-2) | gene:adhE; EC:1.2.1.10/1.1.1.1 | Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662; Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025 |
| pdc (Z. mobilis) | Enzymes/Genes | Central Zymomonas mobilis ethanol-pathway gene; promoter replacement or repression redirects carbon from ethanol. (frohwitter2024anewzymomonas pages 1-2, bao2023metabolicengineeringof pages 9-11) | gene:pdc | Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| ZMO1360 / Pdc | Enzymes/Genes | Locus-tagged pyruvate decarboxylase in Z. mobilis. (zhang2023characterizationandapplication pages 2-4) | gene:ZMO1360; EC:4.1.1.1 | Zhang 2023, DOI:10.3390/ijms24065888, https://doi.org/10.3390/ijms24065888 |
| adhB / AdhB | Enzymes/Genes | Zymomonas alcohol dehydrogenase B participating in ethanol formation. (zhang2023characterizationandapplication pages 2-4, bao2023metabolicengineeringof pages 1-2) | gene:adhB; gene:ZMO1596; EC:1.1.1.1 | Zhang 2023, DOI:10.3390/ijms24065888, https://doi.org/10.3390/ijms24065888; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| ADH1 | Enzymes/Genes | Yeast alcohol dehydrogenase isozyme used in wine and recombinant acetaldehyde-reduction studies. (geng2023enhancedexpressionof pages 12-14, geng2023enhancedexpressionof pages 15-16) | gene:ADH1; EC:1.1.1.1 | Geng 2023, DOI:10.3390/microorganisms12010038, https://doi.org/10.3390/microorganisms12010038 |
| PDC6 | Enzymes/Genes | Stress-responsive pyruvate decarboxylase-associated yeast gene downregulated by benzoic acid during ethanol fermentation. (xiufeng2024responsemechanismof pages 13-15) | gene:PDC6 | Xiu-Feng 2024, DOI:10.1038/s41598-024-80484-1, https://doi.org/10.1038/s41598-024-80484-1 |
| pdcA | Enzymes/Genes | Aspergillus nidulans pyruvate decarboxylase required for growth under reactive nitrogen stress. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, kadooka2024fungalglyceraldehyde3phosphate pages 6-8) | gene:pdcA; EC:4.1.1.1 | Kadooka 2024, DOI:10.3389/fmicb.2024.1475567, https://doi.org/10.3389/fmicb.2024.1475567 |
| alcC | Enzymes/Genes | Aspergillus nidulans alcohol dehydrogenase required for growth and ethanol formation under reactive nitrogen stress. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, kadooka2024fungalglyceraldehyde3phosphate pages 6-8) | gene:alcC; EC:1.1.1.1 | Kadooka 2024, DOI:10.3389/fmicb.2024.1475567, https://doi.org/10.3389/fmicb.2024.1475567 |
| yqhD | Enzymes/Genes | Heterologous alcohol dehydrogenase used with PDC in engineered cyanobacterial CO2-to-ethanol production. (gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 1-2) | gene:yqhD; EC:1.1.1.- | Gao 2023, DOI:10.3389/fmicb.2023.1211004, https://doi.org/10.3389/fmicb.2023.1211004 |
| noxE | Enzymes/Genes | Water-forming NADH oxidase introduced to manipulate NAD+/NADH balance during flux redirection away from ethanol. (bao2023metabolicengineeringof pages 1-2, bao2023metabolicengineeringof pages 9-11) | gene:noxE; EC:1.6.3.4 | Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| pyruvate | Metabolites/Cofactors | Central carbon intermediate feeding ethanol fermentation. (yan2024thebiochemicalbasis pages 2-5, ziegler2024structuralcharacterizationand pages 1-3) | CHEBI:15361 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662 |
| acetaldehyde | Metabolites/Cofactors | Immediate intermediate between pyruvate/acetyl-CoA and ethanol; toxic if not efficiently converted or channeled. (yan2024thebiochemicalbasis pages 2-5, ziegler2024structuralcharacterizationand pages 11-12) | CHEBI:15343 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662 |
| ethanol | Metabolites/Cofactors | Final product of alcoholic fermentation and key industrial biofuel/fermentation metabolite. (yan2024thebiochemicalbasis pages 2-5, yan2024thebiochemicalbasis pages 7-9) | CHEBI:16236 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025 |
| carbon dioxide | Metabolites/Cofactors | Gaseous coproduct released during pyruvate decarboxylation. (yan2024thebiochemicalbasis pages 2-5) | CHEBI:16526 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025 |
| NADH | Metabolites/Cofactors | Reducing cofactor consumed in acetaldehyde reduction and broader redox balancing. (yan2024thebiochemicalbasis pages 2-5, bao2023metabolicengineeringof pages 9-11) | CHEBI:57945 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| NAD+ | Metabolites/Cofactors | Oxidized cofactor regenerated by ethanol formation to sustain glycolysis. (yan2024thebiochemicalbasis pages 2-5, bao2023metabolicengineeringof pages 9-11) | CHEBI:57540 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| acetyl-CoA | Metabolites/Cofactors | Intermediate used in AdhE-based bacterial ethanol synthesis. (ziegler2024structuralcharacterizationand pages 1-3, ziegler2024structuralcharacterizationand pages 6-9) | CHEBI:15351 | Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662 |
| glucose | Metabolites/Cofactors | Major fermentable substrate for yeasts, Z. mobilis, and engineered systems. (hu2023metabolicengineeringof pages 1-2, zhang2023characterizationandapplication pages 2-4) | CHEBI:17234 | Hu 2023, DOI:10.3389/fbioe.2023.1135484, https://doi.org/10.3389/fbioe.2023.1135484; Zhang 2023, DOI:10.3390/ijms24065888, https://doi.org/10.3390/ijms24065888 |
| oxygen limitation / anaerobic conditions | Environmental/Experimental Factors | Condition favoring fermentative metabolism and ethanol production; contrasted with aerobic shifts in product spectrum. (yan2024thebiochemicalbasis pages 2-5, bao2023metabolicengineeringof pages 1-2) | ENVO:01001003 anaerobic environment (candidate) | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| aerobic conditions / oxygen exposure | Environmental/Experimental Factors | Alters flux away from strict ethanologenic output in some systems, including acetoin production in Z. mobilis. (bao2023metabolicengineeringof pages 1-2) | ENVO:01001002 oxygenated environment (candidate) | Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| benzoic acid | Environmental/Experimental Factors | Fermentation inhibitor in molasses that suppresses glycolysis and damages yeast membranes. (xiufeng2024responsemechanismof pages 13-15, xiufeng2024responsemechanismof pages 1-2) | CHEBI:32139 | Xiu-Feng 2024, DOI:10.1038/s41598-024-80484-1, https://doi.org/10.1038/s41598-024-80484-1 |
| reactive nitrogen species (RNS) / acidified nitrite | Environmental/Experimental Factors | Stress condition that impairs respiration and increases dependence on ethanol-fermentation genes in fungi. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, kadooka2024fungalglyceraldehyde3phosphate pages 6-8) | CHEBI:25518 nitrite; label:RNS | Kadooka 2024, DOI:10.3389/fmicb.2024.1475567, https://doi.org/10.3389/fmicb.2024.1475567 |
| high glucose / high sugar stress | Environmental/Experimental Factors | Process condition affecting transporter requirements, osmotic balance, and fermentation physiology. (zhang2023characterizationandapplication pages 2-4, vion2024influenceofyeasts pages 6-7) | label:high sugar stress | Zhang 2023, DOI:10.3390/ijms24065888, https://doi.org/10.3390/ijms24065888; Vion 2024, DOI:10.20870/oeno-one.2024.58.4.7877, https://doi.org/10.20870/oeno-one.2024.58.4.7877 |
| copper induction | Environmental/Experimental Factors | Experimental inducer used in engineered cyanobacterial expression of ethanol-pathway genes. (gao2023rewiringcarbonflow pages 2-4) | CHEBI:27363 copper ion | Gao 2023, DOI:10.3389/fmicb.2023.1211004, https://doi.org/10.3389/fmicb.2023.1211004 |
| Saccharomyces cerevisiae | Organisms/Chassis | Canonical yeast ethanologen and industrial fermentation workhorse. (yan2024thebiochemicalbasis pages 2-5, xiufeng2024responsemechanismof pages 1-2) | NCBITaxon:4932 | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Xiu-Feng 2024, DOI:10.1038/s41598-024-80484-1, https://doi.org/10.1038/s41598-024-80484-1 |
| Zymomonas mobilis | Organisms/Chassis | Natural ethanologenic bacterium with exceptionally high ethanol yield and ED-pathway flux. (frohwitter2024anewzymomonas pages 1-2, bao2023metabolicengineeringof pages 1-2) | NCBITaxon:542 | Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| Aspergillus nidulans | Organisms/Chassis | Fungal model showing stress-induced reliance on pdcA/alcC-mediated ethanol fermentation. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, kadooka2024fungalglyceraldehyde3phosphate pages 6-8) | NCBITaxon:162425 | Kadooka 2024, DOI:10.3389/fmicb.2024.1475567, https://doi.org/10.3389/fmicb.2024.1475567 |
| Clostridium thermocellum | Organisms/Chassis | Anaerobic thermophile producing ethanol via AdhE and useful for AdhE structural/containment biology. (ziegler2024structuralcharacterizationand pages 1-3, ziegler2024structuralcharacterizationand pages 3-6) | NCBITaxon:1515 | Ziegler 2024, DOI:10.1101/2024.02.16.580662, https://doi.org/10.1101/2024.02.16.580662 |
| Synechocystis sp. PCC 6803 | Organisms/Chassis | Engineered photosynthetic chassis for heterologous CO2-to-ethanol conversion. (gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 1-2) | NCBITaxon:1148 | Gao 2023, DOI:10.3389/fmicb.2023.1211004, https://doi.org/10.3389/fmicb.2023.1211004 |
| Ethanol titer | Measurements/Phenotypes | Product concentration used to quantify ethanol fermentation performance. (yan2024thebiochemicalbasis pages 7-9, gao2023rewiringcarbonflow pages 4-6) | label:ethanol titer | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Gao 2023, DOI:10.3389/fmicb.2023.1211004, https://doi.org/10.3389/fmicb.2023.1211004 |
| Ethanol yield | Measurements/Phenotypes | Fraction of theoretical carbon conversion to ethanol; key comparative phenotype. (yan2024thebiochemicalbasis pages 7-9, frohwitter2024anewzymomonas pages 1-2) | label:ethanol yield | Yan 2024, DOI:10.5376/be.2024.14.0025, https://doi.org/10.5376/be.2024.14.0025; Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9 |
| Ethanol productivity / production rate | Measurements/Phenotypes | Time-normalized ethanol output used for strain/process comparisons. (gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 6-7) | label:ethanol productivity | Gao 2023, DOI:10.3389/fmicb.2023.1211004, https://doi.org/10.3389/fmicb.2023.1211004 |
| Glucose uptake rate | Measurements/Phenotypes | High substrate uptake is a hallmark of Z. mobilis ethanologen physiology. (frohwitter2024anewzymomonas pages 5-7, frohwitter2024anewzymomonas pages 1-2) | label:glucose uptake rate | Frohwitter 2024, DOI:10.1186/s12934-024-02419-9, https://doi.org/10.1186/s12934-024-02419-9 |
| Carbon flux redirection away from ethanol | Measurements/Phenotypes | Observable phenotype in engineered strains when pdc or redox balance is perturbed. (hu2023metabolicengineeringof pages 1-2, bao2023metabolicengineeringof pages 9-11) | label:flux redistribution phenotype | Hu 2023, DOI:10.3389/fbioe.2023.1135484, https://doi.org/10.3389/fbioe.2023.1135484; Bao 2023, DOI:10.3390/fermentation9020113, https://doi.org/10.3390/fermentation9020113 |
| Growth under stress with ethanolic fermentation support | Measurements/Phenotypes | Stress-tolerance phenotype linked to intact ethanol-pathway genes under RNS or inhibitor exposure. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, xiufeng2024responsemechanismof pages 1-2) | label:stress-supported fermentative growth | Kadooka 2024, DOI:10.3389/fmicb.2024.1475567, https://doi.org/10.3389/fmicb.2024.1475567; Xiu-Feng 2024, DOI:10.1038/s41598-024-80484-1, https://doi.org/10.1038/s41598-024-80484-1 |


*Table: This table lists curation-ready candidate nodes for an ethanol fermentation TraitMech graph, grouped by biological entity type. It highlights grounded identifiers and the most relevant 2023-2024 sources supporting each node.*

---

## Evidence-backed candidate causal edges (triples)
The following table proposes evidence-backed edges with verbatim snippets, source metadata, and curation notes (including taxon specificity and engineered-vs-native flags).

| Edge (Subject → Predicate → Object) | Evidence snippet (verbatim short quote) | Source (first author year, DOI, URL) | Notes/uncertainty | Suggested identifiers (GO/ChEBI/EC/NCBITaxon where applicable) |
|---|---|---|---|---|
| pyruvate → is substrate for → pyruvate decarboxylase (PDC) reaction yielding acetaldehyde + CO2 | “Pyruvate is decarboxylated to acetaldehyde by pyruvate decarboxylase (PDC), releasing CO2” (yan2024thebiochemicalbasis pages 2-5) | Yan 2024. DOI: 10.5376/be.2024.14.0025. https://doi.org/10.5376/be.2024.14.0025 | Core canonical alcoholic fermentation step; broad but review-level evidence. | CHEBI:15361 pyruvate; EC:4.1.1.1 pyruvate decarboxylase; CHEBI:15343 acetaldehyde; CHEBI:16526 carbon dioxide |
| pyruvate decarboxylase activity → causally contributes to → ethanol fermentation pathway flux | “PDC is the key enzyme converting pyruvate to acetaldehyde” (frohwitter2024anewzymomonas pages 1-2) | Frohwitter 2024. DOI: 10.1186/s12934-024-02419-9. https://doi.org/10.1186/s12934-024-02419-9 | Strong for Zymomonas mobilis; taxon-specific wording but mechanistically generalizable. | EC:4.1.1.1; NCBITaxon:542 Zymomonas mobilis |
| acetaldehyde → is reduced by → alcohol dehydrogenase (ADH) to ethanol | “acetaldehyde is reduced to ethanol by alcohol dehydrogenase (ADH)” (yan2024thebiochemicalbasis pages 2-5) | Yan 2024. DOI: 10.5376/be.2024.14.0025. https://doi.org/10.5376/be.2024.14.0025 | Core canonical step; review evidence. | CHEBI:15343 acetaldehyde; EC:1.1.1.1 alcohol dehydrogenase; CHEBI:16236 ethanol |
| alcohol dehydrogenase reaction → regenerates → NAD+ from NADH | “regenerating NAD+ from NADH to sustain glycolysis” (yan2024thebiochemicalbasis pages 2-5) | Yan 2024. DOI: 10.5376/be.2024.14.0025. https://doi.org/10.5376/be.2024.14.0025 | Central redox-conservation edge; broad review-level support. | CHEBI:57945 NADH; CHEBI:57540 NAD+; GO:0004022 alcohol dehydrogenase (NAD) activity |
| ethanol production pathway in Zymomonas mobilis → is dominated by → pdc-dependent pyruvate decarboxylation | “the native pdc promoter was replaced with an IPTG-inducible PT7A1, enabling controllable pdc expression” and “pdc is widely considered essential” (frohwitter2024anewzymomonas pages 1-2) | Frohwitter 2024. DOI: 10.1186/s12934-024-02419-9. https://doi.org/10.1186/s12934-024-02419-9 | Strongly supported for Z. mobilis; essentiality should be curated as taxon-specific and context-dependent. | gene:pdc (label only); EC:4.1.1.1; NCBITaxon:542 |
| decreased pdc activity in Zymomonas mobilis → redirects carbon flux away from → ethanol and toward alternative pyruvate products | “lactate production… reached 173.6 ± 2.2 mM… while ethanol was reduced to ~18% of theoretical” (frohwitter2024anewzymomonas pages 5-7) | Frohwitter 2024. DOI: 10.1186/s12934-024-02419-9. https://doi.org/10.1186/s12934-024-02419-9 | Strong experimental edge for flux redirection; taxon- and engineering-specific. | gene:pdc (label only); CHEBI:24996 lactate; CHEBI:16236 ethanol; NCBITaxon:542 |
| CRISPRi repression of pdc in Zymomonas mobilis → increases → acetoin production | “CRISPRi of pdc… increased acetoin by 11.24% and decreased ethanol by 15.57%” (bao2023metabolicengineeringof pages 9-11) | Bao 2023. DOI: 10.3390/fermentation9020113. https://doi.org/10.3390/fermentation9020113 | Engineering perturbation evidence; not a native ecological edge. | gene:pdc (label only); CHEBI:15688 acetoin; CHEBI:16236 ethanol; NCBITaxon:542 |
| ZMO1360 (Pdc) → participates in → ethanol production in Zymomonas mobilis | “Pdc (ZMO1360) and alcohol dehydrogenase B as AdhB (ZMO1596)” (zhang2023characterizationandapplication pages 2-4) | Zhang 2023. DOI: 10.3390/ijms24065888. https://doi.org/10.3390/ijms24065888 | Locus-tag grounding for candidate node; pathway participation rather than direct catalytic quote. | gene:ZMO1360 (label only); EC:4.1.1.1; NCBITaxon:542 |
| ZMO1596 (AdhB) → participates in → ethanol production in Zymomonas mobilis | “Pdc (ZMO1360) and alcohol dehydrogenase B as AdhB (ZMO1596)” (zhang2023characterizationandapplication pages 2-4) | Zhang 2023. DOI: 10.3390/ijms24065888. https://doi.org/10.3390/ijms24065888 | Good taxon-specific grounding for AdhB node. | gene:ZMO1596 (label only); EC:1.1.1.1; NCBITaxon:542 |
| AdhE (bifunctional aldehyde/alcohol dehydrogenase) → catalyzes → acetyl-CoA to acetaldehyde and acetaldehyde to ethanol | “AdhE is the key bifunctional enzyme… with ALDH reducing acetyl-CoA to acetaldehyde and ADH reducing acetaldehyde to ethanol” (ziegler2024structuralcharacterizationand pages 1-3) | Ziegler 2024. DOI: 10.1101/2024.02.16.580662. https://doi.org/10.1101/2024.02.16.580662 | Important boundary case: acetyl-CoA-linked ethanol formation in many anaerobic bacteria, not the strict PDC route. Mark as related/alternative mechanism. | gene:adhE (label only); EC:1.2.1.10 aldehyde dehydrogenase (acylating); EC:1.1.1.1 alcohol dehydrogenase; CHEBI:15343 acetaldehyde; CHEBI:15351 acetyl-CoA |
| extended AdhE spirosome conformation → channels/contains → acetaldehyde intermediate | “the extended spirosome presents an entirely enclosed channel” (ziegler2024structuralcharacterizationand pages 11-12) | Ziegler 2024. DOI: 10.1101/2024.02.16.580662. https://doi.org/10.1101/2024.02.16.580662 | Mechanistic structural edge; strong for Clostridium thermocellum AdhE, not universal to all ethanologens. | gene:adhE (label only); CHEBI:15343 acetaldehyde; NCBITaxon:1515 Clostridium thermocellum |
| heterologous pdc + yqhD in Synechocystis PCC 6803 → enables → CO2-to-ethanol production | “engineered Synechocystis sp. PCC 6803 to convert atmospheric CO2 to ethanol by introducing the two heterologous enzymes pyruvate decarboxylase (PDC) and alcohol dehydrogenase (ADH)” (gao2023rewiringcarbonflow pages 1-2) | Gao 2023. DOI: 10.3389/fmicb.2023.1211004. https://doi.org/10.3389/fmicb.2023.1211004 | Strong engineered-implementation edge; not native trait of Synechocystis. | gene:pdc (heterologous, label only); gene:yqhD (label only); CHEBI:16526 carbon dioxide; CHEBI:16236 ethanol; NCBITaxon:1148 Synechocystis sp. PCC 6803 |
| rewiring malate-to-pyruvate/NADPH balance in engineered Synechocystis → promotes → acetaldehyde conversion into ethanol | “created NADPH balance and promoted acetaldehyde conversion into ethanol” (gao2023rewiringcarbonflow pages 1-2) | Gao 2023. DOI: 10.3389/fmicb.2023.1211004. https://doi.org/10.3389/fmicb.2023.1211004 | Useful for application notes; engineered photosynthetic system, indirect edge. | CHEBI:15343 acetaldehyde; CHEBI:16236 ethanol; CHEBI:57783 NADPH; NCBITaxon:1148 |
| benzoic acid stress in Saccharomyces cerevisiae → downregulates → PDC6/glycolysis-associated expression | “HXK1, PYK2, TDH1 and PDC6 showed decreased expression (PDC6 log2 FC −3.80” (xiufeng2024responsemechanismof pages 13-15) | Xiu-Feng 2024. DOI: 10.1038/s41598-024-80484-1. https://doi.org/10.1038/s41598-024-80484-1 | Strong stress-response edge; note PDC6 is one pyruvate decarboxylase isozyme/gene context in yeast. | CHEBI:32139 benzoic acid; gene:PDC6 (label only); NCBITaxon:4932 Saccharomyces cerevisiae |
| benzoic acid stress in Saccharomyces cerevisiae → inhibits → glycolysis and ethanol fermentation efficiency | “benzoic acid inhibited glycolysis and reduced sugar uptake and ATP supply” (xiufeng2024responsemechanismof pages 17-18) | Xiu-Feng 2024. DOI: 10.1038/s41598-024-80484-1. https://doi.org/10.1038/s41598-024-80484-1 | Phenotype-level stress edge; direct readout but not specific to PDC/ADH alone. | CHEBI:32139 benzoic acid; GO:0006096 glycolytic process; NCBITaxon:4932 |
| reactive nitrogen species stress → increases requirement for → pdcA-dependent ethanolic fermentation for growth | “deletion mutants lacking pdcA… show retarded growth under acidified nitrite” (kadooka2024fungalglyceraldehyde3phosphate pages 5-6) | Kadooka 2024. DOI: 10.3389/fmicb.2024.1475567. https://doi.org/10.3389/fmicb.2024.1475567 | Strong but taxon-specific to Aspergillus nidulans stress adaptation. | gene:pdcA (label only); CHEBI:25518 nitrite; NCBITaxon:162425 Aspergillus nidulans |
| reactive nitrogen species stress → increases requirement for → alcC/alcohol dehydrogenase-dependent ethanolic fermentation for growth | “deletion mutants lacking… alcC show retarded growth under acidified nitrite” (kadooka2024fungalglyceraldehyde3phosphate pages 5-6) | Kadooka 2024. DOI: 10.3389/fmicb.2024.1475567. https://doi.org/10.3389/fmicb.2024.1475567 | Strong but taxon-specific to Aspergillus nidulans under RNS stress. | gene:alcC (label only); EC:1.1.1.1; CHEBI:25518 nitrite; NCBITaxon:162425 |
| reactive nitrogen species stress → shifts metabolism toward → glycolysis and ethanol fermentation when respiration is impaired | “RNS-induced mitochondrial dysfunction… is suggested to increase reliance on glycolysis and ethanolic fermentation” (kadooka2024fungalglyceraldehyde3phosphate pages 5-6) | Kadooka 2024. DOI: 10.3389/fmicb.2024.1475567. https://doi.org/10.3389/fmicb.2024.1475567 | Mechanistic interpretation supported by mutant phenotypes; somewhat inferential, mark uncertain/moderate. | GO:0006096 glycolytic process; GO:0006113 fermentation; NCBITaxon:162425 |
| ethanol formation in Zymomonas mobilis → contributes to → NADH/NAD+ and electron balancing | “ethanol formation as serving NADH/NAD+ and electron balancing” (ahmadpanah2023metabolicregulationboosts pages 2-3) | Ahmadpanah 2023. DOI: 10.1038/s41598-023-47846-7. https://doi.org/10.1038/s41598-023-47846-7 | Supports redox role of trait; modeling/engineering context. | CHEBI:57945 NADH; CHEBI:57540 NAD+; NCBITaxon:542 |


*Table: This table compiles evidence-backed causal edges for curating the microbial trait ethanol fermentation, including the core pathway, taxon-specific variants, engineering evidence, and stress-dependent modulation. It is designed to support TraitMech node/edge selection with quotations, citations, uncertainty notes, and ontology grounding suggestions.*

---

## Warnings / claims not yet ready for TraitMech curation
1. **pdc “essentiality”** in *Z. mobilis* is described as “widely considered essential” and deletion attempts may fail due to polyploidy; curate as **taxon- and context-specific**, not universal. (frohwitter2024anewzymomonas pages 1-2, frohwitter2024anewzymomonas pages 5-7)
2. **Engineered modules (heterologous PDC/ADH in cyanobacteria)** demonstrate causal sufficiency for ethanol synthesis but do **not** imply the native cyanobacterium has the ethanol fermentation trait; curate as **application/engineering edges** or as evidence of mechanistic module transferability. (gao2023rewiringcarbonflow pages 1-2)
3. **Stress-induced metabolic shifts** (RNS → “increased reliance on glycolysis and ethanolic fermentation”) include interpretive statements; where possible, prefer direct phenotype evidence (e.g., deletion mutants) over narrative inference. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6)
4. The Yan 2024 review is useful for canonical pathway definitions and industrial context but provides limited gene-level locus grounding; treat as **high-level mechanistic support**, supplemented by primary studies for gene identifiers and quantitative edges. (yan2024thebiochemicalbasis pages 2-5, yan2024thebiochemicalbasis pages 7-9)

---

## DOI-first bibliography (with publication month/year and URLs)
- **Yan S. (Jan 2024).** *The Biochemical Basis of Ethanol Fermentation and Its Industrial Applications.* DOI:10.5376/be.2024.14.0025. https://doi.org/10.5376/be.2024.14.0025 (yan2024thebiochemicalbasis pages 2-5, yan2024thebiochemicalbasis pages 1-2, yan2024thebiochemicalbasis pages 7-9)
- **Frohwitter J, Behrendt G, Klamt S, Bettenbrock K. (May 2024).** *A new Zymomonas mobilis platform strain for the efficient production of chemicals.* *Microbial Cell Factories.* DOI:10.1186/s12934-024-02419-9. https://doi.org/10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 5-7, frohwitter2024anewzymomonas pages 1-2)
- **Hu M, Bao W, Peng Q, et al. (Feb 2023).** *Metabolic engineering of Zymomonas mobilis for co-production of D-lactic acid and ethanol using waste feedstocks of molasses and corncob residue hydrolysate.* *Frontiers in Bioengineering and Biotechnology.* DOI:10.3389/fbioe.2023.1135484. https://doi.org/10.3389/fbioe.2023.1135484 (hu2023metabolicengineeringof pages 1-2)
- **Bao W, Shen W, Peng Q, Du J, Yang S. (Jan 2023).** *Metabolic Engineering of Zymomonas mobilis for Acetoin Production by Carbon Redistribution and Cofactor Balance.* *Fermentation.* DOI:10.3390/fermentation9020113. https://doi.org/10.3390/fermentation9020113 (bao2023metabolicengineeringof pages 1-2, bao2023metabolicengineeringof pages 9-11)
- **Zhang K, Zhang W, Qin M, Li Y, Wang H. (Mar 2023).** *Characterization and Application of the Sugar Transporter Zmo0293 from Zymomonas mobilis.* *IJMS.* DOI:10.3390/ijms24065888. https://doi.org/10.3390/ijms24065888 (zhang2023characterizationandapplication pages 2-4)
- **Ahmadpanah H, Motamedian E, Mardanpour MM. (Nov 2023).** *Metabolic regulation boosts bioelectricity generation in Zymomonas mobilis microbial fuel cell, surpassing ethanol production.* *Scientific Reports.* DOI:10.1038/s41598-023-47846-7. https://doi.org/10.1038/s41598-023-47846-7 (ahmadpanah2023metabolicregulationboosts pages 2-3)
- **Gao E‑B, Wu J, Ye P, et al. (May 2023).** *Rewiring carbon flow in Synechocystis PCC 6803 for a high rate of CO2-to-ethanol under an atmospheric environment.* *Frontiers in Microbiology.* DOI:10.3389/fmicb.2023.1211004. https://doi.org/10.3389/fmicb.2023.1211004 (gao2023rewiringcarbonflow pages 4-6, gao2023rewiringcarbonflow pages 2-4, gao2023rewiringcarbonflow pages 1-2, gao2023rewiringcarbonflow pages 6-7)
- **Ziegler SJ, Knott BC, Gruber JN, et al. (Jun 2024).** *Structural characterization and dynamics of AdhE ultrastructures from Clostridium thermocellum show a containment strategy for toxic intermediates.* DOI:10.1101/2024.02.16.580662. https://doi.org/10.1101/2024.02.16.580662 (ziegler2024structuralcharacterizationand pages 11-12, ziegler2024structuralcharacterizationand pages 1-3, ziegler2024structuralcharacterizationand pages 9-11, ziegler2024structuralcharacterizationand pages 6-9, ziegler2024structuralcharacterizationand pages 3-6)
- **Kadooka C, Katsuki N, Masuo S, et al. (Oct 2024).** *Fungal glyceraldehyde 3-phosphate dehydrogenase GpdC maintains glycolytic mechanism against reactive nitrogen stress-induced damage.* *Frontiers in Microbiology.* DOI:10.3389/fmicb.2024.1475567. https://doi.org/10.3389/fmicb.2024.1475567 (kadooka2024fungalglyceraldehyde3phosphate pages 5-6, kadooka2024fungalglyceraldehyde3phosphate pages 6-8)
- **Long Xiu‑Feng, Xu Y‑L, Zhao X‑M. (Nov 2024).** *Response mechanism of Saccharomyces cerevisiae under benzoic acid stress in ethanol fermentation.* *Scientific Reports.* DOI:10.1038/s41598-024-80484-1. https://doi.org/10.1038/s41598-024-80484-1 (xiufeng2024responsemechanismof pages 13-15, xiufeng2024responsemechanismof pages 1-2, xiufeng2024responsemechanismof pages 17-18)
- **Vion C, Yeramian N, Hranilovic A, et al. (Oct 2024).** *Influence of yeasts on wine acidity: new insights into Saccharomyces cerevisiae.* *OENO One.* DOI:10.20870/oeno-one.2024.58.4.7877. https://doi.org/10.20870/oeno-one.2024.58.4.7877 (vion2024influenceofyeasts pages 6-7)
- **Geng K, Lin Y, Zheng X, et al. (Dec 2023).** *Enhanced Expression of Alcohol Dehydrogenase I in Pichia pastoris Reduces the Content of Acetaldehyde in Wines.* *Microorganisms.* DOI:10.3390/microorganisms12010038. https://doi.org/10.3390/microorganisms12010038 (geng2023enhancedexpressionof pages 12-14)


References

1. (yan2024thebiochemicalbasis pages 2-5): Shudan Yan. The biochemical basis of ethanol fermentation and its industrial applications. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0025, doi:10.5376/be.2024.14.0025. This article has 3 citations.

2. (ziegler2024structuralcharacterizationand pages 1-3): Samantha J. Ziegler, Brandon C. Knott, Josephine N. Gruber, Neal N. Hengge, Qi Xu, Daniel G. Olson, Eduardo E. Romero, Lydia M. Joubert, and Yannick J. Bomble. Structural characterization and dynamics of adhe ultrastructures from clostridium thermocellum show a containment strategy for toxic intermediates. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.16.580662, doi:10.1101/2024.02.16.580662. This article has 2 citations and is from a domain leading peer-reviewed journal.

3. (bao2023metabolicengineeringof pages 9-11): Weiwei Bao, Wei Shen, Qiqun Peng, Jun Du, and Shihui Yang. Metabolic engineering of zymomonas mobilis for acetoin production by carbon redistribution and cofactor balance. Fermentation, 9:113, Jan 2023. URL: https://doi.org/10.3390/fermentation9020113, doi:10.3390/fermentation9020113. This article has 22 citations.

4. (gao2023rewiringcarbonflow pages 1-2): E-Bin Gao, Junhua Wu, Penglin Ye, Haiyan Qiu, Huayou Chen, and Zhen Fang. Rewiring carbon flow in synechocystis pcc 6803 for a high rate of co2-to-ethanol under an atmospheric environment. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1211004, doi:10.3389/fmicb.2023.1211004. This article has 15 citations and is from a peer-reviewed journal.

5. (ziegler2024structuralcharacterizationand pages 11-12): Samantha J. Ziegler, Brandon C. Knott, Josephine N. Gruber, Neal N. Hengge, Qi Xu, Daniel G. Olson, Eduardo E. Romero, Lydia M. Joubert, and Yannick J. Bomble. Structural characterization and dynamics of adhe ultrastructures from clostridium thermocellum show a containment strategy for toxic intermediates. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.16.580662, doi:10.1101/2024.02.16.580662. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (frohwitter2024anewzymomonas pages 1-2): Jonas Frohwitter, Gerrich Behrendt, Steffen Klamt, and Katja Bettenbrock. A new zymomonas mobilis platform strain for the efficient production of chemicals. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02419-9, doi:10.1186/s12934-024-02419-9. This article has 9 citations and is from a peer-reviewed journal.

7. (frohwitter2024anewzymomonas pages 5-7): Jonas Frohwitter, Gerrich Behrendt, Steffen Klamt, and Katja Bettenbrock. A new zymomonas mobilis platform strain for the efficient production of chemicals. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02419-9, doi:10.1186/s12934-024-02419-9. This article has 9 citations and is from a peer-reviewed journal.

8. (hu2023metabolicengineeringof pages 1-2): Mimi Hu, Weiwei Bao, Qiqun Peng, Wei Hu, Xinyu Yang, Yan Xiang, Xiongying Yan, Mian Li, Ping Xu, Qiaoning He, and Shihui Yang. Metabolic engineering of zymomonas mobilis for co-production of d-lactic acid and ethanol using waste feedstocks of molasses and corncob residue hydrolysate. Frontiers in Bioengineering and Biotechnology, Feb 2023. URL: https://doi.org/10.3389/fbioe.2023.1135484, doi:10.3389/fbioe.2023.1135484. This article has 33 citations.

9. (zhang2023characterizationandapplication pages 2-4): Kun Zhang, Wenwen Zhang, Mengxing Qin, Yi Li, and Hailei Wang. Characterization and application of the sugar transporter zmo0293 from zymomonas mobilis. International Journal of Molecular Sciences, 24:5888, Mar 2023. URL: https://doi.org/10.3390/ijms24065888, doi:10.3390/ijms24065888. This article has 6 citations.

10. (gao2023rewiringcarbonflow pages 4-6): E-Bin Gao, Junhua Wu, Penglin Ye, Haiyan Qiu, Huayou Chen, and Zhen Fang. Rewiring carbon flow in synechocystis pcc 6803 for a high rate of co2-to-ethanol under an atmospheric environment. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1211004, doi:10.3389/fmicb.2023.1211004. This article has 15 citations and is from a peer-reviewed journal.

11. (gao2023rewiringcarbonflow pages 2-4): E-Bin Gao, Junhua Wu, Penglin Ye, Haiyan Qiu, Huayou Chen, and Zhen Fang. Rewiring carbon flow in synechocystis pcc 6803 for a high rate of co2-to-ethanol under an atmospheric environment. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1211004, doi:10.3389/fmicb.2023.1211004. This article has 15 citations and is from a peer-reviewed journal.

12. (gao2023rewiringcarbonflow pages 6-7): E-Bin Gao, Junhua Wu, Penglin Ye, Haiyan Qiu, Huayou Chen, and Zhen Fang. Rewiring carbon flow in synechocystis pcc 6803 for a high rate of co2-to-ethanol under an atmospheric environment. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1211004, doi:10.3389/fmicb.2023.1211004. This article has 15 citations and is from a peer-reviewed journal.

13. (kadooka2024fungalglyceraldehyde3phosphate pages 5-6): Chihiro Kadooka, Nozomi Katsuki, Shunsuke Masuo, Saito Kojima, Madoka Amahisa, Kouta Suzuki, Yuki Doi, Norio Takeshita, and Naoki Takaya. Fungal glyceraldehyde 3-phosphate dehydrogenase gpdc maintains glycolytic mechanism against reactive nitrogen stress-induced damage. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1475567, doi:10.3389/fmicb.2024.1475567. This article has 1 citations and is from a peer-reviewed journal.

14. (xiufeng2024responsemechanismof pages 13-15): Long Xiu-Feng, Xu Yu-Lei, and Zhao Xue-Mei. Response mechanism of saccharomyces cerevisiae under benzoic acid stress in ethanol fermentation. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80484-1, doi:10.1038/s41598-024-80484-1. This article has 7 citations and is from a peer-reviewed journal.

15. (xiufeng2024responsemechanismof pages 17-18): Long Xiu-Feng, Xu Yu-Lei, and Zhao Xue-Mei. Response mechanism of saccharomyces cerevisiae under benzoic acid stress in ethanol fermentation. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80484-1, doi:10.1038/s41598-024-80484-1. This article has 7 citations and is from a peer-reviewed journal.

16. (yan2024thebiochemicalbasis pages 7-9): Shudan Yan. The biochemical basis of ethanol fermentation and its industrial applications. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0025, doi:10.5376/be.2024.14.0025. This article has 3 citations.

17. (geng2023enhancedexpressionof pages 12-14): Kun Geng, Ying Lin, Xueyun Zheng, Cheng Li, Shuting Chen, He Ling, Jun Yang, Xiangyu Zhu, and Shuli Liang. Enhanced expression of alcohol dehydrogenase i in pichia pastoris reduces the content of acetaldehyde in wines. Microorganisms, 12:38, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010038, doi:10.3390/microorganisms12010038. This article has 9 citations.

18. (yan2024thebiochemicalbasis pages 1-2): Shudan Yan. The biochemical basis of ethanol fermentation and its industrial applications. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0025, doi:10.5376/be.2024.14.0025. This article has 3 citations.

19. (bao2023metabolicengineeringof pages 1-2): Weiwei Bao, Wei Shen, Qiqun Peng, Jun Du, and Shihui Yang. Metabolic engineering of zymomonas mobilis for acetoin production by carbon redistribution and cofactor balance. Fermentation, 9:113, Jan 2023. URL: https://doi.org/10.3390/fermentation9020113, doi:10.3390/fermentation9020113. This article has 22 citations.

20. (geng2023enhancedexpressionof pages 15-16): Kun Geng, Ying Lin, Xueyun Zheng, Cheng Li, Shuting Chen, He Ling, Jun Yang, Xiangyu Zhu, and Shuli Liang. Enhanced expression of alcohol dehydrogenase i in pichia pastoris reduces the content of acetaldehyde in wines. Microorganisms, 12:38, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010038, doi:10.3390/microorganisms12010038. This article has 9 citations.

21. (kadooka2024fungalglyceraldehyde3phosphate pages 6-8): Chihiro Kadooka, Nozomi Katsuki, Shunsuke Masuo, Saito Kojima, Madoka Amahisa, Kouta Suzuki, Yuki Doi, Norio Takeshita, and Naoki Takaya. Fungal glyceraldehyde 3-phosphate dehydrogenase gpdc maintains glycolytic mechanism against reactive nitrogen stress-induced damage. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1475567, doi:10.3389/fmicb.2024.1475567. This article has 1 citations and is from a peer-reviewed journal.

22. (ziegler2024structuralcharacterizationand pages 6-9): Samantha J. Ziegler, Brandon C. Knott, Josephine N. Gruber, Neal N. Hengge, Qi Xu, Daniel G. Olson, Eduardo E. Romero, Lydia M. Joubert, and Yannick J. Bomble. Structural characterization and dynamics of adhe ultrastructures from clostridium thermocellum show a containment strategy for toxic intermediates. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.16.580662, doi:10.1101/2024.02.16.580662. This article has 2 citations and is from a domain leading peer-reviewed journal.

23. (xiufeng2024responsemechanismof pages 1-2): Long Xiu-Feng, Xu Yu-Lei, and Zhao Xue-Mei. Response mechanism of saccharomyces cerevisiae under benzoic acid stress in ethanol fermentation. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80484-1, doi:10.1038/s41598-024-80484-1. This article has 7 citations and is from a peer-reviewed journal.

24. (vion2024influenceofyeasts pages 6-7): Charlotte Vion, Nadine Yeramian, Ana Hranilovic, Isabelle Masneuf-Pomarède, and Philippe Marullo. Influence of yeasts on wine acidity: new insights into saccharomyces cerevisiae. OENO One, Oct 2024. URL: https://doi.org/10.20870/oeno-one.2024.58.4.7877, doi:10.20870/oeno-one.2024.58.4.7877. This article has 34 citations.

25. (ziegler2024structuralcharacterizationand pages 3-6): Samantha J. Ziegler, Brandon C. Knott, Josephine N. Gruber, Neal N. Hengge, Qi Xu, Daniel G. Olson, Eduardo E. Romero, Lydia M. Joubert, and Yannick J. Bomble. Structural characterization and dynamics of adhe ultrastructures from clostridium thermocellum show a containment strategy for toxic intermediates. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.16.580662, doi:10.1101/2024.02.16.580662. This article has 2 citations and is from a domain leading peer-reviewed journal.

26. (ahmadpanah2023metabolicregulationboosts pages 2-3): Hananeh Ahmadpanah, Ehsan Motamedian, and Mohammad Mahdi Mardanpour. Metabolic regulation boosts bioelectricity generation in zymomonas mobilis microbial fuel cell, surpassing ethanol production. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47846-7, doi:10.1038/s41598-023-47846-7. This article has 3 citations and is from a peer-reviewed journal.

27. (ziegler2024structuralcharacterizationand pages 9-11): Samantha J. Ziegler, Brandon C. Knott, Josephine N. Gruber, Neal N. Hengge, Qi Xu, Daniel G. Olson, Eduardo E. Romero, Lydia M. Joubert, and Yannick J. Bomble. Structural characterization and dynamics of adhe ultrastructures from clostridium thermocellum show a containment strategy for toxic intermediates. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.16.580662, doi:10.1101/2024.02.16.580662. This article has 2 citations and is from a domain leading peer-reviewed journal.