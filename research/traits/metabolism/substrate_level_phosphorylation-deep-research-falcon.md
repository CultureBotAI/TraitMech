---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:55:06.246589'
end_time: '2026-06-18T06:07:38.485732'
duration_seconds: 752.24
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
  causal_graph_summary: 'substrate_level_phosphorylation_direct_atp: 9 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Substrate-level phosphorylation
- **METPO identifier:** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 9 nodes, 6 edges

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
- **METPO identifier:** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 9 nodes, 6 edges

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


## Microbial Trait Causal Graph Curation Report: Substrate-level phosphorylation (SLP)

**Target trait:** Substrate-level phosphorylation (METPO:1000804)  
**Definition (given):** “A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.”  
**Trait category:** METABOLISM; **Term kind:** CLASS

### 1) Scope summary (trait meaning, boundary cases, distinctions)

Substrate-level phosphorylation (SLP) is a microbial **ATP-conservation mechanism** in which **ATP is formed directly in an enzyme-catalyzed phosphoryl transfer**, rather than through chemiosmotic coupling via a membrane ion gradient and ATP synthase. In practice, SLP is most often discussed in the context of **fermentative metabolism** and central carbon metabolism. A recent synthesis of prokaryotic fermentation emphasizes that fermentation occurs in “environments without oxygen” and that many definitions specify ATP production by SLP (10.1093/femsre/fuae016; published online 2024-05-31). (hackmann2024thevastlandscape pages 1-2)

**Boundary cases and “nearby traits”:**
- **Fermentation vs respiration/oxidative phosphorylation:** Fermentation is often defined as catabolism with internally balanced redox where ATP is produced by SLP (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3). However, Hackmann notes electron transport chains exist in fermentative organisms and in at least one organism contributed up to “1/3 of the total ATP,” complicating a strict SLP-only definition of fermentation (hackmann2024thevastlandscape pages 2-3). Therefore, this trait should be curated as **“capacity for ATP generation via direct phosphoryl transfer steps”** rather than assuming it is the sole ATP source.
- **Electron acceptor edge cases:** Hackmann discusses cases where protons or CO2 can act as acceptors/donors in “edge cases” of fermentation definitions (hackmann2024thevastlandscape pages 2-3). For TraitMech, this motivates explicit nodes for **electron acceptor availability** and **redox balancing** rather than equating fermentation strictly with SLP.

### 2) Key concepts and definitions (current understanding)

**Fermentation as the ecological envelope for SLP:** In a 2024 FEMS Microbiology Reviews article, fermentation is framed as “life to thrive without oxygen,” releasing ATP without requiring oxygen and occurring in “the gut… sediments… and anaerobic bioreactors” (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 1-2)

**SLP as a defining ATP-generation mode in fermentation:** Multiple definitions compiled in Hackmann’s review explicitly state that ATP is synthesized “by substrate level phosphorylation” or “produced by substrate-level phosphorylation” (hackmann2024thevastlandscape pages 1-2). This directly supports treating SLP as a trait-level energy conservation mechanism that is especially relevant under anoxia.

### 3) Candidate causal graph entities (curation-oriented node list)

Below are candidate nodes grouped by type. Identifiers are suggested where stable and unambiguous from the evidence; otherwise label-only nodes are provided.

#### A. Processes / pathways / modules
- **Substrate-level phosphorylation** (METPO:1000804; also map to GO:0046034 “ATP metabolic process” as a process container) (hackmann2024thevastlandscape pages 1-2)
- **Fermentation (anaerobic catabolism)** (label; environmental/physiology context for SLP) (hackmann2024thevastlandscape pages 1-2)
- **Glycolysis payoff-phase SLP** (label; PGK/PYK steps—see warnings on evidence source) (chowdhary2023effectofsubstrate pages 17-21)
- **Acetate formation via AckA–Pta (PTA–ACK) pathway** (label; SLP-generating acetate branch) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **Alternative acetate formation modules discovered via genomics/enzymology** (label; includes SCACT/SCS and acetate—CoA ligase ADP-forming) (hackmann2024thevastlandscape pages 4-5)
- **Arginine deiminase (ADI) pathway SLP via carbamate kinase** (label; “additional SLP” in acetogens) (bae2024harnessingacetogenicbacteria pages 7-8)

