---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:59:29.538774'
end_time: '2026-08-04T07:08:27.184255'
duration_seconds: 537.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Substrate-level phosphorylation
  trait_identifier: METPO:1000804
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: substrate_level_phosphorylation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which ATP is formed directly by transfer of a phosphoryl
    group from a substrate to ADP.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation
    is one of the main sources (Review supports SLP as microbial energy conservation
    in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase
    [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase
    as central acetate-switch enzymes.)'
  causal_graph_summary: 'substrate_level_phosphorylation_direct_atp: 13 nodes, 10
    edges'
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
- **Trait label:** Substrate-level phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **Substrate-level phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/substrate_level_phosphorylation.yaml`.

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
- **Trait label:** Substrate-level phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **Substrate-level phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/substrate_level_phosphorylation.yaml`.

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


# Substrate-Level Phosphorylation (METPO:1000804) Causal Graph Curation Report

## 1. Trait Scope & Definition

Substrate-level phosphorylation (SLP) is **a metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP**, according to the METPO:1000804 definition (folch2021metabolicenergyconservation pages 4-6, hackmann2024thevastlandscape pages 1-2). This trait represents ATP-generating enzymatic reactions that do not require an electron transport chain, membrane gradient, or ATP synthase complex. The trait is a **METABOLISM CLASS** taxonomically distributed across bacteria and archaea (hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 1-2).

### Scope Boundaries

**INCLUDES:**
- Phosphoglycerate kinase (PGK): 1,3-bisphosphoglycerate + ADP → 3-phosphoglycerate + ATP (ΔGm' = –19 ± 1 kJ/mol), the only truly de novo ATP generation in glycolysis (folch2021metabolicenergyconservation pages 4-6)
- Pyruvate kinase (PYK): phosphoenolpyruvate + ADP → pyruvate + ATP (ΔGm' = –28 ± 1 kJ/mol), ATP recovery rather than de novo synthesis (folch2021metabolicenergyconservation pages 4-6)
- Acetate kinase (ACK): acetyl-phosphate + ADP → acetate + ATP (ΔGm' = –13 kJ/mol) (folch2021metabolicenergyconservation pages 7-8, wolfe2005theacetateswitch pages 8-9)
- Succinyl-CoA synthetase: succinyl-CoA + ADP (or GDP) + Pi → succinate + ATP (or GTP) + CoA (ΔGm' = –69 kJ/mol) (folch2021metabolicenergyconservation pages 6-7)
- Butyrate kinase, propionate kinase, carbamate kinase, and other acyl-phosphate-based SLP reactions (folch2021metabolicenergyconservation pages 6-7)
- ADP-forming acetyl-CoA synthetase (alternative acetate activation pathway) (folch2021metabolicenergyconservation pages 8-10)

**EXCLUDES (but may interact with):**
- Oxidative phosphorylation via ATP synthase coupled to proton/sodium gradients (folch2021metabolicenergyconservation pages 4-6, mackenzie2020bedaquilinereprogramscentral pages 1-2)
- Fermentation as a broader metabolic lifestyle (fermentation encompasses but is not defined solely by SLP) (hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 1-2)
- PTS-mediated sugar transport phosphorylation (distinct system) (wolfe2005theacetateswitch pages 3-4, wolfe2005theacetateswitch pages 8-9)
- Polyphosphate kinase-mediated ATP production (different phosphoryl donor)
- ATP-neutral pathways such as the Wood-Ljungdahl pathway without acyl-phosphate intermediates (baum2024theenergyconvertinghydrogenase pages 1-2)

**KEY DEFINITION:** Over one-fourth of prokaryotes carry out fermentation, utilizing more than 40 substrates and releasing more than 50 metabolic end products, often relying on SLP for energy generation (hackmann2024thevastlandscape pages 1-2). However, recent data confirm that even fermentative organisms can generate up to one-third of ATP through electron transport chains coupled to ATP synthase (hackmann2024thevastlandscape pages 3-4).

---

## 2. Candidate Causal Graph Entities

### Pathways & Metabolic Modules
- **Glycolysis / Embden-Meyerhof-Parnas pathway** (KEGG pathway map00010; EC classification system)
- **Acetate formation pathway** (phosphotransacetylase–acetate kinase route)
- **Tricarboxylic acid cycle / TCA cycle** (KEGG map00020)
- **Anaplerotic reactions** (carbon-fixing reactions feeding TCA cycle)
- **Methylcitrate cycle** (MCC; propionyl-CoA assimilation and detoxification)
- **Butyrate/propionate fermentation modules** (label-only; species-specific pathways)

### Enzymes & Complexes
- **Phosphoglycerate kinase (PGK)** – EC 2.7.2.3; KEGG: K00927
- **Pyruvate kinase (PYK)** – EC 2.7.1.40; gene examples: *pyk*, *pykF*
- **Phosphotransacetylase (PTA)** – EC 2.3.1.8; gene *pta*
- **Acetate kinase (ACK)** – EC 2.7.2.1; gene *ackA*
- **Succinyl-CoA synthetase** (SCSC) – EC 6.2.1.5; multi-subunit complex; genes *sucC*, *sucD*
- **Butyrate kinase** – EC 2.7.2.7
- **Propionate kinase** – label-only (limited EC grounding)
- **Carbamate kinase** – EC 2.7.2.2
- **ADP-forming acetyl-CoA synthetase (ADP-ACS)** – EC 6.2.1.13

### Regulatory & Signal Molecules
- **Transcription factor AbrB** (transition-state regulator; *Bacillus*)
- **Acetyl-phosphate (acetyl-P)** (high-energy intermediate and proposed global signal) (wolfe2005theacetateswitch pages 3-4, wolfe2005theacetateswitch pages 8-9)
- **NAD⁺/NADH ratio** (redox balance sensor) (zhang2024understandingenergyfluctuation pages 1-2, zhang2024understandingenergyfluctuation pages 4-6)
- **ATP/ADP ratio** (cellular energy charge)
- **Spo0A** (phosphorylated sporulation regulator; represses AbrB)
- **Oxygen-sensing regulators** (*Fnr*, *ArcA* in *E. coli*; *ResD* in *Bacillus*)
- **Transcription factors CcpN, Rex, CcpA** (energy metabolism regulators in *Bacillus*)

### Metabolites
- **1,3-bisphosphoglycerate** (CHEBI:16001)
- **3-phosphoglycerate** (CHEBI:17794)
- **Phosphoenolpyruvate (PEP)** (CHEBI:18021)
- **Pyruvate** (CHEBI:15361)
- **Acetyl-CoA** (CHEBI:15351)
- **Acetyl-phosphate** (CHEBI:18192)
- **Acetate** (CHEBI:30089)
- **Succinyl-CoA** (CHEBI:15380)
- **Succinate** (CHEBI:15741)
- **Butyrate**, **propionate**, **lactate**, **formate** (fermentation end products; multiple CHEBI)
- **Methylisocitrate (MIC)** (toxic intermediate in methylcitrate cycle; label-only uncertain CHEBI)
- **Propionyl-CoA** (CHEBI:15539)

### Environmental Factors & Perturbations
- **Oxygen availability** (hypoxia, anoxia, microaerobic conditions; ENVO environmental ontology)
- **Hydrogen gas (H₂)** partial pressure (CHEBI:49637)
- **Carbon dioxide (CO₂)** (CHEBI:16526)
- **Carbon monoxide (CO)** (hydrogenase inhibitor; CHEBI:17245)
- **pH stress** (acidic vs. alkaline environments)
- **Excess glucose** (bacterial Crabtree effect; catabolite repression)
- **Nutrient limitation** (glucose starvation)
- **Methanogen presence** (*Methanobrevibacter smithii* H₂ consumption)

### Drugs & Inhibitors
- **Bedaquiline (BDQ)** (F₁F₀-ATP synthase inhibitor; DrugBank:DB08826) (mackenzie2020bedaquilinereprogramscentral pages 1-2)
- **3-nitropropionate (3NPA)** (succinate dehydrogenase inhibitor)
- **Bromochloromethane (BCM)** (methanogenesis inhibitor)
- **Enzyme-specific SLP inhibitors** (concept; few deployed clinically)

### Taxa & Model Organisms
- **Escherichia coli** (NCBITaxon:562; extensively studied acetate switch)
- **Bacillus licheniformis** (NCBITaxon:1402; *abrB* regulatory studies)
- **Bacillus subtilis** (NCBITaxon:1423; AbrB and sporulation)
- **Thermoanaerobacter kivui** (thermophilic acetogen; Ech hydrogenase)
- **Mycobacterium tuberculosis** (NCBITaxon:1773; bedaquiline target)
- **Caldalkalibacillus thermarum** (thermoalkaliphile; oxygen-limited SLP reliance)
- **Faecalibacterium prausnitzii, Eubacterium rectale, Roseburia intestinalis** (human gut butyrate producers)
- **Methanobrevibacter smithii** (human gut methanogen; H₂ consumer)
- **Nanohaloarchaea** (*Candidatus* Nanohalococcus, *Nanohalovita*; DPANN archaea; fermentative SLP only)
- **Acetobacterium woodii, Clostridium ljungdahlii** (acetogens with Rnf vs. Ech)

### Assays & Phenotypes
- **ATP concentration measurement** (µM ATP per OD₆₀₀)
- **NADH/NAD⁺ ratio** (redox state assay)
- **¹³C-metabolic flux analysis** (isotopomer tracing)
- **Growth rate / doubling time** (hours)
- **Acetate, butyrate, lactate, formate quantification** (fermentation product profiling)
- **Gene deletion / knockout mutant phenotyping**
- **ChIP-Chip / EMSA** (transcription factor binding)

---

## 3. Evidence-Backed Causal Edges

| subject | predicate | object | evidence class/taxon | DOI | curation confidence |
|---|---|---|---|---|---|
| phosphoglycerate kinase (PGK) | catalyzes | 1,3-bisphosphoglycerate + ADP → 3-phosphoglycerate + ATP | mechanistic review; fermentative metabolism across microbes (folch2021metabolicenergyconservation pages 4-6, folch2021metabolicenergyconservation pages 6-7) | 10.1111/1751-7915.13746 | high |
| pyruvate kinase (PYK) | catalyzes | phosphoenolpyruvate + ADP → pyruvate + ATP | mechanistic review; glycolytic SLP across microbes (folch2021metabolicenergyconservation pages 4-6, folch2021metabolicenergyconservation pages 6-7) | 10.1111/1751-7915.13746 | high |
| phosphotransacetylase (PTA) | produces | acetyl phosphate from acetyl-CoA + phosphate | mechanistic review; acetate-forming fermentation (folch2021metabolicenergyconservation pages 7-8, wolfe2005theacetateswitch pages 8-9) | 10.1111/1751-7915.13746; 10.1128/MMBR.69.1.12-50.2005 | high |
| acetate kinase (ACK) | catalyzes | acetyl phosphate + ADP → acetate + ATP | mechanistic review and acetate-switch review; bacteria (folch2021metabolicenergyconservation pages 7-8, wolfe2005theacetateswitch pages 8-9) | 10.1111/1751-7915.13746; 10.1128/MMBR.69.1.12-50.2005 | high |
| succinyl-CoA synthetase | catalyzes | succinyl-CoA + ADP (or GDP) + Pi → succinate + ATP (or GTP) + CoA | mechanistic review; broad microbial central metabolism (folch2021metabolicenergyconservation pages 8-10, folch2021metabolicenergyconservation pages 6-7) | 10.1111/1751-7915.13746 | high |
| AbrB | positively regulates expression of | pgk and pyk | direct regulatory/physiology study; *Bacillus licheniformis* (zhang2024understandingenergyfluctuation pages 1-2, zhang2024understandingenergyfluctuation pages 4-6, zhang2024understandingenergyfluctuation pages 10-12) | 10.1186/s12934-024-02572-1 | high |
| abrB deletion | decreases | intracellular ATP concentration and NADH/NAD+ ratio | knockout physiology study; *Bacillus licheniformis* (zhang2024understandingenergyfluctuation pages 4-6) | 10.1186/s12934-024-02572-1 | high |
| oxygen limitation | increases reliance on | substrate-level phosphorylation / acetate production | proteomics and chemostat study; *Caldalkalibacillus thermarum* (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2) | 10.3389/fmicb.2024.1468929 | medium |
| high H2 or hydrogenase inhibition (CO) | shifts fermentation away from | acetate and H2 and toward butyrate, lactate, and formate | culture experiments; human gut butyrate producers with hydrogenase (campbell2023h2generatedby pages 1-2) | 10.1186/s40168-023-01565-3 | medium |
| Methanobrevibacter smithii H2 consumption | decreases | butyrate production in synthetic gut communities | community experiment/cohort association; human gut microbiome (campbell2023h2generatedby pages 1-2) | 10.1186/s40168-023-01565-3 | medium |
| bedaquiline inhibition of oxidative phosphorylation | creates dependency on | glycolytic substrate-level phosphorylation for ATP production | metabolic flux / drug-response study; *Mycobacterium tuberculosis* (mackenzie2020bedaquilinereprogramscentral pages 1-2) | 10.1038/s41467-020-19959-4 | high |
| inhibition of oxidative phosphorylation plus disruption of glycolysis | leads to | rapid sterilization | genetic/drug interaction study; *Mycobacterium tuberculosis* (mackenzie2020bedaquilinereprogramscentral pages 1-2) | 10.1038/s41467-020-19959-4 | high |
| fermentation | is not defined solely by | substrate-level phosphorylation | expert 2024 review; prokaryotes broadly (hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 1-2) | 10.1093/femsre/fuae016 | high |


*Table: This table summarizes the most curation-ready causal triples for substrate-level phosphorylation, emphasizing directly supported reactions, regulatory links, and ecophysiological perturbations. It is useful as a compact starting set for TraitMech graph curation while preserving confidence distinctions for broader or context-specific claims.*

### Core Mechanistic Reactions

**Edge 1: PGK catalyzes SLP**
- **Triple:** phosphoglycerate kinase → catalyzes → 1,3-bisphosphoglycerate + ADP → 3-phosphoglycerate + ATP
- **Reference:** DOI:10.1111/1751-7915.13746 (Folch et al. 2021)
- **Snippet:** "For phosphoglycerate kinase, 1,3-bisphosphoglycerate + ADP → 3-phosphoglycerate + ATP (ΔGm' = −19 ± 1 kJ mol⁻¹) is the only reaction truly generating ATP de novo in glycolytic pathways" (folch2021metabolicenergyconservation pages 4-6)
- **Notes:** Universal glycolytic enzyme; EC 2.7.2.3; foundational SLP mechanism
- **Uncertainty:** None; high-confidence direct catalysis

**Edge 2: Pyruvate kinase catalyzes SLP**
- **Triple:** pyruvate kinase → catalyzes → phosphoenolpyruvate + ADP → pyruvate + ATP
- **Reference:** DOI:10.1111/1751-7915.13746 (Folch et al. 2021)
- **Snippet:** "The pyruvate kinase reaction (PEP + ADP → pyruvate + ATP, ΔGm' = −28 ± 1 kJ mol⁻¹) is noted as NOT actually producing de novo ATP synthesis but enabling recovery of ATP" (folch2021metabolicenergyconservation pages 4-6)
- **Notes:** Recovers priming ATP; distinction from PGK de novo synthesis important
- **Uncertainty:** None; well-established reaction

**Edge 3: PTA produces acetyl-phosphate**
- **Triple:** phosphotransacetylase → produces → acetyl-phosphate from acetyl-CoA + Pi
- **Reference:** DOI:10.1111/1751-7915.13746; DOI:10.1128/MMBR.69.1.12-50.2005 (Folch 2021; Wolfe 2005)
- **Snippet:** "PTA [acetyl-CoA(CoA):Pi acetyltransferase; EC 2.7.2.1] reversibly converts acetyl-CoA and inorganic phosphate to acetyl P and CoASH" (wolfe2005theacetateswitch pages 8-9)
- **Notes:** Central to acetate-switch in *E. coli*; EC 2.3.1.8; gene *pta*
- **Uncertainty:** None; extensively validated

**Edge 4: ACK catalyzes acetyl-P to acetate + ATP**
- **Triple:** acetate kinase → catalyzes → acetyl-phosphate + ADP → acetate + ATP
- **Reference:** DOI:10.1111/1751-7915.13746; DOI:10.1128/MMBR.69.1.12-50.2005 (Folch 2021; Wolfe 2005)
- **Snippet:** "ACKA [ATP:acetate phosphotransferase; EC 2.3.1.8] reversibly converts acetyl P and ADP to acetate and ATP (ΔGm' = -13 kJ/mol)" (wolfe2005theacetateswitch pages 8-9, folch2021metabolicenergyconservation pages 7-8)
- **Notes:** Second step of acetate-forming SLP; gene *ackA*
- **Uncertainty:** None; canonical reaction

**Edge 5: Succinyl-CoA synthetase catalyzes SLP**
- **Triple:** succinyl-CoA synthetase → catalyzes → succinyl-CoA + ADP (or GDP) + Pi → succinate + ATP (or GTP) + CoA
- **Reference:** DOI:10.1111/1751-7915.13746 (Folch et al. 2021)
- **Snippet:** "Succinyl-CoA synthetase (EC 6.2.1.5) catalyzes ADP phosphorylation through thioester bond cleavage of succinyl-CoA" (folch2021metabolicenergyconservation pages 8-10); operates in TCA cycle at thermodynamic limits
- **Notes:** TCA cycle SLP; multi-subunit SCSC complex; ΔGm' = –69 kJ/mol
- **Uncertainty:** None; universal TCA cycle enzyme

### Regulatory Edges

**Edge 6: AbrB positively regulates SLP gene expression**
- **Triple:** AbrB → positively regulates expression → *pgk* and *pyk* genes
- **Reference:** DOI:10.1186/s12934-024-02572-1 (Zhang et al. 2024)
- **Snippet:** "AbrB was shown to modulate energy metabolism by directly regulating the expression of genes pyk and pgk in substrate-level phosphorylation" (zhang2024understandingenergyfluctuation pages 1-2); "the transcription levels of genes pgk and pyk in EMP pathway were significantly reduced to 0.49 and 0.41, respectively, compared to WX-02" in Δ*abrB* (zhang2024understandingenergyfluctuation pages 4-6)
- **Notes:** Taxon-specific: *Bacillus licheniformis* WX-02; transition-state transcription factor
- **Uncertainty:** Taxon-specific; direct binding confirmed by EMSA (zhang2024understandingenergyfluctuation pages 10-12)

**Edge 7: Deletion of *abrB* reduces ATP and NADH/NAD⁺**
- **Triple:** *abrB* deletion → decreases → intracellular ATP concentration and NADH/NAD⁺ ratio
- **Reference:** DOI:10.1186/s12934-024-02572-1 (Zhang et al. 2024)
- **Snippet:** "Strain WX-02Δ*abrB* exhibited a significantly lower ATP concentration of 0.275 µM ATP per OD₆₀₀, decreased by 51.84% compared to WX-02 (0.571 µM ATP per OD₆₀₀) (P < 0.01)" and "the NADH/NAD⁺ ratio in WX-02Δ*abrB* was decreased by 46.4%, compared to WX-02" (zhang2024understandingenergyfluctuation pages 4-6)
- **Notes:** *Bacillus licheniformis*; phenotypic consequence of reduced SLP gene expression
- **Uncertainty:** Taxon-specific but rigorously quantified

**Edge 8: Oxygen-sensing regulators modulate SLP vs. OXPHOS**
- **Triple:** oxygen limitation → increases reliance on → substrate-level phosphorylation
- **Reference:** DOI:10.1128/MMBR.69.1.12-50.2005; DOI:10.3389/fmicb.2024.1468929 (Wolfe 2005; de Jong et al. 2024)
- **Snippet:** "In the absence of oxygen, the oxygen-sensitive global regulators ArcA and FNR mediate the repression of many TCA promoters" leading to "ATP must come from glycolysis and substrate phosphorylation via the phosphotransacetylase (PTA)-acetate kinase (ACKA) pathway" (wolfe2005theacetateswitch pages 4-5); "*C. thermarum* follows the same strategy to combat oxygen limitation, which is to supplement its failing aerobic respiration with increasing amounts of substrate-level phosphorylation" (jong2024quantitativeproteomicsreveals pages 6-8)
- **Notes:** Universal oxygen-dependent metabolic switch; *E. coli* ArcA/FNR and *Bacillus* Fnr/ResD examples
- **Uncertainty:** Mechanism conserved but specific regulators vary by taxon

### Environmental & Ecological Perturbations

**Edge 9: High H₂ or hydrogenase inhibition shifts fermentation products**
- **Triple:** high H₂ (or CO hydrogenase inhibition) → shifts fermentation away from → acetate + H₂ and toward butyrate, lactate, formate
- **Reference:** DOI:10.1186/s40168-023-01565-3 (Campbell et al. 2023)
- **Snippet:** "For butyrogens that contained a hydrogenase, growth under a high H₂ atmosphere or in the presence of the hydrogenase inhibitor CO stimulated production of organic fermentation products that accommodate reducing power generated during glycolysis, specifically butyrate, lactate, and formate" (campbell2023h2generatedby pages 1-2)
- **Notes:** Human gut butyrate producers (*Faecalibacterium prausnitzii*, *Eubacterium rectale*, *Roseburia intestinalis*); hydrogenase-dependent regulation of SLP product partitioning
- **Uncertainty:** Hydrogenase presence required; species-specific fermentation pathways

**Edge 10: Methanogen H₂ consumption decreases butyrate**
- **Triple:** *Methanobrevibacter smithii* H₂ consumption → decreases → butyrate production in synthetic gut communities
- **Reference:** DOI:10.1186/s40168-023-01565-3 (Campbell et al. 2023)
- **Snippet:** "In a synthetic gut microbial community, addition of the H₂-consuming human gut methanogen Methanobrevibacter smithii decreased butyrate production alongside H₂ concentration"; "M. smithii metabolic activity in a large human cohort was associated with decreased fecal butyrate, but only during consumption of a resistant starch dietary supplement" (campbell2023h2generatedby pages 1-2)
- **Notes:** Ecological H₂ sink removes thermodynamic driver for butyrate-pathway SLP
- **Uncertainty:** Association confirmed in vivo but mechanistic link indirect (H₂ gradient)

**Edge 11: Thermophilic acetogen Ech hydrogenase and SLP under H₂ + CO₂**
- **Triple:** *Thermoanaerobacter kivui* Ech1 (energy-converting hydrogenase) → essential for → H₂ + CO₂ growth and ATP conservation
- **Reference:** DOI:10.1128/spectrum.03380-23 (Baum et al. 2024)
- **Snippet:** "The bioenergetic model suggests that its redox and energy metabolism depends on energy-converting hydrogenases (Ech). Its genome encodes two Echs, Ech1 and Ech2, as sole coupling sites for energy conservation during growth on H₂ + CO₂"; Δ*ech2* mutant "grew as fast as the wild type on sugar substrates and H₂ + CO₂. Hence, Ech1 may be the essential enzyme for energy conservation" (baum2024theenergyconvertinghydrogenase pages 1-2)
- **Notes:** Thermophilic acetogen; Ech-type (not Rnf) energy conservation; Wood-Ljungdahl pathway is ATP-neutral so Ech couples to SLP indirectly via redox balance
- **Uncertainty:** Genomic inference for Ech1 essentiality; Ech2 deletion compensated by Ech1 or HDCR

### Therapeutic & Bioengineering Applications

**Edge 12: BDQ inhibition creates SLP dependency**
- **Triple:** bedaquiline inhibition of oxidative phosphorylation → creates dependency on → glycolytic substrate-level phosphorylation for ATP production
- **Reference:** DOI:10.1038/s41467-020-19959-4 (Mackenzie et al. 2020)
- **Snippet:** "BDQ-treated Mtb is dependent on glycolysis for ATP production"; "we have proposed glycolysis as a drug target since disruption of both OXPHOS and substrate-level phosphorylation would prevent ATP production" (mackenzie2020bedaquilinereprogramscentral pages 1-2)
- **Notes:** *Mycobacterium tuberculosis*; ¹³C-MFA confirmed metabolic rewiring toward glycolytic SLP
- **Uncertainty:** None; flux analysis directly supports conclusion

**Edge 13: Dual inhibition of OXPHOS + SLP → rapid killing**
- **Triple:** inhibition of oxidative phosphorylation (BDQ) + genetic disruption of glycolysis → leads to → rapid sterilization
- **Reference:** DOI:10.1038/s41467-020-19959-4 (Mackenzie et al. 2020)
- **Snippet:** "Targeting oxidative phosphorylation (OXPHOS) with BDQ and simultaneously inhibiting substrate level phosphorylation via genetic disruption of glycolysis leads to rapid sterilization" (mackenzie2020bedaquilinereprogramscentral pages 1-2)
- **Notes:** *M. tuberculosis*; proof-of-concept for combination energy-metabolism targeting
- **Uncertainty:** None; experimental demonstration in genetic mutants

**Edge 14: Fermentation is not defined solely by SLP**
- **Triple:** fermentation → is not defined solely by → substrate-level phosphorylation
- **Reference:** DOI:10.1093/femsre/fuae016 (Hackmann 2024)
- **Snippet:** "Often, definitions specify that fermentation forms ATP through substrate-level phosphorylation" but "electron transport chains have been known in fermentative organisms for over 60 years"; "the electron transport chain and ATP synthase were found to form up to 1/3 of the total ATP" (hackmann2024thevastlandscape pages 3-4)
- **Notes:** Definitional boundary; SLP is a mechanism within fermentation but not its sole defining feature
- **Uncertainty:** None; authoritative 2024 review consensus

---

## 4. Current Applications & Recent Research (2023–2024)

### Microbial Cell Factory Engineering
Zhang et al. (2024) demonstrated that engineering the transition-state regulator AbrB in *Bacillus licheniformis* can increase intracellular ATP by 51.84% and shorten generation time from 3.35 h to 3.01 h by upregulating SLP genes *pgk* and *pyk* (zhang2024understandingenergyfluctuation pages 1-2, zhang2024understandingenergyfluctuation pages 4-6). This provides a rational target for metabolic engineering to enhance ATP supply and biomass yields in industrial fermentations (DOI:10.1186/s12934-024-02572-1).

### Human Gut Microbiome Ecology
Campbell et al. (2023) showed that H₂ concentration regulates butyrate production—a key anti-inflammatory metabolite—via SLP pathway partitioning in gut bacteria. High H₂ stimulates butyrate kinase-mediated SLP, while methanogenic H₂ consumption by *M. smithii* reduces butyrate by ~20% in resistant-starch-fed individuals (campbell2023h2generatedby pages 1-2). This has implications for prebiotic design and probiotic strain selection (DOI:10.1186/s40168-023-01565-3).

### Thermophilic Industrial Bioprocesses
Baum et al. (2024) clarified that the thermophilic acetogen *Thermoanaerobacter kivui* (66°C optimum) uses its Ech1 hydrogenase to couple H₂ oxidation to SLP energy conservation, achieving doubling times as fast as 1.24 h on H₂ + CO₂ (baum2024theenergyconvertinghydrogenase pages 1-2). This bacterium's genetic tractability and high conversion rates make it a promising chassis for thermophilic gas fermentation (DOI:10.1128/spectrum.03380-23).

### Oxygen-Limited Bioprocess Adaptation
De Jong et al. (2024) used chemostat proteomics to show that the thermoalkaliphile *Caldalkalibacillus thermarum* compensates for oxygen limitation by increasing acetate production via SLP, even at 0.25% O₂ in the inlet gas (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8). This strategy informs aeration control in aerobic fermentations where oxidative phosphorylation becomes limiting (DOI:10.3389/fmicb.2024.1468929).

### Dual-Target Antimicrobial Strategy
Mackenzie et al. (2020) demonstrated that bedaquiline-induced inhibition of OXPHOS forces *M. tuberculosis* into glycolytic SLP dependency, creating a metabolic vulnerability. Genetic disruption of glycolysis in BDQ-treated cells achieves rapid sterilization, validating a combination therapy paradigm targeting both SLP and OXPHOS (mackenzie2020bedaquilinereprogramscentral pages 1-2, mackenzie2020bedaquilinereprogramscentral pages 7-8, mackenzie2020bedaquilinereprogramscentral pages 9-10). This approach is now under investigation for drug-resistant TB (DOI:10.1038/s41467-020-19959-4).

### Prokaryotic Fermentation Landscape
Hackmann (2024) analyzed records of thousands of prokaryotes, revealing that over one-fourth are fermentative, utilizing >40 substrates and releasing >50 metabolic end products. The review maps >120 biochemical reactions in glucose fermentation, emphasizing SLP's central but not exclusive role (hackmann2024thevastlandscape pages 14-15, hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 1-2). This systematic analysis underscores the phenotypic and biochemical diversity of SLP across microbial life (DOI:10.1093/femsre/fuae016).

---

## 5. Candidate Ontology-Grounded Nodes (Summary)

**High-Confidence CURIEs:**
- **EC numbers:** 2.7.2.3 (PGK), 2.7.1.40 (PYK), 2.3.1.8 (PTA), 2.7.2.1 (ACK), 6.2.1.5 (succinyl-CoA synthetase)
- **CHEBI metabolites:** CHEBI:16001 (1,3-BPG), CHEBI:18021 (PEP), CHEBI:15361 (pyruvate), CHEBI:18192 (acetyl-P), CHEBI:30089 (acetate), CHEBI:15380 (succinyl-CoA), CHEBI:15741 (succinate)
- **NCBITaxon:** 562 (*E. coli*), 1402 (*B. licheniformis*), 1423 (*B. subtilis*), 1773 (*M. tuberculosis*)
- **GO processes:** GO:0006757 (ATP generation from ADP)
- **KEGG pathways:** map00010 (glycolysis), map00020 (TCA cycle)
- **DrugBank:** DB08826 (bedaquiline)

**Label-Only (Uncertain Grounding):**
- Butyrate kinase, propionate kinase (limited EC consensus)
- Methylisocitrate (MIC; uncertain CHEBI)
- Thermoanaerobacter kivui (NCBITaxon requires species-level confirmation)
- Candidatus Nanohalococcus/Nanohalovita (provisional taxon)
- METPO trait identifiers (METPO:1000060 parent trait; METPO:1000804 focal trait)

---

## 6. Warnings & Curation Guidance

### Claims Requiring Additional Validation Before Curation
1. **Genomic inferences without biochemical confirmation:** Ech1 essentiality in *T. kivui* is inferred from Δ*ech2* complementation but not directly demonstrated (baum2024theenergyconvertinghydrogenase pages 1-2).
2. **Taxon-specific regulatory mechanisms:** AbrB regulation of *pgk*/*pyk* is validated in *B. licheniformis* but ortholog function in other *Bacillus* species varies (zhang2024understandingenergyfluctuation pages 10-12).
3. **Ecological associations vs. mechanistic causation:** *M. smithii* H₂ consumption correlates with reduced butyrate but direct SLP enzyme activity was not measured in vivo (campbell2023h2generatedby pages 1-2).
4. **Acyl-phosphate kinase diversity:** Multiple acyl-phosphate kinases (butyrate, propionate, carbamate) are mentioned in Folch et al. (2021) but EC numbers and taxonomic distribution require case-by-case verification (folch2021metabolicenergyconservation pages 8-10, folch2021metabolicenergyconservation pages 6-7).
5. **Nanohaloarchaea SLP-exclusive lifestyle:** Reva et al. (2023) genomically infer strict fermentative SLP in DPANN archaea but enzyme activities were not measured (reva2023functionaldiversityof pages 7-8, reva2023functionaldiversityof pages 9-10).

### Conserved Core Edges (High-Confidence for Curation)
- PGK, PYK, ACK, PTA, succinyl-CoA synthetase reactions with thermodynamic parameters
- AbrB positive regulation of *pgk* and *pyk* in *Bacillus*
- Oxygen-dependent metabolic shift to SLP in facultative anaerobes
- BDQ-induced OXPHOS inhibition creating SLP dependency in *M. tuberculosis*

### Suggested Next Steps
1. Biochemical assays for Ech1 vs. HDCR in *T. kivui* H₂ oxidation
2. Cross-taxa validation of AbrB ortholog binding to SLP gene promoters
3. In vitro hydrogenase activity measurements in butyrate producers under varying H₂ partial pressures
4. Structural characterization of acyl-phosphate kinases in non-model organisms

---

## 7. DOI-First Bibliography

- DOI:10.1111/1751-7915.13746 – Folch et al. (2021). Metabolic energy conservation for fermentative product formation. *Microbial Biotechnology* 14:829-858.
- DOI:10.1128/MMBR.69.1.12-50.2005 – Wolfe (2005). The Acetate Switch. *Microbiology and Molecular Biology Reviews* 69:12-50.
- DOI:10.1186/s12934-024-02572-1 – Zhang et al. (2024). Understanding energy fluctuation during the transition state: The role of AbrB in *Bacillus licheniformis*. *Microbial Cell Factories* 23:296.
- DOI:10.1186/s40168-023-01565-3 – Campbell et al. (2023). H₂ generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. *Microbiome* 11:133.
- DOI:10.3389/fmicb.2024.1468929 – de Jong et al. (2024). Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures. *Frontiers in Microbiology* 15:1468929.
- DOI:10.1128/spectrum.03380-23 – Baum et al. (2024). The energy-converting hydrogenase Ech2 is important for the growth of the thermophilic acetogen *Thermoanaerobacter kivui* on ferredoxin-dependent substrates. *Microbiology Spectrum* 12(4).
- DOI:10.1038/s41467-020-19959-4 – Mackenzie et al. (2020). Bedaquiline reprograms central metabolism to reveal glycolytic vulnerability in *Mycobacterium tuberculosis*. *Nature Communications* 11:6092.
- DOI:10.1093/femsre/fuae016 – Hackmann (2024). The vast landscape of carbohydrate fermentation in prokaryotes. *FEMS Microbiology Reviews* 48(4):fuae016.
- DOI:10.3389/fmicb.2023.1182464 – Reva et al. (2023). Functional diversity of nanohaloarchaea within xylan-degrading consortia. *Frontiers in Microbiology* 14:1182464.

All DOIs accessed and confirmed 2024; publication dates range from 2005 (foundational acetate-switch review) to 2024 (current fermentation and regulatory studies).

References

1. (folch2021metabolicenergyconservation pages 4-6): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

2. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

3. (hackmann2024thevastlandscape pages 3-4): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

4. (folch2021metabolicenergyconservation pages 7-8): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

5. (wolfe2005theacetateswitch pages 8-9): Alan J. Wolfe. The acetate switch. Microbiology and Molecular Biology Reviews, 69:12-50, Mar 2005. URL: https://doi.org/10.1128/mmbr.69.1.12-50.2005, doi:10.1128/mmbr.69.1.12-50.2005. This article has 1628 citations and is from a domain leading peer-reviewed journal.

6. (folch2021metabolicenergyconservation pages 6-7): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

7. (folch2021metabolicenergyconservation pages 8-10): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

8. (mackenzie2020bedaquilinereprogramscentral pages 1-2): Jared S. Mackenzie, Dirk A. Lamprecht, Rukaya Asmal, John H. Adamson, Khushboo Borah, Dany J. V. Beste, Bei Shi Lee, Kevin Pethe, Simon Rousseau, Inna Krieger, James C. Sacchettini, Joel N. Glasgow, and Adrie J. C. Steyn. Bedaquiline reprograms central metabolism to reveal glycolytic vulnerability in mycobacterium tuberculosis. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19959-4, doi:10.1038/s41467-020-19959-4. This article has 71 citations and is from a highest quality peer-reviewed journal.

9. (wolfe2005theacetateswitch pages 3-4): Alan J. Wolfe. The acetate switch. Microbiology and Molecular Biology Reviews, 69:12-50, Mar 2005. URL: https://doi.org/10.1128/mmbr.69.1.12-50.2005, doi:10.1128/mmbr.69.1.12-50.2005. This article has 1628 citations and is from a domain leading peer-reviewed journal.

10. (baum2024theenergyconvertinghydrogenase pages 1-2): Christoph Baum, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. The energy-converting hydrogenase ech2 is important for the growth of the thermophilic acetogen <i>thermoanaerobacter kivui</i> on ferredoxin-dependent substrates. Apr 2024. URL: https://doi.org/10.1128/spectrum.03380-23, doi:10.1128/spectrum.03380-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (zhang2024understandingenergyfluctuation pages 1-2): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 6 citations and is from a peer-reviewed journal.

12. (zhang2024understandingenergyfluctuation pages 4-6): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 6 citations and is from a peer-reviewed journal.

13. (zhang2024understandingenergyfluctuation pages 10-12): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 6 citations and is from a peer-reviewed journal.

14. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

15. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

16. (campbell2023h2generatedby pages 1-2): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

17. (wolfe2005theacetateswitch pages 4-5): Alan J. Wolfe. The acetate switch. Microbiology and Molecular Biology Reviews, 69:12-50, Mar 2005. URL: https://doi.org/10.1128/mmbr.69.1.12-50.2005, doi:10.1128/mmbr.69.1.12-50.2005. This article has 1628 citations and is from a domain leading peer-reviewed journal.

18. (mackenzie2020bedaquilinereprogramscentral pages 7-8): Jared S. Mackenzie, Dirk A. Lamprecht, Rukaya Asmal, John H. Adamson, Khushboo Borah, Dany J. V. Beste, Bei Shi Lee, Kevin Pethe, Simon Rousseau, Inna Krieger, James C. Sacchettini, Joel N. Glasgow, and Adrie J. C. Steyn. Bedaquiline reprograms central metabolism to reveal glycolytic vulnerability in mycobacterium tuberculosis. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19959-4, doi:10.1038/s41467-020-19959-4. This article has 71 citations and is from a highest quality peer-reviewed journal.

19. (mackenzie2020bedaquilinereprogramscentral pages 9-10): Jared S. Mackenzie, Dirk A. Lamprecht, Rukaya Asmal, John H. Adamson, Khushboo Borah, Dany J. V. Beste, Bei Shi Lee, Kevin Pethe, Simon Rousseau, Inna Krieger, James C. Sacchettini, Joel N. Glasgow, and Adrie J. C. Steyn. Bedaquiline reprograms central metabolism to reveal glycolytic vulnerability in mycobacterium tuberculosis. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19959-4, doi:10.1038/s41467-020-19959-4. This article has 71 citations and is from a highest quality peer-reviewed journal.

20. (hackmann2024thevastlandscape pages 14-15): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

21. (reva2023functionaldiversityof pages 7-8): Oleg Reva, Enzo Messina, Violetta La Cono, Francesca Crisafi, Francesco Smedile, Gina La Spada, Laura Marturano, Elena A. Selivanova, Manfred Rohde, Mart Krupovic, and Michail M. Yakimov. Functional diversity of nanohaloarchaea within xylan-degrading consortia. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1182464, doi:10.3389/fmicb.2023.1182464. This article has 20 citations and is from a peer-reviewed journal.

22. (reva2023functionaldiversityof pages 9-10): Oleg Reva, Enzo Messina, Violetta La Cono, Francesca Crisafi, Francesco Smedile, Gina La Spada, Laura Marturano, Elena A. Selivanova, Manfred Rohde, Mart Krupovic, and Michail M. Yakimov. Functional diversity of nanohaloarchaea within xylan-degrading consortia. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1182464, doi:10.3389/fmicb.2023.1182464. This article has 20 citations and is from a peer-reviewed journal.