#### B. Enzymes / genes / regulators
- **AckA** (acetate kinase; EC:2.7.2.1) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **Pta** (phosphotransacetylase; EC:2.3.1.8) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **ActP / SatP** (acetate transporters; label) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **ACS (acetyl-CoA synthetase / acetyl-CoA ligase)** (label) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **SCACT/SCS module**: succinyl-CoA:acetate CoA-transferase (EC:2.8.3.18) + succinyl-CoA synthetase [ADP-forming] (EC:6.2.1.5) (hackmann2024thevastlandscape pages 4-5)
- **Acetate—CoA ligase [ADP-forming]** (EC:6.2.1.13) (hackmann2024thevastlandscape pages 4-5)
- **AbrB** (transition-state regulator; Bacillus) (zhang2024understandingenergyfluctuation pages 4-6)
- **Anr (Fnr homolog)** (global anaerobic regulator; Pseudomonas/Neisseria context in review) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **IHF subunit alpha (IhfA; referred as lhfA in excerpt)** (hosmer2023bacterialacetatemetabolism pages 1-3)
- **RpoS** (stationary phase sigma factor; acetate consumption activation) (hosmer2023bacterialacetatemetabolism pages 1-3)

#### C. Metabolites / chemicals
- **ATP** (CHEBI:15422); **ADP** (CHEBI:58289) (hackmann2024thevastlandscape pages 1-2)
- **Acetate** (CHEBI:30089) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **Acetyl-CoA** (CHEBI:15351) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **Acetyl-phosphate** (CHEBI:15344) (chowdhary2023effectofsubstrate pages 17-21)
- **DMSO** (CHEBI:16382) (bae2024harnessingacetogenicbacteria pages 7-8)
- **Nitrate** (CHEBI:17632) (bae2024harnessingacetogenicbacteria pages 7-8)

#### D. Environmental / experimental factors
- **Low oxygen / anaerobiosis** (ENVO label candidate) (hackmann2024thevastlandscape pages 1-2)
- **Glucose present** (catabolite repression context) (hosmer2023bacterialacetatemetabolism pages 1-3)
- **Post-exponential growth / transition state** (growth-phase factor; AbrB, RpoS) (hosmer2023bacterialacetatemetabolism pages 1-3, zhang2024understandingenergyfluctuation pages 4-6)
- **pH-controlled bioreactor vs serum bottle** (process factor affecting nitrate benefit in acetogens) (bae2024harnessingacetogenicbacteria pages 7-8)

### 4) Evidence-backed causal edges (triples)

The following artifact provides a curation-ready edges table with evidence snippets and grounding suggestions.

| Subject node | Predicate | Object node | Mechanistic context (pathway/module) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs where available) |
|---|---|---|---|---|---|---|---|
| low oxygen / anaerobiosis | enables | fermentation | trait scope; anaerobic catabolism | “Fermentation is a type of metabolism carried out by organisms in environments without oxygen.” (hackmann2024thevastlandscape pages 1-2) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Broad scope edge; useful parent context for SLP trait. | ENVO:anaerobic environment (label), METPO:1000804, GO:0046034 |
| fermentation | produces ATP via | substrate-level phosphorylation | core trait definition | “ATP is produced by substrate-level phosphorylation.” (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong definitional edge. | GO:0046034, METPO:1000804 |
| phosphoglycerate kinase (PGK) | catalyzes | 1,3-bisphosphoglycerate + ADP -> 3-phosphoglycerate + ATP | glycolytic payoff phase; SLP | “the high-energy phosphoryl group from carboxyl group of 1,3BPG is transferred to ADP to form ATP and 3-phosphoglycerate” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | Source is an excerpt from an unknown/unclear publication venue; curate as mechanistically plausible but uncertain. | EC:2.7.2.3, GO:0004618, CHEBI:11881 1,3-bisphospho-D-glycerate, CHEBI:58289 ADP, CHEBI:15422 ATP, CHEBI:11801 3-phospho-D-glycerate |
| pyruvate kinase (PYK) | catalyzes | phosphoenolpyruvate + ADP -> pyruvate + ATP | glycolytic payoff phase; SLP | “the phosphoryl group of PEP is transferred to ADP via pyruvate kinase catalysis to yield pyruvate” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | Source venue unclear; mechanistic edge is standard biochemistry but excerpt-based here. | EC:2.7.1.40, GO:0004743, CHEBI:18021 phosphoenolpyruvate, CHEBI:58289 ADP, CHEBI:15361 pyruvate, CHEBI:15422 ATP |
| phosphotransacetylase (PTA/Pta) | catalyzes | acetyl-CoA -> acetyl-phosphate | acetate-formation branch; SLP-associated | “The formation of acetate… begins with phosphorylation of the latter via phosphate acetyltransferase to yield acetyl-P.” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | Enzyme name explicit only in excerpt; treat as uncertain until primary peer-reviewed source is added. | EC:2.3.1.8, GO:0008808, CHEBI:15351 acetyl-CoA, CHEBI:15344 acetyl phosphate |
| acetate kinase (ACK/AckA) | catalyzes | acetyl-phosphate + ADP -> acetate + ATP | acetate-formation branch; SLP | “The acetyl-P is then converted in an ADP dependent reaction to form acetate and ATP.” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | AckA enzyme name is implied by pathway and named in Hosmer review, but the exact catalytic sentence is from excerpt; moderate confidence. | EC:2.7.2.1, GO:0008878, CHEBI:15344 acetyl phosphate, CHEBI:58289 ADP, CHEBI:30089 acetate, CHEBI:15422 ATP |
| AckA-Pta pathway | allows ATP production via | substrate-level phosphorylation | acetate metabolism | “AckA-Pta, a set of reactions that allows ATP production via substrate-level phosphorylation” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Strong review support for pathway-level edge. | GO:0046034, EC:2.3.1.8, EC:2.7.2.1, MetaCyc:PTA-ACK-PWY (label candidate) |
| phosphotransbutyrylase (PTB) | catalyzes | butyryl-CoA -> butyryl-phosphate | butyrate-formation branch | “production of butyrate phosphate via phosphotransbutyrylase” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | Excerpt-only support; venue unclear. | EC:2.3.1.19, CHEBI:15525 butyryl-CoA, CHEBI: not found/label candidate butyryl-phosphate |
| butyrate kinase (BUK) | catalyzes | butyryl-phosphate + ADP -> butyrate + ATP | butyrate-formation branch; SLP | “subsequently converted to butyrate through butyrate kinase” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | ATP formation is inferred from canonical BUK reaction; excerpt gives enzyme/pathway but not full stoichiometry. Mark uncertain. | EC:2.7.2.7, CHEBI:50477 butyrate, CHEBI:58289 ADP, CHEBI:15422 ATP |
| butyrate/acetate branches from acetyl-CoA | contribute substantially to | SLP-derived ATP in mixed culture fermentation | mixed-culture fermentation | “responsible for about half the SLP in an EMP system” (chowdhary2023effectofsubstrate pages 17-21) | Chowdhary 2023 excerpt, 2023, URL not available in provided evidence | Quantitative claim from excerpt; useful but should be validated in a citable peer-reviewed source before hard curation. | KEGG:map00650 (butanoate metabolism), KEGG:map00620 (pyruvate metabolism) |
| succinyl-CoA:acetate CoA-transferase + succinyl-CoA synthetase [ADP-forming] | forms functional pathway for | acetate formation from acetyl-CoA-linked metabolism | alternative acetate-forming pathway | “were found to be active and form a functional pathway for forming acetate” (hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong review summary, but pathway described for specific taxa; mark taxon-specific if curated as direct mechanistic route. | EC:2.8.3.18, EC:6.2.1.5, CHEBI:30089 acetate, KEGG/MetaCyc label candidate: succinyl-CoA:acetate CoA-transferase/SCS acetate pathway |
| acetate—CoA ligase [ADP-forming] | catalyzes | acetate formation from acetyl-CoA | alternative acetate-forming pathway | “acetate was found to be formed from acetyl-CoA by one enzyme (acetate—CoA ligase [ADP-forming]; EC 6.2.1.13)” (hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong but taxon-specific (e.g., Chloroflexus aurantiacus) pathway. | EC:6.2.1.13, CHEBI:30089 acetate |
| AbrB | positively regulates transcription of | pgk | growth-phase regulation of SLP genes | “the transcription levels of genes pgk and pyk… were significantly reduced to 0.49 and 0.41” in abrB deletion strain; “AbrB positively regulated… substrate level phosphorylation (pyk and pgk)” (zhang2024understandingenergyfluctuation pages 4-6, zhang2024understandingenergyfluctuation pages 10-12) | 10.1186/s12934-024-02572-1, 2024, https://doi.org/10.1186/s12934-024-02572-1 | Directly supported in Bacillus licheniformis; taxon-specific regulatory edge. | NCBITaxon:1402 Bacillus licheniformis, pgk (label), GO:0006355 regulation of transcription |
| AbrB | positively regulates transcription of | pyk | growth-phase regulation of SLP genes | “the transcription levels of genes pgk and pyk… were significantly reduced to 0.49 and 0.41” (zhang2024understandingenergyfluctuation pages 4-6) | 10.1186/s12934-024-02572-1, 2024, https://doi.org/10.1186/s12934-024-02572-1 | Direct in B. licheniformis; taxon-specific. | NCBITaxon:1402, pyk (label), GO:0006355 |
| AbrB | binds promoter of | pgk | direct regulation of SLP genes | “AbrB binds the promoters of pgk and pyk” (zhang2024understandingenergyfluctuation pages 6-7) | 10.1186/s12934-024-02572-1, 2024, https://doi.org/10.1186/s12934-024-02572-1 | Strong direct-binding evidence from EMSA in B. licheniformis. | NCBITaxon:1402, pgk (label), GO:0000976 transcription regulatory region sequence-specific DNA binding |
| AbrB | binds promoter of | pyk | direct regulation of SLP genes | “AbrB binds the promoters of pgk and pyk” (zhang2024understandingenergyfluctuation pages 6-7) | 10.1186/s12934-024-02572-1, 2024, https://doi.org/10.1186/s12934-024-02572-1 | Strong direct-binding evidence from EMSA in B. licheniformis. | NCBITaxon:1402, pyk (label), GO:0000976 |
| AbrB deletion | decreases | intracellular ATP concentration | physiological consequence of SLP/energy regulation | “WX-02△abrB exhibited a significantly lower ATP concentration… decreased by 51.84%” (zhang2024understandingenergyfluctuation pages 4-6) | 10.1186/s12934-024-02572-1, 2024, https://doi.org/10.1186/s12934-024-02572-1 | Supports regulatory effect on energy metabolism, not SLP alone. | CHEBI:15422 ATP, NCBITaxon:1402 |
| glucose presence | causes catabolite repression of | acetate utilization | acetate assimilation/consumption | “its utilization can be subject to catabolite repression if glucose is present” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Strong review support; applies broadly, not universally. | CHEBI:17234 glucose, GO:0000016 lactate dehydrogenase? no; label candidate: catabolite repression of acetate utilization |
| RpoS | activates | acetate consumption during post-exponential growth | acetate assimilation/consumption regulation | “There is also evidence of RpoS-mediated activation of acetate consumption during post-exponential growth” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Regulatory edge from review; broad but likely taxon-dependent. | RpoS (label), GO:0006355, acetate consumption (label) |
| anaerobic/fermentative growth | upregulates expression of | ackA-pta | acetate-forming SLP route | “During anaerobic/fermentative growth, up-regulation of ackA-pta expression has been linked to the global anaerobic regulator Anr” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Strong review statement; observed in bacteria such as Pseudomonas spp. and Neisseria spp. | ackA (label), pta (label), ENVO:anaerobic environment (label) |
| Anr (Fnr homolog) | positively regulates expression of | ackA-pta | anaerobic regulation of acetate-forming SLP route | “up-regulation of ackA-pta expression has been linked to the global anaerobic regulator Anr” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Taxon-specific regulator (e.g., Pseudomonas/Neisseria context). | Anr/Fnr homolog (label), ackA (label), pta (label) |
| integration host factor subunit alpha (IhfA) | positively regulates expression of | ackA-pta | anaerobic regulation of acetate-forming SLP route | “up-regulation of ackA-pta expression has been linked to… integration host factor subunit alpha (lhfA)” (hosmer2023bacterialacetatemetabolism pages 1-3) | 10.1042/ETLS20220092, 2023, https://doi.org/10.1042/ETLS20220092 | Gene symbol appears as “lhfA” in excerpt; likely IHF alpha. Keep label cautious. | IHF alpha / ihfA (label), ackA (label), pta (label) |
| DMSO supplementation | increases | intracellular ATP level | acetogen energy conservation; alternative to SLP via IGP | “DMSO increases intracellular ATP levels 2-fold and reduces acetate production by half” (bae2024harnessingacetogenicbacteria pages 7-8) | 10.1039/d4cb00099d, 2024, https://doi.org/10.1039/d4cb00099d | Not an SLP edge; useful contrast/neighbor trait showing alternative ATP conservation. | CHEBI:16382 dimethyl sulfoxide, NCBITaxon:1515 Moorella thermoacetica |
| nitrate supplementation | increases | ATP/ADP ratio | acetogen energy conservation; alternative to SLP via electron sink/IGP | “The study also found a significant increase in the ATP/ADP ratio” (bae2024harnessingacetogenicbacteria pages 7-8) | 10.1039/d4cb00099d, 2024, https://doi.org/10.1039/d4cb00099d | Alternative to SLP; keep as neighboring mechanism, not core SLP edge. | CHEBI:17632 nitrate, CHEBI:15422 ATP, CHEBI:456216 ADP/ATP ratio (label) |
| nitrate supplementation | increases | growth and ethanol production in acetogens | application/performance consequence | “supplying nitrate improved its growth by up to 62% and ethanol production by up to 3-fold from CO2/H2” (bae2024harnessingacetogenicbacteria pages 7-8) | 10.1039/d4cb00099d, 2024, https://doi.org/10.1039/d4cb00099d | Bioprocess edge; context-specific to pH-controlled bioreactors and C. ljungdahlii. | NCBITaxon:329852 Clostridium ljungdahlii, CHEBI:16236 ethanol |
| carbamate kinase in arginine deiminase pathway | generates ATP via | substrate-level phosphorylation | noncanonical/additional SLP route in acetogens | “the carbamate kinase reaction… has been reported to be effective for ATP production in several acetogens” (bae2024harnessingacetogenicbacteria pages 7-8) | 10.1039/d4cb00099d, 2024, https://doi.org/10.1039/d4cb00099d | Useful candidate neighboring SLP module beyond glycolysis/acetate/butyrate; not requested core edge but supported. | EC:2.7.2.2, GO:0046034, arginine deiminase pathway (KEGG label) |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating the microbial trait substrate-level phosphorylation, including core pathway reactions, regulatory links, and nearby alternative ATP-conservation mechanisms. It is designed to support TraitMech YAML drafting while flagging taxon-specific or lower-confidence claims.*

### 5) Recent developments (prioritizing 2023–2024)

**(i) Fermentation/SLP diversity quantified at scale (2024):** Hackmann synthesizes large-scale curation showing **“over 1/4” of ~8,300 prokaryotes** are fermentative, with **55 end products** and **46 chemically-defined substrates**; acetate and lactate are most common products (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 2-3)

**(ii) Newly recognized acetate-forming enzymes that substitute “canonical” routes (2024):** Hackmann highlights discovery of acetate formation in *Cutibacterium granulosum* through **succinyl-CoA:acetate CoA-transferase (EC 2.8.3.18) plus succinyl-CoA synthetase [ADP-forming] (EC 6.2.1.5)**, with biochemical confirmation that these enzymes “form a functional pathway for forming acetate,” and also notes acetate formation via **acetate—CoA ligase [ADP-forming] (EC 6.2.1.13)** in *Chloroflexus aurantiacus* (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 4-5)

**(iii) Direct regulatory control of SLP genes (2024):** In *Bacillus licheniformis*, AbrB is shown to positively regulate SLP-related glycolytic genes **pgk** and **pyk**, with deletion reducing transcripts to 0.49 and 0.41 of WT and producing a strong ATP decrease (10.1186/s12934-024-02572-1; 2024-11). (zhang2024understandingenergyfluctuation pages 4-6)

**(iv) Industrially relevant “ATP-limited” acetogens and strategies (2024):** A 2024 RSC Chemical Biology review highlights that providing alternative terminal electron acceptors (e.g., **DMSO, nitrate**) can increase ATP availability and redirect carbon flow away from acetate; in *Moorella thermoacetica*, DMSO “increases intracellular ATP levels 2-fold and reduces acetate production by half,” while nitrate reduction is estimated to yield **~1.5 ATP vs ~0.63 ATP** for CO2/H2 acetogenesis and can increase growth and ethanol production under controlled conditions (10.1039/d4cb00099d; 2024-07). (bae2024harnessingacetogenicbacteria pages 7-8)

### 6) Current applications and real-world implementations

**Gut, sediments, anaerobic bioreactors:** Fermentative metabolism (where SLP is a central ATP mode) is described as a major microbial process in “the gut… sediments… and anaerobic bioreactors” (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 1-2)

**Biofuels and commodity chemicals:** The same review links fermentation products to societal uses including “biofuels and other commodity chemicals,” and emphasizes that applied outcomes could be improved by “genetic engineering, electrofermentation, probiotics, and enzyme inhibitors” (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 1-2)

**Host-relevant acetate as a fermentation/SLP-linked end product:** In human-associated ecosystems, acetate is the most abundant SCFA and is a major fermentation end product; intestinal SCFAs are 20–140 mM with acetate accounting for 60–75% (10.1042/etls20220092; version of record published 2023-03-22). (hosmer2023bacterialacetatemetabolism pages 1-3)

### 7) Expert opinions / authoritative analysis (what experts emphasize)

- **Definitions have evolved and edge cases matter:** Hackmann argues defining fermentation (and by extension the context in which SLP dominates) is “a surprisingly challenging exercise” and recommends a broader definition while leaving edge cases to investigators (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3)
- **Energy limitation is a key bottleneck in industrial acetogens:** The acetogen-focused review frames inadequate ATP/redox availability as limiting production of energy-demanding chemicals and emphasizes engineering or process strategies to increase ATP availability (10.1039/d4cb00099d; 2024-07). (bae2024harnessingacetogenicbacteria pages 7-8)

### 8) Relevant recent statistics and quantitative data

**Prevalence and diversity (prokaryotes):**
- Over **1/4** of ~**8,300** prokaryotes curated were fermentative (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 2-3)
- **55** fermentation end products and **46** chemically-defined substrates reported; nearly 300 product combinations observed (10.1093/femsre/fuae016; 2024-05-31). (hackmann2024thevastlandscape pages 2-3)

**Host/environment concentrations (acetate/SCFAs):**
- Intestinal SCFAs: **20–140 mM**, acetate **60–75%**; ~**36%** of colonic acetate becomes systemic (venous serum **50–200 μM**) (10.1042/etls20220092; 2023-03-22). (hosmer2023bacterialacetatemetabolism pages 1-3)

**Regulatory perturbation affecting ATP (direct measurement):**
- *B. licheniformis* AbrB deletion decreased ATP from **0.571 μM ATP/OD600** to **0.275 μM ATP/OD600** (−**51.84%**), and increased generation time (10.1186/s12934-024-02572-1; 2024-11). (zhang2024understandingenergyfluctuation pages 4-6)

**Process/bioprocess interventions affecting ATP (acetogens):**
- DMSO increased intracellular ATP **2-fold** and halved acetate production in *M. thermoacetica* (10.1039/d4cb00099d; 2024-07). (bae2024harnessingacetogenicbacteria pages 7-8)
- Nitrate reduction estimated to yield **1.5 ATP** vs **0.63 ATP** for CO2/H2 acetogenesis; nitrate supplementation improved growth by up to **62%** and ethanol by up to **3-fold** in one study context (10.1039/d4cb00099d; 2024-07). (bae2024harnessingacetogenicbacteria pages 7-8)

### 9) Ontology grounding suggestions (high-priority)

- **Trait:** METPO:1000804 (given)
- **SLP process container:** GO:0046034 (ATP metabolic process; use as broad process node if needed) (hackmann2024thevastlandscape pages 1-2)
- **Key enzyme nodes:** EC:2.7.2.1 (AckA), EC:2.3.1.8 (Pta), EC:2.8.3.18 (succinyl-CoA:acetate CoA-transferase), EC:6.2.1.5 (succinyl-CoA synthetase [ADP-forming]), EC:6.2.1.13 (acetate—CoA ligase [ADP-forming]) (hackmann2024thevastlandscape pages 4-5, hosmer2023bacterialacetatemetabolism pages 1-3)
- **Environment:** ENVO label candidate for anaerobic environment (hackmann2024thevastlandscape pages 1-2)
- **Chemicals:** CHEBI:15422 (ATP), CHEBI:58289 (ADP), CHEBI:30089 (acetate), CHEBI:16382 (DMSO), CHEBI:17632 (nitrate) (hosmer2023bacterialacetatemetabolism pages 1-3, bae2024harnessingacetogenicbacteria pages 7-8)

### 10) Warnings / “do not curate yet” items

1. **PGK/PYK/PTA/ACK/PTB/BUK reaction-level edges:** In the current evidence pack, the explicit reaction descriptions for PGK and PYK and the acetate/butyrate branch step descriptions are primarily supported by a text excerpt with unclear venue/peer-review status (chowdhary2023effectofsubstrate pages 17-21). These edges are biochemically standard but should ideally be backed by a citable peer-reviewed review/primary source before being promoted from “candidate/uncertain” to “curation-ready.”

2. **Broad generalization of regulators across taxa:** Regulatory edges such as Anr(Fnr homolog)→ackA-pta and RpoS→acetate consumption come from a mini-review and are likely context/taxon dependent; they should be represented with taxon or clade constraints when possible (hosmer2023bacterialacetatemetabolism pages 1-3).

3. **Equating fermentation with exclusive SLP:** Hackmann explicitly notes some fermenters can generate a substantial fraction of ATP via ETC/ATP synthase (up to 1/3), so SLP trait assertions should not automatically imply absence of respiratory contributions (hackmann2024thevastlandscape pages 2-3).

---

## DOI-first bibliography (recent prioritized)

1. **Hackmann TJ.** *The vast landscape of carbohydrate fermentation in prokaryotes.* **FEMS Microbiology Reviews**. Advance access publication date **2024-05-31**. DOI: **10.1093/femsre/fuae016**. URL: https://doi.org/10.1093/femsre/fuae016 (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 4-5)

2. **Hosmer J, McEwan AG, Kappler U.** *Bacterial acetate metabolism and its influence on human epithelia.* **Emerging Topics in Life Sciences**. Version of record published **2023-03-22**. DOI: **10.1042/etls20220092**. URL: https://doi.org/10.1042/etls20220092 (hosmer2023bacterialacetatemetabolism pages 1-3)

3. **Zhang Q, Zhu W, He S, et al.** *Understanding energy fluctuation during the transition state: The role of AbrB in Bacillus licheniformis.* **Microbial Cell Factories**. **2024-11**. DOI: **10.1186/s12934-024-02572-1**. URL: https://doi.org/10.1186/s12934-024-02572-1 (zhang2024understandingenergyfluctuation pages 4-6)

4. **Bae J, Park C, Jung H, Jin S, Cho B-K.** *Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.* **RSC Chemical Biology**. **2024-07**. DOI: **10.1039/d4cb00099d**. URL: https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 7-8)

5. **Chowdhary K.** *Effect of Substrate Concentration & Elevated CO2 Partial Pressure on the Odd & Even Carboxylate Formation.* **2023**. (Venue/URL unclear in retrieved excerpt; treat as non-authoritative until verified.) (chowdhary2023effectofsubstrate pages 17-21)


References

1. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

2. (hackmann2024thevastlandscape pages 2-3): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (chowdhary2023effectofsubstrate pages 17-21): K Chowdhary. Effect of substrate concentration & elevated co2 partial pressure on the odd & even carboxylate formation. Unknown journal, 2023.

4. (hosmer2023bacterialacetatemetabolism pages 1-3): Jennifer Hosmer, A. McEwan, and U. Kappler. Bacterial acetate metabolism and its influence on human epithelia. Emerging Topics in Life Sciences, 8:1-13, Mar 2023. URL: https://doi.org/10.1042/etls20220092, doi:10.1042/etls20220092. This article has 106 citations.

5. (hackmann2024thevastlandscape pages 4-5): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

6. (bae2024harnessingacetogenicbacteria pages 7-8): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

7. (zhang2024understandingenergyfluctuation pages 4-6): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 5 citations and is from a peer-reviewed journal.

8. (zhang2024understandingenergyfluctuation pages 10-12): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 5 citations and is from a peer-reviewed journal.

9. (zhang2024understandingenergyfluctuation pages 6-7): Qing Zhang, Wanying Zhu, Shisi He, Jiaqi Lei, Liangsheng Xu, Shiying Hu, Zheng Zhang, Dongbo Cai, and Shouwen Chen. Understanding energy fluctuation during the transition state: the role of abrb in bacillus licheniformis. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02572-1, doi:10.1186/s12934-024-02572-1. This article has 5 citations and is from a peer-reviewed journal.